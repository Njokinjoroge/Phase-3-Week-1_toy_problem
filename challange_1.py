# n boxes rangen= n arranged in rows
# k-th box contains a[k] bricks
# you can take one brick from some box and move it to a box next to it in left or right 
#  return the minimum number of moves required to end up with exctly 10 brick in every box

def min_required_moves(N):
    total_bricks = sum(N)
    bricks_per_box=total_bricks//len(N)
    if  total_bricks%len(N) or bricks_per_box == 0:
        return -1

    moves = total_bricks - len(N)*bricks_per_box
    for box in N:
        moves += max(box-bricks_per_box, 0)

    return moves //2   




