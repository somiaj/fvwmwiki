---
layout : wiki
title : Background Menu Menu
type : menu
weight : 200
description : |
  This generates a menu of all files in a background directory
  that can be used to switch backgrounds.

---

# Background Menu

This example uses a shell script to loop through all the images
in a directory and build a menu from them.

## Simple Case

First set up a directory on your system to store the background images
in. In this example I will use $[FVWM_USERDIR]/backgrounds/. After that
we will need to write a script that will put all the files in that
directory into a menu.

To do this the script needs to export the correct syntax for [/Config/Menus](
{{ "/Config/Menus" | prepend: site.baseurl }}) which can be done via
the echo command. Then just use the bash for statement to loop through
all files in the backgrounds directory.

{% highlight shell %}
for i in $[FVWM_USERDIR]/backgrounds/*
do
  echo "AddToMenu BGMenu \"`basename $i`\" SetBG \"`basename $i`\""
done
{% endhighlight %}

This script lists all the files in the given directory and sends the
fiename to the function SetBG to set the background image.

In order to use this with PipeRead first write the script as a single line

{% highlight shell %}
for i in $[FVWM_USERDIR]/backgrounds/*; do echo "AddToMenu BGMenu \"`basename $i`\" SetBG \"`basename $i`\""; done
{% endhighlight %}

And now using PipeRead put this in a function to generate the menu

{% highlight fvwm %}
DestroyFunc BuildBGMenu
AddToFunc BuildBGMenu
+ I DestroyMenu BGMenu
+ I AddToMenu BGMenu "Backgrounds" Title
+ I PipeRead 'for i in $[FVWM_USERDIR]/backgrounds/*; do \
    echo "AddToMenu BGMenu \"`basename $i`\" SetBG \
    \"`basename $i`\""; done'
+ I AddToMenu BGMenu "" Nop
+ I AddToMenu BGMenu "Rebuild" BuildBGMenu

# Call the function to build the menu
BuildBGMenu
{% endhighlight %}

This function builds the menu, and then appends an option
at the end, Rebuild, which can be used to rerun this function
when backgrounds are added/removed from the directory.

Once the menu is built you can open the menu with 'Menu BGMenu'
or include it in another menu using the PopUp command. In addition
you will need a function SetBG to actually set the background. I use
a tool called feh for this.

{% highlight fvwm %}
DestroyFunc SetBG
AddToFunc SetBG
+ I Test (f "$[FVWM_USERDIR]/backgrounds/$0") Exec \
  exec feh --bg-scale "$[FVWM_USERDIR]/backgrounds/$0"
+ I TestRc (Match) Exec exec ln -fs \
  "$[FVWM_USERDIR]/backgrounds/$0" $[FVWM_USERDIR]/.defaultBG

# To load last selected BG at start
AddToFunc StartFunction I Exec exec \
feh --bg-scale $[FVWM_USERDIR]/.defaultBG
{% endhighlight %}

This function also creates a link to 


## Auto generate thumbnails


## Save Menu in a file
