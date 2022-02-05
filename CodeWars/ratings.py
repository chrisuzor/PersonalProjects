def countDecreasingRatings(ratings):
    ratings_dict = {}
    counter = 1
    for i in range(len(ratings)):
        if i == 0:
            ratings_dict[1] = 1
        if i > 0:
            ratings_dict[1] += 1
            if ratings[i] - ratings[i - 1] == -1:
                counter += 1
                for j in range(2, counter):
                    ratings_dict[j] += 1
                if counter in ratings_dict:
                    ratings_dict[counter] += 1
                else:
                    ratings_dict[counter] = 1
            else:
                counter = 1
    return sum(ratings_dict.values())


print(countDecreasingRatings([4,3,5,4,3]))
print(countDecreasingRatings([4,2,3,1]))
print(countDecreasingRatings([2,1,3]))
