# 🏆 Finale Probeklausur – LINA2 Nachklausur

> [!INFO] Über diese Klausur
> Diese **Abschluss-Probeklausur** wurde als Generalprobe vor der echten Klausur konzipiert. Sie kombiniert alle wichtigen Themenbereiche: Rechnen in verschiedenen Körpern, Beweistechniken (Widerspruch, Induktion), Verfahren zum Durchrechnen und Matrixpotenzen. **100 Punkte, 120 Minuten.** Löse alles auf Papier, bevor du die Lösungen aufklappst!

---

---

# Aufgabenpaket 1: Matrix-Eigenschaften über verschiedenen Körpern (25 Punkte)

*Wie verändert sich das Verhalten einer Matrix, wenn man den Grundkörper wechselt?*

Gegeben sei die Matrix mit ganzzahligen Einträgen:

$$A = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 3 & 4 & 0 & 0 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 3 & 1 \end{pmatrix}$$

---

## 1.1 Determinante und Invertierbarkeit (5P)

Berechnen Sie $\det(A)$ über $\mathbb{Z}$. Bestimmen Sie anschließend, ob $A$ über $\mathbb{F}_5$ bzw. über $\mathbb{F}_7$ invertierbar ist.

<details>
<summary><b>Lösung einblenden</b></summary>

$A$ ist eine Blockdiagonalmatrix, daher:
$$\det(A) = \det\begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix} \cdot \det\begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}$$

$$= (2 \cdot 4 - 1 \cdot 3) \cdot (1 \cdot 1 - 2 \cdot 3) = 5 \cdot (-5) = -25$$

- **Über $\mathbb{F}_5$:** $\det(A) = -25 \equiv 0 \pmod{5}$. **Nicht invertierbar!** ✗
- **Über $\mathbb{F}_7$:** $\det(A) = -25 \equiv -25 + 28 = 3 \pmod{7}$. Da $3 \neq 0$: **Invertierbar!** ✓

> **Merke:** Ein und dieselbe Matrix kann in einem Körper invertierbar sein und im anderen nicht!
</details>

---

## 1.2 Charakteristisches Polynom über $\mathbb{F}_5$ (8P)

Bestimmen Sie das charakteristische Polynom $\chi_A(\lambda)$ über $\mathbb{F}_5$ und faktorisieren Sie es vollständig in Linearfaktoren (falls möglich).

<details>
<summary><b>Lösung einblenden</b></summary>

Wegen der Blockstruktur berechnen wir die char. Polynome der 2×2-Blöcke separat.

**Oberer Block** $B_1 = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}$:

$$\chi_{B_1}(\lambda) = (2-\lambda)(4-\lambda) - 1 \cdot 3 = \lambda^2 - 6\lambda + 8 - 3 = \lambda^2 - 6\lambda + 5$$

Über $\mathbb{F}_5$: $\lambda^2 - 6\lambda + 5 \equiv \lambda^2 - \lambda + 0 \equiv \lambda(\lambda - 1) \pmod{5}$

**Unterer Block** $B_2 = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}$:

$$\chi_{B_2}(\lambda) = (1-\lambda)^2 - 2 \cdot 3 = \lambda^2 - 2\lambda + 1 - 6 = \lambda^2 - 2\lambda - 5$$

Über $\mathbb{F}_5$: $\lambda^2 - 2\lambda - 5 \equiv \lambda^2 - 2\lambda \equiv \lambda(\lambda - 2) \pmod{5}$

**Gesamtes char. Polynom über $\mathbb{F}_5$:**

$$\boxed{\chi_A(\lambda) = \lambda(\lambda - 1) \cdot \lambda(\lambda - 2) = \lambda^2(\lambda - 1)(\lambda - 2)}$$

Das Polynom zerfällt vollständig in Linearfaktoren über $\mathbb{F}_5$.
</details>

---

## 1.3 Eigenwerte über $\mathbb{F}_5$ vs. $\mathbb{F}_7$ (6P)

**(a)** Geben Sie über $\mathbb{F}_5$ alle Eigenwerte mit algebraischer Vielfachheit an.

