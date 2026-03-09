# 2. Lineare Abbildungen, Bild-Kern & Determinanten

> [!INFO] Worum geht es hier? – Einfach erklärt
>
> Stell dir eine Matrix als Maschine vor: Du steckst einen Vektor rein und bekommst einen anderen raus. Das **Bild** ist alles, was aus der Maschine rauskommen kann – also die Menge aller möglichen Ergebnisse. Der **Kern** hingegen ist die Menge aller Vektoren, die die Maschine zu Null macht. Wenn der Kern nur aus dem Nullvektor besteht, geht keine Information verloren und die Abbildung ist injektiv.
>
> Das Berechnen von Bild und Kern läuft immer gleich: Du bringst die Matrix mit Gauß auf Zeilenstufenform. Die Pivotspalten verraten dir das Bild, die freien Variablen den Kern. Der **Rangsatz** garantiert dabei, dass sich die Spaltenanzahl immer sauber in Rang (Dimension des Bildes) und Defekt (Dimension des Kerns) aufteilt.
>
> **Determinanten** sind eine einzige Zahl, die einer quadratischen Matrix zugeordnet wird – und diese Zahl enthält überraschend viel Information. Ist sie Null, ist die Matrix nicht invertierbar und das zugehörige Gleichungssystem hat entweder keine oder unendlich viele Lösungen. Ist sie ungleich Null, ist alles eindeutig lösbar. Geometrisch beschreibt der Betrag der Determinante, wie stark die Matrix Volumina verzerrt, und das Vorzeichen sagt dir, ob die Orientierung erhalten bleibt oder gespiegelt wird.
>
> **Für die Nachklausur:** Die Determinante kam in der Klausur bei Aufgabe 1.6–1.8 vor – dort musst du sie aus der Jordan-Normalform ablesen können. Übe die Laplace-Entwicklung und lerne die Rechenregeln (Produktregel, Transposition, Skalierung) wirklich auswendig. Der Bild-Kern-Algorithmus ist dein Schweizer Taschenmesser für fast jede Aufgabe.

## 2.1 Bild-Kern-Algorithmus


> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 3, AP 1: Homomorphiesatz und Dimensionsformel](Uebungszettel_Originale.html#aufgabenpaket-1-homomorphiesatz-und-dimensionsformel)
> - [Übungsblatt 3, AP 2: Bild und Kern berechnen](Uebungszettel_Originale.html#aufgabenpaket-2-bild-und-kern-einer-linearen-abbildung-berechnen)
> - [Übungsblatt 2, AP 4: Abbildungsmatrix erzeugen](Uebungszettel_Originale.html#aufgabenpaket-4-abbildungsmatrix-erzeugen)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Dieser Algorithmus ist die praktische Umsetzung des Homomorphiesatzes. Du schaust, was nach der Abbildung real 'übrig bleibt' (Bild) und was durch die Skalierung 'getötet' wird (Kern).
</blockquote>
</details>


### Kern (Nullraum)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Der Kern ist das 'Schwarze Loch' der Matrix. Alle Vektoren, die im LGS auf den Nullvektor abgebildet werden. Ein großer Kern bedeutet meistens massiven Informationsverlust bei der Abbildung.
</blockquote>
</details>

$$\ker(A) = \{x \in K^n \mid Ax = 0\}$$

**Berechnung:**
1. Bringe $A$ auf Zeilenstufenform (Gauß)
2. Löse das homogene LGS $Ax = 0$
3. Die freien Variablen parametrisieren den Kern

### Bild (Spaltenraum)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Das Bild ist der komplette Raum, den du nach der Transformation noch erreichen kannst. Wenn die Matrix aus 3 Vektoren (Spalten) besteht, ist das Bild einfach der Schatten oder das Volumen, das diese drei Vektoren aufspannen.
</blockquote>
</details>

$$\text{Bild}(A) = \{Ax \mid x \in K^n\}$$

**Berechnung:**
1. Bringe $A$ auf Zeilenstufenform
2. Die Spalten von $A$ (Original!), die Pivotspalten entsprechen, bilden eine Basis des Bildes

### Rang einer Matrix

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Die Dimension des Bildes. Wenn der Rang gleich der Anzahl der Spalten ist, hast du vollen Informationserhalt (Kern ist 0, die Abbildung ist injektiv).
</blockquote>
</details>

$$\text{Rang}(A) = \dim(\text{Bild}(A)) = \text{Anzahl der Pivotspalten}$$

### Zusammenfassung der Zusammenhänge

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Injektiv = Keine zwei Werte crashen auf dasselbe Bild (Kern = 0). Surjektiv = Du triffst wirklich jeden Punkt im Zielraum (Bild füllt alles aus).
</blockquote>
</details>

Für $A \in K^{m \times n}$:
- $\ker(A) \subseteq K^n$ (Unterraum des Definitionsbereichs)
- $\text{Bild}(A) \subseteq K^m$ (Unterraum des Zielraums)
- $\dim(\ker(A)) + \text{Rang}(A) = n$

- $A$ injektiv $\iff \ker(A) = \{0\}$
- $A$ surjektiv $\iff \text{Bild}(A) = K^m$
- $A$ bijektiv $\iff$ injektiv und surjektiv $\iff$ $A$ invertierbar (nur bei $m = n$)

## 2.2 Determinanten


> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 3, AP 3: Bedeutung von "Determinante = 0"](Uebungszettel_Originale.html#aufgabenpaket-3-bedeutung-von-determinante-0)
> - [Übungsblatt 4, AP 1: Determinante der Vandermonde-Matrix](Uebungszettel_Originale.html#aufgabenpaket-1-determinante-der-vandermonde-matrix)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Die Determinante ist der Volumen-Faktor! Eine Det=2 bedeutet: Jedes Quadrat wird nach Transformation doppelt so groß. Det=0 bedeutet: Der Raum wurde so flachgedrückt, dass kein Volumen mehr bleibt (nicht umkehrbar).
</blockquote>
</details>


### Definition (Leibniz-Formel)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Eher theoretisch wichtig. Praktisch zeigt sie, dass die Determinante sich aus allen Permutationen/Vertauschungen der Dimensionen errechnet. Vorzeichen prüfen nicht vergessen!
</blockquote>
</details>

$$\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} a_{i,\sigma(i)}$$

### Rechenregeln (AUSWENDIG LERNEN!)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Klassische Fehlerquelle: Eine Matrix skaliert man in JEDER Dimension. Also ist $det(\lambda \cdot A) = \lambda^n \cdot det(A)$ und NICHT nur $\lambda$. Stell dir vor, du verdoppelst einen 3D-Würfel in Länge, Breite und Höhe: Das Volumen wächst um $2^3 = 8$.
</blockquote>
</details>


| Regel | Formel |
|-------|--------|
| Produktregel | $\det(AB) = \det(A) \cdot \det(B)$ |
| Transposition | $\det(A^T) = \det(A)$ |
| Inverse | $\det(A^{-1}) = \frac{1}{\det(A)}$ |
| Skalierung | $\det(\lambda A) = \lambda^n \det(A)$ für $A \in K^{n \times n}$ |
| Dreiecksmatrix | $\det(A) = \prod_{i=1}^{n} a_{ii}$ (Produkt der Diagonaleinträge) |
| Ähnlichkeit | $\det(SAS^{-1}) = \det(A)$ |

### Laplace-Entwicklung

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Der rechenintensive Weg. Achte auf das Schachbrettmuster aus Plus/Minus bei den Vorzeichen, und nimm IMMER die Zeile/Spalte, wo die meisten Nullen stehen. Zeit ist wertvoll in der Klausur!
</blockquote>
</details>

Nach der $i$-ten Zeile:
$$\det(A) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} \det(A_{ij})$$

wobei $A_{ij}$ die Matrix ohne $i$-te Zeile und $j$-te Spalte ist.

> **Tipp:** Entwickle nach Zeile/Spalte mit den meisten Nullen!

### Geometrische Bedeutung

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Prof. Weber stellt hier seine Det=1 vs Det=-1 Fallen! Eine Spiegelung dreht den Raum komplett 'auf links' (Orientierung umgekehrt = negatives Volumen = Det -1). Eine Drehung hält die Orientierung aufrecht (Det +1).
</blockquote>
</details>

- $|\det(A)|$ = Volumen des Parallelotops, das von den Spaltenvektoren aufgespannt wird
- $\det(A) > 0$: orientierungserhaltend
- $\det(A) < 0$: orientierungsumkehrend
- $|\det(A)| = 1$: volumentreu

> **KLAUSURRELEVANT (Aufgabe 1.6-1.8):**
> - $\det(A) = \det(VJV^{-1}) = \det(V)\det(J)\det(V^{-1}) = \det(J)$
> - Volumentreu $\iff |\det(A)| = 1$
> - Orientierungserhaltend $\iff \det(A) > 0$

## 2.3 LGS-Theorie

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Hier fließen Analysis und Algebra zusammen. Wie löst man Probleme, die eigentlich nicht perfekt lösbar sind? Mit partikulärer Lösung plus Freiheitsgraden (dem Kern).
</blockquote>
</details>


### Lösungsstruktur von $Ax = b$

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Erinner dich an DGLs: Die Gesamtlösung ist IMMER = EINE richtige Speziellösung (partikulär) + die Gesamtheit aller Nullstellen (homogen, also der Kern).
</blockquote>
</details>

- **Homogenes System** ($b = 0$): Lösungsmenge ist $\ker(A)$, ein Unterraum
- **Inhomogenes System** ($b \neq 0$): $L = x_p + \ker(A)$ (eine partikuläre Lösung + Kern)
- Lösbar $\iff b \in \text{Bild}(A)$
- **Eindeutig lösbar** $\iff$ lösbar und $\ker(A) = \{0\}$

### Gauß-Algorithmus

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Er verändert den Lösungsraum nicht essentiell. Achtung: Durch die Umformungen bleibt der Kern zwar identisch, aber der Original-Spaltenraum (das Bild) kann visuell kippen. Deswegen muss man für die Basis des Bildes immer die SPALTEN DER ORIGINALMATRIX ablesen.
</blockquote>
</details>

Erlaubte Zeilenoperationen (ändern die Lösungsmenge nicht):
1. Zeile mit $\lambda \neq 0$ multiplizieren
2. Vielfaches einer Zeile zu einer anderen addieren
3. Zeilen vertauschen

> **Achtung:** Zeilenoperationen ändern **nicht** den Kern, aber sie ändern den Spaltenraum (Bild)!
