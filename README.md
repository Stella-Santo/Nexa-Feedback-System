# 📥 Nexa™ Feedback System – Signature Edition by Stella

Ein hochprofessionelles Discord-Feedback-System mit elegantem Embed-Design, klarer Struktur und persönlichem Branding. Entwickelt für Communities und Organisationen, die Wert auf Qualität, Seriosität und visuelle Ästhetik legen.

---

## ✨ Funktionen

- 🎨 Schönes Embed-Design mit Icons, Farben und klarer Struktur
- 💬 Einfacher Slash-Command `/feedback`
- 👤 Zeigt Empfänger und Sender mit Profilbild
- 💖 Herz-Reaktion als stilvolle Rückmeldung
- 📬 Private Bestätigung per Nachricht
- 📅 Datum, Uhrzeit und „Made by Stella“ im Footer

---

## 🧠 Für wen ist das?

Für alle, die Feedback auf Discord sammeln wollen – egal ob für Teammitglieder, Community-Leitung oder Freunde.  
Du brauchst keine Programmiererfahrung – nur einen eigenen Discord-Bot.

---

## 📦 Installation

1. **Projekt herunterladen:**

```bash
git clone https://github.com/Stella-Santo/nexa-feedback-system.git
cd nexa-feedback-system


🔧 Vorbereitung
 Schritt 1: Discord-Bot erstellen
Falls du noch keinen Bot hast, erstelle einen unter: 👉 https://discord.com/developers/applications

 Dort bekommst du deinen Bot-Token – den brauchst du gleich.

Schritt 2: Token einfügen
Du hast zwei Möglichkeiten:

🔹 Variante A: Direkt im Code
Öffne die letzte Zeile in bot.py und ersetze:
TOKEN = os.getenv("DISCORD_TOKEN")  # Oder direkt: TOKEN = "DEIN_TOKEN"

🔹 Variante B: Über die Kommandozeile (empfohlen)
So setzt du deinen Token als Umgebungsvariable:
set DISCORD_TOKEN=dein_token        # Windows
export DISCORD_TOKEN=dein_token     # macOS/Linux

🚀 Bot starten über CMD (für Einsteiger)
Öffne CMD (Windows) oder Terminal (Mac/Linux)

Navigiere in den Projektordner:
cd pfad/zum/projektordner

Starte den Bot:
Wenn alles klappt, siehst du sowas wie:
✅ Bot ist online als Nexa™ Feedback System
🔄 Slash-Commands synchronisiert: 1

💬 So nutzt du den Bot
Geh auf deinen Discord-Server und gib ein:
/feedback

Dann:

Wähle die Person aus, für die du Feedback geben willst

Schreib deinen Text

Der Bot postet das Feedback automatisch im Feedback-Kanal

Du bekommst eine private Bestätigung

Und das Feedback bekommt ein 💖

🧪 Beispiel
/feedback target:@Stella text:"Antwortet schnell und ist nett!"



🤝 Kontakt
Bei Fragen, Ideen oder Feedback:
📧 stellaxsanto@gmail.com
🌐 github.com/Stella-Santo
