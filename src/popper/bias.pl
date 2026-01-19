% ---------- head ----------
head_pred(valid_sudoku,1).

% ---------- body predicates ----------
body_pred(valid_piece,1).
body_pred(get_row,3).
body_pred(get_col,3).
body_pred(get_block,3).
body_pred(idx,1).

% ---------- types ----------
type(idx, int).

type(sudoku, tuple(
    row,row,row,row,row,row,row,row,row,
    col,col,col,col,col,col,col,col,col,
    block,block,block,block,block,block,block,block,block
)).

type(valid_piece, piece).
type(piece, row).
type(piece, col).
type(piece, block).

type(valid_sudoku, sudoku).
type(get_row, (idx, sudoku, row)).
type(get_col, (idx, sudoku, col)).
type(get_block, (idx, sudoku, block)).

% ---------- limits ----------
max_vars(9).
max_body(9).
