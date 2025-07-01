'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    from_member_following = social_graph[from_member]["following"]
    to_member_following = social_graph[to_member]["following"]

    if to_member in from_member_following and from_member in to_member_following:
        return "friends"
    elif to_member in from_member_following:
        return "follower"
    elif from_member in to_member_following:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    n = len(board)
    none = "NO WINNER"
    for row in board:
        if row[0] != '' and row == [row[0]] * n:
            return row[0]
    for col in range(n):
        column_list = [board[row][col] for row in range(n)]
        if column_list[0] != '' and column_list == [column_list[0]]*n:
            return column_list[0]
    diag_list = [board[i][i] for i in range(n)]
    if diag_list[0] != '' and diag_list == [diag_list[0]]*n:
        return diag_list[0]
    opposite_diag_list = [board[i][n-1-i] for i in range(n)]
    if opposite_diag_list[0] != '' and opposite_diag_list == [opposite_diag_list[0]] * n:
        return opposite_diag_list[0]
    return none


def eta(first_stop, second_stop, route_map):
    total_time=0
    now = first_stop
    while now != second_stop:
        for(start, end), leg_info in route_map.items():
            if start == now:
                total_time += leg_info["travel_time_mins"]
                now=end
                break
    return total_time

legs1 = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
print(eta("b1","a1",legs2))