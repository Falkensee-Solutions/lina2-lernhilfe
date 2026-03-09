# 📐 LINA2 Lernhilfe

**Lineare Algebra II – FU Berlin – WiSe 2025/26**  
PD Dr. Marcus Weber · [Kursseite](https://www.zib.de/userpage/weber/LINA2.html)

> Nachklausur: **19.03.2026**, 8:00 Uhr, Gr. Hörsaal Takustr. 9

---

## 🌐 Live-Seite

👉 **[Zur Lernhilfe](https://falkensee-solutions.github.io/lina2-lernhilfe/)**

---

## 📚 Inhalt

| Dokument | Beschreibung |
|---|---|
| [9-Tage-Lernplan](docs/00_Lernplan.html) | Strukturierter Plan mit täglichen Aufgaben |
| Zusammenfassungen 1–6 | Alle Themen von komplexen Zahlen bis Isometrien |
| [Das große Ganze](docs/Vernetzung_Das_Grosse_Ganze.html) | Vernetzung aller Themen untereinander |
| [Karteikarten](docs/Karteikarten.html) | 30+ Karteikarten zum aktiven Wiederholen |
| [Checkliste](docs/Checkliste_Themen.html) | Themen-Checkliste mit Prioritäten |
| [Übungsaufgaben](docs/Uebungsaufgaben.html) | 13 Aufgaben mit Hinweisen & Lösungen |
| [Formelblatt](docs/Formelblatt.html) | Kompaktes Formelblatt zum Nachschlagen |
| [Klausur-Musterlösungen](docs/Klausur_Musterloesungen.html) | Vollständige Lösungen der Erstklausur |

## 🛠 Lokales Bauen

```bash
# Voraussetzung: Python 3
python3 build.py
open docs/index.html
```

Die Markdown-Quellen liegen in `markdown/`, die generierten HTML-Seiten in `docs/`.

## 📖 GitHub Pages aktivieren

1. Repo auf GitHub pushen
2. **Settings → Pages → Source: Deploy from a branch**
3. Branch: `main`, Ordner: `/docs`
4. Save → Seite ist nach ca. 1 Min. live

## 🖨 PDF-Export

Jede Seite kann über `Cmd+P` → „Als PDF speichern" exportiert werden.  
Die Druckansicht ist optimiert (Navigation wird ausgeblendet).

## 📝 Beitragen

Fehler gefunden? Pull Requests und Issues sind willkommen!

---

*Erstellt zur Klausurvorbereitung LINA2 WiSe 2025/26 an der FU Berlin.*
