local fn = vim.fn

-- Automatically install packer
local install_path = fn.stdpath 'data' .. '/site/pack/packer/start/packer.nvim'
---@diagnostic disable-next-line: missing-parameter
if fn.empty(fn.glob(install_path)) > 0 then
  PACKER_BOOTSTRAP = fn.system {
    'git',
    'clone',
    '--depth',
    '1',
    'https://github.com/wbthomason/packer.nvim',
    install_path,
  }
  print 'Installing packer close and reopen Neovim...'
  vim.cmd [[packadd packer.nvim]]
end

-- Autocommand that reloads neovim whenever you save the plugins.lua file
vim.cmd [[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerSync
  augroup end
]]

-- Use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, 'packer')
if not status_ok then
  return
end

-- Have packer use a popup window
packer.init {
  -- snapshot = 'july-24',
  snapshot_path = fn.stdpath 'config' .. '/snapshots',
  max_jobs = 50,
  display = {
    open_fn = function()
      return require('packer.util').float { border = 'rounded' }
    end,
    prompt_border = 'rounded', -- Border style of prompt popups.
  },
}
return require('packer').startup(function(use)
  -- Plugin Manager
  use 'wbthomason/packer.nvim'
  -- Theme
  use 'navarasu/onedark.nvim'
  use 'kyazdani42/nvim-web-devicons'
  -- Utilities
  use 'kyazdani42/nvim-tree.lua' -- a sidebar file explorer
  use { 'nvim-telescope/telescope.nvim', tag = '0.1.0',
    requires = { {'nvim-lua/plenary.nvim'} }
  }
  use {'nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'}}
  use 'theprimeagen/harpoon'
  use 'mbbill/undotree'
  use 'tpope/vim-fugitive' -- git integraton
  use 'lewis6991/gitsigns.nvim' -- inline git commit history
  use 'nvim-lualine/lualine.nvim' -- Fancier statusline
  use 'lukas-reineke/indent-blankline.nvim' -- Add indentation guides even on blank lines
  use 'numToStr/Comment.nvim' -- comment visually selected regions with 'gc'
  use {
    'VonHeikemen/lsp-zero.nvim',
    branch = 'v1.x',
    requires = {
      -- LSP Support
      {'neovim/nvim-lspconfig'},
      {'williamboman/mason.nvim'},
      {'williamboman/mason-lspconfig.nvim'},

      -- Autocompletion
      {'hrsh7th/nvim-cmp'},
      {'hrsh7th/cmp-buffer'},
      {'hrsh7th/cmp-path'},
      {'saadparwaiz1/cmp_luasnip'},
      {'hrsh7th/cmp-nvim-lsp'},
      {'hrsh7th/cmp-nvim-lua'},

      -- Snippets
      {'L3MON4D3/LuaSnip'},
      {'rafamadriz/friendly-snippets'},
    }
  }
  use 'windwp/nvim-autopairs' -- automatically close brackets
  use 'akinsho/toggleterm.nvim' -- terminal
  use 'norcalli/nvim-colorizer.lua' -- show hex colours etc
  -- use 'epwalsh/obsidian.nvim'
  -- AI
  --use 'github/copilot.vim'
  use 'zbirenbaum/copilot.lua'
  -- platform.io
  use 'normen/vim-pio'
  -- quickfix
  use 'stefandtw/quickfix-reflector.vim'
  -- Automatically set up your configuration after cloning packer.nvim
  -- Put this at the end after all plugins
  if PACKER_BOOTSTRAP then
    require('packer').sync()
  end
end)

