# homepage
c.url.start_pages = ['about:blank']
c.url.default_page = 'about:blank'
c.colors.webpage.bg = "#282c34"

# search engine
c.url.searchengines = { 'DEFAULT': 'https://google.com/search?hl=en&q={}' }

# theming
c.colors.webpage.preferred_color_scheme = "dark"
config.source('themes/onedark.py')

# font
c.fonts.default_size = "10pt"
c.fonts.default_family = "JetbrainsMonoNerdFont"
# tabs
c.tabs.favicons.scale = 1.5
c.tabs.padding = {
    "bottom": 8,
    "left": 5,
    "top": 10,
    "right": 5,
    }

# ranger as browser file picker
config.set("fileselect.handler", "external")
config.set("fileselect.single_file.command", ['kitty', '--class', 'ranger-filepicker', '-e', 'ranger', '--choosefile', '{}'])
config.set("fileselect.multiple_files.command", ['kitty', '--class', 'ranger-filepicker', '-e', 'ranger', '--choosefiles', '{}'])


# keybindings
# Leader ( )
config.bind(' l', 'spawn --userscript qute-bitwarden')
# yank to clipboard
config.bind(' y', 'yank selection')

config.load_autoconfig()
