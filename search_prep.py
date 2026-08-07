"""
================================================================================
KMITL Data Structures (01276122) - Offline Terminal Study & Search Tool
--------------------------------------------------------------------------------
Usage:
  python search_prep.py <keyword>
  python search_prep.py <chapter_number> <item_number>

Examples:
  python search_prep.py stack
  python search_prep.py queue
  python search_prep.py 3 2
================================================================================
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def search_files(keyword):
    print(f"\n🔍 Searching for '{keyword}' across solution files...\n" + "="*60)
    found = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for f in sorted(files):
            if f.endswith('.py') and f != 'search_prep.py':
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    if keyword.lower() in content.lower() or keyword.lower() in f.lower():
                        found += 1
                        rel_path = os.path.relpath(path, BASE_DIR)
                        print(f"\n📄 [{found}] {rel_path}\n" + "-"*40)
                        lines = content.split('\n')
                        # Display non-comment code snippet preview
                        code_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')][:12]
                        print("\n".join(code_lines))
                        print("-" * 40)
    print(f"\n✅ Total {found} file(s) matched for '{keyword}'.\n")

def get_item(ch, item):
    ch_num = int(ch)
    item_num = int(item)
    folder_prefix = f"Chapter_{ch_num:02d}"
    print(f"\n📖 Looking for Chapter {ch_num} Item {item_num}...")
    
    for root, dirs, files in os.walk(BASE_DIR):
        if folder_prefix in root or f"Chapter_{ch_num}" in root:
            for f in sorted(files):
                if f.startswith(f"item_{item_num}_"):
                    path = os.path.join(root, f)
                    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                        print("\n" + "="*60 + f"\n📄 File: {f}\n" + "="*60)
                        print(file.read())
                    return
    print("❌ Exercise not found!")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        search_files(sys.argv[1])
    elif len(sys.argv) == 3:
        get_item(sys.argv[1], sys.argv[2])
    else:
        print(__doc__)
