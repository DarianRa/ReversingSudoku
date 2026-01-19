% ---------- basic validation ----------
valid_piece(Piece) :-
    piece_list(Piece, List),
    \+ has_duplicate(List).

has_duplicate([X|Xs]) :-
    member(X, Xs).
has_duplicate([_|Xs]) :-
    has_duplicate(Xs).

% ---------- piece list ----------
piece_list(row(L), L).
piece_list(col(L), L).
piece_list(block(L), L).

% ---------- indices ----------
idx(1). idx(2). idx(3).
idx(4). idx(5). idx(6).
idx(7). idx(8). idx(9).

% ---------- get_row ----------
get_row(N,
    sudoku(R1,R2,R3,R4,R5,R6,R7,R8,R9),
    Row) :-
    idx(N),
    nth1(N, [R1,R2,R3,R4,R5,R6,R7,R8,R9], Row).

% ---------- get_col ----------
get_col(N,
    sudoku(
        row(A1,A2,A3,A4,A5,A6,A7,A8,A9),
        row(B1,B2,B3,B4,B5,B6,B7,B8,B9),
        row(C1,C2,C3,C4,C5,C6,C7,C8,C9),
        row(D1,D2,D3,D4,D5,D6,D7,D8,D9),
        row(E1,E2,E3,E4,E5,E6,E7,E8,E9),
        row(F1,F2,F3,F4,F5,F6,F7,F8,F9),
        row(G1,G2,G3,G4,G5,G6,G7,G8,G9),
        row(H1,H2,H3,H4,H5,H6,H7,H8,H9),
        row(I1,I2,I3,I4,I5,I6,I7,I8,I9)
    ),
    col(Col)
) :-
    idx(N),
    nth1(N,
        [A1,B1,C1,D1,E1,F1,G1,H1,I1,
         A2,B2,C2,D2,E2,F2,G2,H2,I2,
         A3,B3,C3,D3,E3,F3,G3,H3,I3,
         A4,B4,C4,D4,E4,F4,G4,H4,I4,
         A5,B5,C5,D5,E5,F5,G5,H5,I5,
         A6,B6,C6,D6,E6,F6,G6,H6,I6,
         A7,B7,C7,D7,E7,F7,G7,H7,I7,
         A8,B8,C8,D8,E8,F8,G8,H8,I8,
         A9,B9,C9,D9,E9,F9,G9,H9,I9],
        Col).

% ---------- get_block ----------
get_block(N, S, block(Block)) :-
    block_indices(N, Idxs),
    findall(V,
        (member((R,C),Idxs),
         get_row(R,S,row(Row)),
         nth1(C,Row,V)),
        Block).

block_indices(1, [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]).
block_indices(2, [(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)]).
block_indices(3, [(1,7),(1,8),(1,9),(2,7),(2,8),(2,9),(3,7),(3,8),(3,9)]).
block_indices(4, [(4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(6,1),(6,2),(6,3)]).
block_indices(5, [(4,4),(4,5),(4,6),(5,4),(5,5),(5,6),(6,4),(6,5),(6,6)]).
block_indices(6, [(4,7),(4,8),(4,9),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9)]).
block_indices(7, [(7,1),(7,2),(7,3),(8,1),(8,2),(8,3),(9,1),(9,2),(9,3)]).
block_indices(8, [(7,4),(7,5),(7,6),(8,4),(8,5),(8,6),(9,4),(9,5),(9,6)]).
block_indices(9, [(7,7),(7,8),(7,9),(8,7),(8,8),(8,9),(9,7),(9,8),(9,9)]).
