#!/usr/bin/env python3
import sys
from datetime import datetime, timedelta
from parse import parse

def main():
    sign = None
    date = datetime.now()
    for arg in sys.argv[1:]:

        if sign:
            r = parse("{}:{}:{}", arg)
            delta = timedelta(hours = int(r[0]), minutes = int(r[1]), seconds = int(r[2]))
            if sign == "+":
                date += delta
            else:
                date -= delta
            sign = None

        try:
            date = datetime.fromisoformat(arg)
        except ValueError:
            if arg == "now":
                date = datetime.now()
            elif arg == "+" or arg == "-":
                sign = arg

    print(date)

if __name__ == "__main__":
    main()
