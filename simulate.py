# Fabrix v0.1 (Novembre 2024)
# Simulatore di processi produttivi nel settore secondario
# Sviluppatore: Stefano Solazzi Contessa
# File: simulate.py - Processi di simulazione

# Importazione librerie e dipfineenze
import random
import datetime

# Funzione che viene richiamata dalla GUI con lo scopo di
def simulate(checkboxPercentualeProdottiFallati, checkboxPercentualeProdottiPrelevati, checkboxProbabilitaGuasti, checkboxTempoDiSettaggio):

    parametriProduzione = generaParametriProduzione() # Genero i paramtri di produzione

    numeroProdotti = generaNumeroProdottiDaProdurre() # Genero il numero di prodotti da produrre

    tempiReparti, tempoProduzioneTotale = calcoloTempoReparti(parametriProduzione, numeroProdotti) # Calcolo il tempo impiegato per la produzione in ogni reparto ed il tempo totale del processo

    # Gestisco le dinamiche dei "Prodotti Fallati", se il parametro "Percentuale Prodotti Fallati" è attivo
    if checkboxPercentualeProdottiFallati:
        percentualeFallati = round(random.uniform(0.5, 2), 2) # Calcola casualmente la percentuale di prodotti fallati entro il range stabilito

        # Aggiorna il numero totale di prodotti per includere la percentuale fallata
        for prodotto in numeroProdotti: # Ciclo attraverso ogni tipologia di prodotto nel dizionario
            quantitaOriginale = numeroProdotti[prodotto] # Recupero la quantità originale prevista per la produzione del prodotto
            quantitaFallata = int(quantitaOriginale * (percentualeFallati / 100)) # Calcolo il numero di prodotti fallati in base alla percentuale
            numeroProdotti[prodotto] = quantitaOriginale + quantitaFallata # Aggiorno la quantità totale di prodotti includfineo quelli fallati

    # Gestisco le dinamiche dei "Prodotti Prelevati", se il parametro "Percentuale Prodotti Prelevati" è attivo
    if checkboxPercentualeProdottiPrelevati:
        percentualePrelevati = round(random.uniform(0.1, 0.5), 2) # Calcola casualmente la percentuale di prodotti prelevati entro il range stabilito

        # Aggiorna il numero totale di prodotti per includere la percentuale prelevata
        for prodotto in numeroProdotti: # Ciclo attraverso ogni tipologia di prodotto nel dizionario
            quantitaOriginale = numeroProdotti[prodotto] # Recupero la quantità originale prevista per la produzione del prodotto
            quantitaAggiuntiva = int(quantitaOriginale * (percentualePrelevati / 100)) # Calcolo il numero di prodotti prelevati in base alla percentuale
            numeroProdotti[prodotto] = quantitaOriginale + quantitaAggiuntiva # Aggiorno la quantità totale di prodotti includfineo quelli prelevati

    # Gestisco le dinamiche dei "Probabilità Guasti", se il parametro "Probabilità Guasti" è attivo
    if checkboxProbabilitaGuasti:
        oreDiProduzione = tempoProduzioneTotale / 60 # Recupero le ore di produzione totali stimate
        giornateDiProduzione = oreDiProduzione / 24 # Recupero le giornate di produzione totali stimate
        probabilitaGuasti = random.randint(1, 3)  # Calcola casualmente la frequenza dei guasti entro il range stabilito
        tempoRisoluzioneGuasto = random.randint(60, 120) # Calcola casualmente il tempo di ripristino dai guasti entro il range stabilito
        numeroGuasti = int(giornateDiProduzione / probabilitaGuasti)  # Calcolo il numero di guasti che rientratno nel periodo di produzione
        tempoProduzioneTotale += numeroGuasti * tempoRisoluzioneGuasto # Aggiungo al tempo di produzione totale il tempo aggiuntivo causato dai guasti

    # Gestisco le dinamiche dei "Tempo di settaggio", se il parametro "Tempo di settaggii" è attivo
    if checkboxTempoDiSettaggio:
        tempoDiSettaggio = random.randint(30, 120) # Calcolo casualmente il tempo di settaggio entro il range stabilito
        tempoProduzioneTotale += tempoDiSettaggio * 3  # Aggiungo al tempo di produzione totale il tempo aggiuntivo derivato dall'attrezzeria dei tre prodotti nel reparto di stampaggio (gli altri reparti non necessitano di attrezzaggio)

    tempoDiProduzioneProdotto1 = 0 # Inizializzazione dei tempi totali di produzione per il prodotto 1: "Raccorderia a pressare"
    tempoDiProduzioneProdotto2 = 0 # Inizializzazione dei tempi totali di produzione per il prodotto 2: "Sistemi di scarico"
    tempoDiProduzioneProdotto3 = 0 # Inizializzazione dei tempi totali di produzione per il prodotto 3: "Collari"

    # Calcolo del tempo totale di produzione per il prodotto "Raccorderia a pressare"
    for chiave, tempo in parametriProduzione["Raccorderia a pressare"].items(): # Ciclo attraverso ogni processo produttivo associato al prodotto "Raccorderia a pressare"
        tempoDiProduzioneProdotto1 += tempo  # Aggiungo il tempo di ciascun processo al tempo totale di produzione per il prodotto "Raccorderia a pressare"

    # Calcola i tempi di produzione per il prodotto "Sistemi di scarico"
    for chiave, tempo in parametriProduzione["Sistemi di scarico"].items(): # Ciclo attraverso ogni processo produttivo associato al prodotto "Sistemi di scarico"
        tempoDiProduzioneProdotto2 += tempo # Aggiungo il tempo di ciascun processo al tempo totale di produzione per il prodotto "Sistemi di scarico"

    # Calcola i tempi di produzione per il prodotto "Collari"
    for chiave, tempo in parametriProduzione["Collari"].items(): # Ciclo attraverso ogni processo produttivo associato al prodotto "Collari"
        tempoDiProduzioneProdotto3 += tempo # Aggiungo il tempo di ciascun processo al tempo totale di produzione per il prodotto "Collari"

    capacitaProduttiva = calcolatoreCapacitaReparto(parametriProduzione) # Richiamo la funzione per calcolare la capacità produttiva giornaliera di ogni reparto per ogni prodotto

    # Preparo il dizionario 'risultati' inserfineo i dati finali della simulazione
    risultati = {
        'percentualeProdottiFallati': percentualeFallati if checkboxPercentualeProdottiFallati else "Non attivo", # Registro nel dizionario la percentuale di prodotti fallati (se attivo)
        'percentualeProdottiPrelevati': percentualePrelevati if checkboxPercentualeProdottiPrelevati else "Non attivo", # Registro nel dizionario la percentuale di prodotti prelevati (se attivo)
        'probabilitaGuasti': probabilitaGuasti if checkboxProbabilitaGuasti else "Non attivo", # Registro nel dizionario la probabilità di guasti (se attivo)
        'tempoRisoluzioneGuasto': tempoRisoluzioneGuasto if checkboxProbabilitaGuasti else "Non attivo", # Registro nel dizionario il tempo di risoluzione guasti (se attivo)
        'tempoDiSettaggio': tempoDiSettaggio if checkboxTempoDiSettaggio else "Non attivo", # Registro nel dizionario il tempo di settaggio (se attivo)
        'tempoProduzioneTotale': round(tempoProduzioneTotale, 2), # Registro nel dizionario il tempo di produzione totale (arrotondato a due crifre decimali)
        'produzioneProdotto1': numeroProdotti.get("Raccorderia a pressare", 0), # Registro nel dizionario il valore da produrre del prodotto "Raccorderia a pressare"
        'produzioneProdotto2': numeroProdotti.get("Sistemi di scarico", 0), # Registro nel dizionario il valore da produrre del prodotto "Sistemi di scarico"
        'produzioneProdotto3': numeroProdotti.get("Collari", 0), # Registro nel dizionario il valore da produrre del prodotto "Collari"
        'tempoDiProduzioneProdotto1': tempoDiProduzioneProdotto1, # Registro nel dizionario il tempo totale di produzione per "Raccorderia a pressare"
        'tempoDiProduzioneProdotto2': tempoDiProduzioneProdotto2, # Registro nel dizionario il tempo totale di produzione per "Sistemi di scarico"
        'tempoDiProduzioneProdotto3': tempoDiProduzioneProdotto3, # Registro nel dizionario il tempo totale di produzione per "Collari"
        'capacitaGiornalieraRepartoStampaggioProdotto1': capacitaProduttiva["Raccorderia a pressare"]["tempoStampaggioRaccorderiaapressare"], # Registro nel dizionario la capacità giornaliera del reparto "Stampaggio" riguardo la produzione del prodotto "Raccorderia a pressare"
        'capacitaGiornalieraRepartoTrattamentoSuperficialeProdotto1': capacitaProduttiva["Raccorderia a pressare"]["tempoTrattamentoSuperficialeRaccorderiaapressare"], # Registro nel dizionario la capacità giornaliera del reparto "Trattamento superficiale" riguardo la produzione del prodotto "Raccorderia a pressare"
        'capacitaGiornalieraRepartoPiegaturaProdotto1': "ND", # Registro nel dizionario la capacità giornaliera del reparto "Piegatura" riguardo la produzione del prodotto "Raccorderia a pressare"
        'capacitaGiornalieraRepartoAssemblaggioProdotto1': capacitaProduttiva["Raccorderia a pressare"]["tempoAssemblaggioRaccorderiaapressare"], # Registro nel dizionario la capacità giornaliera del reparto "Assemblaggio" riguardo la produzione del prodotto "Raccorderia a pressare"
        'capacitaGiornalieraRepartoConfezionamentoProdotto1': capacitaProduttiva["Raccorderia a pressare"]["tempoConfezionamentoRaccorderiaapressare"], # Registro nel dizionario la capacità giornaliera del reparto "Confezionamento" riguardo la produzione del prodotto "Raccorderia a pressare"
        'capacitaGiornalieraRepartoStampaggioProdotto2': capacitaProduttiva["Sistemi di scarico"]["tempoStampaggioSistemidiscarico"], # Registro nel dizionario la capacità giornaliera del reparto "Stampaggio" riguardo la produzione del prodotto "Sistemi di scarico"
        'capacitaGiornalieraRepartoTrattamentoSuperficialeProdotto2': capacitaProduttiva["Sistemi di scarico"]["tempoTrattamentoSuperficialeSistemidiscarico"], # Registro nel dizionario la capacità giornaliera del reparto "Trattamento superficiale" riguardo la produzione del prodotto "Sistemi di scarico"
        'capacitaGiornalieraRepartoPiegaturaProdotto2': capacitaProduttiva["Sistemi di scarico"]["tempoPiegaturaSistemidiscarico"], # Registro nel dizionario la capacità giornaliera del reparto "Piegatura" riguardo la produzione del prodotto "Sistemi di scarico"
        'capacitaGiornalieraRepartoAssemblaggioProdotto2': capacitaProduttiva["Sistemi di scarico"]["tempoAssemblaggioSistemidiscarico"], # Registro nel dizionario la capacità giornaliera del reparto "Assemblaggio" riguardo la produzione del prodotto "Sistemi di scarico"
        'capacitaGiornalieraRepartoConfezionamentoProdotto2': capacitaProduttiva["Sistemi di scarico"]["tempoConfezionamentoSistemidiscarico"], # Registro nel dizionario la capacità giornaliera del reparto "Confezionamento" riguardo la produzione del prodotto "Sistemi di scarico"
        'capacitaGiornalieraRepartoStampaggioProdotto3': capacitaProduttiva["Collari"]["tempoStampaggioCollari"], # Registro nel dizionario la capacità giornaliera del reparto "Stampaggio" riguardo la produzione del prodotto "Collari"
        'capacitaGiornalieraRepartoTrattamentoSuperficialeProdotto3': "ND", # Registro nel dizionario la capacità giornaliera del reparto "Trattamento superficiale" riguardo la produzione del prodotto "Collari"
        'capacitaGiornalieraRepartoPiegaturaProdotto3': capacitaProduttiva["Collari"]["tempoPiegaturaCollari"], # Registro nel dizionario la capacità giornaliera del reparto "Piegatura" riguardo la produzione del prodotto "Collari"
        'capacitaGiornalieraRepartoAssemblaggioProdotto3': capacitaProduttiva["Collari"]["tempoAssemblaggioCollari"], # Registro nel dizionario la capacità giornaliera del reparto "Assemblaggio" riguardo la produzione del prodotto "Collari"
        'capacitaGiornalieraRepartoConfezionamentoProdotto3': capacitaProduttiva["Collari"]["tempoConfezionamentoCollari"], # Registro nel dizionario la capacità giornaliera del reparto "Confezionamento" riguardo la produzione del prodotto "Collari"
        'nomeLotto': datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Registro nel dizionario il valore del lotto. Per questa simulazione utilizzerò il valore del timestamp
    }

    return risultati # Ritorno il dizionario alla funzione chiamante

