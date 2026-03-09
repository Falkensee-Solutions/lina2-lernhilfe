# Originale Klausuren

## Klausur 2026

**Lineare Algebra II – FU Berlin**
19.02.2026

**Aufgabenpaket 1: Jordan-Normalform (30 P.)**
Gegeben die Matrix $A \in \mathbb{R}^{5\times 5}$ mit $A = V J V^{-1}$, wobei die Matrizen $J, V \in \mathbb{R}^{5\times 5}$ folgende Gestalt haben sollen:
$$
J = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & -1 & 1 & 0 \\
0 & 0 & 0 & -1 & 0 \\
0 & 0 & 0 & 0 & -1
\end{pmatrix}
\quad \text{und} \quad
V = \begin{pmatrix}
| & | & | & | & | \\
v_1 & v_2 & v_3 & v_4 & v_5 \\
| & | & | & | & |
\end{pmatrix}.
$$
Dabei sind $v_i \in \mathbb{R}^5$ für $i = 1, \dots, 5$ die Spalten der Matrix $V$. (kurz gesagt: $J$ ist eine Jordan-Normalform von $A$)

**1.1** Ohne Begründung: Wie lautet das charakteristische Polynom von $A$?
**1.2** Wie lautet das Minimalpolynom von $A$? Begründen Sie!
**1.3** Geben Sie Basisvektoren des Eigenraums zum Eigenwert -1 von $A$ an! Begründen Sie!
**1.4** Geben Sie jeweils die geometrische Vielfachheit der Eigenwerte von $A$ an! Begründen Sie!
**1.5** Ohne Begründung: Geben Sie einen Hauptvektor erster Stufe von $A$ an!
**1.6** Berechnen Sie die Determinante von $A$ (Hinweis: Zeigen Sie, dass $A$ und $J$ die gleiche Determinante haben)!
**1.7** Stellt die Matrix $A$ eine volumentreue lineare Abbildung dar? Begründen Sie!
**1.8** Stellt die Matrix $A$ eine orientierungserhaltende lineare Abbildung dar? Begründen Sie!
**1.9** Kann $A \in \mathbb{R}^{5\times 5}$ eine symmetrische Matrix sein? Begründen Sie!

**Aufgabenpaket 2: Bedeutung von Eigenwerten (20 P.)**
**2.1** Gegeben sei das Orthonormalsystem $v_1, v_2, v_3 \in \mathbb{R}^n, n > 3$, bezüglich des Standard-Skalarproduktes $\langle x|y \rangle = x^\top y$. Für die reellen Zahlen $\lambda_1, \lambda_2, \lambda_3 \in \mathbb{R}$ sei ferner die folgende Matrix $M \in \mathbb{R}^{n\times n}$ gegeben:
$$
M = \lambda_1 v_1 v_1^\top + \lambda_2 v_2 v_2^\top + \lambda_3 v_3 v_3^\top.
$$
Zeigen Sie, dass die Matrix $M$ jeweils den Eigenvektor $v_i$ zum Eigenwert $\lambda_i$ für $i \in \{1, 2, 3\}$ besitzt!
**2.2** Welche möglichst genauen Angaben kann man bezüglich des Defekts einer Matrix $A$ machen, die den Eigenwert $\lambda = 0$ mit algebraischer Vielfachheit $m \geq 1$ besitzt? Begründen Sie!

**Aufgabenpaket 3: Gram-Schmidt-Verfahren (30 P.)**
Gegeben seien die beiden Funktionen $f_1, f_2 : [0, 1] \to \mathbb{C}$, wobei
$f_1(x) = 1, \quad f_2(x) = ix.$
Berechnen Sie ausführlich eine Orthonormalbasis des Vektorraumes, der von diesen beiden Funktionen aufgespannt wird, bezüglich des Skalarproduktes
$$
\langle f|g \rangle = \int_0^1 \overline{f(x)} g(x) dx.
$$

