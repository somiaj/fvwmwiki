---
layout : wiki
title : Syntax
type : config
weight : 950
description : |
  The basic syntax of the configuration file.

---

# Fvwm2rc Configuration Syntax

The configuration file syntax is a command followed
by a list of options. Commands are keywords and options
are generally lists separated by spaces, comma separated lists,
and sometimes inside grouping symbols (). KeyWords generally follow
the first letter of each subword is capitalized for convention,
but the case is not important.

Commands are read on a line by line basis, and if the last character
of a line is \\, the line is extended to the next. Once a command is
Read, the configuration is changed or action is executed. Most the
time Fvwm will not wait for a command to complete to move on. This can
sometimes lead to race conditions -- [/Config/FunctionSynchronisation](
{{ "/Config/FunctionSynchronisation" | prepend: site.baseurl }}).

Commands can be sent to Fvwm while it is running though [/Modules/FvwmConsole](
{{ "/Modules/FvwmConsole" | prepend: site.baseurl }}) or [/Modules/FvwmCommandS](
{{ "/Modules/FvwmCommandS" | prepend: site.baseurl }}). This gives one
the ability to test out commands before saving them to the configuration file
and not having to Restart Fvwm as often.

Here are some examples commands. Everything after
a "#" is a comment and will be ignored by Fvwm.

{% highlight fvwm %}
# DefaultFont
DefaultFont "xft:Sans:size=10:antialias=True"

# Desktop
DesktopName 0 Main
DesktopSize 3x2

# Default Styles
Style * SloppyFocus, MouseFocusClickRaises, \
        Colorset 1, HilightColorset 2

# Run an xterm
Exec exec xterm

# Iconfiy all windows except the one with focus
All (CurrentPage, !Iconified, !Focused) Iconify
{% endhighlight %}

Each line is read in order and changes the current setting
of Fvwm. For the most part the order of the lines is personal
preference, though there are some exceptions. Variables need to
be set with InfoStoreAdd or SetEnv before they are used. Functions and
Menus need to be fully read before the point at which you
call them. If there are conflicting Styles (see [/Config/StyleTips](
{{ "/Config/StyleTips" | prepend: site.baseurl }})) that match the same
window, the most recent (last) Style is used.

Fvwm commands can run system applications, configuring a setting,
open menus, configure and run a module,  preforming an action on
a window -- such as Maximize, Move, Iconify -- and so on. Fvwm also
provides ways to write custom functions and thus custom commands by
stringing together chains of Fvwm commands along with the help of
shell scripts.

The most complete resource for information about a command, its syntax
and capabilities is the man page. If you know the command you can search
though the manpage for it to find more info. You can also find the manpage
online [here](http://fvwm.org/documentation/manpages/). The online version
contains a table of contents to make finding info in the manpage a little easier.

The [FvwmWiki]({{ "/" | prepend: site.baseurl }}) contains a collection of config
examples and their descriptions. Here is a starting point: [/Config](
{{ "/Config" | prepend: site.baseurl }})

Fvwm 2.6.7 comes with a [/DefaultConfig]({{ "/DefaultConfig" | prepend: site.baseurl }})
that can be used as an example or starting point when building your own config.

