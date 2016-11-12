---
layout : wiki
title : Transparency
type : tip
description : |
  A few tips about Transparent FvwmButtons.

---


# Transparency

If you want to make your swallowed FvwmPager transparent, you have to make the FvwmButtons transparent, too.

    Pixmap none

will not work, you have to use: 

    Pixmap /path/to/transparent/image 

for both modules.

But it is much better to always use colorsets. So, instead of Pixmap, use
``Colorset <n> Transparent/RootTransparent``, and then ``Style FvwmButtons
ParentalRelativity``.
