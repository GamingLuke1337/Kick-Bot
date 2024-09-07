Dieser Discord Bot ermöglicht es Administratoren, alle Mitglieder ohne eine bestimmte Rolle per Slash Command zu kicken. Der Bot wird lokal gehostet und erfordert eine Administrator-Berechtigung, um diesen Befehl auszuführen.

## Voraussetzungen

Bevor du den Bot ausführen kannst, stelle sicher, dass die folgenden Voraussetzungen erfüllt sind:

1. **Python 3.8 oder höher**: Installiere Python von der offiziellen [Python-Website](https://www.python.org/).
2. **Discord Developer Account**: Erstelle eine neue Bot-Anwendung im [Discord Developer Portal](https://discord.com/developers/applications) und erhalte den Bot-Token.
3. **Bot Token**: Kopiere den Token deines Bots aus dem Developer Portal.
4. **discord.py**: Der Bot nutzt `discord.py` und `app_commands`, um mit der Discord API zu interagieren.

## Installation

1. **Projekt aufsetzen**:
   - Klone dieses Repository oder erstelle eine lokale Kopie des Codes.

   ```bash
   git clone https://github.com/deinBenutzername/discord-role-kick-bot.git
   cd discord-role-kick-bot
   ```

2. **Installiere Abhängigkeiten**:
   - Installiere die Python-Bibliotheken mit `pip`.

   ```bash
   pip install discord.py
   ```

3. **Bot-Token konfigurieren**:
   - Öffne die Datei `bot.py` und ersetze den Wert von `your_token` mit deinem Bot-Token aus dem Discord Developer Portal.

   ```python
   TOKEN = 'your_token'  # Hier deinen Bot-Token einfügen
   ```

4. **Rollen-ID festlegen**:
   - Finde die ID der Rolle, die Mitglieder haben müssen (z. B. "Staatsbürger"). Ersetze `required_role_id` im Code mit dieser ID.

   ```python
   required_role_id = 1234567890  # Ersetze dies mit der ID der "Staatsbürger"-Rolle
   ```

   Um die Rollen-ID zu finden, aktiviere den Entwicklermodus in Discord und klicke mit der rechten Maustaste auf die Rolle, um die ID zu kopieren.

## Verwendung

1. **Starte den Bot**:
   - Führe das Python-Skript aus, um den Bot zu starten.

   ```bash
   python bot.py
   ```

2. **Slash Command verwenden**:
   - Nachdem der Bot gestartet wurde, können Administratoren den Slash Command `/kick` verwenden, um alle Mitglieder ohne die festgelegte Rolle zu kicken.

   ```bash
   /kick
   ```

   - Der Bot wird dann alle Mitglieder, die nicht die angegebene Rolle besitzen, aus dem Server entfernen.

## Wichtige Hinweise

- **Berechtigungen**: Stelle sicher, dass der Bot über die nötigen Berechtigungen verfügt, um Mitglieder zu kicken. Dazu benötigt er die Berechtigung `Mitglieder kicken` und muss in der Rollen-Hierarchie über den Mitgliedern stehen, die gekickt werden sollen.
- **Bots nicht kicken**: Der Bot wird andere Bots nicht kicken, nur Mitglieder ohne die festgelegte Rolle.
- **Ephemeral Messages**: Der Bot wird eine "ephemeral" Nachricht an den Administrator senden, die nur von ihm gesehen werden kann, um die Anzahl der gekickten Mitglieder zu bestätigen.
  


Dieses Projekt ist unter der MIT-Lizenz lizenziert.
