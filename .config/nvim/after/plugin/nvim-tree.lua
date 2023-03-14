require('nvim-tree').setup({
    filters = {
       --disable the filtering out of dotfiles
        dotfiles = false
    },
    git = {
      enable = true,
      ignore = false,
      timeout = 500,
    },
    update_focused_file = {
        enable = true,
        update_root = true,
        ignore_list = {},
      },
})

-- Open For Directories And Change Neovim's Directory
local function open_nvim_tree(data)
  -- buffer is a directory
  local directory = vim.fn.isdirectory(data.file) == 1
  if not directory then
    -- change to the directory of the file
    -- vim.cmd.cd(vim.fn.fnamemodify(data.file, ":h"))
    return
  end
  -- create a new, empty buffer
  vim.cmd.enew()
  -- wipe the directory buffer
  vim.cmd.bw(data.buf)
  -- change to the directory
  vim.cmd.cd(data.file)
  -- open the tree
  -- require("nvim-tree.api").tree.open()
end

-- automatically run open_nvim_tree on open
vim.api.nvim_create_autocmd("VimEnter", { callback = open_nvim_tree })

-- attempt at autoclose
vim.api.nvim_create_autocmd("BufEnter", {
  nested = true,
  callback = function()
    if #vim.api.nvim_list_wins() == 1 and require("nvim-tree.utils").is_nvim_tree_buf() then
      vim.cmd "quit"
    end
  end
})

vim.keymap.set('n', '<leader>et', vim.cmd.NvimTreeToggle, { desc = '[E]xplorer [T]oggle' })
vim.keymap.set('n', '<leader>ef', vim.cmd.NvimTreeFindFile, { desc = '[E]xplorer [F]ind File' })
vim.keymap.set('n', '<leader>ec', vim.cmd.NvimTreeCollapse, { desc = '[E]xplorer [C]ollapse Folders' })

