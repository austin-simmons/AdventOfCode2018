#!/usr/bin/env python

current_freq = 0
freq_changes = []

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

    for d in input_data:
        freq_changes.append({
            'action': d[0],
            'value': int(d[1:])
        })

for f in freq_changes:
    if f['action'] == '+':
        current_freq += f['value']
    elif f['action'] == '-':
        current_freq -= f['value']

print(current_freq)
