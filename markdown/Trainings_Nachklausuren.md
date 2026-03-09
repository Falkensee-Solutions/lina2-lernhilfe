# 🎓 Trainings-Nachklausuren (Neue Version)

> [!INFO] Über diese Klausuren
> Diese 4 Probeklausuren wurden **präzise nach den Hinweisen des Dozenten** zur Nachklausur modelliert. Sie decken exakt die genannten Zusammenhänge, Algorithmen und Beweistechniken ab – mit **anderen Aufgaben** als die Erstklausur. Jede Klausur hat ca. 100 Punkte mit der Verteilung ~1/3 Methoden, ~1/3 Verstehen, ~1/3 Beweisen.
> **Tipp:** Bearbeite jede Aufgabe zuerst auf Papier, bevor du die Lösung aufklappst. Zeitvorgabe: 120 Minuten pro Klausur.

---

---

# 📝 Klausur A — „Die Wahrscheinlichste"

*Schwerpunkte: Körper (Prof-Tipp!), Matrixexponential via D+N, Gram-Schmidt + Projektion, Zusammenhänge*

---

## Aufgabe A1: Rechnen in endlichen Körpern (25 Punkte) — Methoden

### (a) Körper $\mathbb{F}_5$ — Grundoperationen (5P)

Bestimmen Sie im Körper $\mathbb{F}_5 = \{0, 1, 2, 3, 4\}$ (Restklassen modulo 5):

1. $3 + 4 = \;?$
2. $2 \cdot 3 = \;?$
3. Das multiplikative Inverse von $2$, also $2^{-1} = \;?$

<details>
<summary><b>Lösung einblenden</b></summary>

1. $3 + 4 = 7 \equiv 2 \pmod{5}$. **Antwort: $2$**
2. $2 \cdot 3 = 6 \equiv 1 \pmod{5}$. **Antwort: $1$**
3. Wir suchen $x$ mit $2x \equiv 1 \pmod{5}$. Da $2 \cdot 3 = 6 \equiv 1$, ist $2^{-1} = 3$. **Antwort: $3$**
</details>

### (b) Gleichung $ub + a = 0$ im Körper lösen (10P)

Lösen Sie im Körper $\mathbb{F}_5$ die Gleichung $u \cdot b + a = 0$ für $a = 3$ und $b = 4$.

**Gehen Sie exakt nach dem Tipp des Professors vor:**
1. Finden Sie zunächst das additiv Inverse $A$ von $a$, sodass $A + a = 0$.
2. Finden Sie dann $u$ mit $u \cdot b = A$.

<details>
<summary><b>Lösung einblenden</b></summary>

**Schritt 1:** Additiv Inverses von $a = 3$ in $\mathbb{F}_5$:
$A + 3 \equiv 0 \pmod{5}$. Da $2 + 3 = 5 \equiv 0$, ist $A = 2$.

**Schritt 2:** Löse $u \cdot 4 \equiv 2 \pmod{5}$.
Wir brauchen das multiplikativ Inverse von $4$ in $\mathbb{F}_5$:
$4 \cdot 1 = 4$, $4 \cdot 2 = 8 \equiv 3$, $4 \cdot 3 = 12 \equiv 2$, $4 \cdot 4 = 16 \equiv 1$.
Also ist $4^{-1} = 4$.

Multiplikation beider Seiten mit $4$:
$$u = 2 \cdot 4 = 8 \equiv 3 \pmod{5}$$

**Antwort: $u = 3$**

**Probe:** $3 \cdot 4 + 3 = 12 + 3 = 15 \equiv 0 \pmod{5}$ ✓
</details>

### (c) Lineares Gleichungssystem über $\mathbb{F}_5$ (10P)

Lösen Sie über $\mathbb{F}_5$ das LGS:
$$\begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$$

<details>
<summary><b>Lösung einblenden</b></summary>

Gauß-Algorithmus über $\mathbb{F}_5$:

$$\left(\begin{array}{cc|c} 2 & 1 & 4 \\ 3 & 4 & 2 \end{array}\right)$$

**Zeile 1 mit $2^{-1} = 3$ multiplizieren** (in $\mathbb{F}_5$):
$Z_1 \to 3 \cdot Z_1$: $(3 \cdot 2, 3 \cdot 1, 3 \cdot 4) = (6, 3, 12) \equiv (1, 3, 2)$

$$\left(\begin{array}{cc|c} 1 & 3 & 2 \\ 3 & 4 & 2 \end{array}\right)$$

**$Z_2 \to Z_2 - 3 \cdot Z_1$:**
$(3 - 3, 4 - 9, 2 - 6) = (0, -5, -4) \equiv (0, 0, 1)$

$$\left(\begin{array}{cc|c} 1 & 3 & 2 \\ 0 & 0 & 1 \end{array}\right)$$

Zeile 2 besagt $0 = 1$. **Das LGS hat keine Lösung!**

**Alternativ:** $\det(A) = 2 \cdot 4 - 1 \cdot 3 = 8 - 3 = 5 \equiv 0 \pmod{5}$. Die Matrix ist singulär über $\mathbb{F}_5$, daher ist das LGS nicht für jede rechte Seite lösbar.
</details>

---

## Aufgabe A2: Matrixexponential via $D+N$-Zerlegung (25 Punkte) — Methoden

Gegeben sei die Matrix:
$$A = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix}$$

### (a) Zerlegung $A = D + N$ (5P)

Zerlegen Sie $A = D + N$ in einen diagonalen Anteil $D$ und einen nilpotenten Anteil $N$. Verifizieren Sie $DN = ND$.

<details>
<summary><b>Lösung einblenden</b></summary>

$$D = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix} = 3I, \qquad N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

Da $D = 3I$ ein Vielfaches der Einheitsmatrix ist, kommutiert es mit jeder Matrix:
$$DN = 3I \cdot N = 3N = N \cdot 3I = ND \quad ✓$$
</details>

### (b) Nilpotenz von $N$ (5P)

Berechnen Sie $N^2$ und $N^3$. Ab welcher Potenz ist $N^k = 0$?

<details>
<summary><b>Lösung einblenden</b></summary>

$$N^2 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$$N^3 = N^2 \cdot N = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = 0$$

$N$ ist nilpotent der **Ordnung 3**: $N^3 = 0$, aber $N^2 \neq 0$.
</details>

### (c) Berechnung von $\exp(N)$ (7P)

Berechnen Sie $\exp(N)$ mithilfe der Taylorreihe.

<details>
<summary><b>Lösung einblenden</b></summary>

Da $N^k = 0$ für $k \geq 3$, bricht die Taylorreihe ab:

$$\exp(N) = I + N + \frac{N^2}{2!} + \underbrace{\frac{N^3}{3!} + \cdots}_{=0}$$

$$= \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} + \frac{1}{2}\begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$$\boxed{\exp(N) = \begin{pmatrix} 1 & 1 & 1/2 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}}$$
</details>

### (d) Berechnung von $\exp(A)$ (8P)

Berechnen Sie $\exp(A)$.

<details>
<summary><b>Lösung einblenden</b></summary>

Da $DN = ND$, gilt $\exp(A) = \exp(D + N) = \exp(D) \cdot \exp(N)$.

$$\exp(D) = \exp(3I) = e^3 I = \begin{pmatrix} e^3 & 0 & 0 \\ 0 & e^3 & 0 \\ 0 & 0 & e^3 \end{pmatrix}$$

$$\exp(A) = e^3 I \cdot \exp(N) = e^3 \begin{pmatrix} 1 & 1 & 1/2 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$

$$\boxed{\exp(A) = \begin{pmatrix} e^3 & e^3 & e^3/2 \\ 0 & e^3 & e^3 \\ 0 & 0 & e^3 \end{pmatrix}}$$

**DGL-Anwendung:** Die Lösung von $\dot{x}(t) = Ax(t)$ mit Start $x(0) = x_0$ ist $x(t) = e^{tA} x_0$, wobei man überall $e^3$ durch $e^{3t}$ und $1/2$ durch $t^2/2$ und die mittleren Einsen durch $t$ ersetzt.
</details>

---

## Aufgabe A3: Gram-Schmidt, Projektion & Ausgleichsrechnung (30 Punkte) — Methoden

### (a) Gram-Schmidt in $\mathbb{R}^3$ (12P)

Orthonormalisieren Sie die Vektoren $v_1 = (1, 0, 1)^T$ und $v_2 = (1, 1, 0)^T$ bezüglich des Standard-Skalarprodukts mit dem Gram-Schmidt-Verfahren.

<details>
<summary><b>Lösung einblenden</b></summary>

