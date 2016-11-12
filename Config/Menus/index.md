---
layout : wiki
title : Menus
type : config
weight : 700
description : |
  Fvwm can use Menus for lots of things. Menus items can run any
  Fvwm command or custom functions. They can even be built dynamically
  with scripts, such as wall paper menus, a menu that allows you to
  see all files in $HOME, etc. This is the basics of configuring
  Menus.

---
* TOC
{:toc}

Menus
=====

Menus are lists you can pop up from a binding or hook it to a start menu
on a panel. Menus can be used to list programs or even be created dynamically
so you can list the contents of a directory, a recent applications menu,
etc.

## MenuStyles

MenuStyles are similar to [/Config/Styles]({{ "/Config/Styles" | prepend: site.baseurl }})
and can be used with wild cards '\*' to set up the style so all your menus look the same
or can be used to make different menus use different MenuStyles.

An example of some MenuStyles from the default config is

{% highlight fvwm %}
# MenuStyles
MenuStyle * MenuColorset 5, ActiveColorset 6, GreyedColorset 7, TitleColorset 8
MenuStyle * Hilight3DOff, HilightBack, HilightTitleBack, SeparatorsLong
MenuStyle * TrianglesSolid, TrianglesUseFore
MenuStyle * ItemFormat "%|%3.1i%5.3l%5.3>%|"
MenuStyle * Font "xft:Sans:Bold:size=8:antialias=True"
{% endhighlight %}


Refer to the [manpage](http://fvwm.org/documentation/manpages/fvwm.html#lbBO)
for a descriptoin of what each option does.
If you want different menus to look and act differentially you can replace '\*' with the
menu name your interested. For example you could use

{% highlight fvwm %}
MenuStyle FvwmMenu* ...
MenuStyle MyMenu* ...
{% endhighlight %}

...to have two separate looking menus, menus with names
starting with FvwmMenu and names starting with MyMenu.

## Creating Menus

Now that we have set the MenuStyles, its time to build some menus.
Building menus is quite similar to building functions, you first should destroy the
previous menu and then add items to the menu in the order you want them to appear.
A basic root menu could look like this

{% highlight fvwm %}
# Root Menu
DestroyMenu MenuFvwmRoot
AddToMenu   MenuFvwmRoot "Fvwm" Title
+ "&Programs%icons/programs.png%" Popup MenuPrograms
+ "XDG &Menu%icons/apps.png%" Popup XDGMenu
+ "&XTerm%icons/terminal.png%" Exec exec xterm
+ "" Nop
+ "Fvwm&Console%icons/terminal.png%" Module FvwmConsole -terminal xterm
+ "&Wallpapers%icons/wallpaper.png%" Popup BGMenu
+ "M&an Pages%icons/help.png%" Popup MenuFvwmManPages
+ "" Nop
+ "Re&fresh%icons/refresh.png%" Refresh
+ "&Restart%icons/restart.png%" Restart
+ "&Quit%icons/quit.png%" Module FvwmScript FvwmScript-ConfirmQuit
{% endhighlight %}

The basic menu item format is

    "[item name]%[icon]%" [command]

...the + just applies the item to the previous AddToMenu statement. It doesn't matter
if the icon comes before or after the name, for example '"%[icon]%[item name]" [commands]'
will have the same effect. If you use \*..\* instead of %..% the icon will
appear above the menu item instead of to the right. The & symbol sets the
hot key that can be used to trigger that items command. Additionally, you can use multiple
icons and adjust where they appear in the menu with MenuStyle * ItemFormat.

This menu can then be opened by using the Menu command. For example
you could bind this menu to open when you click on the root window as follows:

{% highlight fvwm %}
Mouse 1 R A Menu MenuFvwmRoot
{% endhighlight %}

Each item's command can be triggered by selecting it with a mouse click,
moving around the menu with the arrow keys and using enter, or using the hot key
defined by the & string in the above example.

Menu items can Popup new menus, run programs, custom functions. One can also create
a menu of window operations. For example I have the following list of menu of
window operations that opens when I right click the desktop or a window title bar.

{% highlight fvwm %}
DestroyMenu MenuWindowOpsLong
AddToMenu   MenuWindowOpsLong
+ "Move"                Move
+ "Resize"              Resize
+ "(De)Iconify"         Iconify
+ "(Un)Maximize"        Maximize
+ "(Un)Shade"           WindowShade
+ "(Un)Sticky"          Stick
+ "" Nop
+ "Close"               Close
+ "Destroy"             Destroy
+ "" Nop
+ "Raise"               Raise
+ "Lower"               Lower
+ "" Nop
+ "StaysOnTop"          Pick (CirculateHit) Layer 0 6
+ "StaysPut"            Pick (CirculateHit) Layer 0 4
+ "StaysOnBottom"       Pick (CirculateHit) Layer 0 2
+ "" Nop
+ "Identify"            Module FvwmIdent
{% endhighlight %}

## Automatic Menu Generation

