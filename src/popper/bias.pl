head_pred(valid_sudoku,1).
body_pred(all_blocks_valid,1).
body_pred(all_rows_valid,1).
body_pred(all_cols_valid,1).

% optional but helpful:
type(valid_sudoku,(sudoku,)).
type(all_blocks_valid,(sudoku,)).
type(all_rows_valid,(sudoku,)).
type(all_cols_valid,(sudoku,)).
