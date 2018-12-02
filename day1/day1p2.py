#!/usr/bin/env python

done = False
current_freq = 0
freq_changes = []
count_dict = {}

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

    for d in input_data:
        freq_changes.append({
            'action': d[0],
            'value': int(d[1:])
        })

while not done:
    for f in freq_changes:
        if f['action'] == '+':
            current_freq += f['value']
        elif f['action'] == '-':
            current_freq -= f['value']

        try:
            count_dict[str(current_freq)] += 1
        except KeyError:
            count_dict[str(current_freq)] = 1

        if count_dict[str(current_freq)] == 2:
            print(current_freq)
            done = True
            break
