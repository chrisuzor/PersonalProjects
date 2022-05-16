def classPhotos(redShirtHeights, blueShirtHeights):
    photo_dict = {"blue": 0, "red": 0}
    redShirtHeights.sort()
    blueShirtHeights.sort()
    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] > blueShirtHeights[i]:
            photo_dict["red"] += 1
        elif blueShirtHeights[i] > redShirtHeights[i]:
            photo_dict["blue"] += 1
    for key, value in photo_dict.items():
        if value == len(redShirtHeights):
            return True
    return False


print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
