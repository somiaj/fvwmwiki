---
layout : wiki
title : FvwmAuto
type : module
description : |
  The FvwmAuto module allows you to define actions for when the pointer enters
  and leaves a window after a specified delay. A common use of this would be
  to automatically raise windows, which is in fact the module's default
  behaviour. This can also be used to auto show/hide a panel/dock.

---
* TOC
{:toc}

# FvwmAuto

## Module Description

The FvwmAuto module allows you to define actions for when the pointer enters
and leaves a window after a specified delay. A common use of this would be
to automatically raise windows, which is in fact the module's default
behaviour.

## Sample Configuration

FvwmAuto doesn't have a module configuration in the same sense as a lot of
the other modules.  The way this particular module works, is listening for
certain events that you can specify.  Along with that is the action to be
performed (typically a function.)

In its simplest form, the following would raise the focused window 250
milliseconds after receiving and maintaining focus:


    Module FvwmAuto 250


## Advanced Features

You can also use FvwmAuto to do a lot of other things.  One power of
FvwmAuto is the ability to schedule events when a window (essentially)
receives and loses focus [1].  The
[man page](http://www.fvwm.org/documentation/manpages/FvwmAuto.html)
has more examples about that.

-------
[1] This is not how EnterFocus and LeaveFocus operate, but from an explanation point of view, it suffices.
