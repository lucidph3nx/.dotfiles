
local mark = require("harpoon.mark")
local ui = require("harpoon.ui")

vim.keymap.set("n", "<leader>a", mark.add_file, { desc = '[A]dd file to Harpoon'})
vim.keymap.set("n", "<leader>h", ui.toggle_quick_menu, { desc = 'Toggle [H]arpoon Menu'})

vim.keymap.set("n", "<leader>1", function() ui.nav_file(1) end, { desc = 'Jump Harpoon File [1]'})
vim.keymap.set("n", "<leader>2", function() ui.nav_file(2) end, { desc = 'Jump Harpoon File [2]'})
vim.keymap.set("n", "<leader>3", function() ui.nav_file(3) end, { desc = 'Jump Harpoon File [3]'})
vim.keymap.set("n", "<leader>4", function() ui.nav_file(4) end, { desc = 'Jump Harpoon File [4]'})

