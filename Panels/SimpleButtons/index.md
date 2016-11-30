---
layout : wiki
title : SimpleButtons
type : panel
weight : 500
description : |
  This is a simple horizontal Buttons that holds 6 icons to show
  the basics of FvwmButtons.

---

# SimpleButtons

Here is a simple example of using FvwmButtons as a panel that contains
6 Icons to launch applications.

|![image](scrot.jpg)|

First determine the layout of the buttons. I am going to use 48x48 pixel
icons with some padding so I decided on 6 60x60 pixel buttons positioned
as shown

![image](layout.png)

So this means the Buttons need to be 60*6 = 360 pixels wide and 60
pixels high. Next I want to position them in the middle of my
screen 50 pixles from the bottom. To put this dock in the middle
of my screen I calculate that half my screen is 1920/2 = 960 and
half my Buggons width is 360/2 = 180. This puts them 960 - 180 =
780 pixles from the left end of the monintor.

Putting this altogether I get a Geometry string of the form

    [Width]x[Height]+[XFromRight]-[YFromBottom]
    360x60+780-50

Next set the Colorset of the buttons and the Frame to 0 (so the buttons
are just a solid background color). Then divide the Buttons into a grid
with 1 Row and 6 Columns. This makes all the buttons the same size of 1x1.
Then define the 6 Buttons. Each button is just an Icon and an Action that
runs a program when clicked by the mouse.

{% highlight fvwm %}
DestroyModuleConfig SimpleButtons: *
*SimpleButtons: Geometry 360x60+780-50
*SimpleButtons: Colorset 10
*Simplebuttons: Frame 0
*SimpleButtons: Rows 1
*SimpleButtons: Columns 6
*SimpleButtons: (1x1, Icon "48x48/xterm.png", \
              Action(Mouse 1) "Exec exec xterm")
*SimpleButtons: (1x1, Icon 48x48/firefox.png, \
              Action(Mouse 1) "Exec exec firefox")
*SimpleButtons: (1x1, Icon 48x48/gimp.png, \
              Action(Mouse 1) "Exec exec gimp")
*SimpleButtons: (1x1, Icon 48x48/gvim.png, \
              Action(Mouse 1) "Exec exec gvim")
*SimpleButtons: (1x1, Icon 48x48/vlc.png, \
              Action(Mouse 1) "Exec exec vlc")
*SimpleButtons: (1x1, Icon 48x48/editor.png, \
              Action(Mouse 1) "Exec exec libreoffice ")
{% endhighlight %}

Be sure to define the Colorset and add some Styles
for the Buttons such as no Borders or Title, and
WindowListSkip so it won't be on window lists.

{% highlight fvwm %}
Colorset 10 fg #ffffff, bg #003c3c
Style SimpleButtons !Borders, !Title, WindowListSkip
{% endhighlight %}

Then run the Buttons by using the following command, or optionally
add this to the StartFuction so it loads when Fvwm starts.

{% highlight fvwm %}
Module FvwmButtons SimpleButtons
AddToFunc StartFunction I Module FvwmButtons SimpleButtons
{% endhighlight %}


