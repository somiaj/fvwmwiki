---
layout : wiki
title : Irc
type : main
weight : 300
description : |
  #fvwm on irc.freenode.net has been a gathering place for Fvwm users.
  Here is the channel FAQ and a few conversations that occurred on irc.

---

# \#fvwm on irc.freenode.net

## HashFvwmFAQ

[/Irc/HashFvwmFAQ]({{ "/Irc/HashFvwmFAQ" | prepend: site.baseurl }})
is an FAQ created by users of #fvwm.

## Conversations

Here are the list of conversations:

{% assign pages = site.pages | where:"type","irc" | sort:"weight" %}
{% for mypage in pages reversed %}
  <p class="title-indent">
  <a href="{{ mypage.url | prepend: site.baseurl }}">
  {{ mypage.url | remove: "Irc" | remove: "/" }}</a><br>
  {{ mypage.description }}
  </p>
{% endfor %}
