# Testing er helt Python
Et repo med eksempler fra testpub med Norsk Testforum

## Installer python
Installer Python 3

## Opprett et nytt virtuelt miljø
    python -m venv testpub

## Aktiver det virtuelle miljøet
Linux/Mac

    source testpub/bin/activate

Windows

    testpub\scripts\activate.bat

Windows PowerShell

    testpub\scripts\activate.ps1

## Installer alle nødvendige pakker
    pip install -r requirements.txt

## Kjør unittest-eksemplene
    python -m unittest -v test_unittest.py

## Kjør doctest-eksemplene
    python -m doctest -v test_doctest.py

## Kjør pytest-eksemplene
    python -m pytest -v test_pytest.py

## Kjør splinter-eksemplene
For at dette skal virke må du gjøre følgende før du kjører eksemplene:
* Koden er satt opp til å kjøre med firefox og geckodriver. Installer derfor firefox og geckodriver, akkurat som når man bruker selenium. Du kan også eventuelt bytte ut 'firefox' med 'chrome' i koden og installere chromedriver om du heller vil kjøre Chrome. 
* Start demosiden i /website/ mappen i et nytt shell. Husk å aktivere det virtuelle miljøet


    python run.py


Når dette er klart kan du kjøre splinter ved å kalle på pytest:

    python -m pytest test_splinter

Registrerte brukere lagres i users.pdl. Denne filen kan slettes om du ønsker å starte på nytt uten registrerte brukere. Husk å stoppe demosiden før du sletter filen.

## Kjør bandit
    python -m bandit -r website
