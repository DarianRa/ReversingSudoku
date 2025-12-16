% ---------- head ----------
head_pred(valid_block,1).

% ---------- body predicates ----------
body_pred(valid,1).

% ---------- types ----------
type(valid, bool).
type(block,(list,)).
type(valid_block,(block,)).

% ---------- allow predicate invention ----------
max_inv_preds(2).
max_inv_bodies(3).
