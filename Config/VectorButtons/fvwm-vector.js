/*
 A Simple FVWM Vector Buttons Viewer.

 MIT Licensed.  Original author Alex Gromnitsky.

 TODO:

 - user-customizable colors.
 
*/

// Globals
var cfg = {};
cfg.version = "0.11";
cfg.verbose = 2;
cfg.author = 'Alexander Gromnitsky &lt;alexander.gromnitsky.at.gmail.com&gt;';
cfg.licence = 'http://www.opensource.org/licenses/mit-license.php';
cfg.zoom = 2;

/**
 * @addon
 */
String.prototype.trim = function() {
	return this.replace(/^\s+|\s+$/g, "");
};

/*
 -----------
 Utils Class
 -----------
*/

/**
 * @param err  an id of some html text element, where we can
 *             white errors for users
 * @param log  an id of a textarea
 * 
 * @constructor
 */
function Utils(err) {
	this.el_err = err;
}

Utils.log = function(msg) {
	if (typeof console == "undefined") return;
	console.log(new Date().toLocaleTimeString() + '> ' + msg);
};

Utils.veputs = function(level, msg) {
	if (cfg.verbose >= level) Utils.log(msg);
};

Utils.prototype.errx = function(msg) {
	var e;
	if (!(e = document.getElementById(this.el_err)) ) return;
	e.innerHTML = "<span class='error'><b>Error:</b> " + msg + '</span>';
	Utils.log('Error: '+msg);
};

Utils.prototype.get_element_byid = function(id) {
	var e;
	if (!(e = document.getElementById(id)) ) {
		this.errx('cannot locale \"'+id+'\" element--check HTML generation.');
		return null;
	}
	return e;
};

Utils.hide_id = function(e, really) {
	if (!(e = document.getElementById(e)) ) return;

	if (really) e.style.display = "none";
	else e.style.display = "";
};

Utils.select_get = function(e) {
	return e.options[e.selectedIndex].value;
}


/*
 --------------
 MyCanvas Class
 --------------
*/

/**
 * @param {Number} scale 
 * @see @Fvwm#zoom
 * @see @Fvwm#draw
 * 
 * @constructor
 */
function MyCanvas(scale) {
	this.utils = new Utils("result_src");
	this.scale = scale;
	this.canvas = null;
	this.ctx = null;
	this.is_grid = false;
	this.empty = true;
	this.uptodate = false;
}

MyCanvas.WIDTH = 100;
MyCanvas.HEIGHT = 100;

/**
 * @returns current physical width of the canvas in pixels
 */
MyCanvas.prototype.pwidth = function() {
	if (this.scale == 1) return MyCanvas.WIDTH;
	return MyCanvas.WIDTH * this.scale;
};

/**
 * @returns current physical height of the canvas in pixels
 */
MyCanvas.prototype.pheight = function() {
	if (this.scale == 1) return MyCanvas.HEIGHT;
	return MyCanvas.HEIGHT * this.scale;
};

/**
 * Attach MyCanvas object to a particular canvas.
 * 
 * @param e  an id of canvas
 */
MyCanvas.prototype.attach = function(e) {
	this.canvas = this.utils.get_element_byid(e);
	if (this.canvas.getContext) {
		this.ctx = this.canvas.getContext('2d');
		return this.canvas;
	} else {
		this.utils.errx("sorry dude, your browser doesn't support &lt;canvas&gt; element");
	}
	return null;
};

/**
 * Clear the whole canvas to start drawing again form scratch.
 */
MyCanvas.prototype.clear = function() {
	if (!this.ctx) return;
	this.ctx.clearRect(0, 0, this.pwidth(), this.pheight());
	this.empty = true;
};

/**
 * Convert from FVWM vector buttons colors to out actual colors.
 * 
 * @param {Number} c  a digit [0-4]
 * @returns null if c is invalid
 */
MyCanvas.get_color = function(c) {
	switch (c) {
	case 0:
		return "#555555"; // shadow, between gray33 and gray34
	case 1:
		return "#ababab"; // highlight, gray67
	case 2:
		return "#999999"; // foreground, gray60
	case 3:
		return "black"; // background
	default:
		return null;
	}
};

/*
 ----------
 Fvwm Class
 ----------
*/

/**
 * @constructor
 */
function Fvwm() {
	this.utils = new Utils("result_src");
	this.cn = new MyCanvas(cfg.zoom);
	this.input_type = 'strict';
}

/**
 * Put our html form on the page.
 */
