---
layout : wiki
title : Modules
type : main
weight : 700
description : |
  Fvwm has various modules that can be used to create custom panels,
  docks, task managers, desktop switchers and more. These are a collection
  of pages describing the different modules in Fvwm.

---

# FVWM Modules

Here is the list of modules:

{% assign pages = site.pages | where:"type","module" | sort:"weight" %}
{% for mypage in pages reversed %}
  <p class="title-indent">
  <a href="{{ mypage.url | prepend: site.baseurl }}">
  {{ mypage.url | remove: "Modules" | remove: "/" }}</a><br>
  {{ mypage.description }}
  </p>
{% endfor %}
