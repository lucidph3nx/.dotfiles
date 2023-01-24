vim.keymap.set('n', '<leader>gs', vim.cmd.Git, { desc = '[G]it [S]tatus in Fugitive'})

local fugitive_lucidph3nx = vim.api.nvim_create_augroup("fugitive_lucidph3nx", {})

local autocmd = vim.api.nvim_create_autocmd
autocmd("BufWinEnter", {
    group = fugitive_lucidph3nx,
    pattern = "*",
    callback = function()
        -- only applies to files with filetype fugitive
        if vim.bo.ft ~= "fugitive" then
            return
        end

        local bufnr = vim.api.nvim_get_current_buf()
        local opts = {buffer = bufnr, remap = false}

        vim.keymap.set("n", "<leader>p", function()
            vim.cmd.Git('push')
        end, opts)

        vim.keymap.set("n", "<leader>P", function()
            vim.cmd.Git('pull --rebase')
        end, opts)
    end,
})
