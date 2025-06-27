import random

def create_chessBoard():
    return [random.randint(0,7) for _ in range(8)]    

def print_board(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if board[col] == row:
                line+=" Q "
            else:
                line+=" . "
        print(line)
    print()

def count_conflicts(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                conflicts+=1
    return conflicts

def get_neighbors(board):
    neighbors = []
    for col in range(len(board)):
        for row in range(8):
            if board[col]!= row:
                neighbor = board[:]
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(show_steps=False):
    current_board = create_chessBoard()
    current_conflicts = count_conflicts(current_board)

    step =0
    if show_steps:
        print(f"Step {step}: Board = {current_board}, Conflicts = {current_conflicts}")
        print_board(current_board)

    while True:
        neighbors = get_neighbors(current_board)
        best_neighbor = min(neighbors,key= count_conflicts)
        best_neighbor_conflicts = count_conflicts(best_neighbor)

        if best_neighbor_conflicts >= current_conflicts:
            return current_board, current_conflicts
        
        current_board = best_neighbor
        current_conflicts = best_neighbor_conflicts
        step+=1

        if show_steps:
            print(f"Step {step}: Board = {current_board}, Conflicts = {current_conflicts}")
            print_board(current_board)

def random_hill_climbing(max_restart = 100, show_steps = False):
    for restart in range(max_restart):
        if show_steps:
            print(f"Restart {restart+1}: ")
        solution, conflicts = hill_climbing(show_steps=show_steps)
        
        if conflicts == 0:
            return solution,conflicts
    return None,-1

solution, conflicts = random_hill_climbing(show_steps=True)

if conflicts == 0: 
    print(f"\n Conflict count: {conflicts}, Solution Found!")
    print("Board: ", solution)
    print("Conflicts: ", conflicts)
    print_board(solution)
else: 
    print("\nNo solution found even after multiple restart!")








