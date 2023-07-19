import os
import re

path = os.getenv("PATH")
patharr = path.split(":")

bins = []
filter_relative_list = [
    "alias",
    "echo",
]

filter_absolute_list = [
    "starship"
]

for pathdir in patharr:
    try:
        files = os.listdir(pathdir)
        for file in files:
            if file not in filter_relative_list:
                bins.append(file)
            if file not in filter_absolute_list:
                bins.append(f"{pathdir}/{file}")
    except:
        print(f"messed up on: {pathdir}")

# add some builtins
bins.append("exit")
bins.append("source")

# prevent using absolute paths
bins.append("/")
# re-add echo and alias at the end
#bins.append("echo")
bins.append("alias")

pattern = re.compile("^[a-zA-Z-\/]*$")
with open("badrc", "w") as f:
    for bin in bins:
        if pattern.match(bin):
            f.write(f'\nalias {bin}="echo no"')
