# 5. Jordan-Normalform, Minimalpolynom & Cayley-Hamilton

> ⚡ **PRIORITÄT 2 – Hier hast du 27/50 Punkte verloren (Aufgaben 1 + 4)!**

## 5.1 Jordan-Normalform (JNF)

### Jordan-Block
Ein **Jordan-Block** der Größe $k$ zum Eigenwert $\lambda$:

$$J_k(\lambda) = \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & & \ddots & \ddots & \vdots \\ 0 & \cdots & & \lambda & 1 \\ 0 & \cdots & & 0 & \lambda \end{pmatrix}$$

### Jordan-Normalform
Jede Matrix $A \in \mathbb{C}^{n \times n}$ ist ähnlich zu einer **Blockdiagonalmatrix** aus Jordan-Blöcken:

$$J = \begin{pmatrix} J_{k_1}(\lambda_1) & & \\ & J_{k_2}(\lambda_2) & \\ & & \ddots \end{pmatrix}$$

Es gibt eine invertierbare Matrix $V$ mit $A = VJV^{-1}$.

### Was man aus der JNF ablesen kann

| Information | Wie ablesen |
|-------------|-------------|
| Eigenwerte | Diagonaleinträge von $J$ |
| Algebraische VF von $\lambda$ | Summe der Größen aller Blöcke zu $\lambda$ |
| Geometrische VF von $\lambda$ | **Anzahl** der Blöcke zu $\lambda$ |
| Char. Polynom | $\chi_A(\lambda) = \prod_i (\lambda_i - \lambda)$ aus Diag. |
| Minimalpolynom | Produkt $\prod (\lambda - \lambda_i)^{m_i}$ wobei $m_i$ = Größe des **größten** Blocks zu $\lambda_i$ |
| Diagonalisierbar? | Ja $\iff$ alle Blöcke haben Größe 1 |
| Determinante | Produkt der Diagonaleinträge |

## 5.2 Klausuraufgabe 1 – Analyse der JNF

**Gegeben:**
$$J = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & -1 & 1 & 0 \\ 0 & 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0 & -1 \end{pmatrix}$$

**Struktur:**
- Block 1: $J_1(1)$ → Eigenwert 1, Größe 1
- Block 2: $J_1(1)$ → Eigenwert 1, Größe 1
- Block 3: $J_2(-1)$ → Eigenwert -1, Größe 2
- Block 4: $J_1(-1)$ → Eigenwert -1, Größe 1

### 1.1: Charakteristisches Polynom
$$\chi_A(\lambda) = (\lambda - 1)^2 (\lambda + 1)^3$$

(alg. VF von 1 ist 2, alg. VF von -1 ist 3)

### 1.2: Minimalpolynom
$$\mu_A(\lambda) = (\lambda - 1)(\lambda + 1)^2$$

**Begründung:** Der größte Jordan-Block zu EW 1 hat Größe 1, der größte zu EW -1 hat Größe 2.

### 1.3: Eigenraum zum Eigenwert -1
Die Eigenvektoren zum EW -1 sind die Spalten von $V$, die dem **Anfang** jedes Jordan-Blocks zu -1 entsprechen.

$E_{-1} = \text{span}(v_3, v_5)$ (Spalte 3 und 5 von $V$, da Block 3 bei Spalte 3 beginnt und Block 4 bei Spalte 5)

**Begründung:** $Av_3 = -v_3$ und $Av_5 = -v_5$ (aus $AV = VJ$ und der Struktur von $J$)

### 1.4: Geometrische Vielfachheiten
- geo. VF(1) = 2 (zwei Blöcke der Größe 1)
- geo. VF(-1) = 2 (zwei Blöcke: einer Größe 2, einer Größe 1)

### 1.5: Hauptvektor erster Stufe
$v_4$ ist ein **Hauptvektor** erster Stufe zum EW $-1$ (auch verallgemeinerter Eigenvektor).

Er erfüllt: $(A - (-1)I)v_4 = (A + I)v_4 = v_3 \neq 0$, aber $(A + I)^2 v_4 = 0$.

### 1.6: Determinante
$$\det(A) = \det(VJV^{-1}) = \det(V)\det(J)\det(V^{-1}) = \det(J)$$
$$\det(J) = 1 \cdot 1 \cdot (-1) \cdot (-1) \cdot (-1) = -1$$

### 1.7: Volumentreu?
$|{\det(A)}| = |-1| = 1$ → **Ja**, die Abbildung ist volumentreu.

### 1.8: Orientierungserhaltend?
$\det(A) = -1 < 0$ → **Nein**, die Abbildung ist **nicht** orientierungserhaltend.

**Begründung:** Eine lineare Abbildung ist orientierungserhaltend $\iff \det(A) > 0$.

### 1.9: Kann $A$ symmetrisch sein?
**Nein.**

**Begründung:** Symmetrische reelle Matrizen sind immer diagonalisierbar (Spektralsatz). Aber $A$ hat einen Jordan-Block der Größe 2 (zu EW -1), ist also **nicht** diagonalisierbar. Widerspruch!

