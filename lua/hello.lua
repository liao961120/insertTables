file = io.open("ast.md", "r")
x = file:read("*a")
print(x)
file:close()


local handle = io.popen("pandoc ")
local result = handle:read("*a")
handle:close()
