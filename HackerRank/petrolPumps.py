def truckTour(petrolpumps):
    # Write your code here
    total_distance = len(petrolpumps)
    for i in range(0, total_distance):
        amount_of_petrol = petrolpumps[i][0]
        distance_to_travel = petrolpumps[i][1]
        distance_cover = amount_of_petrol - distance_to_travel
        print(
            "Amount of Petrol is {} and disance to travel is {}".format(
                amount_of_petrol, distance_to_travel
            )
        )
        print("Distance cover is {}".format(distance_cover))
        if distance_cover < 0:
            continue
        print("Passed I")
        for j in range(i + 1, total_distance):
            print("Enter J")
            if distance_cover < 0:
                continue
            distance_cover_j = petrolpumps[j][0] - petrolpumps[j][1]
            distance_cover += distance_cover_j
            print(distance_cover)
        for k in range(((total_distance - 1) - (total_distance - i)), -1, -1):
            print("Enter k")
            if distance_cover < 0:
                continue
            print(distance_cover)
            distance_cover_k = petrolpumps[k][0] - petrolpumps[k][1]
            distance_cover += distance_cover_k

        if distance_cover > 0:
            print("Final Lap is remaining {}".format(distance_cover))
            return i


print(truckTour([[1, 5], [10, 3], [3, 4]]))
