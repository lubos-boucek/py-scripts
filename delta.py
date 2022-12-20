#!/usr/bin/env python3
import sys
from datetime import datetime, timedelta
from parse import parse
from enum import Enum

Type = Enum("Type", ["DATETIME", "SIGN", "DELTA"])

def print_error(*messages):
    print(*messages, file = sys.stderr)
    exit(1)

def process_delta(arg):
    # r = parse("{:tt}", arg)
    r = parse("{:d}:{:d}:{:d}", arg)

    if not r:
        print_error("An error occurred while parsing the delta, which should be specified as \"H:M:S\".")

    return timedelta(hours = int(r[0]), minutes = int(r[1]), seconds = int(r[2]))

def main():
    dt = None
    last = None

    for arg in sys.argv[1:]:
        try:
            new_dt = datetime.fromisoformat(arg)
            if dt:
                print(dt)
            dt = new_dt
            current = Type.DATETIME
        except ValueError:
            if arg == "now":
                if dt:
                    print(dt)
                dt = datetime.now()
                current = Type.DATETIME
            elif arg == "+" or arg == "-":
                sign = arg
                current = Type.SIGN
            else:
                delta = process_delta(arg)
                current = Type.DELTA

        if current == Type.DELTA and not last == Type.SIGN or \
        last == Type.SIGN and not current == Type.DELTA or \
        not last and not current == Type.DATETIME:
            print_error("Nonsensical order of arguments.")

        if (current == Type.DELTA):
            if sign == "+":
                dt += delta
            elif sign == "-":
                dt -= delta
        
        last = current

    if dt:
        print(dt)

if __name__ == "__main__":
    main()
