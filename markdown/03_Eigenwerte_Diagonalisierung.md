# 3. Eigenwerte, Eigenvektoren & Diagonalisierung

> ⚡ **PRIORITÄT 1 – Hier hast du 19/20 Punkte verloren (Aufgabe 2)!**

> [!INFO] Worum geht es hier? – Einfach erklärt
>
> Eigenwerte und Eigenvektoren sind eines der wichtigsten Konzepte der gesamten linearen Algebra – und gleichzeitig das Thema, das in deiner Klausur am schlechtesten lief. Aber die Grundidee ist gar nicht so kompliziert: Ein **Eigenvektor** ist ein Vektor, der durch eine Matrix nicht seine Richtung ändert, sondern nur gestreckt oder gestaucht wird. Der Faktor, um den er gestreckt wird, heißt **Eigenwert**. Wenn du zum Beispiel eine Spiegelungsmatrix hast, dann bleibt ein Vektor, der genau auf der Spiegelachse liegt, unverändert – er hat den Eigenwert 1. Ein Vektor senkrecht dazu wird umgeklappt – er hat den Eigenwert −1.
>
> Eigenwerte findest du, indem du das **charakteristische Polynom** berechnest – das ist $\det(A - \lambda I)$ – und dessen Nullstellen bestimmst. Der Kniff ist, dass jede Nullstelle ein Eigenwert ist. Für jeden Eigenwert berechnest du dann den **Eigenraum**, also die Menge aller zugehörigen Eigenvektoren, indem du den Kern von $(A - \lambda I)$ bestimmst.
>
> Die große Frage ist dann: Kann man eine Basis finden, die nur aus Eigenvektoren besteht? Wenn ja, ist die Matrix **diagonalisierbar** – und das vereinfacht alles enorm, weil eine Diagonalmatrix trivial zu potenzieren ist. Ob das klappt, hängt davon ab, ob für jeden Eigenwert genug linear unabhängige Eigenvektoren existieren. Dafür vergleichst du die **algebraische Vielfachheit** (wie oft der Eigenwert als Nullstelle im char. Polynom vorkommt) mit der **geometrischen Vielfachheit** (Dimension des Eigenraums). Stimmen beide überein, ist die Matrix diagonalisierbar.
>
> **Für die Nachklausur:** In der Klausur solltest du zeigen, dass gewisse Vektoren Eigenvektoren sind, und den Defekt einer Matrix bestimmen. Übe insbesondere den Beweis, dass bei einer Matrix $M = \lambda_1 v_1 v_1^T + \ldots$ die $v_i$ tatsächlich Eigenvektoren sind – genau das kam dran!

## 3.1 Grundbegriffe

### Eigenwert & Eigenvektor
$\lambda \in K$ ist **Eigenwert** von $A$ und $v \neq 0$ ist **Eigenvektor** zum Eigenwert $\lambda$, wenn:
$$Av = \lambda v$$

### Eigenraum
$$E_\lambda = \ker(A - \lambda I) = \{v \in V \mid Av = \lambda v\}$$

Der Eigenraum ist immer ein **Unterraum** von $V$.

### Charakteristisches Polynom
$$\chi_A(\lambda) = \det(A - \lambda I)$$

Die Eigenwerte sind genau die **Nullstellen** von $\chi_A$.

> **KLAUSURRELEVANT (Aufgabe 1.1):** Bei Jordan-Normalform $J$ kann man $\chi_A$ direkt ablesen!
> Wenn $J$ die Diagonaleinträge $\lambda_1, \ldots, \lambda_n$ hat:
> $$\chi_A(\lambda) = \prod_{i=1}^{n} (\lambda_i - \lambda)$$

## 3.2 Algebraische vs. Geometrische Vielfachheit

### Algebraische Vielfachheit (alg. VF)
= Vielfachheit von $\lambda$ als Nullstelle von $\chi_A$

**Beispiel:** $\chi_A(\lambda) = (\lambda - 2)^3(\lambda + 1)^2$ → alg. VF von 2 ist **3**, alg. VF von -1 ist **2**

### Geometrische Vielfachheit (geo. VF)
$$\text{geo. VF}(\lambda) = \dim(\ker(A - \lambda I)) = \dim(E_\lambda)$$

= Anzahl der linear unabhängigen Eigenvektoren zum Eigenwert $\lambda$

### Fundamentale Ungleichung
$$1 \leq \text{geo. VF}(\lambda) \leq \text{alg. VF}(\lambda)$$

