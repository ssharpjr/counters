#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4

import sys
from random import randrange
from time import sleep


if len(sys.argv) < 4:
    print("Usage: " + sys.argv[0] + " generator type (bin or hex), number of iterations, pause timer")
    print("Example: 'python3 " + sys.argv[0] + " bin 100 1'")
    print("This will run 100 binary generations with a 1 second pause between runs.")
    sys.exit(2)


generator_type = str(sys.argv[1])
iterations = int(sys.argv[2])
sleep_timer = float(sys.argv[3])


def generate_8bit_bin_number():
    r_num = randrange(255)
    b_num = format(r_num, '08b')
    return b_num


def generate_8bit_hex_number():
    r_num = randrange(4294967295)
    h_num = format(r_num, '08X')
    return h_num


def generate_random_number_list(gen_type, number):
    if gen_type == 'bin':
        rng = generate_8bit_bin_number()
    if gen_type == 'hex':
        rng = generate_8bit_hex_number()
    rnd_num_list = []
    for i in range(number):
        rnd_num = rng
        rnd_num_list.append(rnd_num)
    return rnd_num_list


def print_rnd_bin_list(gen_type, number, timer=None):
    counter = 0
    try:
        for i in range(number):
            rnd_list = generate_random_number_list(gen_type, 8)
            print(rnd_list[0], rnd_list[1], rnd_list[2], rnd_list[3],
                  rnd_list[4], rnd_list[5], rnd_list[6], rnd_list[7])
            counter += 1
            if timer:
                sleep(timer)
    except KeyboardInterrupt:
        print("\nNot complete.")
    finally:
        print("\n{:,} iterations".format(counter))
        print()


# sleep_timer = 0
print_rnd_bin_list(generator_type, iterations, sleep_timer)
