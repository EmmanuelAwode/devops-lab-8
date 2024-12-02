def solve_sudoku(board):
    # Input validation: Ensure it's a 9x9 grid
    if not isinstance(board, list) or len(board) != 9 or not all(isinstance(row, list) and len(row) == 9 for row in board):
        raise TypeError("Invalid board format. Must be a 9x9 list of lists.")

    def is_valid(num, row, col):
        # Check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        # Check 3x3 subgrid
        sub_row, sub_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(sub_row, sub_row + 3):
            for j in range(sub_col, sub_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def is_board_valid():
        # Check for duplicates in rows, columns, and subgrids
        for i in range(9):
            row_numbers = [num for num in board[i] if num != 0]
            if len(row_numbers) != len(set(row_numbers)):
                return False
            col_numbers = [board[j][i] for j in range(9) if board[j][i] != 0]
            if len(col_numbers) != len(set(col_numbers)):
                return False
        for sub_row in range(0, 9, 3):
            for sub_col in range(0, 9, 3):
                subgrid = [
                    board[i][j]
                    for i in range(sub_row, sub_row + 3)
                    for j in range(sub_col, sub_col + 3)
                    if board[i][j] != 0
                ]
                if len(subgrid) != len(set(subgrid)):
                    return False
        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(num, i, j):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = 0
                    return False
        return True

    # Validate the initial board
    if not is_board_valid():
        return None

    # Start solving the board
    if not backtrack():
        return None
    return board
