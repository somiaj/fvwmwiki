---
layout : wiki
title : Decor
type : main
weight : 600
description : |
  Information about how to decorate your windows.

---
# FVWM Decors

Here is the list of Decors:

{% assign pages = site.pages | where:"type","decor" | sort:"weight" %}
{% for mypage in pages reversed %}
  <p class="title-indent">
  <a href="{{ mypage.url | prepend: site.baseurl }}">
  {{ mypage.url | remove: "Decor" | remove: "/" }}</a><br>
  {{ mypage.description }}
  </p>
{% endfor %}