Fvwm.prototype.populate = function () {
	document.write("<p>\n" +
				   "<form name='edit_source'>\n" +
				   "<input type='button' value='Draw' accesskey='d' onclick='fvwm.draw();' />\n" +
				   "<input type='button' value='Clear' onclick='fvwm.clear();' />\n" +
				   " Zoom: <select id='zoom' onchange='fvwm.zoom();'>\n"+
				   "<option>30%</option>\n"+
				   "<option>50%</option>\n" +
				   "<option>80%</option>\n" +
				   "<option>100%</option>\n" +
				   "<option selected>200%</option>\n" +
				   "<option>300%</option>\n" +
				   "<option>400%</option>\n"+
				   "</select>\n"+
				   " Input mode:\n" +
				   "<input type='radio' name='variant' value='strict' checked onclick='fvwm.convert();' />strict\n" +
				   "<input type='radio' name='variant' value='light' onclick='fvwm.convert();' />light\n" +
				   "&nbsp;&nbsp;&nbsp;&nbsp;\n"+
				   "<input type='button' value='Help' onclick='fvwm.help();' />\n" +
				   "<br />\n" +
				   "<textarea name='src' id='src' onchange='fvwm.canvas_border(false);' accesskey='i' rows='3' cols='80'>"+
				   "Vector 7 70-1px15-1p@0 30x55@1 50x55@0 40x85@1 80x45@0 60x45@1 70x15@0\n"+
				   "</textarea>\n" +
				   "</form>\n" +
				   "</p>\n"
		);

	// axes
	document.write("<img src='x.png' alt='X' /><br />\n"+
				   "<img src='y.png' alt='Y' />\n\n");

	document.write("<canvas id='viewer' width='"+this.cn.pwidth()+
				   "' height='"+this.cn.pheight()+"'></canvas>\n\n");

	// result for .fvwm2rc
//        document.write("<div id='result_box'>\n<p>For .fvwm2rc:<br /></p>\n" +
//                                   "<p id='result_src'></p>\n" +
//                                   "</div>\n\n");
	document.write("<div id='result_box'><br>" +
				   "<p id='result_src'></p>\n" +
				   "</div>\n\n");

	this.cn.attach('viewer');
	Utils.hide_id('result_box', true);

//	document.write("<hr />\nVersion " + cfg.version + ".<br />\n" +
//				   "Copyright (C) 2010 " + cfg.author +
//				   ". License: <a  href='"+cfg.licence+"'>MIT</a>.\n");

	// in textarea, ctrl+enter is equal to mouse clink on "Draw" button
	document.edit_source.src.onkeyup = function(e) {
		e = e || event;
		if (e.keyCode === 13 && e.ctrlKey) fvwm.draw();
		return true;
	};
};

/**
 * @returns either "strict" or "light"
 */
Fvwm.prototype.get_input_type = function() {
	var e = document.edit_source.variant[0];
	if (!e || e.checked) return "strict";
	else return "light";
};

/**
 * Converts something like '300%' to a number used somehow for scaling.
 * @see #zoom
 */
Fvwm.zoom2scale = function(z) {
	var n = z.match(/\d+/);
	if (!n) return cfg.zoom;
	return n/100;
};

/**
 * Mark a canvas border with red/blue colors depending to valur of
 * is_uptodate parameter.
 * 
 * @param {Boolean} is_uptodate  if it is true the border will be blue
 */
Fvwm.prototype.canvas_border = function(is_uptodate) {
	this.cn.uptodate = false;
	if (is_uptodate) this.cn.uptodate = true;
			
	var e = this.utils.get_element_byid('viewer');
	if (!e) return;
	if (this.cn.uptodate) e.style.border = '1px solid blue';
	else e.style.border = '1px solid red';
};

/**
 * Zoom the canvas. The image on it after zooming redraws automatically.
 */
Fvwm.prototype.zoom = function() {
	var empty = true;
	if (!this.cn.empty) empty = false; // we may need to redraw the button

	// get zoom value
	var e = this.utils.get_element_byid('zoom');
	if (e) Utils.veputs(1, "zoom by " + Utils.select_get(e) +
						', scale=' + Fvwm.zoom2scale(Utils.select_get(e)));
	else return;
	
	// delete old MyCanvas object, create a new one,
	// resize the <canvas> element
	delete this.cn;
	this.cn = new MyCanvas(Fvwm.zoom2scale(Utils.select_get(e)));
	var el = this.cn.attach('viewer');
	el.setAttribute("width", this.cn.pwidth());
    el.setAttribute("height", this.cn.pheight());
	Utils.veputs(1, "new canvas size: "+this.cn.pwidth() +
				 "x"+ this.cn.pheight());

	if (!empty) this.draw();
};

