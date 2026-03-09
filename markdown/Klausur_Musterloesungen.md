# Klausur-Musterlösungen – Vollständige Lösungen der Erstklausur

> Diese Lösungen zeigen den **idealen Lösungsweg** mit allen Begründungen, die in der Klausur erwartet werden. Vergleiche mit deinen eigenen Lösungsversuchen!

---

## Aufgabe 1: Jordan-Normalform (30 Punkte)

**Gegeben:**
$$J = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & -1 & 1 & 0 \\ 0 & 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0 & -1 \end{pmatrix}, \quad V = (v_1 | v_2 | v_3 | v_4 | v_5), \quad A = VJV^{-1}$$

**Blockstruktur von $J$:**
- $J_1(1)$: Zeile/Spalte 1 (Eigenwert 1, Größe 1)
- $J_1(1)$: Zeile/Spalte 2 (Eigenwert 1, Größe 1)
- $J_2(-1)$: Zeilen/Spalten 3-4 (Eigenwert -1, Größe 2)
- $J_1(-1)$: Zeile/Spalte 5 (Eigenwert -1, Größe 1)

---

### 1.1 Charakteristisches Polynom (ohne Begründung)

$$\boxed{\chi_A(\lambda) = (\lambda - 1)^2 (\lambda + 1)^3}$$

*Direkt aus der JNF: alg. VF(1) = 2 (zwei 1×1-Blöcke), alg. VF(-1) = 3 (ein 2×2-Block + ein 1×1-Block).*

---

### 1.2 Minimalpolynom (mit Begründung)

$$\boxed{\mu_A(\lambda) = (\lambda - 1)(\lambda + 1)^2}$$

**Begründung:** Das Minimalpolynom ergibt sich aus den **größten** Jordan-Blöcken zu jedem Eigenwert:
- Größter Block zu EW 1: Größe 1 → Faktor $(\lambda - 1)^1$
- Größter Block zu EW -1: Größe 2 → Faktor $(\lambda + 1)^2$

Also $\mu_A(\lambda) = (\lambda - 1)(\lambda + 1)^2$.

---

### 1.3 Eigenraum zum Eigenwert -1 (mit Begründung)

$$\boxed{E_{-1} = \text{span}(v_3, v_5)}$$

**Begründung:** Aus $AV = VJ$ (spaltenweise) ergibt sich:
- Spalte 3: $Av_3 = -1 \cdot v_3$ (da $J$ in Spalte 3 den Diagonaleintrag -1 hat und kein "1" links davon). → $v_3$ ist Eigenvektor zu -1.
- Spalte 4: $Av_4 = v_3 + (-1)v_4 = v_3 - v_4 \neq -v_4$. → $v_4$ ist **kein** Eigenvektor (sondern Hauptvektor).
- Spalte 5: $Av_5 = -1 \cdot v_5$. → $v_5$ ist Eigenvektor zu -1.

Da $V$ invertierbar ist, sind $v_1, \ldots, v_5$ linear unabhängig. Insbesondere sind $v_3, v_5$ linear unabhängig und bilden eine Basis von $E_{-1}$.

---

### 1.4 Geometrische Vielfachheiten (mit Begründung)

$$\boxed{\text{geo. VF}(1) = 2, \quad \text{geo. VF}(-1) = 2}$$

**Begründung:**
- **EW 1:** Es gibt 2 Jordan-Blöcke zu EW 1 (beide Größe 1). Die geometrische Vielfachheit = Anzahl der Blöcke = 2. Eigenvektoren: $v_1, v_2$.
- **EW -1:** Es gibt 2 Jordan-Blöcke zu EW -1 (Größe 2 und 1). Die geometrische Vielfachheit = Anzahl der Blöcke = 2. Eigenvektoren: $v_3, v_5$.

---

### 1.5 Hauptvektor erster Stufe (ohne Begründung)

$$\boxed{v_4}$$

$v_4$ ist ein Hauptvektor der Stufe 2 zum Eigenwert -1 (manchmal auch "verallgemeinerter Eigenvektor 1. Stufe" genannt), da $(A+I)v_4 = v_3 \neq 0$, aber $(A+I)^2 v_4 = (A+I)v_3 = 0$.

---

### 1.6 Determinante (mit Berechnung)

$$\boxed{\det(A) = -1}$$

**Berechnung:**

