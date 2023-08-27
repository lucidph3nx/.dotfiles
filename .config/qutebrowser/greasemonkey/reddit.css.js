// ==UserScript==
// @name    Userstyle (reddit.css)
// @include    https://www.reddit.com/*
// ==/UserScript==
GM_addStyle(`
:root {
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
}
/* Hide annoying stuff */
 .give-gold-button, .goldvertisement, .embed-comment, .promoted, .nub {
     display: none !important;
}
/* Reset */
 *, *:before, *:after {
     background-color: var(--atom-background) !important;
     color: var(--atom-text) !important;
}
.reddit-video-player-root * {
     background: rgba(0,0,0,0) !important;
}
.reddit-video-controller-root > div.reddit-video-seek-bar-root > div.seek-bar-bar.seek-bar-progress {
     background: var(--atom-green) !important;
}
/* Default links */
 a {
     color: var(--atom-blue) !important;
}
 a:visited {
     color: var(--atom-magenta) !important;
}
 a:hover {
     color: var(--atom-magenta) !important;
}
/* Background */
 html, body, #sr-more-link {
     background-color: var(--atom-background) !important;
}
/* Top bar */
 .drop-choices, .hover-bubble, .modal-dialog {
     background: var(--atom-background) !important;
}
 .tabmenu .selected a {
     color: var(--atom-foreground) !important;
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
     background: var(--atom-background) !important;
     color: var(--atom-foreground) !important;
     font-weight: normal !important;
}
/* Listing */
 .thing .title {
     color: var(--atom-text) !important;
}
 .title:visited {
     color: var(--atom-white) !important;
}
 .thing .title:hover {
     color: var(--atom-white) !important;
}
 .expando-button {
     filter: brightness(45%) contrast(180%);
     background-color: transparent !important;
}
 .moderator, .green {
     color: var(--atom-green) !important;
}
 .admin, .nsfw-stamp * {
     color: var(--atom-red) !important;
}
 .pagename a, .trophy-name {
     color: var(--atom-foreground) !important;
}
 .buttons li {
     padding: 0 !important;
}
 .buttons a {
     margin-right: 8px !important;
     color: var(--atom-foreground) !important;
}
 .buttons a:visited {
     color: var(--atom-foreground) !important;
}
 .buttons a:hover {
     color: var(--atom-white) !important;
}
 .pagename, .tabmenu li, .link .midcol, .buttons a, .subreddit {
     font-weight: normal !important;
}
 .search-expando.collapsed:before, .comment-fade {
     display: none !important;
}
 .recommended-link {
     border-color: var(--atom-background) !important;
}
/* Comments */
 .link .usertext .md, blockquote, pre, code, .md blockquote {
     border-left: solid 4px var(--atom-background) !important;
}
 .md td {
     border: solid 1px var(--atom-background) !important;
}
 hr {
     border-bottom: solid 1px var(--atom-background) !important;
}
 .comment .author, .morecomments a {
     font-weight: normal !important;
}
/* RES */
 .guider, .guiders_button, .res-fancy-toggle-button, #RESConsoleContainer, #RESShortcutsAddFormContainer {
     background: var(--atom-background) !important;
}
 .RESDialogSmall, .RESDropdownOptions, .RESNotification, #alert_message {
     background: var(--atom-background) !important;
}
 .RES-keyNav-activeElement, .RES-keyNav-activeElement .md-container {
     background: var(--atom-background) !important;
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
     color: var(--atom-red) !important;
}
 .link .score.dislikes {
     color: var(--atom-magenta) !important;
}
 .linkinfo>div:nth-child(2)>span:nth-child(1) {
     color: var(--atom-green) !important;
}
/* Subreddit header */
 .pagename a, .trophy-name {
     color: var(--atom-cyan) !important;
}
 .tabmenu .selected a {
     color: var(--atom-cyan) !important;
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
     background-color: var(--atom-white-light) !important;
     white-space: nowrap;
     float: none;
}
 .linkinfo .shortlink input, .new-comment .usertext-body, .morelink a, .morelink:hover a, .fancy-toggle-button a {
     background: var(--atom-background) !important;
     color: var(--atom-white-light) !important;
     font-weight: normal !important;
}
 input, textarea {
     background: rgb(40, 44, 51) !important;
     color: var(--atom-white-light) !important;
}
 .submit-link>div:nth-child(1)>a:nth-child(1) {
     background: var(--atom-blue) !important;
     color: rgba(248, 248, 242, 0.85) !important;
     font-weight: bold !important;
}
 .submit-text>div:nth-child(1)>a:nth-child(1) {
     background: var(--atom-blue) !important;
     color: rgba(248, 248, 242, 0.85) !important;
     font-weight: bold !important;
}
 a.hover {
     color: var(--atom-cyan) !important;
}
`)
