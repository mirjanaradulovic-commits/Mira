import os

# Datei-Name festlegen
filename = "app.log"

# 1. Prüfen, ob die Datei existiert. Wenn nicht: Automatisch erstellen!
if not os.path.exists(filename):
    print(f"Erstelle Test-Datei '{filename}'...")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("2026-07-22 10:00:01 [INFO] Anwendung gestartet\n")
        f.write("2026-07-22 10:00:05 [WARNING] Speicher fast voll\n")
        f.write("2026-07-22 10:00:10 [ERROR] Verbindung zur Datenbank fehlgeschlagen\n")
        f.write("2026-07-22 10:00:15 [INFO] Benutzer hat sich angemeldet\n")
        f.write("2026-07-22 10:00:20 [ERROR] Datei nicht gefunden\n")
        f.write("2026-07-22 10:00:25 [WARNING] Hohe CPU-Auslastung\n")

# 2. Zähler-Dictionary anlegen
log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

# 3. Datei einlesen und zählen
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        if "[INFO]" in line:
            log_counts["INFO"] += 1
        elif "[WARNING]" in line:
            log_counts["WARNING"] += 1
        elif "[ERROR]" in line:
            log_counts["ERROR"] += 1

# 4. Gesamtzahl berechnen (wie die Summe in Calc)
total_logs = sum(log_counts.values())

# 5. Zusammenfassung sauber ausgeben
print("\n=== LOG-DATEI AUSWERTUNG ===")
for level, count in log_counts.items():
    percent = (count / total_logs) * 100 if total_logs > 0 else 0
    print(f"{level:7}: {count} mal ({percent:.2f}%)")

print("----------------------------")
print(f"Gesamt : {total_logs} Log-Einträge")