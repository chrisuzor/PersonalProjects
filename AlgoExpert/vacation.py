def solution(A):
    unique_visits = {val: 1 for val in set(A)}
    len_of_unique_locations = len(unique_visits)
    current_index = min_visits = max_visits = 0
    for current_j, num in enumerate(A, 1):
        if unique_visits[num] > 0:
            len_of_unique_locations -= 1
        unique_visits[num] -= 1
        if not len_of_unique_locations:
            print(unique_visits)
            while current_index < current_j and unique_visits[A[current_index]] < 0:
                unique_visits[A[current_index]] += 1
                print(unique_visits)
                print("reduce ", A[current_index])
                current_index += 1
                print("Current index ", current_index)
            if not max_visits or current_j - current_index <= max_visits - min_visits:
                min_visits, max_visits = current_index, current_j
                print("Max and Min Visits are {} and {}".format(max_visits, min_visits))
                print(unique_visits)
    return max_visits - min_visits


# print(solution([7,3,7,3,1,3,4,1]))
print(solution([2, 1, 1, 3, 2, 1, 1, 3]))
# print(solution([7,5,2,7,2,7,4,7]))


def solutionB(A):
    set_locations = {val: 1 for val in set(A)}
    len_of_unique_locations = len(set_locations)
    min_window_holder, min_index, max_index = 0
    for max_window_holder, location in enumerate(A, 1):
        pass
