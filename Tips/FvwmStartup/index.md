---
layout : wiki
title : Fvwm Startup Procedure
type : tip
description : |
  This describes how Fvwm Starts.

---

# How FVWM starts applications                                                  

*This is a direct transpose of a mailing list post by Thomas Adam, found
[here](http://www.mail-archive.com/fvwm@lists.math.uh.edu/msg16494.html).*

* TOC
{:toc #toc-full }

## Introduction

A lot of people new to FVWM seem to be confused as to how FVWM goes about
starting up, the files it reads in, the order their file is processed (and
even if there is any order), as well as how the best way of starting up
applications with FVWM is -- whether they're supposed to use something like
~/.xsession or something FVWM-specific.

The following describes the situation:

    I'm using DeskTopSize 3x3 on Fvwm 2.5.27 and trying to start an xterm
    on page 1 2 (middle bottom) and that sometimes works but other times
    the xterm starts on page 0 0 (top left).

    I'm starting the xterm in .xinitrc rather than .fvwm/config because I
    want it to survive the death of the window manager.

This is trying to be achieved through use of the StartFunction
and InitFunction as follows:

{% highlight fvwm %}
DestroyFunc StartFunction
AddToFunc StartFunction
+ I Module FvwmAnimate

DestroyFunc InitFunction
AddToFunc InitFunction
+ I exec xsetroot -solid SteelBlue
+ I Module FvwmPager OnePager *
+ I Module FvwmPager FourPager 0 3
+ I GotoPage 1 2
+ I exec xlogo -render -fg blue -bg yellow -xrm "*Page: 0 1 2"
{% endhighlight %}

This is not quite right for several reasons:

## Explanation

I'm going to give you more information here than you wanted since this
question comes up so often that i get tired of answering it.  So this
is one for the archives...

### 1. In which order FVWM reads in the configuration (in general)

When you run FVWM it does this in terms of config reading:

SetRCDefaults() ``->`` Read $(fvwm-config -d)/ConfigFvwmDefaults ``->``
System-wide or $HOME/.fvwm2rc file.

SetRCDefaults() is just a function that sets up the *bare* minimum for
interacting FVWM, it provides a menu a set of limited bindings, and
hopes for the best.  If you pass FVWM a config which is empty, perhaps
via:

    fvwm -f /dev/null

... you can see for yourself what that looks like.  Then, as part of
SetRCDefault, the file $(fvwm-config -d)/ConfigFvwmDefaults is loaded
-- this expands to (on my machine):

    /usr/local/share/fvwm/ConfigFvwmDefaults

This file is crucial.  It defines a load of common functions (which
tend to act as callbacks) for various things:

* "WindowListFunc" -- used when an item is selected from the WindowList.
* "EWMHActivateWindowFunc" -- used when an EWMH-window requires handling.
* "UrgencyFunc" -- the function that's run if an XClient demands attention -- such as pidgin chat windows.

This file also defines a set of bindings for interacting with the menu
(that is, fvwm\_menu) defined earlier in the SetRCDefaults() function,
as well as some rudimentary bindings.  Nothing more though.  Take a
look for yourself.

After this comes either what was passed in as a file to look for via
the "-f" flag, or then one of predefined list of system-wide config
files FVWM expects to find, or one in $HOME -- and indeed, FVWM config
files are looked for in $HOME/.fvwm/ before anywhere else.

So you can gather now, what the purpose of a .fvwm2rc file is -- it's
either going to augment functionality found in $(fvwm-config
-d)/ConfigFvwmDefaults, or more likely replace it with functionality
the user wants.

### 2. In which order FVWM reads in the configuration (in concrete terms)

So... now that's covered, we now look at how your ~/.fvwm2rc file is
read [1].  FVWM does nothing special.  It will start at the top and
read its instructions in line-by-line until it reaches the end.
Depending on what it reads in, it will either execute that line on the
spot, or collate line(s) together to run at a certain point.

This explains why a typical ordering is suggested for your .fvwm2rc file:

    SetEnv (Ugh!)
    Colorsets
    Style lines
    Bindings
    Functions

Since, for example, if a Style line used a variable from SetEnv, it
would have to come after the env var was declared, as FVWM would be
unable to interpolate it out for the specific style line, resulting in
a parsing error of that line.

I said earlier that FVWM will and can collate lines to run -- there's
two instances on *initialisation* where this is true:

{% highlight fvwm %}
InitFunction
StartFunction
{% endhighlight %}

In that order.  Hence, now that you realise how FVWM parses its file,
why it's possible to do this:

{% highlight fvwm %}
DestroyFunc StartFunction
AddToFunc   StartFunction
+ I Beep

Style foo !Icon

AddToFunc StartFunction I Beep
{% endhighlight %}

... AddToFunc is cumulative when used in successive calls with a known
function.  So you can build up (in this case) StartFunction, and
because it's run after processing the whole file, you know you're not
going to lose anything by doing it this way.

So, InitFunction if it's defined is called first.  Then StartFunction.
 So you might ask what's the difference, and why should you care.
Well, here's the rub:

*INITFUNCTION IS CALLED ONCE -- AT INIT TIME WHEN FVWM FIRST STARTS.
STARTFUNCTION IS CALLED AT INIT AND RESTART.*

So you can see now that you only need one function for your purposes,
as you can add checks to StartFunction to tell it to do one thing if
FVWM is initialising, and another if it's not (i.e., presumably at
restart).

So to go back to your original example of the functions you had:

{% highlight fvwm %}
DestroyFunc StartFunction
AddToFunc StartFunction
+ I Module FvwmAnimate

DestroyFunc InitFunction
AddToFunc InitFunction
+ I exec xsetroot -solid SteelBlue
+ I Module FvwmPager OnePager *
+ I Module FvwmPager FourPager 0 3
+ I GotoPage 1 2
+ I exec xlogo -render -fg blue -bg yellow -xrm "*Page: 0 1 2"
{% endhighlight %}

You would now define the one function as the following:

{% highlight fvwm %}
DestroyFunc StartFunction
AddToFunc   StartFunction
+ I Module FvwmAnimate
+ I Test (Init) Exec exec xsetroot -solid SteelBlue
+ I Module FvwmPager OnePager *
+ I Module FvwmPager FourPager 0 3
+ I Test (Init) GotoPage 1 2
+ I Test (Init) Exec exec xlogo -render -fg blue -bg yellow -xrm "*Page: 0 1 2"
{% endhighlight %}

### 3. Miscellaneous things

There's a couple of things to note here:

#### 3.1. At which point you should start modules

* Modules do not get treated specifically as wanting to start just at
initialisation time because you most likely don't want this (one
exception to this though would be FvwmBanner perhaps) -- when FVWM
restarts, modules die because FVWM closes the pipes it was using to
communicate with them, so having them load up regardless of whether
it's at init time or not makes sense.

