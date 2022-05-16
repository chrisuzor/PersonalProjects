def minimunBribes(q):
    bribes_list = [0 for _ in range(0, len(q) + 1)]
    for j in range(0, len(q)):
        if q == sorted(q):
            break
        for i in range(0, len(q)):
            if i + 1 == len(q):
                break
            if q[i] > q[i + 1]:
                temp = q[i]
                q[i] = q[i + 1]
                q[i + 1] = temp
                bribes_list[temp] += 1
    print(q)
    print(bribes_list)
    if max(bribes_list) > 2:
        print("Too chaotic")
    else:
        print(sum(bribes_list))


minimunBribes([1, 2, 3, 5, 4, 6, 7, 8])
print("--------------------------------")
minimunBribes([4, 1, 2, 3])
print("--------------------------------")
minimunBribes([1, 2, 5, 3, 7, 8, 6, 4])
print("--------------------------------")
minimunBribes([2, 5, 1, 3, 4])
print("--------------------------------")
minimunBribes([2, 1, 5, 3, 4])
