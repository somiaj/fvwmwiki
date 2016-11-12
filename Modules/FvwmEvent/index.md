---
layout : wiki
title : FvwmEvent
type : module
weight : 5
description : |
  FvwmEvent can be configured to trigger on specific events. When
  the event is triggered, the module can run any command.

---
* TOC
{:toc}

# FvwmEvent

*This page was originally written by Thomas Adam, and published in the          
[Linux Gazete](http://linuxgazette.net/127/adam1.html), June 2006.*   

**Note:** The example of maximizing when it is loaded via FvwmEvent can be
achieved with [InitialMapCommand](
{{ "/CookBook/InitialMapCommand" | prepend: site.baseurl }}).

## Introduction

Most window managers have some form of automation that allows the user to
'script' various aspects of its operation. Indeed, the 'kahakai'
[^1]:  http://kahakai.sourceforge.net/
window manager has long since defined Python as way of scripting its
capabilities.

In FVWM, there are a few ways of scripting events. The use of FvwmPerl is
one such way. However, in almost all cases, when people say they want to
define actions, what they're really after is some way of conditionally
checking windows when they're created, or something similar. The combination
of this ability coupled with a series of commands grouped together to form
what FVWM calls a function is something that can be quite powerful.

## What is FvwmEvent?

FvwmEvent is a module - a piece of code that is separate from the core of
FVWM. There are a lot of different modules in FVWM, all of which share that
important distinction; there's no point in loading extra code which might
never be used, or loading it on an ad-hoc basis where the user never
requested it.

FvwmEvent is a module which allows listening for various events, and acting
upon them when they occur. Originally it was known as FvwmAudio, since its
job was primarily in playing sounds when various things happened (such as a
window being closed, iconified, etc). FvwmEvent still retains that
functionality, but now also has the capability of running specific tasks
based on those events.

So what are these events? They're triggers associated with the operations of
windows (many of which are wrappers around various low-level Xlib library
calls). Whenever an event that FvwmEvent has been told to listen for occurs,
it will look for an associated action and execute it. A sample valid list of
events that FvwmEvent knows to listen for can be seen in its man page2. The
one this article will examine is *add_window* note that this is only a
working example, and should be thoroughly tested before using in production.

## FvwmEvent Example

A generic FvwmEvent configuration looks like the following (note that the
line numbers have been added as a convenient reference point, and are not
part of the configuration):

    1   DestroyModuleConfig FvwmEvent: *
    2   *FvwmEvent: <some_event_name> <some_action>
    3 
    4   Module FvwmEvent

The very first thing that happens is that the module config is destroyed
(Line 1). This might seem a little strange at first given that nothing has
been declared yet, but the point of it here is that for any previous
definitions of it (say via multiple parsings of one's '.fvwm2rc' file during
restarts), it gets destroyed and then recreated; otherwise, the module
definition would just be added to continuously - something that is most
undesirable. What follows next (line 2) is the start of the alias definition
that FvwmEvent will eventually read. Obviously <some_name> and <some_action>
are dependent on the event and the action required. <some_action> might be a
function, or a single command. Line 4 simply tells FVWM to load the
FvwmEvent module.

Note the concept of what's happening. Most modules have the concept of
aliases - that is, an identifier that the module can be told to use (in
earlier version of FVWM, in order for multiple aliases of a specific module
to be used, one had to symlink the alias name to the module). In the case of
the generic example above, that's using \*FvwmEvent which is fine until more
instances of FvwmEvent need to be loaded. It's permissible, of course, to
just   have one instance of FvwmEvent running and declare all the events it
will listen for in there.   The problem is that it's often desirable to run
different actions on the same event -   something you can't do with one
alias. So the heuristic approach is to define a unique alias   to FvwmEvent,
which isn't \*FvwmEvent. Any name can be used, as will become apparent.

        add_window event: maximising windows

This is perhaps the most common event people use when they consider running
commands on a window. This event is triggered whenever a window is mapped
(created) to the screen3. Perhaps one of the most common operations that
people wish to perform when this happens is maximizing a window. This has
been covered in part in the main FVWM FAQ4.  Of course, in encountering this
question, it is often the case that when people say 'maximised', they also
mean so-called 'full-screen' - which implies the removal of any title bars
and borders, and other such window decorations. That's fine, and can be
dealt with at a later stage, although the premise of maximisation has to be
discussed first of all.

It also seems to surprise many people that FVWM has no 'StartMaximised'
style option. The reason for this is that in introducing such an option it
would break the ICCCM5 - since clients set their own geometry, either by
themselves or via user interaction.

The first thing to be done is setting up FvwmEvent:

    DestroyModuleConfig FE-StartMaximised: *
    *FE-StartMaximised: Cmd Function
    *FE-StartMaximised: add_window StartAppMaximised
    
    Module FvwmEvent FE-StartMaximised

This tells FvwmEvent a few things. One is that the alias we're using for it
is \*FE-StartMaximised. Secondly, we've informed the module that the command
specified for the event is a function. Thirdly, the event we're listening
for is add\_window. Then the module is started.

The function we'll declare is quite simple to start off with (again, line
numbers are for point of reference only, and are not part of the syntax):

    1   DestroyFunc StartAppMaximised
    2   AddToFunc   StartAppMaximised
    3   + I Maximize

