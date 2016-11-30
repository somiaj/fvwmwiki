---
layout : wiki
title : Window Ops Menu
type : menu
weight : 500
description : |
  This menu is just a collection of actions (Maximize, Iconify,
  Close, etc) that can be used to control windows.

---
* TOC
{:toc}

# WindowOps Menu

These are a collection of Menus that can be used to control windows.
The menus can be accessed from a root menu in which you have to select
the window to operate on. They can also be bound to window buttons or
FvwmIconMan buttons and operate directly on the selected window.

## Default Config

Here are the WindowOps menus from the [DefaultConfig](
{{ "/DefaultConfig" | prepend: site.baseurl }}). The different variations
of the Menu are used for different bindings. A small menu which opens up
if you click the Menu button on a window, a longer form from a right click
on the root window and a modified form for icons and FvwmIconMan.

{% highlight fvwm %}
DestroyMenu MenuWindowOps
AddToMenu   MenuWindowOps
+ "Move"      Move
+ "Resize"    Resize
+ "Iconify"   Iconify
+ "Maximize"  Maximize
+ "Shade"     WindowShade
+ "Stick"     Stick
+ "" Nop
+ "Close"     Close
+ "More..."   Menu MenuWindowOpsLong This 0 0

DestroyMenu MenuWindowOpsLong
AddToMenu   MenuWindowOpsLong
+ "Move"                Move
+ "Resize"              Resize
+ "(De)Iconify"         Iconify
+ "(Un)Maximize"        Maximize
+ "(Un)Shade"           WindowShade
+ "(Un)Sticky"		Stick
+ "(No)TitleBar"	Pick (CirculateHit) ToggleTitle
+ "Send To Desk"        Popup MenuSendToDesk
+ "" Nop
+ "Close"               Close
+ "Destroy"             Destroy
+ "" Nop
+ "Raise"		Raise
+ "Lower"		Lower
+ "" Nop
+ "StaysOnTop"          Pick (CirculateHit) Layer 0 6
+ "StaysPut"            Pick (CirculateHit) Layer 0 4
+ "StaysOnBottom"       Pick (CirculateHit) Layer 0 2
+ "" Nop
+ "Identify"            Module FvwmIdent

DestroyMenu MenuIconOps
AddToMenu   MenuIconOps
+ "(De)Iconify"         Iconify
+ "(Un)Maximize"        Maximize
+ "(Un)Shade"           WindowShade
+ "(Un)Sticky"		Stick
+ "(No)TitleBar"	Pick (CirculateHit) ToggleTitle
+ "Send To Desk"        Popup MenuSendToDesk
+ "" Nop
+ "Close"               Close
+ "Destroy"             Destroy
+ "" Nop
+ "Raise"		Raise
+ "Lower"		Lower
+ "" Nop
+ "StaysOnTop"          Pick (CirculateHit) Layer 0 6
+ "StaysPut"            Pick (CirculateHit) Layer 0 4
+ "StaysOnBottom"       Pick (CirculateHit) Layer 0 2
+ "" Nop
+ "Identify"            Module FvwmIdent

DestroyMenu MenuSendToDesk
AddToMenu   MenuSendToDesk
+ "Current"	MoveToDesk
+ "Desk 0"	MoveToDesk 0 0
+ "Desk 1"	MoveToDesk 0 1
+ "Desk 2"	MoveToDesk 0 2
+ "Desk 3"	MoveToDesk 0 3
{% endhighlight %}

These Menus require the function ToggleTitle, which can be used
to show or hide the title bar of a menu. Additionally these
Menus are bound windows and FvwmIconMan as follows.

{% highlight fvwm %}
# Function: ToggleTitle
DestroyFunc ToggleTitle
AddToFunc   ToggleTitle
+ I ThisWindow (State 1) WindowStyle Title
+ I TestRc (Match) State 1 False
+ I TestRc (Match) Break
+ I WindowStyle !Title
+ I State 1 True
 
# Mouse Bindings
Mouse 1 1 A Menu MenuWindowOps
Mouse 3	R A Menu MenuWindowOpsLong
Mouse 3	T A Menu MenuWindowOps
Mouse 3 I A Menu MenuIconOps

# FvwmIconMan
*FvwmIconMan: Action Mouse 3 A sendcommand "Menu MenuIconOps"
{% endhighlight %}

## Dynamic WindowOps

Here is a variation of the WindowOps menu that is dynamic in the sense
it will put a checkmark near an option the window currently has.
You will first need a [checkmark](check.png) icon for the menu
in your [ImagePath]({{ "/Config/ImagePath" | prepend: site.baseurl }}).

Then a function to build the menu that uses [Conditionals](
{{ "/Config/Conditionals" | prepend: site.baseurl }}) to test for
the different window states and then put a checkmark next to
the states it finds.

{% highlight fvwm %}
DestroyFunc GenWindowOps
AddToFunc GenWindowOps
+ I AddToMenu DynamicWindowOps
+ I ThisWindow (Iconified) + "Iconify%check.png%" Iconify
+ I TestRc (NoMatch) + "Iconify" Iconify
+ I ThisWindow (Maximized) + "Maximize%check.png%" Maximize
+ I TestRc (NoMatch) + "Maximize" Maximize
+ I ThisWindow (Shaded) + "Shade%check.png%" WindowShade
+ I TestRc (NoMatch) + "Shade" WindowShade
+ I ThisWindow (Sticky) + "Stick%check.png%" Stick
+ I TestRc (NoMatch) + "Stick" Stick
+ I ThisWindow (State 1) + "TitleBar" ToggleTitle
+ I TestRc (NoMatch) + "TitleBar%check.png%" ToggleTitle
+ I + "" Nop
+ I ThisWindow (Layer 6) + "StaysOnTop%check.png%" Layer 0 4
+ I TestRc (NoMatch) + "StaysOnTop" Layer 0 6
+ I ThisWindow (Layer 4) + "StaysPut%check.png%" Nop
+ I TestRc (NoMatch) + "StaysPut" Layer 0 4
+ I ThisWindow (Layer 2) + "StaysOnBottom%check.png%" Layer 0 4
+ I TestRc (NoMatch) + "StaysOnBottom" Layer 0 2
{% endhighlight %}

Now that we have a function to build the menu, we need to configure
Fvwm to create the menu each time it is opened. To do this configure
the DynamicPopUpAction and DynamicPopDownAction as follows.

{% highlight fvwm %}
DestroyMenu DynamicWindowOps
AddToMenu DynamicWindowOps DynamicPopUpAction GenWindowOps
AddToMenu DynamicWindowOps DynamicPopDownAction \
          DestroyMenu recreate DynamicWindowOps
{% endhighlight %}

Last bind the menu to a window. For example a right click anywhere on
the title bar would be:

{% highlight fvwm %}
Mouse 3 T A Menu DynamicWindowOps
{% endhighlight %}


