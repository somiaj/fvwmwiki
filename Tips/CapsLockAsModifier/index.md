---
layout : wiki
title : Auto Hiding Windows
type : tip
description : |
  This describes how to configure CapsLock as a Modifier for Key and
  Mouse bindings.

---
* TOC
{:toc}

# Caps Lock as FVWM Key

## Introduction

Many people think of Caps Lock as a very annoying key at an annoying
position. Lots of us also know Windows, Amiga, or Macintosh keys, which are
special for keybindings used in these environments. But what about a FVWM
key, which all keybindings are bound to, so that other applications can make
use of all other modifiers like CTRL, Alt and Shift?  Here we go ...

## Changing Xmodmap

First of all we need to remove the original function of Caps Lock, then we
can make it a new modifier to be used in FVWM keybindings. We need to edit
~/.xmodmap if this is read automatically at startup of your X Session. If
not, change it, or edit a similar xmodmap file, that is read. You need the
following lines:

    remove Lock = Caps_Lock
    add mod4 = Caps_Lock

After changing this you need to run:

    xmodmap ~/.xmodmap

Now Caps Lock acts as a fourth modifier key.

An other way is to place 

    Option "XkbOptions" "ctrl:nocaps"

in your XF86Config[-4]

### Binding Keys
Now we are going to make use of our new defined modifier. That is quite as
easy as step one. In the modifier column of your keybinding-defining line
just use 4 instead of C, M or S:

{% highlight fvwm %}
Key Left        A 4     Scroll -100 +0
Key Up          A 4     Scroll +0 -100
Key Right       A 4     Scroll +100 +0
Key Down        A 4     Scroll +0 +100
{% endhighlight %}

This lets you change your desktop pages using Caps+Arrow Keys
