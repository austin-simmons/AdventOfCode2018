#!/usr/bin/env python


def dif_ids(id_1: str, id_2: str):
    diffs = []
    res = []
    for i in range(len(id_1)):
        if id_1[i] != id_2[i]:
            diffs.append(id_1[i])

    if len(diffs) == 1:
        for i in range(len(id_1)):
            if id_1[i] == id_2[i]:
                res.append(id_1[i])

        return ''.join(res)


input_data = []

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

for input_id in input_data:
    for i in range(len(input_data)):
        match = dif_ids(input_id, input_data[i])
        if match:
            print(match)
