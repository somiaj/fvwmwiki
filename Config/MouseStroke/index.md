---
layout : wiki
title : MouseStroke
type : config
weight : 600
description : |
  This describes how to configure Mouse Stroke which allows
  you to run commands on different Mouse Stroke patterns.

---

Mouse Stroke
============

Another method to send commands to FVWM is via mouse strokes.
If FVWM is configured to be able to understand a Mouse Stroke
(`fvwm --version` to check)
it is then possible to add additional 'bindings'. A mouse stroke is mearly
a pattern you move the mouse in and triger an action.

First FVWM provides you with two methods to describe a 'Stroke'.
Each method is essentially the same. Picture you mouse pointer is on a grid,
you can then describe the direction you move around the grid to crate different
'Stroke' patterns. The only difference between the two methods is how the
grid is describe. I have provided you with an ASCII comment block describing
these two methods.

{% highlight fvwm %}
###########
# Stroke Grid:
#   Telephone:  (N)umpad:
#     1 2 3      7 8 9
#     4 5 6      4 5 6
#     7 8 9      1 2 3
#
#  Stroke {(window)} [sequence] [button] [context] [modifiers] [action]
####################
{% endhighlight %}

For the most part a 'Stroke' is just like a mouse binding with the button, context
and modifier just as above. The main part about the stroke is describing the sequence.
Before describing the sequence, take note that though you can ideally use any Context,
only the 'R' (root window) context acually works. Since it is common that the root
window is covered by other windows, you can require the 'StrokeFunc' to initiate a
Stroke sequence. If the StrokeFunc is bound to a mouse or key event, and when
the mouse or key is pressed a sequence is recorded until you release the mouse button or key.
Any Stroke sequence using button '0' can be called though the StrokeFunc.
The following is an example.

{% highlight fvwm %}
Mouse 3 A A StrokeFunc DrawMotion FeedBack StrokeWidth 2
Stroke 75369 0 A N Refresh
Stroke 1596357 0 W N Close
Stroke 7415963 0 A N Exec exec firefox
{% endhighlight %}

The first binding says that whenever you hold down the third mouse button it
starts the StrokeFunc (and records the sequence until you release the button).
I have set the options DrawMotion with a StrokeWidth of 2
to draw the stroke pattern on the screen. The FeekBack option causes FVWM to change
the cursor to a 'Wait' cursor if your pattern matches any bound sequence.

The next are three Stroke examples. The first will Refresh the sceen
if you draw a backwards 'V'. Note that by default the sequence is written
in terms of the telephone grid. If you would prefer to write the sequence
in terms of the numeric pad, put an 'N' in front of the sequnce. For example
the sequence '75369' and 'N15963' are the same. Either option is valid,
so use the one which you prefer. The second Stroke command will close
a window if you draw and 'X' in it, and the third will open the firefox
webbrowser if you draw a 'N'.

One thing to note is that your shape may have slight
varriants. For example a 'N' could also look like '74148963', '74158963', '7418963'
or '415963'. If you wish to have the the firefox webbrowser open
on any of these sloppy 'N' shapes, you will have to provide a Stroke
definition for each one.


