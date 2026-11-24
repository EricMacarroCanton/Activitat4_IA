# Exercici 2: automatitzar les proves generant un script amb el model

**Objectiu:** crear un script que automatitzi les proves de l'exercici 1: repeteix un prompt les vegades que vulgueu, amb la temperatura que li indiqueu, sense haver d'escriure `/clear`. L'script **no l'heu d'escriure vosaltres**: us el generarà el model `gemma3:4b`. Així veureu fins on arriba un model petit escrivint codi i per què cal llegir-lo i provar-lo abans de fiar-se'n. Aquest script serà el vostre laboratori: als exercicis següents l'ampliareu amb nous paràmetres a mesura que els necessiteu.

**Predicció (abans de començar):** el primer codi que us doni el model funcionarà? Quants intents us caldran?

**La vostra predicció:**

1. **Configureu l'entorn de Python.** Aquest exercici i els següents fan servir Python. No cal crear cap carpeta nova: feu-ho dins del mateix repositori. Només cal fer-ho un cop, amb Visual Studio Code:

   1. Obriu el repositori a VS Code (*File > Open Folder*). Cal tenir instal·lada l'extensió *Python* de Microsoft.
   2. Premeu `Ctrl+Shift+P`, escriviu `Python: Create Environment` i trieu-lo.
   3. Seleccioneu **Venv** i, després, l'intèrpret de Python que voleu fer servir. VS Code crea la carpeta `.venv`.
   4. Obriu un terminal nou (*Terminal > New Terminal*): l'entorn s'activa sol i veureu `(.venv)` al principi de la línia. Instal·leu la llibreria:

      ```powershell
      pip install ollama
      ```

2. Obriu un segon terminal a VS Code i inicieu el model (el mateix `gemma3:4b` de la Preparació, que també sap escriure codi):

   ```
   ollama run gemma3:4b
   ```

