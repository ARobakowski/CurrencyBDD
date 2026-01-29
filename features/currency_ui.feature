# language: pl
Funkcja: Weryfikacja pobierania kursów przez interfejs
Aby mieć pewność, że użytkownik widzi poprawne dane
Jako tester systemu
Chcę sprawdzić czy wybranie waluty i okresu wyświetla wyniki

Scenariusz: Pobieranie kursu dla ostatnich 3 dni
Zakładając, że aplikacja webowa jest uruchomiona
Gdy użytkownik wprowadzi walutę "EUR"
I wybierze okres "3dni"
I wyśle formularz
Wtedy system powinien wyświetlić listę kursów historycznych

Scenariusz: Próba pobrania nieistniejącej waluty
Zakładając, że aplikacja webowa jest uruchomiona
Gdy użytkownik wprowadzi walutę "XYZ"
I wyśle formularz
Wtedy system powinien wyświetlić błąd "Brak danych dla XYZ w tym okresie."

Scenariusz: Próba wysłania pustego pola waluty
Zakładając, że aplikacja webowa jest uruchomiona
Gdy użytkownik pozostawi pole waluty puste
I wyśle formularz
Wtedy system nie powinien wysłać zapytania i poprosić o wypełnienie pola