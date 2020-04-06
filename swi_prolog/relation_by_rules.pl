parent(tom, bob). %Tom is a parent of Bob.
parent(tom, liz). %Tom is a parent of Liz.
parent(pam, bob). %Pam is a parent of Pam.
parent(bob, ann). %Bob is a parent of Ann.
parent(bob, pat). %Bob is a parent of Pat.
parent(pat, jim). %Pat is a parent of Jim.

%Adding more fact about familiy tree above as below

female(pam).
female(liz).
female(pat).
female(ann).
male(jim).
male(bob).
male(tom).

%Create a rules |-:.for_all(x,y) P(x,y).Q(y) --> R(x,y)

mother(X,Y) :- parent(X,Y), female(X).
father(X,Y) :- parent(X,Y), male(X).

%Create a rules |-:.for_all(x,y,z). P(x,y).P(y,z) --> Q(x,z)

grand_parent(X,Z):-
	parent(X,Y),
	parent(Y,Z).

%Create a rules |-:.for_all(x,y,z). P(z,x).P(z,y).Q(x) --> R(x,y)

sister(X,Y):-
	parent(Z,X),
	parent(Z,Y),
	female(X).

sister_improved(X,Y):-
	parent(Z,X),
	parent(Z,Y),
	female(X),
	X \= Y.

%Everybody has a child is happy
%Create a rules happy and has a child
%After that, we create a rules happy(x) :- has_a_child(x).

child_of(X,Y) :- parent(Y,X).
has_a_child(X) :- parent(X,Y), child_of(Y,X).
has_a_parent(X) :- child_of(X,Y), parent(Y,X).
happy(X) :- has_a_child(X).

%X have two children if has_a_child(X) who has a sister.

has_two_children(X) :-
	child_of(Y,X),
	child_of(Z,X),
	sister_improved(Y,Z).

grand_children(X,Y) :- grand_parent(Y,X).

%X is aunt of Y if X sister of Z and Z parent of X.
aunt(X,Y) :- sister_improved(X,Z), parent(Z,Y).
