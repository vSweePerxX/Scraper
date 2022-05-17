# Scraper

## Installation von Python und Pip

Laden Sie die ausführbare Installationsdatei für Python 3.7 Windows x86-64 von der [Downloads-Seite](https://www.python.org/downloads/) von [Python.org](https://www.python.org/) herunter.

1. Führen Sie das Installationsprogramm aus.
2. Wählen Sie **Add Python 3.7 to PATH (Python 3.7 zu PATH hinzufügen)** aus.
3. Wählen Sie **Install Now (Jetzt installieren)** aus.

Das Installationsprogramm installiert Python in Ihrem Benutzerordner und fügt seine ausführbaren Verzeichnisse Ihrem Benutzerpfad hinzu.

## Installation eines **Virtual Environments**

1. Die Datei [requirements.txt](https://github.com/vSweePerxX/Scraper/blob/master/requirements.txt) aus Git laden
2. Öffnen des Terminals
3. Zum einem gewünschten Zielpfad navigieren
4. Mit dem Befehl `mkvirtualenv [environment_name]` ein neues environment anlegen
5. Mit dem Befehl `source environment_name/bin/activate` das Environment aktivieren
6. pip install -r requirements.txt

In dem Ordner: `anwaltsregisterScraper` → `ScraperResults` liegt eine Datei = `resultsAll.xlsx`

Diese Datei ist ein Sammeldokument aller Daten.

## Ausführen von dem Scraper

1. Mit dem Befehl `source environment_name/bin/activate` das Environment aktivieren
    1. Aktive ist es, wenn der Name des Environments am Anfang der kommandozeile steht:`(tutorial-env) MacBook-Pro-2:~ xxxx`
2. Mit dem Befehl `cd BeispielPfad/anwaltsregisterScraper` in den ordner [anwaltsregisterScraper](https://github.com/vSweePerxX/Scraper/tree/master/anwaltsregisterScraper) navigieren
3. Hier können nun verschiedene scraper gestartet werden
    1. `scrapy crawl anwaltCrawler -a bundesland=Hessen -o example.json`
        1. Stadt ‘Hessen’ kann jedes belibige Bundesland verwendet werden
    2. `scrapy crawl bvaiCrawler -o example.json`
    
    Der Output wird in den anwaltsregisterScraper Ordner geschrieben
