from pygments.lexer import RegexLexer, bygroups, using, include
from pygments.token import (
    Text,
    Comment,
    Operator,
    Keyword,
    Name,
    String,
    Number,
    Punctuation,
)

class RONLexer(RegexLexer):
    """
    Pygments lexer for RON (Rusty Object Notation) files.
    """

    name = 'RON'
    aliases = ['ron']
    filenames = ['*.ron']

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),

            # Comments
            (r'//[^\n]*', Comment.Single),
            (r'/\*', Comment.Multiline, 'block-comment'),

            # Strings
            (r'r#{0,10}"', String.Double, 'raw-string'),
            (r'rb#{0,10}"', String.Double, 'raw-byte-string'),
            (r'b"', String.Byte, 'byte-string'),
            (r'"', String.Double, 'string'),

            # Characters
            (r"'", String.Char, 'char'),

            # Numbers
            (r'[-+]?(?:0b[01_]+|0o[0-7_]+|0x[\da-fA-F_]+|\d[\d_]*)(?:[iu](?:8|16|32|64|128))?', Number.Integer),
            (r'[-+]?(?:\d[\d_]*\.\d[\d_]*|\.\d[\d_]+|\d[\d_]*)(?:[eE][-+]?\d[\d_]*)?(?:f(?:32|64))?', Number.Float),

            # Keywords
            (r'\b(?:true|false|None|Some)\b', Keyword.Constant),

            # Operators and Punctuation
            (r'[{}()\[\],.:]', Punctuation),
            (r'[+-/*=<>!&|^%~]', Operator),

            # Identifiers
            (r'\b[rR]#[a-zA-Z0-9_.+-]+\b', Name.Variable),
            (r'\b[A-Za-z_][\w]*\b', Name),

            # Anything else
            (r'.', Text),
        ],

        'block-comment': [
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[^/*]+', Comment.Multiline),
            (r'[/*]', Comment.Multiline),
        ],

        'string': [
            (r'\\[nrt0\'"\\]', String.Escape),
            (r'\\x[0-9a-fA-F]{2}', String.Escape),
            (r'\\u[0-9a-fA-F]{4,6}', String.Escape),
            (r'"', String.Double, '#pop'),
            (r'[^"\\]+', String.Double),
            (r'.', String.Double),
        ],

        'raw-string': [
            # Match the ending quote with the same number of hashes
            (r'"#{0,10}', String.Double, '#pop'),
            (r'[^"#]+', String.Double),
            (r'[#""]', String.Double),
        ],

        'byte-string': [
            (r'\\[nrt0\'"\\]', String.Escape),
            (r'\\x[0-9a-fA-F]{2}', String.Escape),
            (r'"', String.Byte, '#pop'),
            (r'[^"\\]+', String.Byte),
            (r'.', String.Byte),
        ],

        'raw-byte-string': [
            # Match the ending quote with the same number of hashes
            (r'"#{0,10}', String.Byte, '#pop'),
            (r'[^"#]+', String.Byte),
            (r'[#""]', String.Byte),
        ],

        'char': [
            (r"\\[nrt0'\"\\]", String.Escape),
            (r"\\x[0-9a-fA-F]{2}", String.Escape),
            (r"\\u[0-9a-fA-F]{4,6}", String.Escape),
            (r"'", String.Char, '#pop'),
            (r'[^\'\\]', String.Char),
            (r'.', String.Char),
        ],
    }

