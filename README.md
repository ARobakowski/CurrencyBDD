# 📈 CurrencyBDD - System Analizy Kursów Walut NBP

## 📝 Opis projektu
Projekt jest aplikacją internetową służącą do pobierania i wyświetlania historycznych kursów walut z API Narodowego Banku Polskiego. Aplikacja pozwala na analizę trendów w różnych przedziałach czasowych (dni, tygodnie, miesiące, lata). Projekt został zrealizowany w celu zademonstrowania podejścia **BDD (Behavior-Driven Development)** oraz zalet **konteneryzacji** przy użyciu Dockera.

---

## 🛠️ Technologie i Narzędzia
Do budowy i testowania aplikacji wykorzystano:
* **Framework Web**: Flask (Python).
* **Framework BDD**: **Behave** (dla języka Python).
* **Integracja**: NBP Web API (Requests).
* **Konteneryzacja**: Docker oraz Docker Compose.
* **UI**: HTML5 + CSS3 (Jinja2).

---

## 📂 Struktura Projektu
Zorientowana na podejście BDD:

```text
CurrencyBDD/
│
├── features/               # Opisy funkcjonalności w języku Gherkin
│   └── currency_ui.feature
│
├── features/steps/         # Implementacja kroków testowych (Python)
│   └── currency_steps.py
│
├── static/                 # Style CSS (warstwa wizualna)
├── templates/              # Szablony HTML (interfejs użytkownika)
├── app.py                  # Logika serwera i integracja z API
├── Dockerfile              # Definicja kontenera aplikacji
└── requirements.txt        # Zależności projektu