Line 1 destroys the previous function definition. It's generally a good idea
to do this when declaring functions, since it removes a previous definition
for it. Indeed, the AddToFunc command (line 2) is cumulative. Each time it
is used, it just adds to the definition of the function. If it doesn't
exist, the function is created. Quite often this cumulative nature isn't
wanted, so removing the definition beforehand is advised. Line 3 is the
important line since it is the line which defines the action for the
function.

One can define as many actions within a function as is necessary. There are
a few prefixes as well which define when and how those actions are to be
invoked:

[[!table data="""
Function Operators|Context|Meaning
I|Immediate|executed as soon as the function is called.
C|Click|executed when the mouse button is clicked once.
D|Double-click|executed when the mouse button is double-clicked.
M|Motion|executed when the mouse is moved.
H|Hold|executed when the mouse button is held down.
"""]]

Usually the most common operator is I for non-interactive functions, since
those commands will always get executed when the function is called. So
within this example, the command Maximize is run whenever a window is
created. Try it and see; start up an xterm. It will then be maximised. Start
up any application in fact, and all of those windows will be maximised.
Clearly this is suboptimal, but a start nevertheless.

## Function Context

So far, it's been shown how one can use FvwmEvent plus a function to define
actions for events. But there will be times in loading applications (which
produce windows mapped to the screen) when some windows won't get maximised.
The reason for this has to do with the context in which the function is
being run.

In most cases, functions are designed to run within a window context. This
means that, when they're run, it's known which window or windows the
function is to start operating from. Without the proper context, a function
will prompt for one, or not run at all. So it's important to ensure a
context is forced wherever it's not apparent.

One can achieve this is in a number of ways, and a lot of it depends upon
the situation the function is likely to be called in. Recall the definition
for StartAppMaximised - at the moment the line looks like:

    + I Maximize
 
This already assumes a window context. But one can always make sure by using
the   ThisWindow command, as in:

    + I ThisWindow Maximize

ThisWindow is extremely useful to refer to windows directly without implying
any   presumptions. Indeed, there are other conditional commands, such as
Current, which is quite a common way to imply context:

    + I Current Maximize

However, its use implies that the window already has focus. Sometimes this
is useful to refer to the specific window; however, in the case of the
StartAppMaximised function one cannot assume the operand windows will always
have the focus - hence, the use of ThisWindow is preferable. Where one is
unsure as to the operand window (i.e., it is to be decided when the function
runs), one can use the Pick command which will prompt for a   window to
operate on if it is not already known.

## Improving StartAppMaximised

