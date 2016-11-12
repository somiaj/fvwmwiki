---
layout : wiki
title : Auto Hiding Windows
type : tip
description : |
  This describes how to configure windows to hide themselves
  by using WindowShade and the FvwmAuto Module.

---
# Autohiding Windows

Some applications have a feature usually called "autohiding"
which allows to withdraw a window to a location where it does
not use precious desktop space.  It is possible to write some
small functions in fvwm that can hide any window you like:

This approach only works in fvwm-2.5.8 or later:

{% highlight fvwm %}
DestroyFunc autohide
AddToFunc autohide
+ I ThisWindow ($0) Deschedule $[w.id]
+ I ThisWindow ($0) ThisWindow (Shaded) WindowShade off
+ I TestRc (!Match) All ($0, !Shaded) autohide\_hide $1 $2

DestroyFunc autohide_hide
AddToFunc autohide_hide
+ I Schedule $0 $[w.id] WindowShade $1
+ I Schedule $0 $[w.id] Deschedule $[w.id]

# Start FvwmAuto
AddToFunc StartFunction I Module FvwmAuto FvwmAutohide -menter enter_handler

# Add the windows you want to autohide
DestroyFunc enter_handler
AddToFunc enter_handler
+ I autohide FvwmButtons 500 S
#            ^           ^   ^
#            |           |   |___  Shade direction (optional)
#            |           |_______  Hide delay (milliseconds)
#            |___________________  Unique window name/resource
{% endhighlight %}

Simply add any windows you like to the enter\_handler function
as in the example above.  The autohide function is called with
two or three parameters.  The first one is the window's name
or class, which must be unique.  The second is the delay in
milliseconds before the window is hidden after the pointer
leaves it, and the last - optional - one indicates the
direction in which it is hidden (N, S, E, W, NW, NE, SW or SE).
