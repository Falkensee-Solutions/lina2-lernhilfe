# 6. Bilinearformen, Orthogonalität, Isometrien & Gruppentheorie

> [!INFO] Worum geht es hier? – Einfach erklärt
>
> In diesem Kapitel kommen mehrere Themen zusammen, die auf den ersten Blick unterschiedlich wirken, aber alle mit der Frage zu tun haben: Wie misst man Geometrie in Vektorräumen, und welche Abbildungen erhalten diese Geometrie?
>
> Eine **Bilinearform** ist wie ein verallgemeinertes Skalarprodukt – eine Funktion, die zwei Vektoren nimmt und eine Zahl zurückgibt, und die in beiden Argumenten linear ist. Im Komplexen heißt das Ganze **Sesquilinearform**, weil es im ersten Argument „anderthalblinear" (anti-linear) ist. Jede Bilinearform lässt sich durch eine Matrix $G$ darstellen: $\beta(v, w) = v^T G w$. Die **Signatur** von $G$ (wie viele positive, negative und Null-Eigenwerte sie hat) ist eine Invariante – sie ändert sich nicht, egal welche Basis du wählst.
>
> **Adjungiertheit** ist ein Konzept, bei dem du fragst: Wenn ich eine Matrix $A$ auf der linken Seite eines Skalarprodukts habe, welche Matrix $A^*$ muss ich auf die rechte Seite schreiben, damit der Wert gleich bleibt? Im Reellen ist das einfach die Transponierte, im Komplexen die konjugiert-Transponierte. Daraus ergeben sich wichtige Matrixklassen: **selbstadjungierte** Matrizen (alle Eigenwerte reell), **orthogonale** Matrizen (erhalten Längen und Winkel) und **unitäre** Matrizen (die komplexe Version davon).
>
> **Isometrien** sind Abbildungen, die alle Abstände erhalten – sie verzerren den Raum nicht. Orthogonale Matrizen sind genau die Isometrien des $\mathbb{R}^n$: entweder Drehungen (Determinante $+1$) oder Spiegelungen (Determinante $-1$). Die Menge aller solchen Matrizen bildet eine **Gruppe** – das heißt, du kannst sie hintereinander ausführen und jede rückgängig machen, und das Ergebnis ist wieder eine Isometrie.
>
> **Für die Nachklausur:** Dieses Kapitel ist hinter den Kulissen überall präsent. In der Klausur kam die Frage, ob eine Matrix symmetrisch sein kann (Aufgabe 1.9) – dafür brauchst du den **Spektralsatz**: symmetrische Matrizen sind diagonalisierbar. Die Gruppentheorie-Grundlagen (Definition einer Gruppe, Untergruppe, wichtige Beispiele wie $GL(n)$, $O(n)$, $SO(n)$) solltest du kennen – mindestens die Definitionen.

## 6.1 Bilinearformen

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Denk an Bilinearformen als ein verallgemeinertes Skalarprodukt. Eine Maschine, die zwei Vektoren als Input frisst und dir dazu passend genau einen reellen Wert/Skalar ausspuckt.
</blockquote>
</details>


### Definition

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Längentreu bedeutet: $\Vert f(v) \Vert = \Vert v \Vert$. Der komplette Zielraum wird als starrer Block gedreht oder an einer Achse geklappt.
</blockquote>
</details>

Eine **Bilinearform** $\beta: V \times V \to K$ ist linear in **beiden** Argumenten:
- $\beta(\alpha u + \beta v, w) = \alpha \beta(u, w) + \beta \beta(v, w)$
- $\beta(u, \alpha v + \beta w) = \alpha \beta(u, v) + \beta \beta(u, w)$

### Sesquilinearform (Halbilinearform)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
WICHTIG in Klausuren! Das komplexe Integral ist im 1. Argument stets 'antilinear'. Zieht man dort ein $i$ aus der Klammer, wandert es als komplex konjugiertes $-i$ nach draußen.
</blockquote>
</details>

Im Komplexen: $\sigma: V \times V \to \mathbb{C}$ ist linear im 2. Argument, **antilinear** im 1.:
$$\sigma(\alpha u, v) = \overline{\alpha} \, \sigma(u, v)$$

Ein komplexes Skalarprodukt ist eine **positiv definite hermitesche Sesquilinearform**.

### Darstellungsmatrix

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Jede Bilinearform kann durch schlichte Matrizen-Multiplikation formuliert werden: $v^T A w$. Das $A$ ist das Herzstück der Maschine.
</blockquote>
</details>

Bzgl. einer Basis $B = (b_1, \ldots, b_n)$:
$$G_{ij} = \beta(b_i, b_j)$$

Dann: $\beta(v, w) = [v]_B^T \cdot G \cdot [w]_B$

### Symmetrie/Antisymmetrie

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ist die Matrix $A=A^T$ (symmetrisch), dürfen links und rechts die Inputs getauscht werden. Antisymmetrie begegnet dir ständig als Kreuzprodukt in der Physik.
</blockquote>
</details>

