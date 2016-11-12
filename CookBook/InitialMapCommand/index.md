---
layout : wiki
title : InitialMapCommand
type : recipe
description : |
  Old recipes required using FvwmEvent to preform an action on a new
  window such as Maximizing it or moving it to the top right corner
  of the screen. Such complex setups are no longer needed as this and
  more can be achieved though the InitialMapCommand.

---
# Running custom functions on newly created Windows.

There are a class of questions along the lines of how do I do "X"
when a window loads. Such as how does one start a window Maximized
or start a window the top right corner. In these cases there is
no default style that achieves this affect, so we need to use
InitialMapCommand.

To start all xterms in the top right of the screen we can use
AnimatedMove when the window loads to move the xterm to the desired
place. 

{% highlight fvwm %}
Style XTerm InitialMapCommand AnimatedMove -0 +0
{% endhighlight %}

To start chromium maximized just use the Maximze command.

{% highlight fvwm %}
Style chromium InitialMapCommand Maximize
{% endhighlight %}

This idea can be extended into various other applications of having a
a window start in a specific state. Take note that there are some
built in Styles that affect how applications start such as StartsIconic,
StartsShaded, StartsOnPage, etc. InitialMap command is there for
when there is no default Style to achieve the desired effect.