**(b)** Bestimmen Sie die Eigenwerte über $\mathbb{F}_7$. Warum hat $A$ über $\mathbb{F}_7$ weniger Eigenwerte?

<details>
<summary><b>Lösung einblenden</b></summary>

**(a) Eigenwerte über $\mathbb{F}_5$:**

Aus dem char. Polynom $\lambda^2(\lambda-1)(\lambda-2)$:

| Eigenwert | alg. VF |
|-----------|---------|
| $\lambda = 0$ | 2 |
| $\lambda = 1$ | 1 |
| $\lambda = 2$ | 1 |

---

**(b) Eigenwerte über $\mathbb{F}_7$:**

**Oberer Block:** $\chi_{B_1}(\lambda) = \lambda^2 - 6\lambda + 5 \pmod{7}$.

Nullstellen suchen: $\lambda = 1$: $1 - 6 + 5 = 0$ ✓. $\lambda = 5$: $25 - 30 + 5 = 0$ ✓.

Also $\chi_{B_1} = (\lambda - 1)(\lambda - 5)$ über $\mathbb{F}_7$.

**Unterer Block:** $\chi_{B_2}(\lambda) = \lambda^2 - 2\lambda - 5 \equiv \lambda^2 - 2\lambda + 2 \pmod{7}$.

Diskriminante: $\Delta = 4 - 8 = -4 \equiv 3 \pmod{7}$.

Ist $3$ ein Quadrat in $\mathbb{F}_7$? Prüfe: $1^2 = 1$, $2^2 = 4$, $3^2 = 2$, $4^2 = 2$, $5^2 = 4$, $6^2 = 1$.

Die Quadrate in $\mathbb{F}_7$ sind $\{0, 1, 2, 4\}$. Da $3 \notin \{0,1,2,4\}$: **$3$ ist kein Quadrat in $\mathbb{F}_7$!**

$\Rightarrow$ $\lambda^2 - 2\lambda + 2$ ist **irreduzibel** über $\mathbb{F}_7$ (hat keine Nullstelle).

| Eigenwert | alg. VF |
|-----------|---------|
| $\lambda = 1$ | 1 |
| $\lambda = 5$ | 1 |

$$\chi_A(\lambda) = (\lambda - 1)(\lambda - 5) \underbrace{(\lambda^2 - 2\lambda + 2)}_{\text{irreduzibel über } \mathbb{F}_7}$$

$A$ hat über $\mathbb{F}_7$ **nur 2 Eigenwerte** (statt 3 über $\mathbb{F}_5$), weil der Faktor $\lambda^2 - 2\lambda + 2$ über $\mathbb{F}_7$ nicht in Linearfaktoren zerfällt – seine Diskriminante ist kein quadratischer Rest modulo 7.
</details>

---

## 1.4 Kern über $\mathbb{F}_5$ (3P)

Bestimmen Sie über $\mathbb{F}_5$ eine Basis von $\ker(A)$.

<details>
<summary><b>Lösung einblenden</b></summary>

Wegen der Blockstruktur lösen wir $B_1 x_{12} = 0$ und $B_2 x_{34} = 0$ getrennt.

**Oberer Block** über $\mathbb{F}_5$: $\begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 0$

$Z_1 \cdot 2^{-1}=3$: $(1, 3)$. Dann $Z_2 - 3Z_1$: $(0, 4-9) = (0, -5) = (0, 0)$.

$\Rightarrow x_1 + 3x_2 = 0 \Rightarrow x_1 = -3x_2 = 2x_2$ in $\mathbb{F}_5$.

Basisvektor: $(2, 1)^T$.

**Unterer Block** über $\mathbb{F}_5$: $\begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} x_3 \\ x_4 \end{pmatrix} = 0$

$Z_2 - 3Z_1$: $(0, 1-6) = (0, -5) = (0, 0)$.

$\Rightarrow x_3 + 2x_4 = 0 \Rightarrow x_3 = -2x_4 = 3x_4$ in $\mathbb{F}_5$.

Basisvektor: $(3, 1)^T$.

