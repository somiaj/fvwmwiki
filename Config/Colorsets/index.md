---
layout : wiki
title : Colorsets
type : config
weight : 800
description : |
  Colorsets are used to define colors in Fvwm. A Colorset is a collection
  of colors that describe different aspects of an object. This includes
  the foreground and background color along with the shade and highlight
  color (for 3D relief on borders). Colorsets can also use pixmaps
  and be transparent.

---
* TOC
{:toc}

# Colorsets

A Colorset is a collection of colors: foreground (fg), background (bg), hilight (hi),
and shade (sh). The foreground is the color of the text, background is the color
behind the text, and the hilight and shade are used to give a 3D beveled effect around
the border. This causes a raised or sunk look, like a button. Besides just setting
the color, Colorsets can use pixmaps, gradients, shape masks and be pseudo-transparent.

## Basic Syntax

Colorsets are identified by a number zero or greater. You can use a very large number
of Colorsets but should keep the numbers small -- FVWM will use memory for
__all__ Colorsets up to the maximum number used. 

For example, define Colorset 2 with a white foreground (fg) and black background (bg)
as follows:

{% highlight fvwm %}
Colorset 2 fg #ffffff, bg #000000
{% endhighlight %}

In the case no hilight (hi) and shade (sh) are set, fvwm will generate
them when they are being used for the 3D raise/sunk looks. You can set the
hi and sh color if you want more control of the beveled look. If you
set them to be the same color, this will give a solid border.

The color in this example are defined using the hex syntax for colors
in the form #rrggbb where rr, bb, gg are the values for red, green
and blue between 00 and ff (in hexadecimal). 

In addition to this format you can also use rgb:rr/gg/bb or color names
such as

{% highlight fvwm %}
Colorset 2 fg white, bg black
Colorset 3 fg rgb:ff/ff/ff, bg rgb:00/00/00
{% endhighlight %}

Color names are used using rgb.txt from X (/etc/X11/rgb.txt).

When changing Colorsets inside a running instance of Fvwm (such as
switching themes), you may have to deal with any previous definitions
used. One way is to use CleanupColorsets to reset all the colorsets.

Another is to include additional options to force the defaults. For
example

{% highlight fvwm %}
Colorset 2 fg #ffffff, bg #000000, hi, sh, fgsh, Plain, NoShape, Tint, Alpha
{% endhighlight %}

This will do almost the exact same thing as the first example without these
additional options. The difference is this example removed any previous definitions
of the colorsets including pixmaps, shape masks, tint and alpha settings.

Unless you are regularly changing your Colorsets there is no need for the additional
options.  So if you see a Colorset example with these additional options,
they are just there to ensure the default behavior.


## Number Convention

One can use any numbering convention for the Colorsets that fits your configs deisgn.
If you don't want to create one of your own, here is the one used in the default
config.

{% highlight fvwm %}
######
# 3: Colorsets
#
#   0 - Default
#   1 - Inactive Windows
#   2 - Active Window
#   3 - Inactive Windows Borders
#   4 - Active Windows Borders
#   5 - Menu - Inactive Item
#   6 - Menu - Active Item
#   7 - Menu - Grayed Item
#   8 - Menu - Title
#  10+ Modules
###########
Colorset 0  fg #ffffff, bg #003c3c
Colorset 1  fg #000000, bg #8f9f8f
Colorset 2  fg #ffffff, bg #003c3c
Colorset 3  fg black, bg #4d4d4d, hi #676767, sh #303030
Colorset 4  fg black, bg #2d2d2d, hi #474747, sh #101010
Colorset 5  fg #000000, bg #ffffff
Colorset 6  fg #ffffff, bg #2d2d2d
Colorset 7  fg grey30, bg #ffffff
Colorset 8  fg #ffffff, bg #003c3c
{% endhighlight %}

## Color Themes

Here are two Colorset collections taken from fvwm-themes. These Colorset
definitions all use the above convention and define Colorsets 0 through 8.

+ [CdeColors](CdeColors.tar.gz) contains 41 colors themes with names such
  as Alpine, Arizona, Charcoal, Neptune, etc...
+ [LuthienColors](LuthienColors.tar.gz) contains 33 color themes with names
  such as Africa, Cocoa, Ocean, Prisim, etc...

These two collections contain a lot of files Name.fvwm2rc which is just a
list of the Colorset definitions 0 though 8. You can copy the Colorset
definitions into your config or create a menu which lets you switch
between the color themes.

To do this extract each of the above collections into $FVWM_USERDIR ($HOME/.fvwm).
Then to build a menu for CdeColors/* use the following

{% highlight fvwm %}
DestroyMenu CdeColorMenu
AddToMenu CdeColorMenu "Cde Colors" Title
PipeRead 'for i in $[FVWM_USERDIR]/CdeColors/*.fvwm2rc; do \
  echo "AddToMenu CdeColorMenu $(basename -s .fvwm2rc $i) Read $i"; done'
{% endhighlight %}

This menu will Read the file that contains the Colorset definitions when
selected and give you a way to switch between the color themes.

Once CdeColorMenu is built you can open it with Menu CdeColorMenu or add it to your
current menus as a submenu with Popup. See [/Config/Menus](
{{ "/Config/Menus" | prepend: site.baseurl }}).

Using these Colorsets themes works best with a decor setup that relies on Colorsets
over images such as [/Decor/CDE]({{ "/Decor/CDE" | prepend: site.baseurl }}).

## Additional Options

Besides just Colors, Colorsets have settings for the background image
created in Menus, TitleBars and Modules. Instead of just using straight
colors, pixmaps, graidents, and even tinting, blending and pseudo-transparent
effects are available.

+ fgsh for the font shadow effect.
+ Pixmap, TiledPixMap, AspectPixmap to use Pixmaps as the background.
+ Transparent, RootTransparent to use an image of the root window as
  the background for a transparent feel.
  This is only a pseudo-transparent effect. For a full transparent
  affect you will need a third party tool like Xcompmgr.
+ ?Graident to create various types of Gradients as backgrounds.
+ Tint, Alpha, IconTint, IconAlpha - Tint or blend the background or icon.
+ Shape, TiledShape, AspectShape - Set a shape mask (can be used to make rounded
  corners on FvwmButtons).

All the details about these options can be found in the [manpage](
http://fvwm.org/documentation/manpages/fvwm.html#lbCB). 


