-- General purpose linters
return {
  -- https://github.com/mfussenegger/nvim-lint
  'mfussenegger/nvim-lint',
  event = 'BufWritePost',
  config = function ()
    require('lint').linters_by_ft = {
      python = {
        'flake8',
        'mypy',
        'pylint',
      }
    }

  vim.api.nvim_create_autocmd( { "BufWritePost" }, {
      pattern = { "*.py", },
      callback = function()
        require("lint").try_lint()
      end,
    })
  end
}
