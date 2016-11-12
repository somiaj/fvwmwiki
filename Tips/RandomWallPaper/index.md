---
layout : wiki
title : Random Wallpaper
type : tip
description : |
  Setting random background images.

---
# Choosing and setting random images from a folder

* TOC                                                                           
{:toc #toc-full}   


## Choosing the random image 

For this Task, you can use the following program:

{% highlight lisp %}
#!/usr/bin/env clisp

;;; Here you set the directory to look for images in (wildcards allowed, as you see)
(defconstant images "~/.fvwm/images/*")

(defun randomimage (lst)
  (nth (random (length lst) (make-random-state t))
       lst))

(format t "~A" (namestring (randomimage (directory images))))
{% endhighlight %}

## Setting the chosen Image

You can add the following to your fvwm configuration (for example)

{% highlight fvwm %}
AddToFunc StartFunction
+ I Exec exec Esetroot -scale $(randomimage.lisp)
{% endhighlight %}

Where randomimage.lisp is the name of the executable file you named the
above as. If you are not using clisp, you have to remove the first line in
the program and add the according interpreter call in front of
"randomimage.lisp" in your FVWM configuration.

## Using XV to set random background image

From the ancient times [XV](http://www.trilon.com/xv/downloads.html) has been
used for this purpose in the following way

{% highlight fvwm %}
AddToFunc StartFunction
+ "I" Exec   xv -root -max -quit -random ~/.fvwm/images/*
{% endhighlight %}

## Using wmsetbg to set random background image

wmsetbg has better support for pseudo transparency than xv. It can be used as follows:

{% highlight fvwm %}
AddToFunc StartFunction
+ I Exec exec wmsetbg -a `ls $FVWM_USERDIR/Background/*.jpg|sort -R|tail -1`
{% endhighlight %}

## Random background color from rgb.txt

{% highlight shell %}
#!/bin/sh
# randomcolor.sh
# Change to appropriate location
RGB="/usr/X11R6/lib/X11/rgb.txt"

# '$RANDOM' is bash specific
RNDLINE=$(sed -n $(expr $RANDOM % $(sed -n '$=' $RGB))p $RGB)
RNDCOLOR=$(echo $RNDLINE | awk '{ print $4, $5, $6 }' |\
        sed 's/[[:blank:]]//g')
echo $RNDCOLOR
{% endhighlight %}

Then call it from FVWM

{% highlight fvwm %}
AddToFunc StartFunction
+ I Exec xsetroot -solid $(randomcolor.sh)
{% endhighlight %}
