---
layout : wiki
title : FvwmAnimate
type : module
description : |
  This module animates iconification and de-iconification on command.
---
* TOC
{:toc}

# FvwmAnimate

## Module Description

The FvwmAnimate module animates iconification and de-iconification or on command.  There are currently 6 different animation effects.

These are:

 * Frame
 * Lines
 * Flip
 * Turn
 * Zoom3D
 * Twist
 * Random
 * None

You can also specify a Pixmap, or a color can be used for XOR against the backdrop.

## Sample Configuration

Here is a sample configuration for FvwmAnimate.


        # Destroy the module definition.
        DestroyModuleConfig FvwmAnimate: *

        # I don't care which effect I use.  I like variety.
        *FvwmAnimate: Effect Random

        # How many steps the iterations will be.  25 is about right, but if
        # this is too long, shorten the number.
        *FvwmAnimate: Iterations 25

        # How many milliseconds to wait before the next frame starts.
        *FvwmAnimate: Delay 2

        # How thick (in pixels) the lines for the animation are to be drawn.
        *FvwmAnimate: Width 3

        # How many revolutions to twist the iconification frame.
        *FvwmAnimate: Twist 6


## Advanced Use

You can have a lot of fun with this module. For those of you that don't like
icons, but still want to use the FvwmAnimate module, then you can use the
following:

        Mouse 1 R A SomeFunc

        AddToFunc SomeFunc
        + I SendToModule FvwmAnimate animate 20 25 15 10 44 23 6 12#
        + I Iconify

Which assumes that when you click in the root window, the !SomeFunc function
gets run, iconifying the window using an odd effect.  The numbers passed to
the module denote starting and ending coordinates in pairs of four lots.

Other features include being able to pause animation, continue animation,
and save the current status of the module to a file that FvwmAnimate will
load up each time it starts.

## Man Page

The Man Page is available on the fvwm.org site.
[FvwmAnimate](http://fvwm.org/documentation/manpages/FvwmAnimate.html)

