---
layout : wiki
title : Settings and Styles
type : config
weight : 900
description : |
  Styles are per window settings that can be applied to all, different
  collections or a single window.

---

# Window Styles

Styles are options that can be applied to one, many or all windows.
Fvwm has hundreds of Styles, and this page is only going to describe
the syntax. See the [manpage](
http://fvwm.org/documentation/manpages/fvwm.html#lbBU) for a list
and description of all the different Styles.

The syntax for Styles is:

{% highlight fvwm %}
Style stylename Style1, Style2, Style3, ...
{% endhighlight %}

A Style is applied to all windows whose name, title, class or resource
matches the stylename (the module [/Modules/FvwmIdent](
{{ "/Modules/FvwmIdent" | prepend: site.baseurl }}) can be used to find this
info). Stylenames can include the wildcards * and ? to match differnt
groups of windows. After the stylename, list as many styles
as you want to apply separating them with commas.

To apply a style to all windows, use the wild card *. Here are some examples
of styles applied to all windows I use in my config file.

{% highlight fvwm %}
# Window Placement and Focus
Style * SloppyFocus, MouseFocusClickRaises, !FPGrabFocus
Style * MinOverlapPlacement, !UsePPosition

# Transient Windows
Style * DecorateTransient, RaiseTransient, \
        DontLowerTransient, StackTransientParent

# WindowShade
Style * WindowShadeScrolls, WindowShadeSteps 10

# Window Colorset Defaults
Style * Colorset 1, HilightColorset 2, \
        BorderColorset 3, HilightBorderColorset 4
{% endhighlight %}


You can also apply styles to windows by matching their
class/resource/name. For example the follow styles are for specific windows.

{% highlight fvwm %}
Style FvwmButtons !Title, !Borders, !Handles, Sticky, \
                  WindowListSkip, NeverFocus
Style ConfirmQuit !Title, PositionPlacement Center, \
                  WindowListSkip, Layer 6
Style FvwmIdent WindowListSkip
Style xterm MiniIcon icon/xterm.png
{% endhighlight %}

In general I try to use the class or resource of a window to match
for the style names. These usually will not change like a title or name can.

If you have multiple conflicting stylenames that match the same window,
the last one read will be the one that used. In this case you should
always generalize (list the * styles first) before you specialize. See
[/Config/StyleTips/]({{ "/Config/StyleTips" | prepend: site.baseurl }})
for a more details on working with styles.

