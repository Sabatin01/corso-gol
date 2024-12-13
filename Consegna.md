
# Consegna progetto finale

Realizzare un'applicazione Python che permetta di gestire un piccolo magazzino e il processo di ordini dei clienti. L'applicazione sarà composta da due moduli principali:

1.  **G"estione Magazzino**: Permette di visualizzare, aggiungere, aggiornare o rimuovere prodotti dal magazzino.
    
2.  **Gestione Ordini**: Consente di creare ordini basati sui prodotti disponibili e di visualizzare la cronologia degli ordini.
    

#### **Requisiti**

Il progetto deve utilizzare:

*   **Liste**, **array**, e **dizionari** per organizzare i dati.
    
*   Strutture di controllo (if, while, for) per implementare la logica.
    
*   La suddivisione del codice in moduli separati:
    
    *   warehouse\_management.py per la gestione del magazzino.
        
    *   order\_management.py per la gestione degli ordini.
        
*   Un menu principale per navigare tra le varie funzionalità.
    

### **Istruzioni**

#### **Parte 1: Creazione del Magazzino**

1.  ```warehouse = { "Elettronica": {"Laptop": 10, "Smartphone": 20}, "Abbigliamento": {"Maglietta": 50, "Jeans": 30}, "Cibo": {"Mela": 30, "Pane": 25}}```
    
    *   Le **chiavi principali** rappresentano le categorie.
        
    *   Le **sottocategorie** sono dizionari con i prodotti e le rispettive quantità disponibili.
        
2.  Implementa le seguenti funzioni:
    
    *   **visualizza\_prodotti()**: Mostra i prodotti disponibili suddivisi per categoria.
        
    *   **aggiungi\_prodotto()**: Permette di aggiungere un prodotto o aggiornare la quantità di un prodotto esistente.
        
    *   **rimuovi\_prodotto()**: Rimuove un prodotto dal magazzino.
        
    *   **aggiorna\_quantita()**: Modifica la quantità di un prodotto specifico.
        
3.  Crea un menu principale per gestire il magazzino. Deve permettere di:
    
    *   Visualizzare i prodotti.
        
    *   Aggiungere nuovi prodotti.
        
    *   Aggiornare la quantità.
        
    *   Rimuovere prodotti.
        
    *   Accedere alla gestione degli ordini.
        
    *   Uscire dall'applicazione.
        

#### **Parte 2: Gestione degli Ordini**

1.  Crea una lista vuota chiamata order\_history per memorizzare gli ordini effettuati.
    
2.  Implementa le seguenti funzioni:
    
    *   **crea\_ordine(magazzino)**:
        
        *   Consente all'utente di scegliere i prodotti dal magazzino.
            
        *   Aggiorna il magazzino sottraendo le quantità ordinate.
            
        *   Salva i dettagli dell'ordine in order\_history.
            
    *   **visualizza\_ordini()**:
        
        *   Mostra la cronologia degli ordini effettuati.
            
3.  Implementa un menu per la gestione degli ordini, che permetta di:
    
    *   Creare un nuovo ordine.
        
    *   Visualizzare la cronologia degli ordini.
        
    *   Tornare al menu principale.
        

### **Consegna e Dettagli Tecnici**

1.  **Suddividi il progetto in due file principali**:
    
    *   warehouse\_management.py per la gestione del magazzino.
        
    *   order\_management.py per la gestione degli ordini.
        
2.  **Importa correttamente i moduli** e fai in modo che il menu principale gestisca entrambe le funzionalità.
    
3.  **Documenta il codice con commenti**:
    
    *   Ogni funzione deve avere un breve commento che spiega cosa fa.
        
    *   Usa nomi di variabili chiari e significativi.
        

### **Esempio di Utilizzo**

#### **Scenario 1: Gestione Magazzino**

*   L'utente accede al menu del magazzino.
    
*   Aggiunge un nuovo prodotto alla categoria "Cibo".
    
*   Visualizza i prodotti per verificare che il nuovo prodotto sia stato aggiunto.
    

#### **Scenario 2: Creazione di un Ordine**

*   L'utente accede al menu ordini.
    
*   Crea un nuovo ordine selezionando prodotti dal magazzino.
    
*   Visualizza la cronologia degli ordini per controllare l'ordine appena creato.
    

### **Valutazione**

Il progetto verrà valutato in base a:

1.  **Correttezza funzionale**: Tutte le funzionalità richieste sono implementate correttamente.
    
2.  **Uso delle strutture dati**: Liste, array e dizionari devono essere usati in modo appropriato.
    
3.  **Qualità del codice**: Il codice deve essere leggibile, ben organizzato e commentato.
    
4.  **Test degli scenari**: Verifica che il progetto gestisca correttamente input validi e invalidi.
