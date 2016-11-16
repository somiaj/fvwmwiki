---
layout : wiki
title : Window Decorations
type : config
weight : 450
description : |
  This gives an overview of how to configure window decorations.
  See <a href="{{ "/Decor" | prepend: site.baseurl }}">/Decor</a>
  for example decors.

---
* TOC
{:toc}

# Window Decor

A Window Decor defines how a window looks. There are two
different meanings of Window Decor that could get used.

+ The collection of all the different things that can be configured
  to affect the look of a window.
+ The Decor definition (see AddToDecor) which is a wrapper for some
  of the options, namely ButtonStyle, TitleStyle and BorderStyle.

When talking about the window decor in general, this is the collection
of the following config options:

1. [/Config/Colorsets]({{ "/Config/Colorsets" | prepend: site.baseurl }})
   -- Default Colorsets of the windows.
2. [/Config/Bindings]({{ "/Config/Bindings" | prepend: site.baseurl }})
   -- Bindings to the buttons, titlebar and border to interact with the window.
3. [WindowStyles](#window-styles)
   -- The Window Styles which includes ButtonStyles, TitleStyles and
   BorderStyles.
4. [/Config/Style]({{ "/Config/Style" | prepend: site.baseurl }})
   -- The window Styles that affect looks.

Below is a description of the basics behind configuring a Decor. See
[/Decor]({{ "/Decor" | prepend:site.baseurl }}) for examples.

## Colorsets

There are four basic default Colorsets for windows. The Titlebar/Buttons and the Borders
for both Active and Inactive windows.
Using the Style command we can set these [Colorsets](
{{ "/Config/Colorsets" | prepend: site.baseurl }}) to the convention:

{% highlight fvwm %}
#   1 - Inactive Windows
#   2 - Active Window
#   3 - Inactive Windows Borders
#   4 - Active Windows Borders
Style * Colorset 1, HilightColorset 2, \
        BorderColorset 3, HilightBorderColorset 4
{% endhighlight %}

Active Window is the current window with focus, and all the other windows
are Inactive.

You can also set the Colorset via the TitleStyle, ButtonStyle and BorderStyle
options (see below). I prefer to use the above Styles to set the Colorset, because
it makes it easier to change just the Colorset for a single window via a Style
command.

{% highlight fvwm %}
Style MyDifferentWindow Colorset 11, HilightColorset 12
{% endhighlight %}


## Bindings

Bindings are used to configure how the window interacts with the mouse.
The aspect that is important to the decor is you need to configure what
happens when the window buttons are clicked.

For example you could have 4 buttons on your windows:

{% highlight fvwm %}
# Window Button Locations [1 Title 642]
Mouse 1 2 A Close
Mouse 1 4 A Maximize
Mouse 1 6 A Iconify
Mouse 1 1 A Menu MenuWindowOps
{% endhighlight %}

You can also use the "Button N" and "!Button N" Styles to show/hide buttons. By default
only buttons with Bindings will be shown.

## Window Styles

Window Styles are split into three different types: ButtonStyles,
TitleStyles, and BorderStyles. Each of these styles controls the look
of the associated piece.

These styles have lots of options, so only the most common are given below.
Use the [manpage](http://fvwm.org/documentation/manpages/fvwm.html#lbBV)
to get a complete description of all possibilities.

### TitleStyle

TitleStyle controls the main titlebar, not including the window buttons.

There are two different ways to use TitleStyle. The first is

{% highlight fvwm %}
TitleStyle justification Height N
{% endhighlight %}

This controls the basics of the titlebar, setting the justification
to Centered, RightJustified or LeftJustified and the height of the title
bar in pixels (note: The justification statement is optional).
For example:

{% highlight fvwm %}
TitleStyle RightJustified Height 22
{% endhighlight %}

The second way to use TitleStyle is

{% highlight fvwm %}
TitleStyle State Style -- Flag
{% endhighlight %}

+ State is the state of the titlebar. The state is one of ActiveUp,
  ActiveDown, Active (means both ActiveUp and ActiveDown), InactiveUp,
  InactiveDown or Inactive.

  Active is the focused window, Inactive is all others. Up/Down is if the mouse
  is currently clicking on the titlebar to press it Down or not.

  If State is omitted, the style is applied to all windows.

+ Style is the style to use. Some of the styles used in this wiki are
  + __?Gradient__ - This uses a Gradient for the titlebar. ?Gradient
    could be HGradient (horizontal), VGradient (vertical), DGradient
    (diagonal), and more (see manpage).
  + __Pixmap__ - Specifies a pixmap to use for the titlebar. Alternatives are
    AdjustedPixmap, ShrunkPixmap, StretchedPixmap, TiledPixmap to control
    how the Pixmap is placed modified to fit on the titlebar.
  + __MultiPixmap__ - This is a flexible option that lets you set a different
    TiledPixmap, AdjustedPixmap or Colorset to different parts of the titlebar.

+ Flag is one of "Flat", "Raised" or "Sunk". This will control the 3D beveled
  look and either make the title bar appear flat, raised up or sunk down.

TitleStyle needs to be defined for each different state. In a basic setup you only
need to define the Active and Inactive states. To have a Flat title bar using
gradients, use something like

{% highlight fvwm %}
TitleStyle Active HGradient 20 navy red -- Flat
TitleStyle Inactive HGradient 20 navy grey -- Flat
{% endhighlight %}

This will set up a horizontal gradient for the titlebar. Active windows will
change from the color navy to red, and the inactive windows will change from
the color navy to grey. Basic syntax for gradients is

Additionally you can put multiple states in a single (extended) line as follows

{% highlight fvwm %}
TitleStyle \
    ActiveUp (style -- flag) \
    ActiveDown (style -- flag) \
    InActiveUp (style -- flag) \
    InActiveDown (style -- flag)
{% endhighlight %}

Finally there is AddTitleStyle which is similar to TitleStyle, with the difference
it will Add the style to the previous defined TitleStyle (and any other AddToTitleStyle
settings).

#### MultiPixmap

The MultiPixmap style can be used to define a TiledPixmap, AdjustedPixmap,
or Colorset of different regions of the titlebar. The following shows how
the title bar is split up into multiple sections.

|![image](MultiPixmap.png)|

The basic syntax for a MultiPixmap is

{% highlight fvwm %}
TitleStyle state MultiPixmap section style, section style, ...
{% endhighlight %}

For example if you wanted to put a TiledPixmap under the main part of the
title bar but include a transitional image on both the LeftEnd and RightEnd
you could use something like

{% highlight fvwm %}
TitleStyle Active MultiPixmap \
    Main TiledPixmap main-active.png, \
    LeftEnd AdjustedPixmap leftend-active.png, \
    RightEnd AdjustedPixmap rightend-active.png
TitleStyle Inactive MultiPixmap \
    Main TiledPixmap main-inactive.png, \
    LeftEnd AdjustedPixmap leftend-inactive.png, \
    RightEnd AdjustedPixmap rightend-inactive.png
{% endhighlight %}

You don't need to set the image for the Buttons as that is done with ButtonStyle.
But if you use LeftButtons, RightButtons (or Buttons for both) in a MultiPixmap,
you need to specify UseTitleStyle in the ButtonStyle.

One last thing to be aware of is LeftEnd, RightEnd, LeftOfText and RightOfText
require space available. If the title text is so long there is no room left,
these sections will not be sown and you will only see UnderText and the Buttons.

### ButtonStyle

ButtonStyle controls the different styles of the window
buttons. There are two different ways to use ButtonStyle. The first is

{% highlight fvwm %}
ButtonStyle button - flag
{% endhighlight %}

This sets basic Toggle flags for the button. The possible flags are
MwmDecorMax, MwmDecorMin, MwmDecorMenu, MwmDecorShade, MwmDecorStick and
MwmDecorLayer [layer]. Adding a ! will remove the flag and there is also
a Clear flag to remove all flags.

These flags affect the Toggle states of a button. If you have configured
a Toggle style for a Maximized button, the MwmDecorMax flag needs to be set.
If so the button will display a different style when the window is Maximized.

The second way to use ButtonStyle is very similar to TitleStyle

{% highlight fvwm %}
ButtonStyle Button State Style -- Flag
{% endhighlight %}

+ Button is the button number or one of "All", "Left" or "Right". This
  sets which button(s) the style is for.
+ State is the state of the button such as the Active/Inactive, Pressed
  Up/Down and last Toggled (for the MwmDecor flags). You can specify
  a single state or use groups of states. The full list of possibilities is

      ActiveUp, ActiveDown, Active, InactiveUp, InactiveDown, Inactive,
      ActiveUpToggled, ActiveDownToggled, ActiveToggled,
      InactiveUpToggled, InactiveDownToggled, InactiveToggled,
      AllNormal, AllToggled, AllActive, AllInactive, AllUp, AllDown,
      AllActiveUp, AllActiveDown, AllIncativeUp, AllInactiveDown

  If the state is omitted, the ButtonStyle applies to all buttons.

+ Style configures one of the following styles to the buttons that match
  the given state. These styles are similar to the ones for TitleStyle
  + __Colorset__ - Sets the colorset of the button.
  + __Vector__ - Configures a [VectorButton](
    {{ "/Config/VectorButtons" | prepend: site.baseurl }}) for the button.
  + __?Gradient__ - Uses a gradient for the button.
  + __Pixmap__ - Sets a pixmap, can also use AdjustedPixmap, ShrunkPixmap,
    StretchedPixmap and TiledPixmap.
  + __MiniIcon__ - Displays the MiniIcon of an app in the button. The MiniIcon
    can be set by Style App MiniIcon icon.png.

+ Flag is one of "Flat", "Raised" or "Sunk". This will control the 3D beveled
  look and either make the title bar appear flat, raised up or sunk down.

  Additionally there are two more flags, UseTitleStyle and UseBorderStyle,
  which can be used for the button to Use the corresponding style.

As with TitleStyles you can specify one ButtonStyle per line

{% highlight fvwm %}
ButtonStyle 2 Active Pixmap close-active.png
ButtonStyle 2 Inactive Pixmap close-inactive.png
{% endhighlight %}

Or you can include multiple states in a single (extended) line configuration

{% highlight fvwm %}
ButtonStyle 2 \
    ActiveUp (Pixmap close-activeup.png -- Flat) \
    ActiveDown (Pixmap close-activedown.png -- Flat) \
    Inactive (Pixmap close-inactive.png -- Flat)
{% endhighlight fvwm %}

There is also an AddButtonStyle that works like ButtonStyle, with the
difference is it will Add the new style to any existing styles.
  
### BorderStyle

BorderStyles are like TitleStyle and ButtonStyle but have far less options.
The basic syntax is

{% highlight fvwm %}
BorderStyle state style -- flag
{% endhighlight %}

+ State is either Active or Inactive.
+ Style can be TiledPixmap or Colorset.
+ Flag can be Raised, Sunk or Flat. Additionally you can also use
  HiddenHandles or NoInset for controlling if the line between window
  corners and sides is drawn. 

### AddToDecor

TitleStyles, ButtonStyles and BorderStyles can all be grouped together
into a single Decor via the AddToDecor command.

{% highlight fvwm %}
AddToDecor MyDecor
+ TitleStyle ...
+ ButtonStyle ...
+ BorderStyle ...
+ ...
{% endhighlight %}

This will group all the styles into a Decor so they can be applied
via the UseDecor style.

{% highlight fvwm %}
Style * UseDecor MyDecor
{% endhighlight %}

Decors can be useful as a way to group all the Styles together and also
give you a way to use different Decors for different windows.

## Decor Styles

Here are some additional styles that affect window looks.

+ Title, !Title -- Set if the window has a titlebar.
+ Borders, !Borders -- Sets if the window has borders.
+ Handles, !Handles -- Sets if the handles (the area for a mouse binding
  commonly used to resize the window).
+ HandleWidth, BorderWidth -- Sets the width of the Handles and/or Borders.
+ DepressableBorder, FirmBorder -- Sets if the border has a sunken look
  when the borders are clikced.
+ Button N, !Button N -- Configures if the window shows button N or not.
  By default only the buttons with bindings are shown.
+ MwmButtons, FvwmButtons -- MwmButtons makes a button look pressed-in when
  maximized by using the MwmDecorMax flag. FvwmButtons switches this off.
+ TitleAtBottom, Left, Right, Top -- To put the title bar on various sides
  of the window.
+ LeftTitleRotatedCW, RightTitleRotatedCCW -- Rotates title text. There is actually
  four options for all combinations.
+ TopTitleRotate, BottomTitleNotRotated -- Rotates text for top/bottom tiles or not.
  Four options total.
+ Font -- Sets the font used by the titlebar (used DefaultFont otherwise).
+ TitleFormat -- String to set the format of the info displayed in the title.

## Examples

You can find a collection of examples in the [/Decor](
{{ "/Decor" | prepend: site.baseurl }}) page. These examples
range from simple Vector and Colorset examples to ones that use Pixmaps.
Here are some links to the example decors:

__Vector Examples__:
+ [/Decor/Default]({{ "/Decor/Default" | prepend: site.baseurl }})
  -- Flat Decor for the default config.
+ [/Decor/CDE]({{ "/Decor/CDE" | prepend: site.baseurl }})
  -- CDE looking decor.
+ [/Decor/Vectors]({{ "Decor/Vectors" | prepend: site.baseurl }})
  -- Basic Vector decor showing the Raised/Sunk effects.

__Pixmap Examples__:
+ [/Decor/OSX]({{ "/Decor/OSX" | prepend: site.baseurl }})
  -- Mac OSX look-a-like.
+ [/Decor/Redmond98]({{ "/Decor/Redmond98" | prepend: site.baseurl }})
  -- Windows 98 look-a-like.
+ [/Decor/RedmondXP]({{ "/Decor/RedmondXP" | prepend: site.baseurl }})
  -- Windows XP look-a-like.
+ [/Decor/QNX]({{ "/Decor/QNX" | prepend: site.baseurl }})
  -- Custom pixmap decor.
+ [/Decor/Mech]({{ "/Decor/Mech" | prepend: site.baseurl }})
  -- Another custom pixmap decor.

__Mixed Example__:
+ [/Decor/Crux]({{ "/Decor/Crux" | prepend: site.baseurl }})
  -- An example of the sawfish crux theme only uses two images along with
  gradients and colorsets. This is a nice write up of mixing the different
  styles together.


