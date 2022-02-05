import itertools as it

all_ones = it.repeat(1)

print(next(all_ones))

all_ones = it.repeat(1, times=5)

friends = ['Chris', 'Joe', 'Psalm', 'Mike']

print(list(it.permutations(friends, r=3)))