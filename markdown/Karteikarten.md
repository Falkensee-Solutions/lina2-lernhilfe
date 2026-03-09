# Karteikarten – LINA2 Definitionen & Sätze

> Lerne jede Karte: Lies die **Frage**, versuche die Antwort zu formulieren, dann vergleiche mit der **Antwort**.

---

## 📦 Block A: Grundbegriffe

### Karte A1
**F:** Was ist ein Vektorraum?  
**A:** Eine abelsche Gruppe $(V, +)$ mit Skalarmultiplikation über einem Körper $K$, die Assoziativität, neutrales Element ($1 \cdot v = v$) und zwei Distributivgesetze erfüllt.

### Karte A2
**F:** Wann ist eine Teilmenge $U \subseteq V$ ein Unterraum?  
**A:** Wenn $U \neq \emptyset$ und $U$ unter Addition und Skalarmultiplikation abgeschlossen ist. Kurzform: $\lambda u + \mu w \in U$ für alle $\lambda, \mu \in K$ und $u, w \in U$.

### Karte A3
**F:** Was bedeutet "linear unabhängig"?  
**A:** $v_1, \ldots, v_n$ sind linear unabhängig, wenn $\lambda_1 v_1 + \cdots + \lambda_n v_n = 0$ nur die triviale Lösung $\lambda_1 = \cdots = \lambda_n = 0$ hat.

### Karte A4
**F:** Was ist eine Basis? Was ist die Dimension?  
**A:** Eine Basis ist ein linear unabhängiges Erzeugendensystem. Die Dimension ist die Anzahl der Basisvektoren. Jede Basis hat gleich viele Elemente.

### Karte A5
**F:** Wann ist eine Abbildung $f: V \to W$ linear?  
**A:** Wenn $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ für alle $\alpha, \beta \in K$ und $u, v \in V$.

---

## 📦 Block B: Determinanten

### Karte B1
**F:** Wie berechnet man die Determinante einer Dreiecksmatrix?  
**A:** Produkt der Diagonaleinträge: $\det(A) = \prod_{i=1}^n a_{ii}$

### Karte B2
**F:** Nenne 4 wichtige Rechenregeln für Determinanten.  
**A:**
1. $\det(AB) = \det(A) \cdot \det(B)$
2. $\det(A^T) = \det(A)$
3. $\det(\lambda A) = \lambda^n \det(A)$
4. $\det(SAS^{-1}) = \det(A)$

### Karte B3
**F:** Was sagt $\det(A)$ geometrisch aus?  
**A:** $|\det(A)|$ = Volumenfaktor. $\det(A) > 0$: orientierungserhaltend. $\det(A) < 0$: orientierungsumkehrend. $|\det(A)| = 1$: volumentreu.

### Karte B4
**F:** Was ist die Laplace-Entwicklung?  
**A:** $\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij} \det(A_{ij})$ (Entwicklung nach $i$-ter Zeile). Tipp: Zeile/Spalte mit den meisten Nullen wählen.

---

## 📦 Block C: Eigenwerte & Diagonalisierung

### Karte C1
**F:** Was sind Eigenwert und Eigenvektor?  
**A:** $\lambda$ ist Eigenwert und $v \neq 0$ ist Eigenvektor von $A$, wenn $Av = \lambda v$.

### Karte C2
**F:** Wie findet man die Eigenwerte?  
**A:** Als Nullstellen des charakteristischen Polynoms $\chi_A(\lambda) = \det(A - \lambda I) = 0$.

### Karte C3
**F:** Was ist der Unterschied zwischen algebraischer und geometrischer Vielfachheit?  
**A:** **Alg. VF:** Vielfachheit als Nullstelle von $\chi_A$. **Geo. VF:** $\dim(\ker(A - \lambda I))$ = Anzahl linear unabhängiger Eigenvektoren. Es gilt: $1 \leq \text{geo} \leq \text{alg}$.

### Karte C4
**F:** Wann ist $A$ diagonalisierbar?  
**A:** Genau dann, wenn geo. VF = alg. VF für **jeden** Eigenwert. Äquivalent: Es existiert eine Basis aus Eigenvektoren. Äquivalent: Alle Jordan-Blöcke haben Größe 1.

### Karte C5
**F:** Wie hängen Eigenwerte und Determinante/Spur zusammen?  
**A:** $\det(A) = \prod \lambda_i$ und $\text{Spur}(A) = \sum \lambda_i$.

### Karte C6
**F:** Was besagt der Defekt bei EW = 0?  
**A:** Hat $A$ den EW $0$ mit alg. VF $m$, dann: $\text{Defekt}(A) = \dim(\ker(A)) = \text{geo. VF}(0)$, mit $1 \leq \text{Defekt} \leq m$.

### Karte C7
**F:** Wie zeigt man $Mv_i = \lambda_i v_i$ wenn $M = \sum \lambda_k v_k v_k^T$ und $\{v_k\}$ ONS?  
**A:** Einsetzen: $Mv_i = \sum_k \lambda_k v_k (v_k^T v_i)$. Wegen ONS: $v_k^T v_i = \delta_{ki}$. Also bleibt nur $\lambda_i v_i$. **Schlüssel: ONS-Eigenschaft!**

---

## 📦 Block D: Skalarprodukte & Gram-Schmidt

### Karte D1
**F:** Nenne die Axiome eines komplexen Skalarprodukts.  
**A:** 1) Hermitesche Symmetrie: $\langle u|v\rangle = \overline{\langle v|u\rangle}$ 2) Antilinear im 1. Argument 3) Linear im 2. Argument 4) Positiv definit: $\langle v|v\rangle > 0$ für $v \neq 0$

