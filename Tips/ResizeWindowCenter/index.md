---
layout : wiki
title : Resize a Window then Center It
type : tip
description : |
  Describes how to resize a window and then center it.

---

# Resizing a Window, in the centre

You will also need the function CenterWindow from [Tips/CenterPlacement](
{{ "/Tips/CenterPlacement" | prepend: site.baseurl }})
for this way of solving the problem.  This function allows you to resize a
window, and then have it moved to the centre of the screen, afterwards.

{% highlight fvwm %}
DestroyFunc ResizeCenter
AddToFunc ResizeCenter
+ I Resize $*
+ I CenterWindow

Key KP_Next A S4 ResizeCenter br w+5 w+5
Key KP_Home A S4 ResizeCenter br w-5 w-5
Key KP_Left A S4 ResizeCenter br w-5 keep
Key KP_Right A S4 ResizeCenter br w+5 keep
Key KP_Up A S4 ResizeCenter br keep w-5
Key KP_Down A S4 ResizeCenter br keep w+5
{% endhighlight %}

Note though, that in FVWM version 2.5.X, there is also the style of "CenterPlacement" that you can use:

{% highlight fvwm %}
DestroyFunc ResizeCenter
AddToFunc ResizeCenter
+ I Resize $*
+ I ThisWindow WindowStyle CenterPlacement
+ I UpdateStyles
{% endhighlight %}

