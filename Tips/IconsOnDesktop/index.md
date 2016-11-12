---
layout : wiki
title : Desktop Icons
type : tip
description : |
  Using FvwmButtons to put icons on the Desktop to launch
  applications.

---
# Desktop Icons 

Normally an icon represents a minimized application.  If you
want to turn that around, and launch applications by clicking
on icons we can't stop you.  Here's a way to do that using
FvwmButtons:

{% highlight fvwm %}
# FvwmButtons icon launcher:
DestroyFunc Launcher
AddToFunc Launcher
+ I DestroyModuleConfig $0Launch: *
+ I *$0Launch: Geometry 64x68
+ I *$0Launch: Columns 1
+ I *$0Launch: Rows    4
+ I *$0Launch: Frame   0
+ I *$0Launch: (1x3+0+0, Icon $1, Action (Mouse 1) `Exec exec $2`)
+ I *$0Launch: Pixmap none
+ I *$0Launch: (1x1+0+3, Font 9x15, Fore White, Back DarkBlue, \
                Title $0, Action (Mouse 1) `Exec exec $2`)
+ I Style $0Launch HandleWidth 0, NoTitle
+ I Module FvwmButtons $3 $0Launch
+ I UpdateStyles
    
# Examples:
Launcher RXVT xterm.xpm "rxvt -bg black" "-g +0+0"
Launcher XV   xv.xpm    xv   "-g +0+100"
{% endhighlight %}

Also, GNOME and KDE have desktop icon applications gmc and kfm,
which enable this functionality.  These applications may be run under FVWM.
Another solution is using the pinboard (desktop with icons) of
[ROX Filer](http://rox.sourceforge.net).

There is another solution which is very much easy to use:
[Idesk](http://idesk.sourceforge.net/) lucky.
