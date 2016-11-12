---
layout : wiki
title : Rxvt Run Dialogue
type : tip
description : |
  This uses Rxvt to configure pop up a little dialog you can type a command
  to execute.

---
* TOC
{:toc}

# An RXVT based run dialog with tab completion

## Introduction

What follows is the description of a very simple way to realize a run dialog (a
little dialog where the user can enter the name of an executable to start) using
an RXVT (a terminal emulator as e.g. xterm). The trick is to bind the string
``"&\nexit\n"`` to the return key.  See [Tips/XTermRunDialogue](
{{ "/Tips/XTermRunDialogue" | prepend: site.baseurl }})
on how to do this with xterm.

The following script, starts the dialog:

{% highlight shell %}
#!/bin/sh
rxvt +sb -name fvwm-run-dialog -title "run" -geometry 80x1+224+360 \  
--keysym.0xFF0D: " &\nexit\n" -e bash --init-file \
$HOME/.fvwm/run-dialog.bash-init
{% endhighlight %}

This above script needs the following BASH initialization script

{% highlight shell %}
# ~/.fvwm/run-dialog.bash-init
export PS1=""
{% endhighlight %}

To bind the dialog to a key put for example the following lines in your
FVWM configuration:

{% highlight fvwm %}
Style fvwm-run-dialog FPGrabFocus, FPReleaseFocus
Key R A 4 Exec exec $[HOME]/.fvwm/run-dialog
{% endhighlight %}

This allows you to start the dialog using "Win-R". Note that the dialog is not pretty
but it's resource friendly and offers tab completion since it's based on a real
shell.

## Enhancements

Its quite annoying having "exit" written to my .bash\_history every time i use this "Run" Dialog.
So I put an additional line to dialog script:

{% highlight shell %}
export PS1=""
export HISTCONTROL="ignorespace"
{% endhighlight %}

And I changed the script to read:

{% highlight shell %}
#!/bin/sh
rxvt +sb -name fvwm-run-dialog -title "run" -geometry 80x1+224+360 \  
--keysym.0xFF0D: " &\n exit\n" -e bash --init-file \
$HOME/.fvwm/run-dialog.bash-init
{% endhighlight %}

Notice the Space right before "exit".

To explain: HISTCONTROL="ignorespace" tells bash not to write commands to
the history file which are preceded by a Space.

And the Space before "exit" makes this line not appear in the history.
