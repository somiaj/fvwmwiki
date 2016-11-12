#
# Pygments Lexer for Fvwm configuration files (fvwm2rc)
#
# 
# This is a simple highther that is not that accurate in terms of
# the inputs of subcommands. For example for Styles the first word
# of each item is treated as a correct style. In general the highlighter
# hilights based off of word placement more than if it is an actual Fvwm
# command. This was built for the wiki which should contain tested
# configurations and there should be no need to have the syntax higlighting
# verify if it is correct or not.
#

from pygments.lexer import RegexLexer, include, words, bygroups
from pygments.token import *

__all__ = ['FvwmLexer']

class FvwmLexer(RegexLexer):
    name = "f2vwm"
    aliases = ['fvwm']
    filenames = ['*.fvwm2rc']


    # Highlight: Keyword
    Command = ('Silent', 'Beep')
    # Highlight: Keyword Name
    CommandName = ('DestroyFunc', 'DestroyMenu', 'InfoStoreRemove',
                   'DestroyDecor', 'UseDecor', 'UnsetEnv', 'Popup',
                   'AddToDecor')
    # Highlight: Keyword Name String
    CommandNameString = ('InfoStoreAdd', 'SetEnv')
    # Highlight: Keyword (input)
    CommandInput = ('Exec', 'PipeRead', 'Break', 'Raise', 'WindowShade',
                    'Maximize', 'Iconify', 'FlipFocus', 'Focus', 'State',
                    'Title', 'Refresh', 'Restart', 'Quit', 'WindowList',
                    'Nop', 'Close', 'Delete', 'Destroy', 'Stick', 'Resize', 'Move',
                    'Lower', 'Layer', 'MoveToDesk', 'Echo', 'MoveThreshold',
                    'DesktopName', 'DesktopSize', 'EdgeScroll', 'EdgeResistance',
                    'EdgeThickness', 'EwmhBaseStruts', 'DefaultFont',
                    'OpaqueMoveSize', 'HideGeometryWindow', 'XorValue',
                    'IgnoreModifiers', 'ClickTime', 'MoveThreshold', 'GotoDesk',
                    'ImagePath', 'DefaultColorset', 'StrokeFunc', 'WarpToWindow',
                    'Schedule', 'Deschedule', 'MoveToPage', 'BugOpts', 'Read',
                    'GotoDeskAndPage')
    # Highlight: Keyword Name (input)
    CommandNameInput = ('SendToModule', 'Module', 'Menu', 'Function', 'KillModule')

    # Highlight: Keyword (conditions)
    Conditional = ('Test', 'TestRc', 'Current', 'All', 'ThisWindow', 'Next',
                       'Prev', 'Any', 'None', 'Pick', 'PointerWindow', 'WindowList')


    tokens = {
        # Common Filters
        'strings': [
            (r'\$\[[a-zA-Z0-9*_\-.]+\]', Name.Variable),
            (r'\$[a-zA-Z0-9*_\-.]*', Name.Variable),
        ],

        # Main Loop
        'root': [
            (r'\s+', Text), # Removes any whitespace
            (r'#.*\n', Comment), # Rest of line is comment

            # Strings
            include('strings'),

            # Trigger Style State
            (r'(Style|MenuStyle)(\s+)(\S+)', bygroups(Keyword, Text, String), 'style'),
            (r'WindowStyle\s+', Keyword, 'style'),
            (r'(Colorset\s+)(\d+)', bygroups(Keyword, Name), 'style'),
            (r'(Colorset\s+)(\$\S+\s+)', bygroups(Keyword, Name.Variable), 'style' ),

            # Conditional Statements
            (words(Conditional, suffix='(\s+\()'),
             bygroups(Keyword, Text), 'conditions'),
            (words(Conditional, suffix='\s+'), Keyword),

            # Highlight Commands
            (words(Command), Keyword),
            (words(CommandNameString, suffix='(\s+)(\S+)(\s+)(.*)$'),
             bygroups(Keyword, Text, Name, Text, String)),
            (words(CommandName, suffix='(\s+)(\S+)'), bygroups(Keyword, Text, Name)),
            (words(CommandNameInput, suffix='(\s+)(\S+)'),
             bygroups(Keyword, Text, Name), 'input'),
            (words(CommandInput, suffix='$'), Keyword),
            (words(CommandInput, suffix='\s+'), Keyword, 'input'),

            # AddToFunc Syntax
            (r'(AddToFunc\s+)([a-zA-Z0-9]+)(\s+[ICDHM])',
             bygroups(Keyword, Name, String)),
            (r'(AddToFunc\s+)([a-zA-Z0-9]+)',
             bygroups(Keyword, Name)),
            (r'(\+\s+)([ICDHM])', bygroups(Text, String)),

            # Menus
            (r'(AddToMenu\s+)([a-zA-Z0-9]+)$', bygroups(Keyword, Name)),
            (r'(AddToMenu\s+)([a-zA-Z0-9]+)(\s)',
             bygroups(Keyword, Name, Text), 'menuitem'),
            (r'\+\s+', Text, 'menuitem'),

            # Bindings
            ('(Key|Mouse)(\s*\()(.*)(\))(\s+\S+\s+)(\S+\s+\S+)',
             bygroups(Keyword, Text, String, Text, Name, String.Other)),
            ('(Key|Mouse)(\s+\S+\s+)(\S+\s+\S+)',
             bygroups(Keyword, Name, String.Other)),
            ('(Stroke\s+)(\s*\()(.*)(\))(\d+\s+\d+\s+\S+\s+\S+\s+)',
             bygroups(Keyword, Text, String, Text, String.Other)),
            ('(Stroke\s+)(\d+\s+\d+\s+\S+\s+\S+\s+)',
             bygroups(Keyword, String.Other)),

            # Module Alias
            (r'(DestroyModuleConfig\s+)([^:]+)(:\s*)(\S+)$',
             bygroups(Keyword, Name.Entity, Text, String.Other)),
            (r'(\*[a-zA-Z0-9\-$]+:\s+)(\()([^,\)]+)',
             bygroups(Name.Entity, Text, String.Other ), 'buttons'),
            (r'(\*[a-zA-Z0-9\-$]+:\s+)(\S+)', bygroups(Name.Entity, Keyword), 'input'),

            # No Match: Highlight as Name (input).
            (r'[^\s\n]+', Name, 'input')
        ],
        # Style state 
        # Items are ended by commas. Items are Highlisted as
        #   Default: Keyword Input,
        #   FvwmCommandName: Keyword Name,
        #   FvwmCommandNameString: Keyword Name String,
        # Ends at new line. Can be exteded with \.
        'style': [
            (r',(\s+)\\\n', Text),
            (r'\n', Text, "#pop"),
            (r',', Text),
            (r'\s+', Text),
            (words(CommandName, suffix='(\s+)([^,\n\s]*)'),
             bygroups(Keyword, Text, Name)),
            (r'(!?[a-zA-Z0-9]*)([^,\n]*)', bygroups(Keyword, String.Other))
        ],
        # Parses menu items for & and icons, %png% or *png*
        'menuitem': [
            (r'\s', Text, "#pop"),
            (r'"', String, 'menuitemquote'),
            (r'[^&%*\s$]+', String),
            (r'&', String.Other),
            (r'%.*%', String.Other),
            (r'\*.*\*', String.Other),
            include('strings')
        ],
        'menuitemquote': [
            (r'"', String, "#pop:2"),
            (r'[^&%*$"]+', String),
            (r'&', String.Other),
            (r'%.*%', String.Other),
            (r'\*.*\*', String.Other),
            include('strings')
        ],
        # FvwmButtons List
        'buttons': [
            (r'\\', Text),
            (r'\)', Text, "#pop"),
            (r',?\s+', Text),
            (r'\(', Text, 'nested'),
            (r'(!?[a-zA-Z0-9]+)', Keyword, 'inputbutton')
        ],
        'inputbutton': [
           (r'\\', Text),
           (r'\)', Text, "#pop:2"),
           (r',', Text, "#pop"),
           (r'\s+', Text),
           (r'\(', Text, 'nested'),
           include('strings'),
           (r'[^,\)\n\$]*', String.Other),
        ],
        'nested': [
            (r'\)', Text, "#pop"),
            (r'\s+', Text),
            (r'\(', Text, "#push"),
            (r'[^\)\n]*', String.Other)
        ],
        # Condition List
        'conditions': [
            (r'\\\n', Text),
            (r'\n', Text, "#pop"),
            (r'\)', Text, "#pop"),
            (r',?\s+', Text),
            include('strings'),
            (r'(!?[a-zA-Z0-9_]+)', Name.Attribute, 'inputcondition')
        ],
        'inputcondition': [
           (r'\n', Text, "#pop:2"),
           (r'\)', Text, "#pop:2"),
           (r',', Text, "#pop"),
           (r'\s+', Text),
           include('strings'),
           (r'[^,\)\n\$]*', String.Other),
        ],
        # Input List
        'input': [
           (r'\\\n', Text),
           (r'\n', Text, "#pop"),
           (r'\s+', Text),
           include('strings'),
           (r'[^\n\$\\]+', String.Other)
        ],
        'input2': [
           (r'\\\n', Text),
           (r'\n', Text, "#pop:2"),
           (r'\s+', Text),
           include('strings'),
           (r'[^\\\n\$]+', String.Other),
        ],

    }
