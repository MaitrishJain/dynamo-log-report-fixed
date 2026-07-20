import json
import re
from collections import Counter

paths, ips, total = Counter(), set(), 0
with open("/app/access.log", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"[A-Z]+ (\S+) HTTP/\d(?:\.\d)?"', line)
        if m:
            paths[m.group(1)] += 1

with open("/app/report.json", "w", encoding="utf-8") as out:
    json.dump(
        {
            "total_requests": total,
            "unique_ips": len(ips),
            "top_path": paths.most_common(1)[0][0],
        },
        out,
        indent=2,
        sort_keys=True,
    )
print("wrote /app/report.json")