$$\boxed{\ker(A) = \text{span}\left\{ \begin{pmatrix} 2 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 3 \\ 1 \end{pmatrix} \right\}, \quad \dim(\ker A) = 2}$$

**Probe:** $\dim(\ker A) = 2 =$ alg. VF des Eigenwerts $0$ ✓ (konsistent mit Diagonalisierbarkeit)
</details>

---

## 1.5 Diagonalisierbarkeit (3P)

Entscheiden und begründen Sie: Ist $A$ über $\mathbb{F}_5$ diagonalisierbar? Ist $A$ über $\mathbb{F}_7$ diagonalisierbar?

<details>
<summary><b>Lösung einblenden</b></summary>

**Über $\mathbb{F}_5$: Ja, $A$ ist diagonalisierbar!**

Begründung: geo. VF = alg. VF für **alle** Eigenwerte:
- $\lambda = 0$: alg. VF $= 2$, geo. VF $= \dim(\ker A) = 2$ ✓
- $\lambda = 1$: alg. VF $= 1$, also automatisch geo. VF $= 1$ ✓
- $\lambda = 2$: alg. VF $= 1$, also automatisch geo. VF $= 1$ ✓

Die JNF über $\mathbb{F}_5$ wäre: $\text{diag}(0, 0, 1, 2)$.

---

**Über $\mathbb{F}_7$: Nein, $A$ ist NICHT diagonalisierbar!**

Begründung: Das char. Polynom $(\lambda-1)(\lambda-5)(\lambda^2-2\lambda+2)$ zerfällt über $\mathbb{F}_7$ **nicht** vollständig in Linearfaktoren. Eine Matrix ist nur dann diagonalisierbar, wenn eine Basis aus Eigenvektoren existiert. Da der irreduzible quadratische Faktor keine Nullstellen in $\mathbb{F}_7$ hat, liefert der untere $2 \times 2$-Block keine Eigenvektoren. Es gibt nur 2 Eigenvektoren für eine $4 \times 4$-Matrix – zu wenig.

> **Fazit:** Über $\mathbb{F}_5$ ist $A$ **nicht invertierbar, aber diagonalisierbar**. Über $\mathbb{F}_7$ ist $A$ **invertierbar, aber nicht diagonalisierbar**. Der Körper bestimmt alles!
</details>

---

---

# Aufgabenpaket 2: Beweis – Matrixgleichung, Eigenwerte & Invertierbarkeit (25 Punkte)

*Beweistechniken: Widerspruchsbeweis, Minimalpolynom, Diagonalisierbarkeit*

Sei $A \in \mathbb{R}^{n \times n}$ eine Matrix, die die Gleichung

$$A^2 - 5A + 6I = 0$$

erfüllt (wobei $I$ die Einheitsmatrix und $0$ die Nullmatrix ist).

---

## 2.1 Mögliche Eigenwerte bestimmen (5P)

Bestimmen Sie alle Eigenwerte, die $A$ haben kann.

<details>
<summary><b>Lösung einblenden</b></summary>

Sei $\lambda$ ein Eigenwert von $A$ mit Eigenvektor $v \neq 0$, also $Av = \lambda v$.

Wir wenden die Matrixgleichung auf $v$ an:

$$(A^2 - 5A + 6I)v = 0$$

$$A^2 v - 5Av + 6v = 0$$

$$\lambda^2 v - 5\lambda v + 6v = 0$$

$$(\lambda^2 - 5\lambda + 6) v = 0$$

Da $v \neq 0$, folgt:

$$\lambda^2 - 5\lambda + 6 = 0$$

$$(\lambda - 2)(\lambda - 3) = 0$$

$$\boxed{\lambda \in \{2, 3\}}$$

Die einzig möglichen Eigenwerte von $A$ sind $2$ und $3$.
</details>

---

## 2.2 Widerspruchsbeweis: $A$ ist invertierbar (8P)

Zeigen Sie per **Widerspruchsbeweis**, dass $A$ invertierbar ist.

<details>
<summary><b>Lösung einblenden</b></summary>

**Beweis (Widerspruch):**

**Annahme:** $A$ ist **nicht** invertierbar.

