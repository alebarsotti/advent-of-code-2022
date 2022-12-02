class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def print_color(text, color=''):
    return f'{color}{BOLD}{text}{END}'


def print_color_underline(text, color=''):
    return f'{color}{UNDERLINE}{text}{END}'
