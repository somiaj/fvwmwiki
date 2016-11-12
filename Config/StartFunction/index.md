---
layout : wiki
title : StartFunction
type : function
weight : 600
description : |
  The StartFunction is run as soon as Fvwm is done Reading
  the config file. Similarly the ExitFunction is run when fvwm
  ends.

---
# StartFunction

The StartFunction is the function FVWM will run after it has completed
reading [/Config/Fvwm2rc]({{ "/Config/Fvwm2rc" | prepend: site.baseurl }}).
In this function you can preform you basic
'StartUp' actions after FVWM is fully configured. Note that in FVWM 2.4.x
this was split up into three functions, 'StartFunction', 'InitFunction'
and 'RestartFunction'. This is no longer needed because though the 'Test'
condition we can test if this is run after an 'Init' or 'Restart'.

{% highlight fvwm %}
#####
# StartFunction
###########
DestroyFunc StartFunction
AddToFunc   StartFunction
+ I Test (Init) Exec exec xscreensaver
+ I Test (Init) Exec fvwm-root -r \
    $[FVWM_USERDIR]/wallpapers/background.png
+ I Test (Init) Exec exec vlc
+ I Test (Restart) PipeRead 'echo Echo Restarted: `date`'
+ I Module FvwmBanner
+ I Module FvwmPager 0 2
+ I Module FvwmButtons MyButtons
{% endhighlight %}

Upon startup this function will launch xscreensaver and vlc if we
satisfy the 'Init' condition (the initial launch of fvwm). I also
set the background though the provided command 'fvwm-root' (Note:
Use an application, such as feh, for backgrounds if you want to be
able to scale images and use .jpeg images).

This will Echo the restart time into .xsession-errors when Fvwm
is restarted. And then either if it is starting the first time
or being restarted, modules are loaded. Modules must be loaded each time
Fvwm restarts because they loose their communication pipe when Fvwm shuts
down and restarts.

Due to [/Config/FunctionSynchronisation](
{{ "/Config/FunctionSynchronisation" |prepend: site.baseurl }})
applications you launch from StartFunction may
not finish loading in the same order. [/Tips/FvwmStartup](
{{ "/Tips/FvwmStartup" | prepend: site.baseurl }}) gives a more detailed
look at this.

## ExitFunction

The ExitFunction is run when fvwm Exits. By using the Quit and ToRestart
conditions you can run commands depending on if you are quitting or
restarting. A quick example would give

{% highlight fvwm %}
DestroyFunc ExitFunction
AddToFunc ExitFunction
+ I Test (Quit) Echo Bye-bye
+ I KillModule MyBuggyModule
+ I Test (ToRestart) Beep
{% endhighlight %}

