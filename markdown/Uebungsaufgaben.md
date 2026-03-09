# Übungsaufgaben mit Lösungshinweisen

> Bearbeite jede Aufgabe selbständig, bevor du die Hinweise liest!
> Die Aufgaben sind nach Klausurrelevanz sortiert.

---

## ⚡ Aufgabenblock 1: Eigenwerte & Beweise (wie Klausuraufgabe 2)

### Aufgabe 1.1 – ONS und Eigenwerte
Gegeben: $v_1 = \frac{1}{\sqrt{2}}\binom{1}{1}$, $v_2 = \frac{1}{\sqrt{2}}\binom{1}{-1}$ (ONS in $\mathbb{R}^2$) und $M = 3 v_1 v_1^T + 5 v_2 v_2^T$.

a) Zeige: $Mv_1 = 3v_1$ und $Mv_2 = 5v_2$.  
b) Berechne $M$ explizit als $2 \times 2$-Matrix.  
c) Ist $M$ diagonalisierbar? Begründe!

**Hinweis a):** Setze $v_1$ in $M$ ein und nutze $v_i^T v_j = \delta_{ij}$.  
**Hinweis b):** $v_1 v_1^T = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$ berechnen, analog $v_2 v_2^T$, dann einsetzen.  
**Hinweis c):** Prüfe: geo. VF = alg. VF für jeden EW? Oder: Haben wir eine Basis aus EV?

<details>
<summary>Lösung</summary>

a) $Mv_1 = 3v_1(v_1^Tv_1) + 5v_2(v_2^Tv_1) = 3v_1 \cdot 1 + 5v_2 \cdot 0 = 3v_1$ ✓

b) $M = 3 \cdot \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix} + 5 \cdot \frac{1}{2}\begin{pmatrix}1&-1\\-1&1\end{pmatrix} = \begin{pmatrix}4&-1\\-1&4\end{pmatrix}$

c) Ja, denn $v_1, v_2$ sind linear unabhängig und bilden eine Basis aus Eigenvektoren. Alternativ: $M$ ist symmetrisch ($M = M^T$), also nach Spektralsatz diagonalisierbar.
</details>

---

### Aufgabe 1.2 – Defekt und Rang
Gegeben: $A \in \mathbb{R}^{4 \times 4}$ mit $\chi_A(\lambda) = \lambda^2(\lambda - 3)(\lambda + 1)$.

a) Welche Eigenwerte hat $A$? Gib die algebraischen Vielfachheiten an.  
b) Was kannst du über den Defekt von $A$ sagen?  
c) Was kannst du über den Rang von $A$ sagen?  
d) Ist $A$ invertierbar? Begründe!

**Hinweis b):** Defekt = geo. VF(0). Welche Schranken gelten?  
**Hinweis c):** Rangsatz: Rang = $n$ - Defekt.

<details>
<summary>Lösung</summary>

a) EW: $\lambda_1 = 0$ (alg. VF 2), $\lambda_2 = 3$ (alg. VF 1), $\lambda_3 = -1$ (alg. VF 1)

b) Defekt = geo. VF(0). Es gilt: $1 \leq \text{geo. VF}(0) \leq \text{alg. VF}(0) = 2$. Also Defekt $\in \{1, 2\}$.

c) Rang = $4 - \text{Defekt} \in \{2, 3\}$.

d) Nein! $\lambda = 0$ ist Eigenwert, also $\det(A) = 0 \cdot 0 \cdot 3 \cdot (-1) = 0$.
</details>

---

### Aufgabe 1.3 – Symmetrische Matrix und Diagonalisierbarkeit
Zeige: Wenn $A \in \mathbb{R}^{n \times n}$ einen Jordan-Block der Größe $k \geq 2$ besitzt, dann ist $A$ **nicht** symmetrisch.

**Hinweis:** Was weißt du über die Diagonalisierbarkeit symmetrischer Matrizen (Spektralsatz)?

