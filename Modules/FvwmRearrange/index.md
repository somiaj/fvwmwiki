---
layout : wiki
title : FvwmRearrange
type : module
description : |
  FvwmRearrange can be used to tile or cascade windows.

---
* TOC
{:toc}

# FvwmRearrange

## Module Description

This module can be called to tile or cascade windows.

When tiling the module attempts to tile windows on the current
screen subject to certain constraints. Horizontal or vertical tiling
is performed so that each window does not overlap another,
and by default each window is resized to its nearest
resize increment (note sometimes some space might appear between
tiled windows -- this is why).

When cascading the module attempts to cascade windows on the
current screen subject to certain constraints. Layering is performed
so consecutive windows will have their window titles visible underneath
the previous.


