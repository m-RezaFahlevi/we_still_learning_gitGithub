male('Russel').
male('BertrandRussel').
male('JohnRussel').
male('JJRussel').
male('QuantumRussel').
male('WilliamRHammilton').
male('EugeneHammilton').
male('EulerHammilton').
male('SomaHammilton').
male('AlucardHammilton').

female('Victoria').
female('Stephany').
female('JessicaRussel').
female('ScarletRussel').
female('Mina').

ayah('Russel','BertrandRussel').
ayah('Russel','JohnRussel').
ayah('Russel','JessicaRussel').
ayah('BertrandRussel','JJRussel').
ayah('BertrandRussel','QuantumRussel').
ayah('BertrandRussel','ScarletRussel').
ayah('WilliamRHammilton','EugeneHammilton').
ayah('WilliamRHammilton','EulerHammilton').
ayah('EugeneHammilton','SomaHammilton').
ayah('EulerHammilton','AlucardHammilton').

ibu('Victoria','BertrandRussel').
ibu('Victoria','JohnRussel').
ibu('Victoria','JessicaRussel').
ibu('Stephany','JJRussel').
ibu('Stephany','QuantumRussel').
ibu('Stephany','ScarletRussel').
ibu('ScarletRussel','EugeneHammilton').
ibu('ScarletRussel','EulerHammilton').
ibu('Mina','SomaHammilton').
ibu('Yoko','AlucardHammilton').

anak(X,Y):- ayah(Y,X); ibu(Y,X), X \= Y.
suami(X,Y):- anak(Z,X), anak(Z,Y), X \= Y, male(X), female(Y).
istri(X,Y):- anak(Z,X), anak(Z,Y), X \= Y, female(X), male(Y).
saudaraKandung(X,Y) :- ayah(Z,X), ayah(Z,Y), X \= Y, ibu(L,X), ibu(L,Y).
keponakan(X,Y):- ayah(K,X), ayah(L,Y), saudaraKandung(K,L), K\=L.
mertua(X,Y):- 
	istri(L,Y), ayah(X,L); suami(L,Y), ayah(X,L);
	istri(L,Y), ibu(X,L); suami(L,Y), ibu(X,L).
kakek(X,Y):- ayah(W,Y), ayah(X,W); ibu(W,Y), ayah(X,W).
nenek(X,Y):- ayah(W,Y), ibu(X,W); ibu(W,Y), ibu(X,W).