Whilst the function does work, it needs improving. For a start, the function
is maximising every window that is created - this is clearly not something
likely to be desirable. One can conditionally place restrictions on
windows by matching against their name, class or resource by using any of
the conditional commands mentioned earlier:
 
    DestroyFunc StartAppMaximised 
    AddToFunc   StartAppMaximised 
    + I ThisWindow ("name of window") Maximize

What happens here is that only the window with the name 'name of window' is
considered. If it matches the window just created, then it is maximised;
otherwise, nothing happens. Of course, the maximize command has a toggling
action to it. If the said window 'name of window' were to already be
maximised at the time it was created (presumably via some command-line flag)
then the maximize command would have the opposite effect, "unmaximising" it.
Luckily FVWM has a conditional test, Maximized that can be used to test if
the window is maximised. The negation of this is !Maximized:

 
    DestroyFunc StartAppMaximised
    AddToFunc   StartAppMaximised
    + I ThisWindow ("name of window",!Maximized) Maximize

Looking better, certainly. There's still room for improvement, though. In
FVWM 2.5.X, one is able to specify multiple windows to match on, if more
than one window need be considered:

    DestroyFunc StartAppMaximised
    AddToFunc   StartAppMaximised
    + I ThisWindow ("name of window|another window", !Maximized) Maximize

The '|' operator acts as a logical OR command, matching either of the titles
and applying the maximized condition to the (possibly) matched window. In
FVWM 2.4.X, one would have to use multiple lines one after the other:

    DestroyFunc StartAppMaximised
    AddToFunc   StartAppMaximised
    + I ThisWindow ("name of window",!Maximized) Maximize
    + I ThisWindow ("some\_window",!Maximized) Maximize

There's still one more condition to consider: different window types. Up
until now, the assumption has been that normal windows are considered.
Whilst in most cases that's true, FVWM has (at the simplest level) two
different window types that it manages; ordinary application windows and
transient windows. By its very nature, a transient window is one which is
generally only on screen for a short length of time. Also known as 'popup'
windows, they're typically used for 'Open' and 'Save' dialogue windows. It's
not likely (due to their implementation) that one is going to be able to
maximise them anyway, but it's worth excluding them. FVWM allows for this
via the Transient conditional check, which can be negated to !Transient:

      DestroyFunc StartAppMaximised
      AddToFunc   StartAppMaximised
      + I ThisWindow ("name of window|another window", !Maximized, !Transient) Maximize 

## Full-screen mode

The basis and functionality for the StartAppMaximized function is complete.
The last remaining item is to make certain windows borderless and to remove
their title so that they appear to cover the entire viewport. In the
simplest case, the window's name or class is known beforehand, and an
appropriate style line can be set6. For example:

Style "name of window" !Title, !Borders, HandleWidth 0, BorderWidth 0,
ResizeHintOverride That line ought to be pretty self-explanatory. The
ResizeHintOverride condition makes those applications which are column-sized
aware (such as XTerm, GVim, XV, etc) not to be so. Without it, some
applications would leave a noticeable gap at the bottom of the screen.

## Conclusion

This has been a very brief look into how FvwmEvent can be used to monitor
and react to various events. The most important thing to remember about the
use of FvwmEvent is specificity: always be as specific as possible when
operating on windows. Where a certain amount of automation is required,
always enforce a given context, unless it's a requirement that the user is
to select an appropriate operand window at the time the event is triggered.

References

[^1]: http://kahakai.sf.net

## Some general links that might be of interest:

http://edulinux.homeunix.org/fvwm/fvwmcookbookfaq.html
http://fvwm.lair.be
http://www.fvwmwiki.org
1

2
http://www.fvwm.org/documentation/manpages/unstable/FvwmEvent.php
3
This is a slight simplification, since a window can be mapped and in a 'withdrawn' state.
4
http://www.fvwm.org/documentation/faq/\#3.18
5
Inter-client Communications Convention Manual (http://tronche.com/gui/x/icccm/)
6
In FVWM 2.4.X, one would have to use: Style "name of window" NoTitle, NoBorder, HandleWidth 0, BorderWidth 0
