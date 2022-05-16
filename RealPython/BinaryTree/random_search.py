from random import randint


def find(items, search_val):
    while True:
        rand_dex = randint(0, len(items) - 1)
        rand_el = items[rand_dex]
        if rand_el == search_val:
            return rand_dex
