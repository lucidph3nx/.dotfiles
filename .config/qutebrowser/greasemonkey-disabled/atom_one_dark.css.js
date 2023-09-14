// ==UserScript==
// @name    Userstyle (atom_one_dark.css)
// @include   /^qute://start/*/
// @include    about:blank
// ==/UserScript==
GM_addStyle(`
body {
  background-color: #282c34;
  font-family: "JetbrainsMonoNerdFont", monospace;
}
.header {
  margin-top: 220px;
}
input {
  background-color: #454C59;
  color: #cfd7e6;
  border-radius: 0px !important;
  font-family: "JetbrainsMonoNerdFont", monospace;
}
::placeholder {
  color: #cfd7e6 !important;
}
.bookmarks {
  display: none;
}
`)
