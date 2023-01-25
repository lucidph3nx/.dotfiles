require('copilot').setup({
  panel = {
    enabled = true,
    auto_refresh = false,
    layout = {
      position = "bottom", -- | top | left | right
      ratio = 0.4
    },
  },
  suggestion = {
    enabled = true,
    auto_trigger = true,
    debounce = 75,
  },
  filetypes = {
    markdown = false,
    help = false,
    gitcommit = false,
    gitrebase = false,
    hgcommit = false,
    svn = false,
    cvs = false,
    ["."] = true,
  },
  -- pin to specific node binary
  copilot_node_command = vim.fn.expand("$HOME") .. "/.local/share/nvm/versions/node/v18.13.0/bin/node",
})

-- suggestion keybindings for insert mode
vim.keymap.set("i", "<CR>", function()
  vim.cmd.Copilot('suggestion accept')
end, {desc = 'Accept suggestion'})

vim.keymap.set("i", "<C-J>", function()
  vim.cmd.Copilot('suggestion prev')
end, {desc = 'Previous suggestion'})

vim.keymap.set("i", "<C-K>", function()
  vim.cmd.Copilot('suggestion next')
end, {desc = 'Next suggestion'})

-- pannel stuff
vim.keymap.set("n", "<leader>cp", function()
  vim.cmd.Copilot('panel open')
end, {desc = '[C]opilot [P]anel'})

local copilot_lucidph3nx = vim.api.nvim_create_augroup("copilot_lucidph3nx", {})
-- key bindings inside the copilot panel
local autocmd = vim.api.nvim_create_autocmd
autocmd("BufWinEnter", {
    group = copilot_lucidph3nx,
    pattern = "*",
    callback = function()
        -- only applies to files with filetype fugitive
        if vim.bo.ft ~= "Bot" then
            return
        end

        local bufnr = vim.api.nvim_get_current_buf()
        local opts = {buffer = bufnr, remap = false}

        vim.keymap.set("n", "[[", function()
          vim.cmd.Copilot('panel jump_prev')
        end, opts)

        vim.keymap.set("n", "]]", function()
          vim.cmd.Copilot('panel jump_next')
        end, opts)

        vim.keymap.set("n", "r", function()
          vim.cmd.Copilot('panel refresh')
        end, opts)

        vim.keymap.set("n", "<CR>", function()
          vim.cmd.Copilot('panel accept')
        end, opts)
    end,
})
