---
layout : wiki
title : ShowDesktop
type : recipe
description : |
  This is the MS-Windows inspired feature that will show the desktop
  by Iconfiying all the windows on the current Page. Further it shows
  how to save the State of the windows so only the windows affected
  can be restored.

---
## "Show Desktop" Feature.

One thing that again has been borrowed from MS-Windows is the idea of "Show
Desktop" -- that is, making the root window visible. In it's simplest form,
it can be emulated as per #1, although what this does not do is take into
account the restoration of windows to their original position afterwards.

Indeed, the application of this is probably best suited to a button inside
an FvwmButtons instance -- and this is what we'll demonstrate here. In its
simplest form one can iconify all windows with the following command:

{% highlight fvwm %}
All (CurrentPage, !Iconic) Iconify
{% endhighlight %}

... which would iconify windows on the current page. But the problem then
arises of making sure that the toggle action restores the original windows
to their state, Now, FVWM allows for a window, or windows to be flagged via
a number (anywhere between 0 - 31 inclusive). These states can the be used
to flag the windows before they iconify so that they can be restored.

{% highlight fvwm %}
DestroyFunc ShowDesktop
AddToFunc   ShowDesktop
+ I All (CurrentPage, Iconic, State 1) RestoreDesktop
+ I TestRc (Match) Break
+ I All (CurrentPage, !Iconic, !State 1) ThisWindow State 1 True
+ I All (CurrentPage, !Iconic, State 1) Iconify
{% endhighlight %}

In many ways this function works backwards -- the very first thing it does is
to look at all windows on the current page, that are iconic, and have a state
of one. If that matches, even for one window then the RestoreDesktop
function gets called. The reason why the check is done at the beginning of
this function rather than at the end (as logic might well dictate) is
because the window state flags get cleared -- invalidating the windows in
the first place.  The next line then checks the success of the first line.
If:

{% highlight fvwm %}
+ I All (CurrentPage, Iconic, State 1) RestoreDesktop
{% endhighlight %}

... returns true (i.e. it matched some windows) then the rest of the
function isn't executed. The remaining lines in that function flag all
windows to use a state number of one (chosen arbitrarily for this example),
and then iconify all windows with that state.

Moving on to the RestoreDesktop, that does the reverse -- in that it
deiconifies all windows with the state 1 bit on them, and then removes it:

{% highlight fvwm %}
DestroyFunc RestoreDesktop
AddToFunc   RestoreDesktop
+ I All (CurrentPage, Iconic, State 1) Iconify off
+ I All (CurrentPage, State 1) ThisWindow State 1 False
{% endhighlight %}

I mentioned you might want to bind this operation to FvwmButtons. As an
example, here's a part of a likely config:

{% highlight fvwm %}
*MyPanel: (1x2, Icon showdesk.png, Action (Mouse 1) Function ShowDesktop)
{% endhighlight %}

You might also bind that to a key binding, or some such.

