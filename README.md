# Gemeindeexekutiven des Kanton Zürich
Auswertungen für das Projekt [Wer regiert uns](https://interaktiv.tagesanzeiger.ch/2021/wer-regiert-uns/) des Tages-Anzeigers.
## Daten
`data/Gemeinde_Exekutive - daten.csv` enthält alle Informationen über die Gemeinde- und Stadtratsmitglieder.  

**!!Wichtig 1!!**  
Manche Gemeinden haben `Jahrgang` und `Partei` nicht pro Gemeinderat ausgewiesen, sondern nur mitgeteilt, welche Jahrgänge respektiv Parteien in ihrem Gemeinderat vorkommen. Diese Angaben wurden zufällig Gemeinderät:innen dieser Gemeinde zugeordnet und **in der Spalte `jahrgang_nicht_zugeordnet` sowie `partei_nicht_zugeordnet` vermerkt.**
  
**!!Wichtig 2!!**
Vakante Sitze wurden mit `Name` *vakant* erfasst.
  

Column | Type | Info
--- | --- | ---
**Gemeinde** | `string` | Name der Geemeinde
**Name** | `string` | Name und Infos des Gemeinderates, nicht bereinigt
**Name_cleaned** | `string` | Name bereinigt nach Schema `Vorname Nachname`
**Jahrgang** | `int` | Jahrgang vierstellig
**Geschlecht** | `enum` | `w` oder `m`
**Partei** | `string` | Partei, normalisiert
**Funktion** | `enum` | `leer` (Mitglied), `chair` (Gemeindepräsident:in), `school` (Schulvorsteher:in, nicht konsequent erfasst)
**Hinweis** | `string ` | Notizen zu dieser Person
**jahrgang_nicht_zugeordnet** | `bool` | `True` = Jahrgang gehört nicht zwingend zu dieser Person, jedoch zu dieser Gemeinde
**partei_nicht_zugeordnet** | `bool` | `True` = Partei gehört nicht zwingend zu dieser Person, jedoch zu dieser Gemeinde
**Gecheckt 2021** | `string` | Daten wurden im 2021 nochmals geprüft

*Stand der Daten: April 2021*