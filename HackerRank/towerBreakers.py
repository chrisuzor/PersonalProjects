def towerBreakers(n, m):
    player_turn = "player1"
    tower_arrays = [m for _ in range(n)]

    if m == 1:
        return 2
    if n == 1:
        return 1
    nm = n * m
    if nm % 2 == 1:
        return 1
    else:
        return 2

    # if n == 1:
    #     return 1
    # elif m
    #
    # while max(tower_arrays) > 1:
    #     if player_turn == 'player1':
    #         player_turn = 'player2'
    #     else:
    #         player_turn = 'player1'
    #
    #     if n == 1:
    #         return 1
    #
    #     current_tower_in_play = max(tower_arrays)
    #     tower_removed = current_tower_in_play // 2
    #     position_of_current_tower = tower_arrays.index(current_tower_in_play)
    #     remaining_tower = current_tower_in_play - tower_removed
    #     tower_arrays[position_of_current_tower] = remaining_tower
    # return 2 if player_turn == 'player1' else 1


print(towerBreakers(386823, 517868))
print(towerBreakers(924902, 837899))
