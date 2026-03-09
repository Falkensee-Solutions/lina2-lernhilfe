# 1. Komplexe Zahlen & Vektorräume

## 1.1 Komplexe Zahlen

### Definition
$\mathbb{C} = \{a + bi \mid a, b \in \mathbb{R}\}$ mit $i^2 = -1$

### Rechenregeln
- **Addition:** $(a+bi) + (c+di) = (a+c) + (b+d)i$
- **Multiplikation:** $(a+bi)(c+di) = (ac - bd) + (ad + bc)i$
- **Konjugation:** $\overline{a+bi} = a - bi$
- **Betrag:** $|a+bi| = \sqrt{a^2 + b^2}$
- **Division:** $\frac{z_1}{z_2} = \frac{z_1 \cdot \overline{z_2}}{|z_2|^2}$

### Wichtige Eigenschaften
- $z \cdot \overline{z} = |z|^2$ (immer reell und ≥ 0)
- $\overline{z_1 \cdot z_2} = \overline{z_1} \cdot \overline{z_2}$
- $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$
- $|z_1 \cdot z_2| = |z_1| \cdot |z_2|$

### Polarform
$z = r \cdot e^{i\varphi} = r(\cos\varphi + i\sin\varphi)$

wobei $r = |z|$ und $\varphi = \arg(z)$

**Multiplikation in Polarform:**
$z_1 \cdot z_2 = r_1 r_2 \cdot e^{i(\varphi_1 + \varphi_2)}$

→ Multiplikation = Streckung um $r_2$ + Drehung um $\varphi_2$

### Geometrische Interpretation
- Addition: Vektoraddition in der Ebene
- Multiplikation mit $e^{i\varphi}$: Drehung um Winkel $\varphi$
- Konjugation: Spiegelung an der reellen Achse

## 1.2 Quaternionen (kurz)
$\mathbb{H} = \{a + bi + cj + dk \mid a,b,c,d \in \mathbb{R}\}$

mit $i^2 = j^2 = k^2 = ijk = -1$

**Nicht kommutativ!** $ij = k$ aber $ji = -k$

→ Anwendung: Drehungen im 3D-Raum

## 1.3 Vektorräume

### Definition
Ein **Vektorraum** $V$ über einem Körper $K$ ist eine abelsche Gruppe $(V, +)$ mit einer Skalarmultiplikation $K \times V \to V$, die folgende Axiome erfüllt:

1. $\lambda(\mu v) = (\lambda\mu)v$ (Assoziativität)
2. $1 \cdot v = v$ (neutrales Element)
3. $\lambda(u+v) = \lambda u + \lambda v$ (Distributivität 1)
4. $(\lambda + \mu)v = \lambda v + \mu v$ (Distributivität 2)

### Unterräume
$U \subseteq V$ ist **Unterraum** $\iff$
1. $U \neq \emptyset$ (d.h. $0 \in U$)
2. $u, w \in U \Rightarrow u + w \in U$ (abgeschlossen unter Addition)
3. $\lambda \in K, u \in U \Rightarrow \lambda u \in U$ (abgeschlossen unter Skalarmultiplikation)

**Kurzkriterium:** $U \neq \emptyset$ und $\lambda u + \mu w \in U$ für alle $\lambda, \mu \in K$ und $u, w \in U$

### Basis & Dimension
- **Linear unabhängig:** $\lambda_1 v_1 + \cdots + \lambda_n v_n = 0 \Rightarrow \lambda_1 = \cdots = \lambda_n = 0$
- **Erzeugendensystem:** Jedes $v \in V$ ist Linearkombination der Erzeuger
- **Basis:** linear unabhängiges Erzeugendensystem
- **Dimension:** Anzahl der Basisvektoren: $\dim(V) = n$

### Lineare Abbildungen
$f: V \to W$ ist **linear** $\iff$
- $f(u + v) = f(u) + f(v)$
- $f(\lambda v) = \lambda f(v)$

**Matrixdarstellung:** Jede lineare Abbildung $f: K^n \to K^m$ wird durch eine Matrix $A \in K^{m \times n}$ dargestellt: $f(v) = Av$

### Dimensionsformel (Rangsatz)
$$\dim(V) = \dim(\ker(f)) + \dim(\text{Bild}(f))$$
$$n = \text{Defekt} + \text{Rang}$$

> **KLAUSURRELEVANT:** Diese Formel verbindet Kern und Bild. Wenn du den Rang einer Matrix kennst, kennst du auch die Dimension des Kerns!
