-- a function to construct opts for keymaps
_G.make_opts = function(desc, local_opts)
  local merged_opts = {}
  if local_opts then
    for k, v in pairs(local_opts) do
      merged_opts[k] = v
    end
  end
  merged_opts.desc = desc
  return merged_opts
end
