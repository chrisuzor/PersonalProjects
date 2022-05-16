def is_palindrome(value):
    value = value.replace(" ", "").lower()
    split = len(value) // 2

    if len(value) % 2 == 0:
        left = value[:split]
        right = value[split:]
    else:
        left = value[:split]
        right = value[split + 1 :]

    return left == right[::-1]
