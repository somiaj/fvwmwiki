---
layout : wiki
title : Panels/Docks
type : main
weight : 700
description : |
  Panels/Docks are a broad term for various control panels, launchers,
  information displays, etc that are usually always visible -- such
  as a taskbar or pager. Fvwm provides various modules to help build
  panels. This can also be mixed with third party software or even
  use a third party panel.

---
* TOC
{:toc}

# Panels and Docks

Like everything else in Fvwm these need to be configured. Fvwm provides
lots of choice of how to configure the panels you want to use.

First Fvwm provides many Modules that can be used to build panels:
+ [FvwmButtons]({{ "/Modules/FvwmButtons" | prepend: site.baseurl }})
  -- This is one of the main panel building modules that lays out
  a panel into a series of buttons which can each be configured to be
  anything from text/icons to swallowing other applications.
+ [FvwmIconMan]({{ "/Modules/FvwmIconMan" | prepend: site.baseurl }})
  -- This is a list of running applications that can be used to control
  them, the main part of a taskbar for example.
+ [FvwmPager]({{ "/Modules/FvwmPager" | prepend: site.baseurl }})
  -- This module gives a graphical representation of the virtual
  [Pages and Desks]({{ "/Config/PagesAndDesks" | prepend: site.baseurl }}).

In addition to just Fvwm Modules, there is additional third party software
that can be used in panels, such as:
+ Stalonetray or Trayer -- Systemtrays
+ xmem -- Memory/Swap monitor that can be swallowed in FvwmButtons.
+ xosview -- system monitor(s) that can be swallowed in FvwmButtons.

There are also third party panels/docks that maybe already configured
and used with Fvwm. Some examples are
+ tint2 -- Customizable panel
+ rox-panel -- Customizable panel
+ cario-dock -- Customizable dock
+ pypanel -- Customizable panel in python
+ conky -- Customizable sensors
+ gkrellm -- Customizable sensors

## Example Panels

Here is the list of example panels:

{% assign pages = site.pages | where:"type","panel" | sort:"weight" %}
{% for mypage in pages reversed %}
  <p class="title-indent">
  <a href="{{ mypage.url | prepend: site.baseurl }}">
  {{ mypage.url | remove: "Panels" | remove: "/" }}</a><br>
  {{ mypage.description }}
  </p>
{% endfor %}
