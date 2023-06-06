local ap = require("nvim-autopairs")
ap.setup()

-- I dont want to use autopairs for strings
ap.remove_rule('"')
