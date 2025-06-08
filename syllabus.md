# SAD Syllabus: Lato 2025

## Ogólnie o kursie

Ten kurs nauczy Cię, jak myśleć o **danych** i ich **analizowaniu** w celu wykonania profesjonalnego raportu **eksploracyjnej analizy danych** (EDA - Exploratory Data Analysis). 

Będzie obejmować stawianie i analizowanie pytań takich jak:

-   Jak jest **formatowany** zbiór danych i czy jest to odpowiedni format dla tego, co chcę zrobić? (cz. 1/2)
-   Czy ten zbiór danych jest **reprezentatywny** lub czy odzwierciedla **obiektywną próbę**? (cz. 1/2)
-   Jakie **problemy techniczne** powinno się wziąć pod uwagę podczas porządkowania i czyszczenia danych? (cz. 1/2)
-   Jakiej metody wizualizacji i analizy danych uzyć dla danej skali pomiarowej wybranej zmiennej? (cz. 1/2)
-   Jak dobrać metodę wnioskowania z próby do zadanego problemu badawczego? (cz. 2/2)
-   Jaki **model** jest najbardziej odpowiedni dla tych danych? (cz. 2/2)
-   W jaki sposób **projektować i wdrażać** te modele - od [regresji liniowej](https://en.wikipedia.org/wiki/Linear_regression) do [maszyn wektorów nośnych](https://en.wikipedia.org/wiki/Support_vector_machine)? (cz. 2/2)

Tematy te zostaną omówione w kontekście serii krótkich **ćwiczeń praktycznych** z rzeczywistymi zestawami danych w **środowisku programistycznym Python**. Będziemy uzywać Visual Studio Code, formatu notatnika Jupyter Notebook, ew. pliku Markdown (MD) połączonego na stałe z Twoim repozytorium na GitHubie dzięki wtyczce GitLens.

## Kluczowe efekty kształcenia

Ten kurs ma na celu zapewnienie słuchacz(k)om szeregu narzędzi koncepcyjnych i technicznych. 
Moim celem jest, abyś pod koniec kursu był(a) w stanie:

-   **Zdiagnozować** i **naprawić** problemy techniczne danych, począwszy od braków danych, obserwacji odstających, brudnych danych (niekonsystencji). (cz. 1/2)
-   **Projektować** i **wdrażać** jasne, zwięzłe i dokładne przekrojowe wizualizacje danych. (cz. 1/2)
-   **Proponować** i **testować** hipotezy dotyczące danych przy użyciu modeli statystycznych na próbie danych. (cz. 2/2)
-   **Konstruować** modele statystyczne w Pythonie i **interpretować** wyniki.  (cz. 2/2)
-   Rozważać zalety i wady różnych metryk oceny modeli. (cz. 2/2)

## Logistyka kursu

### Prowadzący - instruktor

-   [Karol Flisikowski](https://pg.edu.pl/p/karol-flisikowski-20826): Profesor uczelni w Katedrze Statystyki i Ekonometrii PG / SAD część 1. w semestrze letnim.

#### Konsultacje

| Kto?              | Kiedy?      | Gdzie?                                                         |
|--------------------|------------------------|-----------------------------|
| Karol Flisikowski | Środy 14-15 | [Online](https://calendly.com/flisik/konsultacje-office-hours) |

### Kiedy/Gdzie?:

#### Ścieżka techniczna 

-   Sesja 1. i 2. 26/04/2025 9:00 - 16:00 z przerwą 12:15-12:45 /sala 209
-   Sesja 3. 16/05/2025 16:30 - 20:00 /sala 203
-   Sesja 4. 17/05/2025 12:50 - 16:30 /sala 203
-   Termin nadesłania projektu: najpóźniej do 6 lipca 23:59 (na Waszą prośbę termin przedłuzony o 1 tydzień). Mailowo podeślijcie mi tylko link do REPO projektu.

#### Ścieżka praktyczna

-   Sesja 1. 30/05/2025 16:30 - 19:45 Online: [link do spotkania](https://teams.microsoft.com/l/meetup-join/19%3ameeting_MjdjNGJhZjctNDM0MS00ZjZhLWE5OTgtOTkyYjdjOTc4OWQw%40thread.v2/0?context=%7b%22Tid%22%3a%2286760356-0022-486f-b793-a2d470bba5a5%22%2c%22Oid%22%3a%22cee5544e-5052-4880-984d-b175250e4a23%22%7d)
-   Sesja 2. i 3. 31/05/2025 9:00 - 16:00 Online: [link do spotkania](https://teams.microsoft.com/l/meetup-join/19%3ameeting_M2FiOGNkZWEtZTMwYy00MzE2LTkwZTgtMjg4YmIyNzlhNTcw%40thread.v2/0?context=%7b%22Tid%22%3a%2286760356-0022-486f-b793-a2d470bba5a5%22%2c%22Oid%22%3a%22cee5544e-5052-4880-984d-b175250e4a23%22%7d)
-   Sesja 4. 21/06/2025 12:50 - 16:00 Online: [link do spotkania](https://teams.microsoft.com/l/meetup-join/19%3ameeting_YzU1YTE5YzMtMDRmNy00MjAwLWFlM2YtMGQwMjgyZTNmZmU1%40thread.v2/0?context=%7b%22Tid%22%3a%2286760356-0022-486f-b793-a2d470bba5a5%22%2c%22Oid%22%3a%22cee5544e-5052-4880-984d-b175250e4a23%22%7d)
-   Termin nadesłania projektu: najpóźniej do 6 lipca 23:59 (na Waszą prośbę termin przedłuzony o 1 tydzień). Mailowo podeślijcie mi tylko link do REPO projektu.

## Ocena końcowa

### Projekt końcowy

Twoja ocena końcowa bazuje na wykonaniu w małej grupie projektu końcowego: [szczegóły nt. projektu](final.md).

### Skala ocen

Jeśli bierzesz udział w kursie na ocenę, Twoja ocena zostanie ustalona zgodnie z poniższą skalą.

Należy pamiętać, że liczba po **prawej** stronie zakresu *nie jest zawarta* w danym zakresie: to znaczy, że „4.5” waha się od 84% aż do 90.99%, ale nie obejmuje 91% (91% to 5.0).

| Procent |      Ocena      |
|:--------:|:---------------:|
| \> 91%  |       5.0       |
| 84-91%  |       4.5       |
| 77-84%  |       4.0       |
| 70-77%  |       3.5       |
| 60-70%  |       3.0       |
| \< 60%  | brak zaliczenia |

### O zaokrąglaniu

Należy pamiętać, że moją zasadą jest *nie* zaokrąglanie ocen w górę z dwóch powodów:

1.  Jeśli zaokrąglanie jest stosowane wybiórczo (tj. tylko wobec słuchaczy, którzy o to poproszą), jest to niesprawiedliwe wobec innych.
2.  Jeśli zaokrąglanie jest stosowane powszechnie, po prostu redefiniuje granicę między dwiema ocenami literowymi (np. czyniąc 87% punktem odcięcia dla 4.5).

### Opóźnione nadesłanie projektu

Słuchacze mogą przesyłać spóźnione zadania do 48 godzin po terminie ich składania, uzyskując 75% punktów, które by otrzymali (tj. jeśli uzyskali 90% punktów, otrzymają 67,5% z karą za spóźnienie).

W przeciwnym wypadku - zgodnie z regulaminem studiów podyplomowych i umową, przysługuje Państwu zaliczenie poprawkowe w kolejnej edycji studiów 2026.

## Pytania, informacje zwrotne i komunikacja

Z instruktorami można skontaktować się w następujący sposób:

-   Godziny pracy.
-   Publiczne pytanie na kanale Discord kursu SAD.
-   Prywatna wiadomość przez Discord.
-   E-mail.

Dołącz do kanału Discord kursu SAD tutaj: [kanał Discord SAD 2025](https://discord.gg/K5Z3pTjs)

Należy pamiętać, że generalnie preferujemy komunikację przez Discord, a nie e-mail.

## Uczciwość akademicka

Prosimy o oddawanie własnych prac. Mimo że zachęcamy do wspólnej pracy nad niektórymi zadaniami, nadal należy rozumieć przesłany kod. 

Zestawy zadań i projekt końcowy powinny być wykonywane niezależnie.

Prosimy o zapoznanie się z zasadami uczciwości akademickiej [tutaj](https://cdn.files.pg.edu.pl/chem/Studenci/Dokumenty/Dla%20dyplomantów/PO%2029-2024%20-%20wytyczne%20dot.%20narzędzi%20GenAl.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=mediamgr%2F20250320%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250320T133048Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1200&X-Amz-Signature=e3400f2a33247b1f62ad6c3cace31f890c0818a47a8e7a671844cbb2181fb251). 

Oszukiwanie i plagiatowanie są nieuczciwe wobec innych i ostatecznie wobec Ciebie. Zamiast tego, jeśli masz z czymś trudności - poproś o pomoc!