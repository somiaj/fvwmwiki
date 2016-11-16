---
layout : wiki
title : Decor
type : main
weight : 600
description : |
  Information about how to decorate your windows.

---
# FVWM Decors

A Decor is a collection of configurations for the looks of the windows.
These pages are a collection of example decors that can be used in your
setup. Most of these decors were adopted from
[fvwm-themes](http://fvwm-themes.sourceforge.net) and are available here
as examples along with the images with any images needed.

These are only examples, for a description of a decor see
[/Config/Decor]({{ "/Config/Decor" | prepend: site.baseurl }})

## Decors

{% assign pages = site.pages | where:"type","decor" | sort:"weight" %}
{% for mypage in pages reversed %}
  <p class="title-indent">
  <a href="{{ mypage.url | prepend: site.baseurl }}">
  {{ mypage.url | remove: "Decor" | remove: "/" }}</a><br>
  {{ mypage.description }}
  </p>
{% endfor %}
