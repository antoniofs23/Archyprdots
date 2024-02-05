return {
  'mfussernegger/nvim-dap-python',
  ft = 'python',
  dependencies = {
    'mfussernegger/nvim-dap',
  },
  config = function ()
    require('dap-python').setup('/home/ant/miniforge3/bin/python3')
  end
}
