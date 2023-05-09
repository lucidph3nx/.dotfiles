local lsp = require('lsp-zero')

lsp.preset('recommended')
 -- https://github.com/neovim/nvim-lspconfig/blob/master/doc/server_configurations.md#configurations
lsp.ensure_installed({
  'tsserver',
  'eslint',
  'lua_ls',
  'ltex',
})

-- Fix Undefined global 'vim'
lsp.configure('lua_ls', {
    settings = {
        Lua = {
            diagnostics = {
                globals = { 'vim' }
            }
        }
    }
})

lsp.configure('ltex', {
  settings = {
    ltex = {
      language = 'en-NZ',
      additionalRules = {
        enablePickyRules = false,
      },
      dictionary = {
        ['en-NZ'] = { 'neovim' }
      },
      checkFrequency = 'edit',
      hiddenFalsePositives = {},
      hiddenTruePositives = {},
    }
  }
})

lsp.configure('yamlls', {
  settings = {
    yaml = {
      keyOrdering = false
    }
  }
})

lsp.configure('sqlls', {
  cmd = { 'sql-language-server', 'up', '--method', 'stdio' },
  filetypes = { 'sql' },
  root_dir = require('lspconfig.util').root_pattern('.git', vim.fn.getcwd()),
})

local cmp = require('cmp')
local cmp_select = {behavior = cmp.SelectBehavior.Select}
local cmp_mappings = lsp.defaults.cmp_mappings({
  ['<C-p>'] = cmp.mapping.select_prev_item(cmp_select),
  ['<C-n>'] = cmp.mapping.select_next_item(cmp_select),
  ['<C-y>'] = cmp.mapping.confirm({ select = true }),
  ["<C-Space>"] = cmp.mapping.complete(),
})

lsp.on_attach(function(client, bufnr)
  local opts = {buffer = bufnr, remap = false}

  vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, make_opts("[g]et [D]eclaration", opts))
  vim.keymap.set("n", "gd", vim.lsp.buf.definition, make_opts("[g]et [d]efinition", opts))
  vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, make_opts("[g]et [i]mplementation", opts))
  vim.keymap.set('n', 'gt', vim.lsp.buf.type_definition, make_opts("[g]et [t]ype definition", opts))
  vim.keymap.set("n", "K", vim.lsp.buf.hover, make_opts("[K]eyword", opts))
  vim.keymap.set("n", "<leader>vd", vim.diagnostic.open_float, make_opts("[v]iew [d]iagnostics", opts))
  vim.keymap.set("n", "<leader>]", vim.diagnostic.goto_next, make_opts("Next Diagnostic", opts))
  vim.keymap.set("n", "<leader>[", vim.diagnostic.goto_prev, make_opts("Previous Diagnostic", opts))
  vim.keymap.set("n", "<leader>lca", vim.lsp.buf.code_action, make_opts("[l]sp [c]ode [a]ction", opts))
  vim.keymap.set("n", "<leader>lrr", vim.lsp.buf.references, make_opts("[l]sp [r]eferences (quickfix)", opts))
  vim.keymap.set("n", "<leader>lrn", vim.lsp.buf.rename, make_opts("[l]sp [r]ename", opts))
  vim.keymap.set('n', '<leader>f', function() vim.lsp.buf.format { async = true } end, make_opts("[f]ormat", opts))
end)

lsp.setup()
