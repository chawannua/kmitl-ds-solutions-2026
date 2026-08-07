"""
================================================================================
KMITL Data Structures (01276122) - Offline Study & Solution Search Tool
================================================================================
Usage:
  python search_prep.py <keyword>
  python search_prep.py <chapter_number> <item_number>

Examples:
  python search_prep.py stack
  python search_prep.py "linked list"
  python search_prep.py 3 1
  python search_prep.py 5 2
================================================================================
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def print_help():
    print("""
================================================================================
 KMITL Data Structures Solutions - Search & Study Helper (search_prep.py)
================================================================================

USAGE:
  1. Search solutions by keyword:
     python search_prep.py <keyword>
     Example: python search_prep.py stack
              python search_prep.py recursion
              python search_prep.py Parentheses

  2. Direct item view (Chapter & Item):
     python search_prep.py <chapter_number> <item_number>
     Example: python search_prep.py 1 1     (Chapter 1, Item 1)
              python search_prep.py 3 2     (Chapter 3, Item 2)
              python search_prep.py 5 4     (Chapter 5, Item 4)

AVAILABLE CHAPTERS:
  Chapter 1 : Python 1 (Rabbit/Turtle, Multi-sum, Digit sum, Function, Vickrey Auction)
  Chapter 2 : Python 2 (Roman Number, Spherical, New Range, 3 SUM, funString)
  Chapter 3 : Stack (Parentheses v1, Parenthesis Matching, Infix to Postfix, Stack Calc, Parking Lot)
  Chapter 4 : Queue (Basic Queue, Queue 2, Concept Queue, Cafe, Search Portal)
  Chapter 5 : Linked List (Singly List, Doubly List, Merge Order, VIM Editor, Radix Sort)
  Chapter 6 : Recursion (Fibonacci, String Length, GCD, Tower of Hanoi, Draw Stair)
================================================================================
""")


def search_files(keyword):
    kw = keyword.lower()
    print(f"\n" + "=" * 70)
    print(f" 🔍 SEARCH RESULTS FOR: '{keyword}'")
    print("=" * 70)

    total_files_matched = 0
    total_lines_matched = 0

    solution_files = []
    for root, dirs, files in sorted(os.walk(BASE_DIR)):
        dirs.sort()
        for f in sorted(files):
            if f.endswith('.py') and f != 'search_prep.py':
                solution_files.append(os.path.join(root, f))

    for path in solution_files:
        rel_path = os.path.relpath(path, BASE_DIR)
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
        except Exception:
            continue

        filename_match = kw in os.path.basename(path).lower()
        matching_lines = []

        for idx, line in enumerate(lines, start=1):
            if kw in line.lower():
                matching_lines.append((idx, line.rstrip('\r\n')))

        if filename_match or matching_lines:
            total_files_matched += 1
            total_lines_matched += len(matching_lines)

            print(f"\n📄 File: {rel_path}")
            print("-" * 70)

            if matching_lines:
                for line_num, line_content in matching_lines:
                    print(f"  Line {line_num:4d} | {line_content}")
            elif filename_match:
                print("  [Filename matched keyword]")
                preview_count = 0
                for line_num, line_content in enumerate(lines, start=1):
                    if line_content.strip():
                        print(f"  Line {line_num:4d} | {line_content.rstrip()}")
                        preview_count += 1
                        if preview_count >= 5:
                            break

            print("-" * 70)

    print(f"\n✅ Summary: Found {total_files_matched} matching file(s) and {total_lines_matched} matching line(s).\n")


def get_item(ch_arg, item_arg):
    try:
        ch_num = int(ch_arg)
        item_num = int(item_arg)
    except ValueError:
        print(f"❌ Invalid chapter or item number: '{ch_arg}', '{item_arg}'. Must be numbers.")
        return

    target_dir = None
    for item in sorted(os.listdir(BASE_DIR)):
        item_path = os.path.join(BASE_DIR, item)
        if os.path.isdir(item_path) and item.startswith("Chapter_"):
            parts = item.split('_')
            if len(parts) >= 2 and parts[1].isdigit():
                if int(parts[1]) == ch_num:
                    target_dir = item_path
                    break

    if not target_dir:
        print(f"\n❌ Chapter {ch_num} directory not found.")
        print("Available chapters are 1 through 6.\n")
        return

    target_file = None
    for f in sorted(os.listdir(target_dir)):
        if f.endswith('.py'):
            parts = f.split('_')
            if len(parts) >= 2 and parts[0] == 'item' and parts[1].isdigit():
                if int(parts[1]) == item_num:
                    target_file = os.path.join(target_dir, f)
                    break

    if not target_file:
        print(f"\n❌ Chapter {ch_num} Item {item_num} solution file not found in {os.path.basename(target_dir)}.")
        available_items = []
        for f in sorted(os.listdir(target_dir)):
            if f.endswith('.py'):
                parts = f.split('_')
                if len(parts) >= 2 and parts[0] == 'item' and parts[1].isdigit():
                    available_items.append(parts[1])
        if available_items:
            print(f"Available items in Chapter {ch_num}: {', '.join(available_items)}\n")
        return

    rel_path = os.path.relpath(target_file, BASE_DIR)
    print("\n" + "=" * 80)
    print(f" 📖 SOLUTION CODE & EXPLANATION: Chapter {ch_num} - Item {item_num}")
    print(f" 📄 Path: {rel_path}")
    print("=" * 80 + "\n")

    try:
        with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            print(content)
    except Exception as e:
        print(f"❌ Error reading file: {e}")

    print("\n" + "=" * 80 + "\n")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in ("-h", "--help", "help"):
        print_help()
    elif len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        get_item(sys.argv[1], sys.argv[2])
    else:
        keyword = " ".join(sys.argv[1:])
        search_files(keyword)


if __name__ == "__main__":
    main()
