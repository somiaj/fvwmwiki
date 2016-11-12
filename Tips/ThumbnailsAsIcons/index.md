---
layout : wiki
title : Thumbnails as Icons
type : tip
description : |
  This will take a screenshot of your window before Iconifying
  it and use that as the Icon that is placed on the Desktop.

---

# Thumbnails as Icons 

You will need imagemagick for this function to work.  The two functions take
a snapshot of the window before it is iconified, and then assigns the icon
to the iconified window.

{% highlight fvwm %}
DestroyFunc Thumbnail
AddToFunc Thumbnail
+ I ThisWindow (Shaded) WindowShade toggle
+ I Schedule 800 Raise 
+ I Raise
+ I Piperead "xwd -silent -id $[w.id] > $[HOME]/.fvwm/icon.tmp.$[w.id].xwd"
+ I Iconify
+ I ThisWindow (Iconifiable, !Iconic) PipeRead `nice -n 19 convert -resize 64x64 \
    -frame 1x1 -mattecolor black -quality 0 xwd:$[HOME]/.fvwm/icon.tmp.$[w.id].xwd \
    png:$[HOME]/.fvwm/icon.tmp.$[w.id].png ; rm $[HOME]/.fvwm/icon.tmp.$[w.id].xwd`
+ I ThisWindow WindowStyle IconOverride, Icon $[HOME]/.fvwm/icon.tmp.$[w.id].png, StaysOnBottom

DestroyFunc DeThumbnail
AddToFunc DeThumbnail
+ I DestroyWindowStyle
+ I Exec rm -f $HOME/.fvwm/icon.tmp.$[w.id].*
+ I deiconify-and-focus
{% endhighlight %}

Now you have to change all your key- and mousebindings from Iconify to
Thumbnail and deIconify to deThumbnail.  You could also use FvwmEvent to do
the same thing, if you have functions that iconify windows in them.