$$\det(A) = \det(VJV^{-1}) = \det(V) \cdot \det(J) \cdot \det(V^{-1})$$
$$= \det(V) \cdot \det(J) \cdot \frac{1}{\det(V)} = \det(J)$$

$J$ ist eine obere Dreiecksmatrix, also:
$$\det(J) = 1 \cdot 1 \cdot (-1) \cdot (-1) \cdot (-1) = -1$$

---

### 1.7 Volumentreu? (mit Begründung)

$$\boxed{\text{Ja, } A \text{ ist volumentreu.}}$$

**Begründung:** Eine lineare Abbildung ist volumentreu genau dann, wenn $|\det(A)| = 1$. Es gilt $|\det(A)| = |-1| = 1$. ✓

---

### 1.8 Orientierungserhaltend? (mit Begründung)

$$\boxed{\text{Nein, } A \text{ ist nicht orientierungserhaltend.}}$$

**Begründung:** Eine lineare Abbildung ist orientierungserhaltend genau dann, wenn $\det(A) > 0$. Es gilt $\det(A) = -1 < 0$. ✗

---

### 1.9 Kann $A$ symmetrisch sein? (mit Begründung)

$$\boxed{\text{Nein.}}$$

**Begründung (Widerspruchsbeweis):** Angenommen, $A$ wäre symmetrisch ($A = A^T$). Dann wäre $A$ nach dem **Spektralsatz** orthogonal diagonalisierbar, d.h. alle Jordan-Blöcke hätten Größe 1 (die JNF wäre eine Diagonalmatrix). Aber $J$ enthält den Jordan-Block $J_2(-1)$ der Größe 2. **Widerspruch!** Also kann $A$ nicht symmetrisch sein.

---

## Aufgabe 2: Bedeutung von Eigenwerten (20 Punkte)

### 2.1 Zeige: $Mv_i = \lambda_i v_i$ (ca. 10 Punkte)

**Gegeben:** ONS $v_1, v_2, v_3 \in \mathbb{R}^n$ (bzgl. Standard-SP), $M = \lambda_1 v_1 v_1^T + \lambda_2 v_2 v_2^T + \lambda_3 v_3 v_3^T$.

**Beweis:** Wir zeigen $Mv_i = \lambda_i v_i$ für $i \in \{1, 2, 3\}$.

Sei $i \in \{1, 2, 3\}$ beliebig. Dann:

$$Mv_i = \left(\lambda_1 v_1 v_1^T + \lambda_2 v_2 v_2^T + \lambda_3 v_3 v_3^T\right) v_i$$

$$= \lambda_1 v_1 (v_1^T v_i) + \lambda_2 v_2 (v_2^T v_i) + \lambda_3 v_3 (v_3^T v_i)$$

Da $v_1, v_2, v_3$ ein **Orthonormalsystem** bilden, gilt:

$$v_j^T v_i = \langle v_j | v_i \rangle = \delta_{ji} = \begin{cases} 1 & \text{falls } j = i \\ 0 & \text{falls } j \neq i \end{cases}$$

Einsetzen:

$$Mv_i = \lambda_1 v_1 \cdot \delta_{1i} + \lambda_2 v_2 \cdot \delta_{2i} + \lambda_3 v_3 \cdot \delta_{3i} = \lambda_i v_i$$

Also ist $v_i$ Eigenvektor von $M$ zum Eigenwert $\lambda_i$ für $i = 1, 2, 3$. $\square$

---

### 2.2 Defekt bei EW $\lambda = 0$ (ca. 10 Punkte)

**Gegeben:** $A$ hat den Eigenwert $\lambda = 0$ mit algebraischer Vielfachheit $m \geq 1$.

**Behauptung:** Der Defekt (= Dimension des Kerns) von $A$ hat die Schranken:

$$\boxed{1 \leq \text{Defekt}(A) \leq m}$$

**Begründung:**

$$\text{Defekt}(A) = \dim(\ker(A)) = \dim(\ker(A - 0 \cdot I)) = \text{geo. VF}(0)$$

Für die geometrische Vielfachheit eines jeden Eigenwerts gilt die fundamentale Ungleichung:

$$1 \leq \text{geo. VF}(\lambda) \leq \text{alg. VF}(\lambda)$$

Mit $\lambda = 0$ und alg. VF$(0) = m$:

$$1 \leq \text{Defekt}(A) \leq m$$

