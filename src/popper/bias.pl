% ---------- head ----------
head_pred(valid_sudoku,1).

% ---------- body predicates ----------
body_pred(valid_piece,1).
body_pred(get_row,3).
body_pred(get_col,3).
body_pred(get_block,3).

% ---------- types ----------
type(valid_piece,(list_t)).
type(valid_sudoku,(sudoku)).
type(get_row,(int,sudoku,list_t)).
type(get_col,(int,sudoku,list_t)).
type(get_block,(int,sudoku,list_t)).


% ---------- predicate invention ----------
max_inv_preds(1000).
max_inv_bodies(1000).
