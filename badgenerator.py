import os
import re

path = os.getenv("PATH")
patharr = path.split(":")

bins = []

for pathdir in patharr:
    try:
        files = os.listdir(pathdir)
        bins.extend(files)
    except:
        print(f"messed up on: {pathdir}")

bins = list(filter(lambda x: x != "alias" and x != "echo", bins))

# add some builtins
bins.append("exit")
bins.append("source")

# re-add echo and alias at the end
#bins.append("echo")
bins.append("alias")

pattern = re.compile("^[a-zA-Z-]*$")
with open("badrc", "w") as f:
    for bin in bins:
        if pattern.match(bin):
            f.write(f'\nalias {bin}="echo no"')
