# Formelblatt – LINA2 Nachklausur

> Kompakte Übersicht aller wichtigen Formeln und Sätze. Zum schnellen Nachschlagen und als letzte Wiederholung vor der Klausur.

---

## 1. Komplexe Zahlen

| Formel | |
|--------|-|
| $\overline{a+bi} = a - bi$ | Konjugation |
| $\|a+bi\| = \sqrt{a^2+b^2}$ | Betrag |
| $z \cdot \bar{z} = \|z\|^2$ | |
| $z = r e^{i\varphi}$ | Polarform |
| $e^{i\varphi} = \cos\varphi + i\sin\varphi$ | Euler |
| $\overline{z_1 z_2} = \bar{z}_1 \bar{z}_2$ | |

---

## 2. Vektorräume

$$\dim(V) = \dim(\ker(f)) + \dim(\text{Bild}(f))$$

- Kern = Lösungsraum von $Ax = 0$
- Bild = Spaltenraum von $A$ (Pivotspalten der Originalmatrix)
- Rang = Anzahl Pivotspalten

---

## 3. Determinanten

$$\det(AB) = \det(A)\det(B)$$
$$\det(A^T) = \det(A)$$
$$\det(A^{-1}) = \frac{1}{\det(A)}$$
$$\det(\lambda A) = \lambda^n \det(A) \quad (A \in K^{n \times n})$$
$$\det(SAS^{-1}) = \det(A)$$

Dreiecksmatrix: $\det(A) = \prod a_{ii}$

Laplace ($i$-te Zeile): $\det(A) = \sum_j (-1)^{i+j} a_{ij} \det(A_{ij})$

---

## 4. Eigenwerte

$$\chi_A(\lambda) = \det(A - \lambda I) = 0$$

$$1 \leq \text{geo. VF}(\lambda) \leq \text{alg. VF}(\lambda)$$

$$\det(A) = \prod_i \lambda_i, \qquad \text{Spur}(A) = \sum_i \lambda_i$$

Diagonalisierbar $\iff$ geo. VF = alg. VF für alle EW

---

## 5. Skalarprodukte

**Reell:** $\langle x | y \rangle = x^T y$

**Komplex:** $\langle x | y \rangle = \bar{x}^T y = x^* y$

**Funktionen:** $\langle f | g \rangle = \int_a^b \overline{f(x)} g(x) \, dx$

**Norm:** $\|v\| = \sqrt{\langle v|v\rangle}$

**Cauchy-Schwarz:** $|\langle u|v\rangle| \leq \|u\| \cdot \|v\|$

---

## 6. Gram-Schmidt

$$\tilde{e}_k = v_k - \sum_{j=1}^{k-1} \langle e_j | v_k \rangle \, e_j$$

$$e_k = \frac{\tilde{e}_k}{\|\tilde{e}_k\|}$$

---

## 7. Jordan-Normalform

Aus JNF $J$ ablesen:

| | Formel |
|-|--------|
| char. Polynom | $\chi_A = \prod (\lambda_i - \lambda)^{a_i}$ wobei $a_i$ = alg. VF |
| Minimalpolynom | $\mu_A = \prod (\lambda - \lambda_i)^{s_i}$ wobei $s_i$ = größter Block zu $\lambda_i$ |
| geo. VF($\lambda$) | Anzahl Blöcke zu $\lambda$ |
| alg. VF($\lambda$) | Summe der Blockgrößen zu $\lambda$ |
| Diagonalisierbar? | Alle Blöcke Größe 1 |
| $\det(A) = \det(J)$ | Produkt der Diagonaleinträge |

