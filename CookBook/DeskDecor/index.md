---
layout : wiki
title : DeskDecor
type : recipe
description : |
  This recipe describes how to configure different Decors or
  Colorsets for different Pages and/or Desks. This is achieved
  by using FvwmEvent to trigger a function when the Page/Desk
  is changed.
---
# Different decors/colorsets for different pages/desks.

This is very similar to #3 in that this is more a variation on a theme. The
difference here though is that rather than relying on a change of property of a
window, there's a need to do something when a new page/desk event occurs --
and then for whichever page or desk requires the new decors, to adapt those
for all windows (in this situation, anyway.) You could construct all sorts
of elaborate things with this idea.

For simplicity's sake, let's assume that the desktop and page we want to
flag as different is "0 0 0". The first thing we should do is setup
FvwmEvent.  Remember that all we need to do is to listen for a change of
page/desk:

{% highlight fvwm %}
DestroyModuleConfig FvwmEvent-newPage: *
*FvwmEvent-newPage: new_page FvwmFuncNewStyle

Module FvwmEvent FvwmEvent-newPage
{% endhighlight %}

Then the fun starts -- defining the FvwmFuncNewStyle function that will
ultimately do all the hard work for us. The logic behind this is when a
change of desk/page happens, make sure that we're on desk 0, page 0 0. If we
are, then change all windows to use a decor or colorset, or what have you.
In addition to that, when we leave "0 0 0", we'll need to restore the
decor/colorsets to what they were originally.

{% highlight fvwm %}
DestroyFunc FvwmFuncNewStyle
AddToFunc   FvwmFuncNewStyle
+ I PipeRead '[[ $[desk.n] -eq 0 && $[page.nx] -eq 0 && $[page.ny] -eq 0 ]] \
    && echo "Function ChangeDecorWithMenu || echo "Function RestoreDecor"'
{% endhighlight %}

The PipeRead in the above, just qualifies which desk we're on, when we've
switched to it. It tests the desk number ($[desk.n]), and the two pages ($
[pages.nx], $[pages.ny]).

If we land on Desk 0 page 0 0, then the function ChangeDecorWithMenu is run.

{% highlight fvwm %}
DestroyFunc ChangeDecorWithMenu
AddToFunc  ChangeDecorWithMenu
+ I All (!Iconic,  AcceptsFocus, CurrentPage) WindowStyle Colorset 0
+ I All (!Iconic, AcceptsFocus, CurrentPage)  WindowStyle HilightColorset 3
{% endhighlight %}

Here, I have said that all windows that are not iconic (!Iconic), and that
accept focus (AcceptsFocus). (In the case of applying colorset styles to
windows this is important, since if the window cannot accept focus, then the
hilight colorset is useless applied to it, and just wastes precious little
memory), and that are on the current page to have an inactive colorset
defined as 0, and an active one defined as 3. Hence those might look like
the following:

{% highlight fvwm %}
Colorset 0 fg black, bg #60a0c0
Colorset 3 fg black, bg darkgreen
{% endhighlight %}

RestorDecor was the other function that we had defined earlier on. That will
get run on all pages to restore windows to some 'default' hilight colorset:

{% highlight fvwm %}
DestroyFunc RestoreDecor
AddToFunc   RestoreDecor
+ I All (!Iconic, AcceptsFocus, CurrentPage) WindowStyle HilightColorSet 1
{% endhighlight %}

And you could do other things with these functions. You could incorporate it
into [StickyDecor]({{ "/CookBook/StickyDecor" | prepend: site.baseurl }})
so that you selectively flagged different sticky windows. Or you could (as
the title of this question alludes to) use these functions to change decors,
and so forth. All good fun... :)

