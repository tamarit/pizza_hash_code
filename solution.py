import itertools
import collections


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

sum_till = 0
pos_start_comb = 0
while sum_till < max_slices:
    sum_till += type_pizza[pos_start_comb][1]
    if sum_till < max_slices:
        pos_start_comb += 1


def combinations(l):
    subsets = []
    for L in range(0, len(l)+1):
        for subset in itertools.combinations(l, L):
            subsets.append(list(subset))
    subsets.remove([])
    return subsets


print(type_pizza[:pos_start_comb])
# print(combinations(type_pizza[:pos_start_comb]))
# print(combinations(type_pizza[pos_start_comb:]))

dict_complements = dict()
max_dict_complements = 0
for c in combinations(type_pizza[:pos_start_comb]):
    suma = sum(map(lambda x: x[1], c))
    max_dict_complements = suma if suma > max_dict_complements else max_dict_complements
    print(suma)
    dict_complements[suma] = c

dict_complements = collections.OrderedDict(sorted(dict_complements.items(), reverse=True))
# print(dict_complements)

comb_try = dict()
for c in combinations(type_pizza[pos_start_comb:]):
    suma = sum(map(lambda x: x[1], c))
    if suma <= max_slices:
        comb_try[suma] = c
# comb_try = sorted(comb_try, reverse=True, key=lambda x:x[1])

comb_try = collections.OrderedDict(sorted(comb_try.items(), reverse=True))

current_max = 0
chosen = []
for total in comb_try:
    # print(current_max)
    # print(c)
    if max_dict_complements + total < current_max:
        break
    if total == max_slices:
        current_max = total
        chosen = list(map(lambda x: x[0], c))
        break
    else:
        for k in dict_complements:
            if (total + k) < max_slices:
                current_max = (total + k)
                chosen = list(map(lambda x: x[0], comb_try[total])) + list(map(lambda x: x[0], dict_complements[k]))
                break

chosen = sorted(chosen)
print(current_max)

# permutacions part xicoteta a diccionari de num -> types, e.g. 3 -> 0 + 1
# permutacions de la part major, descartar les que son majors, ordenar de majro a menor la resta, intentar completar amb diccionai de dalt. si trobe numero redo parar. si no seguir fins arribar a un valor que amb el máxim de la primera part no spuerre el maxim que dugem


total_chosen = len(chosen)
content_out = str(total_chosen) + "\n" + " ".join(map(str, chosen))

with open(args.OUTPUT, 'w') as handle:
    handle.write(content_out)
