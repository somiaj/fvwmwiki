---
layout : wiki
title : Pages and Desks
type : config
weight : 470
description : |
  Fvwm supports multiple Virtual Desktops. And more you can also
  split each Desktop up into an nxm grid of Pages.

---

# Virtual Desktops

Fvwm supports multiple Desktops. The default desktop is 0 and there
is no set cap on the number of desktops you can use. Desktops are
available on demand and can be moved between using the GotoDesk
command (note MoveToDesk, for windows, as the same syntax).

GotoDesk can be configured to go to a specific Desk or just cycle
through them. Here are some examples:

{% highlight fvwm %}
# GotoDesk [step] [min] [max]
# One Desk forward, max of 6
GotoDesk 1 0 6
# One desk backwards min of 0
GotoDesk -1 0 6

# GotoDesk [relative] [absolute]
# GotoDesk 5
GotoDesk 0 5
# GotoDesk 2
GotoDesk 0 2
{% endhighlight %}

Additionally Desktops can be given names with:

{% highlight fvwm %}
DesktopName 0 Main
DesktopName 1 Web
...
{% endhighlight %}

# Pages

Each Desktop can be further split into a grid of Pages, where one
Page is the size of your viewport (monitor) and you can move around
the Pages as if you had a bigger screen, but only see one portion of it.

Here is an example to configure Pages:

{% highlight fvwm %}
# 4 Desktops split into a 3x2 Grid
#   +---+---+---+
#   |0 0|1 0|2 0|
#   +---+---+---+
#   |0 1|1 1|2 1|
#   +---+---+---+
DesktopSize 3x2
{% endhighlight %}

That will give you a grid of 3x2 Pages where the numbers
are the x and y coordinates of each page. You can move through
the pages using the GotoPage (and MoveToPage for windows) in a similar
fashion to GotoDesk above.

In addition to just moving through the page you can scroll or only move part
way between two pages. You can also set up functions that will automatically
move you between pages when your mouse hits the edge of the screen. For example:

{% highlight fvwm %}
# EdgeScroll Xpercent Ypercent
# EdgeResistance - Timer before scrolling
# EdgeThickness - size of border for mouse around edge of screen
# Styles for dragging windows over the boundaries.
#
# Set EdgeScroll 0 0 and/or EdgeResistance -1 to disable.
EdgeScroll 100 100
EdgeResistance 450
EdgeThickness 1
Style * EdgeMoveDelay 350, EdgeMoveResistance 350
{% endhighlight %}

Additionally you can move around with

{% highlight fvwm %}
GotoDeskAndPage desk Xpage yPage
{% endhighlight %}

Or use [/Modules/FvwmPager]({{ "/Modules/FvwmPager" | prepend: site.baseurl }})
to give a miniature view of your Desks, Pages and Windows.

