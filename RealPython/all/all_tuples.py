import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


numbers = [2, 3, 5, 7, 11]
all([is_prime(x) for x in numbers])
all(is_prime(x) for x in numbers)


x = 42

validation_conditions = (
<<<<<<< HEAD
    isinstance(x, int),
    0 <= x <= 100,
    x % 2 == 0,
=======
     isinstance(x, int),
     0 <= x <= 100,
     x % 2 == 0,
>>>>>>> 94a81eb432a52582e503668e85b4cc9249584108
)

if all(validation_conditions):
    print("Valid input")
else:
    print("Invalid input")


numbers = [10, 5, 6, 4, 7, 8, 20]
# Greater than 0
all(x > 0 for x in numbers)
# From 0 to 20 (Both included)
all(0 <= x <= 20 for x in numbers)
# From 0 to 20 (integers only)
all(x in range(21) for x in numbers)


numbers = ["1", "2", "3.0"]
all(number.isdecimal() for number in numbers)


<<<<<<< HEAD
raw_data = [
    ["name", "job", "email"],
    ["Linda", "Technical Lead", ""],
    ["Joe", "Senior Web Developer", "joe@example.com"],
    ["Lara", "Project Manager", "lara@example.com"],
    ["David", "", "david@example.com"],
    ["Jane", "Senior Python Developer", "jane@example.com"],
]

clean_data = list(filter(all, raw_data))

clean_data_ = [row for row in raw_data if all(row)]
=======
raw_data = [['name', 'job', 'email'],
 ['Linda', 'Technical Lead', ''],
 ['Joe', 'Senior Web Developer', 'joe@example.com'],
 ['Lara', 'Project Manager', 'lara@example.com'],
 ['David', '', 'david@example.com'],
 ['Jane', 'Senior Python Developer', 'jane@example.com']]

clean_data = list(filter(all, raw_data))

clean_data_ = [row for row in raw_data if all(row)]
>>>>>>> 94a81eb432a52582e503668e85b4cc9249584108
