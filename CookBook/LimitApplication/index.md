---
layout : wiki
title : LimitApplication
type : recipe
description : |
  When running an application this will check to see if it is already
  running. And if so instead of launching a new application, switch
  to the one that is currently running.

---

# Limiting instantiation of a window/application.

Sometimes there is a need to make sure that only one instance of a running
application is active, and any attempt to run another one silently fails.
It's rather specific, but is useful in some situations. For example, I have
a screen session that I have active. Rather than reloading it and attaching
it, I like to just warp to wherever the window is. If the window isn't
active, then it is launched.

{% highlight fvwm %}
DestroyFunc LimitApplication
AddToFunc   LimitApplication
+ I Next ($0, CurrentDesk, CirculateHit) FlipFocus
+ I TestRc (NoMatch) None ($0, CurrentDesk) Exec exec $0
{% endhighlight %}

So the above looks for the next window that is on the current desk, and if
it is, the focus is sent to that window. Else, if there isn't (TestRc
(NoMatch)), and there really isn't a window with that name, then it is
started. Note that there is quite a few ways that you can write the above
function.

As to how it is invoked, there's any number of ways. In the form as it is
above, it can only match based on the function receiving parameters -- so
this would suggest something along the lines of key-bindings, as in:

{% highlight fvwm %}
Key s A CM LimitApplication screen1
Key x A CM LimitApplication xine
Key d A CM LimitApplication irssi
{% endhighlight %}

So that "$0" in the function is expanded to whatever is passed into the
function -- in this case, either "screen1", or, "xine", or "irssi". The
drawback to this approach is that the applications being checked/launched
can only be done so via FVWM -- be it via key bindings as demonstrated, or
mouse bindings, etc. Launching, say, irssi, from an xterm by-passes the use
of the function, and so the window will start up, when we might not want it
to. In situations like that, it's best to use FvwmEvent.  The function will
need adapting.

Note that the above implementation has some limitations, not least of which is
that the function assumes the name of the application is the same name as the
binary -- but most applications change their WM_NAME as they run.  Instead, it
might be better to pass in two parameters -- the first one could be the Class
of the window, and the remaining arguments could be how to start the application.
Here's an example of that:

{% highlight fvwm %}
DestroyFunc LimitApplicationImproved
AddToFunc   LimitApplicationImproved
+ I Next ($0, CurrentDesk, CirculateHit) FlipFocus
+ I TestRc (NoMatch) None ($0, CurrentDesk) Exec exec $[1-]
{% endhighlight %}

That way, we could then do the following:

{% highlight fvwm %}
Key s A CM LimitApplicationImproved screen1 xterm -T screen1 -e screen
Key x A CM LimitApplicationImproved Xine xine
Key d A CM LimitApplicationImproved irssi xterm -T irssi -e irssi
{% endhighlight %}

So that in the above example, FVWM would check for a window called "screen1",
and if that didn't exist, FVWM would spawn an xterm with the title "screen1",
running screen.


