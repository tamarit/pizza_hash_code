import itertools
import collections
from itertools import islice




import argparse
parser = argparse.ArgumentParser()
parser.add_argument('INPUT')
parser.add_argument('OUTPUT')
args = parser.parse_args()


with open(args.INPUT, 'r') as handle:
    content_in = handle.read()

lines = [l.split() for l in content_in.split("\n")]

max_slices = int(lines[0][0])
max_types = int(lines[0][1])
type_pizza = list(enumerate(map(int, lines[1])))



def combinations_dict(l):
    returned = dict()
    for L in range(0, len(l)+1):
        for subset in itertools.combinations(l, L):
            subset = list(subset)
            # print(subset)
            suma = sum(map(lambda x: x[1], subset))
            returned[suma] = list(subset)
    return returned

def combinations_dict_from_dict(d):
    returned = dict()
    for L in range(0, len(d)+1):
        for subset in itertools.combinations(d, L):
            # suma = sum(map(lambda x: x[0], subset))
            combination = list(set(sum(map(lambda x: x[1], subset), [])))
            suma = sum(map(lambda x: x[1], combination))
            returned[suma] = combination
    return returned

CHUNK_SIZE = 4
type_pizza_chunked = []
i = 0
while i < max_types:
    ni = i + CHUNK_SIZE
    type_pizza_chunked.append(type_pizza[i:ni])
    i = ni

# print(type_pizza_chunked)

total_dict = dict()
for c in type_pizza_chunked:
    total_dict = {**total_dict, **combinations_dict(c)}


new_total_dict = dict()
for k in total_dict:
    if k <= max_slices:
        new_total_dict[k] = total_dict[k]
total_dict = new_total_dict

# if max_slices in total_dict:
#     break
# print(total_dict)
len_prev_total_dict = 0

while (max_slices not in total_dict) and len(total_dict) != len_prev_total_dict:
    # print(total_dict)
    len_prev_total_dict = len(total_dict)
    total_dict_chunked = []
    i = 0
    total_dict.items
    total_dict_items = list(total_dict.items())
    # print(total_dict_items)
    while i < len(total_dict):
        ni = i + CHUNK_SIZE
        # print(total_dict_items[i:ni])
        total_dict_chunked.append(total_dict_items[i:ni])
        i = ni

    # print(total_dict_chunked)

    total_dict = dict()
    for c in total_dict_chunked:
        total_dict = {**total_dict, **combinations_dict_from_dict(c)}

    
    # print(total_dict)
    new_total_dict = dict()
    for k in total_dict:
        if k <= max_slices:
            new_total_dict[k] = total_dict[k]
    total_dict = new_total_dict
    # print(total_dict)
    print(len_prev_total_dict)
    print(len(total_dict))
    # print(total_dict)

print(sorted(total_dict.keys()))
max_k = 0
for k in total_dict:
    if k > max_k:
        max_k = k

print(max_slices)
print(max_k)
print(total_dict[max_k])

content_out = str(len(total_dict[max_k])) + "\n" + " ".join(map(str, sorted(map(lambda x:x[0], total_dict[max_k]))))

with open(args.OUTPUT, 'w') as handle:
    handle.write(content_out)
