head_pred(valid_sudoku,1).
body_pred(all_rows_valid,1).
body_pred(all_cols_valid,1).
body_pred(all_blocks_valid,1).

type(valid_sudoku,(sudoku,)).
type(all_rows_valid,(sudoku,)).
type(all_cols_valid,(sudoku,)).
type(all_blocks_valid,(sudoku,)).

direction(valid_sudoku,(in,)).
direction(all_rows_valid,(in,)).
direction(all_cols_valid,(in,)).
direction(all_blocks_valid,(in,)).

% Force Popper to see that these only need to be called once
recall(all_rows_valid,1).
recall(all_cols_valid,1).
recall(all_blocks_valid,1).

max_vars(1).
max_body(3).
max_clauses(1).