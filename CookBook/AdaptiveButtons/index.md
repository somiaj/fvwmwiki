---
layout : wiki
title : AdaptiveButtons
type : recipe
description : |
  Through the SendToModule command, FvwmButtons can be configured
  to be more dynamic. You can change the Colorset, Icon, Title,
  etc. of a Button.
---

## FvwmButtons: adaptive configuration.

FvwmButtons is an extremely useful module in that it has the ability to
swallow applications and house them as containers. Most people usually just
leave it at that, although FvwmButtons' use can get quite involved with some
needed 'added extras' to crop up from time to time. To take a simple
example, let's imagine that a button with an FvwmButtons instance controls
the sound volume -- and that the desired effect is to have the icon change
when the volume is muted, and restored when unmuted, etc., etc.

This requires flagging the correct button within the FvwmButtons instance so
that it can be 'referenced' from within FVWM itself -- via functions, menus,
and so forth. Here's an example of a snippet of a FvwmButtons instance:

{% highlight fvwm %}
*OSXDock: (24x26+1100+0, Padding 1 0, Icon v4.png, ActionOnPress, \
    Action(Mouse 1) Menu MenuVol Rectangle +$left+25 0 0m)
{% endhighlight %}

... which works fine. In order for us to 'flag' it, we just need to add the
"Id" command to it:

{% highlight fvwm %}
*OSXDock: (24x26+1100+0, Id "A", Padding 1 0, Icon v4.png, ActionOnPress, \
    Action(Mouse 1) Menu MenuVol Rectangle +$left+25 0 0m)
{% endhighlight %}

Hence, we can now refer to this button as button A. Now we have to concentrate
on changing the icon to reflect the state of the volume. The menu entries
which hold the volume increments might be defined as the following:

{% highlight fvwm %}
DestroyMenu MenuVol
AddToMenu MenuVol
+ "100%%" Exec exec aumix -w 100
+ "90%%" Exec exec aumix -w 90
+ "80%%" Exec exec aumix -w 80
+ "70%%" Exec exec aumix -w 70
+ "60%%" Exec exec aumix -w 60
+ "50%%" Exec exec aumix -w 50
+ "40%%" Exec exec aumix -w 40
+ "30%%" Exec exec aumix -w 30
+ "20%%" Exec exec aumix -w 20
+ "10%%" Exec exec aumix -w 10
+ "0%%" Exec exec aumix -w 0
{% endhighlight %}

This is fine, and will work, but we have yet to connect the actions of the menu
operations, and the changing of the icon. The continual duplication of the
"Exec exec" lines for the same program (but with different parameters) can
be smartened up into a function call:

{% highlight fvwm %}
DestroyMenu MenuVol
AddToMenu MenuVol
+ "100%%" ChangeSoundVolAndIcon 100
+ "90%%" ChangeSoundVolAndIcon 90
+ "80%%" ChangeSoundVolAndIcon 80
+ "70%%" ChangeSoundVolAndIcon 70
+ "60%%" ChangeSoundVolAndIcon 60
+ "50%%" ChangeSoundVolAndIcon 50
+ "40%%" ChangeSoundVolAndIcon 40
+ "30%%" ChangeSoundVolAndIcon 30
+ "20%%" ChangeSoundVolAndIcon 20
+ "10%%" ChangeSoundVolAndIcon 10
+ "0%%"  SoundChangeIcon
{% endhighlight %}

By separating out the functionality into a different function, we only then
have to change one item, if any changes to the calling program need to be
made, hence the following will provide the same functionality as in the
original version -- the only difference is that we're passing in the volume
level as a parameter.

{% highlight fvwm %}
DestroyFunc ChangeSoundVolAndIcon
AddToFunc ChangeSoundVolAndIcon
+ I Exec exec aumix -w $0
{% endhighlight %}

Added to which we can now add to that function the definition to change the
FvwmButtons icon:

{% highlight fvwm %}
+ I SendToModule OSXDock ChangeButton "A" Icon v4.png
{% endhighlight %}

The SendToModule command accepts some parameters -- the first one is the module
alias of the module we're wishing to send the command to. In this case, it is
'OSXDock'. The next command is 'ChangeButton' which accepts a parameter -- the
button Id we defined earlier on, and then the last parameter is the new icon
the button is to take on.

The sharp-eyed amongst you will have realized that for a volume of zero; we
will need to change the icon to mute. We can do this by calling for that
value only, a different function instance:

{% highlight fvwm %}
DestroyFunc SoundChangeIcon
AddToFunc SoundChangeIcon
+ I Exec exec aumix -w 0
+ I SendToModule OSXDock ChangeButton "A" Icon mute.png
{% endhighlight %}
