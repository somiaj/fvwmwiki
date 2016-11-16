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

import re

from pygments.lexer import RegexLexer, include, words, bygroups
from pygments.token import *

from pygments.lexers._openedge_builtins import OPENEDGEKEYWORDS

__all__ = ['FvwmLexer']

class FvwmLexer(RegexLexer):
    name = "Fvwm"
    aliases = ['fvwm']
    filenames = ['*.fvwm2rc']

    flags = re.IGNORECASE | re.MULTILINE

    # Highlight: Keyword
    Command = ('Silent', 'Beep', 'Nop', 'RaiseLower')
    # Highlight: Keyword Name
    CommandName = ('DestroyFunc', 'DestroyMenu', 'InfoStoreRemove',
                   'DestroyDecor', 'UnsetEnv', 'AddToDecor',
                   'AddToMenu', 'AddToFunc')
    # Highlight: Keyword Name String
    CommandNameString = ('InfoStoreAdd', 'SetEnv')
    # Highlight: Keyword (input)
    CommandInput = ('Exec', 'PipeRead', 'Break', 'Raise', 'WindowShade',
                    'Maximize', 'Iconify', 'FlipFocus', 'Focus', 'State',
                    'Title', 'Refresh', 'Restart', 'Quit', 'WindowList',
                    'Close', 'Delete', 'Destroy', 'Stick', 'Resize', 'Move',
                    'Lower', 'Layer', 'MoveToDesk', 'Echo', 'MoveThreshold',
                    'DesktopName', 'DesktopSize', 'EdgeScroll', 'EdgeResistance',
                    'EdgeThickness', 'EwmhBaseStruts', 'DefaultFont',
                    'OpaqueMoveSize', 'HideGeometryWindow', 'XorValue',
                    'IgnoreModifiers', 'ClickTime', 'MoveThreshold', 'GotoDesk',
                    'ImagePath', 'DefaultColorset', 'StrokeFunc', 'WarpToWindow',
                    'Schedule', 'Deschedule', 'MoveToPage', 'BugOpts', 'Read',
                    'GotoDeskAndPage', 'WindowList', 'Read', 'AnimatedMove',
                    'Wait')
    # Highlight: Keyword Name (input)
    CommandNameInput = ('SendToModule', 'Module', 'Menu', 'Function', 'KillModule',
                        'Popup', 'Mouse', 'Colorset')

    # Highlight: Keyword (conditions)
    Conditional = ('Test', 'TestRc', 'Current', 'All', 'ThisWindow', 'Next',
                       'Prev', 'Any', 'None', 'Pick', 'PointerWindow', 'WindowList')

    DecorStates = ('ActiveUp', 'ActiveDown', 'Active', 'InactiveUp', 'InactiveDown',
                   'Inactive', 'ToggledActiveUp', 'ToggledActiveDown', 'ToggledActive',
                   'ToggledInactiveUp', 'ToggledInactiveDown', 'ToggledInactive',
                   'AllNormal', 'AllToggled', 'AllActive', 'AllInactive', 'AllUp', 'AllDown',
                   'AllActiveUp', 'AllActiveDown', 'AllIncativeUp', 'AllInactiveDown',
                   'State')
    DecorStyles = ('MultiPixmap', 'Pixmap', 'AdjustedPixmap', 'ShrunkPixmap',
                   'StretchedPixmap', 'TiledPixmap', 'HGradient', 'VGradient',
                   '?Gradient', 'DGradient', 'BGradient', 'SGradient', 'CGradient',
                   'RGradient', 'YGradient', 'Colorset', 'Solid', 'Simple', 'Default',
                   'Vector', 'MiniIcon', 'Centered', 'LeftJustified', 'Height',
                   'RightJustified', 'MinHeight', 'Style')
    DecorNames = ('Main', 'LeftMain', 'RightMain', 'UnderText', 'LeftButtons',
                  'LeftEnd', 'LeftOfText', 'RightOfText', 'RightEnd', 'RightButtons',
                  'Buttons')
    DecorFlags = ('Flat', 'Raised', 'Sunk', 'UseTitleStyle', 'UseBorderStyle',
                  'MwmDecorMax', 'MwmDecorMin', 'MwmDecorStick', 'MwmDecorLayer',
                  'MwmDecorMenu', 'MwmDecorStick', 'Clear', 'HiddenHandles',
                  'NoInset', 'Flag')

    tokens = {
        # Common Filters
        'strings': [
            (r'\$\[[a-zA-Z0-9*_\-.]+\]', Name.Variable),
            (r'\$[a-zA-Z0-9*_\-.]*', Name.Variable),
        ],
        'commands': [
            (words(Command, suffix="($|\s+)"), Keyword),
            (words(CommandName, suffix="(\s*$|\s+\S+)"),
             bygroups(Keyword, Name)),
            (words(CommandNameString, suffix="(\s+\S+\s+)(.*)"),
             bygroups(Keyword, Name, String)),
            (words(CommandInput, suffix='$'), Keyword),
            (words(CommandInput, suffix='\s+'), Keyword, 'input'),
            (words(CommandNameInput, suffix='$'), Keyword),
            (words(CommandNameInput, suffix='(\s+\S+)'),
             bygroups(Keyword, Name), 'input'),
        ],
        'commands-input': [
            (words(Command, suffix="($|\s+)"), Keyword),
            (words(CommandName, suffix="(\s+\S+)"),
             bygroups(Keyword, Name)),
            (words(CommandName, suffix="\s*$"), Keyword),
            (words(CommandNameString, suffix="(\s+\S+\s+)(.*)"),
             bygroups(Keyword, Name, String)),
            (words(CommandNameInput, suffix='\s*$'), Keyword),
            (words(CommandNameInput, suffix='(\s+\S+)'),
             bygroups(Keyword, Name)),
            (words(CommandInput, suffix='($|\s+)'), Keyword),
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

            # Window Styles
            (r'(\+\s+)?(ButtonStyle\s+)(\S+)(\s+-\s+)',
             bygroups(Text, Keyword, Name, Keyword), 'decor3'),
            (r'(\+\s+)?(ButtonStyle|AddButtonStyle)(\s+\w+\s+)',
             bygroups(Text, Keyword, Name), 'decor'),
            (r'(\+\s+)?(TitleStyle|AddTitleStyle|BorderStyle|ButtonStyle|AddButtonStyle)(\s+)',
             bygroups(Text, Keyword, Text), 'decor'),

            
            # AddToFunc Syntax
            (r'(AddToFunc\s+)([a-zA-Z0-9]+)(\s+[ICDHM])',
             bygroups(Keyword, Name, String)),
            (r'(AddToFunc\s+)([a-zA-Z0-9]+)',
             bygroups(Keyword, Name)),
            (r'(\+\s+)([ICDHM])', bygroups(Text, String)),

            # Menus
            (r'(AddToMenu\s+)([a-zA-Z0-9]+\s*\n)', bygroups(Keyword, Name)),
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
            (r'(DestroyModuleConfig\s+)([^:]+)(:\s*)(\S+\s*\n)',
             bygroups(Keyword, Name.Entity, Text, String.Other)),
            (r'(\*[a-zA-Z0-9\-$]+:\s+)(\()([^,\)]+)',
             bygroups(Name.Entity, Text, String.Other ), 'buttons'),
            (r'(\*[a-zA-Z0-9\-$]+:\s+)(\S+)', bygroups(Name.Entity, Keyword), 'input'),

           # Highlight Commands
            include('commands'),

            # No Match: Highlight as Name (input).
            (r'[^\s\n]+', Name, 'input')
        ],
        # Style state 
        # Ends at new line. Can be exteded with \.
        'style': [
            (r'\\\n', Text),
            (r'\s*\n', Text, "#pop"),
            (r',\s+', Text),
            (r'\s+', Text),
            (r'(!?[a-zA-Z0-9]*)([^,\n]*)', bygroups(Keyword.Type, String.Other))
        ],
        'decor': [
            (r'\\\n', Text),
            (r'\s*\n', Text, "#pop"),
            (r'\s*\)', Text, "#pop"),
            (r'\s+', Text),
            (words(DecorStates, suffix='($|\s+)'), String),
            (words(DecorStyles, suffix='($|\s+)'), Keyword.Type),
            (words(DecorNames, suffix='($|\s+)'), Name),
            (r'--', Keyword, 'decor2'),
            (r'-', String.Other),
            (r'\(', Text, "#push"),
            (r'[^\s()\-\n\\]+', String.Other),
        ],
        'decor2': [
            (r'\\\n', Text),
            (r'\)', Text, "#pop:2"),
            (r'\s*\n', Text, "#pop:2"),
            (r'\s+', Text),
            (words(DecorFlags, prefix='(!)?', suffix='($|\s*)'), Keyword.Type),
            (r'[^\s)\n\\]+', String.Other),
        ],
        'decor3': [
            (r'\\\n', Text),
            (r'\s*\n', Text, "#pop"),
            (r'\s+', Text),
            (words(DecorFlags, prefix='(!)?', suffix='($|\s*)'), Keyword.Type),
            (r'[^\s\n\\]+', String.Other),
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
            include('strings'),
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
           (r'\s*\n', Text, "#pop:2"),
           (r'\)', Text, "#pop:2"),
           (r',', Text, "#pop"),
           (r'\s+', Text),
           include('strings'),
           (r'[^,\)\n\$]*', String.Other),
        ],
        # Input List
        'input': [
           (r'\\\n', Text),
           (r'\s*\n', Text, "#pop"),
           (r'\s+', Text),
           (r'["\'()]', Text),
           include('commands-input'),
           include('strings'),
           (r'[^\n\s$\\"\'()]+', String.Other)
        ],
        'input2': [
           (r'\\\n', Text),
           (r'\s*\n', Text, "#pop:2"),
           (r'\s+', Text),
           (r'["\'()]', Text),
           include('commands-input'),
           include('strings'),
           (r'[^\\\n$\s"\'()]+', String.Other),
        ],

    }
