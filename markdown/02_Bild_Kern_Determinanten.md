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

### Kern (Nullraum)
$$\ker(A) = \{x \in K^n \mid Ax = 0\}$$

**Berechnung:**
1. Bringe $A$ auf Zeilenstufenform (Gauß)
2. Löse das homogene LGS $Ax = 0$
3. Die freien Variablen parametrisieren den Kern

### Bild (Spaltenraum)
$$\text{Bild}(A) = \{Ax \mid x \in K^n\}$$

**Berechnung:**
1. Bringe $A$ auf Zeilenstufenform
2. Die Spalten von $A$ (Original!), die Pivotspalten entsprechen, bilden eine Basis des Bildes

### Rang einer Matrix
$$\text{Rang}(A) = \dim(\text{Bild}(A)) = \text{Anzahl der Pivotspalten}$$

### Zusammenfassung der Zusammenhänge
Für $A \in K^{m \times n}$:
- $\ker(A) \subseteq K^n$ (Unterraum des Definitionsbereichs)
- $\text{Bild}(A) \subseteq K^m$ (Unterraum des Zielraums)
- $\dim(\ker(A)) + \text{Rang}(A) = n$
- $A$ injektiv $\iff \ker(A) = \{0\}$
- $A$ surjektiv $\iff \text{Bild}(A) = K^m$
- $A$ bijektiv $\iff$ injektiv und surjektiv $\iff$ $A$ invertierbar (nur bei $m = n$)

## 2.2 Determinanten

### Definition (Leibniz-Formel)
$$\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} a_{i,\sigma(i)}$$

### Rechenregeln (AUSWENDIG LERNEN!)

| Regel | Formel |
|-------|--------|
| Produktregel | $\det(AB) = \det(A) \cdot \det(B)$ |
| Transposition | $\det(A^T) = \det(A)$ |
| Inverse | $\det(A^{-1}) = \frac{1}{\det(A)}$ |
| Skalierung | $\det(\lambda A) = \lambda^n \det(A)$ für $A \in K^{n \times n}$ |
| Dreiecksmatrix | $\det(A) = \prod_{i=1}^{n} a_{ii}$ (Produkt der Diagonaleinträge) |
| Ähnlichkeit | $\det(SAS^{-1}) = \det(A)$ |

### Laplace-Entwicklung
Nach der $i$-ten Zeile:
$$\det(A) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} \det(A_{ij})$$

wobei $A_{ij}$ die Matrix ohne $i$-te Zeile und $j$-te Spalte ist.

> **Tipp:** Entwickle nach Zeile/Spalte mit den meisten Nullen!

### Geometrische Bedeutung
- $|\det(A)|$ = Volumen des Parallelotops, das von den Spaltenvektoren aufgespannt wird
- $\det(A) > 0$: orientierungserhaltend
- $\det(A) < 0$: orientierungsumkehrend
- $|\det(A)| = 1$: volumentreu

> **KLAUSURRELEVANT (Aufgabe 1.6-1.8):**
> - $\det(A) = \det(VJV^{-1}) = \det(V)\det(J)\det(V^{-1}) = \det(J)$
> - Volumentreu $\iff |\det(A)| = 1$
> - Orientierungserhaltend $\iff \det(A) > 0$

## 2.3 LGS-Theorie

### Lösungsstruktur von $Ax = b$
- **Homogenes System** ($b = 0$): Lösungsmenge ist $\ker(A)$, ein Unterraum
- **Inhomogenes System** ($b \neq 0$): $L = x_p + \ker(A)$ (eine partikuläre Lösung + Kern)
- Lösbar $\iff b \in \text{Bild}(A)$
- **Eindeutig lösbar** $\iff$ lösbar und $\ker(A) = \{0\}$

### Gauß-Algorithmus
Erlaubte Zeilenoperationen (ändern die Lösungsmenge nicht):
1. Zeile mit $\lambda \neq 0$ multiplizieren
2. Vielfaches einer Zeile zu einer anderen addieren
3. Zeilen vertauschen

> **Achtung:** Zeilenoperationen ändern **nicht** den Kern, aber sie ändern den Spaltenraum (Bild)!