- **Symmetrisch:** $\beta(u, v) = \beta(v, u)$ $\iff$ $G = G^T$
- **Antisymmetrisch:** $\beta(u, v) = -\beta(v, u)$ $\iff$ $G = -G^T$

## 6.2 Quadratische Formen

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Du steckst zwei mal den GLEICHEN Vektor v in die Formel hinein: $Q(v) = v^T A v$. Grafisch im Raum erzeugt das z.B. Parabolstäbe oder Schüsseln (wie $x^2 + y^2$).
</blockquote>
</details>

$$q(v) = \beta(v, v) = v^T G v$$

### Signatur

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Sylvester sagt: Auch wenn du dein Koordinatensystem brutal verbiegst, die Anzahl der '+', '-', und '0' Vorzeichen bleibt gleich. $(+,+)$ formt eine Schale nach oben, $(+,-)$ einen Pringles-artigen Sattel.
</blockquote>
</details>

Die Signatur $(p, q, r)$ gibt an:
- $p$ = Anzahl positiver Eigenwerte von $G$
- $q$ = Anzahl negativer Eigenwerte von $G$
- $r$ = Anzahl Null-Eigenwerte von $G$

**Trägheitssatz von Sylvester:** Die Signatur ist eine Invariante (unabhängig von der Basis).

## 6.3 Adjungiertheit

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Adjungiert = Das große Gegenstück. Wie bei komplexen Zahlen das Konjugieren, nur eben für Matrizen. Bei reellen Matrizen ist es einfach nur Matrix transponieren $
ightarrow A^T$.
</blockquote>
</details>


### Definition

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Längentreu bedeutet: $\Vert f(v) \Vert = \Vert v \Vert$. Der komplette Zielraum wird als starrer Block gedreht oder an einer Achse geklappt.
</blockquote>
</details>

$A^*$ heißt **Adjungierte** von $A$ bzgl. $\langle \cdot | \cdot \rangle$, wenn:
$$\langle Av | w \rangle = \langle v | A^* w \rangle \quad \text{für alle } v, w$$

### Konkret

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Der Standard-Move im Komplexen: Diagonale spiegeln (transponieren) UND sofort noch jedes 'i' zu einem '-i' machen.
</blockquote>
</details>

- **Reell** mit Standard-SP: $A^* = A^T$
- **Komplex** mit Standard-SP: $A^* = \overline{A}^T$ (konjugiert-transponiert)

### Spezialmatrizen

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Selbstadjungiert heißt Matrix = Matrix*. In der Quantenphysik garantiert das z.B., dass Messwerte der Schwingungen absolut reell bleiben.
</blockquote>
</details>


| Typ | Bedingung | Eigenschaft |
|-----|-----------|-------------|
| Selbstadjungiert (hermitesch) | $A^* = A$ | Alle EW reell |
| Schiefsymmetrisch | $A^* = -A$ | Alle EW rein imaginär |
| Normal | $A^*A = AA^*$ | Unitär diagonalisierbar |
| Orthogonal | $A^T A = I$ | $|{\lambda_i}| = 1$ |
| Unitär | $A^* A = I$ | $|{\lambda_i}| = 1$ |

## 6.4 Trigonalisierbarkeit

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Wenn Diagonalisieren scheitert (wie z.B. bei reinen Rotationsmatrizen, die keine reellen EW haben), formen wir in den komplexen Zahlen wenigstens eine hübsche obere Dreiecksmatrix.
</blockquote>
</details>


### Satz

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Über den komplexen Zahlen $\mathbb{C}$ hat wirklich jedes Polynom eine Wurzel. Deswegen ist das dort immer garantiert machbar. Im Reellen versuchen uns Rotationen das Leben schwerzumachen.
</blockquote>
</details>

Jede Matrix $A \in \mathbb{C}^{n \times n}$ ist **trigonalisierbar**, d.h. es gibt eine unitäre Matrix $U$ mit:
$$U^* A U = T \quad \text{(obere Dreiecksmatrix)}$$

### Schur-Zerlegung

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Der Beweis, dass wir diese Dreiecksstruktur durch eine absolut ordentliche Transformationsmatrix U erreichen, die selbst Isometrien (Basiswinkel) erhält.
</blockquote>
</details>

Für **normale** Matrizen ($A^*A = AA^*$) ist die Schur-Zerlegung eine Diagonalisierung:
$$U^* A U = D$$

> **Spektralsatz:** Selbstadjungierte (= hermitesche) Matrizen sind **unitär diagonalisierbar** mit **reellen** Eigenwerten.

## 6.5 Isometrien

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Transformationen absoluter Unveränderlichkeit! Weder stauchen noch strecken sie den Raum. Abstände zwischen Objektpunkten bleiben beim Bewegen erhalten.
</blockquote>
</details>


### Definition

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Längentreu bedeutet: $\Vert f(v) \Vert = \Vert v \Vert$. Der komplette Zielraum wird als starrer Block gedreht oder an einer Achse geklappt.
</blockquote>
</details>

$A$ ist eine **Isometrie**, wenn sie Abstände erhält:
$$\|Av\| = \|v\| \quad \text{für alle } v$$

