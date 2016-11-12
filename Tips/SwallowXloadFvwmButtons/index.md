---
layout : wiki
title : Swallow Xload inside FvwmButtons
type : tip
description : |
  This describes how to build a system monintor by Swallowing
  xload inside of FvwmButtons.

---
* TOC
{:toc}

# Using FvwmButtons to Swallow Xload

## Simple Example

The simplest example of swallowing xload is to create a definition similar to this one:

{% highlight fvwm %}
DestroyModuleConfig FvwmButtons-test: *
*FvwmButtons-test: Geometry 100x100-1-1
*FvwmButtons-test: (1x1, Title 'xload', \
        Swallow(UseOld,NoHints,NoRespawn) "xload" \
        'Exec xload', \
        Action(Mouse1) 'Exec xterm -e top')

Module FvwmButtons FvwmButtons-test
{% endhighlight %}

This result will be a 100x100 pixel button in the lower right hand corner of
the screen that draws a running xload.  If you click on the button, an xterm
will pop up running top.

## Advanced Example

Because of X11's network transperancy, it is possible to use Swallow to
display xload running from other machines as well.  This example shows how
to set up a collapsible FvwmButtons Panel that contains xloads running on 3
remote machines (named machineA, machineB, and machineC).

Before setting up your fvwm configuration, you will need to make some changes to your remote machines.

* Enable X11Forwarding in the /etc/ssh/sshd\_config files
* Set up security so that you can ssh to the remote machines without being prompted for passwords.  
* On machineA run 'ln -s /usr/X11R6/bin/xload /usr/X11R6/bin/xload.machineA' and make similar links on machineB and machineC.

At this point, you should be able to run 'ssh machineA xload.machineA' on your local machine and see
an xload window from machineA.

Adding the following fvwm configuration would draw a collapsible panel in the lower right corner of
the screen that contains 3 xload buttons.  Left-clicking the buttons brings up an ssh login to the
remote machine, and Right-clicking the buttons will restart xload on the button if the connection
to the remote server has been dropped.

{% highlight fvwm %}
DestroyFunc StartXLoadOn
AddToFunc   StartXLoadOn
+ I None (xload) Exec ssh $0 /usr/X11R6/bin/xload.$0 &

DestroyModuleConfig FvwmButtonsXLoad-Panel: *
*FvwmButtonsXLoad-Panel: Geometry 300x100
*FvwmButtonsXLoad-Panel: Rows 1
*FvwmButtonsXLoad-Panel: Columns 3
*FvwmButtonsXLoad-Panel: (1x1+0+0, \
        Title 'machineA', \
        Swallow(NoOld,NoHints,Respawn,Kill) "xload.machineA" \
        'StartXLoadOn machineA', \
        Action(Mouse 3) 'StartXLoadOn machineA', \
        Action(Mouse 1) 'Exec xterm -e ssh machineA')
*FvwmButtonsXLoad-Panel: (1x1+1+0, \
        Title 'machineA', \
        Swallow(NoOld,NoHints,Respawn,Kill) "xload.machineB" \
        'StartXLoadOn machineB', \
        Action(Mouse 3) 'StartXLoadOn machineB', \
        Action(Mouse 1) 'Exec xterm -e ssh machineB')
*FvwmButtonsXLoad-Panel: (1x1+2+0, \
        Title 'machineA', \
        Swallow(NoOld,NoHints,Respawn,Kill) "xload.machineC" \
        'StartXLoadOn machineC', \
        Action(Mouse 3) 'StartXLoadOn machineC', \
        Action(Mouse 1) 'Exec xterm -e ssh machineC')

DestroyModuleConfig FvwmButtonsXLoad: *
*FvwmButtonsXLoad: Back #ffffff
*FvwmButtonsXLoad: Fore #000000
*FvwmButtonsXLoad: Geometry 20x100-1-1
*FvwmButtonsXLoad: Rows 1
*FvwmButtonsXLoad: Frame 1
*FvwmButtonsXLoad: Padding 0 0
*FvwmButtonsXLoad: (Panel(left, steps 0, delay 0, position top, indicator 10) \
        "FvwmButtonsXLoad-Panel" 'Module FvwmButtons FvwmButtonsXLoad-Panel')

Module FvwmButtons FvwmButtonsXload
{% endhighlight %}
