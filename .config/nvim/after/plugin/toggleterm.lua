
require("toggleterm").setup {
    -- open_mapping = [[<c-\>]],
    size = 15,
    shell = "zsh",
    hide_numbers = true,
    close_on_exit = true,
    direction = "float",
    float_opts = {
        border = "single",
        width = 100,
        height = 30,
        winblend = 3,
    },
}

vim.keymap.set('n', '<tab>', vim.cmd.ToggleTerm, { desc = 'Toggle Terminal' })
vim.keymap.set('t', '<tab>', vim.cmd.ToggleTerm, { desc = 'Toggle Terminal' })
