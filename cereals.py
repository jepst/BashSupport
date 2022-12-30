#!/usr/bin/env python3

import csv
import argparse

def main():
    parser = argparse.ArgumentParser(description='Extract cereals from csv')
    parser.add_argument('file')
    args = parser.parse_args()

    firsts = []
    with open(args.file) as f:
        reader = csv.reader(f)
        for num, row in enumerate(reader):
            if num == 0:
                continue
            if len(row)>0:
                firsts.append(row[0])
    firsts.sort()
    for first in firsts:
        print(first)

main()