# Checkliste – Was muss ich können?

> Gehe jedes Thema durch und bewerte ehrlich: ✅ kann ich | ⚠️ unsicher | ❌ muss ich lernen
> Bearbeite die ❌ und ⚠️ Themen priorisiert!

---

## Thema 1: Komplexe Zahlen (Tag 1)
- [ ] Grundrechenarten mit komplexen Zahlen (Addition, Multiplikation, Division)
- [ ] Konjugation und Betrag berechnen
- [ ] Polarform: $z = re^{i\varphi}$ umrechnen
- [ ] Geometrische Bedeutung der Multiplikation (Drehstreckung)
- [ ] Eulersche Formel: $e^{i\varphi} = \cos\varphi + i\sin\varphi$

## Thema 2: Vektorräume & Lineare Abbildungen (Tag 1)
- [ ] Vektorraum-Axiome aufzählen können
- [ ] Unterraum-Kriterium anwenden (3 Bedingungen prüfen)
- [ ] Lineare Unabhängigkeit prüfen
- [ ] Basis und Dimension bestimmen
- [ ] Lineare Abbildung: Definition und Matrixdarstellung
- [ ] Dimensionsformel (Rangsatz): $\dim(V) = \dim(\ker) + \dim(\text{Bild})$

## Thema 3: Bild-Kern-Algorithmus (Tag 2)
- [ ] Kern einer Matrix berechnen (Gauß → homogenes LGS lösen)
- [ ] Bild einer Matrix bestimmen (Pivotspalten der Originalmatrix)
- [ ] Rang und Defekt bestimmen
- [ ] Injektivität/Surjektivität/Bijektivität über Kern/Bild prüfen

## Thema 4: Determinanten (Tag 2)
- [ ] Determinante einer 2×2- und 3×3-Matrix berechnen
- [ ] Laplace-Entwicklung anwenden
- [ ] Dreiecksmatrix: Determinante = Produkt der Diagonale
- [ ] Rechenregeln: $\det(AB) = \det(A)\det(B)$, $\det(SAS^{-1}) = \det(A)$, etc.
- [ ] Geometrische Bedeutung erklären (Volumen, Orientierung)
- [ ] **Begründen können:** Warum $\det(A) = \det(J)$ bei JNF?

## Thema 5: Eigenwerte & Diagonalisierung (Tag 3) ⚡
- [ ] Eigenwerte über $\chi_A(\lambda) = \det(A - \lambda I) = 0$ berechnen
- [ ] Eigenräume berechnen
- [ ] Algebraische vs. geometrische Vielfachheit unterscheiden und berechnen
- [ ] Diagonalisierbarkeits-Kriterium anwenden (geo = alg für jeden EW)
- [ ] Matrix diagonalisieren: $A = SDS^{-1}$
- [ ] Zusammenhang: $\det(A) = \prod \lambda_i$, $\text{Spur}(A) = \sum \lambda_i$
- [ ] **Beweis führen:** ONS-Eigenschaft nutzen für Eigenwert-Nachweis (Klausur 2.1)
- [ ] **Begründen:** Defekt bei EW = 0 (Klausur 2.2)

## Thema 6: Skalarprodukte (Tag 4) ⚡
- [ ] Axiome eines reellen Skalarprodukts
- [ ] Axiome eines komplexen Skalarprodukts (hermitesch!)
- [ ] Integral-Skalarprodukt $\langle f|g\rangle = \int \overline{f}g \, dx$ korrekt anwenden
- [ ] Norm berechnen: $\|v\| = \sqrt{\langle v|v\rangle}$
- [ ] Orthogonalität prüfen: $\langle u|v\rangle = 0$
- [ ] Konjugation im 1. Argument **nicht vergessen!**

## Thema 7: Gram-Schmidt-Verfahren (Tag 4) ⚡
- [ ] GS-Algorithmus Schritt für Schritt aufschreiben können
- [ ] Projektion: $\text{proj}_{e}(v) = \langle e | v \rangle \, e$
- [ ] Residuum: $\tilde{e}_k = v_k - \sum_{j<k} \langle e_j | v_k \rangle e_j$
- [ ] Normierung: $e_k = \tilde{e}_k / \|\tilde{e}_k\|$
- [ ] GS mit komplexem Integral-Skalarprodukt durchführen (Klausur 3!)
- [ ] **Probe:** Ergebnis auf Orthonormalität prüfen

## Thema 8: Jordan-Normalform (Tag 5) ⚡
- [ ] Jordan-Blöcke erkennen und aufschreiben
- [ ] Aus JNF ablesen: char. Polynom, Minimalpolynom, geo. VF, alg. VF
- [ ] Eigenraum über $V$-Matrix und JNF-Struktur bestimmen
- [ ] Hauptvektoren identifizieren und berechnen
- [ ] Zusammenhang JNF ↔ Diagonalisierbarkeit erklären