# Funzione che calcola la capacità giornaliera di ogni reparto relativa ad ogni differente prodotto
def calcolatoreCapacitaReparto(parametriProduzione):

    totaleMinutiLavoro = 24 * 60  # Calcolo il totale dei minuti lavorativi in un turno di 24 ore

    capacitaReparto = {} # Inizializzazione di un dizionario destinato a contenere le capacità di produzione
    for prodotto, tempi in parametriProduzione.items(): # Ciclo per ogni prodotto e relativo tempo di produzione per ciascun reparto
        capacitaReparto[prodotto] = {} # Inizializzo un dizionario per ogni prodotto
        for chiave, tempo in tempi.items(): # Ciclo per ogni reparto associato al reparto

            capacitaReparto[prodotto][chiave] = int(totaleMinutiLavoro / tempo) # Calcolo il numero massimo di pezzi che possono essere prodotti in un giorno

    return capacitaReparto # Ritorno al chiamante il dizionario

# Funzione per calcolare i tempi di produzione per ogni reparto e prodotto
def calcoloTempoReparti(parametriProduzione, numeroProdotti):
    tempiReparto = {reparto: 0 for reparto in ["Stampaggio", "TrattamentoSuperficiale", "Piegatura", "Assemblaggio", "Confezionamento"]} # Creo un dizionario per tenere traccia del tempo utilizzato da ogni reparto
    tempiProdottoReparto = {prodotto: {reparto: 0 for reparto in tempiReparto} for prodotto in numeroProdotti} # Creo un dizionario per tenere traccia del tempo utilizzato per ogni prodotto in ogni reparto

    tempoProduzioneTotale = 0 # Creo una variabile per sommare il tempo totale della produzione

    # Calcolo i tempi di produzione dei diversi reparti
    for prodotto, dettagli in parametriProduzione.items(): # Ciclo su ogni prodotto e relativi dettagli
        tempoPrecedente = 0 # Variabile temporanea per tenere in memoria il tempo di fine dell'ultimo processo
        for key in dettagli: # Ciclo su ogni chiave nei dettagli del prodotto
            reparto = key.split('tempo')[1].replace(prodotto.replace(' ', ''), '') # Estraggo il nome del reparto dalla chiave
            tempoCiclo = dettagli[key] # Ottengo il tempo di ciclo per un pezzo in questo reparto, come generato dalla funzione preposta
            numeroPezzi = numeroProdotti[prodotto] # Ottengo il numero di pezzi da produrre, come generato dalla funzione preposta
            tempoTotaleReparto = tempoCiclo * numeroPezzi  # Calcolo il tempo totale di produzione per tutti i pezzi in questo reparto

            partenza = max(tempiReparto[reparto], tempoPrecedente) # Determino il momento di inizio del processo corrente
            fine = partenza + tempoTotaleReparto # Calcolo il momento di fine del processo corrente
            tempiReparto[reparto] = fine  # Aggiorno il tempo in cui ha terminato il processo nel dizionario dei tempi di reparto
            tempiProdottoReparto[prodotto][reparto] = fine # Aggiorno il tempo in cui ha terminato il processo nel dizionario dei prodotti
            tempoPrecedente = fine # Imposto il tempo di fine corrente per la prossima ciclata
            tempoProduzioneTotale += tempoTotaleReparto # Aggiungo il tempo totale del reparto al tempo di produzione totale

    tempiTotaliReparto = {reparto: max(prodotto[reparto] for prodotto in tempiProdottoReparto.values()) for reparto in tempiReparto} # Calcolo i tempi totali per ciascun reparto prendendo il massimo tempo di fine tra tutti i prodotti

    return tempiTotaliReparto, tempoProduzioneTotale # Restituisco i dizionari dei tempi totali per reparto e il tempo totale di produzione al chiamante

