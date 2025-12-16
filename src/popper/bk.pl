% ---------- basic validation ----------
valid_piece(List) :-
    \+ has_duplicate(List).

has_duplicate([X|Xs]) :-
    member(X, Xs).
has_duplicate([_|Xs]) :-
    has_duplicate(Xs).

% ---------- getters ----------
% get_row(+Index, +Sudoku, -Row)
get_row(N, sudoku(R1,R2,R3,R4,R5,R6,R7,R8,R9,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_), Row) :-
    nth1(N, [R1,R2,R3,R4,R5,R6,R7,R8,R9], Row).

% get_col(+Index, +Sudoku, -Col)
get_col(N, sudoku(_,_,_,_,_,_,_,_,_,C1,C2,C3,C4,C5,C6,C7,C8,C9,_,_,_,_,_,_,_,_,_,_), Col) :-
    nth1(N, [C1,C2,C3,C4,C5,C6,C7,C8,C9], Col).

% get_block(+Index, +Sudoku, -Block)
get_block(N, sudoku(_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,B1,B2,B3,B4,B5,B6,B7,B8,B9), Block) :-
    nth1(N, [B1,B2,B3,B4,B5,B6,B7,B8,B9], Block).