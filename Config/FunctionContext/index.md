---
layout : wiki
title : FunctionContext
type : function
weight : 900
description : |
  Functions are usually run in the context of the window in which
  they were run, but not always. Here are some pointers for ensuring
  commands are run in the correct context.

---
* TOC
{:toc}

# Function Context

## Introduction

Under most circumstances, functions tend to be invoked within a window context.
That means the set of commands within the function operate on a window.  More
importantly, the context it runs under goes as far as to dictate the window at
the time the function was invoked.

It's not enough to assume that because a window has the focus at the time of a
function being called, that the window with the focus is the operand window.
So for example, suppose you had a function that, when invoked, echoed the name of
that window to FVWM's logfile (typically ''~/.xsession-errors'')


{% highlight fvwm %}
DestroyFunc FuncDisplayName
AddToFunc   FuncDisplayName
+ I Echo $[w.name]
{% endhighlight %}

If you had for example ''FocusFollowsMouse'' (which is the same as
''MouseFocus'') as the default focus policy, and you had the root-window
"focused", then tried invoking ''!FuncDisplayName'', you'd realise that in the
logfile you'd see:

{% highlight fvwm %}
$[w.name]
{% endhighlight %}

... instead of the actual window name.  This is because the function is being
called outside of a window context -- it doesn't have an operand point to
start from.  And as the Echo command doesn't require one, it just prints what
it has been told verbatim.

The same things can happen when functions are called from a menu.  Hence:


{% highlight fvwm %}
DestroyMenu MenuSomeMenu
AddToMenu   MenuSomeMenu CallMyFunction FuncDisplayName
    
Popup MenuSomeMenu
{% endhighlight %}

The function (if invoked outside of a window context) would be trying to call
a function itself not in a window context.

You will also see various references to ThisWindow.  ''ThisWindow'' operates
on a given window with set conditions.  By default it is not necessarily the
window that has the focus.  But it can be applied to windows which do.  So
for instance, the use of ThisWindow is useful when using FvwmEvent on
add\_window or configure\_window events, where the window(s) you want to use do not have the focus.

## Solvability

Ensuring commands or functions run within the intended context can be achieved
in a few ways.  In the case of the example ''!FuncDisplayName'' the use of
Current to force the window with the focus can be used to imply a window
context, hence:


{% highlight fvwm %}
DestroyFunc FuncDisplayName
AddToFunc   FuncDisplayName
+ I Current Echo $[w.name]
{% endhighlight %}

But what if there were more commands in the function than just a simple Echo
statement, such as:

{% highlight fvwm %}
DestroyFunc FuncDisplayName
AddToFunc   FuncDisplayName
+ I Current Echo $[w.name]
+ I Raise
+ I Move
{% endhighlight %}

At each statement, the commands Raise and Move would need a given context.
You could prepend Current in front of them, however, doing so could be
considered counter-productive.   What if you didn't always want the current
focused window to be the window to receive the function's attention?

This is where the Pick command comes in useful.  That will force a context on
a command or function if it isn't already running in one.  If it is, then it
runs normally.  This is especially useful where (in the case of the
!FuncDisplayName above) there's lots of commands each themselves requiring some
form of context.  Hence:

{% highlight fvwm %}
Pick FuncDisplayName
{% endhighlight %}