<details>
<summary>🎓 <b>Wikipedia-Ergänzung: Minimalpolynom</b></summary>
<blockquote>
Das Minimalpolynom $\mu_A$ einer quadratischen $n \times n$-Matrix $A$ über einem Körper $K$ ist das normierte Polynom kleinsten Grades, für das $\mu_A(A) = 0$ (die Nullmatrix) gilt.
<br><br>
<b>Eigenschaften:</b>
<ul>
    <li>Die Nullstellen des Minimalpolynoms stimmen genau mit den Nullstellen des charakteristischen Polynoms (also den Eigenwerten) überein, nur ggf. mit kleinerer algebraischer Vielfachheit.</li>
    <li>Die Vielfachheit eines Eigenwerts $\lambda$ im Minimalpolynom entspricht der <i>Größe des größten Jordan-Blocks</i> zu diesem Eigenwert in der jordanschen Normalform.</li>
    <li><b>Satz von Cayley-Hamilton:</b> Weil $\chi_A(A) = 0$, ist das char. Polynom ein Vielfaches des Minimalpolynoms ($\mu_A$ teilt $\chi_A$).</li>
</ul>
</blockquote>
</details>

---

## 8. Cayley-Hamilton & Matrixexponential

$$\chi_A(A) = 0 \quad \text{(Cayley-Hamilton)}$$

$$\exp(A) = \sum_{k=0}^{\infty} \frac{A^k}{k!}$$

**Spezialfälle:**
- $D = \text{diag}(\lambda_i)$: $\exp(D) = \text{diag}(e^{\lambda_i})$
- $A^2 = A$ (idempotent): $\exp(A) = I + (e-1)A$
- $A^2 = 0$ (nilpotent Ord. 2): $\exp(tA) = I + tA$
- DGL: $\dot{x} = Ax \implies x(t) = e^{tA} x_0$

---

## 9. Spezialmatrizen

| Typ | Bedingung | Eigenschaft |
|-----|-----------|-------------|
| Symmetrisch | $A = A^T$ | Reelle EW, orthogonal diagonalisierbar |
| Orthogonal | $A^TA = I$ | $\det = \pm 1$, Isometrie |
| Unitär | $A^*A = I$ | $|\lambda_i| = 1$ |
| Normal | $A^*A = AA^*$ | Unitär diagonalisierbar |
| Projektion | $P^2 = P$ | EW $\in \{0, 1\}$ |
| Nilpotent | $A^k = 0$ | Alle EW = 0 |

---

## 10. Isometrien & Orientierung

$$|\det(A)| = 1 \iff \text{volumentreu}$$
$$\det(A) > 0 \iff \text{orientierungserhaltend}$$

Orthogonal: $A^TA = I$, $\det(A) = \pm 1$
- $\det = +1$: Rotation ($SO(n)$)
- $\det = -1$: Spiegelung

---

## 11. Beweistechniken – Kurzreferenz

**Induktion:** IA (Basis) → IV (Annahme) → IS (Schritt)

**Widerspruch:** Negation annehmen → Widerspruch herleiten

**Unterraum zeigen:** 1) $0 \in U$ 2) $u+w \in U$ 3) $\lambda u \in U$

**"Zeige $A = B$" bei Mengen:** $A \subseteq B$ und $B \subseteq A$

---

## 12. Flüchtigkeitsfehler-Checkliste ⚠️

- [ ] Konjugation im 1. Argument bei komplexem SP: $\langle f|g\rangle = \int \overline{f} \cdot g$
- [ ] Vorzeichen bei Determinante: $(-1)^{i+j}$ bei Laplace
- [ ] Normierung **nicht vergessen** bei Gram-Schmidt
- [ ] $\det(\lambda A) = \lambda^{\mathbf{n}} \det(A)$, nicht $\lambda \det(A)$
- [ ] Symmetrische Matrizen: EW zu **verschiedenen** EW sind automatisch orthogonal
- [ ] Jordan-Block: 1en auf **Neben**diagonale, nicht Diagonale
- [ ] Minimalpolynom: **größter** Block, nicht kleinster!
- [ ] $A^2 = A$ beweisen, bevor du es in 4.3 und 4.4 verwendest
