import modshim

# Register the virtual merged module immediately upon import
modshim.shim(
    lower="unyt",                    # 1. The original base package
    upper="dipro_unyt.extension", # 2. Your custom modifications file
    mount="unyt"          # 3. Mounts the result to this package name
)