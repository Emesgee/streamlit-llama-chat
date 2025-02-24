# Streamlit Web UI med LlamaIndex og GPT-4 Oversættelse

Dette projekt leverer en brugervenlig Streamlit-baseret webgrænseflade, hvor brugere kan stille spørgsmål på dansk og modtage præcise, semantiske svar på dansk. Systemet kombinerer LlamaIndex og OpenAI's GPT-4 for effektiv dokumenthåndtering og oversættelse.


## NB: Husk at oprette to mapper og opret en .env fil med api-nøgle:

- ./data: Placér dine PDF-filer her.
- ./storage: Vector-data og indeks gemmes automatisk her.
- .env: OPENAI_API_KEY="din api nøgle her."


## Funktionalitet

### Streamlit Web UI

- Simpel og intuitiv brugergrænseflade.

- Mulighed for at stille spørgsmål på naturligt dansk.

### LlamaIndex VectorStoreIndex

- Indlæser dokumenter automatisk fra en angivet mappe (SimpleDirectoryReader fra DATA_DIR).

- Opretter og gemmer indeks i mappen ./storage.

- Genbruger eksisterende indeks, hvis de allerede er oprettet.

- Udfører avancerede semantiske søgninger for at finde de mest relevante svar.

### OpenAI GPT-4 (Oversættelseslag)

- Modtager svar fra LlamaIndex på engelsk.

- Oversætter automatisk og præcist svarene til dansk for en bedre brugeroplevelse.

Denne kombination sikrer høj kvalitet, hurtige responstider og en naturlig dansk interaktion med data.

# Arkitektur af appen:
+--------------------------------------------------------------------------------+
|                               Streamlit Web UI                                 |
|            (Brugergrænseflade til at stille spørgsmål på dansk)                |
+-----------------------------+--------------------------------------------------+
                              |
                              |
                              v
+-----------------------------+--------------------------------------------------+
|          LlamaIndex VectorStoreIndex                                           |
| - Loader dokumenter (SimpleDirectoryReader fra DATA_DIR)                       |
| - Opretter og gemmer indeks (i ./storage)                                      |
| - Loader eksisterende indeks, hvis allerede til stede                          |
| - Udfører semantiske forespørgsler mod indekset                                |
+-----------------------------+--------------------------------------------------+
                              |
                              |
                              v
+-----------------------------+--------------------------------------------------+
|           OpenAI GPT-4 (Translation Layer)                                     |
|  - Modtager svar fra LlamaIndex (på engelsk)                                   |
|  - Oversætter svaret til dansk                                                 |
+--------------------------------------------------------------------------------+


## Komponenternes roller: 
### Streamlit UI:

- Brugerinput og visning af output.
- Håndterer interaktion, fejl og visuelle elementer.

## LlamaIndex:

- Indlæser dokumenter fra disk og opretter en semantisk indeks.
- Udfører forespørgsler mod dokumentindholdet.

## OpenAI GPT-4 API:

- Oversætter svarene fra engelsk til dansk, så brugeren modtager naturlige svar.

## Flow:
1. Bruger skriver forespørgsel i Streamlit.
2. Streamlit sender forespørgsel til LlamaIndex.
3. LlamaIndex returnerer svar (på engelsk).
4. OpenAI GPT-4 oversætter svaret til dansk.
5. Streamlit viser det danske svar til brugeren.



