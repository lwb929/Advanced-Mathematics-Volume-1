#!/usr/bin/env python3
"""Canvas 路径前缀修复：当本文件夹被放入现有 Obsidian 库的子目录时，
canvas 的 file 路径（库根相对路径）会失效。运行本脚本输入子目录前缀即可修复。
用法：python3 fix_canvas_prefix.py [子目录前缀]
例：库根/Vault/Docs/高等数学-同济八版上册/ 时，前缀 = Docs/高等数学-同济八版上册
"""
import json, sys, glob, os

prefix = sys.argv[1].strip("/") if len(sys.argv) > 1 else ""
here = os.path.dirname(os.path.abspath(__file__))
for c in glob.glob(here + "/*.canvas"):
    d = json.load(open(c))
    n = 0
    for node in d.get("nodes", []):
        if node.get("type") == "file" and prefix and not node["file"].startswith(prefix + "/"):
            node["file"] = prefix + "/" + node["file"]
            n += 1
    json.dump(d, open(c, "w"), ensure_ascii=False, indent=1)
    print(f"{os.path.basename(c)}: {n} file-paths -> {'(root)' if not prefix else prefix}")
