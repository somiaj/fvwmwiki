---
layout : wiki
title : Window Decorations
type : config
weight : 450
description : |
  This gives an overview of how to configure window decorations.
  See <a href="{{ "/Decor" | prepend: site.baseurl }}">/Decor</a>
  for example decors.

---

6: Window Decor
===============

1. TOC
{:toc}


The window decor defines how the windows look. FVWM can set up window
decorations by using a color scheme or pixmaps. For the first example
lets look at a simple window decor with no pixmaps.  For starters define some colorsets
to set up the basic colors your window decorations will use. Colorsets can be
used to define the colors for all parts of FVWM. The following sets up
three simple colorsets.

## Vector Buttons

The decor can be broken up into three parts, the TitleStyle, the ButtonStyle
and the BorderStyle. The following sets up a simple decor.

<pre>
<font color="#0000ff">#####</font>
<font color="#0000ff"># Window Decor</font>
<font color="#0000ff">###########</font>
<font color="#008b8b">DestroyDecor</font> MyDecor
<font color="#008b8b">AddToDecor</font>   MyDecor
+ <font color="#008b8b">TitleStyle</font> <font color="#a52a2a"><b>LeftJustified</b></font> <font color="#a52a2a"><b>Height</b></font> 18
+ <font color="#008b8b">ButtonStyle</font> 1 <font color="#a52a2a"><b>ActiveUp</b></font> <font color="#a52a2a"><b>Vector</b></font> 4 30x30@3 60x60@3 60x30@4 30x60@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> 1 <font color="#a52a2a"><b>ActiveDown</b></font> <font color="#a52a2a"><b>Vector</b></font> 4 30x30@3 60x60@3 60x30@4 30x60@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> 1 <font color="#a52a2a"><b>Inactive</b></font> <font color="#a52a2a"><b>Vector</b></font> 4 30x30@3 60x60@3 60x30@4 30x60@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> 3 <font color="#a52a2a"><b>ActiveUp</b></font> <font color="#a52a2a"><b>Vector</b></font> 5 30x60@3 60x60@3 60x50@3 30x50@3 30x60@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> 3 <font color="#a52a2a"><b>ActiveDown</b></font> <font color="#a52a2a"><b>Vector</b></font> 5 30x60@3 60x60@3 60x50@3 30x50@3 30x60@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> 3 <font color="#a52a2a"><b>Inactive</b></font> <font color="#a52a2a"><b>Vector</b></font> 5 30x60@3 60x60@3 60x50@3 30x50@3 30x60@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> 5 <font color="#a52a2a"><b>ActiveUp</b></font> <font color="#a52a2a"><b>Vector</b></font> 7 30x30@3 30x60@3 60x60@3 60x30@3 30x30@3 30x35@3 60x35@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> 5 <font color="#a52a2a"><b>ActiveDown</b></font> <font color="#a52a2a"><b>Vector</b></font> 7 30x30@3 30x60@3 60x60@3 60x30@3 30x30@3 30x35@3 60x35@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> 5 <font color="#a52a2a"><b>Inactive</b></font> <font color="#a52a2a"><b>Vector</b></font> 7 30x30@3 30x60@3 60x60@3 60x30@3 30x30@3 30x35@3 60x35@3 -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">TitleStyle</font> -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">BorderStyle</font> <font color="#a52a2a"><b>Simple</b></font> -- <font color="#a52a2a"><b>NoInset</b></font> <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> <font color="#a52a2a"><b>All</b></font> -- <font color="#a52a2a"><b>UseTitleStyle</b></font>
</pre>

This decor sets up three buttons, numbers 1, 3 and 5 (the positions is the same
as in the window bindings section) using vectors. Note that before a button
can be added to a Decor it must first be bound to some action via some binding.
Each part is followed by a '-- Flat' to make the buttons and title bar
not appear to be pushed out (or in) from the window. Vectors are just simple line drawings.
Each vector is set up on a 100x100 grid and can have any number of points all connected
by lines. The syntax is 'Vector [number of points] [[point1] [point2] ...]'.
The points are defined by 'XxY@Z' where Z is any number 0-4 representing the color
to be used for the line. 0 - Shadow(sh), 1 - Hilight(hi), 2 - Background(bg),
3 - Foreground(fg), 4 - Invisible.

## Pixmaps

Here is an example of a more elaborate Decor using pixmaps for the buttons and title bar.

<pre>
<font color="#0000ff">#####</font>
<font color="#0000ff"># Pixmap Decor</font>
<font color="#0000ff">###########</font>
<font color="#008b8b">DestroyDecor</font> PixmapDecor
<font color="#008b8b">AddToDecor</font>   PixmapDecor
+ <font color="#008b8b">TitleStyle</font> <font color="#a52a2a"><b>LeftJustified</b></font> <font color="#a52a2a"><b>Height</b></font> 24
+ <font color="#008b8b">ButtonStyle</font> 1 \
        <font color="#a52a2a"><b>ActiveUp</b></font>     (<font color="#a52a2a"><b>Pixmap</b></font> close-activeup.png -- <font color="#a52a2a"><b>Flat</b></font>) \
        <font color="#a52a2a"><b>ActiveDown</b></font>   (<font color="#a52a2a"><b>Pixmap</b></font> close-activedown.png -- <font color="#a52a2a"><b>Flat</b></font>) \
        <font color="#a52a2a"><b>Inactive</b></font>     (<font color="#a52a2a"><b>Pixmap</b></font> inactive.png -- <font color="#a52a2a"><b>Flat</b></font>)
