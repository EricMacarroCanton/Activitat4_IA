# Exercici 3: la temperatura depèn de la tasca

**Objectiu:** comprovar que no hi ha una temperatura «millor»: una tasca de precisió i una de creativitat necessiten valors diferents. També veureu que una temperatura baixa fa el model més consistent, però no el fa encertar més: si no sap fer una tasca, s'equivoca igualment.

**Predicció (abans de començar):** amb quina temperatura creieu que el model encertarà més una multiplicació? I amb quina proposarà noms més variats?

** Amb 0 encertarà una multiplicació i  amb 1.5 ens donarà nomes més variats**

**Script:** aquest exercici no necessita cap paràmetre nou: feu servir `lab.py` tal com el teniu.

1. Deseu els dos prompts en variables de PowerShell. El prompt A mesura la precisió (la resposta correcta és 337491) i el B, la creativitat:

   ```powershell
   $promptA = "Quant fa 487 × 693? Respon només amb el número."
   $promptB = "Dona'm 5 noms originals per a una cafeteria d'informàtics. Respon només amb els noms."
   ```

2. Executeu cada prompt **3 vegades** amb temperatura 0 i **3 vegades** amb temperatura 1.5, i completeu la taula:

   ```powershell
   python lab.py $promptA --vegades 3 --temperature 0
   python lab.py $promptA --vegades 3 --temperature 1.5
   python lab.py $promptB --vegades 3 --temperature 0
   python lab.py $promptB --vegades 3 --temperature 1.5
   ```

| Prompt | Temperatura 0 | Temperatura 1.5 |
| :- | :- | :- |
| A: 487 × 693 (quantes vegades ha encertat?) |0 de 3 encerts ja que només ens dona 337821 (la resposta correcta és 337491) | 0 de 3 encerts amb tres resultats diferents (339339, 339081 i 337,851)|
| B: noms de cafeteria (hi ha varietat? són repetits?) | Poca varietat ja que les repeticions 2 i 3 són idèntiques i la 1 només canvia un parell de noms | Noms i idees diferents i a la 3a tira canvia el format de llista|

## Preguntes

1. Amb quina temperatura funciona millor cada tasca? Per què?

   **Cada tasca funciona millor amb un valor diferent perquè el paràmetre de temperatura regula com de aleatòria és la selecció del següent token. Per a tasques de precisió és millor una temperatura baixa per evitar variacions. En canvi, per a tasques creatives una temperatura més alta ajuda a trobar opcions menys probables i més variades, tot i que no ens hem de passar ja que a 1.5 es nota dispersió i canvis de format**

2. Quina temperatura triaríeu per a un assistent de codi? I per un generador de noms de projectes o de startups tecnològiques?
per a un generador d'idees per a un eslògan?


   **Per a un assistent de codi triaria temperatura baixa perquè el codi necessita precisió, coherència i resultats fiables sense inventar APIs o trencar l'estructura.

   En un generador de noms de projectes o startups tecnològiques una temperatura mitjana-alta per obtenir propostes variades i originals sense perdre el sentit.

   Finalment per un generador d'idees per a un eslògan temperatura mitjana-alta ja que un bon eslògan necessita originalitat i ganxo, però ha de mantenir prou control perquè sigui entenedor i adequat al producte**

3. Amb temperatura 0, el model ha donat sempre la mateixa resposta al prompt A? Era correcta? Que una resposta sigui consistent vol dir que sigui correcta? Com resoldríeu aquest problema en una aplicació real?

   **Sí, amb temperatura 0.0 ha donat sempre la mateixa resposta (337821 les 3 vegades), però no era correcta. Que una resposta sigui igual només significa que el model tria sempre la mateixa continuació més probable per a aquell prompt, no que tingui raó ja que un LLM no executa aritmètica exacta com una calculadora, sinó que prediu tokens basant-se en patrons estadístics. En una aplicació real ho resoldria passant el càlcul a una eina o codi extern i validant els resultats en lloc de fiar-me del càlcul mental del model.**

