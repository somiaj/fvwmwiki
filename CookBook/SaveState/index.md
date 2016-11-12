---
layout : wiki
title : SaveState
type : recipe
description : |
  When a Maximized application is closed, this will save its state,
  and the next time that application is run, the application will be
  Maximized. This idea can be extended to other window states.

---
## Remembering the state of maximized windows.

This question was originally asked in IRC, although it since migrated to the
Fvwm forums. I often see questions like this -- and what they really amount to
is: "I want to emulate part of the functionality of a session manager, but
don't want to run one". That's fair enough -- although most session managers
have the option of excluding certain applications.

The trick to this, is to get Fvwm to remember the applications that were
maximized when they are closed, and then restored that way when they're next
open again. The solution proposed isn't the best, and it is probably better to
use FvwmPerl. But for something that works quickly, here's what I came up with.
First thing to think about is FvwmEvent. That will have to be used in order to
catch the events of the windows being mapped and unmapped (opened and
destroyed, to use layman's' terms.)

{% highlight fvwm %}
DestroyModuleConfig FE-Maximize: *
*FE-Maximize: Cmd Function
*FE-Maximize: add_window     FuncCheckWindowAW
*FE-Maximize: destroy_window FuncCheckWindowDW

Module FvwmEvent FE-Maximize
{% endhighlight %}

So the FvwmEvent instance FE-Maximize just sets up listeners for
{add,destroy}_window, and will call those functions as necessary. That's the
easy bit -- FvwmEvent really does simplify things for us.

The next stage is to determine how to store the state of those applications.
The easiest way is to use a flat-file that just stores a list of window names
or classes. This file is the one that used to make sure windows created get
maximized, if they were maximized when they were closed/destroyed. So this file
needs to be read in a line at a time, and each entry needs to be matched
against the window that has been created. It's not as complex as it sounds:

{% highlight fvwm %}
DestroyFunc FuncCheckWindowAW
AddToFunc   FuncCheckWindowAW
+ I ThisWindow PipeRead `while read; do \
    [ "$REPLY" = "$[w.class]" ] && echo 'ThisWindow (!Maximized) Maximize \
    || echo 'Nop'; done < $[FVWM_USERDIR]/windowlist`
{% endhighlight %}

Note that I've made a decision to use the window's class as opposed to its
actual name. That's important, since not all the names of windows are
consistent -- just look at Mozilla or Firefox. So uniqueness is important --
and the class of window is unlikely to change, unless the application
allows for it via a command-line option, but then that becomes a PEBCAK
issue. :) The next step is to then record the window if applicable, when any
window is destroyed. This is a little more involved than the previous
function, since we need to check to see whether the window is maximized or
not.

{% highlight fvwm %}
DestroyFunc FuncCheckWindowDW
AddToFunc   FuncCheckWindowDW
+ I ThisWindow (Maximized) Exec /bin/sh -c 'if ! grep -q $[w.class] \
    $[FVWM_USERDIR]/windowlist; then \
    echo $[w.class] >> $[FVWM_USERDIR]/windowlist; fi'
+ I ThisWindow (!Maximized) Exec /bin/sh -c 'if grep -q $[w.class] \
    $[FVWM_USERDIR]/windowlist; then \
    sed -ie "/$[w.class]/d;" $[FVWM_USERDIR]/windowlist; fi'
{% endhighlight %}

Breaking this down a bit:

{% highlight fvwm %}
+ I ThisWindow (Maximized) Exec /bin/sh -c 'if ! grep -q $[w.class] \
    $[FVWM_USERDIR]/windowlist; then \
    echo $[w.class] >> $[FVWM_USERDIR]/windowlist; fi'
{% endhighlight %}

This part checks to see whether the window has been destroyed, and whether
it is maximized. If it is, then it greps the windowlist file for previous
entries of the same class name. If nothing is found in that file, then the
class name of the window is recorded in the windowlist file to be maximized
next time the window is matched.

Similarly, but in the reverse; the following does the opposite:

{% highlight fvwm %}
+ I ThisWindow (!Maximized) Exec /bin/sh -c 'if grep -q $[w.class] \
    $[FVWM_USERDIR]/windowlist; then \
    sed -ie "/$[w.class]/d;" $[FVWM_USERDIR]/windowlist; fi'
{% endhighlight %}

This checks to see that for a window being closed that isn't maximized; and
that was previously listed as maximized, that the entry for it in the
windowlist file is removed, so that it isn't maximized next time around.
One caveat with section above, is the use of sed. The "-i" flag was
introduced into sed recently, and certainly isn't compatible with older
versions across different unixes. So for portability the following ought to
be used:

{% highlight fvwm %}
+ I ThisWindow (!Maximized) Exec /bin/sh -c 'if grep -q $[w.class] \
    $[FVWM_USERDIR]/windowlist; then sed \
    -e "/$[w.class]/d;" < $[FVWM_USERDIR]/windowlist > \
    $[FVWM_USERDIR]/.temp && mv $[FVWM_USERDIR]/.temp \
    $[FVWM_USERDIR]/windowlist; fi'
{% endhighlight %}

There's plenty of other variations -- such as recording iconic states, and
so forth.

