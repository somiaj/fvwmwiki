---
layout : wiki
title : Center Placement of Windows
type : tip
description : |
  Various ways to center a window.

---

# Centring Windows

A very easy function to center your window without any hardcoded screen height and width:

{% highlight fvwm %}
DestroyFunc CenterWindow
AddToFunc   CenterWindow
+ I ThisWindow Piperead "echo Move \
    $(( $[vp.width]/2-$[w.width]/2 ))p \
    $(( $[vp.height]/2-$[w.height]/2 ))p"

Key KP\_Begin A 4 CenterWindow
{% endhighlight %}

Note that in Fvwm >=2.5.12, one can use a default style ''CenterPlacement'', hence:

{% highlight fvwm %}
Style myapp CenterPlacement
{% endhighlight %}

And with FVWM >=2.5.27, the CenterPlacement style was folded into the
PositionPlacement style option, hence:

{% highlight fvwm %}
Style myapp PositionPlacement center
{% endhighlight %}

If the window still doesn't follow correctly, try to disable PPosition and USPosition:

{% highlight fvwm %}
Style myapp PositionPlacement center, NoPPosition, NoUSPosition
{% endhighlight %}