## Thema 9: Minimalpolynom & Cayley-Hamilton (Tag 5) ⚡
- [ ] Minimalpolynom Definition und Berechnung
- [ ] Satz von Cayley-Hamilton formulieren: $\chi_A(A) = 0$
- [ ] Cayley-Hamilton anwenden, um Matrixgleichungen zu zeigen (z.B. $A^2 = A$)
- [ ] Zusammenhang Min.poly ↔ JNF ↔ Char. Poly erklären

## Thema 10: Matrixexponential (Tag 5-6) ⚡
- [ ] Definition: $\exp(A) = \sum_{k=0}^\infty A^k/k!$
- [ ] Für Diagonalmatrizen: $\exp(D) = \text{diag}(e^{\lambda_i})$
- [ ] Spezialfall idempotente Matrix: $\exp(A) = I + (e-1)A$
- [ ] Anwendung auf DGL: $\dot{x} = Ax \Rightarrow x(t) = e^{tA} x_0$
- [ ] **Induktionsbeweis:** $A^m = A$ für $m \geq 1$ (Klausur 4.3)

<details>
<summary>🎓 <b>Wikipedia-Ergänzung: Matrixexponential</b></summary>
<blockquote>
Das Matrixexponential stiftet die Verbindung zwischen einer Matrix $A$ (oder Lie-Algebra) und der entsprechenden Lie-Gruppe. 
<br><br>
<b>Zentrale Eigenschaften:</b>
<ul>
    <li>$e^0 = I$</li>
    <li>Kommutierende Matrizen: $AB=BA \implies e^{A+B} = e^A e^B$</li>
    <li>Die Matrix $e^A$ ist immer invertierbar mit Inverser $e^{-A}$.</li>
    <li>Determinante: $\det(e^A) = e^{\text{Spur}(A)}$</li>
</ul>
<b>Berechnung:</b>
<ul>
    <li>Für diagonale Matrizen: Werte auf der Diagonale gewöhnlich exponentieren.</li>
    <li>Mit Jordan-Normalform $J$: $e^A = P e^J P^{-1}$.</li>
    <li>Nilpotente Matrizen: Taylor-Reihe bricht nach endlich vielen Termen ab.</li>
</ul>
</blockquote>
</details>

## Thema 11: Beweistechniken (Tag 6)
- [ ] Vollständige Induktion sauber aufschreiben (IA, IV, IS)
- [ ] Direkter Beweis: Voraussetzungen → logische Kette → Behauptung
- [ ] Widerspruchsbeweis: Gegenteil annehmen → Widerspruch herleiten
- [ ] "Zeige, dass..." Aufgaben: Was ist zu zeigen? Was darf ich verwenden?
- [ ] Begründungen präzise formulieren (nicht nur "Ergebnis hinschreiben")

## Thema 12: Bilinearformen & Adjungiertheit (Tag 7)
- [ ] Bilinearform, Sesquilinearform: Definition und Unterschied
- [ ] Darstellungsmatrix (Gram-Matrix) aufstellen
- [ ] Adjungierte Matrix: $A^*$ im Reellen ($A^T$) und Komplexen ($\overline{A}^T$)
- [ ] Selbstadjungiert, schiefsymmetrisch, normal: Definitionen
- [ ] Trigonalisierbarkeit (jede Matrix über $\mathbb{C}$ ist trigonalisierbar)

## Thema 13: Isometrien & Orthogonale Matrizen (Tag 7)
- [ ] Isometrie-Definition: $\|Av\| = \|v\|$
- [ ] Orthogonale Matrix: $A^TA = I$, Spalten = ONB
- [ ] $\det(A) = \pm 1$ für orthogonale Matrizen
- [ ] Rotation ($\det = 1$) vs. Spiegelung ($\det = -1$) unterscheiden
- [ ] Spektralsatz: symmetrische Matrizen = orthogonal diagonalisierbar

## Thema 14: Gruppentheorie Basics (Tag 7)
- [ ] Gruppe: 4 Axiome aufzählen
- [ ] Beispiele: $GL(n)$, $SL(n)$, $O(n)$, $SO(n)$, $S_n$
- [ ] Untergruppen-Kriterium
- [ ] Körper: Kombination zweier Gruppenstrukturen + Distributivgesetz

---

## 🎯 Prioritäts-Zusammenfassung

**MUSS (>60% der Klausurpunkte):**
1. Eigenwerte, Vielfachheiten, Defekt (Thema 5)
2. Gram-Schmidt mit komplexem SP (Thema 7)
3. JNF ablesen & interpretieren (Thema 8)
4. Cayley-Hamilton & Matrixexponential (Thema 9-10)
5. Determinanten-Regeln & Bedeutung (Thema 4)

**SOLLTE:**
6. Beweistechniken (Thema 11)
7. Bild-Kern-Algorithmus (Thema 3)
8. Skalarprodukt-Axiome (Thema 6)

**KANN (wenn Zeit übrig):**
9. Bilinearformen, Isometrien (Thema 12-13)
10. Gruppentheorie (Thema 14)
