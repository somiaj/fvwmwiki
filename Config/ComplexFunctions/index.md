---
layout : wiki
title : ComplexFunctions
type : function
weight : 1000
description : |
  This page gives the basics about complex functions.

---
* TOC
{:toc}

# ComplexFunction

## Introduction

A Complex Function in FVWM is nothing more than a series of commands
grouped together to perform a given task.  How that function operates
depends entirely on how it was written and what [[FunctionContext]] it runs
in.  A function can have any number of commands, including builtin FVWM
commands, external commands, etc.

## Declarations of Functions

The formal declaration of a function is started with the AddToFunc
keyword, its syntax being:

{% highlight fvwm %}
AddToFunc [name [I | M | C | H | D action]]
{% endhighlight %}

To take an example, suppose we wanted to write a function (a useless one
in this context, but serves for demonstrative purposes) called !RaiseMe
which raises a window as soon as a function is called.  We would write:

{% highlight fvwm %}
AddToFunc RaiseMe I Raise
{% endhighlight %}

We might decide we want to bind that function to the titlebar of a window:

{% highlight fvwm %}
Mouse 1 T A RaiseMe
{% endhighlight %}

Such that when we then clicked on the titlebar with mouse button 1, the
window is raised.  Now let's assume in addition to that we wanted to (at
the same time), move the window to the previous page as well.

Since we have already declared the function !RaiseMe earlier on, we
could continue to add to its definition as in:

{% highlight fvwm %}
AddToFunc RaiseMe I MoveToPage prev
{% endhighlight %}

The point being here is that each time a new definition is added to the
function, the AddToFunc keyword does that, although it can be an issue at
times since it's somewhat harder to follow.   There is another way of
declaring functions, and that is to list each operation of it below a
single AddToFunc definition using the group operator *+*.

{% highlight fvwm %}
AddToFunc RaiseMe
+ I Raise
+ I MoveToPage prev
{% endhighlight %}

The plus operator just extends the definition of AddToFunc (but works in
the same way with AddToDecor and AddToMenu), effectively grouping the
elements after it together.

## Removal of Functions

It would be quite annoying if we could only ever continue adding to a
function without somehow being able to remove its definition.  Luckily
though, FVWM has the DestroyFunc command to do this:

{% highlight fvwm %}
DestroyFunc [name]
{% endhighlight %}

Hence:

{% highlight fvwm %}
DestroyFunc RaiseMe
{% endhighlight %}

...would make FVWM forget the definition of that function.

## Triggering actions from Functions

The astute will have noticed that the first parameter to a function is a
single letter.   Those letters define what part of the function runs,
depending on certain conditions, hence:


|Operator|Context|Meaning|
|:-------:|-------|-------|
| I | Immediate | Called when the function is invoked.|
| M | Motion | Called when an item is moved.|
| C | Click | Called when an item is clicked.|
| D | Double-click | Called when an item is double-clicked.|
| H | Hold | Called when an the pointer is held on an item.|
|---------|-------|-------|

Usually (although not always) "I" is used the most often, as it denotes
something to be done regardless of whether one is clicking on something,
or wanting to move an item, for instance.

"M" is useful if you want to have something happen when a window is moved.
This action is triggered as soon as the window starts to move, and can
sometimes conflict with "H" if it is used within the same function.  For
example, "M" is useful to, well, __move__ a window, since it might not be
an implicit operation.  "H" tends to be designated the same value as "M"
(and vice-versa) when they're used within the same function as it often
then means there's no ambiguity in the delay between the window moving,
and the button being held within the window.

"C" and "D" are useful to define actions for clicking on a window, or
parts of it.

Here's an example:  FuncMoveOrRaiseLower

{% highlight fvwm %}
DestroyFunc FuncMoveOrRaiseLower
AddToFunc   FuncMoveOrRaiseLower
+ H Move
+ M Move
+ C RaiseLower
{% endhighlight %}

... which says that when the function is called, if the mouse button is
either held or the window is invoked to be moved by the mouse button, then
the window moves, otherwise if there's a single-click instead, the then
the item is either Raised or Lowered, depending on what state it is in
before the click event occurs.

## Piecing the parts together

When writing functions it should perhaps be obvious then that removing a
function's definition before you define it (irrespective of whether it is
the fist time the function has been defined) is probably a good idea,
hence:

{% highlight fvwm %}
DestroyFunc myFunction
AddToFunc   myFunction
+ I ....
+ M ....
{% endhighlight %}

There is no agreed definition as to function naming conventions, other
than to choose something and try and be consistent in its use.  I
(ThomasAdam) like to use the prefix ''Func'' and then a descriptive name
about the function.   Like most things in FVWM, the actual name of the
function is read case-insensitive to FVWM although the use of !CamelCase as
a convention is quite popular.

## Function Inputs

When calling complex functions you can provide the function inputs
as a space separated list. Each input is stored as a variable
$0, $1, $2, ..., $9. Use $\[n\] to access a parameter bigger
than 9. Additionally you can use $\[n-m\], $\[n-\], $\* or $\[\*\]
for different collections of the input(s). For example

{% highlight fvwm %}
# Function: MoveClickX $0 $1 $2
#   $0 - Action on Mouse Hold + Move
#   $1 - Action on Mouse Click
#   $2 - Action on Mouse DoubleClick
#  Example: Mouse 1 T A MoveClickX Move Raise Maximize
DestroyFunc MoveClickX
AddToFunc MoveClickX
+ M $0
+ C $1
+ D $2
{% endhighlight %}

This function can then be bound to window buttons, title bars, etc
like

{% highlight fvwm %}
# Titlebar: Move or Raise on single click or Maximze on double
Mouse 1 T A MoveClickX Move Raise Maximize
{% endhighlight %}

## Function Caveats

I'm sure by now functions sound great -- and they are!  But like
everything, there's a few caveats to bear in mind with them.  During the
lifetime of a function (that is from the time it was invoked to the time
it ends), the pointer is grabbed.  What that means is that the mouse
pointer is under control of the XServer until it is released.  For most
things this won't matter much, and the user (that's you) won't be aware of
it.  However there is some programs (such as ''import'') which need the
pointer to actively workout what screenshot it is going to take.  This
won't therefore work the way it's intended from within a function such as:

{% highlight fvwm %}
+ I Exec exec import -window root ...
{% endhighlight %}

To alleviate such problems, one would have to use PipeRead to fork off a
new process (away from the function).

Synchronisation is another important issue within function execution.  To
take an example, suppose you have the following function that performs a
series of operations:

{% highlight fvwm %}
DestroyFunc FuncSomeFunction
AddToFunc   FuncSomeFunction
+ I Raise
+ I AnimatedMove 500 300
+ I Lower
{% endhighlight %}

You might expect these commands to run one after the other.  They do,
although there are times when that might not always be the case.  FVWM
performs no [/Config/FunctionSynchronisation](
{{ "/Config/FunctionSynchronisation" | prepend: site.baseurl }})
as to the ordering of the commands -- or rather it makes no guarantees.
If a strict set of synchronised commands is needed, it is recommended to
use PipeRead -- since FVWM will wait for the PipeRead to return before
carrying on with the rest of its input (such as the other commands in the
function).

