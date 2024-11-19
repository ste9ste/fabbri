# Fabrix v0.1 (Novembre 2024)
# Simulatore di processi produttivi nel settore secondario
# Sviluppatore: Stefano Solazzi Contessa
# File: simulate.py - Processi di simulazione

# Importazione librerie e dipfineenze
import random
import datetime

# Funzione che viene richiamata dalla GUI con lo scopo di generare la simulazione della produzione
def simulate(checkboxPercentualeProdottiFallati, checkboxPercentualeProdottiPrelevati, checkboxProbabilitaGuasti, checkboxTempoDiSettaggio):

    parametriProduzione = generaParametriProduzione() # Genero i paramtri di produzione

    numeroProdotti = generaNumeroProdottiDaProdurre() # Genero il numero di prodotti da produrre

    tempiReparti, tempoProduzioneTotale = calcoloTempoReparti(parametriProduzione, numeroProdotti) # Calcolo il tempo impiegato per la produzione in ogni reparto ed il tempo totale del processo

    # Gestisco le dinamiche dei "Prodotti Fallati", se il parametro "Percentuale Prodotti Fallati" è attivo
    if checkboxPercentualeProdottiFallati:
        percentualeFallati = round(random.uniform(0.8, 2.8), 2) # Calcola casualmente la percentuale di prodotti fallati entro il range stabilito

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
        probabilitaGuastiDeformatrice = random.randint(10, 20)  # Calcola casualmente la frequenza dei guasti deformatrice entro il range stabilito
        probabilitaGuastiForatrice = random.randint(5, 9)  # Calcola casualmente la frequenza dei guasti foratrice entro il range stabilito
        probabilitaGuastiTornitura = random.randint(14,28)  # Calcola casualmente la frequenza dei guasti tornitura entro il range stabilito
        tempoRisoluzioneGuastoDeformatrice = random.randint(1000, 2000) # Calcola casualmente il tempo di ripristino dai guasti deformatrice entro il range stabilito
        tempoRisoluzioneGuastoForatrice = random.randint(150,210)  # Calcola casualmente il tempo di ripristino dai guasti foratrice entro il range stabilito
        tempoRisoluzioneGuastoTornitura = random.randint(2500,3500)  # Calcola casualmente il tempo di ripristino dai guasti tornitura entro il range stabilito
        numeroGuastiDeformatrice = int(giornateDiProduzione / probabilitaGuastiDeformatrice)  # Calcolo il numero di guasti deformatrice che rientrano nel periodo di produzione
        numeroGuastiForatrice = int(giornateDiProduzione / probabilitaGuastiForatrice)  # Calcolo il numero di guasti deformatrice che rientrano nel periodo di produzione
        numeroGuastiTornitura = int(giornateDiProduzione / probabilitaGuastiTornitura)  # Calcolo il numero di guasti deformatrice che rientrano nel periodo di produzione

        numeroGuasti =  numeroGuastiDeformatrice + numeroGuastiForatrice+ numeroGuastiTornitura # Nel campo probabilità guasti inserisco il numero totale di guasti
        tempoRisoluzioneGuasti =  (numeroGuastiDeformatrice * tempoRisoluzioneGuastoDeformatrice) + (numeroGuastiForatrice * tempoRisoluzioneGuastoForatrice) + (numeroGuastiTornitura + tempoRisoluzioneGuastoTornitura) # Somma totale del tempo impiegato per risolvere i guasti

        tempoProduzioneTotale +=  tempoRisoluzioneGuasti # Aggiungo al tempo di produzione totale il tempo aggiuntivo causato dai guasti

    # Gestisco le dinamiche dei "Tempo di settaggio", se il parametro "Tempo di settaggii" è attivo
    if checkboxTempoDiSettaggio:
        # Alcuni prodotti non necessitano di alcuni reparti quindi moltiplico il tempo settaggio reparti per il numero di prodotti che sono lavorati nel reparto
        tempoDiSettaggioLaser = 3 * random.randint(100, 140) # Calcolo casualmente il tempo di settaggio entro il range stabilito reparto Taglio
        tempoDiSettaggioTrattamentoTermico = 3 * random.randint(10,20)  # Calcolo casualmente il tempo di settaggio entro il range stabilito reparto Trattamento Termico
        tempoDiSettaggioImballo = 3 * random.randint(5,15)  # Calcolo casualmente il tempo di settaggio entro il range stabilito reparto Imballlo
        tempoDiSettaggioDeformatura = 2 * random.randint(220,260)  # Calcolo casualmente il tempo di settaggio entro il range stabilito reparto Deformatura
        tempoDiSettaggioTornitura = 1 * random.randint(250,350)  # Calcolo casualmente il tempo di settaggio entro il range stabilito reparto Tornitura
        tempoDiSettaggioPiegatura = 1 * random.randint(20,40)  # Calcolo casualmente il tempo di settaggio entro il range stabilito reparto Piegatura
        tempoDiSettaggioForatura = 1 * random.randint(100, 140)  # Calcolo casualmente il tempo di settaggio entro il range stabilito reparto Foratura
        tempoDiSettaggioSaldatura = 1 * random.randint(20,40)  # Calcolo casualmente il tempo di settaggio entro il range stabilito reparto Saldatura

        # Sommo il tempo di settaggio dei singoli reparti
        tempoDiSettaggio = tempoDiSettaggioLaser + tempoDiSettaggioTrattamentoTermico + tempoDiSettaggioImballo + tempoDiSettaggioDeformatura + tempoDiSettaggioTornitura + tempoDiSettaggioPiegatura + tempoDiSettaggioForatura + tempoDiSettaggioSaldatura

    tempoDiProduzioneProdotto1 = 0 # Inizializzazione dei tempi totali di produzione per il prodotto 1: "Curve"
    tempoDiProduzioneProdotto2 = 0 # Inizializzazione dei tempi totali di produzione per il prodotto 2: "Tee"
    tempoDiProduzioneProdotto3 = 0 # Inizializzazione dei tempi totali di produzione per il prodotto 3: "Manicotti"

    # Calcolo del tempo totale di produzione per il prodotto "Curve"
    for chiave, tempo in parametriProduzione["Curve"].items(): # Ciclo attraverso ogni processo produttivo associato al prodotto "Curve"
        tempoDiProduzioneProdotto1 += tempo  # Aggiungo il tempo di ciascun processo al tempo totale di produzione per il prodotto "Curve"

    # Calcola i tempi di produzione per il prodotto "Tee"
    for chiave, tempo in parametriProduzione["Tee"].items(): # Ciclo attraverso ogni processo produttivo associato al prodotto "Tee"
        tempoDiProduzioneProdotto2 += tempo # Aggiungo il tempo di ciascun processo al tempo totale di produzione per il prodotto "Tee"

    # Calcola i tempi di produzione per il prodotto "Manicotti"
    for chiave, tempo in parametriProduzione["Manicotti"].items(): # Ciclo attraverso ogni processo produttivo associato al prodotto "Manicotti"
        tempoDiProduzioneProdotto3 += tempo # Aggiungo il tempo di ciascun processo al tempo totale di produzione per il prodotto "Manicotti"

    capacitaProduttiva = calcolatoreCapacitaReparto(parametriProduzione) # Richiamo la funzione per calcolare la capacità produttiva giornaliera di ogni reparto per ogni prodotto

    # Preparo il dizionario 'risultati' inserfineo i dati finali della simulazione
    risultati = {
        'percentualeProdottiFallati': percentualeFallati if checkboxPercentualeProdottiFallati else "Non attivo", # Registro nel dizionario la percentuale di prodotti fallati (se attivo)
        'percentualeProdottiPrelevati': percentualePrelevati if checkboxPercentualeProdottiPrelevati else "Non attivo", # Registro nel dizionario la percentuale di prodotti prelevati (se attivo)
        'numeroGuasti': numeroGuasti if checkboxProbabilitaGuasti else "Non attivo", # Registro nel dizionario il numero di guasti (se attivo)
        'tempoRisoluzioneGuasti': tempoRisoluzioneGuasti if checkboxProbabilitaGuasti else "Non attivo", # Registro nel dizionario il tempo di risoluzione guasti (se attivo)
        'tempoDiSettaggio': tempoDiSettaggio if checkboxTempoDiSettaggio else "Non attivo", # Registro nel dizionario il tempo di settaggio (se attivo)
        'tempoProduzioneTotale': round(tempoProduzioneTotale, 2), # Registro nel dizionario il tempo di produzione totale (arrotondato a due crifre decimali)
        'produzioneProdotto1': numeroProdotti.get("Curve", 0), # Registro nel dizionario il valore da produrre del prodotto "Curve"
        'produzioneProdotto2': numeroProdotti.get("Tee", 0), # Registro nel dizionario il valore da produrre del prodotto "Tee"
        'produzioneProdotto3': numeroProdotti.get("Manicotti", 0), # Registro nel dizionario il valore da produrre del prodotto "Manicotti"
        'tempoDiProduzioneProdotto1': round(tempoDiProduzioneProdotto1, 2), # Registro nel dizionario il tempo totale di produzione per "Curve"
        'tempoDiProduzioneProdotto2': round(tempoDiProduzioneProdotto2, 2), # Registro nel dizionario il tempo totale di produzione per "Tee"
        'tempoDiProduzioneProdotto3': round(tempoDiProduzioneProdotto3, 2), # Registro nel dizionario il tempo totale di produzione per "Manicotti"

        # Registrazione Prodotto 1
        # Registro nel dizionario la capacità giornaliera del reparto "Taglio" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoTaglioProdotto1': capacitaProduttiva["Curve"]["tempoTaglioCurve"],
        # Registro nel dizionario la capacità giornaliera del reparto "Tornitura" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoTornituraProdotto1': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Piegatura" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoPiegaturaProdotto1': capacitaProduttiva["Curve"]["tempoPiegaturaCurve"],
        # Registro nel dizionario la capacità giornaliera del reparto "Deformatura" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoDeformaturaProdotto1': capacitaProduttiva["Curve"]["tempoDeformaturaCurve"],
        # Registro nel dizionario la capacità giornaliera del reparto "Foratura" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoForaturaProdotto1': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Saldatura" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoSaldaturaProdotto1': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Trattamento termico" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoTrattamentoTermicoProdotto1': capacitaProduttiva["Curve"]["tempoTrattamentoTermicoCurve"],
        # Registro nel dizionario la capacità giornaliera del reparto "Montaggio o Marcatura" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoMontaggioOrMarcaturaProdotto1': capacitaProduttiva["Curve"]["tempoMontaggioOrMarcaturaCurve"],
        # Registro nel dizionario la capacità giornaliera del reparto "Imballo" riguardo la produzione del prodotto "Curve"
        'capacitaGiornalieraRepartoImballoProdotto1': capacitaProduttiva["Curve"]["tempoImballoCurve"],

        # Registrazione Prodotto 2
        # Registro nel dizionario la capacità giornaliera del reparto "Taglio" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoTaglioProdotto2': capacitaProduttiva["Tee"]["tempoTaglioTee"],
        # Registro nel dizionario la capacità giornaliera del reparto "Tornitura" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoTornituraProdotto2': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Piegatura" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoPiegaturaProdotto2': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Deformatura" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoDeformaturaProdotto2': capacitaProduttiva["Tee"]["tempoDeformaturaTee"],
        # Registro nel dizionario la capacità giornaliera del reparto "Foratura" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoForaturaProdotto2': capacitaProduttiva["Tee"]["tempoForaturaTee"],
        # Registro nel dizionario la capacità giornaliera del reparto "Saldatura" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoSaldaturaProdotto2': capacitaProduttiva["Tee"]["tempoSaldaturaTee"],
        # Registro nel dizionario la capacità giornaliera del reparto "Trattamento termico" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoTrattamentoTermicoProdotto2': capacitaProduttiva["Tee"]["tempoTrattamentoTermicoTee"],
        # Registro nel dizionario la capacità giornaliera del reparto "Montaggio o Marcatura" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoMontaggioOrMarcaturaProdotto2': capacitaProduttiva["Tee"]["tempoMontaggioOrMarcaturaTee"],
        # Registro nel dizionario la capacità giornaliera del reparto "Imballo" riguardo la produzione del prodotto "Tee"
        'capacitaGiornalieraRepartoImballoProdotto2': capacitaProduttiva["Tee"]["tempoImballoTee"],

        # Registrazione Prodotto 3
        # Registro nel dizionario la capacità giornaliera del reparto "Taglio" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoTaglioProdotto3': capacitaProduttiva["Manicotti"]["tempoTaglioManicotti"],
        # Registro nel dizionario la capacità giornaliera del reparto "Tornitura" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoTornituraProdotto3': capacitaProduttiva["Manicotti"]["tempoTornituraManicotti"],
        # Registro nel dizionario la capacità giornaliera del reparto "Piegatura" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoPiegaturaProdotto3': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Deformatura" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoDeformaturaProdotto3': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Foratura" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoForaturaProdotto3': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Saldatura" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoSaldaturaProdotto3': "ND",
        # Registro nel dizionario la capacità giornaliera del reparto "Trattamento termico" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoTrattamentoTermicoProdotto3': capacitaProduttiva["Manicotti"]["tempoTrattamentoTermicoManicotti"],
        # Registro nel dizionario la capacità giornaliera del reparto "Montaggio o Marcatura" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoMontaggioOrMarcaturaProdotto3': capacitaProduttiva["Manicotti"]["tempoMontaggioOrMarcaturaManicotti"],
        # Registro nel dizionario la capacità giornaliera del reparto "Imballo" riguardo la produzione del prodotto "Manicotti"
        'capacitaGiornalieraRepartoImballoProdotto3': capacitaProduttiva["Manicotti"]["tempoImballoManicotti"],

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
    tempiReparto = {reparto: 0 for reparto in ["Taglio", "Tornitura", "Piegatura", "Deformatura", "Foratura", "Saldatura", "TrattamentoTermico", "MontaggioOrMarcatura", "Imballo"]} # Creo un dizionario per tenere traccia del tempo utilizzato da ogni reparto
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
        "Curve": [
            ("Taglio", 0.054, 0.066),
            ("Piegatura", 0.054, 0.066),
            ("Deformatura", 0.18, 0.22),
            ("TrattamentoTermico", 0.022, 0.026),
            ("MontaggioOrMarcatura", 0.09, 0.11),
            ("Imballo", 0.036, 0.044)
        ],
        "Tee": [
            ("Taglio", 0.077, 0.095),
            ("Deformatura", 0.54, 0.66),
            ("Foratura", 0.9, 1.1),
            ("Saldatura", 0.338, 0.413),
            ("TrattamentoTermico", 0.022, 0.026),
            ("MontaggioOrMarcatura", 0.36, 0.44),
            ("Imballo", 0.036, 0.044)
        ],
        "Manicotti": [
            ("Taglio", 0.09, 0.11),
            ("Tornitura", 0.12, 0.146),
            ("TrattamentoTermico", 0.022, 0.026),
            ("MontaggioOrMarcatura", 0.135, 0.165),
            ("Imballo", 0.036, 0.044)
        ]
    } # Dizionario dei prodotti con i rispettivi reparti e range di tempo di produzione in minuti

    parametri = {} # Dizionario per memorizzare i parametri di produzione con tempi specifici per ciascun reparto

    # Cicli annidati per generare tempi di produzione casuali per ogni prodotto in ogni reparto
    for prodotto, reparti in prodotti.items(): # Ciclo per ogni prodotto
        parametri[prodotto] = {}  # Creo un dizionario vuoto per memorizzare i tempi di produzione del prodotto
        for reparto in reparti: # Ciclo per ogni reparto relativo al prodotto
            nomeReparto, minTempo, maxTempo = reparto # Recupero il nome del reparto e i relativi range di tempo
            tempoCasuale = random.uniform(minTempo, maxTempo) # Genero casualmente un tempo di produzione per il prodotto nel range previsto dal reparto
            tempoChiave = f"tempo{nomeReparto.replace(' ', '')}{prodotto.replace(' ', '')}" # Costruisco la chiave per il dizionario
            parametri[prodotto][tempoChiave] = tempoCasuale # Assegno il tempo di produzione casuale generato per il prodotto al reparto

    return parametri # Restituisco il dizionario al chiamante

# Funzione per generare casualmente il numero di prodotti da produrre nel lotto nelle tre varianti
def generaNumeroProdottiDaProdurre():

    # La produzione aziendale avviene per lotti che possono avere dimensioni diverse, ma stabilite
    prodotti = {
        "Curve": [20000, 50000],  # Lotti disponibili per "Curve"
        "Tee": [4000, 8000, 12000],  # Lotti disponibili per "Tee"
        "Manicotti": [15000, 30000, 50000]  # Lotti disponibili per "Manicotti"
    } # Dizionario contentene le tre varianti prodotto

    # Ciclo per associare ad ogni prodotto un numero casuale di unità da produrre nel un range stabilito
    numeroProdotti = {prodotto: random.choice(lotti) for prodotto, lotti in prodotti.items()}

    return numeroProdotti  # La funzione ritorna il dizionario al termine dell'elaborazione
