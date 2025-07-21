# Imagine this is your main app:
plugin_names = ["plugin_a", "plugin_b"]  # could come from config or folder scan

for name in plugin_names:
    plugin = __import__(name)
    plugin.run()  # assuming every plugin has a run() function

"""
get only specific vars, functions, etc
"""
module = __import__(module_name, fromlist=[func_name])
    func = getattr(module, func_name)