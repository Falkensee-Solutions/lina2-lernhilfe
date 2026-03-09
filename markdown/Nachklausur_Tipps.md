# 💡 Nachklausur Tipps vom Prof

> [!INFO] Hinweise und Schwerpunkte zur Nachklausur
> Die Erstklausur wird **nicht** einfach wiederholt – es werden andere Aufgaben sein!
> Hier ist eine exakte Übersicht der **Zusammenhänge und Schwerpunkte**, die für die Nachklausur relevant sind, inklusive eines direkten Lösungstipps für eine schwerere Aufgabe.

## 🔗 Wichtige Zusammenhänge

Du musst die Verbindungen zwischen den folgenden Konzepten verstanden haben und erklären/anwenden können:

* **Matrizeneigenschaften & LGS:** Determinante / Eigenwerte / Invertierbarkeit / Kern einer Matrix / Lösbarkeit LGS
* **Eigenvektoren:** Geometrische Bedeutung von Eigenvektoren im Bezug auf die lineare Abbildung
* **Strukturtheorie:** Jordan Normalform / Minimalpolynom / Haupträumen / Diagonalisierbarkeit / Linearfaktorzerlegung
* **Reversibilität:** Zusammenhang zwischen Reversibilität und Eigenwerten / Eigenvektoren (links und rechts)
* **Differentialgleichungen:** Zusammenhang zwischen Matrixexponential und der Lösung einer Differentialgleichung
* **Matrix-Arten & Abbildungen:** Zusammenhang zwischen der Art der Matrix (z.B. orthogonal, unitär, $\det(A)=1$, $\det(A)<0$) und der linearen Abbildung
* **Gruppentheorie:** Zusammenhang zwischen Symmetrie/Symmetriebrechung und Symmetriegruppe/Untergruppe
* **Geometrie:** Zusammenhang zwischen Skalarprodukten und Längen- (=Norm-) und Winkelmessung

---

## 🧮 Zentrale Rechenverfahren & Algorithmen

Die folgenden Berechnungen müssen sicher sitzen:

* **Sicheres Lösen von LGS:** Allgemeine Lösung eines linearen Gleichungssystems (mit dem Bild-Kern-Algorithmus)
* **Ausgleichsrechnung:** Nutzen der Normalengleichung
* **Inverse Matrix:** Berechnung der Inversen einer Matrix (Bild-Kern-Algorithmus)
* **Eigenräume:** Berechnung der Eigenräume einer Matrix (Bild-Kern-Algorithmus)
* **Polynome:** Berechnung der Nullstellen eines Polynoms (pq-Formel, Linearfaktoren abspalten z.B. durch Horner-Schema)
* **Determinanten:** Berechnung der Determinante einer Matrix (Spalten-/Zeilenumformung, Laplace, Leibniz, Sarrus)
* **Euklidischer Algorithmus:** Speziell für Polynome
* **Distanzgeometrie:** Lösung des Distanzgeometrie-Problems (Realisierung einer Gram-Matrix)
* **Matrixexponential:** Berechnung von $\exp(A)$ aus einer Matrix der Form $A = D + N$ mit $DN = ND$ (Taylorreihe für Matrizen)
* **Gram-Schmidt:** Orthonormalisierung einer gegebenen Vektorraum-Basis in ein ONS
* **Projektion & Galerkin:** 
  * Berechnung der/des Projektionsmatrix/operators auf die Basis eines ONS (Summe dyadischer Produkte)
  * Berechnung einer darstellenden Matrix auf Basis eines ONS (Galerkin)

---

## 🧠 Beweise & Theorie-Fragen

* **Geometrie mit komplexen Zahlen:** Geometrische Aussagen beweisen unter Nutzung komplexer Zahlen (Typische geleitete Klausuraufgaben, so wie im Video „Geometrieaufgaben“ in der ersten Vorlesungswoche)
* **Ulmer Skript (9. Woche):** Alle Aussagen im „Ulmer Skript“ beweisen können.
* **Wahr oder Falsch:** Mit allen in den drei verlinkten Muster-Klausuren (11. bis 13. Woche) bewiesenen Aussagen Fragen des Typs *„wahr oder nicht wahr“* beantworten können – jeweils mit einer **selbst-formulierten Begründung**!
* **Übungszettel 6:** Zettel 6, Aufgabenpaket 3.1 sicher beherrschen.

---

## ⚠️ Exklusiver Extra-Tipp zur Nachklausur!

> **Ein offizieller Tipp für eine etwas schwerere Aufgabe in einem Körper:**
> 
> *„Mit welcher Zahl muss ich $b$ multiplizieren, so dass es zu $a$ addiert Null ergibt?“*
> 
> Wenn man die Gleichung $u \cdot b + a = 0$ mit gegebenem $a$ und gegebenem $b$ und gesuchtem $u$ in einem Körper lösen will, dann muss man **zunächst das additiv Inverse von $a$ finden**. 
> Nennen wir das jetzt mal $A$ (also $A + a = 0$). 
> Und jetzt muss man einen Faktor $u$ finden, so dass $u \cdot b = A$ gilt.
