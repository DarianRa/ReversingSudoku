% ---------- block ----------
block([_,_,_,_,_,_,_,_,_]).

% ---------- BS is Valid Crutch ----------
valid(Block) :-
    \+ has_duplicate(Block).

has_duplicate([X|Xs]) :-
    member(X, Xs).     
has_duplicate([_|Xs]) :-
    has_duplicate(Xs).
