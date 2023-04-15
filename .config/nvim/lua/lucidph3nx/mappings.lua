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

-- Helix inspired redo
map('n', 'U', '<C-r>', opts)


-- when something is highlighted, move up and down with J & K
map("v", "J", ":m '>+1<CR>gv=gv", opts)
map("v", "K", ":m '<-2<CR>gv=gv", opts)

-- quickfix list
map("n", "<leader>q", "<cmd>copen<CR>", opts)
map("n", "<C-k>", "<cmd>cnext<CR>", opts)
map("n", "<C-j>", "<cmd>cprev<CR>", opts)
-- quickfix on current window
map("n", "<leader>k", "<cmd>lnext<CR>", opts)
map("n", "<leader>j", "<cmd>lprev<CR>", opts)

-- switch to new session in tmux
map("n", "<C-f>", "<cmd>!tmux neww tmux-sessionizer<CR>", opts)

-- start a replace with current word
map("n", "<leader>fr", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]], opts)
-- same but with current visual selection
map("v", "<leader>fr", [[y<Esc>:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]], opts)
-- make current file executable
map("n", "<leader>x", "<cmd>!chmod +x %<CR>", opts)

-- encrypt file with sops
map('n', '<leader>ds', ':lua sops_helper.decrypt()<CR>', opts)
map('n', '<leader>es', ':lua sops_helper.encrypt()<CR>', opts)

