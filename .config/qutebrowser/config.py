# pylint: disable=C0111,W0127
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103

# load configs done via gui
config.load_autoconfig()

# homepage
c.url.start_pages = ['qute://start']
c.url.default_page = 'qute://start'
c.url.searchengines = {
    'DEFAULT': 'https://google.com/search?hl=en&q={}',
    'g': 'https://google.com/search?hl=en&q={}',
    'y': 'https://www.youtube.com/results?search_query={}',
    'nw': 'https://www.newworld.co.nz/shop/Search?q={}',
}
c.downloads.location.directory = '~/downloads'
# content settings

# disable autoplay globally
c.content.autoplay = False
# allow autoplay on some sites
config.set('content.autoplay',True, 'https://app.pluralsight.com/*')

# turn off geolocation
c.content.geolocation = False
# allow location on some sites
config.set('content.geolocation',True, 'https://www.bunnings.co.nz')
config.set('content.geolocation',True, 'https://www.metlink.org.nz')
config.set('content.geolocation',True, 'https://www.newworld.co.nz')
config.set('content.geolocation',True, 'https://www.pbtech.co.nz')

# ms teams video, audio, screen share
config.set('content.desktop_capture', True, 'https://teams.microsoft.com')
config.set('content.media.audio_capture', True, 'https://teams.microsoft.com')
config.set('content.media.video_capture', True, 'https://teams.microsoft.com')
config.set('content.media.audio_video_capture', True, 'https://teams.microsoft.com')

# turn off notifications
c.content.notifications.enabled = False

# allow clipboard access
c.content.javascript.clipboard = 'access'

c.content.tls.certificate_errors = 'ask-block-thirdparty'

c.spellcheck.languages = ['en-AU']

c.completion.open_categories = [
    'searchengines',
    'quickmarks',
    'bookmarks',
    'history'
]

# theming
c.colors.webpage.preferred_color_scheme = 'dark'
config.source('current-theme.py')

# disable window decorations (wont work unti using Qt6)
config.set ('window.hide_decoration', True)

# editor
c.editor.command = ['kitty', '--class', 'qute-editor', '-e', 'nvim', '{}']

# font
c.fonts.default_size = '10pt'
c.fonts.default_family = 'JetBrains Mono'
# tabs
c.tabs.position = 'top'
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
    # tab give (pop out)
    'tg': 'tab-give',
    # bitwarden bindings
    '<Space>ll': 'spawn --userscript qute-bitwarden --auto-lock 604800 --totp',
    '<Space>lu': 'spawn --userscript qute-bitwarden --auto-lock 604800 --username-only',
    '<Space>lp': 'spawn --userscript qute-bitwarden --auto-lock 604800 --password-only',
    '<Space>lt': 'spawn --userscript qute-bitwarden --auto-lock 604800 --totp-only',
    # youtube music download
    '<Space>md': 'spawn --userscript ytm-download',
    '<Space>y': 'yank selection',
    # open in firefox
    '<Space>ff': 'spawn --userscript open-firefox',
}