<details>
<summary>Lösung</summary>

Angenommen $A$ wäre symmetrisch. Dann ist $A$ nach dem Spektralsatz (reell, orthogonal) diagonalisierbar. D.h. alle Jordan-Blöcke haben Größe 1. Widerspruch zu der Annahme, dass ein Block Größe $k \geq 2$ hat. Also kann $A$ nicht symmetrisch sein. $\square$
</details>

---

## ⚡ Aufgabenblock 2: Gram-Schmidt (wie Klausuraufgabe 3)

### Aufgabe 2.1 – GS im Reellen
Wende Gram-Schmidt auf $v_1 = (1, 1, 0)^T$ und $v_2 = (1, 0, 1)^T$ an (Standard-Skalarprodukt in $\mathbb{R}^3$).

**Hinweis:** Schritt 1: Normiere $v_1$. Schritt 2: Orthogonalisiere $v_2$ bzgl. $e_1$, dann normiere.

<details>
<summary>Lösung</summary>

$\|v_1\| = \sqrt{2}$, also $e_1 = \frac{1}{\sqrt{2}}(1,1,0)^T$

$\langle e_1 | v_2 \rangle = \frac{1}{\sqrt{2}}(1 \cdot 1 + 1 \cdot 0 + 0 \cdot 1) = \frac{1}{\sqrt{2}}$

$\tilde{e}_2 = v_2 - \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}(1,1,0)^T = (1,0,1)^T - \frac{1}{2}(1,1,0)^T = (\frac{1}{2}, -\frac{1}{2}, 1)^T$

$\|\tilde{e}_2\| = \sqrt{\frac{1}{4} + \frac{1}{4} + 1} = \sqrt{\frac{3}{2}}$

$e_2 = \frac{1}{\sqrt{3/2}}(\frac{1}{2}, -\frac{1}{2}, 1)^T = \frac{1}{\sqrt{6}}(1, -1, 2)^T$

Probe: $\langle e_1 | e_2 \rangle = \frac{1}{\sqrt{12}}(1 - 1 + 0) = 0$ ✓
</details>

---

### Aufgabe 2.2 – GS mit komplexem Integral-Skalarprodukt
Gegeben: $f_1(x) = 1$, $f_2(x) = e^{ix}$ auf $[0, 2\pi]$ mit $\langle f|g\rangle = \frac{1}{2\pi}\int_0^{2\pi} \overline{f(x)} g(x) \, dx$.

Bestimme eine ONB von $\text{span}(f_1, f_2)$.

**Hinweis:** Berechne $\|f_1\|$, dann $\langle e_1 | f_2 \rangle$. Nutze $\int_0^{2\pi} e^{ix} dx = 0$.

<details>
<summary>Lösung</summary>

$\|f_1\|^2 = \frac{1}{2\pi}\int_0^{2\pi} 1 \, dx = 1$, also $e_1 = 1$.

$\langle e_1 | f_2 \rangle = \frac{1}{2\pi}\int_0^{2\pi} 1 \cdot e^{ix} dx = \frac{1}{2\pi}\left[\frac{e^{ix}}{i}\right]_0^{2\pi} = \frac{1}{2\pi} \cdot \frac{e^{2\pi i} - 1}{i} = 0$

Also $\tilde{e}_2 = f_2 - 0 = e^{ix}$.

$\|\tilde{e}_2\|^2 = \frac{1}{2\pi}\int_0^{2\pi} e^{-ix} \cdot e^{ix} dx = \frac{1}{2\pi}\int_0^{2\pi} 1 \, dx = 1$

Also $e_1(x) = 1$ und $e_2(x) = e^{ix}$ – sie waren schon orthonormal!
</details>

---

## ⚡ Aufgabenblock 3: JNF, Minimalpolynom, Cayley-Hamilton (wie Klausuraufgaben 1 + 4)