Die untere Schranke gilt, weil $\lambda = 0$ ein Eigenwert ist, also existiert mindestens ein Eigenvektor $v \neq 0$ mit $Av = 0$, d.h. $\ker(A) \neq \{0\}$.

Die obere Schranke folgt aus der fundamentalen Ungleichung geo. VF $\leq$ alg. VF.

**Genauere Angaben über den Rang:**
$$\text{Rang}(A) = n - \text{Defekt}(A)$$

Also: $n - m \leq \text{Rang}(A) \leq n - 1$.

$\square$

---

## Aufgabe 3: Gram-Schmidt-Verfahren (30 Punkte)

**Gegeben:** $f_1(x) = 1$, $f_2(x) = ix$ auf $[0,1]$  
**Skalarprodukt:** $\langle f | g \rangle = \int_0^1 \overline{f(x)} \, g(x) \, dx$

**Gesucht:** ONB von $V = \text{span}(f_1, f_2)$.

---

**Schritt 1: Normierung von $f_1$**

$$\|f_1\|^2 = \langle f_1 | f_1 \rangle = \int_0^1 \overline{1} \cdot 1 \, dx = \int_0^1 1 \, dx = [x]_0^1 = 1$$

$$\|f_1\| = 1$$

$$\boxed{e_1(x) = 1}$$

---

**Schritt 2: Berechnung von $\langle e_1 | f_2 \rangle$**

$$\langle e_1 | f_2 \rangle = \int_0^1 \overline{1} \cdot ix \, dx = i \int_0^1 x \, dx = i \left[\frac{x^2}{2}\right]_0^1 = \frac{i}{2}$$

---

**Schritt 3: Orthogonalisierung**

$$\tilde{e}_2(x) = f_2(x) - \langle e_1 | f_2 \rangle \cdot e_1(x) = ix - \frac{i}{2} \cdot 1 = i\left(x - \frac{1}{2}\right)$$

**Interpretation:** Wir subtrahieren die Komponente von $f_2$ in Richtung $e_1$. Das Ergebnis $\tilde{e}_2$ steht senkrecht auf $e_1$.

---

**Schritt 4: Normierung von $\tilde{e}_2$**

$$\|\tilde{e}_2\|^2 = \int_0^1 \overline{i(x - \tfrac{1}{2})} \cdot i(x - \tfrac{1}{2}) \, dx$$

Da $\overline{i} = -i$:

$$= \int_0^1 (-i)(x - \tfrac{1}{2}) \cdot i(x - \tfrac{1}{2}) \, dx = \int_0^1 \underbrace{(-i)(i)}_{= -i^2 = 1}(x - \tfrac{1}{2})^2 \, dx$$

$$= \int_0^1 (x - \tfrac{1}{2})^2 \, dx$$

Substitution $u = x - \frac{1}{2}$:

$$= \int_{-1/2}^{1/2} u^2 \, du = \left[\frac{u^3}{3}\right]_{-1/2}^{1/2} = \frac{1}{24} - \left(-\frac{1}{24}\right) = \frac{1}{12}$$

$$\|\tilde{e}_2\| = \frac{1}{\sqrt{12}} = \frac{1}{2\sqrt{3}} = \frac{\sqrt{3}}{6}$$

---

**Schritt 5: Ergebnis**

$$\boxed{e_1(x) = 1}$$

$$\boxed{e_2(x) = \frac{\tilde{e}_2}{\|\tilde{e}_2\|} = 2\sqrt{3} \cdot i\left(x - \frac{1}{2}\right)}$$

---

**Probe:$\langle e_1 | e_2 \rangle = 0$?**

$$\langle e_1 | e_2 \rangle = \int_0^1 \overline{1} \cdot 2\sqrt{3} \, i(x - \tfrac{1}{2}) \, dx = 2\sqrt{3} i \int_0^1 (x - \tfrac{1}{2}) \, dx$$

$$= 2\sqrt{3} i \left[\frac{x^2}{2} - \frac{x}{2}\right]_0^1 = 2\sqrt{3} i \left(\frac{1}{2} - \frac{1}{2}\right) = 0 \quad ✓$$

**Probe: $\|e_2\| = 1$?**

$$\|e_2\|^2 = (2\sqrt{3})^2 \cdot \frac{1}{12} = 12 \cdot \frac{1}{12} = 1 \quad ✓$$

---

## Aufgabe 4: Matrixexponential (20 Punkte)

