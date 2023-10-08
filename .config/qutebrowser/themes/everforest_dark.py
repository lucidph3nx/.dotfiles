from qutebrowser.config.config import ConfigContainer  # noqa: F401
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

c.colors.webpage.preferred_color_scheme = 'dark'

# pallete
t = {
    'fg': '#d3c6aa',
    'red': '#e67e80',
    'orange': '#e69875',
    'yellow': '#dbbc7f',
    'green': '#a7c080',
    'aqua': '#83c092',
    'blue': '#7fbbb3',
    'purple': '#d699b6',
    'grey0': '#7a8478',
    'grey1': '#859289',
    'grey2': '#9da9a0',
    'statusline1': '#a7c080',
    'statusline2': '#d3c6aa',
    'statusline3': '#e67e80',
    'bg_dim': '#232a2e',
    'bg0': '#2d353b',
    'bg1': '#343f44',
    'bg2': '#3d484d',
    'bg3': '#475258',
    'bg4': '#4f585e',
    'bg5': '#56635f',
    'bg_visual': '#543a48',
    'bg_red': '#514045',
    'bg_green': '#425047',
    'bg_blue': '#3a515d',
    'bg_yellow': '#4d4c43',
}

c.colors.webpage.bg = t['bg0']

c.colors.keyhint.fg = t['fg']
c.colors.keyhint.suffix.fg = t['red']
c.colors.keyhint.bg = t['bg0']

c.colors.messages.error.bg = t['bg_red']
c.colors.messages.error.fg = t['fg']
c.colors.messages.info.bg = t['bg_blue']
c.colors.messages.info.fg = t['fg']
c.colors.messages.warning.bg = t['bg_yellow']
c.colors.messages.warning.fg = t['fg']

c.colors.prompts.bg = t['bg0']
c.colors.prompts.fg = t['fg']

c.colors.completion.category.bg = t['bg3']
c.colors.completion.category.fg = t['fg']
c.colors.completion.fg = t['fg']
c.colors.completion.even.bg = t['bg0']
c.colors.completion.odd.bg = t['bg1']
c.colors.completion.match.fg = t['red']
c.colors.completion.item.selected.fg = t['fg']
c.colors.completion.item.selected.bg = t['bg_yellow']
c.colors.completion.item.selected.border.top = t['bg_yellow']
c.colors.completion.item.selected.border.bottom = t['bg_yellow']

c.colors.completion.scrollbar.bg = t['bg_dim']
c.colors.completion.scrollbar.fg = t['fg']

c.colors.hints.bg = t['bg0']
c.colors.hints.fg = t['fg']
c.colors.hints.match.fg = t['red']
c.hints.border = '0px solid black'

c.colors.statusbar.normal.fg = t['fg']
c.colors.statusbar.normal.bg = t['bg3']

c.colors.statusbar.insert.fg = t['bg0']
c.colors.statusbar.insert.bg = t['statusline1']

c.colors.statusbar.caret.fg = t['bg0']
c.colors.statusbar.caret.bg = t['purple']

c.colors.statusbar.command.fg = t['fg']
c.colors.statusbar.command.bg = t['bg0']

c.colors.statusbar.passthrough.fg = t['bg0']
c.colors.statusbar.passthrough.bg = t['blue']

c.colors.statusbar.url.error.fg = t['orange']
c.colors.statusbar.url.fg = t['fg']
c.colors.statusbar.url.hover.fg = t['blue']
c.colors.statusbar.url.success.http.fg = t['green']
c.colors.statusbar.url.success.https.fg = t['green']

c.colors.tabs.bar.bg = t['bg_dim']
c.colors.tabs.even.bg = t['bg0']
c.colors.tabs.odd.bg = t['bg0']
c.colors.tabs.even.fg = t['fg']
c.colors.tabs.odd.fg = t['fg']
c.colors.tabs.selected.even.bg = t['bg2']
c.colors.tabs.selected.odd.bg = t['bg2']
c.colors.tabs.selected.even.fg = t['fg']
c.colors.tabs.selected.odd.fg = t['fg']
c.colors.tabs.indicator.start = t['blue']
c.colors.tabs.indicator.stop = t['green']
c.colors.tabs.indicator.error = t['red']