**Schritt 1: Normierung von $v_1$**
$$\|v_1\| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{2}$$
$$e_1 = \frac{v_1}{\|v_1\|} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$

**Schritt 2: Orthogonalisierung von $v_2$**
$$\langle e_1 | v_2 \rangle = \frac{1}{\sqrt{2}}(1 \cdot 1 + 0 \cdot 1 + 1 \cdot 0) = \frac{1}{\sqrt{2}}$$

$$\tilde{e}_2 = v_2 - \langle e_1 | v_2 \rangle \cdot e_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} - \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} - \begin{pmatrix} 1/2 \\ 0 \\ 1/2 \end{pmatrix} = \begin{pmatrix} 1/2 \\ 1 \\ -1/2 \end{pmatrix}$$

**Schritt 3: Normierung**
$$\|\tilde{e}_2\| = \sqrt{1/4 + 1 + 1/4} = \sqrt{3/2} = \frac{\sqrt{6}}{2}$$

$$e_2 = \frac{\tilde{e}_2}{\|\tilde{e}_2\|} = \frac{2}{\sqrt{6}}\begin{pmatrix} 1/2 \\ 1 \\ -1/2 \end{pmatrix} = \frac{1}{\sqrt{6}}\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$$

**Probe:** $\langle e_1 | e_2 \rangle = \frac{1}{\sqrt{12}}(1 \cdot 1 + 0 \cdot 2 + 1 \cdot (-1)) = 0$ ✓

$\|e_1\| = 1$ ✓, $\|e_2\| = \sqrt{1/6 + 4/6 + 1/6} = 1$ ✓
</details>

### (b) Projektionsmatrix (8P)

Berechnen Sie die Projektionsmatrix $P$ auf $U = \text{span}(v_1, v_2)$ als Summe dyadischer Produkte.

<details>
<summary><b>Lösung einblenden</b></summary>

$$P = e_1 e_1^T + e_2 e_2^T$$

$$e_1 e_1^T = \frac{1}{2}\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}(1, 0, 1) = \frac{1}{2}\begin{pmatrix} 1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \end{pmatrix}$$

$$e_2 e_2^T = \frac{1}{6}\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}(1, 2, -1) = \frac{1}{6}\begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & -2 \\ -1 & -2 & 1 \end{pmatrix}$$

$$P = \frac{1}{2}\begin{pmatrix} 1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \end{pmatrix} + \frac{1}{6}\begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & -2 \\ -1 & -2 & 1 \end{pmatrix}$$

$$= \begin{pmatrix} 3/6 + 1/6 & 2/6 & 3/6 - 1/6 \\ 2/6 & 4/6 & -2/6 \\ 3/6 - 1/6 & -2/6 & 3/6 + 1/6 \end{pmatrix}$$

$$\boxed{P = \frac{1}{6}\begin{pmatrix} 4 & 2 & 2 \\ 2 & 4 & -2 \\ 2 & -2 & 4 \end{pmatrix} = \frac{1}{3}\begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix}}$$

**Probe:** $P^2 = P$ ✓ (Projektion), $P = P^T$ ✓ (Orthogonalprojektion)
</details>

### (c) Ausgleichsrechnung — Normalengleichung (10P)

Die Datenpunkte $(1, 2)$, $(2, 3)$, $(3, 6)$ sollen durch eine Gerade $y = mx + c$ bestmöglich approximiert werden. Bestimmen Sie $m$ und $c$ mittels der Normalengleichung $A^T A \hat{x} = A^T b$.

<details>
<summary><b>Lösung einblenden</b></summary>

Modell: $\begin{pmatrix} 1 & 1 \\ 2 & 1 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} m \\ c \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}$, also $A = \begin{pmatrix} 1 & 1 \\ 2 & 1 \\ 3 & 1 \end{pmatrix}$, $b = \begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}$.

**Schritt 1:** Gram-Matrix $A^TA$ berechnen:
$$A^T A = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 2 & 1 \\ 3 & 1 \end{pmatrix} = \begin{pmatrix} 14 & 6 \\ 6 & 3 \end{pmatrix}$$

**Schritt 2:** Rechte Seite $A^T b$:
$$A^T b = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix} = \begin{pmatrix} 26 \\ 11 \end{pmatrix}$$

**Schritt 3:** LGS lösen: $\begin{pmatrix} 14 & 6 \\ 6 & 3 \end{pmatrix}\begin{pmatrix} m \\ c \end{pmatrix} = \begin{pmatrix} 26 \\ 11 \end{pmatrix}$

$Z_2 \to Z_2 - \frac{6}{14} Z_1 = Z_2 - \frac{3}{7} Z_1$:

$3 - \frac{3}{7} \cdot 6 = 3 - \frac{18}{7} = \frac{3}{7}$ und $11 - \frac{3}{7} \cdot 26 = 11 - \frac{78}{7} = \frac{-1}{7}$

Also $\frac{3}{7} c = \frac{-1}{7}$ → $c = -\frac{1}{3}$

Rückeinsetzen: $14m + 6 \cdot (-\frac{1}{3}) = 26$ → $14m = 28$ → $m = 2$

$$\boxed{y = 2x - \frac{1}{3}}$$

**Probe:** $f(1) = 5/3 \approx 1.67$, $f(2) = 11/3 \approx 3.67$, $f(3) = 17/3 \approx 5.67$. Residuenvektor: $(-1/3, -2/3, 1/3)^T$, symmetrisch verteilt ✓
</details>

---

## Aufgabe A4: Zusammenhänge — Wahr/Falsch & Reversibilität (20 Punkte) — Verstehen/Beweisen

### (a) Wahr oder Falsch? (10P, je 2P)

Entscheiden Sie mit Begründung:

1. Wenn $\det(A) \neq 0$, dann hat das LGS $Ax = b$ für jedes $b$ genau eine Lösung.
2. Jede $3 \times 3$-Matrix über $\mathbb{C}$ ist trigonalisierbar.
3. Wenn $A$ und $B$ dieselben Eigenwerte (mit Vielfachheiten) haben, dann ist $A$ ähnlich zu $B$.
4. Für eine orthogonale Matrix $Q$ gilt stets $Q^{-1} = Q^T$.
5. Wenn $A$ nilpotent ist (d.h. $A^k = 0$ für ein $k$), dann ist $\det(A) = 0$.

<details>
<summary><b>Lösung einblenden</b></summary>

1. **Wahr.** $\det(A) \neq 0 \Rightarrow A$ invertierbar $\Rightarrow$ eindeutige Lösung $x = A^{-1}b$.

2. **Wahr.** Über $\mathbb{C}$ zerfällt das char. Polynom in Linearfaktoren. Der Satz von Schur besagt, dass dann jede Matrix über $\mathbb{C}$ unitär trigonalisierbar ist.

3. **Falsch.** Gegenbeispiel: $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ und $B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ haben beide den Eigenwert $1$ mit alg. VF $2$, aber $A$ ist nicht diagonalisierbar, $B$ schon. Sie haben verschiedene JNF und sind daher nicht ähnlich.

4. **Wahr.** Aus $Q^TQ = I$ folgt direkt $Q^{-1} = Q^T$ (Definition der Orthogonalität).

5. **Wahr.** Wenn $A^k = 0$, dann $\det(A)^k = \det(A^k) = \det(0) = 0$. Also $\det(A) = 0$.
Alternativ: Alle Eigenwerte nilpotenter Matrizen sind $0$ (denn $Av = \lambda v \Rightarrow 0 = A^k v = \lambda^k v \Rightarrow \lambda = 0$), also $\det(A) = \prod \lambda_i = 0$.
</details>

### (b) Reversibilität — Beweis (10P)

Sei $A \in \mathbb{R}^{n \times n}$ eine **reversible** Matrix, d.h. es existiert eine invertierbare Matrix $R$ mit $RAR^{-1} = -A$.

**Zeigen Sie:** Wenn $\lambda$ ein Eigenwert von $A$ ist, dann ist auch $-\lambda$ ein Eigenwert von $A$.

<details>
<summary><b>Lösung einblenden</b></summary>

**Beweis:**

Sei $\lambda$ ein Eigenwert von $A$, also $Av = \lambda v$ für ein $v \neq 0$.

Aus der Reversibilitätsbedingung $RAR^{-1} = -A$ folgt, dass $A$ und $-A$ **ähnlich** sind.

Ähnliche Matrizen haben dasselbe charakteristische Polynom:
$$\chi_{-A}(\mu) = \det(-A - \mu I) = \det(-(A + \mu I)) = (-1)^n \det(A + \mu I) = (-1)^n \chi_A(-\mu)$$

Da $A$ und $-A$ ähnlich sind: $\chi_A(\mu) = \chi_{-A}(\mu) = (-1)^n \chi_A(-\mu)$.