> **KLAUSURRELEVANT (Aufgabe 1.4):** Bei JNF:
> - geo. VF = Anzahl der Jordan-Blöcke zum Eigenwert $\lambda$
> - alg. VF = Summe der Größen aller Jordan-Blöcke zum Eigenwert $\lambda$

## 3.3 Diagonalisierbarkeit

$A$ ist **diagonalisierbar** $\iff$ eine der folgenden äquivalenten Bedingungen gilt:
1. Es existiert eine Basis aus Eigenvektoren von $A$
2. $\text{geo. VF}(\lambda_i) = \text{alg. VF}(\lambda_i)$ für **jeden** Eigenwert $\lambda_i$
3. Die JNF von $A$ ist eine Diagonalmatrix (alle Jordan-Blöcke haben Größe 1)
4. Das Minimalpolynom hat nur einfache Nullstellen

> **Achtung:** Eine Matrix **kann** diagonalisierbar sein, auch wenn Eigenwerte mehrfache algebraische Vielfachheit haben! Entscheidend ist: geo = alg für jeden EW.

### Diagonalisieren: Algorithmus
1. Berechne $\chi_A(\lambda)$ und finde alle Eigenwerte
2. Berechne für jeden EW $\lambda_i$ den Eigenraum $E_{\lambda_i} = \ker(A - \lambda_i I)$
3. Prüfe: geo. VF = alg. VF für alle EW?
4. Wenn ja: $S = (v_1 | \cdots | v_n)$ (Eigenvektoren als Spalten)
5. Dann: $A = S \cdot D \cdot S^{-1}$ mit $D = \text{diag}(\lambda_1, \ldots, \lambda_n)$

## 3.4 Defekt einer Matrix

$$\text{Defekt}(A) = \dim(\ker(A)) = n - \text{Rang}(A)$$

> **KLAUSURRELEVANT (Aufgabe 2.2):**
> Hat $A$ den Eigenwert $\lambda = 0$ mit algebraischer Vielfachheit $m \geq 1$, dann:
> - $\text{Defekt}(A) = \dim(\ker(A)) = \text{geo. VF}(0)$
> - Es gilt: $1 \leq \text{geo. VF}(0) \leq m$
> - Also: $1 \leq \text{Defekt}(A) \leq m$
> - Genauer: $\text{Rang}(A) = n - \text{Defekt}(A)$, also $n - m \leq \text{Rang}(A) \leq n - 1$

## 3.5 Beweis zu ONS und Eigenwerten (Klausuraufgabe 2.1!)

**Gegeben:** ONS $v_1, v_2, v_3 \in \mathbb{R}^n$, $M = \lambda_1 v_1 v_1^T + \lambda_2 v_2 v_2^T + \lambda_3 v_3 v_3^T$

**Zu zeigen:** $Mv_i = \lambda_i v_i$

**Beweis:**
$$Mv_1 = (\lambda_1 v_1 v_1^T + \lambda_2 v_2 v_2^T + \lambda_3 v_3 v_3^T) v_1$$
$$= \lambda_1 v_1 \underbrace{(v_1^T v_1)}_{= 1} + \lambda_2 v_2 \underbrace{(v_2^T v_1)}_{= 0} + \lambda_3 v_3 \underbrace{(v_3^T v_1)}_{= 0}$$
$$= \lambda_1 v_1$$

**Schlüssel:** Die ONS-Eigenschaft $v_i^T v_j = \delta_{ij}$ (Kronecker-Delta) ist **der** entscheidende Trick!

Analog für $v_2$ und $v_3$. $\square$

> **Merke:** Das Produkt $v v^T$ (äußeres Produkt) ist eine $n \times n$-Matrix (Rang 1), die auf den Unterraum $\text{span}(v)$ projiziert! So eine Matrix heißt **Projektionsmatrix** (bis auf Normierung).

## 3.6 Zusammenhang: Eigenwerte und Matrixeigenschaften

| Eigenschaft | Bedingung an Eigenwerte |
|-------------|------------------------|
| $A$ invertierbar | Alle $\lambda_i \neq 0$ |
| $\det(A)$ | $= \prod \lambda_i$ |
| $\text{Spur}(A)$ | $= \sum \lambda_i$ |
| $A$ symmetrisch ($A = A^T$) | Alle Eigenwerte reell |
| $A$ positiv definit | Alle $\lambda_i > 0$ |
| $A$ orthogonal | Alle $|\lambda_i| = 1$ |
| $A^k$ hat Eigenwerte | $\lambda_i^k$ |
| $A$ nilpotent | Alle $\lambda_i = 0$ |
| $A$ idempotent ($A^2 = A$) | $\lambda_i \in \{0, 1\}$ |
