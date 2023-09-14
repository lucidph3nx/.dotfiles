// ==UserScript==
// @name    Userstyle (everforest_dark.css)
// @include   /^qute://start/*/
// @include    about:blank
// ==/UserScript==
GM_addStyle(`
body {
  background-color: #2d353b;
  font-family: "JetbrainsMonoNerdFont", monospace;
}
.header {
  margin-top: 220px;
}
input {
  background-color: #475258;
  color: #d3c6aa;
  border-radius: 0px !important;
  font-family: "JetbrainsMonoNerdFont", monospace;
}
::placeholder {
  color: #d3c6aa !important;
}
.bookmarks {
  display: none;
}
`)
