#!/usr/bin/python3
import sys

argv = sys.argv
argc = len(argv) - 1

if argc == 0:
    print("0 arguments.")
else:
    print(f"{argc} argument{'s' if argc != 1 else ''}:")

    for i in range(1, argc + 1):
        print(f"{i}: {argv[i]}")
