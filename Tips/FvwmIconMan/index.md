---
layout : wiki
title : FvwmIconMan
type : tip
description : |
  Some tips about the module FvwmIconMan.

---


# Icon Manager with window-op buttons



Not being able to close/iconfiy/maximize windows with the mousebecause it is
convered by FvwmButtons now has an end. My idea is having a FvwmIconMan
swallowed in FvwmButtons with the height of the titlebar. For example 16
pixels on top of the screen. Let it only show windows on the current page.
Now if the window is fully maximized its titlebar is covered and FvwmIconMan
replaces it. This way you have a very much TAB-like feeling but the titlebar
buttons are covered. So we change our FvwmButtons configuration a bit.


{% highlight fvwm %}
*FvwmButtons-IB: Padding 0 0
*FvwmButtons-IB: Geometry 1276x15+0+0
*FvwmButtons-IB: BoxSize fixed
*FvwmButtons-IB: Rows 1
*FvwmButtons-IB: (1x1, Icon shrink-rvb-black.png, Action Current Iconify)
*FvwmButtons-IB: (80x1, Swallow "FvwmIconMan" "Module FvwmIconMan")
*FvwmButtons-IB: (1x1, Icon grow-rvb-black.png, Action Current Maximize 100 100)
*FvwmButtons-IB: (1x1, Icon cross-rvb-black.png, Action Current Close)
{% endhighlight %}

Now there are titlebar buttons on the FvwmButtons module, but you have to
select the window to act on. To change that behavior you can prevent
FvwmButtons from receiving focus using

{% highlight fvwm %}
Style FvwmButtons-IB NeverFocus
{% endhighlight %}

This way the buttons act on the focused window.

