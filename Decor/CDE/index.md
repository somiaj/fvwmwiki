---
layout : wiki
title : CDE Decor Example
type : decor
weight : 600
description : |
  A Common Desktop Environment (CDE) Decor. This is a simple decor that
  uses no images and is built using Colorsets and Vector buttons.

---
# CDE Decoration Example

This example will configure your windows to look like the CDE desktop.

|![image](scrot.png)|

This is a Decor that doesn't require any images and can be done with
the effects built into Fvwm.

To use this decor first configure the 
[Colorsets]({{ "/Config/Colorsets" | prepend: site.baseurl }})

{% highlight fvwm %}
#   1 - Inactive Windows 
#   2 - Active Window
#   3 - Inactive Windows Borders
#   4 - Active Windows Borders
Colorset 1 fg white, bg #afbdc07ac200
Colorset 2 fg white, bg #cc0068006f00
Colorset 3 fg white, bg #afbdc07ac200
Colorset 4 fg white, bg #cc0068006f00
{% endhighlight %}

Next we need to [Bind]({{ "/Config/Bindings" | prepend: site.baseurl }})
actions to the window buttons (so they show up on the decor). This decor uses
use locations 1, 4 and 2

{% highlight fvwm %}
# Window Button Locations [1 Title 42]
Mouse 1 4 A Iconify
Mouse 1 2 A Maximize
Mouse 1 1 A Menu MenuWindowOps
{% endhighlight %}

Then define the Decor:

{% highlight fvwm %}
AddToDecor CDEDecor
+ TitleStyle    AllInactive -- Raised
+ TitleStyle    AllActive -- Raised
+ ButtonStyle   All Simple -- UseTitleStyle
+ BorderStyle   Simple
+ TitleStyle    Centered -- Raised
+ ButtonStyle   All -- Raised

+ AddButtonStyle 1 Vector 3 23x58@0 77x58@0 77x42@0
+ AddButtonStyle 1 Vector 3 23x58@1 23x42@1 77x42@1

+ AddButtonStyle 2 Vector 3 21x79@0 79x79@0 79x21@0
+ AddButtonStyle 2 Vector 3 21x79@1 21x21@1 79x21@1

+ AddButtonStyle 4 Vector 3 42x58@0 58x58@0 58x42@0
+ AddButtonStyle 4 Vector 3 42x58@1 42x42@1 58x42@1

+ TitleStyle Height MinHeight 20
{% endhighlight %}

Last we need the Styles for the windows to use CDEDecor, the
Colorsets and some other settings.

{% highlight fvwm %}
Style * Colorset 1, HilightColorset 2, \
        BorderColorset 3, HilightBorderColorset 4, \
        BorderWidth 5, HandleWidth 5, \
        MWMBorder, DepressableBorder, \
        MWMButtons, UseDecor CDEDecor
{% endhighlight %}

## Color Themes

This Decor was adopted from fvwm-themes which contained many color themes
that went with it. These themes can be found [here](
{{ "/Config/Colorsets/#color-themes" | prepend: site.baseurl }}). Follow
those instructions to create a menu that can change between the different
color themes.
