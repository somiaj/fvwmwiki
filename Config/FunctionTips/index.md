---
layout : wiki
title : FuncitonTips
type : function
weight : 700
description : |
  Functions are usually run in the context of the window in which
  they were run, but not always. Here are some pointers for ensuring
  commands are run in the correct context.

---
* TOC
{:toc}

# Function tips

## Introduction

Writing [/Config/ComplexFunctions]({{ "/Config/ComplexFunctions" | prepend: site.baseurl }})
is not always that easy.  Indeed, one of the biggest problems tends to be the sequencing
of events -- and knowing when it is appropriate to specify any conditional
commands.

It has become more and more apparent to me (ThomasAdam) that people are
writing functions to do some very clever things, without really thinking
their logic through.   This has lead to all sorts of interesting
situations.   Because FVWM can be "scripted", that doesn't mean to say
that a task ''should'' be done that way.  :)

## An Example

Let's take an example.  Let's suppose we want to write a function that
moves a specific window to the top-right corner of the screen as soon as
it appears on screen.  Sounds simple enough, right?  First thing we have
to solve is how we're going to do that.  FvwmEvent allows for certain
actions to be listened for, and actioned upon where appropriate.  It's a
very useful module, and when writing functions that depend on them, can be
invaluable.  

## Thinking it through

In this specific case, we can use the add\_window event which will fire
off as soon as a window is made to appear (mapped) on the screen.  We can
tell it to call a function, the name of which we'll call MoveWindow,
hence:

{% highlight fvwm %}
DestroyModuleConfig FE-movewindow:*
*Fe-movewindow: Cmd Function
*FE-movewindow: add_window MoveWindow

Module FvwmEvent FE-movewindow
{% endhighlight %}

Sets up the listener that will call the function.  Our function might
first of all look like this:

{% highlight fvwm %}
DestroyFunc MoveWindow
AddToFunc   MoveWindow
+ I AnimatedMove -0 +0
{% endhighlight %}

Try it -- open a window.  Works fine, doesn't it?  As it should do -- the
function is being called in an adequate context already.  However, there
are going to be specific times when this isn't always going to be the
case.  And more to the point, how do we further go on to disclude certain
windows from having this function operating on them in the first place?
Welcome to the use of conditional commands.

## Current, ThisWindow, etc.

[/Config/FunctionContext]({{ "/Config/FunctionContext" | prepend: site.baseurl }})
is everything when it comes to operating on windows.  Indeed, ensuring a
functions runs within a window context is tricker than many think.  In continuing
with our example though, we'll soon see that we need be specific.   What do we
do when need to specify a specific window to be moved, and to ignore all others?
This is where the [/Config/Conditionals]({{ "/Config/Conditionals" | prepend: site.baseurl }})
command ThisWindow comes in useful.

ThisWindow is a command more or less guaranteed to place a window within a
given context.  So if you're ever unsure if the function is going to work
without it -- but you always want to force a window context, use it.
Hence:

{% highlight fvwm %}
DestroyFunc MoveWindow
AddToFunc   MoveWindow
+ I ThisWindow AnimatedMove -0 +0
{% endhighlight %}

And indeed, using ThisWindow to help specify a window name (to match
against) is also a pretty good bet.  One thing ThisWindow as a conditional
command is good at, is providing context without any additional
constraints (i.e. it will pretty much operate on a window, regardless).
Compare of course, the following function instead:

{% highlight fvwm %}
DestroyFunc MoveWindow
AddToFunc   MoveWindow
+ I Current AnimatedMove -0 +0
{% endhighlight %}

Looks innocent enough, right?  The problem here though is that if one
already has a window focused, it's that window which is moved, and not the
window that has just appeared.  This is because ''Current'' has a hidden
and assumed prerequisite --- it implies the current window that has the
focus.  Very useful under certain conditions (when you definitely know
that you want to operate on the currently focused window), but in our
situation, we don't want or need it, so we'll discard it.  And indeed, it
might not always be the case that the operand windows will have focus.

So definitely ThisWindow.  Luckily, like all conditional commands, we
can make specific requirements as to the windows they operate on.  So,
let's expand our function to say that we only want rxvt windows to be
moved to the top-right:

{% highlight fvwm %}
DestroyFunc MoveWindow
AddToFunc   MoveWindow
+ I ThisWindow (rxvt) AnimatedMove -0 +0
{% endhighlight %}

This function can of course be expanded further.

## Conclusion

So, when you're writing a function, consider:

* Context is everything.  If you're unsure, use !ThisWindow to force a context.
* Current isn't always the best context to use, since it initially implies the
  focused window (which will fail if there aren't any focused windows).

