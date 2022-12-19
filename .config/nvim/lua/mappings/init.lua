local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }


vim.g.mapleader = ' '
-- open explorer tree
map('n','<leader>e', ':NvimTreeToggle<CR>', opts)

-- don't forget to install wl-clipboard
-- Copy to clipboard
map('v', '<leader>y', '"+y', opts)
map('n', '<leader>Y',  '"+yg_', opts) --copy to end of file
map('n', '<leader>y',  '"+y', opts)
map('n', '<leader>yy',  '"+yy', opts) --copy whole line
-- Paste from clipboard
map('n', '<leader>p', '"+p', opts)
map('n', '<leader>P', '"+P', opts)
map('v', '<leader>p', '"+p', opts)
map('v', '<leader>P', '"+P', opts)
