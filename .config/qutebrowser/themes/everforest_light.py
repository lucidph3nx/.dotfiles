from qutebrowser.config.config import ConfigContainer  # noqa: F401
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

c.colors.webpage.preferred_color_scheme = 'light'

# pallete
t = {
    'fg': '#5c6a72',
    'red': '#f85552',
    'orange': '#f57d26',
    'yellow': '#dfa000',
    'green': '#8da101',
    'aqua': '#35a77c',
    'blue': '#3a94c5',
    'purple': '#df69ba',
    'grey0': '#a6b0a0',
    'grey1': '#939f91',
    'grey2': '#829181',
    'statusline1': '#93b259',
    'statusline2': '#708089',
    'statusline3': '#e66868',
    'bg_dim': '#efebd4',
    'bg0': '#fdf6e3',
    'bg1': '#f4f0d9',
    'bg2': '#efebd4',
    'bg3': '#e6e2cc',
    'bg4': '#e0dcc7',
    'bg5': '#bdc3af',
    'bg_visual': '#eaedc8',
    'bg_red': '#fbe3da',
    'bg_green': '#f0f1d2',
    'bg_blue': '#e9f0e9',
    'bg_yellow': '#faedcd',
}

c.colors.webpage.bg = t['bg0']

c.colors.keyhint.fg = t['fg']
c.colors.keyhint.suffix.fg = t['red']

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