Dann ist $\det(A) = 0$, was gleichbedeutend damit ist, dass $\lambda = 0$ ein Eigenwert von $A$ ist (denn $A$ hat nichttrivialen Kern, d.h. es existiert $v \neq 0$ mit $Av = 0 \cdot v$).

Aber aus Aufgabe 2.1 wissen wir: Die einzig möglichen Eigenwerte sind $\lambda \in \{2, 3\}$.

Da $0 \notin \{2, 3\}$, kann $\lambda = 0$ **kein** Eigenwert von $A$ sein.

**Widerspruch!** ↯

Also war unsere Annahme falsch, und $A$ **ist invertierbar**. $\square$

---

**Alternativ (direkt):** Aus $A^2 - 5A + 6I = 0$ folgt $6I = 5A - A^2 = A(5I - A)$, also

$$A \cdot \frac{5I - A}{6} = I$$

Damit ist $A^{-1} = \frac{5I - A}{6}$ explizit angegeben und $A$ ist invertierbar. (Dies wird in 2.4 vertieft.)
</details>

---

## 2.3 Diagonalisierbarkeit zeigen (5P)

Zeigen Sie: $A$ ist diagonalisierbar.

<details>
<summary><b>Lösung einblenden</b></summary>

**Beweis:**

Aus der Matrixgleichung $A^2 - 5A + 6I = 0$ folgt, dass das Polynom

$$p(\lambda) = \lambda^2 - 5\lambda + 6 = (\lambda - 2)(\lambda - 3)$$

die Matrix $A$ annulliert: $p(A) = 0$.

Das **Minimalpolynom** $\mu_A$ ist definiert als das normierte Polynom kleinsten Grades, das $A$ annulliert. Per Definition gilt: $\mu_A$ **teilt** jedes Polynom, das $A$ annulliert.

Also teilt $\mu_A$ das Polynom $p(\lambda) = (\lambda - 2)(\lambda - 3)$.

Die Teiler von $(\lambda-2)(\lambda-3)$ sind:
- $(\lambda - 2)$
- $(\lambda - 3)$
- $(\lambda - 2)(\lambda - 3)$

In **allen** Fällen hat $\mu_A$ nur **einfache** Nullstellen (keine Nullstelle mit Vielfachheit $\geq 2$).

**Satz:** Eine Matrix ist genau dann diagonalisierbar, wenn ihr Minimalpolynom nur einfache Nullstellen hat (d.h. in paarweise verschiedene Linearfaktoren zerfällt).

$\Rightarrow$ $A$ ist diagonalisierbar. $\square$
</details>

---

## 2.4 Inverse als Linearkombination (7P)

Bestimmen Sie $A^{-1}$ als Linearkombination von $A$ und $I$. Verifizieren Sie Ihr Ergebnis.

<details>
<summary><b>Lösung einblenden</b></summary>

Aus der Matrixgleichung $A^2 - 5A + 6I = 0$ formen wir um:

$$A^2 - 5A = -6I$$

$$A(A - 5I) = -6I$$

$$A \cdot \frac{-(A - 5I)}{6} = I$$

$$A \cdot \frac{5I - A}{6} = I$$

Also:

$$\boxed{A^{-1} = \frac{1}{6}(5I - A)}$$

---

**Verifikation:**

$$A \cdot A^{-1} = A \cdot \frac{5I - A}{6} = \frac{5A - A^2}{6} = \frac{5A - (5A - 6I)}{6} = \frac{6I}{6} = I \quad ✓$$

Dabei haben wir $A^2 = 5A - 6I$ (umgestellt aus der Matrixgleichung) verwendet.

---

**Zahlenbeispiel zur Kontrolle:** Sei $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$. Dann ist $A^2 - 5A + 6I = \begin{pmatrix} 4 & 0 \\ 0 & 9 \end{pmatrix} - \begin{pmatrix} 10 & 0 \\ 0 & 15 \end{pmatrix} + \begin{pmatrix} 6 & 0 \\ 0 & 6 \end{pmatrix} = 0$ ✓

$A^{-1} = \frac{1}{6}\begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1/2 & 0 \\ 0 & 1/3 \end{pmatrix}$ ✓
</details>

