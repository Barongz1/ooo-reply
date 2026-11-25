"""Funniest One-Line Out-of-Office Reply — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The reply: I am out of office, and so is my patience.
TEXT = "I am out of office and so is my patience. Please email again after the weekend, when I will pretend I missed this."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