### Aufgabe 3.1 – JNF ablesen
Gegeben die JNF:
$$J = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & -3 \end{pmatrix}$$

a) Wie lautet $\chi_A$?  
b) Wie lautet $\mu_A$?  
c) Ist $A$ diagonalisierbar?  
d) geo. VF(2) = ? geo. VF(-3) = ?  
e) $\det(A) = ?$, $\text{Spur}(A) = ?$

<details>
<summary>Lösung</summary>

a) $\chi_A(\lambda) = (\lambda - 2)^3(\lambda + 3)$

b) $\mu_A(\lambda) = (\lambda - 2)^2(\lambda + 3)$ (größter Block zu EW 2 hat Größe 2)

c) Nein, der Jordan-Block $J_2(2)$ hat Größe 2.

d) geo. VF(2) = 2 (zwei Blöcke: $J_2(2)$ und $J_1(2)$). geo. VF(-3) = 1.

e) $\det(A) = 2^3 \cdot (-3) = -24$. $\text{Spur}(A) = 2+2+2+(-3) = 3$.
</details>

---

### Aufgabe 3.2 – Cayley-Hamilton anwenden
$A \in \mathbb{R}^{3 \times 3}$ mit $\chi_A(\lambda) = -\lambda^3 + 4\lambda$.

a) Finde die Eigenwerte.  
b) Drücke $A^3$ durch niedrigere Potenzen von $A$ aus.  
c) Berechne $A^4$ (unter Verwendung von b).

**Hinweis b):** Cayley-Hamilton: $\chi_A(A) = 0$, also $-A^3 + 4A = 0$.

<details>
<summary>Lösung</summary>

a) $-\lambda^3 + 4\lambda = -\lambda(\lambda^2 - 4) = -\lambda(\lambda-2)(\lambda+2) = 0$. EW: $0, 2, -2$.

b) $-A^3 + 4A = 0 \implies A^3 = 4A$

c) $A^4 = A \cdot A^3 = A \cdot 4A = 4A^2$
</details>

---

### Aufgabe 3.3 – Matrixexponential
$A$ ist diagonalisierbar mit einzigem Eigenwert $\lambda = 0$ (d.h. $A = 0$). Berechne $\exp(A)$.

**Hinweis:** Was ist $A^k$ für $k \geq 1$?

<details>
<summary>Lösung</summary>

$A = 0$, also $A^k = 0$ für $k \geq 1$.

$\exp(A) = I + \sum_{k=1}^\infty \frac{0}{k!} = I$

Also $\exp(0) = I$. (Das ist konsistent: $e^0 = 1$.)
</details>

---

### Aufgabe 3.4 – Matrixexponential (schwieriger)
$A \in \mathbb{R}^{2 \times 2}$, nilpotent der Ordnung 2 (d.h. $A^2 = 0$ aber $A \neq 0$). Berechne $\exp(tA)$.

<details>
<summary>Lösung</summary>

$A^k = 0$ für $k \geq 2$.

$\exp(tA) = I + tA + \frac{(tA)^2}{2!} + \cdots = I + tA + 0 = I + tA$

Also $\exp(tA) = I + tA$ (Polynomformel!).
</details>

---

## Aufgabenblock 4: Determinanten & Beweise

### Aufgabe 4.1 – Determinante und Ähnlichkeit
Zeige: Ähnliche Matrizen haben die gleiche Determinante, d.h. $\det(SAS^{-1}) = \det(A)$.

<details>
<summary>Lösung</summary>

$\det(SAS^{-1}) = \det(S) \cdot \det(A) \cdot \det(S^{-1}) = \det(S) \cdot \det(A) \cdot \frac{1}{\det(S)} = \det(A)$

(Verwendet: Produktregel und $\det(S^{-1}) = 1/\det(S)$.) $\square$
</details>

---

