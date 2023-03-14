require('gitsigns').setup({
  signcolumn = true,
  current_line_blame = true,
    current_line_blame_opts = {
      virt_text = true,
      virt_text_pos = 'eol',
      delay = 200,
      ignore_whitespace = false,
    },
    on_attach = function(bufnr)
      local gs = package.loaded.gitsigns
      opts = { buffer = bufnr, remap = false}
      -- keymaps
      vim.keymap.set('n', '<leader>{', gs.prev_hunk, opts)
      vim.keymap.set('n', '<leader>}', gs.next_hunk, opts)

      vim.keymap.set('n', '<leader>td', gs.toggle_deleted, opts)
      vim.keymap.set('n', '<leader>tb', gs.toggle_current_line_blame, opts)
    end
})

