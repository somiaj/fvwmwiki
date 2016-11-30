---
layout : wiki
title : FvwmIconMan
type : module
weight : 500
description : |
  FvwmIconMan provides a list of running applications. You can run one or
  multiple managers and they can be configured to display different
  collections of windows.

---
* TOC
{:toc}

# FvwmIconMan

## Module Description

The FvwmIconMan module provides a grid of Icons (Buttons) that represent
the running windows on the system. FvwmIconMan can be configured to
display different collections of windows and the buttons provides an
interface to interact with the widows, such as giving them Focus
to Iconify them.

## Example Configuration

Here is an example configuration which lists running windows in a
vertical list whose window grows and shrinks with the number of running
apps. Below is a brief description of what the various parts configure.
For a full list of options see the [FvwmIconMan manpage](
http://fvwm.org/documentation/manpages/FvwmIconMan.html).

{% highlight fvwm %}
DestroyModuleConfig FvwmIconMan: *
*FvwmIconMan: UseWinList true
*FvwmIconMan: Resolution global
*FvwmIconMan: Tips needed
*FvwmIconMan: Sort id

# Manager Size
*FvwmIconMan: ButtonGeometry 120x20
*FvwmIconMan: ManagerGeometry 1x0-5+260

# Button Styles
*FvwmIconMan: Colorset 10
*FvwmIconMan: FocusColorset 11
*FvwmIconMan: SelectColorset 12
*FvwmIconMan: FocusAndSelectColorset 12
*FvwmIconMan: IconColorset 14
*FvwmIconMan: IconAndSelectColorset 15
*FvwmIconMan: DrawIcons always
*FvwmIconMan: ReliefThickness 0
*FvwmIconMan: Format "%t"
*FvwmIconMan: Font "xft:Sans:Bold:size=8:antialias=True"

# Button Actions
*FvwmIconMan: Action Mouse 0 N sendcommand Nop
*FvwmIconMan: Action Mouse 1 A sendcommand IconManClick
*FvwmIconMan: Action Mouse 3 A sendcommand "Menu MenuIconOps"
{% endhighlight %}

+ Here the first few options set some basics about which windows to show.
  UseWinList honors the WinListSkip style, Otherwise all windows will be
  shown. The options Show and DontShown can be further used to control
  which windows are included.

  Other True/False options that can be turned on to control the included
  windows are ShowOnlyIcons, ShowNoIcons, ShowTransient, ShowOnlyFocused.

+ Tips configures tool tips which will give the full window name. In this
  case only for windows whose window name is longer than the button or
  as needed.

+ Short will short this list in this case by the window id. You can also
  set up Weights for windows to better control the sort order.
  

### Manager Size

The manager can be configured to be a fixed size, or to grow and shrink
as windows are added and removed. The size and this behavior can be configured
through a combination of:

+ ButtonGeometry XxY: Sets the size of each button in pixels. If the height
  is 0, the font height will be used.

+ ManagerGeometry NxM+X+Y: Sets the size of the manager in terms of number
  of columns (N) and rows (M) of buttons. So the actual size is then also
  based on ButtonGeometry.

  If either of the number of columns or rows are zero, the manager will
  grow and shrink in the direction associated with the zero.

  If the columns and rows are both non zero, the manager will be that
  fixed size and not grow/shrink.

  Note: If swallowing FvwmIconMan in
  [FvwmButtons]({{ "/Modules/FvwmButtons" | prepend: site.baseurl }})
  and FvwmIconMan is configured to grow/shrink, it will grow beyond
  the boundary of the Button if there are enough windows in the list.

+ MaxButtonWidth/MaxButtonWidthByColumns: By default the buttons width
  will grow/shrink to fit when listing them horizontally. These will
  set the max width in either pixels or total number of columns.

### Button Styles

The buttons in the list can have different styles (colorset/relief effect)
depending on if they have Focus, are Iconified or are Selected (by the
mouse or keyboard in the manager) and the various combinations of these.

There are two related options to set these. For example for the Selected
button you could use

{% highlight fvwm %}
*FvwmIconMan: SelectButton style forecolor backcolor
*FvwmIconMan: SelectColorset colorset
{% endhighlight %}

Style is one of flat, up, down, raisededge or sunkedge and the forecolor
and backcolor set the respective color. The color settings are optional
and additionally you can set Colorset of the button, but still have to
use SelectButton to set the style.

The list of different combinations are

    PlainButton/PlainColorset, SelectButton/SelectColorset,
    FocusButton/FocusColorset, IconButton/IconColorset,
    FocusAndSelectButton/FocusAndSelectColorset,
    IconAndSelectButton/IconAndSelectColorset,
    TitleButton/TitleClorset

In addition to configuring the different button types, some other settings
related to the style of the buttons are

+ DrawIcons true/false/always: Sets if mini icons are included on the button.
  true will only show mini icons for Iconified windows, while always shows
  them for all windows.

+ Format and Font control what the title of the button is such as window
  name, etc.

+ ReliefThickness sets the thickness in pixles of the 3D relief border.

+ Colorset, Foreground, Backgound will set the default colors.

  Note: Due to a bug in 2.6.7, the background of the manager which
  has no buttons on it will not honor the Colorset setting. Use
  Foreground and Background instead and PlainColorset to control
  the default button colorset.

### Button Actions

FvwmIconMan can have actions bound to the buttons via Mouse or Key
bindings. These can be configured to control what happens when a
selected button is clicked on to how to move through and control
the buttons with a keyboard.

The basic configuration settings are

{% highlight fvwm %}
*FvwmIconMan: Action Mouse Button Modifier Command
*FvwmIconMan: Action Key Key Modifier Command
{% endhighlight %}

Here command are commands for FvwmIcon man. See the man page for a full
list. The ones used in the example use sendcommand which will send
the command to Fvwm to act on the selected window.

The default is to Iconify the window no matter what mouse button is pressed,
which can be disabled with

{% highlight fvwm %}
*FvwmIconMan: Action Mouse 0 N sendcommand Nop
{% endhighlight %}

The other actions then bind a custom Iconfiy like function to a left click
and opens a [Window Operations Menu](
{{ "/Menus/WindowOps" | prepend: site.baseurl }}) when right clicked to
preform various operations.

The custom function used, which will bring make a window Visable if it is not,
and Iconify it otherwise is

{% highlight fvwm %}
DestroyFunc IconManClick
AddToFunc   IconManClick
+ I ThisWindow (Raised, !Shaded, !Iconic, CurrentPage) Iconify
+ I TestRc (Match) Break
+ I ThisWindow (!Raised) Raise
+ I ThisWindow (Shaded) WindowShade
+ I ThisWindow (Iconic) Iconify
+ I ThisWindow (AcceptsFocus) FlipFocus
{% endhighlight %}

