% bias.pl

% 1. Predicate Declarations
head_pred(valid_sudoku, 1).
body_pred(rows, 2).
body_pred(cols, 2).
body_pred(blocks, 2).
body_pred(all_pieces_valid, 1).

% 2. Types/Directions
direction(valid_sudoku, (in,)).
direction(rows, (in, out)).
direction(cols, (in, out)).
direction(blocks, (in, out)).
direction(all_pieces_valid, (in,)).

% 3. Recalls (The Fix)
% We explicitly set these high. 
% If your Popper version ignores these, we will try a workaround below.
recall(rows, 2, 1).
recall(cols, 2, 1).
recall(blocks, 2, 1).
recall(all_pieces_valid, 1, 4).  % Allow 4 calls just to be safe

% 4. Search Constraints
% Relax these significantly to ensure we don't accidentally prune the solution.
max_vars(6).
max_body(7).
max_clauses(1).