---

---

# Aufgabenpaket 3: Verfahren — Gram-Schmidt mit komplexem Skalarprodukt & Projektion (25 Punkte)

*Rechnung Schritt für Schritt mit Konjugation im 1. Argument*

Gegeben seien die Vektoren in $\mathbb{C}^3$:

$$v_1 = \begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix}, \qquad v_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$

mit dem Standard-Skalarprodukt $\langle x | y \rangle = \bar{x}^T y = \sum_k \overline{x_k} \, y_k$ (konjugiert-linear im **ersten** Argument).

---

## 3.1 Gram-Schmidt: Orthonormalisierung (12P)

Orthonormalisieren Sie $\{v_1, v_2\}$ mit dem Gram-Schmidt-Verfahren. Zeigen Sie jeden Zwischenschritt.

<details>
<summary><b>Lösung einblenden</b></summary>

### Schritt 1: Normierung von $v_1$

$$\|v_1\|^2 = \langle v_1 | v_1 \rangle = \overline{1} \cdot 1 + \overline{i} \cdot i + \overline{0} \cdot 0 = 1 + (-i)(i) + 0 = 1 + 1 = 2$$

$$\|v_1\| = \sqrt{2}$$

$$\boxed{e_1 = \frac{v_1}{\|v_1\|} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix}}$$

---

### Schritt 2: Skalarprodukt $\langle e_1 | v_2 \rangle$

$$\langle e_1 | v_2 \rangle = \frac{1}{\sqrt{2}} \left( \overline{1} \cdot 1 + \overline{i} \cdot 0 + \overline{0} \cdot 1 \right) = \frac{1}{\sqrt{2}} (1 + 0 + 0) = \frac{1}{\sqrt{2}}$$

> **Achtung:** Der Faktor $\overline{i} = -i$ taucht hier nicht auf, weil die zweite Komponente von $v_2$ Null ist. Konjugation immer im 1. Argument!

---

### Schritt 3: Orthogonalisierung

$$\tilde{e}_2 = v_2 - \langle e_1 | v_2 \rangle \cdot e_1 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} - \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} - \frac{1}{2}\begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} = \begin{pmatrix} 1/2 \\ -i/2 \\ 1 \end{pmatrix}$$

---

### Schritt 4: Normierung von $\tilde{e}_2$

$$\|\tilde{e}_2\|^2 = |1/2|^2 + |-i/2|^2 + |1|^2 = \frac{1}{4} + \frac{1}{4} + 1 = \frac{3}{2}$$

$$\|\tilde{e}_2\| = \sqrt{3/2} = \frac{\sqrt{6}}{2}$$

$$\boxed{e_2 = \frac{\tilde{e}_2}{\|\tilde{e}_2\|} = \frac{2}{\sqrt{6}} \begin{pmatrix} 1/2 \\ -i/2 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{6}} \begin{pmatrix} 1 \\ -i \\ 2 \end{pmatrix}}$$

---

### Probe: Orthonormalität

$$\langle e_1 | e_2 \rangle = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{6}} \left( \overline{1} \cdot 1 + \overline{i} \cdot (-i) + \overline{0} \cdot 2 \right) = \frac{1}{\sqrt{12}} \left(1 + (-i)(-i)\right) = \frac{1}{\sqrt{12}}(1 + i^2) = \frac{1}{\sqrt{12}}(1 - 1) = 0 \quad ✓$$

$$\|e_1\| = 1 \; ✓, \qquad \|e_2\| = \sqrt{1/6 + 1/6 + 4/6} = \sqrt{6/6} = 1 \; ✓$$

</details>

---

## 3.2 Orthogonale Projektion (8P)

Projizieren Sie den Vektor $w = (1, 1, 1)^T$ orthogonal auf den Unterraum $U = \text{span}(v_1, v_2)$.

<details>
<summary><b>Lösung einblenden</b></summary>

Die orthogonale Projektion auf $U$ bezüglich des ONS $\{e_1, e_2\}$ ist:

