#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4

# Binary Counter

import itertools

counter = 0

try:
    for i in itertools.product([0, 1], repeat=24):
        # print(i, "\r", end='')
        print(i)
        counter += 1

except KeyboardInterrupt:
    print("\nNot complete\n")

finally:
    print("\n{:,} iterations".format(counter))