Äquivalent: $\langle Av | Aw \rangle = \langle v | w \rangle$ für alle $v, w$

### Orthogonale Matrizen ($\mathbb{R}^n$)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Bestehen in Spalten und Reihen aus ONS-Einheitsvektoren. Orthogonal-Fehlerfalle für Klausuren beachten: Es kann auch eine negative Determinante haben, dann ist es keine reine Drehung, sondern eine Spiegelung!
</blockquote>
</details>

$A$ orthogonal $\iff A^T A = I \iff A^{-1} = A^T$

Eigenschaften:
- $\det(A) = \pm 1$
- Spalten (und Zeilen) bilden eine ONB

- $\det(A) = 1$: **Rotation** (spezielle orthogonale Gruppe $SO(n)$)
- $\det(A) = -1$: **Spiegelung** (oder Drehspiegelung)

### Unitäre Matrizen ($\mathbb{C}^n$)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Das komplexe Bruder-Gegenstück zur Isometrie. Da $A^* A = I$ gilt, liegen alle komplexen Eigenwerte genau auf einem Kreisring mit dem Maß-Betrag 1.
</blockquote>
</details>

$A$ unitär $\iff A^* A = I \iff A^{-1} = A^*$

## 6.6 Grundlagen der Gruppentheorie

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Muss man für die Klausur einordnen können! Gruppen sind abgeschottete Welten (Mengen) mit einer Verknüpfung, aus der man nie zufällig 'herausrechnen' kann (Abgeschlossenheit).
</blockquote>
</details>


### Gruppe

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Die 3 Grundsäulen: Du hast ein Element, das nichts tut (Nullvektor/Identität). Du kannst Aktionen rückgängig machen (Inverses/Subtraktion). Und die Ausführung bleibt in der Menge.
</blockquote>
</details>

$(G, \circ)$ ist eine **Gruppe**, wenn:
1. **Abgeschlossenheit:** $a \circ b \in G$ für alle $a, b \in G$
2. **Assoziativität:** $(a \circ b) \circ c = a \circ (b \circ c)$
3. **Neutrales Element:** $\exists e \in G: e \circ a = a \circ e = a$
4. **Inverses Element:** $\forall a \in G \, \exists a^{-1} \in G: a \circ a^{-1} = e$

**Abelsch:** Wenn zusätzlich $a \circ b = b \circ a$ (kommutativ)

### Wichtige Beispiele

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
$O(n)$ = Komplettes Set von Rotationen und spiegelnden Umklappungen. $SO(n)$ = 'Spezielle' Orthogonalgruppe, die Determinante ist strickt +1 (also absolute reine Drehung im Raum).
</blockquote>
</details>

- $GL(n, K)$: invertierbare $n \times n$-Matrizen (allgemeine lineare Gruppe)
- $SL(n, K)$: Matrizen mit $\det = 1$ (spezielle lineare Gruppe)
- $O(n)$: orthogonale Matrizen
- $SO(n)$: orthogonale Matrizen mit $\det = 1$ (Rotationen)
- $U(n)$: unitäre Matrizen
- $S_n$: Permutationsgruppe (symmetrische Gruppe)

### Untergruppen

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein elitärer Zirkel innerhalb der Gruppe. So bilden Drehungen stets eine Untergruppe, reine Spiegelungen aber z.B. nicht (da Spiegelung hinter Spiegelung sofort in Drehung verfällt – du fällst aus dem Club raus!).
</blockquote>
</details>

$H \subseteq G$ ist **Untergruppe** $\iff$
1. $e \in H$
2. $a, b \in H \Rightarrow a \circ b \in H$
3. $a \in H \Rightarrow a^{-1} \in H$

### Körper

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Sämtliche Regeln unserer Schulmathematik komprimiert. Plus, mal, minus, geteilt – es geht alles (außer geteilt durch 0). Ob reelle Zahlen, komplexe, oder kleine Restklassenkörper – hier klappen alle Vektorraum-Skalaraxiome vollumfänglich.
</blockquote>
</details>

$(K, +, \cdot)$ ist ein **Körper**, wenn:
- $(K, +)$ abelsche Gruppe mit neutralem Element 0
- $(K \setminus \{0\}, \cdot)$ abelsche Gruppe mit neutralem Element 1
- Distributivgesetz gilt

Beispiele: $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ (endliche Körper)

## 6.7 Reversibilität

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein Zusatzkonzept. Wenn Operatoren die Vorzeichen in der Matrix unter bestimmten Spiegelungs-Strukturen komplett invertieren. (Gibt es z.B. für Systeme mit vertauschter Zeitrichtung).
</blockquote>
</details>


Eine lineare Abbildung $A$ heißt **reversibel**, wenn sie:
- bijektiv ist ($\ker(A) = \{0\}$ und $\text{Bild}(A) = V$)
- Also invertierbar: $A^{-1}$ existiert

Äquivalent für quadratische Matrizen:
$$A \text{ invertierbar} \iff \det(A) \neq 0 \iff 0 \text{ ist kein Eigenwert} \iff \ker(A) = \{0\}$$
