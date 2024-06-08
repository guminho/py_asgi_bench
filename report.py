# tqdm==4.66.4
from tqdm import tqdm

with open("report.txt") as f:
    lines = f.read()
lines = lines.splitlines()
lines = [line.split(":") for line in lines]

fwks = [(x, float(y)) for x, y in lines]
fwks = sorted(fwks, key=lambda x: x[1], reverse=True)
print(fwks)

total = 100
ncols = 50
bar_format = "{desc:10}:{postfix:6}|{bar}| {n_fmt}/{total_fmt}"
COEF = fwks[0][1] / total

for fwk in fwks:
    with tqdm(
        total=total,
        ncols=ncols,
        bar_format=bar_format,
        ascii=True,
        desc=fwk[0],
        postfix=int(fwk[1]),
    ) as pbar:
        pbar.update(int(fwk[1] / COEF))
