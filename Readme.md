---
layout : wiki
title : Readme
---
# FvwmWiki at GitHub

This is the mostly Markdown source to build the FvwmWiki, located at
<http://fvwmforums.org/wiki>.

## Building the site with Jekyll

This static site is built from the Markdown files using Jekyll
(<https://jekyllrb.com/>). To build the wiki you need a copy of
the source (<https://github.com/somiaj/fvwmwiki>) and Jekyll installed.
In which case the wiki can be built using

    fvwmwiki# jekyll build

You can build and run a local server of the wiki with

    fvwmwiki# jekyll serve

The static .html for the Wiki is built in fvwmwiki/\_site. If using
`jekyll serve`, you will be given a local address to view the Wiki
on, and any changes you made will be built and updated to be viewed.

## Syntax Highlighting

The Fvwm configuration syntax highlighting is done through using pygments
(<http://pygments.org/>), which is no longer the default highlighter used
by Jekyll 3 onwards. To use pygments you will need to have the python2
package pymgnets installed along with the ruby package pygments.rb to
translate the python to ruby for jekyll.

Additionally you will have to install a copy of the Lexer used to create
the Fvwm syntax highlighting. To do this you will need python2 and pygments
installed, then install the lexer with (as root) from inside the FvwmLexer
directory:

    fvwmwiki/FvwmLexer# sudo python setup.py develop

This basically creates links for python to use the python script
FvwmLexer/fvwmlexer/lexer.py with pygments. pygments will be using
the script in the source, so any changes you make to it will update the
syntax highlighting -- note you will have to kill the jekyll server
and then run `jekyll serve` to have any changes take affect.

To test that the lexer is installed (or to use it for your own config
files) run

    # pygmentize -l fvwm -f html -O full config.fvwm2rc > config.html

You can uninstall the lexer with easy_install

    # easy_install -m fvwmlexer

This will leave an fvwmlexer.egg-link file on your system
(in /usr/local/lib/python/dist-packages here).

__Todo__: Convert the pygment lexer to rogue (default highlighter
written in ruby) and get it included in the rouge source
<https://github.com/jneen/rouge> so the highlighting can be used
on github.io.

