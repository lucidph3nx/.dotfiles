from qutebrowser.config.config import ConfigContainer  # noqa: F401
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

c.colors.webpage.preferred_color_scheme = 'light'

# pallete
t = {
    'fg': '#24292f',
    'red': '#cf222e',
    'orange': '#fb8f44',
    'yellow': '#4d2d00',
    'green': '#116329',
    'aqua': '#1b7c83',
    'blue': '#0969da',
    'purple': '#8250df',
    'grey0': '#6e7781',
    'grey1': '#57606a',
    'grey2': '#424a53',
    'statusline1': '#0969da',
    'statusline2': '#6e7781',
    'statusline3': '#cf222e',
    'bg_dim': '#ffffff',
    'bg0': '#ffffff',
    'bg1': '#f6f8fa',
    'bg2': '#eaeef2',
    'bg3': '#d0d7de',
    'bg4': '#afb8c1',
    'bg5': '#afb8c1',
    'bg_visual': '#ddf4ff',
    'bg_red': '#ffebe9',
    'bg_green': '#dafbe1',
    'bg_blue': '#ddf4ff',
    'bg_yellow': '#fff8c5',
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

c.colors.completion.category.bg = t['bg2']
c.colors.completion.category.fg = t['fg']
c.colors.completion.fg = t['fg']
c.colors.completion.even.bg = t['bg0']
c.colors.completion.odd.bg = t['bg1']
c.colors.completion.match.fg = t['red']
c.colors.completion.item.selected.fg = t['bg0']
c.colors.completion.item.selected.bg = t['blue']
c.colors.completion.item.selected.border.top = t['blue']
c.colors.completion.item.selected.border.bottom = t['blue']

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