## 5.3 Haupträume und Hauptvektoren

### Hauptraum
$$H_\lambda = \ker(A - \lambda I)^{m_\lambda}$$

wobei $m_\lambda$ = algebraische Vielfachheit von $\lambda$.

### Hauptvektor der Stufe $k$
$v$ ist Hauptvektor der Stufe $k$ zum EW $\lambda$, wenn:
$$(A - \lambda I)^k v = 0 \quad \text{aber} \quad (A - \lambda I)^{k-1} v \neq 0$$

- Stufe 0: Nullvektor
- Stufe 1: Eigenvektor (im eigentlichen Sinn, wenn $k=1$ und $(A-\lambda I)v = 0$)
- Stufe $\geq 2$: verallgemeinerter Eigenvektor

> **Achtung Notation:** Manchmal wird "Hauptvektor erster Stufe" für den verallgemeinerten Eigenvektor mit $(A-\lambda I)v \neq 0$ aber $(A-\lambda I)^2 v = 0$ verwendet. In der Klausur war $v_4$ so einer.

## 5.4 Minimalpolynom

### Definition
Das **Minimalpolynom** $\mu_A$ ist das normierte Polynom kleinsten Grades mit $\mu_A(A) = 0$.

### Eigenschaften
- $\mu_A$ teilt $\chi_A$ (d.h. $\chi_A = \mu_A \cdot q$ für ein Polynom $q$)
- $\mu_A$ und $\chi_A$ haben **die gleichen** Nullstellen (= Eigenwerte)
- Aus der JNF: $\mu_A(\lambda) = \prod_i (\lambda - \lambda_i)^{s_i}$, wobei $s_i$ = Größe des **größten** Jordan-Blocks zu $\lambda_i$

### Berechnung ohne JNF
1. Probiere Polynome aufsteigenden Grades, die durch $\chi_A$ teilen
2. Teste ob $p(A) = 0$

## 5.5 Satz von Cayley-Hamilton

> **Satz:** Jede Matrix erfüllt ihr eigenes charakteristisches Polynom:
> $$\chi_A(A) = 0$$

### Anwendung (Klausuraufgabe 4!)

**Gegeben:** $A$ diagonalisierbar mit Eigenwerten $\lambda_1 = 0$ und $\lambda_2 = 1$.

**4.1: Minimalpolynom**
$$\mu_A(\lambda) = \lambda(\lambda - 1) = \lambda^2 - \lambda$$

(Da $A$ diagonalisierbar → alle Jordan-Blöcke Größe 1 → Minimalpolynom hat nur einfache Nullstellen)

**4.2: $A^2 = A$**
Cayley-Hamilton: $\chi_A(A) = 0$. Da $\mu_A | \chi_A$ und $\mu_A(A) = 0$:
$$A^2 - A = 0 \implies A^2 = A$$

(Formal: $\mu_A(\lambda) = \lambda^2 - \lambda$, also $\mu_A(A) = A^2 - A = 0$)

**4.3: $A^m = A$ für $m \geq 1$ (Induktion)**

*Induktionsanfang:* $m = 1$: $A^1 = A$ ✓

*Induktionsschritt:* Angenommen $A^m = A$ für ein $m \geq 1$. Dann:
$$A^{m+1} = A^m \cdot A = A \cdot A = A^2 = A$$

(wobei wir im letzten Schritt $A^2 = A$ aus 4.2 verwenden)

Also gilt $A^{m+1} = A$. $\square$

**4.4: Matrixexponential**
$$\exp(A) = \sum_{k=0}^{\infty} \frac{A^k}{k!} = \frac{A^0}{0!} + \sum_{k=1}^{\infty} \frac{A^k}{k!}$$

$$= I + \sum_{k=1}^{\infty} \frac{A}{k!} \quad \text{(da } A^k = A \text{ für } k \geq 1\text{)}$$

$$= I + A \sum_{k=1}^{\infty} \frac{1}{k!} = I + A\left(\sum_{k=0}^{\infty} \frac{1}{k!} - 1\right) = I + A(e - 1)$$

$$\boxed{\exp(A) = I + (e-1)A}$$

## 5.6 Matrixexponential – Allgemein

### Definition
$$\exp(A) = \sum_{k=0}^{\infty} \frac{A^k}{k!} = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots$$

### Rechenregeln
- $\exp(0) = I$
- Wenn $AB = BA$: $\exp(A+B) = \exp(A)\exp(B)$
- $\exp(A)$ ist **immer** invertierbar mit $\exp(A)^{-1} = \exp(-A)$
- $\det(\exp(A)) = e^{\text{Spur}(A)}$

### Für Diagonalmatrizen
$$\exp\left(\begin{pmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{pmatrix}\right) = \begin{pmatrix} e^{\lambda_1} & & \\ & \ddots & \\ & & e^{\lambda_n} \end{pmatrix}$$

### Anwendung: DGL
Die Lösung von $\dot{x}(t) = Ax(t)$ mit $x(0) = x_0$ ist:
$$x(t) = \exp(tA) \cdot x_0$$
