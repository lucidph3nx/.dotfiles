#c.colors.webpage.darkmode.enabled = True
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

config.load_autoconfig()
