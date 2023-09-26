import re
import toml

# Define the paths to the files
init_file_path = "src/ucyph/__init__.py"
pyproject_file_path = "pyproject.toml"

# Read the current version from __init__.py
with open(init_file_path, "r") as init_file:
    init_content = init_file.read()
    version = re.search(r'__version__ = "(.*?)"', init_content).group(1)

# Increment the version
version_parts = version.split(".")
version_parts[-1] = str(int(version_parts[-1]) + 1)
new_version = ".".join(version_parts)

# Write the new version back to __init__.py
with open(init_file_path, "w") as init_file:
    init_file.write(f'__version__ = "{new_version}"\n')

# Update the version in pyproject.toml
with open(pyproject_file_path, "r") as pyproject_file:
    pyproject_content = toml.load(pyproject_file)

pyproject_content["project"]["version"] = new_version

with open(pyproject_file_path, "w") as pyproject_file:
    toml.dump(pyproject_content, pyproject_file)
