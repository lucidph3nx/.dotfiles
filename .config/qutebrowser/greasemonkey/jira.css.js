// ==UserScript==
// @name    Userstyle (jira.css)
// @include    https://jardengroup.atlassian.net/jira/software/c/projects/PLAT/*
// ==/UserScript==
GM_addStyle(`
body {
  font-family: JetBrains Mono,monospace !important;
}
html[data-color-mode="light"][data-theme~="light:dark"], html[data-color-mode="dark"][data-theme~="dark:dark"] {
  /* my atom colours */
  --atom-red: #e06c75;
  --atom-green: #98c379;
  --atom-yellow: #d19a66;
  --atom-blue: #61afef;
  --atom-magenta: #c678dd;
  --atom-cyan: #56b6c2;
  --atom-black: #282c34;
  --atom-black-light: #454C59;
  --atom-white: #abb2bf;
  --atom-white-light: #cfd7e6;
  --atom-text: var(--atom-white-light);
  --atom-text-inverse: var(--atom-black);
  --atom-foreground: #979fad;
  --atom-background: #282c34;

  /* jira colours */
  --ds-text: var(--atom-text);
  --ds-text-accent-lime: var(--atom-green) !important;
  --ds-text-accent-lime-bolder: var(--atom-green) !important;
  --ds-text-accent-red: var(--atom-red) !important;
  --ds-text-accent-red-bolder: var(--atom-red) !important;
  --ds-text-accent-orange: var(--atom-yellow) !important;
  --ds-text-accent-orange-bolder: var(--atom-yellow) !important;
  --ds-text-accent-yellow: var(--atom-yellow) !important;
  --ds-text-accent-yellow-bolder: var(--atom-yellow) !important;
  --ds-text-accent-green: var(--atom-green) !important;
  --ds-text-accent-green-bolder: var(--atom-green) !important;
  --ds-text-accent-teal: var(--atom-cyan) !important;
  --ds-text-accent-teal-bolder: var(--atom-cyan) !important;
  --ds-text-accent-blue: var(--atom-blue) !important;
  --ds-text-accent-blue-bolder: var(--atom-blue) !important;
  --ds-text-accent-purple: var(--atom-magenta) !important;
  --ds-text-accent-purple-bolder: var(--atom-magenta) !important;
  --ds-text-accent-magenta: var(--atom-magenta) !important;
  --ds-text-accent-magenta-bolder: var(--atom-magenta) !important;
  --ds-text-accent-gray: var(--atom-white) !important;
  --ds-text-accent-gray-bolder: var(--atom-white) !important;
  --ds-text-disabled: var(--atom-white) !important;
  --ds-text-inverse: var(--atom-black) !important;
  --ds-text-selected: var(--atom-black) !important;
  --ds-text-brand: var(--atom-green) !important;
  --ds-text-danger: var(--atom-red) !important;
  --ds-text-warning: var(--atom-yellow) !important;
  --ds-text-warning-inverse: var(--atom-black) !important;
  --ds-text-success: var(--atom-text-inverse) !important;
  --ds-text-discovery: var(--atom-magenta) !important;
  --ds-text-information: var(--atom-blue) !important;
  --ds-text-subtlest: var(--atom-white) !important;
  --ds-text-subtle: var(--atom-white) !important;
  --ds-link: var(--atom-text-inverse) !important;
  --ds-link-pressed: var(--atom-text-inverse) !important;
  --ds-icon: var(--atom-black-light) !important;
  --ds-icon-accent-lime: var(--atom-green) !important;
  --ds-icon-accent-red: var(--atom-red) !important;
  --ds-icon-accent-orange: var(--atom-yellow) !important;
  --ds-icon-accent-yellow: var(--atom-yellow) !important;
  --ds-icon-accent-green: var(--atom-green) !important;
  --ds-icon-accent-teal: var(--atom-cyan) !important;
  --ds-icon-accent-blue: var(--atom-blue) !important;
  --ds-icon-accent-purple: var(--atom-magenta) !important;
  --ds-icon-accent-magenta: var(--atom-magenta) !important;
  --ds-icon-accent-gray: var(--atom-white) !important;
  --ds-icon-disabled: var(--atom-black-light) !important;
  --ds-icon-inverse: var(--atom-black) !important;
  --ds-icon-selected: var(--atom-blue) !important;
  --ds-icon-brand: var(--atom-green) !important;
  --ds-icon-danger: var(--atom-red) !important;
  --ds-icon-warning: var(--atom-yellow) !important;
  --ds-icon-warning-inverse: var(--atom-black) !important;
  --ds-icon-success: var(--atom-green) !important;
  --ds-icon-discovery: var(--atom-magenta) !important;
  --ds-icon-information: var(--atom-blue) !important;
  --ds-icon-subtle: var(--atom-black-light) !important;
  --ds-border: var(--atom-white) !important;
  --ds-border-accent-lime: var(--atom-green) !important;
  --ds-border-accent-red: var(--atom-red) !important;
  --ds-border-accent-orange: var(--atom-yellow) !important;
  --ds-border-accent-yellow: var(--atom-yellow) !important;
  --ds-border-accent-green: var(--atom-green) !important;
  --ds-border-accent-teal: var(--atom-cyan) !important;
  --ds-border-accent-blue: var(--atom-blue) !important;
  --ds-border-accent-purple: var(--atom-magenta) !important;
  --ds-border-accent-magenta: var(--atom-magenta) !important;
  --ds-border-accent-gray: var(--atom-white) !important;
  --ds-border-disabled: #A1BDD914 !important;
  --ds-border-focused: var(--atom-blue) !important;
  --ds-border-input: #A6C5E229 !important;
  --ds-border-inverse: var(--atom-black) !important;
  --ds-border-selected: var(--atom-blue) !important;
  --ds-border-brand: var(--atom-green) !important;
  --ds-border-danger: var(--atom-red) !important;
  --ds-border-warning: var(--atom-yellow) !important;
  --ds-border-success: var(--atom-green) !important;
  --ds-border-discovery: var(--atom-magenta) !important;
  --ds-border-information: var(--atom-blue) !important;
  --ds-border-bold: var(--atom-black-light) !important;
  --ds-background-accent-lime-subtlest: var(--atom-green) !important;
  --ds-background-accent-lime-subtler: var(--atom-green) !important;
  --ds-background-accent-lime-subtle: var(--atom-green) !important;
  --ds-background-accent-lime-bolder: var(--atom-green) !important;
  --ds-background-accent-red-subtlest: var(--atom-red) !important;
  --ds-background-accent-red-subtler: var(--atom-red) !important;
  --ds-background-accent-red-subtle: var(--atom-red) !important;
  --ds-background-accent-red-bolder: var(--atom-red) !important;
  --ds-background-accent-orange-subtlest: var(--atom-yellow) !important;
  --ds-background-accent-orange-subtler: var(--atom-yellow) !important;
  --ds-background-accent-orange-subtle: var(--atom-yellow) !important;
  --ds-background-accent-orange-bolder: var(--atom-yellow) !important;
  --ds-background-accent-yellow-subtlest: var(--atom-yellow) !important;
  --ds-background-accent-yellow-subtler: var(--atom-yellow) !important;
  --ds-background-accent-yellow-subtle: var(--atom-yellow) !important;
  --ds-background-accent-yellow-bolder: var(--atom-yellow) !important;
  --ds-background-accent-green-subtlest: var(--atom-green) !important;
  --ds-background-accent-green-subtler: var(--atom-green) !important;
  --ds-background-accent-green-subtle: var(--atom-green) !important;
  --ds-background-accent-green-bolder: var(--atom-green) !important;
  --ds-background-accent-teal-subtlest: var(--atom-cyan) !important;
  --ds-background-accent-teal-subtler: var(--atom-cyan) !important;
  --ds-background-accent-teal-subtle: var(--atom-cyan) !important;
  --ds-background-accent-teal-bolder: var(--atom-cyan) !important;
  --ds-background-accent-blue-subtlest: var(--atom-blue) !important;
  --ds-background-accent-blue-subtler: var(--atom-blue) !important;
  --ds-background-accent-blue-subtle: var(--atom-blue) !important;
  --ds-background-accent-blue-bolder: var(--atom-blue) !important;
  --ds-background-accent-purple-subtlest: var(--atom-magenta) !important;
  --ds-background-accent-purple-subtler: var(--atom-magenta) !important;
  --ds-background-accent-purple-subtle: var(--atom-magenta) !important;
  --ds-background-accent-purple-bolder: var(--atom-magenta) !important;
  --ds-background-accent-magenta-subtlest: var(--atom-magenta) !important;
  --ds-background-accent-magenta-subtler: var(--atom-magenta) !important;
  --ds-background-accent-magenta-subtle: var(--atom-magenta) !important;
  --ds-background-accent-magenta-bolder: var(--atom-magenta) !important;
  --ds-background-accent-gray-subtlest: var(--atom-white) !important;
  --ds-background-accent-gray-subtler: var(--atom-white) !important;
  --ds-background-accent-gray-subtle: var(--atom-white) !important;
  --ds-background-accent-gray-bolder: var(--atom-white) !important;
  --ds-background-disabled: var(--atom-black-light) !important;
  --ds-background-input: var(--atom-black) !important;
  --ds-background-input-hovered: var(--atom-black) !important;
  --ds-background-input-pressed: var(--atom-black) !important;
  --ds-background-inverse-subtle: var(--atom-black) !important;
  --ds-background-inverse-subtle-hovered: var(--atom-black) !important;
  --ds-background-inverse-subtle-pressed: var(--atom-black) !important;
  --ds-background-neutral: var(--atom-black) !important;
  --ds-background-neutral-hovered: var(--atom-black) !important;
  --ds-background-neutral-pressed: var(--atom-black) !important;
  --ds-background-neutral-subtle: var(--atom-black-light) !important;
  --ds-background-neutral-subtle-hovered: var(--atom-black-light) !important;
  --ds-background-neutral-subtle-pressed: var(--atom-black-light) !important;
  --ds-background-neutral-bold: var(--atom-black-light) !important;
  --ds-background-neutral-bold-hovered: var(--atom-black-light) !important;
  --ds-background-neutral-bold-pressed: var(--atom-black-light) !important;
  --ds-background-selected: var(--atom-blue) !important;
  --ds-background-selected-hovered: var(--atom-blue) !important;
  --ds-background-selected-pressed: var(--atom-blue) !important;
  --ds-background-selected-bold: var(--atom-blue) !important;
  --ds-background-selected-bold-hovered: var(--atom-blue) !important;
  --ds-background-selected-bold-pressed: var(--atom-blue) !important;
  --ds-background-brand-subtlest: var(--atom-blue) !important;
  --ds-background-brand-subtlest-hovered: var(--atom-blue) !important;
  --ds-background-brand-subtlest-pressed: var(--atom-blue) !important;
  --ds-background-brand-bold: var(--atom-green) !important;
  --ds-background-brand-bold-hovered: var(--atom-green) !important;
  --ds-background-brand-bold-pressed: var(--atom-green) !important;
  --ds-background-brand-boldest: var(--atom-green) !important;
  --ds-background-brand-boldest-hovered: var(--atom-green) !important;
  --ds-background-brand-boldest-pressed: var(--atom-green) !important;
  --ds-background-danger: var(--atom-red) !important;
  --ds-background-danger-hovered: var(--atom-red) !important;
  --ds-background-danger-pressed: var(--atom-red) !important;
  --ds-background-danger-bold: var(--atom-red) !important;
  --ds-background-danger-bold-hovered: var(--atom-red) !important;
  --ds-background-danger-bold-pressed: var(--atom-red) !important;
  --ds-background-warning: var(--atom-yellow) !important;
  --ds-background-warning-hovered: var(--atom-yellow) !important;
  --ds-background-warning-pressed: var(--atom-yellow) !important;
  --ds-background-warning-bold: var(--atom-yellow) !important;
  --ds-background-warning-bold-hovered: var(--atom-yellow) !important;
  --ds-background-warning-bold-pressed: var(--atom-yellow) !important;
  --ds-background-success: var(--atom-green) !important;
  --ds-background-success-hovered: var(--atom-green) !important;
  --ds-background-success-pressed: var(--atom-green) !important;
  --ds-background-success-bold: var(--atom-green) !important;
  --ds-background-success-bold-hovered: var(--atom-green) !important;
  --ds-background-success-bold-pressed: var(--atom-green) !important;
  --ds-background-discovery: var(--atom-magenta) !important;
  --ds-background-discovery-hovered: var(--atom-magenta) !important;
  --ds-background-discovery-pressed: var(--atom-magenta) !important;
  --ds-background-discovery-bold: var(--atom-magenta) !important;
  --ds-background-discovery-bold-hovered: var(--atom-magenta) !important;
  --ds-background-discovery-bold-pressed: var(--atom-magenta) !important;
  --ds-background-information: var(--atom-blue) !important;
  --ds-background-information-hovered: var(--atom-blue) !important;
  --ds-background-information-pressed: var(--atom-blue) !important;
  --ds-background-information-bold: var(--atom-blue) !important;
  --ds-background-information-bold-hovered: var(--atom-blue) !important;
  --ds-background-information-bold-pressed: var(--atom-blue) !important;
  --ds-blanket: #10121499 !important;
  --ds-blanket-selected: #1D7AFC14 !important;
  --ds-blanket-danger: #E3493514 !important;
  --ds-interaction-hovered: #ffffff33 !important;
  --ds-interaction-pressed: #ffffff5c !important;
  --ds-skeleton: #A1BDD914 !important;
  --ds-skeleton-subtle: #BCD6F00A !important;
  --ds-chart-categorical-1: #1D9AAA !important;
  --ds-chart-categorical-1-hovered: #37B4C3 !important;
  --ds-chart-categorical-2: #B8ACF6 !important;
  --ds-chart-categorical-2-hovered: #DFD8FD !important;
  --ds-chart-categorical-3: #D97008 !important;
  --ds-chart-categorical-3-hovered: #d19a66 !important;
  --ds-chart-categorical-4: #F797D2 !important;
  --ds-chart-categorical-4-hovered: #FDD0EC !important;
  --ds-chart-categorical-5: #CCE0FF !important;
  --ds-chart-categorical-5-hovered: #E9F2FF !important;
  --ds-chart-categorical-6: #8270DB !important;
  --ds-chart-categorical-6-hovered: #8F7EE7 !important;
  --ds-chart-categorical-7: #FDD0EC !important;
  --ds-chart-categorical-7-hovered: #FFECF8 !important;
  --ds-chart-categorical-8: #FEC57B !important;
  --ds-chart-categorical-8-hovered: #FFE2BD !important;
  --ds-chart-lime-bold: var(--atom-green) !important;
  --ds-chart-lime-bold-hovered: var(--atom-green) !important;
  --ds-chart-lime-bolder: var(--atom-green) !important;
  --ds-chart-lime-bolder-hovered: var(--atom-green) !important;
  --ds-chart-lime-boldest: var(--atom-green) !important;
  --ds-chart-lime-boldest-hovered: var(--atom-green) !important;
  --ds-chart-neutral: var(--atom-black-light) !important;
  --ds-chart-neutral-hovered: var(--atom-black-light) !important;
  --ds-chart-red-bold: var(--atom-red) !important;
  --ds-chart-red-bold-hovered: var(--atom-red) !important;
  --ds-chart-red-bolder: var(--atom-red) !important;
  --ds-chart-red-bolder-hovered: var(--atom-red) !important;
  --ds-chart-red-boldest: var(--atom-red) !important;
  --ds-chart-red-boldest-hovered: var(--atom-red) !important;
  --ds-chart-orange-bold: var(--atom-yellow) !important;
  --ds-chart-orange-bold-hovered: var(--atom-yellow) !important;
  --ds-chart-orange-bolder: var(--atom-yellow) !important;
  --ds-chart-orange-bolder-hovered: var(--atom-yellow) !important;
  --ds-chart-orange-boldest: var(--atom-yellow) !important;
  --ds-chart-orange-boldest-hovered: var(--atom-yellow) !important;
  --ds-chart-yellow-bold: var(--atom-yellow) !important;
  --ds-chart-yellow-bold-hovered: var(--atom-yellow) !important;
  --ds-chart-yellow-bolder: var(--atom-yellow) !important;
  --ds-chart-yellow-bolder-hovered: var(--atom-yellow) !important;
  --ds-chart-yellow-boldest: var(--atom-yellow) !important;
  --ds-chart-yellow-boldest-hovered: var(--atom-yellow) !important;
  --ds-chart-green-bold: var(--atom-green) !important;
  --ds-chart-green-bold-hovered: var(--atom-green) !important;
  --ds-chart-green-bolder: var(--atom-green) !important;
  --ds-chart-green-bolder-hovered: var(--atom-green) !important;
  --ds-chart-green-boldest: var(--atom-green) !important;
  --ds-chart-green-boldest-hovered: var(--atom-green) !important;
  --ds-chart-teal-bold: var(--atom-cyan) !important;
  --ds-chart-teal-bold-hovered: var(--atom-cyan) !important;
  --ds-chart-teal-bolder: var(--atom-cyan) !important;
  --ds-chart-teal-bolder-hovered: var(--atom-cyan) !important;
  --ds-chart-teal-boldest: var(--atom-cyan) !important;
  --ds-chart-teal-boldest-hovered: var(--atom-cyan) !important;
  --ds-chart-blue-bold: var(--atom-blue) !important;
  --ds-chart-blue-bold-hovered: var(--atom-blue) !important;
  --ds-chart-blue-bolder: var(--atom-blue) !important;
  --ds-chart-blue-bolder-hovered: var(--atom-blue) !important;
  --ds-chart-blue-boldest: var(--atom-blue) !important;
  --ds-chart-blue-boldest-hovered: var(--atom-blue) !important;
  --ds-chart-purple-bold: var(--atom-magenta) !important;
  --ds-chart-purple-bold-hovered: var(--atom-magenta) !important;
  --ds-chart-purple-bolder: var(--atom-magenta) !important;
  --ds-chart-purple-bolder-hovered: var(--atom-magenta) !important;
  --ds-chart-purple-boldest: var(--atom-magenta) !important;
  --ds-chart-purple-boldest-hovered: var(--atom-magenta) !important;
  --ds-chart-magenta-bold: var(--atom-magenta) !important;
  --ds-chart-magenta-bold-hovered: var(--atom-magenta) !important;
  --ds-chart-magenta-bolder: var(--atom-magenta) !important;
  --ds-chart-magenta-bolder-hovered: var(--atom-magenta) !important;
  --ds-chart-magenta-boldest: var(--atom-magenta) !important;
  --ds-chart-magenta-boldest-hovered: var(--atom-magenta) !important;
  --ds-chart-gray-bold: var(--atom-white) !important;
  --ds-chart-gray-bold-hovered: var(--atom-white) !important;
  --ds-chart-gray-bolder: var(--atom-white) !important;
  --ds-chart-gray-bolder-hovered: var(--atom-white) !important;
  --ds-chart-gray-boldest: var(--atom-white) !important;
  --ds-chart-gray-boldest-hovered: var(--atom-white) !important;
  --ds-chart-brand: var(--atom-green) !important;
  --ds-chart-brand-hovered: var(--atom-green) !important;
  --ds-chart-danger: var(--atom-red) !important;
  --ds-chart-danger-hovered: var(--atom-red) !important;
  --ds-chart-danger-bold: var(--atom-red) !important;
  --ds-chart-danger-bold-hovered: var(--atom-red) !important;
  --ds-chart-warning: var(--atom-yellow) !important;
  --ds-chart-warning-hovered: var(--atom-yellow) !important;
  --ds-chart-warning-bold: var(--atom-yellow) !important;
  --ds-chart-warning-bold-hovered: var(--atom-yellow) !important;
  --ds-chart-success: var(--atom-green) !important;
  --ds-chart-success-hovered: var(--atom-green) !important;
  --ds-chart-success-bold: var(--atom-green) !important;
  --ds-chart-success-bold-hovered: var(--atom-green) !important;
  --ds-chart-discovery: var(--atom-magenta) !important;
  --ds-chart-discovery-hovered: var(--atom-magenta) !important;
  --ds-chart-discovery-bold: var(--atom-magenta) !important;
  --ds-chart-discovery-bold-hovered: var(--atom-magenta) !important;
  --ds-chart-information: var(--atom-blue) !important;
  --ds-chart-information-hovered: var(--atom-blue) !important;
  --ds-chart-information-bold: var(--atom-blue) !important;
  --ds-chart-information-bold-hovered: var(--atom-blue) !important;
  --ds-surface: var(--atom-background) !important;
  --ds-surface-hovered: var(--atom-background) !important;
  --ds-surface-pressed: var(--atom-background) !important;
  --ds-surface-overlay: var(--atom-background) !important;
  --ds-surface-overlay-hovered: var(--atom-background) !important;
  --ds-surface-overlay-pressed: var(--atom-background) !important;
  --ds-surface-raised: var(--atom-background) !important;
  --ds-surface-raised-hovered: var(--atom-background) !important;
  --ds-surface-raised-pressed: var(--atom-background) !important;
  --ds-surface-sunken: var(--atom-background) !important;
  --ds-shadow-overflow: 0px 0px 12px #0304048F, 0px 0px 1px #03040480 !important;
  --ds-shadow-overflow-perimeter: #03040480 !important;
  --ds-shadow-overflow-spread: #0304048f !important;
  --ds-shadow-overlay: inset 0px 0px 0px 1px #BCD6F01F, 0px 8px 12px #0304045C, 0px 0px 1px #03040480 !important;
  --ds-shadow-raised: inset 0px 0px 0px 1px #00000000, 0px 1px 1px #03040480, 0px 0px 1px #03040480 !important;
  --ds-opacity-disabled: 0.4 !important;
  --ds-opacity-loading: 0.2 !important;
  --ds-UNSAFE-transparent: transparent !important;
--ds-text-highEmphasis: var(--atom-black-light) !important;
--ds-text-link-pressed: var(--atom-blue) !important;
--ds-text-link-resting: var(--atom-blue) !important;
--ds-text-lowEmphasis: var(--atom-black-light) !important;
--ds-text-mediumEmphasis: var(--atom-black-light) !important;
--ds-text-onBold: var(--atom-black) !important;
--ds-text-onBoldWarning: var(--atom-black) !important;
--ds-border-focus: var(--atom-blue) !important;
--ds-border-neutral: #A6C5E229 !important;
--ds-background-accent-red: var(--atom-red) !important;
--ds-background-accent-red-bold: var(--atom-red) !important;
--ds-background-accent-orange: var(--atom-yellow) !important;
--ds-background-accent-orange-bold: var(--atom-yellow) !important;
--ds-background-accent-yellow: var(--atom-yellow) !important;
--ds-background-accent-yellow-bold: var(--atom-yellow) !important;
--ds-background-accent-green: var(--atom-green) !important;
--ds-background-accent-green-bold: var(--atom-green) !important;
--ds-background-accent-teal: var(--atom-cyan) !important;
--ds-background-accent-teal-bold: var(--atom-cyan) !important;
--ds-background-accent-blue: var(--atom-blue) !important;
--ds-background-accent-blue-bold: var(--atom-blue) !important;
--ds-background-accent-purple: var(--atom-magenta) !important;
--ds-background-accent-purple-bold: var(--atom-magenta) !important;
--ds-background-accent-magenta: var(--atom-magenta) !important;
--ds-background-accent-magenta-bold: var(--atom-magenta) !important;
--ds-background-blanket: #03040442 !important;
--ds-background-boldBrand-hover: var(--atom-green) !important;
--ds-background-boldBrand-pressed: var(--atom-green) !important;
--ds-background-boldBrand-resting: var(--atom-green) !important;
--ds-background-boldDanger-hover: var(--atom-red) !important;
--ds-background-boldDanger-pressed: var(--atom-red) !important;
--ds-background-boldDanger-resting: var(--atom-red) !important;
--ds-background-boldDiscovery-hover: var(--atom-magenta) !important;
--ds-background-boldDiscovery-pressed: var(--atom-magenta) !important;
--ds-background-boldDiscovery-resting: var(--atom-magenta) !important;
--ds-background-boldNeutral-hover: #B6C2CF !important;
--ds-background-boldNeutral-pressed: #C7D1DB !important;
--ds-background-boldNeutral-resting: #9FADBC !important;
--ds-background-boldSuccess-hover: var(--atom-green) !important;
--ds-background-boldSuccess-pressed: var(--atom-green) !important;
--ds-background-boldSuccess-resting: var(--atom-green) !important;
--ds-background-boldWarning-hover: var(--atom-yellow) !important;
--ds-background-boldWarning-pressed: var(--atom-yellow) !important;
--ds-background-boldWarning-resting: var(--atom-yellow) !important;
--ds-background-card: #1D2125 !important;
--ds-background-default: #161A1D !important;
--ds-background-inverse: #00000029 !important;
--ds-background-overlay: #22272B !important;
--ds-background-selected-hover: #A6C5E229 !important;
--ds-background-selected-resting: #A1BDD914 !important;
--ds-background-subtleBorderedNeutral-pressed: #A1BDD914 !important;
--ds-background-subtleBorderedNeutral-resting: #BCD6F00A !important;
--ds-background-subtleBrand-hover: var(--atom-green) !important;
--ds-background-subtleBrand-pressed: var(--atom-green) !important;
--ds-background-subtleBrand-resting: var(--atom-green) !important;
--ds-background-subtleDanger-hover: var(--atom-red) !important;
--ds-background-subtleDanger-pressed: var(--atom-red) !important;
--ds-background-subtleDanger-resting: var(--atom-red) !important;
--ds-background-subtleDiscovery-hover: var(--atom-magenta) !important;
--ds-background-subtleDiscovery-pressed: var(--atom-magenta) !important;
--ds-background-subtleDiscovery-resting: var(--atom-magenta) !important;
--ds-background-subtleNeutral-hover: #A6C5E229 !important;
--ds-background-subtleNeutral-pressed: #BFDBF847 !important;
--ds-background-subtleNeutral-resting: #A1BDD914 !important;
--ds-background-subtleSuccess-hover: var(--atom-green) !important;
--ds-background-subtleSuccess-pressed: var(--atom-green) !important;
--ds-background-subtleSuccess-resting: var(--atom-green) !important;
--ds-background-subtleWarning-hover: var(--atom-yellow) !important;
--ds-background-subtleWarning-pressed: var(--atom-yellow) !important;
--ds-background-subtleWarning-resting: var(--atom-yellow) !important;
--ds-background-sunken: #03040442 !important;
--ds-background-transparentNeutral-hover: #A1BDD914 !important;
--ds-background-transparentNeutral-pressed: #A6C5E229 !important;
--ds-background-brand: var(--atom-green) !important;
--ds-background-brand-hovered: var(--atom-green) !important;
--ds-background-brand-pressed: var(--atom-green) !important;
--ds-interaction-inverse-hovered: #ffffff33 !important;
--ds-interaction-inverse-pressed: #ffffff5c !important;
--ds-accent-boldBlue: var(--atom-blue) !important;
--ds-accent-boldGreen: var(--atom-green) !important;
--ds-accent-boldOrange: var(--atom-yellow) !important;
--ds-accent-boldPurple: var(--atom-magenta) !important;
--ds-accent-boldRed: var(--atom-red) !important;
--ds-accent-boldTeal: var(--atom-cyan) !important;
--ds-accent-subtleBlue: var(--atom-blue) !important;
--ds-accent-subtleGreen: var(--atom-green) !important;
--ds-accent-subtleMagenta: var(--atom-magenta) !important;
--ds-accent-subtleOrange: var(--atom-yellow) !important;
--ds-accent-subtlePurple: var(--atom-magenta) !important;
--ds-accent-subtleRed: var(--atom-red) !important;
--ds-accent-subtleTeal: var(--atom-cyan) !important;
--ds-iconBorder-brand: var(--atom-green) !important;
--ds-iconBorder-danger: var(--atom-red) !important;
--ds-iconBorder-warning: var(--atom-yellow) !important;
--ds-iconBorder-success: var(--atom-green) !important;
--ds-iconBorder-discovery: var(--atom-magenta) !important;
--ds-overlay-hover: #BFDBF847 !important;
--ds-overlay-pressed: #9BB4CA80 !important;
--ds-card: 0px 1px 1px #03040480, 0px 0px 1px #03040480 !important;

}
.aui-lozenge {
  border-radius: 0px !important;
  color: var(--atom-background) !important;
}

.ghx-parent-stub .ghx-key, .ghx-parent-stub .ghx-summary {
  color: var(--atom-text-inverse) !important;
}

.ghx-issue {
  border-radius: 0px !important;
  color: var(--atom-background) !important;
  background: var(--atom-black-light) !important;
}

.ghx-issue.ghx-selected {
  border-radius: 0px !important;
  background: var(--atom-blue) !important;
}
.ghx-issue.ghx-selected section {
  color: var(--atom-text-inverse) !important;
}

.ghx-issue.ghx-flagged {
  border-radius: 0px !important;
  background: var(--atom-yellow) !important;
}
.ghx-issue.ghx-flagged section {
  color: var(--atom-text-inverse) !important;
}

.ghx-issue-compact.ghx-selected {
  border-radius: 0px !important;
  background: var(--atom-blue) !important;
}
.ghx-issue-compact.ghx-selected.ghx-issue-content {
  color: var(--atom-text-inverse) !important;
}

.ghx-issue-compact.ghx-flagged {
  border-radius: 0px !important;
  background: var(--atom-yellow) !important;
  color: var(--atom-text-inverse) !important;
}
#ghx-content-group > div.ghx-sprint-group > div.ghx-backlog-container.ghx-sprint-active.js-sprint-container.ghx-open.ui-droppable > div.ghx-meta.ghx-disabled > div.ghx-issues.js-issue-list.ghx-has-issues > div.js-issue.ghx-backlog-card.ghx-newcard.js-sortable.js-parent-drag.ghx-issue-compact.ghx-done.ghx-type-10100.ghx-selected.ghx-selected-primary > div.ghx-issue-content > div.ghx-row.ghx-plan-main-fields > div > span,
#ghx-content-group > div.ghx-sprint-group > div.ghx-backlog-container.ghx-sprint-active.js-sprint-container.ghx-open.ui-droppable > div.ghx-meta.ghx-disabled > div.ghx-issues.js-issue-list.ghx-has-issues > div.js-issue.ghx-backlog-card.ghx-newcard.js-sortable.js-parent-drag.ghx-issue-compact.ghx-type-10201.ghx-flagged > div.ghx-issue-content > div.ghx-row.ghx-plan-main-fields > div > span {
  color: var(--atom-text-inverse) !important;
}

button {
  border-radius: 0px !important;
  margin-left: 2px;
  margin-right: 2px;
}

[data-component-selector="jira-issue-view-select-inline-edit-read-view-container"] a {
  color: var(--atom-text) !important;
  border-radius: 0px !important;
}

[data-testid="issue.issue-view.views.common.child-issues-panel.issues-container"] ul > div {
  border-radius: 0px !important;
}

[data-testid="issue.fields.status.common.ui.status-lozenge.3"] > span:first-child {
  color: var(--atom-text-inverse) !important;
  border-radius: 0px !important;
}
[data-testid="issue.fields.status.common.ui.status-lozenge.4"] > span:first-child {
  color: var(--atom-text-inverse) !important;
  border-radius: 0px !important;
}

[data-test-id="issue.views.issue-base.foundation.breadcrumbs.breadcrumb-current-issue-container"] a {
  padding-left: 5px !important;
  padding-right: 5px !important;
  border-radius: 0px !important;
}
[data-test-id="issue.views.issue-base.foundation.breadcrumbs.parent-issue.item"] a {
  padding-left: 5px !important;
  padding-right: 5px !important;
  border-radius: 0px !important;
}
[data-test-id="rapidboard-breadcrumbs"] a {
  padding-left: 5px !important;
  padding-right: 5px !important;
  border-radius: 0px !important;
}

#ak-side-navigation [role="group"]> div:nth-child(2){
  border-radius: 0px !important;
}

[data-testid="navigation-apps-sidebar-software-classic.ui.menu.roadmap-link"],
[data-testid="navigation-apps-sidebar-software-classic.ui.menu.backlog-link"],
[data-testid="navigation-apps-sidebar-software-classic.ui.menu.board-link"],
[data-testid="navigation-apps-sidebar-software-classic.ui.menu.reports-link--item"] {
  color: var(--atom-text-inverse) !important;
}


`)

