---                                                                             
layout : wiki
title : BorderMaximize
type : tip
description : |
  When Maximizing windows, you may not want them to cover the full screen,
  so they don't cover panels. This tip shows how to configure Fvwm to
  not use the full screen when Maximizing windows.

---
# Maximizing windows with free space at top

I have laptop with a broken LCD, it lacks the first 27pixel rows, these
usually cover the titlebar of normally-maximized windows. Having a window
maximized with some free space at the bottom is an easy task, just use
EwmhBaseStruts which reserves space along the edge of the screen when windows
are maximized and placed:

{% highlight fvwm %}
# EmwhBaseStruts [left] [right] [top] [bottom]
EwmhBaseStruts 0 0 27 0
{% endhighlight %}

An older Alternative was to write a customized MyMaximize function
to do the work. This is done by using the Maximize function inputs
to make the window to be 27 pixels less than the height of
the screen, then Move the window down 27 pixels.

{% highlight fvwm %}
AddToFunc MyMaximize
+ I Maximize 100 -27p
+ I Current (Maximized) Move 0p 27p
{% endhighlight %}

