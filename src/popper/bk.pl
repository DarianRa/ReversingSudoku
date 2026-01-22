% =========================
% bk.pl (full learning)
% =========================

idx(1). idx(2). idx(3). idx(4). idx(5). idx(6). idx(7). idx(8). idx(9).

piece_list(row(L), L).
piece_list(col(L), L).
piece_list(block(L), L).

valid_piece(Piece) :-
    nonvar(Piece),
    piece_list(Piece, L),
    ground(L),
    sort(L, [1,2,3,4,5,6,7,8,9]).

is_sudoku(S) :- nonvar(S), compound(S), functor(S, sudoku, 27).

get_row(I, S, R)   :- idx(I), is_sudoku(S), arg(I, S, R).
get_col(I, S, C)   :- idx(I), is_sudoku(S), O is I+9,  arg(O, S, C).
get_block(I, S, B) :- idx(I), is_sudoku(S), O is I+18, arg(O, S, B).

rows(S, L)   :- is_sudoku(S), findall(R, (idx(I), get_row(I, S, R)), L).
cols(S, L)   :- is_sudoku(S), findall(C, (idx(I), get_col(I, S, C)), L).
blocks(S, L) :- is_sudoku(S), findall(B, (idx(I), get_block(I, S, B)), L).

head([H|_], H).
tail([_|T], T).
empty([]).
