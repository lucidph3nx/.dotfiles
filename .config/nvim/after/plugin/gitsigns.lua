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
      vim.keymap.set('n', '<leader>gph', 
        gs.prev_hunk, make_opts('[g]it [p]revious [h]unk', opts))
      vim.keymap.set('n', '<leader>gnh',
        gs.next_hunk, make_opts('[g]it [n]ext [h]unk', opts))
      vim.keymap.set('n', '<leader>gsh',
        gs.stage_hunk, make_opts('[g]it [s]tage [h]unk', opts))
      vim.keymap.set('n', '<leader>guh',
        gs.undo_stage_hunk, make_opts('[g]it [u]nstage [h]unk', opts))

      vim.keymap.set('n', '<leader>gtd',
        gs.toggle_deleted, make_opts('[g]it [t]oggle [d]eleted', opts))
      vim.keymap.set('n', '<leader>gtb',
        gs.toggle_current_line_blame, make_opts('[g]it [t]oggle [b]lame', opts))
    end
})

