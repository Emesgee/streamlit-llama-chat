# Streamlit Web UI med LlamaIndex og GPT-4 Oversættelse

Dette projekt leverer en brugervenlig Streamlit-baseret webgrænseflade, hvor brugere kan stille spørgsmål på dansk og modtage præcise, semantiske svar på dansk. Systemet kombinerer LlamaIndex og OpenAI's GPT-4 for effektiv dokumenthåndtering og oversættelse.

## Funktionalitet

### Streamlit Web UI

Simpel og intuitiv brugergrænseflade.

Mulighed for at stille spørgsmål på naturligt dansk.

### LlamaIndex VectorStoreIndex

Indlæser dokumenter automatisk fra en angivet mappe (SimpleDirectoryReader fra DATA_DIR).

Opretter og gemmer indeks i mappen ./storage.

Genbruger eksisterende indeks, hvis de allerede er oprettet.

Udfører avancerede semantiske søgninger for at finde de mest relevante svar.

### OpenAI GPT-4 (Oversættelseslag)

- Modtager svar fra LlamaIndex på engelsk.

- Oversætter automatisk og præcist svarene til dansk for en bedre brugeroplevelse.

Denne kombination sikrer høj kvalitet, hurtige responstider og en naturlig dansk interaktion med data.