$$\text{proj}_U(w) = \langle e_1 | w \rangle \, e_1 + \langle e_2 | w \rangle \, e_2$$

**Berechnung der Koeffizienten:**

$$\langle e_1 | w \rangle = \frac{1}{\sqrt{2}}\left(\overline{1} \cdot 1 + \overline{i} \cdot 1 + \overline{0} \cdot 1\right) = \frac{1}{\sqrt{2}}(1 + (-i)) = \frac{1-i}{\sqrt{2}}$$

$$\langle e_2 | w \rangle = \frac{1}{\sqrt{6}}\left(\overline{1} \cdot 1 + \overline{(-i)} \cdot 1 + \overline{2} \cdot 1\right) = \frac{1}{\sqrt{6}}(1 + i + 2) = \frac{3 + i}{\sqrt{6}}$$

**Einsetzen:**

$$\text{proj}_U(w) = \frac{1-i}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} + \frac{3+i}{\sqrt{6}} \cdot \frac{1}{\sqrt{6}}\begin{pmatrix} 1 \\ -i \\ 2 \end{pmatrix}$$

$$= \frac{1-i}{2}\begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} + \frac{3+i}{6}\begin{pmatrix} 1 \\ -i \\ 2 \end{pmatrix}$$

Erster Summand:

$$\frac{1-i}{2}\begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} = \begin{pmatrix} (1-i)/2 \\ i(1-i)/2 \\ 0 \end{pmatrix} = \begin{pmatrix} (1-i)/2 \\ (i-i^2)/2 \\ 0 \end{pmatrix} = \begin{pmatrix} (1-i)/2 \\ (i+1)/2 \\ 0 \end{pmatrix}$$

Zweiter Summand:

$$\frac{3+i}{6}\begin{pmatrix} 1 \\ -i \\ 2 \end{pmatrix} = \begin{pmatrix} (3+i)/6 \\ -i(3+i)/6 \\ (3+i)/3 \end{pmatrix} = \begin{pmatrix} (3+i)/6 \\ (-3i-i^2)/6 \\ (3+i)/3 \end{pmatrix} = \begin{pmatrix} (3+i)/6 \\ (1-3i)/6 \\ (3+i)/3 \end{pmatrix}$$

**Summe** (auf gemeinsamen Nenner 6):

$$\text{proj}_U(w) = \begin{pmatrix} 3(1-i)/6 + (3+i)/6 \\ 3(1+i)/6 + (1-3i)/6 \\ (3+i)/3 \end{pmatrix} = \begin{pmatrix} (3-3i+3+i)/6 \\ (3+3i+1-3i)/6 \\ (3+i)/3 \end{pmatrix}$$

$$\boxed{\text{proj}_U(w) = \begin{pmatrix} (6-2i)/6 \\ 4/6 \\ (3+i)/3 \end{pmatrix} = \begin{pmatrix} (3-i)/3 \\ 2/3 \\ (3+i)/3 \end{pmatrix}}$$

</details>

---

## 3.3 Abstand (5P)

Berechnen Sie den Abstand $d(w, U) = \|w - \text{proj}_U(w)\|$.

<details>
<summary><b>Lösung einblenden</b></summary>

**Residuenvektor:**

$$r = w - \text{proj}_U(w) = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} (3-i)/3 \\ 2/3 \\ (3+i)/3 \end{pmatrix} = \begin{pmatrix} i/3 \\ 1/3 \\ -i/3 \end{pmatrix}$$

**Abstand:**

$$d(w, U)^2 = \|r\|^2 = |i/3|^2 + |1/3|^2 + |-i/3|^2 = \frac{1}{9} + \frac{1}{9} + \frac{1}{9} = \frac{3}{9} = \frac{1}{3}$$

$$\boxed{d(w, U) = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}}$$

**Probe:** $\langle e_1 | r \rangle = 0$ und $\langle e_2 | r \rangle = 0$ (der Residuenvektor steht senkrecht auf $U$).

$\langle e_1 | r \rangle = \frac{1}{\sqrt{2}}(\overline{1} \cdot \frac{i}{3} + \overline{i} \cdot \frac{1}{3} + 0) = \frac{1}{\sqrt{2}}(\frac{i}{3} + \frac{-i}{3}) = 0$ ✓

