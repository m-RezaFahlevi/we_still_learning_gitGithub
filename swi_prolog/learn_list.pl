%Here we are try to understand list
%in programming language (swi-prolog)

p([1,2,3,4]).
p([aomine,midorima,akashi,murasakibara,kise]).
p([sasha,annie,connie,[armin,mikasa,eren]]).

%Recursive searching in List
anggota([apple,sony,samsung,htc,motorolla]).
anggota(X,[X|_]).
anggota(X,[_|Y]):- anggota(X,Y).