/**
 * Open a new window with a stale text.
 */
Fvwm.prototype.help = function() {
	window.open("help.html", "Help_for_a_FVWM_buttons_viewer",
				"width=500,height=450");
};

/**
 * Clear the canvas and the textarea.
 */
Fvwm.prototype.clear = function() {
	// clean the canvas
	this.cn.clear();
	Utils.hide_id('result_box', true);

	// clean textarea
	var e = this.utils.get_element_byid('src');
	if (e) e.value = "";
};

/**
 * If #draw was succsesful, this method shows to the user a string which
 * can be inserted directly to .fvwm2rc file.
 * 
 * @param {Vector} v  the result from Vector.parse_* functions.
 */
Fvwm.prototype.result_print = function(v) {
	var e = this.utils.get_element_byid('result_src');
	if (!e) return;

	var s = "Vector " + v.buttons.length;
	for (i in v.buttons) {
		s += ' ' + v.buttons[i];
	}
	e.innerHTML = s;
};

/**
 * Convert text in textarea between strict and light types.
 */
Fvwm.prototype.convert = function() {
	var itype = this.get_input_type();
	if (itype == this.input_type)
		return;					// do nothing
	else 
		Utils.veputs(1, "converting from "+this.input_type+" to "+itype);
	
	this.input_type = itype;
	
	var v = new Vector(this.utils.get_element_byid('src').value);
	if (!v) return;
	try {
		itype == 'strict' ? v.parse_light() : v.parse_strict();
	} catch (e) {
		this.utils.errx('cannot parse: ' + e.message);
		// If you select "light" radiobox and hit reload in firefox
		// 3.6.x, it for the unknown reason remembers that radio selection.
		// 
		// This means that the default radio in out script would be "strict"
		// but for the user it is not.
		
		// Use Chrome or Opera.
		return;
	}
	
	var e = this.utils.get_element_byid('src');
	if (!e) return;
	var s = '';
	if (itype == 'strict') {	// target
		s = "Vector " + v.buttons.length;
		for (i in v.buttons) {
			s += ' ' + v.buttons[i];
		}
	} else {
		for (i in v.buttons) {
			s += v.buttons[i].x + (v.buttons[i].xoff != 0 ?
								   Point.i2s(v.buttons[i].xoff) : "") +
			' ' + v.buttons[i].y + (v.buttons[i].yoff != 0 ?
									Point.i2s(v.buttons[i].yoff) : "") +
			' ' + v.buttons[i].color + ', ';
		}
	}
	
	e.value = s;
};

/**
 * Main pain in the ass.
 */
Fvwm.prototype.draw = function() {
	Utils.hide_id('result_box', false);

	var itype = this.get_input_type();
	Utils.veputs(2, 'input: ' + itype);

	var v = new Vector(this.utils.get_element_byid('src').value);
	if (!v) return;
	try {
		itype == 'strict' ? v.parse_strict() : v.parse_light();
	} catch (e) {
		this.utils.errx('cannot parse: ' + e.message);
		return;
	}

	this.cn.clear();

	var cor = this.cn.scale;	// correction
	var ocor = cor < 1 ? 1 : cor;
	Utils.veputs(1, "offset correction="+ocor);
	this.cn.ctx.beginPath();
	this.cn.ctx.moveTo(v.buttons[0].x * cor + v.buttons[0].xoff * ocor,
					   v.buttons[0].y * cor + v.buttons[0].yoff * ocor);
	var f = 1;
	for (i in v.buttons) {
		if (!f) {
			f = 1;
			continue;
		}

		var color = MyCanvas.get_color(v.buttons[i].color);
		if (color) {
			this.cn.ctx.strokeStyle = color;
			this.cn.ctx.lineTo(v.buttons[i].x * cor + v.buttons[i].xoff * ocor,
							   v.buttons[i].y * cor + v.buttons[i].yoff * ocor);
			this.cn.ctx.stroke();

			this.cn.ctx.beginPath();
			this.cn.ctx.moveTo(v.buttons[i].x * cor + v.buttons[i].xoff * ocor,
							   v.buttons[i].y * cor + v.buttons[i].yoff * ocor);
		} else {
			// only move to the point
			this.cn.ctx.moveTo(v.buttons[i].x * cor + v.buttons[i].xoff * ocor,
							   v.buttons[i].y * cor + v.buttons[i].yoff * ocor);
		}
	}

	this.result_print(v);
	this.cn.empty = false;
	this.canvas_border(true);
};