+ <font color="#008b8b">ButtonStyle</font> 3 \
        <font color="#a52a2a"><b>ActiveUp</b></font>     (<font color="#a52a2a"><b>Pixmap</b></font> iconify-activeup.png -- <font color="#a52a2a"><b>Flat</b></font>) \
        <font color="#a52a2a"><b>ActiveDown</b></font>   (<font color="#a52a2a"><b>Pixmap</b></font> iconify-activedown.png -- <font color="#a52a2a"><b>Flat</b></font>) \
        <font color="#a52a2a"><b>Inactive</b></font>     (<font color="#a52a2a"><b>Pixmap</b></font> <font color="#a020f0">$[fvwm_img]</font>/<font color="#a52a2a"><b>button</b></font>/inactive.png -- <font color="#a52a2a"><b>Flat</b></font>)
+ <font color="#008b8b">ButtonStyle</font> 5 \
        <font color="#a52a2a"><b>ActiveUp</b></font>     (<font color="#a52a2a"><b>Pixmap</b></font> <font color="#a020f0">$[fvwm_img]</font>/<font color="#a52a2a"><b>button</b></font>/maximize-activeup.png -- <font color="#a52a2a"><b>Flat</b></font>) \
        <font color="#a52a2a"><b>ActiveDown</b></font>   (<font color="#a52a2a"><b>Pixmap</b></font> <font color="#a020f0">$[fvwm_img]</font>/<font color="#a52a2a"><b>button</b></font>/maximize-activedown.png -- <font color="#a52a2a"><b>Flat</b></font>) \
        <font color="#a52a2a"><b>Inactive</b></font>     (<font color="#a52a2a"><b>Pixmap</b></font> <font color="#a020f0">$[fvwm_img]</font>/<font color="#a52a2a"><b>button</b></font>/inactive.png -- <font color="#a52a2a"><b>Flat</b></font>)
+ <font color="#008b8b">ButtonStyle</font> 1 - <font color="#a52a2a"><b>Clear</b></font>
+ <font color="#008b8b">ButtonStyle</font> 3 - <font color="#a52a2a"><b>Clear</b></font> <font color="#a52a2a"><b>MwmDecorMin</b></font>
+ <font color="#008b8b">ButtonStyle</font> 5 - <font color="#a52a2a"><b>Clear</b></font> <font color="#a52a2a"><b>MwmDecorMax</b></font>
+ <font color="#008b8b">TitleStyle</font> AllActive MultiPixmap \
        Main AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-main-active.xpm, \
        LeftEnd AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-leftend-active.xpm, \
        RightEnd AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-rightend-active.xpm, \
        UnderText AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-undertext-active.xpm, \
        LeftOfText AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-leftoftext-active.xpm, \
        RightOfext AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-rightoftext-active.xpm
+ <font color="#008b8b">TitleStyle</font> AllInactive MultiPixmap \
        Main AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-main-inactive.xpm, \
        LeftEnd AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-leftend-inactive.xpm, \
        RightEnd AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-rightend-inactive.xpm, \
        UnderText AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-undertext-inactive.xpm, \
        LeftOfText AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-leftoftext-inactive.xpm, \
        RightOfext AdjustedPixmap <font color="#a020f0">$[fvwm_img]</font>/decor/title-rightoftext-inactive.xpm
+ <font color="#008b8b">TitleStyle</font> -- <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">BorderStyle</font> <font color="#a52a2a"><b>Simple</b></font> -- <font color="#a52a2a"><b>NoInset</b></font> <font color="#a52a2a"><b>Flat</b></font>
+ <font color="#008b8b">ButtonStyle</font> <font color="#a52a2a"><b>All</b></font> -- <font color="#a52a2a"><b>UseTitleStyle</b></font>
</pre>

Now that you got the decor defined we need to tell the windows to use it
and also tell them what colorset to use. This is done as follows:

<pre>
<font color="#0000ff">#####</font>
<font color="#0000ff"># Window Styles</font>
<font color="#0000ff">###########</font>
<font color="#008b8b">Style</font> <font color="#ff00ff">&quot;*&quot;</font> <font color="#a52a2a"><b>UseDecor</b></font> MyDecor
<font color="#008b8b">Style</font> <font color="#ff00ff">&quot;*&quot;</font> <font color="#a52a2a"><b>Font</b></font> <font color="#ff00ff">&quot;xft:Sans:Bold:size=8:minspace=False:antialias=True&quot;</font>
<font color="#008b8b">Style</font> <font color="#ff00ff">&quot;*&quot;</font> <font color="#a52a2a"><b>BorderWidth</b></font> 1, <font color="#a52a2a"><b>HandleWidth</b></font> 1
<font color="#008b8b">Style</font> <font color="#ff00ff">&quot;*&quot;</font> <font color="#a52a2a"><b>MWMBorder</b></font>, <font color="#a52a2a"><b>FirmBorder</b></font>
<font color="#008b8b">Style</font> <font color="#ff00ff">&quot;*&quot;</font> <font color="#a52a2a"><b>Colorset</b></font> 4
<font color="#008b8b">Style</font> <font color="#ff00ff">&quot;*&quot;</font> <font color="#a52a2a"><b>HilightColorset</b></font> 3
<font color="#008b8b">Style</font> <font color="#ff00ff">&quot;*&quot;</font> <font color="#a52a2a"><b>BorderColorset</b></font> 5
<font color="#008b8b">Style</font> <font color="#ff00ff">&quot;*&quot;</font> <font color="#a52a2a"><b>HilightBorderColorset</b></font> 4
</pre>

These string of Styles tell every window to use the Decor MyDecor, along
with setting up the font, BorderWidth, (Hilight)Colorset and
(Hilight)BorderColorset the windows use. I like all my windows to look the same
but one could make different Colorsets and Decors to set up styles for particular applications.

