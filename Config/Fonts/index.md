---
layout : wiki
title : Fonts
type : config
weight : 750
description : |
  Fonts are used for titles, icon names, menus, modules, etc.
  Here is a brief description on how to configure fonts.

---

# Fonts

Fonts are controled on an object by object basis in FVWM. You can set a different font
for your title bars, menus, modules, etc. FVWM supports both X Logical Font
Description (XLFD) and XFT font descriptions. In most cases you will want to
use the XFT font descriptions (`fvwm --version` to check for XFT support).
The following will set the DefaultFont used by FVWM and shows and example of
the XFT font syntax.


{% highlight fvwm %}
DefaultFont "xft:Sans:Bold:size=8:antialias=True"
{% endhighlight %}

The Syntax is xft to tell Fvwm to use XFT fonts, the name of the font, followed
by some options all separated by ":". See the [manpage](
http://fvwm.org/documentation/manpages/fvwm.html#lbAY) for a more detailed
description.

Fonts can be set for the title bar, menus, modules, and so on. Each of these
items has its own configuration setting but will use the same syntax for
the font string as in the above example.

