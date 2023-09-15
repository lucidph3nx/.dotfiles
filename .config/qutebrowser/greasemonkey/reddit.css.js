// ==UserScript==
// @name    Userstyle (reddit.css)
// @include    https://www.reddit.com/*
// ==/UserScript==
GM_addStyle(`
/* Hide annoying stuff */
 .give-gold-button, .goldvertisement, .embed-comment, .promoted, .nub {
     display: none !important;
}
/* Reset */
 *, *:before, *:after {
     background-color: var(--system-theme-bg0) !important;
     color: var(--system-theme-fg) !important;
}
.reddit-video-player-root * {
     background: rgba(0,0,0,0) !important;
}
.reddit-video-controller-root > div.reddit-video-seek-bar-root > div.seek-bar-bar.seek-bar-progress {
     background: var(--system-theme-green) !important;
}
/* Default links */
 a {
     color: var(--system-theme-blue) !important;
}
 a:visited {
     color: var(--system-theme-magenta) !important;
}
 a:hover {
     color: var(--system-theme-magenta) !important;
}
/* Background */
 html, body, #sr-more-link {
     background-color: var(--system-theme-bg0) !important;
}
/* Top bar */
 .drop-choices, .hover-bubble, .modal-dialog {
     background: var(--system-theme-bg0) !important;
}
 .tabmenu .selected a {
     color: var(--system-theme-fg) !important;
}
/* Side bar */
 .listing-chooser-collapsed .grippy {
     width: 1px !important;
}
 .listing-chooser-collapsed .listing-chooser {
     padding-right: 1px !important;
}
 .listing-chooser li.selected {
     box-shadow: none !important;
}
 .grippy:after {
     display: none !important;
}
/* Inputs and buttons */
 input, textarea, .linkinfo .shortlink input, .new-comment .usertext-body, .morelink a, .morelink:hover a, .fancy-toggle-button a, .usertext button {
     background: var(--system-theme-bg0) !important;
     color: var(--system-theme-fg) !important;
     font-weight: normal !important;
}
/* Listing */
 .thing .title {
     color: var(--system-theme-fg) !important;
}
 .title:visited {
     color: var(--system-theme-fg) !important;
}
 .thing .title:hover {
     color: var(--system-theme-fg) !important;
}
 .expando-button {
     filter: brightness(45%) contrast(180%);
     background-color: transparent !important;
}
 .moderator, .green {
     color: var(--system-theme-green) !important;
}
 .admin, .nsfw-stamp * {
     color: var(--system-theme-red) !important;
}
 .pagename a, .trophy-name {
     color: var(--system-theme-fg) !important;
}
 .buttons li {
     padding: 0 !important;
}
 .buttons a {
     margin-right: 8px !important;
     color: var(--system-theme-fg) !important;
}
 .buttons a:visited {
     color: var(--system-theme-fg) !important;
}
 .buttons a:hover {
     color: var(--system-theme-fg) !important;
}
 .pagename, .tabmenu li, .link .midcol, .buttons a, .subreddit {
     font-weight: normal !important;
}
 .search-expando.collapsed:before, .comment-fade {
     display: none !important;
}
 .recommended-link {
     border-color: var(--system-theme-bg0) !important;
}
/* Comments */
 .link .usertext .md, blockquote, pre, code, .md blockquote {
     border-left: solid 4px var(--system-theme-bg0) !important;
}
 .md td {
     border: solid 1px var(--system-theme-bg0) !important;
}
 hr {
     border-bottom: solid 1px var(--system-theme-bg0) !important;
}
 .comment .author, .morecomments a {
     font-weight: normal !important;
}
/* RES */
 .guider, .guiders_button, .res-fancy-toggle-button, #RESConsoleContainer, #RESShortcutsAddFormContainer {
     background: var(--system-theme-bg0) !important;
}
 .RESDialogSmall, .RESDropdownOptions, .RESNotification, #alert_message {
     background: var(--system-theme-bg0) !important;
}
 .RES-keyNav-activeElement, .RES-keyNav-activeElement .md-container {
     background: var(--system-theme-bg0) !important;
}
 .res-nightmode .arrow {
     filter: none !important;
}
/* Thumbnails */
 .thumbnail.self {
     background-image: url(https://img.icons8.com/fluency/344/reddit.png);
    /* Reddit icon by Icons8: https://icons8.com/icon/h3FOPWMfgNnV/reddit */
     background-position: 4px -5px;
     background-repeat: no-repeat;
     background-size: 55px 55px;
}
 .thumbnail.spoiler {
     background-image: url(https://i.imgur.com/lpzPMKX.png);
    /* Reddit icon by Icons8: https://icons8.com/icon/h3FOPWMfgNnV/reddit */
     background-position: 4px -5px;
     background-repeat: no-repeat;
     background-size: 55px 55px;
}
 .thumbnail.default {
     background-image: url(https://i.imgur.com/ZPS7RHE.png);
    /* Reddit icon by Icons8: https://icons8.com/icon/h3FOPWMfgNnV/reddit */
     background-position: 4px -5px;
     background-repeat: no-repeat;
     background-size: 55px 55px;
}
/* Upvote/dowmnvote */
 .arrow.upmod {
     background-image: url(https://i.imgur.com/fmckYhF.png);
    /* Thick Arrow Pointing Up icon by Icons8: https://icons8.com/icon/99690/thick-arrow-pointing-up */
     background-position: -4.5px -1px;
     background-repeat: no-repeat;
     background-size: 24px 24px;
}
 .arrow.downmod {
     background-image: url(https://i.imgur.com/aJJvTy5.png);
    /* Thick Arrow Pointing Up icon by Icons8: https://icons8.com/icon/99690/thick-arrow-pointing-up */
     background-position: -4.5px -9px;
     background-repeat: no-repeat;
     background-size: 24px 24px;
}
/* Score */
 .link .score.likes {
     color: var(--system-theme-red) !important;
}
 .link .score.dislikes {
     color: var(--system-theme-magenta) !important;
}
 .linkinfo>div:nth-child(2)>span:nth-child(1) {
     color: var(--system-theme-green) !important;
}
/* Subreddit header */
 .pagename a, .trophy-name {
     color: var(--system-theme-aqua) !important;
}
 .tabmenu .selected a {
     color: var(--system-theme-aqua) !important;
     font-weight: bold;
}
/* Reddit logo */
 #header-img.default-header {
     text-indent: -9999px;
     background-image: url(https://i.imgur.com/3cKNTd1.png);
     background-position: 10px -11px;
     background-size: 112px 64px;
     background-repeat: no-repeat;
     height: 40px;
     width: 130px;
     display: inline-block;
     vertical-align: bottom;
}
/* Misc */
 a.edit-btn {
     background-color: var(--system-theme-fg) !important;
     white-space: nowrap;
     float: none;
}
 .linkinfo .shortlink input, .new-comment .usertext-body, .morelink a, .morelink:hover a, .fancy-toggle-button a {
     background: var(--system-theme-bg0) !important;
     color: var(--system-theme-fg) !important;
     font-weight: normal !important;
}
 input, textarea {
     background: rgb(40, 44, 51) !important;
     color: var(--system-theme-fg) !important;
}
 .submit-link>div:nth-child(1)>a:nth-child(1) {
     background: var(--system-theme-blue) !important;
     color: rgba(248, 248, 242, 0.85) !important;
     font-weight: bold !important;
}
 .submit-text>div:nth-child(1)>a:nth-child(1) {
     background: var(--system-theme-blue) !important;
     color: rgba(248, 248, 242, 0.85) !important;
     font-weight: bold !important;
}
 a.hover {
     color: var(--system-theme-aqua) !important;
}
`)
