% ---------- head ----------
head_pred(valid_sudoku,1).

% ---------- body predicates ----------
body_pred(valid_piece,1).
body_pred(get_row,3).
body_pred(get_col,3).
body_pred(get_block,3).

% ---------- types ----------
type(row, list(int)).
type(col, list(int)).
type(block, list(int)). 
type(sudoku, (
    row, row, row, row, row, row, row, row, row,
    col, col, col, col, col, col, col, col, col,
    block, block, block, block, block, block, block, block, block
)).
type(valid_piece,(list(int))).
type(valid_sudoku,(sudoku)).
type(get_row,(idx,sudoku,row)).
type(get_col,(idx,sudoku,col)).
type(get_block,(idx,sudoku,block)).


% ---------- predicate invention ----------
max_inv_preds(1000).
max_inv_bodies(1000).