**Aufgabenpaket 4: Matrixexponential (20 P.)**
Eine diagonalisierbare Matrix $A \in \mathbb{R}^{n\times n}$ habe nur die Eigenwerte $\lambda_1 = 0$ und $\lambda_2 = 1$.
**4.1** Ohne Begründung: Wie lautet das Minimalpolynom von $A$?
**4.2** Zeigen Sie anhand des Minimalpolynoms, dass $A^2 = A$ gilt! (Hinweis: Verwenden Sie bei der Begründung den Satz von Cayley-Hamilton)
**4.3** Folgern Sie daraus, dass $A^m = A$ gilt für $m \geq 1$!
**4.4** Zeigen Sie, dass $\exp(A) = I + (e - 1)A$ ist, wobei $I \in \mathbb{R}^{n\times n}$ die Einheitsmatrix sei!


---

## Probeklausur 2026

**Lineare Algebra II**

**Aufgabenpaket 1: Eigenschaften von Matrizen**
Gegeben sei folgende Matrix $A$:
$$
A = \begin{pmatrix}
-1 & -2 & -1 \\
0 & 1 & -1 \\
0 & 0 & 1
\end{pmatrix}.
$$

**1.1** Berechnen Sie die Eigenwerte von $A$. Welche algebraischen Vielfachheiten haben die Eigenwerte?
**1.2** Begründen Sie durch eine Rechnung, dass die Matrix $A$ nicht diagonalisierbar ist.
**1.3** Wie lautet die Jordan-Normalform von $A$? Begründen Sie!
**1.4** Wie lautet das Minimalpolynom von $A$? Begründen Sie!
**1.5** Ist die Matrix $A$ invertierbar? Begründen Sie anhand der Eigenwerte!
**1.6** Wie lautet die allgemeine Lösung des linearen Gleichungssystems $Ax = b$, wobei die rechte Seite $b$ ein Eigenvektor von $A$ zum Eigenwert $1$ sein soll?
**1.7** Stellt die Matrix $A$ eine volumentreue lineare Abbildung dar? Begründen Sie!
**1.8** Stellt die Matrix $A$ eine orientierungserhaltende lineare Abbildung dar? Begründen Sie!

**Aufgabenpaket 2: Konstruierbarkeit von Matrizen**
**2.1** Kann es eine symmetrische Matrix $S \in \mathbb{R}^{4\times 4}$ geben, die eine Rotation im vierdimensionalen Raum darstellt, deren Rotationsachse jedoch nicht im $\mathbb{R}^4$ liegt? Begründen Sie Ihre Aussage!
**2.2** Können Sie die $\ast$-Elemente in der folgenden Matrix
$$
B = \begin{pmatrix}
-1 & -1 & -1 \\
\ast & 1 & -1 \\
\ast & \ast & 1
\end{pmatrix} \in \mathbb{R}^{3\times 3}
$$
so durch reelle Zahlen ergänzen, dass $x^\top By$ ein Skalarprodukt für $x, y \in \mathbb{R}^3$ definiert? Begründen Sie!

**Aufgabenpaket 3: Endliche Körper**
Eine lineare Abbildung $f : K^n \to K^n$ über einem endlichen Körper $K$ mit $n \in \mathbb{N}$ habe keine Eigenwerte in $K$. Zeigen Sie, dass diese Abbildung nicht nilpotent ist! (Tipp: Begründen Sie über das Minimalpolynom).

**Aufgabenpaket 4: Gram-Schmidt-Verfahren**
Gegeben seien die Vektoren
$$
v_1 = \begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix}, \quad v_2 = \begin{pmatrix} 0 \\ 1 \\ i \end{pmatrix}
$$
im Raum $\mathbb{C}^3$.

**4.1** Berechnen Sie eine bezüglich des Standardskalarproduktes $\overline{x}^\top y$ orthonormale Basis des Untervektorraumes, der von $v_1$ und $v_2$ aufgespannt wird!
**4.2** Berechnen Sie die Matrix $\Pi \in \mathbb{C}^{3\times 3}$, die die orthogonale Projektion auf diesen Unterraum darstellt!