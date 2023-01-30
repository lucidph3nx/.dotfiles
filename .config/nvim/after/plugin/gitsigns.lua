require('gitsigns').setup({
  signcolumn = true,
  current_line_blame = true,
    current_line_blame_opts = {
      virt_text = true,
      virt_text_pos = 'eol',
      delay = 200,
      ignore_whitespace = false,
    },
})