Sei $\lambda$ Nullstelle von $\chi_A$: $\chi_A(\lambda) = 0$. Dann ist $\chi_{-A}(\lambda) = 0$, also ist $\lambda$ Eigenwert von $-A$.

Die Eigenwerte von $-A$ sind genau die negierten Eigenwerte von $A$: Wenn $\mu$ Eigenwert von $-A$ ist, dann $-Aw = \mu w$, also $A w = -\mu w$, d.h. $-\mu$ ist Eigenwert von $A$.

Da $\lambda$ Eigenwert von $-A$ ist, ist $-\lambda$ Eigenwert von $A$. $\square$

**Alternativbeweis (direkter):**
Sei $Av = \lambda v$ mit $v \neq 0$. Setze $w := Rv \neq 0$ (da $R$ invertierbar).
$$Aw = A(Rv) = -R(AR^{-1}R)v\;?$$
Besser: Aus $RAR^{-1} = -A$ folgt $RA = -AR$.
$$A(Rv) = AR v$$
Aus $RA = -AR$ folgt $AR = -RA$:
$$A(Rv) = -R(Av) = -R(\lambda v) = -\lambda(Rv) = -\lambda w$$
Also $Aw = -\lambda w$ mit $w = Rv \neq 0$, d.h. $-\lambda$ ist Eigenwert von $A$. $\square$
</details>

---

---

# 📝 Klausur B — „Die Beweislastige"

*Schwerpunkte: JNF berechnen, Geometrie mit komplexen Zahlen, Gram-Schmidt mit Integral-SP, Euklidischer Algorithmus*

---

## Aufgabe B1: Eigenwerte & Jordan-Normalform konkret (30 Punkte) — Methoden

Gegeben sei die Matrix:
$$B = \begin{pmatrix} 2 & 0 & 0 & 0 \\ 1 & 2 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 3 & -1 \end{pmatrix}$$

### (a) Bestimmen Sie das charakteristische Polynom und die Eigenwerte von $B$. (6P)

<details>
<summary><b>Lösung einblenden</b></summary>

$B$ ist eine untere Dreiecksmatrix (in Blockform). Die Eigenwerte stehen auf der Diagonale: $\lambda_1 = 2$ (doppelt), $\lambda_2 = -1$ (doppelt).

$$\chi_B(\lambda) = (\lambda - 2)^2(\lambda + 1)^2$$

**Eigenwerte:** $\lambda_1 = 2$ mit alg. VF $= 2$, $\lambda_2 = -1$ mit alg. VF $= 2$.
</details>

### (b) Berechnen Sie die Eigenräume $E_2$ und $E_{-1}$. (8P)

<details>
<summary><b>Lösung einblenden</b></summary>

**Eigenraum $E_2 = \ker(B - 2I)$:**
$$B - 2I = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & -3 & 0 \\ 0 & 0 & 3 & -3 \end{pmatrix}$$

Gauß:
- Pivots in Zeile 2 (Spalte 1), Zeile 3 (Spalte 3). Zeile 4 → $Z_4 + Z_3$: $(0, 0, 0, -3)$ → Pivot Spalte 4.
- Freie Variable: $x_2$.

$x_1 = 0$, $x_3 = 0$, $x_4 = 0$, $x_2$ frei.

$$E_2 = \text{span}\left(\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}\right), \quad \text{geo. VF}(2) = 1$$

**Eigenraum $E_{-1} = \ker(B + I)$:**
$$B + I = \begin{pmatrix} 3 & 0 & 0 & 0 \\ 1 & 3 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 3 & 0 \end{pmatrix}$$

Gauß: Pivots in Spalte 1, 2, 3. Freie Variable: $x_4$.
$x_1 = 0$, $x_2 = 0$, $x_3 = 0$, $x_4$ frei.

$$E_{-1} = \text{span}\left(\begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}\right), \quad \text{geo. VF}(-1) = 1$$
</details>

### (c) Bestimmen Sie die Jordan-Normalform von $B$. (8P)

<details>
<summary><b>Lösung einblenden</b></summary>

Für jeden Eigenwert haben wir alg. VF $= 2$ und geo. VF $= 1$. Also gibt es zu jedem Eigenwert genau **einen** Jordan-Block der Größe 2.

$$\boxed{J = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & 0 & -1 \end{pmatrix}}$$
</details>

### (d) Minimalpolynom, Determinante, Diagonalisierbarkeit (8P)

Bestimmen Sie:
1. Das Minimalpolynom $\mu_B(\lambda)$.
2. $\det(B)$.
3. Ist $B$ diagonalisierbar?
4. Ist $B$ invertierbar?

<details>
<summary><b>Lösung einblenden</b></summary>

1. **Minimalpolynom:** Der größte Block zu EW $2$ hat Größe 2, der größte zu EW $-1$ hat Größe 2.
$$\mu_B(\lambda) = (\lambda - 2)^2(\lambda + 1)^2$$
(Hier stimmen char. Polynom und Minimalpolynom überein, da es zu jedem EW genau einen Block gibt.)

2. **Determinante:** $\det(B) = \det(J) = 2 \cdot 2 \cdot (-1) \cdot (-1) = 4$.

3. **Nicht diagonalisierbar,** da Jordan-Blöcke der Größe 2 existieren. Äquivalent: geo. VF $\neq$ alg. VF für beide EW.

4. **Invertierbar,** da $\det(B) = 4 \neq 0$.
</details>

---

## Aufgabe B2: Geometrie mit komplexen Zahlen (20 Punkte) — Beweisen

### (a) Drehung als Multiplikation (10P)

Sei $w = e^{i\pi/3}$ und sei $z \in \mathbb{C}$ ein beliebiger Punkt in der komplexen Ebene. Zeigen Sie:

1. $|wz| = |z|$ (die Multiplikation mit $w$ ändert den Abstand zum Ursprung nicht).
2. Die Abbildung $z \mapsto wz$ beschreibt eine Drehung um $60°$ um den Ursprung.

<details>
<summary><b>Lösung einblenden</b></summary>

**1. Längentreue:**
$$|wz| = |w| \cdot |z| = |e^{i\pi/3}| \cdot |z| = 1 \cdot |z| = |z| \quad \square$$

(Für die Polarform $e^{i\theta}$ gilt $|e^{i\theta}| = |\cos\theta + i\sin\theta| = \sqrt{\cos^2\theta + \sin^2\theta} = 1$.)

**2. Drehung um $60°$:**
Schreibe $z = re^{i\varphi}$ in Polarform. Dann:
$$wz = e^{i\pi/3} \cdot re^{i\varphi} = r \cdot e^{i(\varphi + \pi/3)}$$

Der Betrag bleibt $r$, der Winkel wird um $\pi/3 = 60°$ erhöht. Das ist die Definition einer Drehung um den Ursprung mit Winkel $60°$. $\square$
</details>

### (b) Gleichseitiges Dreieck (10P)

Drei Punkte $z_1, z_2, z_3 \in \mathbb{C}$ bilden ein gleichseitiges Dreieck mit Schwerpunkt im Ursprung (d.h. $z_1 + z_2 + z_3 = 0$).

Zeigen Sie: Wenn $z_2 = wz_1$ mit $w = e^{i 2\pi/3}$, dann gilt $z_3 = w^2 z_1$ und $z_1 + z_2 + z_3 = 0$.

<details>
<summary><b>Lösung einblenden</b></summary>

Für ein gleichseitiges Dreieck mit Schwerpunkt im Ursprung sind die Ecken um jeweils $120° = 2\pi/3$ gedreht.

Sei $z_1 = re^{i\alpha}$ ein beliebiger Eckpunkt. Dann:
- $z_2 = wz_1 = e^{i2\pi/3} \cdot re^{i\alpha} = re^{i(\alpha + 2\pi/3)}$
- $z_3 = w^2 z_1 = e^{i4\pi/3} \cdot re^{i\alpha} = re^{i(\alpha + 4\pi/3)}$

**Schwerpunktbedingung:**
$$z_1 + z_2 + z_3 = z_1(1 + w + w^2)$$

Wir berechnen $1 + w + w^2$ mit $w = e^{i2\pi/3}$. Da $w$ eine primitive dritte Einheitswurzel ist, ist $w$ Nullstelle von $\frac{x^3 - 1}{x - 1} = x^2 + x + 1$. Also:

$$w^2 + w + 1 = 0 \implies 1 + w + w^2 = 0$$

Somit: $z_1 + z_2 + z_3 = z_1 \cdot 0 = 0$. $\square$
</details>

---

