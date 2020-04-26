%Here we are try to understand list
%in programming language (swi-prolog)

p([1,2,3,4]).
p([aomine,midorima,akashi,murasakibara,kise]).
p([sasha,annie,connie,[armin,mikasa,eren]]).

%Recursive searching in List
anggota([apple,sony,samsung,htc,motorolla]).
anggota(X,[X|_]).
anggota(X,[_|Y]):- anggota(X,Y).

%Concatenation list
conc([],L,L).
conc([X|L1],L2,[X|L3]):- conc(L1,L2,L3).

%Adding list using predicate add
add(X,L,[X|L]).

%Delete an item in list using predicate del
del(X, [X|Tail],Tail).
del(X,[Y|Tail],[Y|TailX]):- del(X,Tail,TailX).
