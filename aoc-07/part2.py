import re
from pathlib import Path

# file_input = "data-training.txt"
file_input = "data.txt"

TOTAL = 70000000
SPARE = 30000000


cwd = Path("/")
dirtree: dict[Path, int] = {cwd: 0}


def process(cmd: str):
    global cwd
    if cmd.startswith("$"):
        if cmd == "$ ls":
            pass
        elif cmd == "$ cd ..":
            cwd = cwd.parent
        else:  # $ cd dir
            cwd = cwd / cmd[5:]
    elif cmd.startswith("dir"):
        p = cmd[4:]
        dirtree[cwd / p] = 0
    else:
        size = int(cmd.split()[0])
        dirtree[cwd] += size


with open(file_input) as f:
    cmds = [cmd[:-1] for cmd in f]

for cmd in cmds:
    process(cmd)


# trail rest of dirs
for parts in sorted((p.parts for p in dirtree.keys()), reverse=True):
    if len(parts) == 1:
        continue
    p = Path(*parts)
    dirtree[p.parent] += dirtree[p]


free_space = TOTAL - dirtree[Path("/")]
need = SPARE - free_space

res = min(v for v in dirtree.values() if v >= need)

print(res)
