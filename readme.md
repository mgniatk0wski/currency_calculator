PL:

# OPIS PL

# ConvertIT – Kalkulator walut z wykresem historycznym

Prosty i szybki przelicznik walut z wykresem kursów z ostatnich 30 dni  
**Język:** Python 3.13.3  
**Środowisko:** Visual Studio Code  
![ConvertIT – zrzut ekranu aplikacji](app-screen.png)


## Cel projektu

- Szybkie przeliczanie między 30+ walutami  
- Wykres kursów z 30 dni  
- Nowoczesny, ciemny interfejs (PyQt6)  
- Obsługa błędów i walidacja danych  


## Jak to działa?

1. Wybierz waluty  
2. Wpisz kwotę  
3. Kliknij Przelicz / użyj Swap  
4. Wynik natychmiast  
5. Dół okna: wykres 30 dni + tooltipy  


## Wykorzystane technologie

| Technologia     | Zastosowanie            |
|-----------------|-------------------------|
| Python 3.13     | Język główny            |
| PyQt6           | Interfejs graficzny     |
| Matplotlib      | Wykresy                 |
| mplcursors      | Tooltipy                |
| Frankfurter.app | API kursów              |
| requests        | Zapytania HTTP          |
| FigureCanvas    | Osadzanie wykresu       |


## Struktura projektu

├── main.py → uruchamia aplikację  
├── main_window.py → GUI + logika  
├── modules.py → API  
└── style.qss → ciemny motyw  


## Jak uruchomić

pip install PyQt6 matplotlib mplcursors requests  
python main.py  


## Główne funkcjonalności

- Natychmiastowe przeliczanie  
- Przycisk Swap  
- Interaktywny wykres 30 dni  
- Obsługa braku internetu  
- Kurs 1.0 dla tej samej waluty  


## Obsługa błędów

| Sytuacja                 | Zachowanie            |
|--------------------------|-----------------------|
| Niepoprawna liczba       | Blokada + warning     |
| Brak internetu / API     | Critical message      |
| Ta sama waluta           | Kurs 1.0              |
| Brak historii            | Wykres nieodświeżany  |


## Testy funkcjonalne

| Scenariusz         | Wynik           |
|--------------------|-----------------|
| Poprawne dane      | OK              |
| Złe dane           | Warning         |
| Brak internetu     | Critical        |
| Ta sama waluta     | 1.0             |
| Brak historii      | Pusty wykres    |


## Wzorce projektowe

- Observer  
- Adapter  


## Licencja

Projekt na zaliczenie — kod otwarty.



ENG:

# DESCRIPTION EN

# ConvertIT – Currency converter with 30-day historical chart

A simple and fast currency converter with a 30-day historical rate chart  
**Language:** Python 3.13.3  
**Environment:** Visual Studio Code  
![ConvertIT – app screenshot](app-screen.png)


## Project goals

- Fast conversion between 30+ currencies  
- 30-day rate chart  
- Dark UI (PyQt6)  
- Error handling & validation  


## How it works

1. Select currencies  
2. Enter amount  
3. Convert / Swap  
4. Instant result  
5. Bottom: 30-day chart + tooltips  


## Used technologies

| Technology      | Purpose                  |
|-----------------|---------------------------|
| Python 3.13     | Main language             |
| PyQt6           | GUI framework             |
| Matplotlib      | Charts                    |
| mplcursors      | Tooltips                  |
| Frankfurter.app | FX API                    |
| requests        | HTTP requests             |
| FigureCanvas    | Embedding the chart       |


## Project structure

├── main.py → app entry point  
├── main_window.py → UI + logic  
├── modules.py → API handling  
└── style.qss → dark theme  


## How to run

pip install PyQt6 matplotlib mplcursors requests  
python main.py  


## Main features

- Instant conversion  
- Swap button  
- 30-day interactive chart  
- Offline/API error handling  
- Auto 1.0 rate for identical currency  


## Error handling

| Case              | Behavior        |
|-------------------|-----------------|
| Invalid number    | Block + warning |
| No internet       | Critical popup  |
| Same currency     | Returns 1.0     |
| No history        | Chart skipped   |


## Functional tests

| Scenario         | Result     |
|------------------|------------|
| Valid input      | OK         |
| Invalid input    | Warning    |
| No internet      | Critical   |
| Same currency    | 1.0        |
| No history       | Empty chart|


## Design patterns

- Observer  
- Adapter  


## License

Created for course credit — free to use and modify.