# Funzione per generare i parametri di produzione casualmente all'interno di range stabiliti
def generaParametriProduzione():

    prodotti = {
        "Raccorderia a pressare": [
            ("Stampaggio", 1, 5), ("TrattamentoSuperficiale", 1, 3), ("Assemblaggio", 4, 8), ("Confezionamento", 1, 2)
        ],
        "Sistemi di scarico": [
            ("Stampaggio", 1, 10), ("Piegatura", 1, 2), ("TrattamentoSuperficiale", 1, 2), ("Assemblaggio", 8, 15), ("Confezionamento", 2, 5)
        ],
        "Collari": [
            ("Stampaggio", 1, 3), ("Piegatura", 1, 2), ("Assemblaggio", 2, 4), ("Confezionamento", 2, 3)
        ]
    } # Dizionario dei prodotti con i rispettivi reparti e range di tempo di produzione in minuti

    parametri = {} # Dizionario per memorizzare i parametri di produzione con tempi specifici per ciascun reparto

    # Cicli annidati per generare tempi di produzione casuali per ogni prodotto in ogni reparto
    for prodotto, reparti in prodotti.items(): # Ciclo per ogni prodotto
        parametri[prodotto] = {}  # Creo un dizionario vuoto per memorizzare i tempi di produzione del prodotto
        for reparto in reparti: # Ciclo per ogni reparto relativo al prodotto
            nomeReparto, minTempo, maxTempo = reparto # Recupero il nome del reparto e i relativi range di tempo
            tempoCasuale = random.randint(minTempo, maxTempo) # Genero casualmente un tempo di produzione per il prodotto nel range previsto dal reparto
            tempoChiave = f"tempo{nomeReparto.replace(' ', '')}{prodotto.replace(' ', '')}" # Costruisco la chiave per il dizionario
            parametri[prodotto][tempoChiave] = tempoCasuale # Assegno il tempo di produzione casuale generato per il prodotto al reparto

    return parametri # Restituisco il dizionario al chiamante

# Funzione per generare casualmente il numero di prodotti da produrre nelle tre varianti
def generaNumeroProdottiDaProdurre():
    prodotti = ["Raccorderia a pressare", "Sistemi di scarico", "Collari"] # Dizionario contentene le tre varianti prodotto
    numeroProdotti = {prodotto: random.randint(1000, 10000) for prodotto in prodotti} # Associo ad ogni prodotto un numero casuale di unità da produrre in un range prestabilito
    return numeroProdotti # La funzione ritorna il dizionario al termine dell'elaborazione