</details>

---

---

# Aufgabenpaket 4: Matrixpotenzen – Beweis mit vollständiger Induktion (25 Punkte)

*Vermutung aufstellen, beweisen & auf das Matrixexponential anwenden*

Gegeben sei die Matrix:

$$A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$$

---

## 4.1 Potenzen berechnen & Vermutung aufstellen (8P)

Berechnen Sie $A^2$, $A^3$ und $A^4$. Stellen Sie eine Vermutung für die allgemeine Formel $A^n$ auf ($n \geq 1$).

<details>
<summary><b>Lösung einblenden</b></summary>

$$A^2 = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 2^2 & 2 \cdot 2^1 \\ 0 & 2^2 \end{pmatrix}$$

$$A^3 = A^2 \cdot A = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix} = \begin{pmatrix} 2^3 & 3 \cdot 2^2 \\ 0 & 2^3 \end{pmatrix}$$

$$A^4 = A^3 \cdot A = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 16 & 32 \\ 0 & 16 \end{pmatrix} = \begin{pmatrix} 2^4 & 4 \cdot 2^3 \\ 0 & 2^4 \end{pmatrix}$$

**Vermutung:**

$$\boxed{A^n = \begin{pmatrix} 2^n & n \cdot 2^{n-1} \\ 0 & 2^n \end{pmatrix} \quad \text{für alle } n \geq 1}$$

*Muster: In der oberen rechten Ecke steht immer $n \cdot 2^{n-1}$.*
</details>

---

## 4.2 Beweis per vollständiger Induktion (10P)

Beweisen Sie: $A^n = \begin{pmatrix} 2^n & n \cdot 2^{n-1} \\ 0 & 2^n \end{pmatrix}$ für alle $n \geq 1$.

<details>
<summary><b>Lösung einblenden</b></summary>

**Beweis durch vollständige Induktion über $n$:**

---

**Induktionsanfang ($n = 1$):**

$$A^1 = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 2^1 & 1 \cdot 2^0 \\ 0 & 2^1 \end{pmatrix} \quad ✓$$

---

**Induktionsvoraussetzung (IV):** Für ein festes $n \geq 1$ gelte:

$$A^n = \begin{pmatrix} 2^n & n \cdot 2^{n-1} \\ 0 & 2^n \end{pmatrix}$$

---

**Induktionsschritt ($n \to n+1$):**

$$A^{n+1} = A^n \cdot A \overset{\text{IV}}{=} \begin{pmatrix} 2^n & n \cdot 2^{n-1} \\ 0 & 2^n \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$$

Matrixmultiplikation:

$$= \begin{pmatrix} 2^n \cdot 2 + n \cdot 2^{n-1} \cdot 0 & 2^n \cdot 1 + n \cdot 2^{n-1} \cdot 2 \\ 0 \cdot 2 + 2^n \cdot 0 & 0 \cdot 1 + 2^n \cdot 2 \end{pmatrix}$$

$$= \begin{pmatrix} 2^{n+1} & 2^n + n \cdot 2^n \\ 0 & 2^{n+1} \end{pmatrix}$$

Die obere rechte Ecke vereinfacht sich:

$$2^n + n \cdot 2^n = (1 + n) \cdot 2^n = (n+1) \cdot 2^{(n+1)-1}$$

Also:

$$A^{n+1} = \begin{pmatrix} 2^{n+1} & (n+1) \cdot 2^n \\ 0 & 2^{n+1} \end{pmatrix} \quad ✓$$

Dies ist genau die Behauptung für $n+1$.

---

Nach dem Prinzip der vollständigen Induktion gilt die Formel für alle $n \geq 1$. $\square$
</details>

---

## 4.3 Matrixexponential berechnen (5P)

Berechnen Sie $\exp(tA)$ für $t \in \mathbb{R}$.

*Hinweis: Zerlegen Sie $A = D + N$ mit $D$ diagonal und $N$ nilpotent.*

<details>
<summary><b>Lösung einblenden</b></summary>

