from qutebrowser.config.config import ConfigContainer  # noqa: F401
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

c.colors.webpage.preferred_color_scheme = 'dark'

# pallete
# https://github.com/navarasu/onedark.nvim/blob/dac8c39812dae025255c9069a260e1f69d967927/lua/onedark/palette.lua
t = {
    'fg': '#abb2bf',
    'red': '#e06c75',
    'orange': '#d19a66',
    'yellow': '#e5c07b',
    'green': '#98c379',
    'aqua': '#56b6c2',
    'blue': '#61afef',
    'purple': '#c678dd',
    'grey0': '#4d515d',
    'grey1': '#5c6370',
    'grey2': '#848b98',
    'statusline1': '#98c379',
    'statusline2': '#e5c07b',
    'statusline3': '#e06c75',
    'bg_dim': '#21252b',
    'bg0': '#282c34',
    'bg1': '#31353f',
    'bg2': '#393f4a',
    'bg3': '#3b3f4c',
    'bg4': '#',
    'bg5': '#',
    'bg_visual': '#3b3f4c',
    'bg_red': '#382b2c',
    'bg_green': '#31392b',
    'bg_blue': '#1c3448',
    'bg_yellow': '#ebd09c',
}

# c.colors.webpage.bg = t['bg0']

c.colors.keyhint.fg = t['fg']
c.colors.keyhint.suffix.fg = t['fg']
c.colors.keyhint.bg = t['bg0']

c.colors.messages.error.bg = t['red']
c.colors.messages.error.fg = t['bg0']
c.colors.messages.info.bg = t['bg0']
c.colors.messages.info.fg = t['fg']
c.colors.messages.warning.bg = t['purple']
c.colors.messages.warning.fg = t['bg0']

c.colors.prompts.bg = t['bg0']
c.colors.prompts.fg = t['fg']

c.colors.completion.category.bg = t['bg0']
c.colors.completion.category.fg = t['fg']
c.colors.completion.fg = t['fg']
c.colors.completion.even.bg = t['bg0']
c.colors.completion.odd.bg = t['bg1']
c.colors.completion.match.fg = t['blue']
c.colors.completion.item.selected.fg = t['bg0']
c.colors.completion.item.selected.bg = t['green']
c.colors.completion.item.selected.border.top = t['bg0']
c.colors.completion.item.selected.border.bottom = t['bg0']

c.colors.completion.scrollbar.bg = t['bg0']
c.colors.completion.scrollbar.fg = t['fg']

c.colors.hints.bg = t['blue']
c.colors.hints.fg = t['bg0']
c.colors.hints.match.fg = t['fg']
c.hints.border = '1px solid ' + t['bg1']

c.colors.statusbar.normal.fg = t['blue']
c.colors.statusbar.normal.bg = t['bg3']

c.colors.statusbar.insert.fg = t['bg0']
c.colors.statusbar.insert.bg = t['blue']

c.colors.statusbar.caret.fg = t['bg0']
c.colors.statusbar.caret.bg = t['red']

c.colors.statusbar.command.fg = t['fg']
c.colors.statusbar.command.bg = t['bg0']

c.colors.statusbar.url.error.fg = t['red']
c.colors.statusbar.url.fg = t['fg']
c.colors.statusbar.url.hover.fg = t['fg']
c.colors.statusbar.url.success.http.fg = t['aqua']
c.colors.statusbar.url.success.https.fg = t['blue']

c.colors.tabs.bar.bg = t['bg0']
c.colors.tabs.even.bg = t['bg0']
c.colors.tabs.odd.bg = t['bg0']
c.colors.tabs.even.fg = t['fg']
c.colors.tabs.odd.fg = t['fg']
c.colors.tabs.selected.even.bg = t['green']
c.colors.tabs.selected.odd.bg = t['green']
c.colors.tabs.selected.even.fg = t['bg0']
c.colors.tabs.selected.odd.fg = t['bg0']
c.colors.tabs.indicator.start = t['blue']
c.colors.tabs.indicator.stop = t['aqua']
c.colors.tabs.indicator.error = t['red']