#### 3.2. How to indentify the initialisation state

* The test for working out whether FVWM (at the time it reads the
StartFunction) is in Init, is done via:

{% highlight fvwm %}
+ I Test (Init)
{% endhighlight %}

#### 3.3. Use Exec exec to prevent unnecessary dead shell processes

* Unrelated to anything I've mentioned so far, you'll note I am using:

{% highlight fvwm %}
Exec exec foo
{% endhighlight %}

As opposed to:

{% highlight fvwm %}
Exec foo
{% endhighlight %}

... this is so that we don't leave the shell around that FVWM used to
spawn "foo" in the first place.  The double "Exec exec" takes care of
that for us (with other words, it will eliminate the shell as soon as it
has spawned "foo").  The process looks like this with just "Exec foo":

    FVWM ---> (shell) -> foo

But since "Exec" spawns a command via the shell, then what you end up
with is a "dead" (shell) process once "foo" has loaded.  So to get rid
of the shell, just replace it with "foo" outright by using the "exec"
builtin command of the shell, and you will
get this result:

    FVWM ---> foo

This is why the case is important for:  "Exec exec" -- the second
*exec* will be the shell builtin.

### 4. Don'ts

{% highlight fvwm %}
AddToFunc RestartFunction
+ I InitFunction
{% endhighlight %}

Knowing what you do now, you should realise you don't need this.

{% highlight fvwm %}
AddToFunc SessionInitFunction
+ I InitFunction
{% endhighlight %}

Generally a "bad" idea -- especially if your InitFunction spawns terminals.

{% highlight fvwm %}
AddToFunc SessionRestartFunction
+ I RestartFunction
{% endhighlight %}

See above.

### 5. Something about race-conditions

OK.  So now on to your original question.  Here's what you have currently:

{% highlight fvwm %}
DestroyFunc InitFunction
AddToFunc InitFunction
+ I exec xsetroot -solid SteelBlue
+ I Module FvwmPager OnePager *
+ I Module FvwmPager FourPager 0 3
+ I GotoPage 1 2
+ I exec xlogo -render -fg blue -bg yellow -xrm "*Page: 0 1 2"
{% endhighlight %}

But, you've already started your "login" xterm in ~/.xinitrc.  At the
time InitFunction runs, several things could be happening here:

1.  Applications are still starting up; including your "login" window.
2.  The application you expected to start **AFTER** "GotoPage 1 2" is already mapped.

Oops.  You can see the problem, right?  You have a race-condition
here.  You don't know at the point FVWM is running along with starting
up everything else when things will come together.  There is only one
way you can do this reliably:

{% highlight fvwm %}
+ I Schedule 5000 Next (login) MoveToPage 0 1 2
{% endhighlight %}

I say "reliably" loosely here.  The Schedule command is here to give
the window a chance to load, and ensure it really has done before FVWM
tries the condition command asked on it.  Because you're starting
this application out of band from FVWM's own start-up, expecting FVWM
to be able to do anything with the window, because it might not be
mapped or if it is then move it, means you can't do things like this:

{% highlight fvwm %}
Style login StartsOnPage 0 1 2
{% endhighlight %}

... nor can you do something like this:

{% highlight fvwm %}
AddToFunc   StartFunction
+ I None (login) Exec exec xterm -T login
+ I Wait login
+ I Next (login) MoveToPage 0 1 2
{% endhighlight %}

(Well, you could, but you run the risk of doubling-up your original
window, especially if it is just about to start when this does --
you'd get two).

### 6. About the risk of hanging FVWM by using the Wait command

Also bear in mind that I have assumed in all of the above that you
don't need to switch to the page "0 1 2" in question -- you generally
don't, c.f. SkipMapping -- but before that was introduced, one of the
older idioms of making applications appear on the right page was to do
just this:

{% highlight fvwm %}
+ I GotoPage 0 0
+ I Exec xterm -T foo
+ I Wait foo
+ I GotoPage 0 1
+ I Exec xterm -T foo2
+ I Wait foo2
+ I GotoPage 00
{% endhighlight %}

... and so it goes on.  Generally though no longer used.  Given the
caveat of using "Wait" which really will hang FVWM as it waits for a
given window, it would get annoying if one of the commands you were
running which was meant to spawn a window didn't -- or it had a
different name as it transitioned from the time it was mapped to the
point the correct XAtom of the client was consulted to match the given
string used with "Wait" for example, but I digress.

### 7. Finally

You originally mentioned wanting this "login" window to survive the
window manager.  Why not cheat?

{% highlight fvwm %}
DestroyFunc ExitFunction
AddToFunc   ExitFunction
+ I Test (Quit) Restart xterm -T login
{% endhighlight %}
