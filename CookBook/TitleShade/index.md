---
layout : wiki
title : TitleShade
type : recipe
description : |
  WindowShade can be done an any direction, but if it is not in
  the direction of the TitleBar the window will collapse to just
  its borders. This recipe will rotate the TitleBar to the corresponding
  side.

---
## Shading of windows to move TitleBar in the same direction.

FVWM has the ability to shade windows in all directions: North, South, East,
West, and diagonally between those. Whilst this is useful, what the shading
currently does not do, is move the TitleBar to the correct side of the
window, based on the direction the window is being shaded. So for example,
if a window is told to shade to the left, then all one would likely see is
two vertical borders juxtaposed, and nothing more -- the TitleBar would have
shaded inside it. The following function best shows this in action, as
describing it takes far too many words:

{% highlight fvwm %}
DestroyFunc RaiseOrShade
AddToFunc   RaiseOrShade
+ C     Raise
+ D     WindowShade $[func.context]

Mouse 1         SF      A RaiseOrShade
{% endhighlight %}

Clicking once with mouse button 1 on any of the window sides/frame would raise
the window. Double-clicking on the window would shade the window in that
direction -- try it, and you'll see what happens. To de-shade it, just
double- click again. Fun, eh? The trick to that relies on what
$[func.context] expands to. Whenever a window is shaded, it is told in which
direction it is doing so -- FVWM translates that into various 'symbols' that depict a given direction.

So, in order to move the TitleBar in the same direction, we just need to
translate those symbols to directions, and set the TitleBar location. We'll
need a helper function for that, though:

{% highlight fvwm %}
DestroyFunc FuncShadeMe
AddToFunc FuncShadeMe
+ I PipeRead `case $[func.context] in "t") \
    echo 'ThisWindow (Shaded) WindowStyle TitleAtTop'; echo 'WindowShade toggle';; \
    "[") echo 'ThisWindow (!Shaded) WindowStyle TitleAtLeft' && echo 'WindowShade [';; \
    "]") echo 'ThisWindow (!Shaded) WindowStyle TitleAtRight' && echo 'WindowShade ]';; \
    "-") echo 'ThisWindow (!Shaded) WindowStyle TitleAtTop' && echo 'WindowShade -';; \
    "_") echo 'ThisWindow (!Shaded) WindowStyle TitleAtBottom' && echo 'WindowShade _';;esac`
{% endhighlight %}

So you can see from the above that when ``$[func.context]`` interpolates to
a ``[`` that the window is shading to the left, and "]" to the right, etc.
Then knowing that means the style of the window to which the shade operation
is being applied need just be told where to put the TitleBar. The last thing
left to do is adapt the RaiseOrShade function to use this helper function:

{% highlight fvwm %}
DestroyFunc RaiseOrShade
AddToFunc   RaiseOrShade
+ C     Raise
+ D     FuncShadeMe

Mouse 1         SF      A RaiseOrShade
{% endhighlight %}

