% =========================
% bias.pl (Corrected for Recursion/Invention)
% =========================

head_pred(valid_sudoku,1).

body_pred(rows,2).
body_pred(cols,2).
body_pred(blocks,2).
body_pred(valid_piece,1).
body_pred(head,2).
body_pred(tail,2).
body_pred(empty,1).

% Types
type(valid_sudoku,(sudoku,)).
type(rows,(sudoku,pieces)).
type(cols,(sudoku,pieces)).
type(blocks,(sudoku,pieces)).
type(valid_piece,(piece,)).
type(head,(pieces,piece)).
type(tail,(pieces,pieces)).
type(empty,(pieces,)).

direction(valid_sudoku,(in,)).
direction(rows,(in,out)).
direction(cols,(in,out)).
direction(blocks,(in,out)).
direction(valid_piece,(in,)).
direction(head,(in,out)).
direction(tail,(in,out)).
direction(empty,(in,)).

% CRITICAL FIX: Explicit Recalls
% Without these, Popper prunes the solution because it assumes recall=1.
recall(rows, 2, 1).
recall(cols, 2, 1).
recall(blocks, 2, 1).
recall(head, 2, 1).
recall(tail, 2, 1).
recall(valid_piece, 1, 1).
recall(empty, 1, 1).

% Enable invention (Use 'enable_invention' to be safe)
enable_invention.
enable_recursion.

% Limits
% The solution size is roughly 14 literals.
% Main: valid(S) :- rows(S,R), inv1(R), cols(S,C), inv1(C), blocks(S,B), inv1(B). (7 lits)
% Rec:  inv1(L)  :- head(L,H), valid_piece(H), tail(L,T), inv1(T). (5 lits)
% Base: inv1(L)  :- empty(L). (2 lits)
max_clauses(3).
max_body(14).
max_vars(20).
max_size(16).