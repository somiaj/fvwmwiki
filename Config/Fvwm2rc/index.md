---
layout : wiki
title : Fvwm2rc
type : config
weight : 1000
description : |
  Fvwm is configured through a configuration file located at ~/.fvwm/config
  (default). Also as the Fvwm2rc or .fvwm2rc file, this page explains the
  basics of the configuration file.

---
* TOC
{:toc}

# The Fvwm2rc file

Fvwm is configured through an extensive config file. At the release of Fvwm 2,
the config file was located at ~/.fvwm2rc to not conflict with ~/.fvwmrc for Fvwm 1.
It then moved to ~/.fvwm/.fvwm2rc and finally to ~/.fvwm2rc/config (although some old
locations are still supported).

## Why use a config file?

This is best explained by [In the beginning was ...](
http://www.xteddy.org/fvwm/user_enumerate.html).

In short Fvwm has hundreds of options available. The most efficient way to configure
them and build a custom setup is to use a configuration file. Fvwm now comes with
a default config file you can use as a base and edit to build your own. With that
and the examples in this Wiki you, and a little bit of time invested, you can be
on your way to building your own configuration.

## Starting Fvwm

When Fvwm starts it will look for a config file in one of the following locations.
As soon as it finds one of them in that order, it stops looking:

    $HOME/.fvwm/config
    [INSTALL_PREFIX]/share/fvwm/config

    $HOME/.fvwm/.fvwm2rc
    $HOME/.fvwm2rc
    [INSTALL_PREFIX]/share/fvwm/.fvwm2rc
    [INSTALL_PREFIX]/share/fvwm/system.fvwm2rc
    /etc/system.fvwm2rc

If it doesn't find any configuration file in any of those locations, it will load the
default configuration located at

    [INSTALL_PREFIX]/share/fvwm/default-config/

If you have installed from source without any prefix option [INSTALL_PREFIX]
will be /usr/local. Distrubutions may use other prefixes.  You can, of
course, find out the absolute path by running:

    fvwm-config -d

If you want to start from a blank config (and have a very minimal setup) just
use a blank $HOME/.fvwm/config file:

    touch $HOME/.fvwm/config

If you want to use the default config and start editing it you can either use the
CopyConfig script in the menu if currently running the default configuration file
or copy it to your $HOME as

    cp [INSTALL_PREFIX]/share/fvwm/default-config/config $HOME/.fvwm/config

Once you have a config file in place you can start to edit it with the text
editor of your choice. For a more detailed explination of what happens
after Fvwm finds a config file and Reads it see [/Tips/FvwmStartup](
{{ "/Tips/FvwmStartup" | prepend: site.baseurl }}).


## Syntax history

FVWM's configuration file has evolved since FVWM was conceived.  Back in
the 1.24.X days of FVWM, the order of its config file was important.
FVWM1 expected certain features to be in place.  The syntax was radically
different as well.  For example, Style lines had to have the name of the
window/class/resource quoted as in:

{% highlight fvwm %}
Style "myApplication" Icon /some/icon/name.xpm
{% endhighlight %}

In the same way, the declaration of Functions was quite specific:

{% highlight fvwm %}    
Function "Some-Function"
    Exec "I" some_program &
    Exec "I" some_other_program &
EndFunction
{% endhighlight %}
    
Thankfully though things have moved on since then, in that such stringent
quoting and ordering rules have been resolved. See [/Config/Syntax](
{{ "/Config/Syntax" | prepend: site.baseurl }}) for the basics on
the current syntax.

## FVWM 2.X.Y and beyond

### The Single-file approach

Since FVWM2, the way the config file for FVWM is structured, is completely
down to the user.   One approach is to lump everything in one file.  This
approach tends to be the most common -- perhaps a hangover effect from the
old FVWM 1.X days (happy days!).  The main approach here though is that
it makes distribution slightly easier from one machine to another, or to
others'.  

A typical structure for this sort of file is:

* General hints such as ImagePath, EWMH* stuff, etc.
* Style lines
* Decors
* Functions
* Menus
* Key/Mouse bindings
* Module commands

But that is just one possibility, you can shove FVWM commands wherever you
like, and although the order doesn't matter as to where each compoent
goes, the sub-ordering of them does.  So for instance:

1. Any variables via the use of ''InfoStoreAdd'' '''must be
   declared at the top of your file, since the order the commands are listed
   within the .fvwm2rc file is the order they're processed in.  So anything
   depending on these environment variables present, must appear after
   them.
2. The same principle applies for ''ImagePath'' from 1., above.
3. The sub-ordering of Styles is important: [/Config/StyleTips](
   {{ "/Config/StyleTips" | prepend: site.baseurl }}).

### Multi-file approach

Conversely to the single-file approach, the multi-file approach advocates
the use of modualarity to the way one's FVWM setup is produced.  The
advantage of this is that each file will only ever house a limited set of
commands, and will hold a logical grouping of commands.  

As explained above, FVWM looks for its files in
~/.fvwm -- so in that way one can separate out into different files what
functionality is needed and then just call them from ~/.fvwm/config. As
with the structure above you might decide to do (with file names in
brackets):

* General hints such as ImagePath, EWMH* stuff, etc.   [options.fvwm2rc]
* Style lines                                          [styles.fvwm2rc]
* Decors                                               [decors.fvwm2rc]
* Functions                                            [functions.fvwm2rc]
* Menus                                                [menus.fvwm2rc]
* Key/Mouse bindings                                   [bindings.fvwm2rc]
* Module commands                                      [modules.fvwm2rc]

In that way, the only thing you would need to add to ~/.fvwm/config
is lines which make read calls those files, hence:

{% highlight fvwm %}
# Example ~/.fvwm/config file.
#

# InfoStore Vars here.
InfoStoreAdd RXVT "rxvt +sb -ls -fg white -bg black"

# Add StartFunction here to ensure it gets read before anything else.
DestroyFunc StartFunction
AddToFunc   StartFunction
+ I Module FvwmEvent foo
+ I Exec exec bar
    
# Now look at everything we have in the separate files.
Read $./options.fvwm2rc
Read $./bindings.fvwm2rc
# Etc ...
{% endhighlight %}

### Is there a "better" approach?

No, not really.  It depends what is meant by better in this context
though.  There isn't really any real advantage over each of the methods.
The single-file approach is good in that there's only ever one file to
edit.  The multi-file approach is good for those people with tidier minds,
and who like to switch different components of their configuration over,
perhaps via a symlink (essentially reinventing the wheel a la
fvwm-themes).

