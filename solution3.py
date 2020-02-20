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
# type_pizza = list(enumerate(map(int, lines[1])))
type_pizza = list((map(int, lines[1])))

slices = 0
solution = []
for i in reversed(range(max_types)):
    if slices + type_pizza[i] <= max_slices:
        solution.append(i)
        slices += type_pizza[i]

print(max_slices)
print(slices)

content_out = str(len(solution)) + "\n" + " ".join(map(str, solution))

with open(args.OUTPUT, 'w') as handle:
    handle.write(content_out)
