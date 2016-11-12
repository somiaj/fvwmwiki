---
layout : wiki
title : Mouse Gestures
type : tip
description : |
  Running Fvwm commands with Mouse Gestures.

---


# Mouse Gestures

Mouse gestures allow actions to be performed by drawing shapes, lines, etc.,
typically on the root window. In order for gestures to work, you will have
to ensure that FVWM was compiled with libstroke support.  The details of
which you can see from:

    fvwm --version

The way the shapes can be drawn can be done in two ways.  Perhaps the most
intuitive is to structure the shapes in the layout of your numeric keypad on
your keyboard, hence:

     7  8  9

     4  5  6

     1  2  3

For instance, if I wanted to drawn the letter "L" as a shape, to bind to an
action, I would use the combination:

{% highlight fvwm %}
Stroke N74123 ...
{% endhighlight %}

It's the "N" in front of the numbers that denotes the fact I want to use the
numeric layout of the keypad.  Else, by default the layout used is this:

     1  2  3

     4  5  6

     7  8  9

To enable mouse gestures /stokes add the following lines to your config file

{% highlight fvwm %}
# unbind the third mousebutton
Mouse 3 R N -
#Stroke <Sequence> <Button> <Context> <Modifiers> <Function>
#eg. remap the third mousebutton in case the stroke was in fact only click
#click to open window list
Stroke 0 0 R N Menu WindowList Nop
# from bottom left to top right to maximize the current active window
Stroke N159 0 W N Maximize 100 100
# from top right to bottom left to iconify the current active window
Stroke N951 0 W N Iconify
# draw a Z to close the current active window
Stroke N7895123 0 W N Close

# use StrokeFunc to grab + echo gestures (to xsession-errors) + display
Mouse 3 A M StrokeFunc EchoSequence DrawMotion FeedBack StrokeWidth 3
{% endhighlight %}

