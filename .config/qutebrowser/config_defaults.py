# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Automatically start playing `<video>` elements.
# Type: Bool
c.content.autoplay = False

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# Allow websites to request geolocations.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.geolocation', True, 'https://www.bunnings.co.nz')

# Allow websites to request geolocations.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.geolocation', True, 'https://www.newworld.co.nz')

# Allow websites to request geolocations.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.geolocation', False, 'https://www.supercheapauto.co.nz')

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Allow JavaScript to read from or write to the clipboard. With
# QtWebEngine, writing the clipboard as response to a user interaction
# is always allowed.
# Type: String
# Valid values:
#   - none: Disable access to clipboard.
#   - access: Allow reading from and writing to the clipboard.
#   - access-paste: Allow accessing the clipboard and pasting clipboard content.
c.content.javascript.clipboard = 'access'

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow locally loaded documents to access remote URLs.
# Type: Bool
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/ben/.local/share/qutebrowser/userscripts/*')

# Allow locally loaded documents to access other local URLs.
# Type: Bool
config.set('content.local_content_can_access_file_urls', False, 'file:///home/ben/.local/share/qutebrowser/userscripts/*')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', False, 'https://calendar.google.com')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', False, 'https://postimg.cc')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', False, 'https://www.facebook.com')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', False, 'https://www.reddit.com')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', False, 'https://www.youtube.com')

# Allow websites to register protocol handlers via
# `navigator.registerProtocolHandler`.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.register_protocol_handler', True, 'https://calendar.google.com?cid=%25s')

# Allow websites to register protocol handlers via
# `navigator.registerProtocolHandler`.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.register_protocol_handler', False, 'https://mail.google.com?extsrc=mailto&url=%25s')

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
# Type: Directory
c.downloads.location.directory = '~/downloads'

# Which categories to show (in which order) in the :open completion.
# Type: FlagList
# Valid values:
#   - searchengines
#   - quickmarks
#   - bookmarks
#   - history
#   - filesystem
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

# Editor (and arguments) to use for the `edit-*` commands. The following
# placeholders are defined:  * `{file}`: Filename of the file to be
# edited. * `{line}`: Line in which the caret is found in the text. *
# `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['kitty', '--class', 'qute-editor', '-e', 'nvim', '{}']

# Handler for selecting file(s) in forms. If `external`, then the
# commands specified by `fileselect.single_file.command`,
# `fileselect.multiple_files.command` and `fileselect.folder.command`
# are used to select one file, multiple files, and folders,
# respectively.
# Type: String
# Valid values:
#   - default: Use the default file selector.
#   - external: Use an external command.
c.fileselect.handler = 'external'

# Command (and arguments) to use for selecting a single file in forms.
# The command should write the selected file path to the specified file
# or stdout. The following placeholders are defined: * `{}`: Filename of
# the file to be written to. If not contained in any argument, the
# standard output of the command is read instead.
# Type: ShellCommand
c.fileselect.single_file.command = ['kitty', '--class', 'ranger-filepicker', '-e', 'ranger', '--choosefile', '{}']

# Command (and arguments) to use for selecting multiple files in forms.
# The command should write the selected file paths to the specified file
# or to stdout, separated by newlines. The following placeholders are
# defined: * `{}`: Filename of the file to be written to. If not
# contained in any argument, the   standard output of the command is
# read instead.
# Type: ShellCommand
c.fileselect.multiple_files.command = ['kitty', '--class', 'ranger-filepicker', '-e', 'ranger', '--choosefiles', '{}']

# CSS border value for hints.
# Type: String
c.hints.border = '1px solid #353b45'

# Languages to use for spell checking. You can check for available
# languages and install dictionaries using scripts/dictcli.py. Run the
# script with -h/--help for instructions.
# Type: List of String
# Valid values:
#   - af-ZA: Afrikaans (South Africa)
#   - bg-BG: Bulgarian (Bulgaria)
#   - ca-ES: Catalan (Spain)
#   - cs-CZ: Czech (Czech Republic)
#   - da-DK: Danish (Denmark)
#   - de-DE: German (Germany)
#   - el-GR: Greek (Greece)
#   - en-AU: English (Australia)
#   - en-CA: English (Canada)
#   - en-GB: English (United Kingdom)
#   - en-US: English (United States)
#   - es-ES: Spanish (Spain)
#   - et-EE: Estonian (Estonia)
#   - fa-IR: Farsi (Iran)
#   - fo-FO: Faroese (Faroe Islands)
#   - fr-FR: French (France)
#   - he-IL: Hebrew (Israel)
#   - hi-IN: Hindi (India)
#   - hr-HR: Croatian (Croatia)
#   - hu-HU: Hungarian (Hungary)
#   - id-ID: Indonesian (Indonesia)
#   - it-IT: Italian (Italy)
#   - ko: Korean
#   - lt-LT: Lithuanian (Lithuania)
#   - lv-LV: Latvian (Latvia)
#   - nb-NO: Norwegian (Norway)
#   - nl-NL: Dutch (Netherlands)
#   - pl-PL: Polish (Poland)
#   - pt-BR: Portuguese (Brazil)
#   - pt-PT: Portuguese (Portugal)
#   - ro-RO: Romanian (Romania)
#   - ru-RU: Russian (Russia)
#   - sh: Serbo-Croatian
#   - sk-SK: Slovak (Slovakia)
#   - sl-SI: Slovenian (Slovenia)
#   - sq: Albanian
#   - sr: Serbian
#   - sv-SE: Swedish (Sweden)
#   - ta-IN: Tamil (India)
#   - tg-TG: Tajik (Tajikistan)
#   - tr-TR: Turkish (Turkey)
#   - uk-UA: Ukrainian (Ukraine)
#   - vi-VN: Vietnamese (Viet Nam)
c.spellcheck.languages = ['en-AU']

# Scaling factor for favicons in the tab bar. The tab size is unchanged,
# so big favicons also require extra `tabs.padding`.
# Type: Float
c.tabs.favicons.scale = 1

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {'bottom': 5, 'left': 5, 'top': 5, 'right': 5}

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'top'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'qute://start'

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
# multiple times.  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://google.com/search?hl=en&q={}', 'y': 'https://www.youtube.com/results?search_query={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = ['qute://start']

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#abb2bf'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#353b45'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#282c34'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#61afef'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#282c34'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#282c34'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#282c34'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#282c34'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#98c379'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#98c379'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#98c379'

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = '#61afef'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#61afef'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#abb2bf'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#282c34'

# Background color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.bg = '#282c34'

# Foreground color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.fg = '#abb2bf'

# Background color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.bg = '#98c379'

# Foreground color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.fg = '#282c34'

# Background color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.bg = '#353b45'

# Foreground color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.fg = '#565c64'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#282c34'

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = '#282c34'

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = '#61afef'

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = '#282c34'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#56b6c2'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#e06c75'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#282c34'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#61afef'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#abb2bf'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#abb2bf'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#abb2bf'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#282c34'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#282c34'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#e06c75'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#e06c75'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#282c34'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#c678dd'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#c678dd'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#abb2bf'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#282c34'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#282c34'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#abb2bf'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '#282c34'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#282c34'

# Foreground color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.fg = '#abb2bf'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#98c379'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#61afef'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#282c34'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#282c34'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#61afef'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#282c34'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#56b6c2'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#282c34'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#353b45'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#abb2bf'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#282c34'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#abb2bf'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#282c34'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#282c34'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#c678dd'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#282c34'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#61afef'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#61afef'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#abb2bf'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#e06c75'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#abb2bf'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#56b6c2'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#61afef'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#c678dd'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#282c34'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#61afef'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#56b6c2'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#e06c75'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#abb2bf'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#353b45'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#abb2bf'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#282c34'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#282c34'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#98c379'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#282c34'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#98c379'

# Foreground color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.fg = '#c8ccd4'

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = '#61afef'

# Foreground color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.fg = '#c8ccd4'

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = '#56b6c2'

# Foreground color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = '#282c34'

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = '#98c379'

# Foreground color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.fg = '#282c34'

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = '#98c379'

# Value to use for `prefers-color-scheme:` for websites. The "light"
# value is only available with QtWebEngine 5.15.2+. On older versions,
# it is the same as "auto". The "auto" value is broken on QtWebEngine
# 5.15.2 due to a Qt bug. There, it will fall back to "light"
# unconditionally.
# Type: String
# Valid values:
#   - auto: Use the system-wide color scheme setting.
#   - light: Force a light theme.
#   - dark: Force a dark theme.
c.colors.webpage.preferred_color_scheme = 'dark'

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font
c.fonts.default_family = 'JetbrainsMonoNerdFont'

# Default font size to use. Whenever "default_size" is used in a font
# setting, it's replaced with the size listed here. Valid values are
# either a float value with a "pt" suffix, or an integer value with a
# "px" suffix.
# Type: String
c.fonts.default_size = '10pt'

# Bindings for normal mode
config.bind('<Ctrl+h>', 'nop')
config.bind('<Space>ff', 'spawn --userscript open-firefox')
config.bind('<Space>ll', 'spawn --userscript qute-bitwarden --totp')
config.bind('<Space>lp', 'spawn --userscript qute-bitwarden --password-only')
config.bind('<Space>lt', 'spawn --userscript qute-bitwarden --totp-only')
config.bind('<Space>lu', 'spawn --userscript qute-bitwarden --username-only')
config.bind('<Space>md', 'spawn --userscript ytm-download')
config.bind('<Space>y', 'yank selection')
config.bind('ch', 'tab-only --next')
config.bind('cl', 'tab-only --prev')
