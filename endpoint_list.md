# Lista endpointów API

## GET `/`
Zwraca krótką notatkę.

---

## /game/
- **POST `/game/reset-game`**
  - Resetuje całą grę.

- **POST `/game/add-pool/<team>/<int:money>`**
  - Dodaje do puli pieniędzy drużyny.
  - Argumenty:
    - `team` – nazwa drużyny
    - `money` – ilość pieniędzy dodana do puli

- **POST `/game/reset-temp-money`**
  - Resetuje tymczasową pulę pieniędzy każdej z drużyn.

---

## /pool/
- **GET `/pool/get-pool`**
  - Zwraca aktualny stan puli.

- **POST `/pool/reset-pool`**
  - Resetuje pulę pieniędzy.

---

## /round/
- **POST `/round/reset-round`**
  - Resetuje rundę.

- **POST `/round/next-round`**
  - Rozpoczyna następną rundę, przenosi pieniądze i otwiera nową rundę.

- **GET `/round/get-round`**
  - Zwraca informacje o aktualnej rundzie.

- **POST `/round/close-round`**
  - Zamyka rundę (licytację).

- **POST `/round/buy-hint/<team>/<int:money>`**
  - Drużyna kupuje podpowiedź (jeśli nie ma już darmowych podpowiedzi, pobiera pieniądze).
  - Argumenty:
    - `team` – nazwa drużyny
    - `money` – kwota za podpowiedź

---

## /modifier/
- **POST `/modifier/punish-competitor/<team>/<int:money>`**
  - Kara dla zawodnika (odejmuje pieniądze, resetuje tymczasową pulę).
  - Argumenty:
    - `team` – nazwa drużyny
    - `money` – kwota kary

- **POST `/modifier/buy-hint/<team>/<int:money>`**
  - Kupno podpowiedzi przez drużynę (po wybraniu pola podpowiedź).
  - Argumenty:
    - `team` – nazwa drużyny
    - `money` – kwota za podpowiedź

- **POST `/modifier/buypack-lost-player/<team>/<int:money>`**
  - Wykupienie utraconego zawodnika.
  - Argumenty:
    - `team` – nazwa drużyny
    - `money` – kwota wykupu

- **POST `/modifier/buy-blackbox/<team>/<int:money>`**
  - Kupno czarnej skrzynki.
  - Argumenty:
    - `team` – nazwa drużyny
    - `money` – kwota za czarną skrzynkę

- **POST `/modifier/onevsone_step_1/<team1>/<team2>`**
  - Rozpoczęcie pojedynku jeden na jeden (obydwie drużyny płacą 500).
  - Argumenty:
    - `team1`, `team2` – nazwy drużyn

- **POST `/modifier/onevsone_step_2/<team1>/<team2>`**
  - Drugi etap pojedynku jeden na jeden (do uzupełnienia w kodzie).
  - Argumenty:
    - `team1`, `team2` – nazwy drużyn

---

## /team/
- **GET `/team/<team>-info`**
  - Zwraca informacje o drużynie (`name`, `money`, `temp_money`, `bidded`, `onevsone`, `lost_player`, `is_playing`, `max_bet`, `hint`).
  - Argumenty:
    - `team` – nazwa drużyny

- **GET `/team/get-money/<team>`**
  - Zwraca ilość pieniędzy danej drużyny.
  - Argumenty:
    - `team` – nazwa drużyny

- **POST `/team/change-game/<team>`**
  - Zmienia status gry dla drużyny.
  - Argumenty:
    - `team` – nazwa drużyny

- **POST `/team/change-bidded/<team>`**
  - Zmienia status licytacji dla drużyny.
  - Argumenty:
    - `team` – nazwa drużyny
