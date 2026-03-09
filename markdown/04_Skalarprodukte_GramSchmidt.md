# 4. Skalarprodukte & Gram-Schmidt-Verfahren

> ⚡ **PRIORITÄT 3 – Hier hast du 16/30 Punkte verloren (Aufgabe 3)!**

> [!INFO] Worum geht es hier? – Einfach erklärt
>
> Ein **Skalarprodukt** ist eine Methode, um in einem Vektorraum Längen und Winkel zu messen. Im $\mathbb{R}^2$ kennst du das als das gewöhnliche Punktprodukt: $\langle x | y \rangle = x_1 y_1 + x_2 y_2$. Dieses Konzept lässt sich verallgemeinern – sogar auf Funktionenräume, wo das Skalarprodukt ein Integral wird. Entscheidend ist: Zwei Vektoren stehen **senkrecht** (orthogonal) zueinander, wenn ihr Skalarprodukt Null ergibt.
>
> Im Komplexen wird das etwas kniffliger. Weil komplexe Zahlen einen Real- und Imaginärteil haben, muss man beim Skalarprodukt das erste Argument konjugieren: $\langle x | y \rangle = \sum \overline{x_i} y_i$. Das nennt man **hermitesches Skalarprodukt**. Der Haken: $\langle u | v \rangle \neq \langle v | u \rangle$ – stattdessen gilt $\langle u | v \rangle = \overline{\langle v | u \rangle}$. Dieses Detail war in deiner Klausuraufgabe entscheidend!
>
> Das **Gram-Schmidt-Verfahren** ist ein Algorithmus, der aus einer beliebigen Basis eine **Orthonormalbasis** macht – also eine Basis, in der alle Vektoren Länge 1 haben und paarweise senkrecht aufeinander stehen. Die Idee ist einfach: Du nimmst den ersten Vektor und normierst ihn. Dann nimmst du den zweiten Vektor, ziehst den Anteil ab, der in Richtung des ersten zeigt, und normierst das Ergebnis. So machst du weiter, bis alle Vektoren sauber orthogonal zueinander sind. Die Reihenfolge ist immer: erst orthogonalisieren (Projektionen abziehen), dann normieren.
>
> **Für die Nachklausur:** In Aufgabe 3 der Klausur musstest du Gram-Schmidt im Funktionenraum mit komplexem Skalarprodukt durchführen. Der häufigste Fehler hier: Die Konjugation vergessen! Wenn $f(x) = ix$ ist, dann ist $\overline{f(x)} = -ix$. Übe das Verfahren Schritt für Schritt an konkreten Beispielen durch, bis der Ablauf automatisch sitzt.

## 4.1 Skalarprodukte – Axiome


> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 9, AP 1: Euklidische Räume](Uebungszettel_Originale.html#aufgabenpaket-1-euklidische-raeume)
> - [Übungsblatt 9, AP 4: Unitäre Vektorräume](Uebungszettel_Originale.html#aufgabenpaket-4-unitaere-vektorraeume)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Das Skalarprodukt ist letztlich nur das Mathe-Wort für ein Werkzeug, das universell Längen messen und Winkel (Orthogonalität) zwischen zwei Elementen berechnen kann.
</blockquote>
</details>


### Reelles Skalarprodukt

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Das simple Punktprodukt aus der Schule. $x_1 y_1 + x_2 y_2$. Es ist zu sich selbst immer komplett symmetrisch.
</blockquote>
</details>

$\langle \cdot | \cdot \rangle: V \times V \to \mathbb{R}$ heißt Skalarprodukt, wenn:
1. **Symmetrie:** $\langle u | v \rangle = \langle v | u \rangle$
2. **Linearität (im 2. Argument):** $\langle u | \alpha v + \beta w \rangle = \alpha\langle u | v \rangle + \beta\langle u | w \rangle$
3. **Positive Definitheit:** $\langle v | v \rangle \geq 0$ und $\langle v | v \rangle = 0 \iff v = 0$

### Komplexes Skalarprodukt (hermitesch) ← **KLAUSURRELEVANT!**

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Im Komplexen droht ein Problem: Multipliziert man i mit sich selbst, ergäbe das eine negative Länge (-1). Darum muss im Skalarprodukt das erste Argument IMMER konjugiert werden! Dabei gilt: $\langle u|v
angle = \overline{\langle v|u
angle}$.
</blockquote>
</details>

$\langle \cdot | \cdot \rangle: V \times V \to \mathbb{C}$ heißt Skalarprodukt, wenn:
1. **Hermitesche Symmetrie:** $\langle u | v \rangle = \overline{\langle v | u \rangle}$
2. **Antilinearität im 1. Argument:** $\langle \alpha u | v \rangle = \overline{\alpha}\langle u | v \rangle$
3. **Linearität im 2. Argument:** $\langle u | \alpha v \rangle = \alpha\langle u | v \rangle$
4. **Positive Definitheit:** $\langle v | v \rangle \geq 0$ und $\langle v | v \rangle = 0 \iff v = 0$

> ⚠️ **VORSICHT:** Im Komplexen ist $\langle u | v \rangle \neq \langle v | u \rangle$, sondern $\langle u | v \rangle = \overline{\langle v | u \rangle}$!

### Standard-Skalarprodukte

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Denk daran: Integrale sind das absolute Äquivalent zur Vektor-Summe, wenn du von diskreten Spaltenvektoren zu kontinuierlichen Funktionen wechselst. Ein Integral über $f(x)g(x)$ IST ein Skalarprodukt.
</blockquote>
</details>

- **$\mathbb{R}^n$:** $\langle x | y \rangle = x^T y = \sum_{i=1}^n x_i y_i$
- **$\mathbb{C}^n$:** $\langle x | y \rangle = x^* y = \sum_{i=1}^n \overline{x_i} y_i$ (wobei $x^* = \overline{x}^T$)
- **Funktionenraum:** $\langle f | g \rangle = \int_a^b \overline{f(x)} g(x) \, dx$

### Norm (durch Skalarprodukt induziert)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Jedes Skalarprodukt eines Vektors mit sich selbst ergibt die quadrierte Länge. Wenn du am Ende die Wurzel ziehst, ist dein Vektor 'genormt' (Länge 1).
</blockquote>
</details>

$$\|v\| = \sqrt{\langle v | v \rangle}$$

## 4.2 Orthogonalität

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Zwei Vektoren (oder Funktionen!) haben absolut keine Berührungspunkte, keine gemeinsame Richtung. Sie spannen den Raum maximal breit auf.
</blockquote>
</details>


### Definitionen

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Orthogonal = Senkrecht (Skalarprodukt = 0). Orthonormal = Senkrecht UND auf Länge 1 normiert. Ein ONS ist wahnsinnig bequem zu rechnen, da fast jede Multiplikation in 0 oder 1 zerfällt.
</blockquote>
</details>

- **Orthogonal:** $u \perp v \iff \langle u | v \rangle = 0$
- **Orthogonalsystem (OS):** Paarweise orthogonale, nicht-null Vektoren
- **Orthonormalsystem (ONS):** OS mit $\|v_i\| = 1$ für alle $i$
- **Orthonormalbasis (ONB):** ONS, das auch Basis ist

### Orthogonales Komplement

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Das ist genau die Menge aller Vektoren im Raum, die auf deinem Unterraum senkrecht stehen. Wenn du auf dem flachen Fußboden deines Zimmers stehst, ist das Komplement genau die Achse, die zur Decke zeigt.
</blockquote>
</details>

$$U^\perp = \{v \in V \mid \langle v | u \rangle = 0 \text{ für alle } u \in U\}$$

Es gilt: $V = U \oplus U^\perp$ (direkte Summe)

## 4.3 Gram-Schmidt-Verfahren – Schritt für Schritt


> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 6, AP 1: Gram-Schmidt-Verfahren](Uebungszettel_Originale.html#aufgabenpaket-1-gram-schmidt-verfahren)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Der systematische 'Schatten-Auslöscher'-Algorithmus. Wir wollen saubere Orthogonalachsen formen, indem wir iterativ immer das abziehen, was nicht senkrecht ist.
</blockquote>
</details>


**Eingabe:** Linear unabhängige Vektoren $v_1, \ldots, v_k$  
**Ausgabe:** Orthonormalbasis $e_1, \ldots, e_k$

### Algorithmus

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Wenn du von $v_2$ den Term $\langle u_1|v_2
angle u_1$ subtrahierst, schneidest du genau den Schatten ab, den $v_2$ auf $u_1$ wirft. Zurück bleibt genau der Teil, der strikt senkrecht absteht. Das klappt exakt so auch mit Polynomen!
</blockquote>
</details>


**Schritt 1:** Normiere den ersten Vektor
$$e_1 = \frac{v_1}{\|v_1\|}$$

**Schritt 2:** Subtrahiere Projektion, dann normiere
$$\tilde{e}_2 = v_2 - \langle e_1 | v_2 \rangle \, e_1$$
$$e_2 = \frac{\tilde{e}_2}{\|\tilde{e}_2\|}$$

**Schritt $k$:** Subtrahiere alle vorherigen Projektionen, dann normiere
$$\tilde{e}_k = v_k - \sum_{j=1}^{k-1} \langle e_j | v_k \rangle \, e_j$$
$$e_k = \frac{\tilde{e}_k}{\|\tilde{e}_k\|}$$

> **MERKE die Reihenfolge:** Projektion abziehen → normieren. NICHT umgekehrt!

## 4.4 Klausuraufgabe 3 – Komplette Musterlösung

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Hier haben fast alle Punkte verloren! Beim komplexen Integral wird die Konjugation vergessen. Wenn du $ix$ in den linken Slot des Skalarprodukts knallst, MUSS das Integral mit $-ix$ (konjugiert) weiterrechnen sonst wird das Ergebnis falsch.
</blockquote>
</details>


**Gegeben:** $f_1(x) = 1$, $f_2(x) = ix$ auf $[0,1]$  
**Skalarprodukt:** $\langle f | g \rangle = \int_0^1 \overline{f(x)} g(x) \, dx$  
**Gesucht:** ONB von $\text{span}(f_1, f_2)$

---

**Schritt 1: Normiere $f_1$**

$$\|f_1\|^2 = \langle f_1 | f_1 \rangle = \int_0^1 \overline{1} \cdot 1 \, dx = \int_0^1 1 \, dx = 1$$

$$\|f_1\| = 1$$

$$e_1(x) = \frac{f_1(x)}{\|f_1\|} = 1$$

---

**Schritt 2: Berechne $\langle e_1 | f_2 \rangle$**

$$\langle e_1 | f_2 \rangle = \int_0^1 \overline{1} \cdot ix \, dx = i \int_0^1 x \, dx = i \cdot \frac{1}{2} = \frac{i}{2}$$

---

**Schritt 3: Orthogonalisiere $f_2$**

$$\tilde{e}_2(x) = f_2(x) - \langle e_1 | f_2 \rangle \cdot e_1(x)$$
$$= ix - \frac{i}{2} \cdot 1 = ix - \frac{i}{2} = i\left(x - \frac{1}{2}\right)$$

---

**Schritt 4: Normiere $\tilde{e}_2$**

$$\|\tilde{e}_2\|^2 = \langle \tilde{e}_2 | \tilde{e}_2 \rangle = \int_0^1 \overline{i\left(x - \frac{1}{2}\right)} \cdot i\left(x - \frac{1}{2}\right) dx$$

$$= \int_0^1 (-i)\left(x - \frac{1}{2}\right) \cdot i\left(x - \frac{1}{2}\right) dx$$

$$= \int_0^1 (-i \cdot i)\left(x - \frac{1}{2}\right)^2 dx = \int_0^1 1 \cdot \left(x - \frac{1}{2}\right)^2 dx$$

(weil $-i \cdot i = -i^2 = -(-1) = 1$)

$$= \int_0^1 \left(x - \frac{1}{2}\right)^2 dx = \left[\frac{(x - \frac{1}{2})^3}{3}\right]_0^1 = \frac{(\frac{1}{2})^3}{3} - \frac{(-\frac{1}{2})^3}{3} = \frac{1}{24} + \frac{1}{24} = \frac{1}{12}$$

$$\|\tilde{e}_2\| = \frac{1}{\sqrt{12}} = \frac{1}{2\sqrt{3}}$$

---

**Schritt 5: Ergebnis**

$$e_1(x) = 1$$

$$e_2(x) = \frac{\tilde{e}_2}{\|\tilde{e}_2\|} = \frac{i(x - \frac{1}{2})}{\frac{1}{2\sqrt{3}}} = 2\sqrt{3} \cdot i\left(x - \frac{1}{2}\right)$$

---

**Probe:** $\langle e_1 | e_2 \rangle = \int_0^1 1 \cdot 2\sqrt{3} \, i(x - \frac{1}{2}) \, dx = 2\sqrt{3} i \int_0^1 (x - \frac{1}{2}) \, dx = 2\sqrt{3} i \cdot 0 = 0$ ✓

## 4.5 Projektionsoperatoren


> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 5, AP 4: Galerkin-Projektion](Uebungszettel_Originale.html#aufgabenpaket-4-galerkin-projektion)
> - [Übungsblatt 6, AP 2: Projektionsabbildung](Uebungszettel_Originale.html#aufgabenpaket-2-projektionsabbildung)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Wenn man eine zu schwere Gleichung lösen will, projiziert man sie mit $P_U$ auf einen einfacheren Unterraum. Das stutzt die Gleichung auf das Wesentliche zurück.
</blockquote>
</details>


### Orthogonalprojektion auf einen Unterraum

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Hast du eine ONS-Basis, baust du dir deine Projektion direkt aus Summen zusammen. Alles, was nicht reinpasst, fällt atomar zu Null ab.
</blockquote>
</details>

Sei $U = \text{span}(u_1, \ldots, u_k)$ mit ONB $e_1, \ldots, e_k$. Dann:

$$P_U(v) = \sum_{i=1}^{k} \langle e_i | v \rangle \, e_i$$

### Eigenschaften

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
$P^2 = P$ (idempotent) heißt: Wenn ich einmal einen Taschenlampenschatten auf den Boden geworfen habe, bleibt es der exakt selbe Schatten, wenn ich die Lampe nochmal von oben drauf scheinen lasse.
</blockquote>
</details>

- $P^2 = P$ (idempotent)
- $P^* = P$ (selbstadjungiert)
- $\text{Bild}(P) = U$
- $\ker(P) = U^\perp$
- $I - P$ ist die Projektion auf $U^\perp$
