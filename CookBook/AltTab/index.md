---
layout : wiki
title : AltTab
type : recipe
description : |
  Alt-Tab is a common key binding to switch between windows. In Fvwm
  there are lots of different variations on how to do this.

---

## Switching focus between windows. (Alt-Tab)

The default-config Alt-Tab binding in Fvwm looks like

{% highlight fvwm %}
Key Tab A M WindowList Root c c NoDeskSort, SelectOnRelease Meta_L
{% endhighlight %}

When Alt-Tab is hit a Menu appears that lists all the windows. As long
as you hold down the Alt key, you can keep pressing tab to cycle through
this Menu to select the window you want then release Alt to switch to that
menu.

Although WindowList can be configured a bit, not everyone
wants a Menu to appear when one hits Alt-Tab. One
simple solution to that is just use the Next and Prev conditionals
to switch between windows. For example if one wanted to switch between
windows on the current Desktop, the following keybindings would work.

{% highlight fvwm %}
Key Tab A M Next (CurrentDesk, AcceptsFocus) Focus
Key Tab A SM Prev (CurrentDesk, AcceptsFocus) Focus
{% endhighlight %}

This simple solution works but it may not completely achieve the affect you
want. For example if you hit Alt-Tab again do you want to go back to your
previous window or not? Do you want to move the pointer to the window
that is selected? Do you want to DeIconify the window or Raise it? The Focus
command only gives the window Focus, it doesn't alter the window list order,
DeIconfiy, Raise, or even move the mouse pointer. All of this can be achieved
with a more complex function:

{% highlight fvwm %}
# Custom Focus Function
DestroyFunc MyFocusFunc
AddToFunc MyFocusFunc
+ I Iconify off
+ I FlipFocus
+ I Raise
+ I WarpToWindow !raise 5 5

# Key Bindings
Key Tab A M Next (CurrentDesk, AcceptsFocus) MyFocusFunc
Key Tab A SM Prev (CurrentDesk, AcceptsFocus) MyFocusFunc
{% endhighlight %}

As you can see you can keep building on this to achieve an Alt-Tab behavior
that is more like you want. Next is another example that someone used
because even this did not achieve the desired Alt-Tab experience the user
wanted.

## Another Alt-Tab Function

I don't like the default behavior of FVWM's Alt-Tab key combination -- yes,
the WindowList is useful, but it's not what I want to see when I want to
focus other windows --- I prefer (dare I say it) functionality similar to
MS-Windows.  I'd much rather be able to cycle windows. There's some
suggestions in the main FVWM_FAQ about how to do this, although that still
didn't quite emulate what I was after --- indeed, none of the solutions
cycled back round to the first window. So, here's my solution to it.

{% highlight fvwm %}
SetEnv DIR Next

AddToFunc FocusRaiseAndStuff
+ I Iconify off
+ I Focus
+ I Raise

AddToFunc SwitchWindow
+ I $[DIR] (CurrentPage, !Iconic, !Sticky) FocusRaiseAndStuff
+ I Deschedule 134000
+ I PipeRead `[ "$[DIR]" == "Prev" ] && \
    echo 'SetEnv NDIR Next' || \
    echo 'SetEnv NDIR Prev'`
+ I Schedule 700 134000 SetEnv DIR $[NDIR]

Key Tab A M  SwitchWindow
{% endhighlight %}

The SwitchWindow function does all the work. It might look elaborate, but all
it is doing is flipping the value of Next and Prev into the DIR environment
variable, so that if the last window is reached, it goes back to the first.
The schedule command is used because without it, the focusing of windows
gets confused -- so the delay via the Schedule commands ensures this isn't
the case.  The caveat being that switching windows can be ever so slightly
slow.