### Karte D2
**F:** Beschreibe den Gram-Schmidt-Algorithmus.  
**A:** Schritt $k$: $\tilde{e}_k = v_k - \sum_{j<k} \langle e_j | v_k \rangle \, e_j$, dann $e_k = \tilde{e}_k / \|\tilde{e}_k\|$. Projektion abziehen → normieren.

### Karte D3
**F:** Was ist eine Orthogonalprojektion auf $U$?  
**A:** $P_U(v) = \sum_i \langle e_i | v \rangle e_i$ (mit ONB $\{e_i\}$ von $U$). Eigenschaften: $P^2 = P$, $P^* = P$.

### Karte D4
**F:** Was ist das Integral-Skalarprodukt für komplexe Funktionen?  
**A:** $\langle f | g \rangle = \int_a^b \overline{f(x)} g(x) \, dx$. **Achtung:** Konjugation im 1. Argument!

---

## 📦 Block E: Jordan-Normalform

### Karte E1
**F:** Was ist ein Jordan-Block $J_k(\lambda)$?  
**A:** $k \times k$-Matrix mit $\lambda$ auf der Diagonale und 1en auf der oberen Nebendiagonale, sonst 0.

### Karte E2
**F:** Wie liest man das Minimalpolynom aus der JNF ab?  
**A:** $\mu_A(\lambda) = \prod_i (\lambda - \lambda_i)^{s_i}$, wobei $s_i$ = Größe des **größten** Jordan-Blocks zum EW $\lambda_i$.

### Karte E3
**F:** Wie liest man die geometrische Vielfachheit aus der JNF ab?  
**A:** geo. VF($\lambda$) = **Anzahl** der Jordan-Blöcke zum EW $\lambda$.

### Karte E4
**F:** Was ist ein Hauptvektor der Stufe $k$?  
**A:** $v$ mit $(A - \lambda I)^k v = 0$ aber $(A - \lambda I)^{k-1} v \neq 0$.

---

## 📦 Block F: Cayley-Hamilton & Matrixexponential

### Karte F1
**F:** Was besagt der Satz von Cayley-Hamilton?  
**A:** Jede Matrix erfüllt ihr eigenes char. Polynom: $\chi_A(A) = 0$.

### Karte F2
**F:** Was ist das Minimalpolynom und wie hängt es mit $\chi_A$ zusammen?  
**A:** Kleinstes normiertes Polynom $p$ mit $p(A) = 0$. Es teilt $\chi_A$ und hat die gleichen Nullstellen.

### Karte F3
**F:** Was ist das Matrixexponential?  
**A:** $\exp(A) = \sum_{k=0}^\infty \frac{A^k}{k!} = I + A + \frac{A^2}{2!} + \cdots$

### Karte F4
**F:** Wie zeigt man $A^m = A$ für idempotentes $A$ per Induktion?  
**A:** IA: $A^1 = A$ ✓. IS: $A^{m+1} = A^m \cdot A = A \cdot A = A^2 = A$ (letzterer Schritt weil $A^2 = A$).

### Karte F5
**F:** Warum gilt $\exp(A) = I + (e-1)A$ wenn $A^2 = A$?  
**A:** Da $A^k = A$ für $k \geq 1$: $\exp(A) = I + \sum_{k=1}^\infty \frac{A}{k!} = I + A \cdot (e - 1)$.

---

## 📦 Block G: Isometrien & Spezialmatrizen

### Karte G1
**F:** Wann ist $A$ orthogonal? Was folgt?  
**A:** $A^T A = I$ (also $A^{-1} = A^T$). Folgt: $\det(A) = \pm 1$, Spalten sind ONB, $A$ ist eine Isometrie.

### Karte G2
**F:** Wann ist eine reelle $A$ sym.? Was ist der Spektralsatz?  
**A:** Symmetrisch: $A = A^T$. Spektralsatz: sym. Matrizen haben nur reelle EW und sind **orthogonal diagonalisierbar**.

### Karte G3
**F:** Was ist eine Gruppe? Nenne die 4 Axiome.  
**A:** $(G, \circ)$ mit: 1) Abgeschlossenheit 2) Assoziativität 3) Neutrales Element $e$ 4) Inverse existieren.

### Karte G4
**F:** Was ist der Zusammenhang zwischen Isometrie und Determinante?  
**A:** Isometrie $\Rightarrow |\det(A)| = 1$. Wenn $\det = 1$: Rotation. Wenn $\det = -1$: Spiegelung (nicht notw. orientierungserhaltend!).

---

## 📦 Block H: Beweistechniken

### Karte H1
**F:** Wie funktioniert vollständige Induktion?  
**A:** 1) **IA:** Zeige Aussage für $n_0$ (Anfang). 2) **IV:** Nimm an, Aussage gilt für $n = m$. 3) **IS:** Zeige Aussage für $n = m+1$ unter Nutzung von IV.

### Karte H2
**F:** Wie führt man einen Widerspruchsbeweis?  
**A:** Nimm das Gegenteil der Behauptung an. Leite daraus einen Widerspruch (zu Voraussetzung oder bekannter Tatsache) her. Also muss die Behauptung gelten.

### Karte H3
**F:** Wie zeigt man $U$ ist Unterraum?  
**A:** Zeige 3 Dinge: 1) $0 \in U$ (nicht leer). 2) Abgeschlossen unter Addition. 3) Abgeschlossen unter Skalarmultiplikation.
