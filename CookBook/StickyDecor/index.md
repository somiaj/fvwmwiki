---
layout : wiki
title : StickyDecor
type : recipe
description : |
  This recipe gives a way to use a different Decor for Sticky windows.
  This effect can be extended to set the Colorset/Decor of a window
  based on its state.
---
## Change of decor from focus/property change.

I originally wrote this for a friend of mine (hi, Heather). She wanted
sticky windows to have a different decor to any other window. The effect
overall is quite interesting, and could easily be adapted. The first step is
to define a decor for the sticky windows. Example:

{% highlight fvwm %}
AddToDecor StickyDecor
+ BorderStyle Simple
+ TitleStyle -- Raised
+ ButtonStyle Reset
+ ButtonStyle All -- Raised
+ ButtonStyle 1 Active    Pixmap mini.fvwm.xpm
+ ButtonStyle 1 Inactive  Vector 5 25x40@1 25x60@1 75x60@0 75x40@0 25x40@1
+ ButtonStyle 3 Active   Pixmap mini-icons.xpm
+ ButtonStyle 3 InActive Pixmap mini-icons.xpm
+ ButtonStyle 6 Active    Pixmap mini-rball.xpm
+ ButtonStyle 6 Inactive  Vector 5 40x40@1 60x40@1 60x60@0 40x60@0 40x40@1
+ ButtonStyle 4 Active    Pixmap mini-iconify.xpm
+ ButtonStyle 4 InActive  Vector 5 25x25@1 25x75@1 75x75@0 75x25@0 25x25@1
+ ButtonStyle 2 Active    Pixmap mini-x.xpm
+ ButtonStyle 2 InActive  Vector 17 20x20@1 30x20@1 50x40@1 70x20@1 80x20@1 \
  80x30@0 60x50@0 80x70@1 80x80@0 70x80@0 50x60@0 30x80@0 20x80@0 20x70@0 \
  40x50@1 20x30@0 20x20@1
{% endhighlight %}

This looks more complex than it actually is -- and it's beyond the scope of
this document to discuss how the decor works. Suffice it to say that with
the above decor, the buttons of a window will inherit different pixmaps.
The main focus (no pun intended) of this is to then decide which events need
to be flagged to change those windows that will become sticky. When a window
receives focus, we will need to check to see if it is sticky (the state of
the window might have been modified, without necessarily using something
like the mouse, which would send a focus event.) Also, since toggling the
state of a window is happening, we will need to check for the
ConfigureNotify event.  Lastly, we will also want to check the state of any
windows that are mapped on the screen, since they might explicitly have a
style line declaring them Sticky. Hence:

{% highlight fvwm %}
DestroyModuleConfig FvwmEvent-Sticky: *
*FvwmEvent-Sticky: Delay 1
*FvwmEvent-Sticky: configure_window FvwmToggleStickyPixmap
*FvwmEvent-Sticky: focus_change     FvwmToggleStickyPixmap
*FvwmEvent-Sticky: add_window       FvwmToggleStickyPixmap

# This line ensures that it starts up when FVWM does.
AddToFunc StartFunction I Module FvwmEvent FvwmEvent-Sticky
{% endhighlight %}

The last part, is of course, to define the action that is to be called when
any one of those events occurs. It's simple. All that has to be done is a
'toggle' effect, essentially testing whether a window is sticky, and if it
is to change the decor, and vice-versa.

{% highlight fvwm %}
DestroyFunc FvwmToggleStickyPixmap
AddToFunc   FvwmToggleStickyPixmap
+ I ThisWindow (Sticky)  ChangeDecor StickyDecor
+ I ThisWindow (!Sticky) ChangeDecor NormalDecor
{% endhighlight %}

Note that there's any number of things you could do with this, and it's not so
much the application of what has been done, but what you _could_ do with it.
:) You might be wondering why I am using 'ThisWindow' as opposed to
'Current'.  (You might not, but...) 'Current' assumes that the operand
window is the window that currently has the focus. In this situation, it's
probably true that it will, but that might not always be the case.

