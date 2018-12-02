#!/usr/bin/env python
from collections import defaultdict

id_data = []
check_data = {
    'twos': 0,
    'threes': 0
}

with open('input.txt', 'r') as f:
    id_data = f.read().splitlines()

for i in id_data:
    count = defaultdict(int)
    is_two = False
    is_three = False

    for char in i:
        count[char] += 1

    for _, v in count.items():
        if v == 2:
            is_two = True
        if v == 3:
            is_three = True

    if is_two:
        check_data['twos'] += 1
    if is_three:
        check_data['threes'] += 1

    is_two = False
    is_three = False

check = check_data['twos'] * check_data['threes']

print(check)
