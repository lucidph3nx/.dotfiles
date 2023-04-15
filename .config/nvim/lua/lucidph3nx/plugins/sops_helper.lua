sops_helper = {}

function sops_helper.find_age_key(file_path)
  local lyaml = require('lyaml')
  local rex = require('rex_pcre')
  local path = vim.fn.fnamemodify(file_path, ':h')
  local sops_file = nil

  -- search for .sops.yaml in current and parent directories
  while true do
    sops_file = path .. '/.sops.yaml'
    if vim.fn.filereadable(sops_file) == 1 then
      break
    end
    if path == '/' then -- reached the root directory, stop searching
      sops_file = nil
      break
    end
    path = vim.fn.fnamemodify(path, ':h')
  end

  if sops_file == nil then
    print("Could not find .sops.yaml file")
    return nil -- .sops.yaml not found
  end

  local contents = vim.fn.readfile(sops_file)
  local config, err = lyaml.load(table.concat(contents, "\n"))

  if err then
    print("Error loading .sops.yaml file: " .. err)
    return nil
  end

  if not config or not config.creation_rules then
    print("Invalid .sops.yaml file format")
    return nil
  end

  -- convert system path to project-relative path
  local relative_path = vim.api.nvim_call_function('fnamemodify', { vim.fn.expand(file_path .. ':p'), ':.' })

  -- find the first creation_rule that matches the current file path
  for _, rule in ipairs(config.creation_rules) do
    local match, err = pcall(rex.match, file_path, rule.path_regex)
    if match then
      return rule.age
    elseif err then
      print("Error matching path: " .. err)
    end
  end


  print("No matching rule found in .sops.yaml file")
  return nil -- no matching rule found
end

function sops_helper.decrypt()
  local project_path = vim.fn.fnamemodify(vim.fn.expand('%'), ':.')
  local age_key = sops_helper.find_age_key(project_path)
  if age_key == nil then
    print("Error: age key not found")
    return
  end

  local input_file = vim.fn.expand('%:p')
  local sops_command = 'sops --decrypt --in-place --age="' ..
      age_key .. '" ' .. input_file
  local decrypt_success = vim.fn.system(sops_command)
  if vim.v.shell_error ~= 0 then
    print("Error decrypting file: " .. input_file)
    return
  end

  vim.api.nvim_command('edit') -- reload the buffer to show the decrypted content
end

function sops_helper.encrypt()
  local project_path = vim.fn.fnamemodify(vim.fn.expand('%'), ':.')
  local age_key = sops_helper.find_age_key(project_path)
  if age_key == nil then
    print("Error: age key not found")
    return
  end

  local output_file = vim.fn.expand('%:p')
  local sops_command = 'sops --encrypt --in-place --age="' ..
      age_key .. '" ' .. output_file
  local encrypt_success = vim.fn.system(sops_command)
  if vim.v.shell_error ~= 0 then
    print("Error encrypting file: " .. output_file)
    return
  end

  vim.api.nvim_command('edit') -- reload the buffer to show the encrypted content
end

_G.sops_helper = sops_helper
