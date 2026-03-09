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

<details>
<summary>🎓 <b>Wikipedia-Ergänzung: Ausartungsraum & Basiswechsel</b></summary>
<blockquote>
Nach <a href="https://de.wikipedia.org/wiki/Bilinearform">Wikipedia (Bilinearform)</a>:
<ul>
<li><strong>Ausartungsraum:</strong> Dies ist die Menge der Vektoren $v$, die in der Form mit allen anderen Vektoren $w$ den Wert 0 ergeben (d.h. $\beta(v,w) = 0$ für alle $w$). Sind Rechts- und Linkskern einer Form nur $\{0\}$, nennt man sie <em>nicht ausgeartet</em>. Ein Skalarprodukt ist ein prominentes Beispiel einer nicht ausgearteten Form.</li>
<li><strong>Basiswechsel:</strong> Wechselt man die Basis über eine Transformationsmatrix $S$, so ändert sich die darstellende Matrix $G$ nach der Regel $S^T G S$. Man sagt, die Matrizen $G$ und $S^T G S$ sind zueinander <em>kongruent</em>.</li>
</ul>
</blockquote>
</details>

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

<details>
<summary>🎓 <b>Wikipedia-Ergänzung: Polarisierung & Definitheit</b></summary>
<blockquote>
Nach <a href="https://de.wikipedia.org/wiki/Quadratische_Form">Wikipedia (Quadratische Form)</a>:
<ul>
<li><strong>Polarisierung:</strong> Zu jeder quadratischen Form existiert eindeutig eine symmetrische Bilinearform $\beta$, welche durch $\beta(x,y) = \frac{1}{2}(q(x+y) - q(x) - q(y))$ ("Polarisationsformel") zurückgewonnen werden kann. $q$ und $\beta$ bedingen sich gegenseitig zwingend.</li>
<li><strong>Definitheit & Geometrie:</strong> Betrachtet man quadratische Formen über reellen Zahlen, so eignen sie sich zur Einführung von Längen/Metriken genau dann, wenn sie <em>positiv definit</em> sind (Signatur $(n, 0, 0)$), die quadratischen Argumente also nur für den Nullvektor als einziges Null werden.</li>
<li><strong>Anwendungen:</strong> In der Zahlentheorie geht es oft um die Frage, welche ganzen Zahlen sich als Lösungs-Werte einer ganzzahligen quadratischen Form repräsentieren lassen (z.B. der berühmte <em>Vier-Quadrate-Satz</em>: Jede natürliche Zahl ist Summe von vier Quadratzahlen).</li>
</ul>
</blockquote>
</details>

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

<details>
<summary>🎓 <b>Wikipedia-Ergänzung: Satz von Mazur-Ulam & Struktur der Isometrien</b></summary>
<blockquote>
Nach <a href="https://de.wikipedia.org/wiki/Isometrie">Wikipedia (Isometrie)</a>:
<ul>
<li><strong>Struktur im $\mathbb{R}^n$:</strong> Jede Isometrie des euklidischen Raums in sich lässt sich als Verkettung einer orthogonalen (linearen) Abbildung und einer anschließenden Translation darstellen. Es gilt also immer $f(x) = Ax + b$ mit einer orthogonalen Matrix $A$.</li>
<li><strong>Satz von Mazur-Ulam (1932):</strong> Eine erstaunliche Verallgemeinerung besagt: Jede surjektive Isometrie zwischen zwei beliebigen reellen normierten Vektorräumen ist automatisch eine affine Abbildung (Bewahrt Geraden und Parallelität). Man muss also als Bedingung im rellen normierten Raum lediglich die Abständerhaltung fordern, und Linearität/Affinität springt zwingend von selbst heraus!</li>
</ul>
</blockquote>
</details>

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



> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 8, AP 3: Symmetriegruppe aufstellen](Uebungszettel_Originale.html#aufgabenpaket-3-symmetriegruppe-aufstellen)
> - [Übungsblatt 10: Untergruppen von Automorphismen](Uebungszettel_Originale.html#uebungsblatt-10-untergruppen-von-automorphismen)

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
<details>
<summary>🎓 <b>Wikipedia-Ergänzung: Klassifikation & Nebenklassen</b></summary>
<blockquote>
Nach <a href="https://de.wikipedia.org/wiki/Gruppe_(Mathematik)">Wikipedia (Gruppe)</a>:
<ul>
<li><strong>Satz von Lagrange:</strong> Für jede Untergruppe $H$ einer endlichen Gruppe $G$ gilt zwingend, dass die Ordnung (Elementanzahl) von $H$ stets exakt die Ordnung von $G$ teilt.</li>
<li><strong>Nebenklassen & Normalteiler:</strong> Jede Untergruppe $H$ induziert eine Äquivalenzrelation und somit eine Zerlegung der Gesamtgruppe in sogenannte <em>Nebenklassen</em>. Stimmen Links- und Rechtsnebenklassen völlig überein, nennt man $H$ einen <em>Normalteiler</em>, wodurch sich sogenannte Faktorgruppen bilden lassen.</li>
<li><strong>Lie-Gruppen:</strong> Die oben aufgeführten kontinuierlichen Matrixgruppen wie $GL(n)$ oder $O(n)$ sind nicht nur algebraische Gruppen, sondern gleichzeitig topologische Mannigfaltigkeiten, und spielen in der theoretischen Physik als <em>Lie-Gruppen</em> eine überragende Rolle (etwa zur Beschreibung von Naturgesetzen und Symmetrien).</li>
</ul>
</blockquote>
</details>

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