## Aufgabe B3: Gram-Schmidt mit Integral-Skalarprodukt (30 Punkte) — Methoden

Gegeben: $f_1(x) = 1$, $f_2(x) = x$, $f_3(x) = x^2$ auf dem Intervall $[-1, 1]$ mit dem Skalarprodukt:
$$\langle f | g \rangle = \int_{-1}^{1} f(x) \, g(x) \, dx$$

### (a) Orthonormalisieren Sie $\{f_1, f_2\}$ zu einem ONS $\{e_1, e_2\}$. (12P)

<details>
<summary><b>Lösung einblenden</b></summary>

**Schritt 1: Normierung von $f_1 = 1$**

$$\|f_1\|^2 = \int_{-1}^1 1^2 \, dx = 2$$
$$e_1 = \frac{f_1}{\|f_1\|} = \frac{1}{\sqrt{2}}$$

**Schritt 2: Orthogonalisierung von $f_2 = x$**

$$\langle e_1 | f_2 \rangle = \int_{-1}^1 \frac{1}{\sqrt{2}} \cdot x \, dx = \frac{1}{\sqrt{2}} \left[\frac{x^2}{2}\right]_{-1}^1 = \frac{1}{\sqrt{2}} \cdot 0 = 0$$

$f_2 = x$ ist bereits orthogonal zu $e_1$ (symmetrisches Intervall!).

$$\tilde{e}_2 = f_2 - 0 = x$$

**Schritt 3: Normierung**
$$\|\tilde{e}_2\|^2 = \int_{-1}^1 x^2 \, dx = \left[\frac{x^3}{3}\right]_{-1}^1 = \frac{1}{3} - \left(-\frac{1}{3}\right) = \frac{2}{3}$$

$$\boxed{e_1(x) = \frac{1}{\sqrt{2}}, \qquad e_2(x) = \sqrt{\frac{3}{2}} \cdot x}$$

**Probe:** $\langle e_1 | e_2 \rangle = \int_{-1}^1 \frac{1}{\sqrt{2}} \cdot \sqrt{3/2} \cdot x \, dx = \frac{\sqrt{3}}{2} \int_{-1}^1 x \, dx = 0$ ✓
</details>

### (b) Erweitern Sie zu einem ONS $\{e_1, e_2, e_3\}$ durch Gram-Schmidt auf $f_3 = x^2$. (12P)

<details>
<summary><b>Lösung einblenden</b></summary>

**Skalarprodukt $\langle e_1 | f_3 \rangle$:**
$$\langle e_1 | f_3 \rangle = \frac{1}{\sqrt{2}} \int_{-1}^1 x^2 \, dx = \frac{1}{\sqrt{2}} \cdot \frac{2}{3} = \frac{2}{3\sqrt{2}} = \frac{\sqrt{2}}{3}$$

**Skalarprodukt $\langle e_2 | f_3 \rangle$:**
$$\langle e_2 | f_3 \rangle = \sqrt{\frac{3}{2}} \int_{-1}^1 x \cdot x^2 \, dx = \sqrt{\frac{3}{2}} \int_{-1}^1 x^3 \, dx = 0$$

(Ungerade Funktion über symmetrisches Intervall!)

**Orthogonalisierung:**
$$\tilde{e}_3 = f_3 - \langle e_1 | f_3 \rangle e_1 - \langle e_2 | f_3 \rangle e_2 = x^2 - \frac{\sqrt{2}}{3} \cdot \frac{1}{\sqrt{2}} - 0 = x^2 - \frac{1}{3}$$

**Normierung:**
$$\|\tilde{e}_3\|^2 = \int_{-1}^1 \left(x^2 - \frac{1}{3}\right)^2 dx = \int_{-1}^1 \left(x^4 - \frac{2}{3}x^2 + \frac{1}{9}\right) dx$$

$$= \left[\frac{x^5}{5}\right]_{-1}^1 - \frac{2}{3}\left[\frac{x^3}{3}\right]_{-1}^1 + \frac{1}{9}\left[x\right]_{-1}^1 = \frac{2}{5} - \frac{2}{3} \cdot \frac{2}{3} + \frac{1}{9} \cdot 2 = \frac{2}{5} - \frac{4}{9} + \frac{2}{9}$$

$$= \frac{2}{5} - \frac{2}{9} = \frac{18 - 10}{45} = \frac{8}{45}$$

$$\boxed{e_3(x) = \sqrt{\frac{45}{8}}\left(x^2 - \frac{1}{3}\right) = \frac{3\sqrt{5}}{2\sqrt{8}}\left(x^2 - \frac{1}{3}\right) = \frac{3}{2}\sqrt{\frac{5}{2}}\left(x^2 - \frac{1}{3}\right)}$$

*Anmerkung:* Die $e_1, e_2, e_3$ sind (bis auf Normierung) die **Legendre-Polynome** $P_0, P_1, P_2$!
</details>

### (c) Berechnen Sie die Projektionsmatrix $P$ (bzgl. der Basis $\{e_1, e_2\}$) und die beste Approximation von $f_3 = x^2$ im Unterraum $\text{span}(1, x)$. (6P)

<details>
<summary><b>Lösung einblenden</b></summary>

Die beste Approximation von $f_3 = x^2$ im Unterraum $U = \text{span}(e_1, e_2) = \text{span}(1, x)$ ist:

$$\hat{f}_3 = \langle e_1 | f_3 \rangle \, e_1 + \langle e_2 | f_3 \rangle \, e_2 = \frac{\sqrt{2}}{3} \cdot \frac{1}{\sqrt{2}} + 0 = \frac{1}{3}$$

Also: **Die beste Approximation von $x^2$ durch eine Gerade $ax + b$ auf $[-1,1]$ ist die Konstante $\frac{1}{3}$.**

Der Approximationsfehler:
$$\|f_3 - \hat{f}_3\|^2 = \|\tilde{e}_3\|^2 = \frac{8}{45}$$
$$\|f_3 - \hat{f}_3\| = \sqrt{\frac{8}{45}} = \frac{2\sqrt{2}}{3\sqrt{5}} \approx 0.422$$
</details>

---

## Aufgabe B4: Euklidischer Algorithmus & Polynome (20 Punkte) — Methoden/Verstehen

### (a) Horner-Schema (6P)

Bestimmen Sie die Nullstellen von $p(x) = x^3 - 2x^2 - 5x + 6$ mithilfe des Horner-Schemas.

<details>
<summary><b>Lösung einblenden</b></summary>

Nullstelle raten (Teiler von 6): $p(1) = 1 - 2 - 5 + 6 = 0$ ✓

**Horner-Schema** für $(x^3 - 2x^2 - 5x + 6) : (x - 1)$:

| | $1$ | $-2$ | $-5$ | $6$ |
|---|---|---|---|---|
| $1$ | $\downarrow$ | $1$ | $-1$ | $-6$ |
| | $1$ | $-1$ | $-6$ | $0$ |

Restpolynom: $x^2 - x - 6 = (x - 3)(x + 2)$.

**Nullstellen:** $\boxed{x_1 = 1, \; x_2 = 3, \; x_3 = -2}$
</details>

### (b) Euklidischer Algorithmus für Polynome (8P)

Berechnen Sie $\gcd(x^4 - 1, \; x^3 - x)$ mit dem Euklidischen Algorithmus.

<details>
<summary><b>Lösung einblenden</b></summary>

$p(x) = x^4 - 1$, $q(x) = x^3 - x$.

**Schritt 1:** Polynomdivision $p : q$:
$$x^4 - 1 = x \cdot (x^3 - x) + (x^2 - 1)$$
Rest $r_1(x) = x^2 - 1$.

**Schritt 2:** Teile $q$ durch $r_1$:
$$x^3 - x = x \cdot (x^2 - 1) + 0$$
Rest $= 0$.

Der letzte nicht verschwindende Rest ist $r_1(x) = x^2 - 1$.

$$\boxed{\gcd(x^4 - 1, \; x^3 - x) = x^2 - 1}$$

*Probe:* $x^4 - 1 = (x^2 - 1)(x^2 + 1)$ ✓ und $x^3 - x = x(x^2 - 1)$ ✓.
</details>

### (c) Zusammenhang Minimalpolynom & Teilbarkeit (6P)

Sei $A$ eine Matrix mit char. Polynom $\chi_A(\lambda) = (\lambda - 1)^3(\lambda + 2)^2$.
1. Welche Minimalpolynome sind möglich? Listen Sie alle auf.
2. Warum muss das Minimalpolynom $\mu_A$ stets ein Teiler von $\chi_A$ sein?

<details>
<summary><b>Lösung einblenden</b></summary>

**1.** Das Minimalpolynom hat die Form $\mu_A(\lambda) = (\lambda - 1)^a (\lambda + 2)^b$ mit $1 \leq a \leq 3$ und $1 \leq b \leq 2$. Die möglichen Kombinationen:

| $a$ | $b$ | $\mu_A(\lambda)$ |
|-----|-----|-------------------|
| 1 | 1 | $(\lambda-1)(\lambda+2)$ |
| 1 | 2 | $(\lambda-1)(\lambda+2)^2$ |
| 2 | 1 | $(\lambda-1)^2(\lambda+2)$ |
| 2 | 2 | $(\lambda-1)^2(\lambda+2)^2$ |
| 3 | 1 | $(\lambda-1)^3(\lambda+2)$ |
| 3 | 2 | $(\lambda-1)^3(\lambda+2)^2$ |

Insgesamt **6 mögliche** Minimalpolynome.

**2.** Nach dem Satz von Cayley-Hamilton gilt $\chi_A(A) = 0$. Da das Minimalpolynom per Definition das Polynom kleinsten Grades ist mit $\mu_A(A) = 0$, und $\chi_A$ die Matrix ebenfalls annulliert, muss $\mu_A | \chi_A$ gelten (Polynomdivision: der Rest müsste die Matrix auch annullieren, hätte aber kleineren Grad als $\mu_A$ — Widerspruch, also Rest $= 0$).
</details>

---

---

# 📝 Klausur C — „Die Anwendungsorientierte"

*Schwerpunkte: LGS & Inverse, Distanzgeometrie, Körper $\mathbb{F}_{11}$, Spektralsatz & Gruppen*

---

## Aufgabe C1: LGS & Bild-Kern-Algorithmus (25 Punkte) — Methoden

### (a) LGS lösen (10P)

Bestimmen Sie die allgemeine Lösung des linearen Gleichungssystems $Ax = b$ mit:
$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \\ 3 & 6 & 4 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 3 \\ 4 \end{pmatrix}$$

<details>
<summary><b>Lösung einblenden</b></summary>

Erweitertes Tableau:
$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 2 & 4 & 3 & 3 \\ 3 & 6 & 4 & 4 \end{array}\right)$$

$Z_2 \to Z_2 - 2Z_1$: $(0, 0, 1, 1)$
$Z_3 \to Z_3 - 3Z_1$: $(0, 0, 1, 1)$

$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{array}\right)$$

$Z_3 \to Z_3 - Z_2$: $(0, 0, 0, 0)$

$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

$Z_1 \to Z_1 - Z_2$: $(1, 2, 0, 0)$

$$\left(\begin{array}{ccc|c} 1 & 2 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

Pivots: Spalten 1 und 3. Freie Variable: $x_2 = t$.

- $x_3 = 1$
- $x_1 = -2t$

$$\boxed{x = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} + t \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, \quad t \in \mathbb{R}}$$

**Rang** $= 2$, **Defekt** $= 1$, **Bild** $= \text{span}(s_1, s_3)$ der Originalmatrix.
</details>

### (b) Kern bestimmen (5P)

Bestimmen Sie eine Basis des **Kerns** von $A$.

<details>
<summary><b>Lösung einblenden</b></summary>

$\ker(A)$ ist die Lösungsmenge von $Ax = 0$. Aus dem reduzierten Tableau:
$x_1 = -2t$, $x_2 = t$, $x_3 = 0$.

$$\ker(A) = \text{span}\left(\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}\right)$$

$\dim(\ker(A)) = 1$, $\text{Rang}(A) = 2$. Rangsatz: $3 = 2 + 1$ ✓
</details>

### (c) Inverse einer Matrix (10P)

Berechnen Sie die Inverse von:
$$M = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix}$$

<details>
<summary><b>Lösung einblenden</b></summary>

$\det(M) = 1(0-1) - 0 + 1(0-1) = -1 - 1 = -2 \neq 0$ → invertierbar.

Gauß-Jordan mit erweiterter Einheitsmatrix:

$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 0 & 1 \end{array}\right)$$

$Z_3 \to Z_3 - Z_1$:
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & -1 & -1 & 0 & 1 \end{array}\right)$$

$Z_3 \to Z_3 - Z_2$:
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & -2 & -1 & -1 & 1 \end{array}\right)$$

$Z_3 \to Z_3 / (-2)$:
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1/2 & 1/2 & -1/2 \end{array}\right)$$

$Z_1 \to Z_1 - Z_3$, $Z_2 \to Z_2 - Z_3$:
$$\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & 1/2 & -1/2 & 1/2 \\ 0 & 1 & 0 & -1/2 & 1/2 & 1/2 \\ 0 & 0 & 1 & 1/2 & 1/2 & -1/2 \end{array}\right)$$

$$\boxed{M^{-1} = \frac{1}{2}\begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & 1 \\ 1 & 1 & -1 \end{pmatrix}}$$

**Probe:** $M \cdot M^{-1} = I$ ✓
</details>

---

## Aufgabe C2: Distanzgeometrie & Gram-Matrizen (25 Punkte) — Methoden/Verstehen

### (a) Positiv (semi-)definit prüfen (8P)

Gegeben die Gram-Matrix:
$$G = \begin{pmatrix} 9 & 3 \\ 3 & 4 \end{pmatrix}$$

Ist $G$ positiv definit, positiv semidefinit, oder keines von beiden? Existieren Vektoren $v_1, v_2$, die $G$ realisieren?

<details>
<summary><b>Lösung einblenden</b></summary>

$G$ ist symmetrisch: ✓

**Hauptminoren-Test:**
- $D_1 = 9 > 0$ ✓
- $D_2 = \det(G) = 9 \cdot 4 - 3 \cdot 3 = 36 - 9 = 27 > 0$ ✓

$G$ ist **positiv definit** (alle Hauptminoren echt positiv).

Da $G$ positiv definit ist mit $\text{Rang}(G) = 2$, existieren Vektoren $v_1, v_2 \in \mathbb{R}^2$ (mindestens), die $G$ realisieren, d.h. $G_{ij} = \langle v_i | v_j \rangle$.

Man kann sie z.B. via Cholesky-Zerlegung finden: $G = LL^T$ mit
$$L = \begin{pmatrix} 3 & 0 \\ 1 & ? \end{pmatrix}$$

$L_{22}: 1^2 + L_{22}^2 = 4 \Rightarrow L_{22} = \sqrt{3}$.

$$v_1 = \begin{pmatrix} 3 \\ 0 \end{pmatrix}, \quad v_2 = \begin{pmatrix} 1 \\ \sqrt{3} \end{pmatrix}$$

**Probe:** $\langle v_1|v_1\rangle = 9$, $\langle v_1|v_2\rangle = 3$, $\langle v_2|v_2\rangle = 1 + 3 = 4$ ✓
</details>

### (b) Degenerierter Fall (7P)

Gegeben:
$$G' = \begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix}$$

1. Ist $G'$ positiv semidefinit?
2. In welchem Teilraum leben die realisierenden Vektoren?

<details>
<summary><b>Lösung einblenden</b></summary>

**Hauptminoren:** $D_1 = 4 > 0$, $D_2 = 4 \cdot 9 - 36 = 0 \geq 0$.

$G'$ ist **positiv semidefinit** (alle Hauptminoren $\geq 0$, aber $\det = 0$).

**Rang von $G'$:** $\text{Rang}(G') = 1$, da Zeile 2 $= 3/2 \cdot$ Zeile 1.

Die realisierenden Vektoren leben in $\mathbb{R}^1$ (eindimensional): $v_1 = 2$, $v_2 = 3$ (als Skalare).

**Probe:** $v_1^2 = 4$, $v_1 v_2 = 6$, $v_2^2 = 9$ ✓
</details>

### (c) Nicht-realisierbar (10P)

Kann die Matrix
$$G'' = \begin{pmatrix} 1 & 5 \\ 5 & 4 \end{pmatrix}$$
als Gram-Matrix realisiert werden? Begründen Sie ausführlich.

<details>
<summary><b>Lösung einblenden</b></summary>

**Hauptminoren:** $D_1 = 1 > 0$, aber $D_2 = \det(G'') = 1 \cdot 4 - 5 \cdot 5 = 4 - 25 = -21 < 0$.

$G''$ ist **nicht positiv semidefinit** (negativer Hauptminor). Eine Gram-Matrix muss immer positiv semidefinit sein (da $\langle v | v \rangle \geq 0$), daher:

**$G''$ ist nicht als Gram-Matrix realisierbar.** Es gibt keine Vektoren in einem reellen Vektorraum, deren paarweise Skalarprodukte diese Matrix bilden.

*Anschaulich:* $|\langle v_1 | v_2 \rangle| = 5$, aber $\|v_1\| \cdot \|v_2\| = 1 \cdot 2 = 2 < 5$. Das verletzt die **Cauchy-Schwarz-Ungleichung** $|\langle u|v\rangle| \leq \|u\| \|v\|$.
</details>

---

## Aufgabe C3: Körper $\mathbb{F}_{11}$ — Vertiefung (25 Punkte) — Methoden/Beweisen

### (a) Gleichung $ub + a = 0$ lösen (10P)

Lösen Sie in $\mathbb{F}_{11}$ die Gleichung $u \cdot b + a = 0$ für $a = 7$ und $b = 9$.

<details>
<summary><b>Lösung einblenden</b></summary>

**Schritt 1 (Prof-Tipp):** Additiv Inverses von $a = 7$:
$A + 7 \equiv 0 \pmod{11}$. Da $4 + 7 = 11 \equiv 0$, ist $A = 4$.

**Schritt 2:** Löse $u \cdot 9 \equiv 4 \pmod{11}$.
Multiplikativ Inverses von $9$: Suche $x$ mit $9x \equiv 1 \pmod{11}$.
$9 \cdot 1 = 9$, $9 \cdot 2 = 18 \equiv 7$, $9 \cdot 3 = 27 \equiv 5$, $9 \cdot 4 = 36 \equiv 3$, $9 \cdot 5 = 45 \equiv 1$. ✓

Also $9^{-1} = 5$.

$$u = 4 \cdot 5 = 20 \equiv 9 \pmod{11}$$

**Antwort: $u = 9$**

**Probe:** $9 \cdot 9 + 7 = 81 + 7 = 88 = 8 \cdot 11 \equiv 0 \pmod{11}$ ✓
</details>

### (b) Nachweis: Jedes Element $\neq 0$ hat ein multiplikatives Inverses (8P)

Beweisen Sie: In einem endlichen Körper $\mathbb{F}_p$ (mit $p$ prim) hat jedes Element $a \neq 0$ ein multiplikatives Inverses.

<details>
<summary><b>Lösung einblenden</b></summary>

**Beweis:** Sei $a \in \mathbb{F}_p$ mit $a \neq 0$, also $a \in \{1, 2, \ldots, p-1\}$.

Betrachte die Abbildung $\varphi: \mathbb{F}_p^* \to \mathbb{F}_p^*$ mit $\varphi(x) = ax \bmod p$ (wobei $\mathbb{F}_p^* = \{1, \ldots, p-1\}$).

**Injektivität:** Sei $ax \equiv ay \pmod{p}$, also $a(x - y) \equiv 0 \pmod{p}$. Da $p$ prim und $a \not\equiv 0$, folgt $x \equiv y \pmod{p}$. Also ist $\varphi$ injektiv.

Da $\mathbb{F}_p^*$ endlich ist und $\varphi$ injektiv, ist $\varphi$ auch **surjektiv** (Schubfachprinzip). Also gibt es ein $x$ mit $ax \equiv 1 \pmod{p}$. Dieses $x$ ist das multiplikative Inverse von $a$. $\square$
</details>

### (c) Nilpotente Matrizen über endlichen Körpern (7P)

Sei $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ über $\mathbb{F}_{11}$. Zeigen Sie: $A$ ist nilpotent und berechnen Sie $(I - A)^{-1}$ über $\mathbb{F}_{11}$.

<details>
<summary><b>Lösung einblenden</b></summary>

**Nilpotenz:** $A^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0$ ✓

**Inverse via geometrische Reihe:** Da $A^2 = 0$:
$$(I - A)^{-1} = I + A + A^2 + \cdots = I + A$$
(Neumann-Reihe terminiert nach dem linearen Glied.)

$$(I - A)^{-1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

**Probe über $\mathbb{F}_{11}$:**
$$(I - A)(I + A) = I + A - A - A^2 = I - 0 = I \quad ✓$$

(Das funktioniert identisch wie über $\mathbb{R}$, da es nur ganzzahlige Operationen sind.)
</details>

---

## Aufgabe C4: Spektralsatz, Matrixtypen & Gruppen (25 Punkte) — Verstehen/Beweisen

### (a) Wahr oder Falsch? (10P, je 2P)

1. Eine symmetrische reelle Matrix hat stets reelle Eigenwerte.
2. Orthogonale Matrizen bilden eine Untergruppe von $GL(n, \mathbb{R})$.
3. Die Signatur einer quadratischen Form $q(x) = x^T A x$ hängt von der Wahl der Basis ab.
4. Jede normale Matrix ($A^*A = AA^*$) ist unitär diagonalisierbar.
5. Wenn $A \in SO(2)$, dann ist $A$ eine Drehung.

<details>
<summary><b>Lösung einblenden</b></summary>

1. **Wahr.** Spektralsatz: Symmetrische reelle Matrizen haben nur reelle Eigenwerte und sind orthogonal diagonalisierbar.

2. **Wahr.** Untergruppen-Check:
   - $I \in O(n)$: $I^T I = I$ ✓
   - Abgeschlossenheit: $A, B \in O(n) \Rightarrow (AB)^T(AB) = B^T A^T A B = B^T B = I$ ✓
   - Inverse: $A^{-1} = A^T$ und $(A^T)^T A^T = A A^T = I$ ✓

3. **Falsch.** Nach dem Trägheitssatz von Sylvester ist die Signatur $(n_+, n_-, n_0)$ eine **Invariante** — unabhängig von der Basiswahl.

4. **Wahr.** Das ist genau die Aussage des Spektralsatzes (über $\mathbb{C}$): Normale Matrizen sind unitär diagonalisierbar.

5. **Wahr.** $SO(2) = \{A \in O(2) : \det(A) = 1\}$. Jede solche Matrix hat die Form $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, was eine Drehung um den Winkel $\theta$ ist.
</details>

### (b) Beweis: Orthogonale Matrix ist Isometrie (8P)

Zeigen Sie: Wenn $Q \in \mathbb{R}^{n \times n}$ orthogonal ist ($Q^TQ = I$), dann gilt $\|Qv\| = \|v\|$ für alle $v \in \mathbb{R}^n$.

<details>
<summary><b>Lösung einblenden</b></summary>

**Beweis:**

$$\|Qv\|^2 = \langle Qv | Qv \rangle = (Qv)^T(Qv) = v^T Q^T Q v = v^T I v = v^T v = \langle v|v\rangle = \|v\|^2$$

Da Normen nicht-negativ sind: $\|Qv\| = \|v\|$. $\square$

**Korollar:** Orthogonale Abbildungen erhalten auch das Skalarprodukt:
$$\langle Qu | Qv \rangle = u^T Q^T Q v = u^T v = \langle u | v \rangle$$

Das heißt: Längen UND Winkel werden bewahrt → orthogonale Matrizen sind **Isometrien**.
</details>

### (c) Untergruppe zeigen (7P)

Zeigen Sie, dass $SL(n, \mathbb{R}) = \{A \in GL(n, \mathbb{R}) : \det(A) = 1\}$ eine Untergruppe von $GL(n, \mathbb{R})$ ist.

<details>
<summary><b>Lösung einblenden</b></summary>

**Untergruppen-Kriterium** (drei Bedingungen):

**(1) Nicht leer / neutrales Element:**
$I \in SL(n)$, da $\det(I) = 1$. ✓

**(2) Abgeschlossenheit unter Multiplikation:**
Seien $A, B \in SL(n)$, also $\det(A) = \det(B) = 1$.
$$\det(AB) = \det(A) \cdot \det(B) = 1 \cdot 1 = 1$$
Also $AB \in SL(n)$. ✓

**(3) Abgeschlossenheit unter Inversenbildung:**
Sei $A \in SL(n)$, also $\det(A) = 1 \neq 0$, daher existiert $A^{-1}$.
$$\det(A^{-1}) = \frac{1}{\det(A)} = \frac{1}{1} = 1$$
Also $A^{-1} \in SL(n)$. ✓

$\Rightarrow$ $SL(n, \mathbb{R})$ ist Untergruppe von $GL(n, \mathbb{R})$. $\square$
</details>

---

---

# 📝 Klausur D — „Die DGL-Klausur"

*Schwerpunkte: Matrixexponential via JNF, Cayley-Hamilton-Anwendungen, Determinanten, Reversibilität & Isometrien*

---

## Aufgabe D1: Matrixexponential & Differentialgleichungen (25 Punkte) — Methoden

Gegeben sei die Matrix:
$$A = \begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix}$$

### (a) Eigenwerte und Diagonalisierbarkeit (5P)

Bestimmen Sie die Eigenwerte von $A$. Ist $A$ diagonalisierbar?

