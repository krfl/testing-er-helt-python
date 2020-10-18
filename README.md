# Testing er helt Python
Et repo med eksempler fra meetup med Norsk Testforum

## Opprett et nytt virtuelt miljø
    python3 -m venv meetup


## Aktiver det virtuelle miljøet
Linux/Mac

    source meetup/bin/activate

Windows

    meetup/scripts/activate.bat

Windows PowerShell

    meetup/scripts/activate.ps1


## Installer alle nødvendige pakker
    pip install -r requirements.txt

## Kjør unittest-eksemplene
    python -m unittest -v test_unittest.py

## Kjør doctest-eksemplene
    python -m doctest -v test_doctest.py

## Kjør pytest-eksemplene
    python -m pytest -v test_pytest.py

## Kjør splinter-eksemplene
For at dette skal virke må du gjøre følgende før du kjører eksemplene

* Installer firefox og geckodriver, akkurat som når man bruker selenium
* Start demosiden i /website/ mappen i et nytt shell. Husk å aktivere det virtuelle miljøet.



    python run.py


Når dette er klart kan du kjøre splinter ved å kalle på pytest:

    python -m pytest test_splinter


Registrerte brukere lagres i users.pdl