**Gegeben:** $A \in \mathbb{R}^{n \times n}$ diagonalisierbar mit Eigenwerten $\lambda_1 = 0$ und $\lambda_2 = 1$.

---

### 4.1 Minimalpolynom (ohne Begründung)

$$\boxed{\mu_A(\lambda) = \lambda(\lambda - 1) = \lambda^2 - \lambda}$$

*Da $A$ diagonalisierbar, hat das Minimalpolynom nur einfache Nullstellen. Die Nullstellen sind die Eigenwerte 0 und 1.*

---

### 4.2 $A^2 = A$ (mit Beweis über Cayley-Hamilton)

**Zu zeigen:** $A^2 = A$

**Beweis:** Nach dem **Satz von Cayley-Hamilton** erfüllt jede Matrix ihr Minimalpolynom (und auch ihr charakteristisches Polynom):

$$\mu_A(A) = A^2 - A = 0$$

Umstellen: $A^2 = A$. $\square$

> **Alternativ (ohne Cayley-Hamilton, über Diagonalisierung):**
> Da $A$ diagonalisierbar, existiert $S$ mit $A = S \text{diag}(\lambda_1, \ldots, \lambda_n) S^{-1}$, wobei $\lambda_i \in \{0, 1\}$.
> Dann $A^2 = S \text{diag}(\lambda_1^2, \ldots, \lambda_n^2) S^{-1}$.
> Da $0^2 = 0$ und $1^2 = 1$: $\lambda_i^2 = \lambda_i$ für alle $i$. Also $A^2 = A$.

---

### 4.3 $A^m = A$ für $m \geq 1$ (Induktionsbeweis)

**Beweis durch vollständige Induktion über $m$:**

**Induktionsanfang ($m = 1$):**
$$A^1 = A \quad ✓$$

**Induktionsvoraussetzung:** Für ein festes $m \geq 1$ gelte $A^m = A$.

**Induktionsschritt ($m \to m + 1$):**
$$A^{m+1} = A^m \cdot A \overset{\text{IV}}{=} A \cdot A = A^2 \overset{4.2}{=} A$$

Also gilt $A^{m+1} = A$, und nach dem Prinzip der vollständigen Induktion gilt $A^m = A$ für alle $m \geq 1$. $\square$

---

### 4.4 $\exp(A) = I + (e-1)A$ (mit Beweis)

**Beweis:**

Per Definition des Matrixexponentials:

$$\exp(A) = \sum_{k=0}^{\infty} \frac{A^k}{k!}$$

Wir separieren den Term $k = 0$:

$$= \frac{A^0}{0!} + \sum_{k=1}^{\infty} \frac{A^k}{k!} = I + \sum_{k=1}^{\infty} \frac{A^k}{k!}$$

Nach **Aufgabe 4.3** gilt $A^k = A$ für alle $k \geq 1$. Einsetzen:

$$= I + \sum_{k=1}^{\infty} \frac{A}{k!} = I + A \cdot \sum_{k=1}^{\infty} \frac{1}{k!}$$

Die verbleibende Reihe ist die Exponentialreihe minus 1:

$$\sum_{k=1}^{\infty} \frac{1}{k!} = \left(\sum_{k=0}^{\infty} \frac{1}{k!}\right) - \frac{1}{0!} = e - 1$$

Einsetzen:

$$\exp(A) = I + A(e - 1) = I + (e-1)A$$

$$\boxed{\exp(A) = I + (e-1)A} \quad \square$$

---

## Punkteverteilung – Was du beim nächsten Mal holen musst

| Aufgabe | Erstklausur | Ziel Nachklausur | Strategie |
|---------|-------------|------------------|-----------|
| 1 (JNF) | 19/30 | **25/30** | 1.1 und 1.5 nicht mehr vergessen, Begründungen sauber |
| 2 (Eigenwerte) | 1/20 | **15/20** | ONS-Trick lernen, Defekt-Formel auswendig |
| 3 (GS) | 14/30 | **25/30** | Komplexes SP-Integral korrekt berechnen |
| 4 (Exp) | 4/20 | **16/20** | Cayley-Hamilton anwenden, Induktion sauber |
| **Gesamt** | **38/100** | **81/100** | |

> **Realistisches Ziel:** 55-65 Punkte. Damit sicher bestanden.
> **Fokus:** Die leichteren Teilaufgaben (1.1, 1.5, 1.6-1.9, 2.1, 4.1-4.3) bringen ~40 Punkte und sind mit Verständnis machbar!