3. Demaneu-li l'script. No li doneu codi: expliqueu-li què ha de fer.

   **Què ha de fer l'script:**

   - El fitxer es diu `lab.py` i es crida així:

     ```powershell
     python lab.py "prompt" --vegades 5 --temperature 0.8
     ```

   - El prompt és obligatori (text). Si no s'indiquen, `--vegades` (enter) val 5 i `--temperature` (decimal) val 1.
   - Les opcions s'escriuen amb nom (`--vegades`, `--temperature`) i en qualsevol ordre. Així, més endavant, hi podrem afegir més opcions sense trencar res.
   - Si s'executa sense cap argument, no ha de fallar amb un error: ha de mostrar l'ajuda (l'ús i les opcions) i sortir.
   - Fa servir el model `gemma3:4b`.
   - Repeteix el prompt les vegades indicades amb crides independents (sense historial, així no cal `/clear`).
   - Primer imprimeix les opcions que fa servir i, després, cada resposta numerada.

   **Com demanar-ho al model:**

   - Digueu-li que faci servir `argparse`.
   - Doneu-li un exemple de sortida, perquè així el format surt igual cada cop:

     ```
     Prompt: Digues una paraula
     vegades: 3
     temperature: 0.8

     1. Algorisme
     2. Microprocessador
     3. Recursivitat
     ```

   - Demaneu-li que respongui **només amb el codi complet, en un sol bloc i sense explicacions**, perquè sigui fàcil de copiar.

   *Pista:* el model no coneix bé la llibreria d'Ollama. Digueu-li que ha de fer servir `ollama.generate(model=..., prompt=..., options={...})`, que **tots els paràmetres del model** (ara `temperature`; més endavant `seed`, `top_k`, `top_p`, `num_predict`...) han d'anar dins del diccionari `options` i no com a arguments directes de `generate`, i que el text de la resposta és a `r["response"]`. Remarqueu-li que `generate` **no retorna el text directament**, sinó un objecte amb diversos camps, i que cal agafar-ne només el camp `response` abans de netejar-lo i imprimir-lo.

4. Creeu el fitxer `lab.py` a VS Code, copieu-hi el codi que us doni el model i **llegiu-lo** abans d'executar-lo. No el corregiu a mà: si falla, copieu l'error al model i demaneu-li que el solucioni. Apunteu els intents i els errors (els necessitareu per a la pregunta 1) i enganxeu el prompt final a l'apartat «El vostre prompt final» del `README.md` de l'exercici.
5. Proveu-lo amb els prompts de l'exercici 1. Aquests exemples són per a PowerShell:

   ```powershell
   $promptParaula = "Digues una paraula en català de més de 10 lletres. Respon només amb la paraula."
   $promptCapital = "Quina és la capital de França? Respon només amb el nom."

   # Primera prova de l'exercici 1: 3 repeticions amb temperatura 0
   python lab.py $promptParaula --vegades 3 --temperature 0
   # El mateix amb temperatura 0.8
   python lab.py $promptParaula --vegades 3 --temperature 0.8
   # Segona prova de l'exercici 1: 3 repeticions amb temperatura 1.5
   python lab.py $promptCapital --vegades 3 --temperature 1.5
   ```

6. Compareu els resultats amb les taules de l'exercici 1. Amb temperatura 0, les repeticions haurien de donar la mateixa resposta. Atenció: la **primera** resposta pot ser diferent de les altres, perquè Ollama processa el prompt de manera lleugerament diferent la primera vegada. No és un error vostre: repetiu la sèrie i compareu les respostes següents.

## El vostre prompt final

Escriu un script complet en Python anomenat lab.py que utilitzi el mòdul argparse per llegir els arguments de la línia de comandes i automatitzar proves amb Ollama.

Requisits:
- Fes servir argparse.ArgumentParser per definir prompt (argument posicional obligatori de tipus str), --vegades (opció de tipus int, valor per defecte 5) i --temperature (opció de tipus float, valor per defecte 1.0).
- Les opcions --vegades i --temperature s'han de poder passar en qualsevol ordre.
- Crea primer parser = argparse.ArgumentParser(...) i afegeix els add_argument, després comprova if len(sys.argv) == 1: per cridar parser.print_help() i sortir amb sys.exit(0), i finalment fes args = parser.parse_args().
- Ha d'utilitzar la llibreria ollama cridant ollama.generate(model="gemma3:4b", prompt=..., options={"temperature": ...}).
- Tots els paràmetres del model (ara temperature) han d'anar dins del diccionari options, mai com a arguments directes de generate.
- Cada repetició ha de ser una crida independent (sense historial de conversa).
- Extreu el camp response (response['response'].strip()) i imprimeix exactament:
Prompt: <prompt>
vegades: <vegades>
temperature: <temperature>

1. <resposta 1>
2. <resposta 2>

Respon ÚNICAMENT amb el codi complet en un sol bloc, sense explicacions.
Deseu l'script `lab.py` a l'arrel del repositori (no en aquesta carpeta).

## Preguntes

1. Quants intents us han calgut? Quins errors ha comès el model (nom del model, paràmetres, lectura dels arguments...) i com els heu resolt?

Han calgut uns 6 intents fins a obtenir un script completament funcional. Els principals errors del model han estat:

Confondre l'exemple de sortida amb la tasca ja que en el primer intent, en lloc d'escriure codi Python, ha repetit la sortida d'exemple (Algorisme). Ho vaig resoldre demanant explícitament un programa en Python dins un bloc de codi.

Gestió de l'execució sense arguments: inicialment no comprovava si es passaven arguments i argparse llançava l'error the following arguments are required: prompt. Quan li vaig demanar que ho corregís, primer va posar la comprovació (if not args.prompt: / if len(sys.argv) == 1:) després de parser.parse_args() (codi mort) i, en un altre intent, abans de definir la variable parser (que provocava un NameError). Es va resoldre indicant-li l'ordre exacte de les instruccions.

Format de sortida incomplet: en una iteració va respectar l'estructura però va deixar buits els print (Prompt: , vegades: , temperature: ) i mantenia el prefix Resposta X: en lloc de 1. . Ho vaig solucionar especificant-li exactament les línies print amb les variables corresponents.

2. Heu llegit el codi abans d'executar-lo? Per què és important entendre el que s'executa a l'ordinador, encara que l'hagi escrit un model?

Sí, l'he revisat abans de cada execució. És fonamental entendre el codi generat per un model perquè els LLM petits sovint cometen errors de lògica o d'ordre d'execució que no sempre salten a la vista (com comprovar una condició després de parse_args() o fer servir una variable abans de declarar-la). A més, per seguretat i control, mai s'ha d'executar codi a cegues al propi equip sense verificar que no fa operacions no desitjades (esborrar fitxers, fer peticions externes inesperades o entrar en bucles infinits) i perquè, si cal ampliar l'script en exercicis posteriors, cal saber com funciona per dins.
