% ---------- head ----------
head_pred(valid_sudoku,1).

% ---------- body predicates ----------
body_pred(valid_piece,1).
body_pred(get_row,3).    % get_row(+Index, +Sudoku, -Row)
body_pred(get_col,3).    % get_col(+Index, +Sudoku, -Col)
body_pred(get_block,3).  % get_block(+Index, +Sudoku, -Block)

% ---------- types ----------
type(valid_piece,(list,)).
type(valid_sudoku,(sudoku,)).
type(get_row,(int,sudoku,list)).
type(get_col,(int,sudoku,list)).
type(get_block,(int,sudoku,list)).

% ---------- allow predicate invention ----------
max_inv_preds(1000).
max_inv_bodies(1000).
