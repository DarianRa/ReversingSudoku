% bk.pl

% Indices
idx(1). idx(2). idx(3). idx(4). idx(5). idx(6). idx(7). idx(8). idx(9).

% --- PIECE VALIDATION ---
% Handles: row([1..9])
piece_list(row(L), L).
piece_list(col(L), L).
piece_list(block(L), L).

% Checks if one piece is 1..9
valid_piece(Piece) :-
    nonvar(Piece),
    piece_list(Piece, L),
    ground(L),
    is_list(L),
    sort(L, [1,2,3,4,5,6,7,8,9]). % 'sort' removes duplicates, 'msort' does not. Use sort for set equality.

% The Helper
all_pieces_valid([]).
all_pieces_valid([H|T]) :-
    valid_piece(H),
    all_pieces_valid(T).

% --- EXTRACTORS ---
% Safe getters that won't crash if S is partial
get_row(I, S, R)   :- idx(I), arg(I, S, R).
get_col(I, S, C)   :- idx(I), O is I+9,  arg(O, S, C).
get_block(I, S, B) :- idx(I), O is I+18, arg(O, S, B).

rows(S, List) :-
    findall(R, (idx(I), get_row(I, S, R)), List),
    length(List, 9).

cols(S, List) :-
    findall(C, (idx(I), get_col(I, S, C)), List),
    length(List, 9).

blocks(S, List) :-
    findall(B, (idx(I), get_block(I, S, B)), List),
    length(List, 9).