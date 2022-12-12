return require('packer').startup(function(use)
        use 'wbthomason/packer.nvim'
        use 'navarasu/onedark.nvim'
        use 'kyazdani42/nvim-web-devicons'
        use 'kyazdani42/nvim-tree.lua'
        use 'neovim/nvim-lspconfig'
-- couldnt figure out how to get this one working, check later after lsp and uatocomplete is set up        
--        use 'windwp/nvim-autopairs'
        use 'ThePrimeagen/vim-be-good'
end)

