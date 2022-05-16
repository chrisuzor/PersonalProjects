import bisect

fruits = ["apple", "banana", "banana", "orange", "pineapple"]

print(bisect.bisect(fruits, "banana"))

print(bisect.bisect_left(fruits, "banana"))


# where can i put something that would maintain the order

bisect.insort_left(fruits, "kiwi")

print(fruits)
