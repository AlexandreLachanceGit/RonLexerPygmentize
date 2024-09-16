from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from ronlexer import RONLexer

ron_code = '''
GameConfig( // optional struct name
    window_size: (800, 600),
    window_title: "PAC-MAN",
    fullscreen: false,

    mouse_sensitivity: 1.4,
    key_bindings: {
        "up": Up,
        "down": Down,
        "left": Left,
        "right": Right,

        // Uncomment to enable WASD controls
        /*
        "W": Up,
        "S": Down,
        "A": Left,
        "D": Right,
        */
    },

    difficulty_options: (
        start_difficulty: Easy,
        adaptive: false,
    ),
)
'''

# Get the RON lexer
lexer = RONLexer()

# Highlight the RON code
formatter = HtmlFormatter(full=True, linenos=True)
highlighted_code = highlight(ron_code, lexer, formatter)

# Write the highlighted code to an HTML file
with open('highlighted_ron.html', 'w') as f:
    f.write(highlighted_code)

