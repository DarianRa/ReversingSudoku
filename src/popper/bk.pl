% ---------- basic validation ----------
valid_piece(Piece) :-
    piece_list(Piece, List),
    \+ has_duplicate(List).

has_duplicate([X|Xs]) :-
    member(X, Xs).
has_duplicate([_|Xs]) :-
    has_duplicate(Xs).

% helper to extract the list from row/col/block
piece_list(row(List), List).
piece_list(col(List), List).
piece_list(block(List), List).

% ---------- getters ----------
% get_row(+Index, +Sudoku, -Row)
get_row(N, sudoku(R1,R2,R3,R4,R5,R6,R7,R8,R9,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Row) :-
    idx(N),
    nth1(N, [R1,R2,R3,R4,R5,R6,R7,R8,R9], Row).

% get_col(+Index, +Sudoku, -Col)
get_col(N, sudoku(_,_,_,_,_,_,_,_,_,C1,C2,C3,C4,C5,C6,C7,C8,C9,_,_,_,_,_,_,_,_,_), Col) :-
    idx(N),
    nth1(N, [C1,C2,C3,C4,C5,C6,C7,C8,C9], Col).

% get_block(+Index, +Sudoku, -Block)
get_block(N, sudoku(_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,B1,B2,B3,B4,B5,B6,B7,B8,B9), Block) :-
    idx(N),
    nth1(N, [B1,B2,B3,B4,B5,B6,B7,B8,B9], Block).

% ---------- helper ----------
idx(1).
idx(2).
idx(3).
idx(4).
idx(5).
idx(6).
idx(7).
idx(8).
idx(9).