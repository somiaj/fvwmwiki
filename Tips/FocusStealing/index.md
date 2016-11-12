---
layout : wiki
title : Focus Stealing
type : tip
description : |
  Some applications want to steal focus when an event
  is trigered. This describes how to disable apps from
  stealing focus in Fvwm.

---
* TOC
{:toc}

# Stopping Applications Stealing Focus

## Introduction

Many people are confused by some applications appearing to steal focus.
Usually, the following isn't enough:

{% highlight fvwm %}
Style foo !FPGrabFocus
{% endhighlight %}

Because that only works when the window is initially mapped.

## Stock functions changing focus.

FVWM comes with some functions pre-defined.  There's two functions in
particular which have the ability to change the focus to an application.

### EWMHActivateWindowFunc

This function runs when the window in question has some action to perform
-- such as updating itself in a taskbar by flashing the window.  The default
implementation looks like the following:

{% highlight fvwm %}
DestroyFunc EWMHActivateWindowFunc
AddToFunc EWMHActivateWindowFunc 
+ I Iconify Off
+ I Focus
+ I Raise
+ I WarpToWindow 50 50
{% endhighlight %}

It should be fairly obvious that the [[Focus]] command is the culprit here.
Generally, the solution is to simply destroy this function:

{% highlight fvwm %}
DestroyFunc EWMHActivateWindowFunc
{% endhighlight %}

### UrgencyFunc

This function is responsible for running each time a window receives an
UrgencyHint -- typically a BEL character, or a request for the user's
immediate attention through an IM message, or an IRC message, etc.  The
default implementation looks like this:

{% highlight fvwm %}
DestroyFunc UrgencyFunc
AddToFunc UrgencyFunc
+ I Iconify off
+ I FlipFocus
+ I Raise
+ I WarpToWindow 5p 5p
{% endhighlight %}

Again, as with EWMHActivateWindowFunc, the UrgencyFunc has [[FlipFocus]]
which is causing the focus to switch to the application.  This function is
perhaps more useful, so destroying it outright as in:

{% highlight fvwm %}
DestroyFunc UrgencyFunc
{% endhighlight %}

might be considered too drastic by some.  It's possible to selectively
disable this for certain windows:

{% highlight fvwm %}
DestroyFunc UrgencyFunc
AddToFunc   UrgencyFunc
+ I ThisWindow (!"Name1|Name2|Name3|Name4") Break
+ I ...
{% endhighlight %}

Note here, that any window *not* in the list for Name1, etc., would bail out
of the function.  Clearly though this list could get quite long after a
while.  A more sane approach might be to do this:

{% highlight fvwm %}
Style foo State 2
Style bar State 2
Style baz State 2, StartsOnPage 3 0 0
{% endhighlight %}

which sets up foo, bar, and baz, to have a tag, identified as "2" to be
associated with them.  This tag can then be referenced anywhere, as in:

{% highlight fvwm %}
DestroyFunc UrgencyFunc
AddToFunc   UrgencyFunc
+ I ThisWindow (State 2) Break
+ I ...
{% endhighlight %}

### !FPFocusByProgram and !FPFocusByFunction

At a more general level, applications can still decide to take focus
themselves -- even though in doing this they likely break the ICCCM.
However, if an application *still* refuses to give up focus, even after
tweaking the [[UrgencyFunc]] and [[EWMHActivateWindowFunc]] functions, it's
possible to use:

{% highlight fvwm %}
Style foo !FPFocusByProgram
{% endhighlight %}

Which forbids the application to set the focus itself (by disabing
\_XA\_WM\_TAKE\_FOCUS).

Related to that is the ability to tell FVWM to disallow [[Focus]] and
[[FlipFocus]] commands to be used on a specific window from functions.
Hence:

{% highlight fvwm %}
Style foo !FPFocusByFunction
{% endhighlight %}

But note that whilst most people set !FPFocusByFunction without considering
the consequences first, it's usually because they failed to understand
*which* functions -- if any -- from FVWM were causing this.  So use it
sparingly.

### XSetInputFocus()

This function call is outside of FVWM's remit, but this is generally the
last reason after trying everything else that an application will still set
focus, via the XSetInputFocus() call.  Applications shouldn't really use
this, but when they do, it more or less by-passes the window manager.  The
only way around this would be to use LD\_PRELOAD to redefine XSetInputFocus
to void.  This of course requires a .so wrapper in the first place.
