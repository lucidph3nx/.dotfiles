local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }

vim.g.mapleader = ' '

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

-- when something is highlighted, move up and down with J & K
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

-- switch to new session in tmux
vim.keymap.set("n", "<C-f>", "<cmd>silent !tmux neww tmux-sessionizer<CR>")

-- start a replace with current word
vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])

-- make current file executable
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })
