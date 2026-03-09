# 🎓 4 Spezial-Trainingsklausuren zur Nachklausur

> [!INFO] Über diese Klausuren
> Diese 4 Probeklausuren wurden methodisch exakt nach der hochgeladenen **Tipp-Liste des Dozenten zur Nachklausur** modelliert. Sie prüfen genau die Thematiken, Schwerpunkte und Rechenalgorithmen, die relevant sein werden.
> **Tipp:** Versuche zuerst die Aufgaben auf Papier zu bearbeiten, bevor du die Lösung ausklappst!

---

## 📄 Trainingsklausur 1: Grundlagen, Körper & Bild-Kern

### Aufgabe 1.1: Wahr oder Falsch? (Gefragte Zusammenhänge)
Entscheiden Sie, ob folgende Aussagen wahr oder falsch sind, und geben Sie eine kurze Begründung.
1. Eine lineare Abbildung ist genau dann umkehrbar (invertierbar), wenn der Kern der Darstellungsmatrix nur aus dem Nullvektor besteht.
2. Zwei Matrizen, die dasselbe Minimalpolynom besitzen, haben zwingend auch dieselbe Jordan-Normalform.
3. Jede Matrix mit Determinante ungleich Null ist diagonalisierbar.

<details>
<summary><b>Lösung einblenden</b></summary>
1. **Wahr.** Wenn der Kern nur $\{0\}$ enthält (Defekt = 0), ist die Matrix nach dem Rangsatz surjektiv und damit (da quadratisch) bijektiv, also invertierbar.
2. **Falsch.** Gegenbeispiel: Wenn Blockgrößen identisch sind, kann die Multiplizität variieren. Sei das Minimalpolynom $(x-1)^2$. Blockgrößen sind max max 2x2. Bei einer 4x4 Matrix kann die JNF so aussehen: ein 2er Block & zwei 1er Blöcke, ODER zwei 2er Blöcke. Beide haben exakt dasselbe Minimalpolynom!
3. **Falsch.** Die Determinante sagt nur aus, dass der Eigenwert 0 nicht existiert (Invertibilität gewährt). Die Matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ hat Determinante 1, st aber offensichtlich nicht diagonalisierbar.
</details>

### Aufgabe 1.2: Rechnen im Körper (Offizieller Prof-Tipp!)
Betrachten wir den endlichen Körper $\mathbb{F}_7$ (Restklassen modulo 7). Sei $a = 5$ und $b = 3$. Lösen Sie die Gleichung $u \cdot b + a = 0$ für ein gesuchtes $u \in \mathbb{F}_7$. 
**Nutzen Sie explizit den Tipp des Professors:**
1. Ermitteln Sie zunächst das additiv Inverse $A$ von $a$, sodass $A + a = 0$.
2. Finden Sie dann einen Faktor $u$, sodass $u \cdot b = A$.

<details>
<summary><b>Lösung einblenden</b></summary>
1. Wir suchen das additiv Inverse $A$ zu $a=5$ in $\mathbb{F}_7$.
Wegen $5 + 2 = 7 \equiv 0 \pmod 7$ gilt $A = 2$.
Es gilt also $A + a = 0$.

2. Nun muss $u \cdot 3 \equiv 2 \pmod 7$ gelöst werden. 
Wir benötigen das multiplikativ Inverse von $3$. Wir testen: $3 \cdot 1 = 3$, $3 \cdot 2 = 6$, $3 \cdot 3 = 9 \equiv 2$, $3 \cdot 4 = 12 \equiv 5$, $3 \cdot 5 = 15 \equiv 1$.
Das multiplikativ Inverse zu $3$ ist also $5$.
Wir multiplizieren beide Seiten der Gleichung $u \cdot 3 \equiv 2$ mit $5$:

$$ u \cdot (3 \cdot 5) \equiv 2 \cdot 5 \pmod 7 $$
$$ u \cdot 1 \equiv 10 \pmod 7 $$

Da $10 = 7 + 3$, folgt: **$u = 3$**.

*Probe:* $3 \cdot 3 + 5 = 9 + 5 = 14 \equiv 0 \pmod 7$. Stimmt!
</details>

### Aufgabe 1.3: Bild-Kern-Algorithmus zur Invertierung
Berechnen Sie mittels des Bild-Kern-Algorithmus die Inverse der Matrix:
$$ M = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} $$

<details>
<summary><b>Lösung einblenden</b></summary>
Beim Bild-Kern-Algorithmus erweitert man die Matrix mit der Einheitsmatrix und rechnet per Spalten/Zeilenumformung. Bei der klassischen Invertierung durch Gauß-Jordan schreibt man:

$$ \left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 4 & 0 & 1 \end{array} \right) $$

Zeile 2 minus 3*Zeile 1:
$$ \left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & -2 & -3 & 1 \end{array} \right) $$

Zeile 2 durch -2:
$$ \left( \begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & 1.5 & -0.5 \end{array} \right) $$

Zeile 1 minus 2*Zeile 2:
$$ \left( \begin{array}{cc|cc} 1 & 0 & -2 & 1 \\ 0 & 1 & 1.5 & -0.5 \end{array} \right) $$

Die Inverse ist somit: 
$$ M^{-1} = \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix} $$
</details>

---

## 📈 Trainingsklausur 2: Matrixexponential & Polynome

### Aufgabe 2.1: Taylorreihe für Matrizen (Matrixexponential)
Berechnen Sie $\exp(A)$ für die Matrix $A = \begin{pmatrix} 4 & 2 \\ 0 & 4 \end{pmatrix}$.
Nutzen Sie die additive Zerlegung $A = D + N$.

<details>
<summary><b>Lösung einblenden</b></summary>
Wir zerlegen $A = \begin{pmatrix} 4 & 0 \\ 0 & 4 \end{pmatrix} + \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} = D + N$.
Da $D = 4 \cdot I$ ein Vielfaches der Einheitsmatrix ist, gilt unweigerlich $D \cdot N = N \cdot D$.
Da die Matrizen kommutieren, gilt das Exponentialgesetz: $\exp(A) = \exp(D) \cdot \exp(N)$.
Es ist $\exp(D) = e^4 \cdot I = \begin{pmatrix} e^4 & 0 \\ 0 & e^4 \end{pmatrix}$.
Für $N$ gilt $N^2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. 
Die Taylorreihe für $\exp(N)$ bricht also exakt nach dem linearen Glied ab:
$\exp(N) = I + N + \frac{1}{2}N^2 + \dots = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
Zusammensetzen:
$$ \exp(A) = \begin{pmatrix} e^4 & 0 \\ 0 & e^4 \end{pmatrix} \cdot \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^4 & 2e^4 \\ 0 & e^4 \end{pmatrix} $$
</details>

### Aufgabe 2.2: Horner-Schema & Euklidischer Algorithmus
Gesucht sind die Nullstellen des Polynoms $P(x) = x^3 - 6x^2 + 11x - 6$.
1. Raten Sie eine Nullstelle (Tipp: Teiler von 6).
2. Spalten Sie den Linearfaktor mithilfe des Horner-Schemas ab, oder per Polynomdivision.
3. Berechnen Sie im Anschluss den $\operatorname{ggT}(x^3 - 1, x^2 - 1)$ mit dem Euklidischen Algorithmus.

<details>
<summary><b>Lösung einblenden</b></summary>
1. Nullstelle raten: Probieren wir $x_0 = 1$: $1 - 6 + 11 - 6 = 0$.
2. **Horner-Schema** für $(x^3 - 6x^2 + 11x - 6) : (x-1)$:
- Koeffizienten aufschreiben: $1, -6, 11, -6$
- Von links nach rechts durchrechnen:
Restpolynom ist $x^2 - 5x + 6$. 
Dieses lässt sich per pq-Formel zerlegen zu $(x-2)(x-3)$. 
Die Nullstellen sind also $\{1, 2, 3\}$.

3. **Euklidischer Algorithmus:**
$P(x) = x^3-1$, $Q(x) = x^2-1$.
Teile $P$ durch $Q$: 
$(x^3-1) = x \cdot (x^2-1) + (x-1)$. Der Rest ist $r_1 = x-1$.
Nächste Iteration, teile $Q$ durch $r_1$:
$(x^2-1) = (x+1) \cdot (x-1) + 0$.
Der Rest ist 0. Der letzte nicht verschwindende Rest ist somit $(x-1)$.
Also ist der $\operatorname{ggT}(x^3-1, x^2-1) = x-1$.
</details>

---

## 🎯 Trainingsklausur 3: Gram-Schmidt, Ausgleichsrechnung & Symmetrie

### Aufgabe 3.1: Gram-Schmidt & Projektionsmatrix (Galerkin)
Gegeben seien die beiden linear unabhängigen Vektoren im $\mathbb{R}^3$: 
$v_1 = (1, 1, 0)^T$ und $v_2 = (1, 0, 1)^T$.
1. Orthonormalisieren Sie diese Basisfolgen ins System $(u_1, u_2)$ (Gram-Schmidt).
2. Berechnen Sie daraus den Projektionsoperator (Projektionsmatrix) auf die aufgespannte Ebene als iterierte Summe dyadischer Produkte.

<details>
<summary><b>Lösung einblenden</b></summary>
**1. Gram-Schmidt-Verfahren:**
- $u_1 = \frac{v_1}{\|v_1\|} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$.
- Definiere Zwischenvektor $\tilde{u}_2 = v_2 - \langle v_2, u_1 \rangle u_1$.
Das Skalarprodukt liefert: $\langle v_2, u_1 \rangle = \frac{1}{\sqrt{2}}(1\cdot 1 + 0\cdot 1 + 1\cdot 0) = \frac{1}{\sqrt{2}}$.
$\tilde{u}_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} - \frac{1}{2} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0.5 \\ -0.5 \\ 1 \end{pmatrix}$.
Norm von $\tilde{u}_2$: $\|\tilde{u}_2\| = \sqrt{0.25+0.25+1} = \sqrt{1.5} = \sqrt{3/2}$.
Nomierter finaler Vektor: $u_2 = \frac{\tilde{u}_2}{\|\tilde{u}_2\|} = \sqrt{\frac{2}{3}} \begin{pmatrix} 1/2 \\ -1/2 \\ 1 \end{pmatrix}$.

**2. Projektionsmatrix (Summe dyadischer Produkte):**
$P = u_1 u_1^T + u_2 u_2^T$
$u_1 u_1^T = \frac{1}{2} \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$
$u_2 u_2^T = \frac{2}{3} \begin{pmatrix} 1/4 & -1/4 & 1/2 \\ -1/4 & 1/4 & -1/2 \\ 1/2 & -1/2 & 1 \end{pmatrix} = \begin{pmatrix} 1/6 & -1/6 & 1/3 \\ -1/6 & 1/6 & -1/3 \\ 1/3 & -1/3 & 2/3 \end{pmatrix}$
Summe liefert:
$$ P = \begin{pmatrix} 1/2 + 1/6 & 1/2 - 1/6 & 1/3 \\ 1/2 - 1/6 & 1/2 + 1/6 & -1/3 \\ 1/3 & -1/3 & 2/3 \end{pmatrix} = \begin{pmatrix} 2/3 & 1/3 & 1/3 \\ 1/3 & 2/3 & -1/3 \\ 1/3 & -1/3 & 2/3 \end{pmatrix} $$
</details>

### Aufgabe 3.2: Ausgleichsrechnung (Normalengleichung)
Wir sollen die "am besten " passende Gerade $y = mx + c$ für die verrauschten Datenpunkte $(0,1), (1,3), (2,3)$ unter Verwendung der Normalengleichung $A^T A x = A^T b$ bestimmen.

<details>
<summary><b>Lösung einblenden</b></summary>
Unser Modell lautet: $x_i \cdot m + 1 \cdot c = y_i$.
Matrixform $A \begin{pmatrix} m \\ c \end{pmatrix} = b$:
$$ A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \\ 2 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 3 \\ 3 \end{pmatrix} $$
1. Gram-Matrix der Spalten von A konstruieren ($A^T A$):
$$ A^T A = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 1 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 3 & 3 \end{pmatrix} $$
2. Rechte Seite ($A^T b$):
$$ A^T b = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 3 \\ 3 \end{pmatrix} = \begin{pmatrix} 9 \\ 7 \end{pmatrix} $$
3. Gleichungssystem lösen: $\begin{pmatrix} 5 & 3 \\ 3 & 3 \end{pmatrix} \begin{pmatrix} m \\ c \end{pmatrix} = \begin{pmatrix} 9 \\ 7 \end{pmatrix}$.
*(Subtrahiere Zeile 2 von 1)*: $2m = 2 \implies m = 1$.
*(Rückeinsetzen)*: $3(1) + 3c = 7 \implies 3c = 4 \implies c = 4/3 \approx 1.33$.
Die Ausgleichsgerade lautet: **$y = x + 1.33$**.
</details>

---

## 🧭 Trainingsklausur 4: Distanzgeometrie, Rangsatz & Reversibilität

### Aufgabe 4.1: Wahr oder Falsch? (Matrix-Arten & Skalarprodukte)
1. Wenn $M$ unitär ist ($\bar{M}^T M = I$), dann bewahrt $M$ bei Multiplikation mit Vektoren das komplexe Skalarprodukt und damit Winkel und Längen.
2. Jede reelle Matrix mit $\det(A) < 0$ repräsentiert unweigerlich eine Abbildung mit Orientierungsumkehr (z.B. Spiegelung in einer Ebene).

<details>
<summary><b>Lösung einblenden</b></summary>
1. **Wahr.** Definition einer unitären bzw. orthogonalen Matrix: $\langle Mv, Mw \rangle = \langle v, M^* Mw \rangle = \langle v, Iw \rangle = \langle v, w \rangle$. Wenn das Skalarprodukt erhalten bleibt, bleiben Norm (Länge) und die Zwischenwinkel zu 100% erhalten!
2. **Wahr.** Die Determinante gibt exakt den geometrischen Skalierungsfaktor von Volumina an. Ihr Vorzeichen verrät die "Händigkeit" der Transformation. Ein negativer Wert erzwingt zwingend das Umklappen der Raumorientierung (mindestens eine ungerade Anzahl an Spiegelungedimensionen).
</details>

### Aufgabe 4.2: Distanzgeometrie & Gram-Matrizen
Entscheide, ob es Vektoren gibt, die die Konfiguration der Gram-Matrix 
$$ G = \begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix} $$
realisieren. Falls ja, liegen die Vektoren in einem $1D$- oder $2D$-Raum? Begründe.

<details>
<summary><b>Lösung einblenden</b></summary>
Ein Set von Abständen/Skalarprodukten ist genau dann in Realität darstellbar (euklidisch realisierbar), wenn die resultierende Gram-Matrix $G$ nicht nur **symmetrisch**, sondern auch **positiv semidefinit** ist.
1. Symmetrie $G^T = G$ ist gegeben!
2. Positive Definitheit via Hauptminoren untersuchen:
- Der erste Minor (oben links) ist $\det(4) = 4 \geq 0$.
- Die gesamte Matrix: $\det(G) = (4 \cdot 1) - (2 \cdot 2) = 0 \geq 0$.

Da alle Bedingungen greifen, ist sie positiv **semi-definit**. 
Durch die Existenz der Determinante $0$ wissen wir, dass der Rang der Matrix nicht $2$, sondern $1$ ist (Matrix enthält linear abhängige Zeilen). Es existiert genau ein strikt positiver Eigenwert und ein Null-Eigenwert.
Das bedeutet: Beide "Punkte" oder Vektoren liegen direkt auf einer eindimensionalen Linie! Die Menge ist folglich im **$\mathbb{R}^1$** darstellbar!
</details>

### Aufgabe 4.3: Ulmer-Skript Beweis & Reversibilität
Beweisen Sie direkt aus den Axiomen, aus welchem Grund eine reversible Matrix (Zeit-Reversibilität gibt es eine Matrix $R$, sodass $R A R^{-1} = -A$) mit Eigenwert $\lambda$ zwingend auch den Eigenwert $-\lambda$ aufweisen muss.

<details>
<summary><b>Lösung einblenden</b></summary>
Die Gleichung der Reversibilität formt man um: 
$$ R A R^{-1} = -A $$
Dies ist mathematisch exakt die Definition dafür, dass die Systemmatrix $A$ **ähnlich** zu ihrer Negation $-A$ ist! 
Zwei zueinander ähnliche Matrizen haben zwingend identische Charakteristische Polynome und infolgedessen auch exakt dieselben Eigenwerte.
1. Eigenwerte von $A$ nennen wir das Spektrum $\sigma(A) = \{\lambda_1, \ldots, \lambda_n\}$.
2. Eigenwerte von $-A$ sind offenbar negativ zu $A$: $\sigma(-A) = \{-\lambda_1, \ldots, -\lambda_n\}$.
Damit das Ähnlichkeitsgebot der Reversibilität erfüllt ist, müssen beide Mengen elementweise gleich sein!
Taucht also ein bestimmter Wert (wie $+3$) im Spektrum von $A$ auf, muss die Matrix $A$ folgerichtig auch den negierten Wert ($-3$) als Eigenwert besitzen, um die Symmetrie aufrecht zu erhalten. 
Das Paar $(\lambda, -\lambda)$ ist der unverkennbare Signaturstempel eines reversiblen Modells.
</details>