# 1. Komplexe Zahlen & Vektorräume

> [!INFO] Worum geht es hier? – Einfach erklärt
>
> In der Schule hast du mit reellen Zahlen gerechnet – also Zahlen auf dem Zahlenstrahl. Aber manche Gleichungen, wie $x^2 = -1$, haben dort keine Lösung. Deshalb erweitern wir den Zahlenstrahl zu einer ganzen Zahlenebene: den **komplexen Zahlen**. Jede komplexe Zahl hat einen „Realteil" (links-rechts) und einen „Imaginärteil" (oben-unten). Das Besondere: Wenn du eine komplexe Zahl mit einer anderen multiplizierst, passiert geometrisch eine Drehung und Streckung in der Ebene. Das ist kein Zufall – genau deshalb sind komplexe Zahlen so nützlich, um Drehungen und Schwingungen zu beschreiben.
>
> Der zweite große Block hier sind **Vektorräume**. Du kennst Vektoren als Pfeile im $\mathbb{R}^2$ oder $\mathbb{R}^3$. Ein Vektorraum verallgemeinert das: Alles, was man sinnvoll addieren und mit Zahlen strecken kann, ist ein Vektorraum – auch Funktionen oder Polynome. Die zentrale Idee ist die **Basis**: eine minimale Menge von Vektoren, aus denen man durch Linearkombination jeden anderen Vektor im Raum erzeugen kann. Die Anzahl der Basisvektoren ist die **Dimension** des Raums.
>
> **Lineare Abbildungen** sind Funktionen zwischen Vektorräumen, die sich „brav" verhalten: Sie erhalten Addition und Skalierung. Jede solche Abbildung lässt sich als Matrix schreiben. Der **Rangsatz** sagt dir, dass die Dimension des Raums sich aufteilt in das, was die Abbildung trifft (Bild) und das, was sie auf Null schickt (Kern). Dieses Zusammenspiel von Bild und Kern zieht sich wie ein roter Faden durch die gesamte Vorlesung.
>
> **Für die Nachklausur:** Komplexe Zahlen kommen dir bei Eigenwerten und beim Gram-Schmidt mit komplexem Skalarprodukt wieder entgegen. Übe besonders das Rechnen mit $i$, $\bar{z}$ und $|z|$, und stelle sicher, dass du die Polarform sicher beherrschst.

## 1.1 Komplexe Zahlen

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Komplexe Zahlen sprengen den eindimensionalen Zahlenstrahl. Das 'i' ist im Grunde geometrisch eine 90-Grad-Drehung auf eine neue Achse (den Imaginärteil). Zweimal 90 Grad = 180 Grad, was exakt drehen auf die negative X-Achse und somit der Multiplikation mit -1 entspricht!
</blockquote>
</details>


### Definition

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein Vektorraum kann alles sein: Polynome, Matrizen, sogar Audiosignale. Solange du Objekte addieren und skalieren (strecken) kannst, bist du in einem Vektorraum.
</blockquote>
</details>

$\mathbb{C} = \{a + bi \mid a, b \in \mathbb{R}\}$ mit $i^2 = -1$

### Rechenregeln

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Plus/Minus ist einfaches Vektor-Schieben (wie im R²). Mal und Geteilt sind immer Kombinationen aus Streckung (Längen verändern) und Drehung (Winkel addieren).
</blockquote>
</details>

- **Addition:** $(a+bi) + (c+di) = (a+c) + (b+d)i$
- **Multiplikation:** $(a+bi)(c+di) = (ac - bd) + (ad + bc)i$
- **Konjugation:** $\overline{a+bi} = a - bi$
- **Betrag:** $|a+bi| = \sqrt{a^2 + b^2}$
- **Division:** $\frac{z_1}{z_2} = \frac{z_1 \cdot \overline{z_2}}{|z_2|^2}$

### Wichtige Eigenschaften

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Der Trick z * z-quer rettet uns in Klausuren oft aus der Patsche, um aus etwas Komplexem wieder eine handfeste reelle Zahl (den Radius im Quadrat) zu machen.
</blockquote>
</details>

- $z \cdot \overline{z} = |z|^2$ (immer reell und ≥ 0)
- $\overline{z_1 \cdot z_2} = \overline{z_1} \cdot \overline{z_2}$
- $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$
- $|z_1 \cdot z_2| = |z_1| \cdot |z_2|$

### Polarform

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Merk dir: Die Polarform ist der Cheat-Code für Multiplikation! Statt ewig Klammern auszumultiplizieren, addierst du hier einfach die Winkel und nimmst die Radien absolut mal. Es visualisiert das Drehen im Raum direkt.
</blockquote>
</details>

$z = r \cdot e^{i\varphi} = r(\cos\varphi + i\sin\varphi)$

wobei $r = |z|$ und $\varphi = \arg(z)$

**Multiplikation in Polarform:**
$z_1 \cdot z_2 = r_1 r_2 \cdot e^{i(\varphi_1 + \varphi_2)}$

→ Multiplikation = Streckung um $r_2$ + Drehung um $\varphi_2$

