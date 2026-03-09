# 6. Bilinearformen, Orthogonalität, Isometrien & Gruppentheorie

## 6.1 Bilinearformen

### Definition
Eine **Bilinearform** $\beta: V \times V \to K$ ist linear in **beiden** Argumenten:
- $\beta(\alpha u + \beta v, w) = \alpha \beta(u, w) + \beta \beta(v, w)$
- $\beta(u, \alpha v + \beta w) = \alpha \beta(u, v) + \beta \beta(u, w)$

### Sesquilinearform (Halbilinearform)
Im Komplexen: $\sigma: V \times V \to \mathbb{C}$ ist linear im 2. Argument, **antilinear** im 1.:
$$\sigma(\alpha u, v) = \overline{\alpha} \, \sigma(u, v)$$

Ein komplexes Skalarprodukt ist eine **positiv definite hermitesche Sesquilinearform**.

### Darstellungsmatrix
Bzgl. einer Basis $B = (b_1, \ldots, b_n)$:
$$G_{ij} = \beta(b_i, b_j)$$

Dann: $\beta(v, w) = [v]_B^T \cdot G \cdot [w]_B$

### Symmetrie/Antisymmetrie
- **Symmetrisch:** $\beta(u, v) = \beta(v, u)$ $\iff$ $G = G^T$
- **Antisymmetrisch:** $\beta(u, v) = -\beta(v, u)$ $\iff$ $G = -G^T$

## 6.2 Quadratische Formen
$$q(v) = \beta(v, v) = v^T G v$$

### Signatur
Die Signatur $(p, q, r)$ gibt an:
- $p$ = Anzahl positiver Eigenwerte von $G$
- $q$ = Anzahl negativer Eigenwerte von $G$
- $r$ = Anzahl Null-Eigenwerte von $G$

**Trägheitssatz von Sylvester:** Die Signatur ist eine Invariante (unabhängig von der Basis).

## 6.3 Adjungiertheit

### Definition
$A^*$ heißt **Adjungierte** von $A$ bzgl. $\langle \cdot | \cdot \rangle$, wenn:
$$\langle Av | w \rangle = \langle v | A^* w \rangle \quad \text{für alle } v, w$$

### Konkret
- **Reell** mit Standard-SP: $A^* = A^T$
- **Komplex** mit Standard-SP: $A^* = \overline{A}^T$ (konjugiert-transponiert)

### Spezialmatrizen

| Typ | Bedingung | Eigenschaft |
|-----|-----------|-------------|
| Selbstadjungiert (hermitesch) | $A^* = A$ | Alle EW reell |
| Schiefsymmetrisch | $A^* = -A$ | Alle EW rein imaginär |
| Normal | $A^*A = AA^*$ | Unitär diagonalisierbar |
| Orthogonal | $A^T A = I$ | $|{\lambda_i}| = 1$ |
| Unitär | $A^* A = I$ | $|{\lambda_i}| = 1$ |

## 6.4 Trigonalisierbarkeit

### Satz
Jede Matrix $A \in \mathbb{C}^{n \times n}$ ist **trigonalisierbar**, d.h. es gibt eine unitäre Matrix $U$ mit:
$$U^* A U = T \quad \text{(obere Dreiecksmatrix)}$$

### Schur-Zerlegung
Für **normale** Matrizen ($A^*A = AA^*$) ist die Schur-Zerlegung eine Diagonalisierung:
$$U^* A U = D$$

> **Spektralsatz:** Selbstadjungierte (= hermitesche) Matrizen sind **unitär diagonalisierbar** mit **reellen** Eigenwerten.

## 6.5 Isometrien

### Definition
$A$ ist eine **Isometrie**, wenn sie Abstände erhält:
$$\|Av\| = \|v\| \quad \text{für alle } v$$

Äquivalent: $\langle Av | Aw \rangle = \langle v | w \rangle$ für alle $v, w$

### Orthogonale Matrizen ($\mathbb{R}^n$)
$A$ orthogonal $\iff A^T A = I \iff A^{-1} = A^T$

Eigenschaften:
- $\det(A) = \pm 1$
- Spalten (und Zeilen) bilden eine ONB
- $\det(A) = 1$: **Rotation** (spezielle orthogonale Gruppe $SO(n)$)
- $\det(A) = -1$: **Spiegelung** (oder Drehspiegelung)

### Unitäre Matrizen ($\mathbb{C}^n$)
$A$ unitär $\iff A^* A = I \iff A^{-1} = A^*$

## 6.6 Grundlagen der Gruppentheorie

### Gruppe
$(G, \circ)$ ist eine **Gruppe**, wenn:
1. **Abgeschlossenheit:** $a \circ b \in G$ für alle $a, b \in G$
2. **Assoziativität:** $(a \circ b) \circ c = a \circ (b \circ c)$
3. **Neutrales Element:** $\exists e \in G: e \circ a = a \circ e = a$
4. **Inverses Element:** $\forall a \in G \, \exists a^{-1} \in G: a \circ a^{-1} = e$

**Abelsch:** Wenn zusätzlich $a \circ b = b \circ a$ (kommutativ)

### Wichtige Beispiele
- $GL(n, K)$: invertierbare $n \times n$-Matrizen (allgemeine lineare Gruppe)
- $SL(n, K)$: Matrizen mit $\det = 1$ (spezielle lineare Gruppe)
- $O(n)$: orthogonale Matrizen
- $SO(n)$: orthogonale Matrizen mit $\det = 1$ (Rotationen)
- $U(n)$: unitäre Matrizen
- $S_n$: Permutationsgruppe (symmetrische Gruppe)

### Untergruppen
$H \subseteq G$ ist **Untergruppe** $\iff$
1. $e \in H$
2. $a, b \in H \Rightarrow a \circ b \in H$
3. $a \in H \Rightarrow a^{-1} \in H$

### Körper
$(K, +, \cdot)$ ist ein **Körper**, wenn:
- $(K, +)$ abelsche Gruppe mit neutralem Element 0
- $(K \setminus \{0\}, \cdot)$ abelsche Gruppe mit neutralem Element 1
- Distributivgesetz gilt

Beispiele: $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ (endliche Körper)

## 6.7 Reversibilität

Eine lineare Abbildung $A$ heißt **reversibel**, wenn sie:
- bijektiv ist ($\ker(A) = \{0\}$ und $\text{Bild}(A) = V$)
- Also invertierbar: $A^{-1}$ existiert

Äquivalent für quadratische Matrizen:
$$A \text{ invertierbar} \iff \det(A) \neq 0 \iff 0 \text{ ist kein Eigenwert} \iff \ker(A) = \{0\}$$
