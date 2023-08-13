# pylint: disable=C0111,W0127
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103

# load configs done via gui
config.load_autoconfig()

# homepage
c.url.start_pages = ['about:blank']
c.url.default_page = 'about:blank'
c.url.searchengines = {
    'DEFAULT': 'https://google.com/search?hl=en&q={}',
    'y': 'https://www.youtube.com/results?search_query={}',
}
c.downloads.location.directory = '~/downloads'
c.content.autoplay = False

c.completion.open_categories = [
    'searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

# theming
c.colors.webpage.preferred_color_scheme = 'dark'
config.source('themes/onedark.py')

# disable window decorations (wont work unti using Qt6)
# config.set ('window.hide_decoration', True)

# editor
c.editor.command = ['kitty', '--class', 'qute-editor', '-e', 'nvim', '{}']

# font
c.fonts.default_size = '10pt'
c.fonts.default_family = 'JetbrainsMonoNerdFont'
# tabs
c.tabs.show = 'multiple'  # only show tabs if multiple tabs are open
c.tabs.favicons.scale = 1
c.tabs.padding = {
    'bottom': 5,
    'left': 5,
    'top': 5,
    'right': 5,
}

# ranger as browser file picker
config.set('fileselect.handler', 'external')
config.set(
    'fileselect.single_file.command',
    ['kitty', '--class',
        'ranger-filepicker', '-e', 'ranger', '--choosefile', '{}'],
)
config.set(
    'fileselect.multiple_files.command',
    ['kitty', '--class',
        'ranger-filepicker', '-e', 'ranger', '--choosefiles', '{}'],
)


# keybindings
# I did used to use a combination of config.bind and c.bindings
# but my 'ch' with no leader did not work in config.bind
# and having a combination of binding strategies caused them to interfere
c.bindings.commands['normal'] = {
    # unbind
    '<Ctrl-h>': 'nop',
    # close tabs left and right
    'ch': 'tab-only --next',
    'cl': 'tab-only --prev',
    # bitwarden bindings
    '<Space>ll': 'spawn --userscript qute-bitwarden --totp',
    '<Space>lu': 'spawn --userscript qute-bitwarden --username-only',
    '<Space>lp': 'spawn --userscript qute-bitwarden --password-only',
    '<Space>lt': 'spawn --userscript qute-bitwarden --totp-only',
    # youtube music download
    '<Space>md': 'spawn --userscript ytm-download',
    '<Space>y': 'yank selection',
}
