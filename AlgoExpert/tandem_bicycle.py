def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest is True:
        redShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    total_speed = 0
    for i in range(0, len(blueShirtSpeeds)):
        total_speed += max(blueShirtSpeeds[i], redShirtSpeeds[i])
    return total_speed


print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))
