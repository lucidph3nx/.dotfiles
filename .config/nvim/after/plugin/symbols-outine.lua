require('symbols-outline').setup {
  highlight_hovered_item = true,
  show_guides = true,
  auto_preview = false,
  position = 'right',
  keymaps = {
    close = {"<Esc>", "q"},
    goto_location = "<Cr>",
    focus_location = "o",
    hover_symbol = "<C-space>",
    toggle_preview = "K",
    rename_symbol = "r",
    code_actions = "a",
    fold = "h",
    unfold = "l",
    fold_all = "W",
    unfold_all = "E",
    fold_reset = "R",
  },
  lsp_blacklist = {},
}

-- open on <leader>o 
vim.api.nvim_set_keymap('n', '<leader>o', '<cmd>SymbolsOutline<CR>', { noremap = true, silent = true })
