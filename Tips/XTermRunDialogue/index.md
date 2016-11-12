---
layout : wiki
title : XTerm Run Dialogue
type : tip
description : |
  This uses Rxvt to configure pop up a little dialog you can type a command
  to execute.

---


# An xterm based run dialog with tab completion 

What if you want to do [Tips/RxvtRunDialogue](
{{ "/Tips/RxvtRunDialogue" | prepend: site.baseurl }}), but only have xterm
available?  All is not lost.  Good old xterm does not have the
``--keysym`` option, but you can assign actions in a similar way using X
resources.

Add the following to your ~/.Xresource file:

    fvwm-run-dialog.VT100*translations: #override \n\
        <Key>Return: string(" &\n exit\n")

The ``~/.fvwm/run-dialog`` looks more like this:

{% highlight shell %}
#!/bin/sh
xterm +sb -name fvwm-run-dialog -title "run" -geometry 80x1+224+360 \  
-e bash --init-file $HOME/.fvwm/run-dialog.bash-init
{% endhighlight %}

This above script needs the following BASH initialization script
``~/.fvwm/run-dialog.bash-init``:

{% highlight shell %}
export PS1=""
export HISTCONTROL="ignorespace"
{% endhighlight %}

To bind the dialog to a key put for example the following lines in your
FVWM configuration:

{% highlight fvwm %}
Style fvwm-run-dialog FPGrabFocus, FPReleaseFocus
Key R A 4 Exec exec $[FVWM_USERDIR]/run-dialog
{% endhighlight %}
