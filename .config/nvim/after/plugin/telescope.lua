local telescope = require('telescope')
local builtin = require('telescope.builtin')

telescope.setup {
  pickers = {
    find_files = {
      hidden = true
    },
    grep_string = {
      hidden = true
    }
  }
}


vim.keymap.set('n', '<leader>sf', builtin.find_files, { desc = '[S]earch [F]iles' })
vim.keymap.set('n', '<leader>st', builtin.git_files, { desc = '[S]earch [T]racked files (git)' })
vim.keymap.set('n', '<leader>sc', builtin.git_commits, { desc = '[S]earch [C]ommits (git)' })
vim.keymap.set('n', '<leader>sh', builtin.help_tags, { desc = '[S]earch [H]elp' })
vim.keymap.set('n', '<leader>sw', builtin.grep_string, { desc = '[S]earch current [W]ord' })
vim.keymap.set('v', '<leader>ss', builtin.grep_string, { desc = '[S]earch [S]election' })
vim.keymap.set('n', '<leader>sg', builtin.live_grep, { desc = '[S]earch by [G]rep' })
vim.keymap.set('n', '<leader>sd', builtin.diagnostics, { desc = '[S]earch [D]iagnostics' })
vim.keymap.set('n', '<leader>sk', builtin.keymaps, { desc = '[S]earch [K]eymaps' })
vim.keymap.set('n', '<leader>sb', builtin.buffers, { desc = '[S]earch [B]uffers' })
vim.keymap.set('n', '<leader>sj', builtin.jumplist, { desc = '[S]earch [J]umplist' })