<details>
<summary><b>Lösung einblenden</b></summary>

$$\chi_A(\lambda) = (1 - \lambda)(-1 - \lambda) - 0 = -(1 - \lambda)(1 + \lambda) = \lambda^2 - 1$$

Eigenwerte: $\lambda_1 = 1$, $\lambda_2 = -1$.

Zwei verschiedene Eigenwerte bei einer $2 \times 2$-Matrix → **diagonalisierbar** (jeder Eigenwert hat geo. VF = alg. VF = 1).
</details>

### (b) Diagonalisierung (8P)

Finden Sie $S$ und $D$ mit $A = SDS^{-1}$.

<details>
<summary><b>Lösung einblenden</b></summary>

**EW $\lambda_1 = 1$:** $\ker(A - I) = \ker\begin{pmatrix} 0 & 0 \\ 1 & -2 \end{pmatrix}$. Aus $x_1 = 2x_2$ folgt $v_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

**EW $\lambda_2 = -1$:** $\ker(A + I) = \ker\begin{pmatrix} 2 & 0 \\ 1 & 0 \end{pmatrix}$. Aus $x_1 = 0$ folgt $v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

$$S = \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**$S^{-1}$:** $\det(S) = 2$, also $S^{-1} = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ -1 & 2 \end{pmatrix}$.

**Probe:** $SDS^{-1} = \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & 0 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 1 & -1 \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & 0 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix} = A$ ✓
</details>

### (c) Matrixexponential $\exp(tA)$ (7P)

Berechnen Sie $\exp(tA)$ für $t \in \mathbb{R}$.

<details>
<summary><b>Lösung einblenden</b></summary>

Da $A = SDS^{-1}$:
$$\exp(tA) = S \exp(tD) S^{-1} = S \begin{pmatrix} e^t & 0 \\ 0 & e^{-t} \end{pmatrix} S^{-1}$$

$$= \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} e^t & 0 \\ 0 & e^{-t} \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & 0 \\ -1 & 2 \end{pmatrix}$$

$$= \begin{pmatrix} 2e^t & 0 \\ e^t & e^{-t} \end{pmatrix} \cdot \frac{1}{2}\begin{pmatrix} 1 & 0 \\ -1 & 2 \end{pmatrix}$$

$$= \frac{1}{2}\begin{pmatrix} 2e^t & 0 \\ e^t - e^{-t} & 2e^{-t} \end{pmatrix}$$

$$\boxed{\exp(tA) = \begin{pmatrix} e^t & 0 \\ \frac{e^t - e^{-t}}{2} & e^{-t} \end{pmatrix} = \begin{pmatrix} e^t & 0 \\ \sinh(t) & e^{-t} \end{pmatrix}}$$
</details>

### (d) DGL lösen (5P)

Lösen Sie das Anfangswertproblem $\dot{x}(t) = Ax(t)$ mit $x(0) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.

<details>
<summary><b>Lösung einblenden</b></summary>

$$x(t) = \exp(tA) \cdot x(0) = \begin{pmatrix} e^t & 0 \\ \sinh(t) & e^{-t} \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} e^t \\ \sinh(t) \end{pmatrix}$$

$$\boxed{x(t) = \begin{pmatrix} e^t \\ \frac{e^t - e^{-t}}{2} \end{pmatrix}}$$

**Probe:** $\dot{x} = \begin{pmatrix} e^t \\ \cosh(t) \end{pmatrix}$ und $Ax = \begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} e^t \\ \sinh(t) \end{pmatrix} = \begin{pmatrix} e^t \\ e^t - \sinh(t) \end{pmatrix} = \begin{pmatrix} e^t \\ \cosh(t) \end{pmatrix}$ ✓

$x(0) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ ✓
</details>

---

## Aufgabe D2: Cayley-Hamilton & nilpotente Matrizen (25 Punkte) — Beweisen

### (a) Cayley-Hamilton anwenden (8P)

Sei $A \in \mathbb{R}^{3 \times 3}$ mit $\chi_A(\lambda) = -\lambda^3 + 3\lambda^2 - 3\lambda + 1 = -(\lambda - 1)^3$.

1. Welches Matrixpolynom folgt direkt aus Cayley-Hamilton?
2. Drücken Sie $A^3$ durch niedrigere Potenzen von $A$ aus.

<details>
<summary><b>Lösung einblenden</b></summary>

**1.** Cayley-Hamilton: $\chi_A(A) = 0$, also:
$$-A^3 + 3A^2 - 3A + I = 0$$

**2.** Umstellen:
$$A^3 = 3A^2 - 3A + I$$

*Beachte:* $(A - I)^3 = A^3 - 3A^2 + 3A - I = 0$ nach Cayley-Hamilton. Also ist $A - I$ nilpotent der Ordnung $\leq 3$.
</details>

### (b) Nilpotenz und Inverse (10P)

Sei $N \in \mathbb{R}^{n \times n}$ nilpotent mit $N^3 = 0$ (aber $N^2 \neq 0$).

1. Beweisen Sie: $(I - N)$ ist invertierbar und $(I - N)^{-1} = I + N + N^2$.
2. Beweisen Sie: Alle Eigenwerte von $N$ sind $0$.

<details>
<summary><b>Lösung einblenden</b></summary>

**1.** Wir zeigen $(I - N)(I + N + N^2) = I$:

$$(I - N)(I + N + N^2) = I + N + N^2 - N - N^2 - N^3 = I - N^3 = I - 0 = I$$

Also $(I - N)^{-1} = I + N + N^2$. $\square$

*Dies ist die endliche geometrische Reihe für Matrizen: $\sum_{k=0}^{2} N^k$.*

**2.** Sei $\lambda$ ein Eigenwert von $N$ mit Eigenvektor $v \neq 0$, also $Nv = \lambda v$.

Dann: $N^3 v = \lambda^3 v$ (induktiv: $N^k v = \lambda^k v$).

Aber $N^3 = 0$, also $N^3 v = 0 = \lambda^3 v$.

Da $v \neq 0$: $\lambda^3 = 0$, also $\lambda = 0$. $\square$
</details>

### (c) Matrixpotenzen und Induktion (7P)

Sei $A \in \mathbb{R}^{2 \times 2}$ mit $A^2 = 2A - I$. Beweisen Sie durch vollständige Induktion:

$$A^n = nA - (n-1)I \quad \text{für alle } n \geq 1$$

<details>
<summary><b>Lösung einblenden</b></summary>

**Induktionsanfang ($n = 1$):**
$$A^1 = 1 \cdot A - 0 \cdot I = A \quad ✓$$

**Induktionsanfang ($n = 2$):**
$$A^2 = 2A - I \quad ✓ \text{ (Voraussetzung)}$$

**Induktionsvoraussetzung:** Für ein $n \geq 2$ gelte $A^n = nA - (n-1)I$.

**Induktionsschritt ($n \to n+1$):**
$$A^{n+1} = A^n \cdot A \overset{\text{IV}}{=} (nA - (n-1)I) \cdot A$$
$$= nA^2 - (n-1)A$$
$$\overset{A^2 = 2A-I}{=} n(2A - I) - (n-1)A$$
$$= 2nA - nI - (n-1)A$$
$$= (2n - n + 1)A - nI$$
$$= (n+1)A - nI$$

Das ist genau die Formel für $n+1$: $A^{n+1} = (n+1)A - ((n+1)-1)I$ ✓ $\square$
</details>

---

## Aufgabe D3: Determinanten & Eigenwerte (25 Punkte) — Methoden

### (a) Determinante einer 4×4-Matrix via Laplace (10P)

Berechnen Sie die Determinante von:
$$M = \begin{pmatrix} 2 & 0 & 0 & 3 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 4 & 0 \\ 0 & 0 & 0 & 5 \end{pmatrix}$$

<details>
<summary><b>Lösung einblenden</b></summary>

**Laplace-Entwicklung nach Zeile 2** (hat die meisten Nullen):

$$\det(M) = (-1)^{2+2} \cdot 1 \cdot \det\begin{pmatrix} 2 & 0 & 3 \\ 1 & 4 & 0 \\ 0 & 0 & 5 \end{pmatrix}$$

(Alle anderen Einträge in Zeile 2 sind $0$.)

Berechne die 3×3-Determinante, **Laplace nach Zeile 3**:

$$\det = 0 - 0 + 5 \cdot \det\begin{pmatrix} 2 & 0 \\ 1 & 4 \end{pmatrix} = 5 \cdot (8 - 0) = 40$$

$$\boxed{\det(M) = 1 \cdot 40 = 40}$$

*Alternativ-Check:* $M$ hat eine fast-Dreiecksstruktur. Wir können auch nach Spalte 2 entwickeln und erhalten dasselbe Ergebnis.
</details>