### Aufgabe 4.2 – Orientierung und Volumen
$A \in \mathbb{R}^{3 \times 3}$ mit Eigenwerten $2, -1, 3$.

a) Ist $A$ volumentreu?  
b) Ist $A$ orientierungserhaltend?  
c) Ist $A$ invertierbar?

<details>
<summary>Lösung</summary>

$\det(A) = 2 \cdot (-1) \cdot 3 = -6$

a) $|\det(A)| = 6 \neq 1$ → **nicht** volumentreu.
b) $\det(A) = -6 < 0$ → **nicht** orientierungserhaltend.
c) $\det(A) = -6 \neq 0$ → **ja**, invertierbar.
</details>

---

## Aufgabenblock 5: Gemischte Beweisaufgaben

### Aufgabe 5.1 – Induktionsbeweis
Zeige per Induktion: Für eine nilpotente Matrix $N$ mit $N^k = 0$ gilt:
$$(I - N)^{-1} = I + N + N^2 + \cdots + N^{k-1}$$

**Hinweis:** Multipliziere $(I-N)$ mit der rechten Seite und vereinfache.

<details>
<summary>Lösung</summary>

Setze $S = I + N + N^2 + \cdots + N^{k-1}$.

$(I - N) \cdot S = S - NS = (I + N + \cdots + N^{k-1}) - (N + N^2 + \cdots + N^k)$

$= I + (N - N) + (N^2 - N^2) + \cdots + (N^{k-1} - N^{k-1}) - N^k = I - N^k = I - 0 = I$

Also $(I-N) \cdot S = I$, d.h. $S = (I-N)^{-1}$. $\square$

(Das ist eigentlich die geometrische Reihe für Matrizen!)
</details>

---

### Aufgabe 5.2 – Projektionsbeweis
Sei $P$ eine Projektion ($P^2 = P$). Zeige:
a) $\ker(P) = \text{Bild}(I - P)$  
b) $\text{Bild}(P) = \ker(I - P)$  
c) $V = \ker(P) \oplus \text{Bild}(P)$

**Hinweis a):** Zeige $\subseteq$ und $\supseteq$ getrennt.

<details>
<summary>Lösung</summary>

a) "$\subseteq$": Sei $v \in \ker(P)$, also $Pv = 0$. Dann $v = v - 0 = v - Pv = (I-P)v \in \text{Bild}(I-P)$.
"$\supseteq$": Sei $v = (I-P)w$ für ein $w$. Dann $Pv = P(I-P)w = (P - P^2)w = (P - P)w = 0$, also $v \in \ker(P)$.

b) Analog: $v \in \text{Bild}(P) \iff v = Pw \iff (I-P)v = v - Pv = Pw - P^2w = 0 \iff v \in \ker(I-P)$.

c) Für jedes $v$: $v = Pv + (I-P)v$. Dabei $Pv \in \text{Bild}(P)$ und $(I-P)v \in \text{Bild}(I-P) = \ker(P)$. Schnitt: Wenn $v \in \ker(P) \cap \text{Bild}(P)$, dann $Pv = 0$ und $v = Pw$, also $0 = Pv = P^2w = Pw = v$. $\square$
</details>

---

### Aufgabe 5.3 – EW von Matrixpotenzen
Zeige: Wenn $\lambda$ Eigenwert von $A$ mit Eigenvektor $v$, dann ist $\lambda^k$ Eigenwert von $A^k$ mit gleichem Eigenvektor $v$.

**Hinweis:** Induktion über $k$.

<details>
<summary>Lösung</summary>

IA ($k=1$): $A^1 v = Av = \lambda v = \lambda^1 v$ ✓

IS ($k \to k+1$): Angenommen $A^k v = \lambda^k v$.

$A^{k+1} v = A \cdot A^k v = A \cdot \lambda^k v = \lambda^k \cdot Av = \lambda^k \cdot \lambda v = \lambda^{k+1} v$ $\square$
</details>
