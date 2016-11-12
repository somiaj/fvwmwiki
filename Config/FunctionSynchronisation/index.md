---
layout : wiki
title : FunctionsSynchronisation
type : function
weight : 800
description : |
  This page describes how to ensure functions
  finish a command before running the next.

---
* TOC
{:toc}

# Function Synchronisation 

## Introduction
In the #fvwm IrcChannel I (ThomasAdam) quite often see people asking
questions along the lines of "Why are my commands in FuncSomeFunc not
loading in the order I list them."   The answer to this is relatively
straight-forward once one understands what's happening within a
[/Config/ComplexFunction]({{ "/Config/ComplexFunction" | prepend: site.baseurl}}).

## Walkthrough Example

Let's take an example.  Note that all of these examples have to assume an
[I]mmediate context, that is commands that run as soon as the function
is called.

{% highlight fvwm %}
DestroyFunc FuncMyFunction
AddToFunc   FuncMyFunction
+ I Exec exec firefox
+ I Exec exec xterm -name myTerminal -iconic 
+ I Exec exec xteddy -wm
{% endhighlight %}

When FVWM is told to look at this function it does what it's told to
-- it will read it line-by-line and, in this case, exec those commands one
after the other.  This is generally fine, and most commands as listed in order
will start up in that order.

However, note that some of the commands have a certain latency about them.
Hence it is perfectly feasible for xterm and even XTeddy to have loaded before
Firefox does.

## Synchronising Commands

If making commands run one after the other is important then there's a few
ways one can ensure this (with varying degrees of difficulty).  In the case of
the FuncMyFunction example, all of those commands produce ("map" to use
Xlib parlance) windows, hence FVWM can be told to wait for their presence as
in:

{% highlight fvwm %}
DestroyFunc FuncMyFunction
AddToFunc   FuncMyFunction
+ I Exec exec firefox
+ I Wait firefox
+ I Exec exec xterm -name myTerminal -iconic
+ I Wait myTerminal
+ I Exec exec xteddy -wm
+ I Wait xteddy
{% endhighlight %}

What this does is ensure that all processing stops until the specified window
appears.  Note that this *is* order dependant now.  When the function
executes it will exec Firefox and then wait for that window matching "firefox"
to appear, either solely as the window's title, class, or resource in that
order.  If no window appears, then FVWM will hang, in which case the key
combination Ctrl-Alt-Esc can be used to break out of that deadlock.

The above is all very well, but there are some commands which don't produce
any windows, and so trying to use the Wait command is not going to be of much
help.  Luckily there is some other alternatives that can be used.

In FVWM 2.5.X, the Schedule command can be used to delay execution of a
command in milliseconds.   This is a non-blocking way of waiting for commands
to run, and can crudely help in assuring that some commands run in order.  To
take another example, assume the following function definition:


{% highlight fvwm %}
DestroyFunc SomeExampleFunction
AddToFunc   SomeExampleFunction
+ I Exec exec firefox
+ I Schedule 4000 Exec exec xterm -name myTerminal -iconic
+ I Schedule 5000 Exec exec xteddy -wm
{% endhighlight %}

Here, FVWM will read the function as it did before, and will start Firefox
immediately.  It will then come across the two Schedule commands and wait four
and five seconds respectively before executing those commands.  This doesn't
block and so FVWM will then carry on doing whatever else it is told to do.

An alternative method needed for older versions of Fvwm (2.4.X) was use
sleep in a shell something like this:

{% highlight fvwm %}
DestroyFunc SomeExampleFunction
AddToFunc   SomeExampleFunction
+ I Exec exec firefox
+ I Exec exec sleep 4s && exec xterm -name myTerminal -iconic
+ I Exec exec sleep 5s && xteddy -wm
{% endhighlight %}

This the above takes place at the shell level, however there is no blocking on
the commands as there would be when using the Wait command.

To ensure blocking synchronisation for commands that produce no windows, one
would then have to use PipeRead, since FVWM blocks until the PipeRead
processes has finished its processing.  As a very silly example:

{% highlight fvwm %}
DestroyFunc SomeExampleFunction
AddToFunc   SomeExampleFunction
+ I Exec exec firefox
+ I PipeRead `sleep 4s && echo "Exec xterm -name myTerminal -iconic"`
+ I Exec exec sleep 5s && xteddy -wm
{% endhighlight %}