**Zerlegung:** $A = \underbrace{\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}}_{D \,=\, 2I} + \underbrace{\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}}_{N}$

Da $D = 2I$ ein Vielfaches der Einheitsmatrix ist, gilt $DN = ND$ (trivial). Außerdem:

$$N^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0$$

$N$ ist nilpotent der Ordnung 2.

**Matrixexponential:**

$$\exp(tA) = \exp(tD + tN) = \exp(tD) \cdot \exp(tN)$$

$$\exp(tD) = \exp(2tI) = e^{2t} I = \begin{pmatrix} e^{2t} & 0 \\ 0 & e^{2t} \end{pmatrix}$$

$$\exp(tN) = I + tN + \underbrace{\frac{t^2 N^2}{2!} + \cdots}_{= \; 0} = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$$

$$\boxed{\exp(tA) = e^{2t} \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{2t} & t \cdot e^{2t} \\ 0 & e^{2t} \end{pmatrix}}$$

**Konsistenz-Check mit 4.1:** Für die Potenzreihe $\exp(tA) = \sum \frac{t^n}{n!} A^n$ und $A^n$ aus der bewiesenen Formel muss das Gleiche herauskommen. Die obere rechte Ecke wäre $\sum \frac{t^n}{n!} n \cdot 2^{n-1} = t \sum \frac{(2t)^{n-1}}{(n-1)!} = t \cdot e^{2t}$ ✓
</details>

---

## 4.4 Anwendung: Differentialgleichung lösen (2P)

Lösen Sie das Anfangswertproblem $\dot{y}(t) = Ay(t)$ mit $y(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

<details>
<summary><b>Lösung einblenden</b></summary>

$$y(t) = \exp(tA) \cdot y(0) = \begin{pmatrix} e^{2t} & te^{2t} \\ 0 & e^{2t} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

$$\boxed{y(t) = \begin{pmatrix} (1+t) e^{2t} \\ e^{2t} \end{pmatrix}}$$

**Probe:** $y(0) = (1, 1)^T$ ✓. $\dot{y}(t) = \begin{pmatrix} e^{2t} + 2(1+t)e^{2t} \\ 2e^{2t} \end{pmatrix} = \begin{pmatrix} (3+2t)e^{2t} \\ 2e^{2t} \end{pmatrix}$.

$Ay(t) = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} (1+t)e^{2t} \\ e^{2t} \end{pmatrix} = \begin{pmatrix} (2+2t+1)e^{2t} \\ 2e^{2t} \end{pmatrix} = \begin{pmatrix} (3+2t)e^{2t} \\ 2e^{2t} \end{pmatrix}$ ✓
</details>

---

---

## 🏁 Zusammenfassung & Strategie

| Aufgabenpaket | Punkte | Kernthema | Schwierigkeit |
|---------------|--------|-----------|---------------|
| **AP1:** Körperwechsel | 25 | det, EW, Kern, Diag. über $\mathbb{F}_5$ vs. $\mathbb{F}_7$ | ⚡ Mittel |
| **AP2:** Matrixgleichung | 25 | Widerspruchsbeweis, Minimalpolynom, $A^{-1}$ | ⚡ Mittel |
| **AP3:** Gram-Schmidt komplex | 25 | ONS, Projektion, Abstand (mit $\overline{\phantom{x}}$ im 1. Arg.) | ⚡⚡ Schwer |
| **AP4:** Induktion + exp | 25 | $A^n$-Formel, vollst. Induktion, $e^{tA}$, DGL | ⚡ Mittel |

**Optimale Bearbeitungsreihenfolge:**
1. AP4 zuerst (sichere Punkte bei Induktion, Schema ist immer gleich)
2. AP1 (strukturiert abarbeiten, Blockstruktur ausnutzen)  
3. AP2 (Beweisstruktur üben, Widerspruch klar formulieren)
4. AP3 (Gram-Schmidt sauber durchrechnen, Konjugation nicht vergessen!)

**Mindest-Ziel: 60/100** = bestanden. Realistisch erreichbar durch AP4 komplett + AP1 komplett + Teile von AP2 und AP3.
