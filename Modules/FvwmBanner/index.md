---
layout : wiki
title : FvwmBanner
type : module
description : |
  Displays an Fvwm Logo in the center of the screen for a set amount of time.

---
* TOC
{:toc}

# FvwmBanner

## Module Descrpition

Displays an Fvwm Logo in the center of the screen for 3 seconds.

An alternate pixmap can be specified, and the amount of time it's shown can be changed.

## Sample Configuration

Here is a sample configuration for FvwmBanner

    # Destroy the module definition.
    DestroyModuleConfig FvwmBanner: *

    # Don't Decorate the window and set the timeout.
    *FvwmBanner: NoDecor
    *FvwmBanner: Timeout 5

