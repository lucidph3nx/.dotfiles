// ==UserScript==
// @name    Userstyle (github.css)
// @include    https://github.com/*
// ==/UserScript==
GM_addStyle(`
:root {
    --borderRadius-small: 0;
    --borderRadius-medium: 0;
    --borderRadius-large: 0;
    --borderRadius-full: 0;
}
body {
  font-family: JetBrains Mono,monospace !important;
}
.btn {
  border-radius: 0px !important;
}
.form-control {
  border-radius: 0px !important;
}
.Label {
  border-radius: 0px !important;
}
.Counter {
  border-radius: 0px !important;
}
.topic-tag {
  border-radius: 0px !important;
}
.rounded-2 {
  border-radius: 0px !important;
}
.Box--responsive {
  border-radius: 0px !important;
}
.Progress {
  border-radius: 0px !important;
}
.markdown-body .highlight pre, .markdown-body pre {
  border-radius: 0px !important;
}
.search-suggestions {
  border-radius: 0px !important;
}
.graph-before-activity-overview {
  border-radius: 0px !important;
}
.filter-item {
  border-radius: 0px !important;
}
`)
