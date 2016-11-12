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
# Colorsets

A Colorset is a collection of colors: foreground, background, highlight, and shade.
The foreground is the color of the text, background is the color behind the text, and
the highlight and shade are used to give a 3D beveled effect around the border.
Besides just setting the color, Colorsets can use pixmaps, shape masks and be
transparent.

Colorsets are identified by a number zero or greater. You can use a very large number
of Colorsets but should keep the numbers small. FVWM will use memory for
all Colorsets up to the maximum number used.

Different aspects of Fvwm and Modules will have an option in which you can
set the Colorset used. Below are some example Colorsets and a convention of
what each colorset is used for from the default config.

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
#   9 - Reserved
#  10+ Modules
###########
Colorset 0  fg #ffffff, bg #003c3c, hi, sh, Plain, NoShape
Colorset 1  fg #000000, bg #8f9f8f, hi, sh, Plain, NoShape, IconAlpha 50
Colorset 2  fg #ffffff, bg #003c3c, hi, sh, Plain, NoShape
Colorset 3  fg black, bg #4d4d4d, hi #676767, sh #303030, Plain, NoShape
Colorset 4  fg black, bg #2d2d2d, hi #474747, sh #101010, Plain, NoShape
Colorset 5  fg #000000, bg #ffffff, hi, sh, Plain, NoShape
Colorset 6  fg #ffffff, bg #2d2d2d, hi, sh, Plain, NoShape
Colorset 7  fg grey30, bg #ffffff, hi, sh, Plain, NoShape
Colorset 8  fg #ffffff, bg #003c3c, hi, sh, Plain, NoShape
Colorset 10 fg #ffffff, bg #003c3c, hi #aaaaaa, sh #999999, Plain, NoShape
Colorset 11 fg #ffffff, bg #1a6e99, hi #ffffff, sh #ffffff, Plain, NoShape
Colorset 12 fg #2d2d2d, bg #ffffff, hi, sh, Plain, NoShape
Colorset 13 fg #ffffff, bg #006c6c, hi, sh, Plain, NoShape
{% endhighlight %}


Above sets the Colorsets. The main options are up to four different
colors where 'fg' is the foregound, 'bg' is the background, 'hi' is
the highlight and 'sh' is the shade. The highlight and shade color will
be generated from the background color if no color is given (or if it
is omitted from the colorset).

Additional options that can be used are PixMap, Transparent, Shape,
?Gradient, Tint, Alpha, IconTint, IconAlpha, and so on. For a full
description of these additional options see the [manpage](
http://fvwm.org/documentation/manpages/fvwm.html#lbCB).

The Plain and NoShape unset any Pixmap or Shape settings. In general
you won't need these options unless you are changing colorsets in
a running instance of Fvwm.


