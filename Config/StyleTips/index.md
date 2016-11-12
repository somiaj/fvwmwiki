---
layout : wiki
title : Style Tips
type : config
weight : 850
description : |
  Here is some tips for configuring different windows using Styles.
  This is taken from <a href="http://linuxgazette.net/127/adam.html">
  This article</a> by Thomas Adam.

---
* TOC
{:toc}

# FVWM: How Styles are Applied

*This is a copy of the following article by Thomas Adam:
<http://linuxgazette.net/127/adam.html>*

## Introduction

Configuring FVWM can seem like a chore at times. Indeed, there are
certain aspects of it that are easy - and some that are less so. I've been
helping people configure FVWM for some time now, and while I have delved
into some of the more esoteric regions of FVWM, it seems that many people
find the use of Style lines the hardest aspect to grasp.
Hopefully this article will help clarify things.

## What are Style lines?

Style lines (in FVWM parlance) are those lines in an FVWM
configuration file which apply some specific style to a window. It could
be, for instance, that one would want all windows called *foobar* to
be sticky by default. Hence in one's .fvwm2rc file:

{% highlight fvwm %}
Style foobar Sticky
{% endhighlight %}

... would ensure that fact. One can also add multiple properties
to a given window. For instance, it might be desirable that the same window [\[1\]](#1),
*foobar*, have no visible title and a border width of eight pixels. This
can be expressed as:

{% highlight fvwm %}
Style foobar Sticky, !Title, BorderWidth 8
{% endhighlight %}

More style lines can then be added, line by line, with a
specific window for each style. Here's an example:

{% highlight fvwm %}
Style amble*  !Borders
Style Login?  CenterPlacement
Style Gvim    Title, !Sticky
Style urlview StartsOnPage 1 1, SkipMapping, Icon wterm.xpm, !Closable
Style irssi   StartsOnPage 1 1, SkipMapping, Icon 32x32-kde/chat.xpm, \
              !Closable, StickyAcrossDesks
{% endhighlight %}

FVWM also allows for the use of wildcards when matching a
window's name as in the above example. The '*' matches for anything
after what precedes it, whereas the '?' matches a single
character.

What's even more important is that the matching of Style lines
is *case sensitive*. This means that for the
following, both are separate entities:

{% highlight fvwm %}
Style Window1 BorderWidth 23
Style WINdoW1 BorderWidth 23
{% endhighlight %}

## How FVWM Interprets Styles

So far, everything's going great. Window names are being added as
style options, and everything's working just fine - until you have a
series of lines which look like the following:

{% highlight fvwm %}
Style myapp* NoStick, NoTitle
Style Fvwm* NoBorders, NoTitle, CirculateSkip, Sticky
Style Mozilla* NoTitle
Style Firefox* NoTitle
{% endhighlight %}

At first glance there's nothing wrong with them. Sure, FVWM is doing
exactly what you asked for... except that '*' is a greedy match, which is
what one would expect in using it. In the example above, Mozilla has, in
theory, only been told to display no title as a Style directive - but it
may also produce entirely unexpected results due to that greediness. As an
example, it may match an earlier declaration (e.g., 'Style Fvwm*') if that
string exists in the window title.

In all of the problems encountered with style lines, this has to be the
most common.  The reason for this isn't that Mozilla or Firefox are
misbehaving, but usually that there's a lack of understanding of
how Style lines are applied.

With applications such as Mozilla and Firefox, titles are dynamic -
they often change as a tab or page loads in them.  Assuming that we're
using the style lines from above, and that we're looking at, say, a webpage
that has the title: *"Fvwm: my nice screenshot"*:

{% highlight fvwm %}
Style Fvwm* NoBorders, NoTitle, CirculateSkip, Sticky
{% endhighlight %}

...this matches (in part) some of Firefox's title [<a href="#1">1</a>].
If one were to then restart FVWM with this page still showing in Firefox
(or issue a *Recapture* command), then the window would become
sticky - annoying, and certainly not what we want. Most people will also
try something like this to remedy the situation:

{% highlight fvwm %}
Style *Firefox* NoBorders
{% endhighlight %}

...which also has the same problems, and perhaps even more so,
since that's matching 'Firefox' anywhere within the title of a
window.

To get around this, something unique needs to be used. With dynamically
changing titles such as those in a web browser, specifying the full name of
the window just won't work. However, FVWM also allows us to match by a
window's class, as well.

Take Firefox. That will either have a class of Firefox-bin
or Gecko - which will provide a unique class match.

The reason one wants to match on a window's class in this
instance is that it's less ambiguous than the title of the window,
which might be something like this:

    Fvwm Forums :: Post a reply - Mozilla Firefox

There are a few ways to obtain a specific window's class.
Perhaps the preferred option is using the module *FvwmIdent*,
although window manager-agnostic commands such as *xwininfo*
and *xprop* can also be used. Using the window class instead
of the title, the previous style command would be replaced
with:</p>

{% highlight fvwm %}
Style Gecko NoTitle
{% endhighlight %}

You can be fairly well assured that the Class of a window tends
to be unique to that application (the exceptions are things like
RXVT which sometimes have been known to set their class to that of
XTerm.) The problem here though is that the same application will
generally always have the same Class.

Indeed, you might be wondering how FVWM knows which attribute
style lines match. Truth is, it doesn't really know, however FVWM
defaults to cycling through a known series of window attributes.
Hence, FVWM will match your window's style line thus:

    Title --> Class --> Resource

So, FVWM checks the title of a window first. If a match is
unsuccessful, it will then look at the Class, and if that fails, it
will then look at the Resource of that window for a match. By and
large, where wildcards are used in style lines -- it's normally the
window's title that gets matched in the first instance.

## Remedying the Situation

There are other considerations that need to be taken into
account. Style lines are ANDed. That is, for successive lines that
are specified one after the other for the same application, both
lines are considered. So for the following:

{% highlight fvwm %}
Style foo Sticky
Style foo !Title
{% endhighlight %}

The window 'foo' would be displayed without a title *and* would
become sticky. Because of this, the ordering of style lines is VERY
important to prevent race conditions, or other oddities that can creep
in.

But that's not the entire story, either. Specificity is important. Yes,
for the *same* window title, the styles are ANDed together. The
order that the style lines appear within your .fvwm2rc also matters. For
those of you who are familiar with the concepts of Object Oriented
programming, you can consider style lines as following the rules for
inheritance. The rule of thumb for style lines is:

**"Always generalise, before you specialise."**

That means, aggregate styles for all windows (Style * [...])
before you specify the style lines for specific applications.
FVWM's parsing is quite literal in that sense. When FVWM parses its
configuration file, it reads it line-by-line. This is why it's
important to think of Style lines as an inheritance model.

Hence, if you wanted all windows to be sticky, and a window
whose name is 'foofoo' to not be sticky and have no borders, the
correct order to write that in would be:

{% highlight fvwm %}
Style * Sticky
Style foofoo !Sticky, !Borders
{% endhighlight %}

Note that because we had previously declared a global style in which
all windows are sticky, it is necessary to negate that Sticky
condition for the specific application. Otherwise it would be
"inherited".

Writing that the other way around, however, gets one into
trouble:

{% highlight fvwm %}
Style foofoo !Sticky, !Borders
Style * Sticky
{% endhighlight %}

The greedy match of "*" for all windows, irrespective of the
specific condition for 'foofoo' above, means that the greedy match
takes precedent.

It was mentioned earlier that style lines are ANDed. This is
indeed true, and you can see that in operation. But we have another rule
that applies: given two contradictory Style 
statements, the latter one always wins. So, for example (and I see
this a lot in people's configs), assume you had written this:

{% highlight fvwm %}
Style * SloppyFocus
Style * FocusFollowsMouse
{% endhighlight %}

... because they're both focus policies being applied to all
windows, FocusFollowsMouse would win because it was the last one
specified.

## Conclusion
So, to recap:
+ Style lines are matched on a case-sensitive basis.
+ When specifying a window to be matched, the order of operation
  is: Name --> Class --> Resource.
+ Specificity is important. Generalise the styles for all
  programs at the top, and define specific window styles lower down.

---

<a name="1"></a>

__[1]__:
Although the term *title* is used throughout this
document, it should be noted that it's really the window's
*name* that is used (see xprop(1)). For convenience's sake,
the window title is often set from the name of the window.
