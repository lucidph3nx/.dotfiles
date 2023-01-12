require('nvim-tree').setup({
    filters = {
       --disable the filtering out of dotfiles
        dotfiles = false
    },
})

-- attempt at autoclose
vim.api.nvim_create_autocmd("BufEnter", {
  nested = true,
  callback = function()
    if #vim.api.nvim_list_wins() == 1 and require("nvim-tree.utils").is_nvim_tree_buf() then
      vim.cmd "quit"
    end
  end
})

vim.keymap.set('n', '<leader>et', vim.cmd.NvimTreeToggle)
