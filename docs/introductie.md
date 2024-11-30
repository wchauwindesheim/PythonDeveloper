# Introductie
In deze cursus gebruiken we een aantal tools:

- Command Line Interface (CLI) (tekstgebaseerde instructieregels)
- Python Interpreter
- Visual Studio Code (code editor)
- Github (online versiebeheer)
- Git (versiebeheersysteem)


## Command Line Interface (CLI)

Met de command line kunnen we via de zogenaamde Terminal opdrachten aan de computer geven.

Openen van de Terminal:

- Open het windows menu en type in 'cmd' en kies voor 'Command Prompt'

Dit open de powershell of in sommige gevallen nog een oude DOS prompt. 
Hier kun je verschillende commando's gebruiken om bijvoorbeeld de inhoud van je harde schijf te zien:

- ```ls``` (powershell) of ```dir``` (DOS)

Je krijgt mappen te zien. Om in een van de mappen te komen, kun je een ander commando gebruiken:

- cd

Doe bijvoorbeeld cd \<mapnaam> en daarna nog een keer ls en je krijgt nu de inhoud van \<mapnaam> te zien.

- pwd

Met dit commando kun je zien in welke map je momenteel zit in de command line. Na het intypen van dit commando krijg je de volledige padnaam te zien.

### Pijltjestoetsen

Met de pijltjestoetsen kun je heen en weer gaan tussen eerder ingetypte commando's en kun je eerdere commando's terughalen en opnieuw uitvoeren waardoor je niet steeds opnieuw hoeft in te typen.

## Python Interpreter

Om Python te programmeren heb je een zogenaamde interpreter nodig. Dit is een programma dat de Python instructies kan vertalen naar machinecode om op de computer uit te voeren. Dit gebeurt in realtime, dus is het wat langzamer dan andere soorten programmeertalen die van tevoren vertaald zijn.

- Installeer de Python interpreter (let op: zet het vinkje 'Add python.exe to PATH' aan)

Ga naar https://www.python.org/downloads/ and download de Python versie voor jouw computer en installeer deze. 

Als het is geinstalleerd, kun je in de command line Python programmeren. 

Open een nieuwe command line en type:
- python --version

Hiermee krijg je het geinstalleerde versienummer van Python te zien. Het kan zijn dat Python nog niet werkt in jouw command line. Dit komt waarschijnlijk doordat het nog niet in je pad (PATH) staat. Om dit in Windows op te lossen kun je de bijvoorbeeld de volgende stappen proberen: https://phoenixnap.com/kb/add-python-to-path




## Visual Studio Code

Omdat het programmeren van Python in de command line nogal kaal en onhandig is, maken we gebruik van een code editor. In deze cursus gebruiken we de populaire code editor Visual Studio Code.
- Installeer Visual Studio Code

Ga naar https://code.visualstudio.com/ en download de VS Code versie voor jouw computer installeer deze.

Als het is geinstalleerd:
- maak een nieuwe map aan op jouw computer
- open deze map met VS Code

Maak een nieuw tekstbestand aan genaamd 'readme.txt' en type hierin 'Dit is mijn Python project'
- sla het bestand op

noem het bestand 'readme.txt'. na het opslaan zie je het bestand links in de explorer.
- zet ook 'Autosave' aan (File -> Autosave)

### Terminal/CLI in VSCode
In VSCode kun je ook een command line openen. Dit gebeurt via het Terminal menu.

## Github
Github is een online platform voor softwareontwikkeling en versiebeheer.
- maak een github account aan

Ga naar https://github.com/ en klik op 'Sign Up'en volg de instructies.

voor meer informatie zie: https://www.geeksforgeeks.org/how-to-add-git-credentials-in-vscode/

## GIT

GIT is een versiebeheersysteem waarmee je code versie kunt beheren. Daarnaast kun je hiermee samenwerken met andere developers. Git is geintegreerd in Visual Studio Code waarvan wij ook gebruik van gaan maken.

- installeer GIT (een versiebeheersysteem) 

Ga naar https://git-scm.com/downloads en download de git versie voor jouw computer en installeer deze. Laat alle opties op default staan.

Met Git en VS Code kun je een aantal acties uitvoeren om versiebeheer te gebruiken (git moet wel geinstalleerd zijn):

## Aanmaken Git credentials (git user.name en user.email)

Om Git te kunnen gebruiken moeten eerst ook de username en email in git geconfigureerd worden. Dit gebeurt in de command line met de volgende commando's:
- ```git config --global user.name "FIRST_NAME LAST_NAME"```
- ```git config --global user.email "MY_NAME@example.com"```

Gebruik hierbij je eigen naam en email. Voor meer informatie zie https://support.atlassian.com/bitbucket-cloud/docs/configure-your-dvcs-username-for-commits/

## Git in VSCode
Open VS Code met jouw map en jouw 'readme.txt' bestand geopend.

klik op het 3e icoontje (onder het vergrootglas) aan de linkerzjkant in de toolbalk. Je ziet twee blauwe knoppen 'Initialize Repository' en 'Publish to Github'

### git init
Om je eigen nieuwe repository te maken klik op 'Initialize Repository'

### git commit
Type vervolgens in de input balk onder 'Source control' 'Nieuwe repository' in en klik op de blauwe knop 'Commit'. Klik op 'yes' of 'always' als gevraagd wordt of je al je veranderingen wilt opslaan. De eerste versie van jouw repository is nu opgeslagen.

## Connectie maken tussen jouw lokale Git en Github

*Let op: bij deze stap moet er 2 keer een popup verschijnen die om autorisatie vraagt. Ook moet je inloggen via de browser.*

### git push

Klik vervolgens op Publish Branch en VSCode vraagt of je met Github wil connecten. 
**Dit is de 1e popup**. Klik op 'Allow' in de popup en je browser opent github.com. Log in met je Github account. Klik op de groene knop 'Continue' en vervolgens op de groene knop 'Authorize Visual-Studio-code'. Klik vervolgens op 'open' als de browser Visual Studio Code wil openen. VS Code mag nu pushen naar jouw Github account. 

- Kies 'Publish to Github public repository'

Hiermee wordt jouw repository naar Github gepusht. VS Code vraag je nu weer om in te loggen. **Dit is de 2e popup**.  Kies de blauwe knop 'Sign in with your browser'. Klik vervolgens op de groene knop 'Authorize git-ecosystem'. Een lege pagina opent in je browser. Ga terug naar VS Code, jouw repo heeft nu de veranderingen in Github opgeslagen (gepusht)
- Kijk op Github of jouw repository aanwezig is in jouw account

## Optionele commando's
### git pull
Als de code op Github in een hogere versie zit dan jouw lokale versie, kun je een zogenaamde 'git pull' doen om de laatste veranderingen op te halen.

### git clone
Als je een project van Github lokaal op je computer wilt. kun je deze clonen.



