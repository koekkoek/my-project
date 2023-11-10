# my-project
[![Run Tests](https://github.com/koekkoek/my-project/actions/workflows/run-tests.yml/badge.svg)](https://github.com/koekkoek/my-project/actions/workflows/run-tests.yml)

## Componenten van mijn oplossing
1. Verbinding github en lokale pc: hiermee zorg ik ervoor dat ik updates naar github push;
2. Github action: deze bestaat uit twee stappen: (A) het uitvoeren van pytest om te kijken of alle testen slagen. Zo ja voert hij (B) uit: het pushen van de code naar Digital Ocean.
3. Om de code te pushen Github Action in de yml file bash code uit via een script.
4. De verbinding tussen Github en Digital Ocean komt tot stand via SSH. Hiervoor heb ik diverse secrets ingesteld in Github.


## Waar liep ik tegenaan?
1. Verbinding ssh tussen Digital Oceans Virtual Machine en github;

    Ik ben behoorlijk lang bezig geweest met uitzoeken hoe ik de verbinding tussen de VM en Github regel. Uiteindelijk heb ik gekozen voor SSH. Ik kwam de code van appleboy tegen die ik hiervoor kon gebruiken. Vervolgens moest ik de juiste secrets invoeren. Dat heb ik gedaan bij Github via settings -> Deploy keys en settings -> secrets and variables -> actions. Bij die laatste heb ik vier variabelen aangemaakt: HOST, PORT, SSH_PRIVATE_KEY en USERNAME.

2. Github cloonde niet de repo van github

    Er ontbrak nog een .git file in mijn directory op de betreffende map op de VM. Deze heb ik toen met bash commands aangemaakt.

3. Dat VM niet de juiste website laadde

    Toen de code gepushd was naar de VM, verscheen het niet live op mijn site. Hiervoor heb ik Gunicorn en NGINX opnieuw geconfigureerd. Daarvoor heb ik de stappen uit "Exercise: Deployment" gebruikt.

4. Ik kreeg de volgende error: "err: mkdir: cannot create directory ‘/home/farm’: File exists"

    Ik gaf elke keer het bash command mee om een nieuwe directory aan te maken. Deze bestond al, dus heb ik het commando verwijderd.

5. Vervolgens werden updates aan de code niet langer op de VM geüpdated.

    Bij een nieuwe git push vanaf mijn lokale pc, startte github actions. Deze gaf vervolgens een foutmelding dat hij de code niet kon pushen. Wat bleek? Via het command "cd /home/farm" kwam ik niet in de juiste directory terecht. Dit moest "cd /home/farm/my-project" zijn. Na deze aanpassing lukte het om de code te updaten en werden wijzigingen ook op de website zichtbaar.

## Tot slot
Het was vooral een heel boeiende opdracht waarin ik heb leren werken met Gunicorn, NGINX, Github Actions en verbindingen via SSH d.m.v. secrets.
