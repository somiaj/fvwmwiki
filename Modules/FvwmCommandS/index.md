---
layout : wiki
title : FvwmCommandS
type : module
weight : 300
description : |
  This is a server that runs in the background allow you to issue commands
  to fvwm via FvwmCommand on the command line (say inside a terminal like
  xterm).
---
* TOC
{:toc}

# FvwmCommand

## Description

FvwmCommand lets you monitor fvwm transaction and issue fvwm commands
from a shell command line or scripts. FvwmCommand takes each argument
as a fvwm command. Quotes can be used to send commands including
spaces. FvwmCommand 'FvwmPager 0 1'

## Configuration and Use

The only configuration needed is to run the server FvwmCommandS from your
config file. One such way is to do this when FVWM starts with:

{% highlight fvwm %}
AddToFunc StartFunction I Module FvwmCommandS
{% endhighlight %}

Once the server is running you can issue commands to fvwm from the command
line in your terminals or from scripts. To do so just run

{% highlight shell %}
FvwmCommand "Command"
{% endhighlight %}