### (b) Eigenwerte mit Horner-Schema (10P)

Bestimmen Sie die Eigenwerte von:
$$C = \begin{pmatrix} 4 & -2 & 1 \\ 0 & 3 & -1 \\ 0 & 0 & 2 \end{pmatrix}$$

Geben Sie an: Ist $C$ diagonalisierbar? Was sind $\det(C)$ und $\text{Spur}(C)$?

<details>
<summary><b>Lösung einblenden</b></summary>

$C$ ist eine **obere Dreiecksmatrix**. Die Eigenwerte stehen auf der Diagonale:

$$\lambda_1 = 4, \quad \lambda_2 = 3, \quad \lambda_3 = 2$$

Da alle Eigenwerte verschieden, ist $C$ **diagonalisierbar** (jeder EW hat automatisch geo. VF = alg. VF = 1).

$$\det(C) = 4 \cdot 3 \cdot 2 = 24$$
$$\text{Spur}(C) = 4 + 3 + 2 = 9$$
</details>

### (c) Daraus folgende Eigenschaften (5P)

Für die Matrix $C$ aus (b):
1. Ist $C$ invertierbar?
2. Ist $C$ volumentreu?
3. Ist $C$ orientierungserhaltend?
4. Kann $C$ orthogonal sein?

<details>
<summary><b>Lösung einblenden</b></summary>

1. **Ja**, da $\det(C) = 24 \neq 0$.
2. **Nein**, da $|\det(C)| = 24 \neq 1$.
3. **Ja**, da $\det(C) = 24 > 0$.
4. **Nein**, denn für orthogonale Matrizen gilt $\det = \pm 1$, aber $\det(C) = 24$. Alternativ: Eigenwerte orthogonaler Matrizen haben Betrag 1, aber hier ist $|\lambda_1| = 4 \neq 1$.
</details>

---

## Aufgabe D4: Reversibilität, Isometrien & Strukturtheorie (25 Punkte) — Verstehen/Beweisen

### (a) Zusammenhang Determinante, EW, Kern und LGS (8P)

Sei $A \in \mathbb{R}^{n \times n}$. Beweisen Sie die Äquivalenz der folgenden Aussagen:
1. $\det(A) \neq 0$
2. $\ker(A) = \{0\}$
3. $Ax = b$ hat für jedes $b$ genau eine Lösung.

<details>
<summary><b>Lösung einblenden</b></summary>

**$(1) \Rightarrow (2)$:** $\det(A) \neq 0$ bedeutet, dass $A$ invertierbar ist. Sei $v \in \ker(A)$, also $Av = 0$. Dann $v = A^{-1} \cdot 0 = 0$. Also $\ker(A) = \{0\}$.

**$(2) \Rightarrow (3)$:** $\ker(A) = \{0\}$ bedeutet Defekt $= 0$. Nach dem Rangsatz: $\text{Rang}(A) = n - 0 = n$. Also hat $A$ vollen Rang, $A$ ist surjektiv (Bild $= \mathbb{R}^n$), und $Ax = b$ hat für jedes $b$ eine Lösung. Da $\ker(A) = \{0\}$, ist die Lösung eindeutig (homogene Lösung ist trivial).

**$(3) \Rightarrow (1)$:** Wenn $Ax = b$ für jedes $b$ genau eine Lösung hat, dann insbesondere für jede Spalte $e_i$ der Einheitsmatrix. Die Lösungsvektoren bilden $A^{-1}$, also existiert $A^{-1}$, und daher $\det(A) \neq 0$. $\square$
</details>

### (b) Eigenwerte spezieller Matrizen (10P)

Beweisen Sie:

1. Wenn $A$ orthogonal ist ($A^T A = I$), dann gilt $|\lambda| = 1$ für jeden Eigenwert $\lambda$ von $A$.
2. Wenn $A$ schiefsymmetrisch ist ($A^T = -A$, reelle Matrix), dann sind alle Eigenwerte rein imaginär (d.h. $\lambda = i\mu$ mit $\mu \in \mathbb{R}$).

<details>
<summary><b>Lösung einblenden</b></summary>

**1.** Sei $Av = \lambda v$ mit $v \neq 0$ (möglicherweise $\lambda \in \mathbb{C}$, $v \in \mathbb{C}^n$).

$$\|Av\|^2 = (Av)^* (Av) = v^* A^* A v = v^* A^T A v = v^* I v = v^* v = \|v\|^2$$

Andererseits: $\|Av\|^2 = \|\lambda v\|^2 = |\lambda|^2 \|v\|^2$.

Da $v \neq 0$: $|\lambda|^2 = 1$, also $|\lambda| = 1$. $\square$

**2.** Sei $A^T = -A$ und $Av = \lambda v$ mit $v \neq 0$ ($v \in \mathbb{C}^n$).

Betrachte $v^* A v$ auf zwei Arten:

**Einerseits:** $v^* A v = v^* (\lambda v) = \lambda \|v\|^2$.

**Andererseits:** $(v^* A v)^* = v^* A^* v = v^* \overline{A}^T v = v^* (-\overline{A}) v$

Da $A$ reell: $\overline{A} = A$, also $(v^* A v)^* = -v^* A v$.

Also $\overline{v^* A v} = -v^* A v$, d.h. $\overline{\lambda}\|v\|^2 = -\lambda\|v\|^2$.

Da $v \neq 0$: $\overline{\lambda} = -\lambda$, also $\text{Re}(\lambda) = 0$. $\square$
</details>

### (c) Reversibilität und Spur (7P)

Sei $A$ reversibel (d.h. $\exists R$ invertierbar mit $RAR^{-1} = -A$).

Zeigen Sie: $\text{Spur}(A) = 0$.

<details>
<summary><b>Lösung einblenden</b></summary>

**Beweis:**

Ähnliche Matrizen haben die gleiche Spur (da die Spur eine Invariante unter Ähnlichkeitstransformationen ist):
$$\text{Spur}(RAR^{-1}) = \text{Spur}(A)$$

Aus der Reversibilitätsbedingung $RAR^{-1} = -A$:
$$\text{Spur}(A) = \text{Spur}(RAR^{-1}) = \text{Spur}(-A) = -\text{Spur}(A)$$

Also: $2 \cdot \text{Spur}(A) = 0$, d.h. $\text{Spur}(A) = 0$. $\square$

*Alternativ:* Da (wie in Klausur A, Aufgabe 4 gezeigt) die Eigenwerte einer reversiblen Matrix paarweise $(\lambda, -\lambda)$ auftreten, heben sie sich in der Spur $= \sum \lambda_i$ gegenseitig auf.
</details>

---

---

# 📊 Übersicht: Themenabdeckung der 4 Klausuren

| Thema | A | B | C | D |
|-------|---|---|---|---|
| **Körper (Prof-Tipp!)** | ✅ $\mathbb{F}_5$ | — | ✅ $\mathbb{F}_{11}$ | — |
| **Matrixexponential** | ✅ $D+N$ | — | — | ✅ via Diag. |
| **Gram-Schmidt** | ✅ $\mathbb{R}^3$ | ✅ Integral-SP | — | — |
| **Ausgleichsrechnung** | ✅ | — | — | — |
| **Projektionsmatrix** | ✅ | ✅ | — | — |
| **JNF berechnen** | — | ✅ konkret | — | — |
| **JNF ablesen** | — | — | — | — |
| **Eigenwerte/Diag.** | — | ✅ | — | ✅ |
| **Determinanten** | — | — | — | ✅ Laplace |
| **Euklidischer Alg.** | — | ✅ | — | — |
| **Horner-Schema** | — | ✅ | — | ✅ |
| **Geometrie kompl. Zahlen** | — | ✅ Drehung | — | — |
| **Distanzgeometrie** | — | — | ✅ | — |
| **LGS / Bild-Kern** | ✅ | — | ✅ | — |
| **Inverse berechnen** | — | — | ✅ | — |
| **Reversibilität** | ✅ | — | — | ✅ |
| **Cayley-Hamilton** | — | ✅ | — | ✅ |
| **Induktionsbeweis** | — | — | — | ✅ |
| **Wahr/Falsch** | ✅ | — | ✅ | — |
| **Isometrien/Gruppen** | — | — | ✅ | ✅ |
| **Nilpotenz** | — | — | ✅ | ✅ |
| **DGL mit $\exp(tA)$** | — | — | — | ✅ |
| **Spektralsatz** | — | — | ✅ | — |

> **Empfehlung:** Bearbeite die Klausuren in der Reihenfolge A → C → D → B (aufsteigender Schwierigkeitsgrad).
