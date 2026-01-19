all_rows_valid(S) :-
    get_row(1,S,R1), valid_piece(R1),
    get_row(2,S,R2), valid_piece(R2),
    get_row(3,S,R3), valid_piece(R3),
    get_row(4,S,R4), valid_piece(R4),
    get_row(5,S,R5), valid_piece(R5),
    get_row(6,S,R6), valid_piece(R6),
    get_row(7,S,R7), valid_piece(R7),
    get_row(8,S,R8), valid_piece(R8),
    get_row(9,S,R9), valid_piece(R9).

all_cols_valid(S) :-
    get_col(1,S,C1), valid_piece(C1),
    get_col(2,S,C2), valid_piece(C2),
    get_col(3,S,C3), valid_piece(C3),
    get_col(4,S,C4), valid_piece(C4),
    get_col(5,S,C5), valid_piece(C5),
    get_col(6,S,C6), valid_piece(C6),
    get_col(7,S,C7), valid_piece(C7),
    get_col(8,S,C8), valid_piece(C8),
    get_col(9,S,C9), valid_piece(C9).

all_blocks_valid(S) :-
    get_block(1,S,B1), valid_piece(B1),
    get_block(2,S,B2), valid_piece(B2),
    get_block(3,S,B3), valid_piece(B3),
    get_block(4,S,B4), valid_piece(B4),
    get_block(5,S,B5), valid_piece(B5),
    get_block(6,S,B6), valid_piece(B6),
    get_block(7,S,B7), valid_piece(B7),
    get_block(8,S,B8), valid_piece(B8),
    get_block(9,S,B9), valid_piece(B9).



% ---------- domain ----------

idx(1). idx(2). idx(3). idx(4). idx(5). idx(6). idx(7). idx(8). idx(9).

% ---------- list helpers (self-defined, no library) ----------
select(X, [X|Xs], Xs).
select(X, [Y|Ys], [Y|Zs]) :-
    select(X, Ys, Zs).

perm([], []).
perm(L, [X|Xs]) :-
    select(X, L, L1),
    perm(L1, Xs).

perm_1_9(L) :-
    perm([1,2,3,4,5,6,7,8,9], L).

% ---------- extract list from row/col/block ----------
piece_list(row(L), L).
piece_list(col(L), L).
piece_list(block(L), L).


all_nonvar([]).
all_nonvar([X|Xs]) :-
    nonvar(X),
    all_nonvar(Xs).

% Valid piece: exactly the numbers 1..9, each exactly once
% remove_first(+X, +List, -Rest)  (deterministic choice of one occurrence)
remove_first(X, [X|Xs], Xs) :- !.
remove_first(X, [Y|Ys], [Y|Zs]) :-
    remove_first(X, Ys, Zs).

valid_piece(Piece) :-
    piece_list(Piece, L),
    msort(L, [1,2,3,4,5,6,7,8,9]).


% ---------- getters WITHOUT nth1/3 ----------
% sudoku(R1..R9, C1..C9, B1..B9)

% Use arg/3 to avoid counting underscores!
% Row 1-9 are arguments 1-9 of the sudoku term
get_row(I, S, R) :- 
    idx(I), 
    arg(I, S, R).

% Col 1-9 are arguments 10-18
get_col(I, S, C) :- 
    idx(I), 
    Offset is I + 9, 
    arg(Offset, S, C).

% Block 1-9 are arguments 19-27
get_block(I, S, B) :- 
    idx(I), 
    Offset is I + 18, 
    arg(Offset, S, B).

% ---------- aggregate checks WITHOUT forall/2 ----------



