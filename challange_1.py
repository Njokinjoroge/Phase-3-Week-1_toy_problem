# n boxes rangen= n arranged in rows
# k-th box contains a[k] bricks
# you can take one brick from some box and move it to a box next to it in left or right 
#  return the minimum number of moves required to end up with exctly 10 brick in every box

# def min_required_moves(N):
#     total_bricks = sum(N)
#     bricks_per_box=total_bricks//len(N)
#     if  total_bricks%len(N) !=0 or bricks_per_box == 0:
#         return -1
#     for i in range(len(N)):

    
import heapq

def min_moves(A):
    n = len(A)
    moves = 0
    pq = []
    for i, bricks in enumerate(A):
        diff = 10 - bricks
        if diff > 0:
            heapq.heappush(pq, (-diff, i))
    while pq:
        diff, i = heapq.heappop(pq)
        diff = -diff
        if i > 0:
            bricks_to_move = min(diff, A[i-1])
            A[i-1] -= bricks_to_move
            A[i] += bricks_to_move
            moves += bricks_to_move
            if A[i-1] > 0:
                heapq.heappush(pq, (-A[i-1], i-1))
            if A[i] < 10:
                heapq.heappush(pq, (A[i], i))
        elif i < n-1:
            bricks_to_move = min(diff, A[i+1])
            A[i+1] -= bricks_to_move
            A[i] += bricks_to_move
            moves += bricks_to_move
            if A[i+1] > 0:
                heapq.heappush(pq, (-A[i+1], i+1))
            if A[i] < 10:
                heapq.heappush(pq, (A[i], i))
    return moves



