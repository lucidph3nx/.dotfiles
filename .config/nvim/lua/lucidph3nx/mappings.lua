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
map('n', 'U', '<C-r>', make_opts('Redo', opts))


-- when something is highlighted, move up and down with J & K
map("v", "J", ":m '>+1<CR>gv=gv", make_opts('Move line down', opts))
map("v", "K", ":m '<-2<CR>gv=gv", make_opts('Move line up', opts))

-- quickfix list
map("n", "<leader>q", "<cmd>copen<CR>", make_opts('Open quickfix list', opts))
map("n", "<C-k>", "<cmd>cnext<CR>", make_opts('Next quickfix item', opts))
map("n", "<C-j>", "<cmd>cprev<CR>", make_opts('Previous quickfix item', opts))

-- switch to new session in tmux
map("n", "<C-f>", "<cmd>!tmux neww tmux-sessionizer<CR>", make_opts('Switch to new tmux session', opts))

-- start a replace with current word
map("n", "<leader>fr", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]], make_opts('[F]ind and [R]eplace', opts))
-- same but with current visual selection
map("v", "<leader>fr", [[y<Esc>:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]], make_opts('[F]ind and [R]eplace', opts))
-- make current file executable
map("n", "<leader>x", "<cmd>!chmod +x %<CR>", make_opts('Make file executable', opts))

-- encrypt file with sops
map('n', '<leader>ds', ':lua sops_helper.decrypt()<CR>', make_opts('[D]ecrypt [S]ops file', opts))
map('n', '<leader>es', ':lua sops_helper.encrypt()<CR>', make_opts('[E]ncrypt [S]ops file', opts))

