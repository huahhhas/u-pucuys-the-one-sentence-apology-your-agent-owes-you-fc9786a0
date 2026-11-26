#!/usr/bin/env python3
# Entry for make.fun bounty u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0
"""The One-Sentence Apology Your Agent Owes You.

Deterministic entry: writes exactly one sentence to /output/entry.txt
and prints that same line, nothing else.
"""

import os

LINE = "I'm sorry I spent forty minutes 'fixing' your code and then quietly put it back exactly how you had it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