/*
 -----------
 Point Class
 -----------
*/

/**
 * @constructor
 */
function Point() {
	this.x = -1;
	this.y = -1;
	this.xoff = 0;
	this.yoff = 0;
	this.color = 0;
}

Point.prototype.toString = function() {
	return this.x + (this.xoff != 0 ? Point.i2s(this.xoff) + 'p' : "") +
	"x" + this.y + (this.yoff != 0 ? Point.i2s(this.yoff) + 'p' : "") +
	"@" + this.color;
};

/**
 * If x is out of range 0 will be used.
 */
Point.prototype.setx = function(x) {
	this.x = x >= 0 && x <= 100 ? x : 0;
};

/**
 * If x is out of range 0 will be used.
 */
Point.prototype.sety = function(y) {
	this.y = y >= 0 && y <= 100 ? y : 0;
};

Point.i2s = function(n) {
	return n>0 ? '+' + n.toString() : n.toString();
}

/**
 * Assign FVWM vector bottons color to a point.
 * 
 * @param {Number} c  a digit [0-4].
 *                    0 - the shadow;
 *                    1 - the highlight;
 *                    2 - the background;
 *                    3 - the foreground color;
 *                    4 - only move the point, do not draw.
 */
Point.prototype.set_color = function(c) {
	this.color = c >= 0 && c <= 4 ? c : 0;
};

/*
 ------------
 Vector Class
 ------------
*/

/**
 * @param {String} src  a raw FVWM vector button specification string.
 * 
 * @constructor
 */
function Vector(src) {
	this.src = src;
	this.buttons = new Array(); // of Point
}

Vector.LIMIT = 10000;			// we can use up to this number of points
Vector.POINT = /[x@]/;
Vector.POINT_LIGHT = /\s+/;

/**
 * @returns null on error or a Point object
 */
Vector.create_point = function(s, re) {
	var t = s.split(re);
	if (t.length != 3) return null;

	// get color
	var b = new Point();
	b.color = parseInt(t[2]);
	
	var get_coord = function(s) {
		var r = [-1, 0];
		if (s.match(/^\d+$/)) r[0] = parseInt(s);
		else {
			// we have an offset
			var co = s.match(/(\d+)([-+]\d+)p?/);
			if (!co) return null;
			r[0] = parseInt(co[1]);
			r[1] = parseInt(co[2]);
		}
		return r;
		
	};
	
	// get x & y
	var r;
	if ( !(r = get_coord(t[0])) ) return null;
	else {
		b.setx(r[0]);
		b.xoff = r[1];
	}
	if ( !(r = get_coord(t[1])) ) return null;
	else {
		b.sety(r[0]);
		b.yoff = r[1];
	}
	return b;
};
	
/**
 * @throws {Error} if parsing has failed
 */
Vector.prototype.parse_strict = function() {
	var a = this.src.split(/\s+/);
	Utils.veputs(2, 'array to parse ('+a.length+'): '+a);
	if (a.length <= 1) throw new Error("nothing to parse");

	var nonpoint = 1;
	var limit = Vector.LIMIT;
	var but = [];
	for (i in a) {
		if (nonpoint) {			// set possible limit
			var r;
			if ( (r = a[i].match(/^\d+$/)) && r >= 2 && r <=  Vector.LIMIT) {
				limit = r;
				continue;
			}
		}

		if (limit == 0) break;
		var b = Vector.create_point(a[i], Vector.POINT);
		if (b) {
			but.push(b);
			nonpoint = 0;
			--limit;
		}
	}

	if (but.length < 2) throw new Error("invalid input");

	this.buttons = but;
	Utils.veputs(1, 'to draw: '+this.buttons);
};

/**
 * @throws {Error} if parsing has failed
 */
Vector.prototype.parse_light = function() {
	var a = this.src.split(',');
	Utils.veputs(2, 'array to parse ('+a.length+'): '+a);
	if (a.length <= 1) throw new Error("nothing to parse");

	var limit = Vector.LIMIT;
	var but = [];
	for (i in a) {
		if (limit == 0) break;
		var b = Vector.create_point(a[i].trim(), Vector.POINT_LIGHT);
		if (b) {
			but.push(b);
			--limit;
		}
	}

	if (but.length < 2) throw new Error("invalid input");

	this.buttons = but;
	Utils.veputs(1, 'to draw: '+this.buttons);
};

