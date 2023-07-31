# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401
config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

# homepage
c.url.start_pages = ['about:blank']
c.url.default_page = 'about:blank'
c.colors.webpage.bg = "#282c34"

# search engine
c.url.searchengines = {'DEFAULT': 'https://google.com/search?hl=en&q={}'}

# theming
c.colors.webpage.preferred_color_scheme = "dark"
config.source('themes/onedark.py')

# disable window decorations (wont work unti using Qt6)
# config.set ("window.hide_decoration", True)

# font
c.fonts.default_size = "10pt"
c.fonts.default_family = "JetbrainsMonoNerdFont"
# tabs
c.tabs.favicons.scale = 1
c.tabs.padding = {
    "bottom": 6,
    "left": 5,
    "top": 6,
    "right": 5,
    }


# ranger as browser file picker
config.set("fileselect.handler", "external")
config.set("fileselect.single_file.command", ['kitty', '--class', 'ranger-filepicker', '-e', 'ranger', '--choosefile', '{}'])
config.set("fileselect.multiple_files.command", ['kitty', '--class', 'ranger-filepicker', '-e', 'ranger', '--choosefiles', '{}'])


# keybindings
# I did used to use a combination of config.bind and c.bindings, but my 'ch' with no leader did not work in config.bind
# and having a combination of binding strategies caused them to interfere
c.bindings.commands['normal'] = {
        # close tabs left and right
        'ch': 'tab-only --next',
        'cl': 'tab-only --prev',
        # bitwarden bindings
        '<Space>ll': 'spawn --userscript qute-bitwarden --totp',
        '<Space>lu': 'spawn --userscript qute-bitwarden --username-only',
        '<Space>lp': 'spawn --userscript qute-bitwarden --password-only',
        '<Space>lt': 'spawn --userscript qute-bitwarden --totp-only',
        '<Space>y': 'yank selection',
        }

config.load_autoconfig()
