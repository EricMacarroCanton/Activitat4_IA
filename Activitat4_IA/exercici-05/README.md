# Exercici 5: top_k i top_p

**Objectiu:** veure com limitem els candidats entre els quals el model tria el token següent.

**Predicció (abans de començar):** què creieu que passarà si el model només pot triar entre 2 candidats? I si pot triar entre tots?

**La vostra predicció:**

- `top_k`: només es consideren els *k* tokens més probables (`top_k` 0 desactiva aquest límit).
- `top_p`: només es consideren els tokens més probables fins a sumar aquesta probabilitat (`top_p` 1 vol dir tots).

1. **Actualitzeu `lab.py`:** afegiu les opcions `--top_k` i `--top_p`. Van dins d'`options` i només s'han d'enviar si s'indiquen. **Comproveu** que l'script imprimeix les opcions que li passeu: `python lab.py "Hola" --vegades 1 --temperature 0 --seed 1 --top_k 5 --top_p 0.9` ha de mostrar entre les opcions `seed`, `top_k` i `top_p`.
2. Deseu aquest prompt en una variable de PowerShell:

   ```powershell
   $prompt = "Digues un emoji. Respon només amb l'emoji."
   ```

3. Executeu cada configuració (15 repeticions i sense llavor, així cada repetició pot donar un resultat diferent). Fixeu-vos que cada configuració canvia **una sola cosa** respecte de la referència (A), tret de D i E, que comparteixen la temperatura alta:

   ```powershell
   python lab.py $prompt --vegades 15 --temperature 1 --top_k 0 --top_p 1
   python lab.py $prompt --vegades 15 --temperature 1 --top_k 2 --top_p 1
   python lab.py $prompt --vegades 15 --temperature 1 --top_k 0 --top_p 0.3
   python lab.py $prompt --vegades 15 --temperature 2.5 --top_k 0 --top_p 1
   python lab.py $prompt --vegades 15 --temperature 2.5 --top_k 64 --top_p 0.95
   ```

4. A cada fila de la taula, compteu **quants emojis diferents** han sortit de les 15 respostes.

| Configuració | temperature | top_k | top_p | Emojis diferents (de 15) |
| :- | :- | :- | :- | :- |
| A (referència) | 1 | 0 | 1 | 3 |
| B | 1 | 2 | 1 | 2 |
| C | 1 | 0 | 0.3 |1|
| D | 2.5 | 0 | 1 | 9 |
| E | 2.5 | 64 | 0.95 |4|

## Preguntes

1. Ordeneu A, B i C de més a menys varietat. Per què `top_k` 2 i `top_p` 0.3 redueixen el nombre d'emojis diferents?

   **A (3 emojis diferents) > B (2 emojis diferents) > C (1 emoji diferent). Amb top_k = 2, el model només pot escollir entre els 2 tokens més probables en cada pas, descartant la resta d'opcions. Amb top_p = 0.3, només es mantenen els tokens dels quals la suma de probabilitats arriba com a màxim al 30%, de manera que si un emoji ja concentra bona part d'aquesta probabilitat, queda com l'única opció disponible.**

2. Quin valor de `top_k` hauria de tenir la configuració B perquè el model es comportés com si la temperatura fos 0? Per què?

   **Ha de tenir top_k = 1, perquè limita el conjunt de candidats a un sol token (el de probabilitat més alta)**

3. Compareu les configuracions D i E. Quants emojis diferents surten a cada una? Quin és l'emoji més inesperat o amb menys sentit com a resposta, i a quina configuració ha aparegut? Per què `top_k` i `top_p` ajuden a evitar respostes sense sentit quan la temperatura és alta?

   **En D surten 9 emojis diferents i a E surten 4. L'emoji més inesperat és 🏆, que ha aparegut a la D. Quan la temperatura és alta, la distribució de probabilitats s'iguala i tokens poc probables guanyen més probabilitat. Top_k i top_p redueixen aquesta cua de respostes improbables**