### Geometrische Interpretation

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Prof. Weber liebt Geometrie! Merk dir: Konjugieren ist immer eine Spiegelung an der reellen Achse. Multiplizieren mit $e^{iarphi}$ ist die exakte Drehung um den Ursprung.
</blockquote>
</details>

- Addition: Vektoraddition in der Ebene
- Multiplikation mit $e^{i\varphi}$: Drehung um Winkel $\varphi$
- Konjugation: Spiegelung an der reellen Achse

## 1.2 Quaternionen (kurz)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Damit haben Hamilton und Grassmann den 3D-Raum verknüpft (das baut direkt auf komplexe Zahlen auf). Wichtigstes Detail: Das Kommutativgesetz bricht! a*b ist nicht mehr b*a, denn in 3D kommt es massiv darauf an, ob du erst um X oder erst um Y drehst.
</blockquote>
</details>

$\mathbb{H} = \{a + bi + cj + dk \mid a,b,c,d \in \mathbb{R}\}$

mit $i^2 = j^2 = k^2 = ijk = -1$

**Nicht kommutativ!** $ij = k$ aber $ji = -k$

→ Anwendung: Drehungen im 3D-Raum

## 1.3 Vektorräume

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Verlasse gedanklich den Schul-Vektor (xyz-Pfeil). Abstraktion ist gefragt: Eine Lösungsmenge eines LGS, eine Menge von Differentialgleichungen – das sind alles abstrakte Vektoren.
</blockquote>
</details>


### Definition

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein Vektorraum kann alles sein: Polynome, Matrizen, sogar Audiosignale. Solange du Objekte addieren und skalieren (strecken) kannst, bist du in einem Vektorraum.
</blockquote>
</details>

Ein **Vektorraum** $V$ über einem Körper $K$ ist eine abelsche Gruppe $(V, +)$ mit einer Skalarmultiplikation $K \times V \to V$, die folgende Axiome erfüllt:

1. $\lambda(\mu v) = (\lambda\mu)v$ (Assoziativität)
2. $1 \cdot v = v$ (neutrales Element)
3. $\lambda(u+v) = \lambda u + \lambda v$ (Distributivität 1)
4. $(\lambda + \mu)v = \lambda v + \mu v$ (Distributivität 2)

### Unterräume

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein Unterraum ist eine stabile, 'brave' Teilwelt. Wenn du auf einer 2D-Ebene im 3D-Raum bleibst und durch den Ursprung gehst, hast du so eine Welt. Wichtig: Die Null (Ursprung) MUSS immer drin sein!
</blockquote>
</details>

$U \subseteq V$ ist **Unterraum** $\iff$
1. $U \neq \emptyset$ (d.h. $0 \in U$)
2. $u, w \in U \Rightarrow u + w \in U$ (abgeschlossen unter Addition)
3. $\lambda \in K, u \in U \Rightarrow \lambda u \in U$ (abgeschlossen unter Skalarmultiplikation)

**Kurzkriterium:** $U \neq \emptyset$ und $\lambda u + \mu w \in U$ für alle $\lambda, \mu \in K$ und $u, w \in U$

### Basis & Dimension

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Basis = Absolutes Raster. Nimmst du einen Vektor weg, erreichst du nicht mehr jeden Punkt (Erzeugendensystem kaputt). Tust du einen dazu, gibt es Redundanzen (Lineare Abhängigkeit). Die Dimension ist exakt die Mindest-Baustein-Zahl.
</blockquote>
</details>

- **Linear unabhängig:** $\lambda_1 v_1 + \cdots + \lambda_n v_n = 0 \Rightarrow \lambda_1 = \cdots = \lambda_n = 0$
- **Erzeugendensystem:** Jedes $v \in V$ ist Linearkombination der Erzeuger
- **Basis:** linear unabhängiges Erzeugendensystem
- **Dimension:** Anzahl der Basisvektoren: $\dim(V) = n$

### Lineare Abbildungen

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Lineare Abbildungen sind Transformationen, die das Gitter des Raumes nicht verbiegen, sondern nur gleichmäßig drehen/strecken/scheren. Jede lineare Abbildung kann man in eine Matrix übersetzen.
</blockquote>
</details>

$f: V \to W$ ist **linear** $\iff$
- $f(u + v) = f(u) + f(v)$
- $f(\lambda v) = \lambda f(v)$

**Matrixdarstellung:** Jede lineare Abbildung $f: K^n \to K^m$ wird durch eine Matrix $A \in K^{m \times n}$ dargestellt: $f(v) = Av$

### Dimensionsformel (Rangsatz)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Die wohl wichtigste Intuition der Vorlesung! Du hast einen 3D-Raum (n=3). Die Matrix projiziert/quetscht ihn auf ein 2D-Blatt (Bild hat Dim 2). Wo ist die dritte Dimension hin? Sie wurde zu Null zerquetscht! Das ist der Kern (Dim 1).
</blockquote>
</details>

$$\dim(V) = \dim(\ker(f)) + \dim(\text{Bild}(f))$$
$$n = \text{Defekt} + \text{Rang}$$

> **KLAUSURRELEVANT:** Diese Formel verbindet Kern und Bild. Wenn du den Rang einer Matrix kennst, kennst du auch die Dimension des Kerns!
