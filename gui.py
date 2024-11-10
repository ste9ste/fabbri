# Fabrix v0.1 (Novembre 2024)
# Simulatore di processi produttivi nel settore secondario
# Sviluppatore: Stefano Solazzi Contessa
# File: gui.py - Gestione dell'interfaccia grafica

# Importazione librerie e dipendenze
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QCheckBox, QHBoxLayout, QGroupBox, QTableWidget, QHeaderView
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from simulate import simulate

# Classe di gestione dell'interfaccia grafica
class Gui(QWidget):

    # Costuttore della classe
    def __init__(self):
        super().__init__() # Inizializza la classe base QWidget
        self.inizializzaInterfacciaGrafica() # Chiamata alla funzione per inizializzazione interfaccia

    # Funzione per inizializzazione interfaccia
    def inizializzaInterfacciaGrafica(self):

        # Sezione Finestra
        self.setWindowTitle('Fabrix') # Impostazione titolo finestra
        self.resize(600, 900) # Impostazione dimensioni finestra
        self.center() # Richiamo funzione per centrare la finestra
        layoutPrincipale = QVBoxLayout() # Creazione layout principale
        layoutPrincipale.setAlignment(Qt.AlignTop) # Allineamento widget in alto

        # Sezione Logo Fabrix
        etichettaLogo = QLabel(self) # Etichetta del logo
        immagineLogo = QPixmap("fabrix.png") # Caricamento immagine logo
        immagineLogo = immagineLogo.scaled(250, immagineLogo.height(), Qt.KeepAspectRatio) # Impostazione rapporto di aspetto
        etichettaLogo.setPixmap(immagineLogo) # Inserimento dell'immagine nell'etichetta
        etichettaLogo.setAlignment(Qt.AlignCenter) # Allineamento al centro dell'etichetta
        layoutLogo = QVBoxLayout() # Creazione layout logo
        layoutLogo.setAlignment(Qt.AlignCenter) # Allineamento al centro del layout del logo
        layoutLogo.setContentsMargins(0, 15, 0, 0) # Dichiarazione margini logo
        layoutLogo.addWidget(etichettaLogo) # Aggiunta etichetta al layout
        layoutPrincipale.addLayout(layoutLogo) # Aggiunta layout del logo al layout principale

        # Sezione gruppo "Parametri di simulazione"
        groupBoxParametri = QGroupBox("Parametri di simulazione") # Creazione gruppo "Parametri di simulazione"
        groupBoxParametriLayout = QHBoxLayout()  # Creazione layout su due colonne

        # Sezione gruppo "Parametri di simulazione" - Colonna 1
        colonna1 = QVBoxLayout() # Creazione layout per colonna 1

        # Sezione parametro "Percentuale prodotti fallati"
        self.checkboxPercentualeProdottiFallati = QCheckBox("Attiva Percentuale prodotti fallati") # Checkbox "Prodotti fallati"
        self.testoPercentualeProdottiFallati = QLineEdit() # Creazione casella di testo "Prodotti fallati"
        self.testoPercentualeProdottiFallati.setReadOnly(True) # Set casella di testo "Prodotti fallati" in sola lettura
        colonna1.addWidget(self.checkboxPercentualeProdottiFallati) # Aggiunta checkbox "Prodotti fallati" a colonna 1
        colonna1.addWidget(self.testoPercentualeProdottiFallati) # Aggiunta casella di testo "Prodotti fallati" a colonna 1

        # Sezione parametro "Prodotti prelevati controllo qualità"
        self.checkboxPercentualeProdottiPrelevati = QCheckBox(
            "Attiva Percentuale prodotti prelevati per controllo qualità") # Checkbox "Prodotti prelevati controllo qualità"
        self.testoPercentualeProdottiPrelevati = QLineEdit() # Creazione casella di testo "Prodotti prelevati controllo qualità"
        self.testoPercentualeProdottiPrelevati.setReadOnly(True) # Set casella di testo "Prodotti prelevati controllo qualità" in sola lettura
        colonna1.addWidget(self.checkboxPercentualeProdottiPrelevati) # Aggiunta checkbox "Prodotti prelevati controllo qualità" a colonna 1
        colonna1.addWidget(self.testoPercentualeProdottiPrelevati)  # Aggiunta casella di testo "Prodotti prelevati controllo qualità" a colonna 1

        # Sezione parametro "Probabilità guasti"
        self.checkboxProbabilitaGuasti = QCheckBox("Attiva Probabilità guasti") # Checkbox "Probabilità guasti"
        self.testoProbabilitaGuasti = QLineEdit() # Creazione casella di testo "Probabilità guasti"
        self.testoProbabilitaGuasti.setReadOnly(True) # Set casella di testo "Probabilità guasti" in sola lettura
        colonna1.addWidget(self.checkboxProbabilitaGuasti) # Aggiunta checkbox "Probabilità guasti" a colonna 1
        colonna1.addWidget(self.testoProbabilitaGuasti) # Aggiunta casella di testo "Probabilità guasti" a colonna 1

        # Sezione parametro "Tempo di settaggio"
        self.checkboxTempoDiSettaggio = QCheckBox("Attiva Tempo di settaggio") # Checkbox "Tempo di settaggio"
        self.testoTempoDiSettaggio = QLineEdit() # Creazione casella di testo "Tempo di settaggio"
        self.testoTempoDiSettaggio.setReadOnly(True) # Set casella di testo "Tempo di settaggio" in sola lettura
        colonna1.addWidget(self.checkboxTempoDiSettaggio) # Aggiunta checkbox "Tempo di settaggio" a colonna 1
        colonna1.addWidget(self.testoTempoDiSettaggio) # Aggiunta casella di testo "Tempo di settaggio" a colonna 1

        # Sezione gruppo "Parametri di simulazione" - Colonna 2
        colonna2 = QVBoxLayout() # Creazione layout per colonna 2

        # Sezione parametro "Tempo risoluzione guasto"
        self.testoTempoRisoluzioneGuasto = QLineEdit() # Creazione casella di testo "Tempo risoluzione guasto"
        self.testoTempoRisoluzioneGuasto.setReadOnly(True) # Set casella di testo "Tempo risoluzione guasto" in sola lettura
        colonna2.addWidget(QLabel("Tempo risoluzione guasto")) # Aggiunta didascalia "Tempo risoluzione guasto" a colonna 2
        colonna2.addWidget(self.testoTempoRisoluzioneGuasto) # Aggiunta casella di testo "Tempo risoluzione guasto" a colonna 2

        # Sezione indicazione "Lotto"
        self.testoLotto = QLineEdit() # Creazione casella di testo "Lotto"
        self.testoLotto.setReadOnly(True) # Set casella di testo "Lotto" in sola lettura
        colonna2.addWidget(QLabel("Lotto")) # Aggiunta didascalia "Lotto" a colonna 2
        colonna2.addWidget(self.testoLotto) # Aggiunta casella di testo "Lotto" a colonna 2

        # Aggiunta colonne nel layout gruppo "Parametri di simulazione"
        groupBoxParametriLayout.addLayout(colonna1) # Inserimento colonna 1 nel gruppo "Parametri di simulazione"
        groupBoxParametriLayout.addLayout(colonna2) # Inserimento colonna 2 nel gruppo "Parametri di simulazione"

        groupBoxParametri.setLayout(groupBoxParametriLayout) # Impostazione del layout contenente le due colonne
        layoutPrincipale.addWidget(groupBoxParametri) # Aggiunta del gruppo "Parametri di simulazione" al layout principale

        layoutDoppiaColonna = QHBoxLayout() # Impostazione layout orizzontale per le due colonne inferiori

        colonna1 = QVBoxLayout() # Creazione layout per colonna 1

        # Sezione gruppo "Produzione Prodotto 1" - Colonna 1
        groupBoxProduzione1 = QGroupBox("Produzione Raccorderia a pressare") # Creazione gruppo "Produzione Prodotto 1"
        groupBoxProduzione1Layout = QVBoxLayout() # Creazione layout verticale per gruppo "Produzione Prodotto 1"
        self.testoProduzioneProdotto1 = QLineEdit() # Creazione casella di testo "Produzione Prodotto 1"
        self.testoProduzioneProdotto1.setReadOnly(True) # Set casella di testo "Produzione Prodotto 1" in sola lettura
        groupBoxProduzione1Layout.addWidget(self.testoProduzioneProdotto1) # Aggiunta casella di testo "Produzione Prodotto 1" al layout del gruppo "Produzione Prodotto 1"
        self.testoTempoDiProduzioneProdotto1 = QLineEdit() # Creazione casella di testo "Tempo Di Produzione Prodotto 1"
        self.testoTempoDiProduzioneProdotto1.setReadOnly(True) # Set casella di testo "Tempo Di Produzione Prodotto 1" in sola lettura
        groupBoxProduzione1Layout.addWidget(self.testoTempoDiProduzioneProdotto1) # Aggiunta casella di testo "Tempo di Produzione Prodotto 1" al layout del gruppo "Produzione Prodotto 1"
        groupBoxProduzione1.setLayout(groupBoxProduzione1Layout) # Imposta il layout del gruppo "Produzione Prodotto 1"
        colonna1.addWidget(groupBoxProduzione1) # Aggiunta gruppo "Produzione Prodotto 1" a colonna 1

        # Sezione gruppo "Produzione Prodotto 2" - Colonna 1
        groupBoxProduzione2 = QGroupBox("Produzione Sistemi di scarico") # Creazione gruppo "Produzione Prodotto 2"
        groupBoxProduzione2Layout = QVBoxLayout() # Creazione layout verticale per gruppo "Produzione Prodotto 2"
        self.testoProduzioneProdotto2 = QLineEdit() # Creazione casella di testo "Produzione Prodotto 2"
        self.testoProduzioneProdotto2.setReadOnly(True) # Set casella di testo "Produzione Prodotto 2" in sola lettura
        groupBoxProduzione2Layout.addWidget(self.testoProduzioneProdotto2) # Aggiunta casella di testo "Produzione Prodotto 2" al layout del gruppo "Produzione Prodotto 2"
        self.testoTempoDiProduzioneProdotto2 = QLineEdit() # Creazione casella di testo "Tempo Di Produzione Prodotto 2"
        self.testoTempoDiProduzioneProdotto2.setReadOnly(True) # Set casella di testo "Tempo Di Produzione Prodotto 2" in sola lettura
        groupBoxProduzione2Layout.addWidget(self.testoTempoDiProduzioneProdotto2) # Aggiunta casella di testo "Tempo di Produzione Prodotto 2" al layout del gruppo "Produzione Prodotto 2"
        groupBoxProduzione2.setLayout(groupBoxProduzione2Layout) # Imposta il layout del gruppo "Produzione Prodotto 2"
        colonna1.addWidget(groupBoxProduzione2) # Aggiunta gruppo "Produzione Prodotto 2" a colonna 1

        # Sezione gruppo "Produzione Prodotto 3" - Colonna 1
        groupBoxProduzione3 = QGroupBox("Produzione Collari") # Creazione gruppo "Produzione Prodotto 3"
        groupBoxProduzione3Layout = QVBoxLayout() # Creazione layout verticale per gruppo "Produzione Prodotto 3"
        self.testoProduzioneProdotto3 = QLineEdit() # Creazione casella di testo "Produzione Prodotto 3"
        self.testoProduzioneProdotto3.setReadOnly(True) # Set casella di testo "Produzione Prodotto 3" in sola lettura
        groupBoxProduzione3Layout.addWidget(self.testoProduzioneProdotto3) # Aggiunta casella di testo "Produzione Prodotto 3" al layout del gruppo "Produzione Prodotto 3"
        self.testoTempoDiProduzioneProdotto3 = QLineEdit() # Creazione casella di testo "Tempo Di Produzione Prodotto 3"
        self.testoTempoDiProduzioneProdotto3.setReadOnly(True) # Set casella di testo "Tempo Di Produzione Prodotto 3" in sola lettura
        groupBoxProduzione3Layout.addWidget(self.testoTempoDiProduzioneProdotto3) # Aggiunta casella di testo "Tempo di Produzione Prodotto 3" al layout del gruppo "Produzione Prodotto 3"
        groupBoxProduzione3.setLayout(groupBoxProduzione3Layout) # Imposta il layout del gruppo "Produzione Prodotto 3"
        colonna1.addWidget(groupBoxProduzione3) # Aggiunta gruppo "Produzione Prodotto 3" a colonna 1

        # Sezione gruppo "Tempo di produzione totale" - Colonna 1
        groupBoxTempoTotale = QGroupBox("Tempo di produzione totale") # Creazione gruppo "Tempo di produzione totale"
        self.testoTempoProduzioneTotale = QLineEdit() # Creazione casella di testo "Tempo di produzione totale"
        self.testoTempoProduzioneTotale.setReadOnly(True) # Set casella di testo "Tempo di produzione totale" in sola lettura
        groupBoxTempoTotaleLayout = QVBoxLayout() # Creazione layout verticale per gruppo "Tempo di produzione totale"
        groupBoxTempoTotaleLayout.addWidget(self.testoTempoProduzioneTotale) # Aggiunta casella di testo "Tempo di produzione totale" al layout del gruppo "Tempo di produzione totale"
        groupBoxTempoTotale.setLayout(groupBoxTempoTotaleLayout) # Imposta il layout del gruppo "Tempo di produzione totale"
        colonna1.addWidget(groupBoxTempoTotale) # Aggiunta gruppo "Tempo di produzione totale" a colonna 1

        colonna2 = QVBoxLayout() # Creazione layout per colonna 2

        # Sezione gruppo "Sezione Capacità giornaliera per reparto" - Colonna 2
        groupBoxCapacitaReparto = QGroupBox("Capacità giornaliera per reparto") # Creazione gruppo "Capacità giornaliera per reparto"
        groupBoxCapacitaRepartoLayout = QVBoxLayout() # Creazione layout verticale per gruppo "Capacità giornaliera per reparto"

        # Sezione tabella "Sezione Capacità giornaliera per reparto"
        self.tabellaCapacitaReparto = QTableWidget()  # Inizializzazione della tabella "Sezione Capacità giornaliera per reparto"
        self.tabellaCapacitaReparto.setRowCount(5)  # Impostazione numero di righe
        self.tabellaCapacitaReparto.setColumnCount(3)  # Impostazione numero di colonne
        self.tabellaCapacitaReparto.setHorizontalHeaderLabels(["P1", "P2", "P3"])  # Aggiunta etichetta a colonne tabella
        self.tabellaCapacitaReparto.setVerticalHeaderLabels(
            ["Stampaggio", "Piegatura", "Trattamento Superficiale", "Assemblaggio",
             "Confezionamento"])  # Aggiunta etichetta a righe tabella
        self.tabellaCapacitaReparto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Impostazione dimensioni colonne per spazio uniformemente

        # Cicli annidati per popolare righe e colonne della tabella con widget di tipo QLineEdit
        for row in range(self.tabellaCapacitaReparto.rowCount()): # Ciclo sulle righe
            for col in range(self.tabellaCapacitaReparto.columnCount()): #Ciclo sulle colonne
                lineEdit = QLineEdit() # Creazione di un nuovo widget QLineEdit
                lineEdit.setReadOnly(True) # Set del widget QLineEdit in sola lettura
                self.tabellaCapacitaReparto.setCellWidget(row, col, lineEdit) # Inserisco il QLineEdit nella cella corrispondente

        # Aggiunta della tabella al layout del gruppo "Capacità giornaliera per reparto"
        groupBoxCapacitaRepartoLayout.addWidget(self.tabellaCapacitaReparto)

        groupBoxCapacitaReparto.setLayout(groupBoxCapacitaRepartoLayout) # Imposta il layout del gruppo Capacità giornaliera per reparto"
        colonna2.addWidget(groupBoxCapacitaReparto) # Aggiunta gruppo "Capacità giornaliera per reparto" a colonna 2

        layoutDoppiaColonna.addLayout(colonna1) # Aggiunta colonna 1 al layout doppia colonna
        layoutDoppiaColonna.addLayout(colonna2) # Aggiunta colonna 2 al layout doppia colonna

        layoutPrincipale.addLayout(layoutDoppiaColonna) # Aggiunta layout doppia colonna al layout principale

        # Sezione "Pulsanti azione"
        pulsanteGeneraSimulazione = QPushButton("Genera simulazione", self)  # Creazione pulsante "Genera simulazione"
        pulsanteGeneraSimulazione.clicked.connect(self.generaSimulazione) # Collegamento azione pulsante "Genera simulazione" alla funzione "generaSimulazione"
        pulsanteEsci = QPushButton("Esci", self) # Creazione pulsante "Esci"
        pulsanteEsci.clicked.connect(self.close)  # Collegamento azione pulsante "Esci" alla funzione di chiusura della finestra
        layoutPrincipale.addWidget(pulsanteGeneraSimulazione)  # Aggiunta pulsante "Genera simulazione" al layout principale
        layoutPrincipale.addWidget(pulsanteEsci) # Aggiunta pulsante "Esci" al layout principale

        self.setLayout(layoutPrincipale) # Imposto il layout principale come layout della finestra
        self.show() # Mostra la finestra

    # Funzione per generare i dati della simulazione
    def generaSimulazione(self):
        
        # Chiamo la funzione "simulate" passando lo stato dei checkbox per attivare o disattivare i parametri
        risultati = simulate(
            self.checkboxPercentualeProdottiFallati.isChecked(), # Verifica il checkbox "Percentuale prodotti fallati"
            self.checkboxPercentualeProdottiPrelevati.isChecked(), # Verifica il checkbox "Prodotti prelevati controllo qualità"
            self.checkboxProbabilitaGuasti.isChecked(), # Verifica il checkbox "Probabilità guasti"
            self.checkboxTempoDiSettaggio.isChecked() # Verifica il checkbox "Tempi di settaggio"
        ) # Raccolgo i risulati della funzione "simulate" nella dizionario "risultati"

        # Aggiorno casella di testo "Percentuale prodotti fallati" con i risultati della generazione, se la checkbox corrispondente è attiva
        self.testoPercentualeProdottiFallati.setText(
            f"{risultati['percentualeProdottiFallati']}%" if self.checkboxPercentualeProdottiFallati.isChecked() else "Non attivo")

        # Aggiorno casella di testo "Percentuale prodotti prelevati" con i risultati della generazione, se la checkbox corrispondente è attiva
        self.testoPercentualeProdottiPrelevati.setText(
            f"{risultati['percentualeProdottiPrelevati']}%" if self.checkboxPercentualeProdottiPrelevati.isChecked() else "Non attivo")

        # Aggiorno casella di testo "Probabilità guasti" con i risultati della generazione, se la checkbox corrispondente è attiva
        self.testoProbabilitaGuasti.setText(
            f"1 ogni {risultati['probabilitaGuasti']} giorni" if self.checkboxProbabilitaGuasti.isChecked() else "Non attivo")

        # Aggiorno casella di testo "Tempi di settaggio" con i risultati della generazione, se la checkbox corrispondente è attiva
        self.testoTempoDiSettaggio.setText(
            f"{risultati['tempoDiSettaggio']} minuti" if self.checkboxTempoDiSettaggio.isChecked() else "Non attivo")

        # Aggiorno casella di testo "Tempo risoluzione guasto" con i risultati della generazione
        self.testoTempoRisoluzioneGuasto.setText(f"{risultati['tempoRisoluzioneGuasto']} minuti")

        # Aggiorno casella di testo "Lotto" con i risultati della generazione
        self.testoLotto.setText(risultati['nomeLotto'])

        # Aggiorno casella di testo "Produzione prodotto 1" con i risultati della generazione
        self.testoProduzioneProdotto1.setText(f"{risultati['produzioneProdotto1']} pezzi")

        # Aggiorno casella di testo "Produzione prodotto 2" con i risultati della generazione
        self.testoProduzioneProdotto2.setText(f"{risultati['produzioneProdotto2']} pezzi")

        # Aggiorno casella di testo "Produzione prodotto 3" con i risultati della generazione
        self.testoProduzioneProdotto3.setText(f"{risultati['produzioneProdotto3']} pezzi")

        # Aggiorno casella di testo "Tempo di produzione prodotto 1" con i risultati della generazione
        self.testoTempoDiProduzioneProdotto1.setText(f"{risultati['tempoDiProduzioneProdotto1']} minuti")

        # Aggiorno casella di testo "Tempo di produzione prodotto 2" con i risultati della generazione
        self.testoTempoDiProduzioneProdotto2.setText(f"{risultati['tempoDiProduzioneProdotto2']} minuti")

        # Aggiorno casella di testo "Tempo di produzione prodotto 3" con i risultati della generazione
        self.testoTempoDiProduzioneProdotto3.setText(f"{risultati['tempoDiProduzioneProdotto3']} minuti")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Stampaggio" e "Prodotto "1"
        self.lineEditStampaggioProdotto1 = self.tabellaCapacitaReparto.cellWidget(0, 0)
        self.lineEditStampaggioProdotto1.setText(f"{risultati['capacitaGiornalieraRepartoStampaggioProdotto1']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Piegatura" e "Prodotto "1"
        self.lineEditStampaggioProdotto1 = self.tabellaCapacitaReparto.cellWidget(1, 0)
        self.lineEditStampaggioProdotto1.setText(f"{risultati['capacitaGiornalieraRepartoPiegaturaProdotto1']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Trattamento Superficiale" e "Prodotto "1"
        self.lineEditStampaggioProdotto1 = self.tabellaCapacitaReparto.cellWidget(2, 0)
        self.lineEditStampaggioProdotto1.setText(f"{risultati['capacitaGiornalieraRepartoTrattamentoSuperficialeProdotto1']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Assemblaggio" e "Prodotto "1"
        self.lineEditStampaggioProdotto1 = self.tabellaCapacitaReparto.cellWidget(3, 0)
        self.lineEditStampaggioProdotto1.setText(f"{risultati['capacitaGiornalieraRepartoAssemblaggioProdotto1']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Confezionamento" e "Prodotto "1"
        self.lineEditStampaggioProdotto1 = self.tabellaCapacitaReparto.cellWidget(4, 0)
        self.lineEditStampaggioProdotto1.setText(f"{risultati['capacitaGiornalieraRepartoConfezionamentoProdotto1']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Stampaggio" e "Prodotto "2"
        self.lineEditStampaggioProdotto2 = self.tabellaCapacitaReparto.cellWidget(0, 1)
        self.lineEditStampaggioProdotto2.setText(f"{risultati['capacitaGiornalieraRepartoStampaggioProdotto2']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Piegatura" e "Prodotto "1"
        self.lineEditStampaggioProdotto2 = self.tabellaCapacitaReparto.cellWidget(1, 1) 
        self.lineEditStampaggioProdotto2.setText(f"{risultati['capacitaGiornalieraRepartoPiegaturaProdotto2']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Trattamento Superficiale" e "Prodotto "2"
        self.lineEditStampaggioProdotto2 = self.tabellaCapacitaReparto.cellWidget(2, 1)
        self.lineEditStampaggioProdotto2.setText(f"{risultati['capacitaGiornalieraRepartoTrattamentoSuperficialeProdotto2']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Assemblaggio" e "Prodotto "2"
        self.lineEditStampaggioProdotto2 = self.tabellaCapacitaReparto.cellWidget(3, 1)
        self.lineEditStampaggioProdotto2.setText(f"{risultati['capacitaGiornalieraRepartoAssemblaggioProdotto2']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Confezionamento" e "Prodotto "2"
        self.lineEditStampaggioProdotto2 = self.tabellaCapacitaReparto.cellWidget(4, 1)
        self.lineEditStampaggioProdotto2.setText(f"{risultati['capacitaGiornalieraRepartoConfezionamentoProdotto2']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Stampaggio" e "Prodotto "3"
        self.lineEditStampaggioProdotto3 = self.tabellaCapacitaReparto.cellWidget(0, 2)
        self.lineEditStampaggioProdotto3.setText(f"{risultati['capacitaGiornalieraRepartoStampaggioProdotto3']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Piegatura" e "Prodotto "3"
        self.lineEditStampaggioProdotto3 = self.tabellaCapacitaReparto.cellWidget(1, 2)
        self.lineEditStampaggioProdotto3.setText(f"{risultati['capacitaGiornalieraRepartoPiegaturaProdotto3']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Trattamento Superficiale" e "Prodotto "3"
        self.lineEditStampaggioProdotto3 = self.tabellaCapacitaReparto.cellWidget(2, 2)
        self.lineEditStampaggioProdotto3.setText(f"{risultati['capacitaGiornalieraRepartoTrattamentoSuperficialeProdotto3']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Assemblaggio" e "Prodotto "3"
        self.lineEditStampaggioProdotto3 = self.tabellaCapacitaReparto.cellWidget(3, 2)
        self.lineEditStampaggioProdotto3.setText(f"{risultati['capacitaGiornalieraRepartoAssemblaggioProdotto3']}")

        # Aggiorno tabella "Capacità giornaliera reparto", cella corrispondente a reparto "Confezionamento" e "Prodotto "3"
        self.lineEditStampaggioProdotto3 = self.tabellaCapacitaReparto.cellWidget(4, 2)
        self.lineEditStampaggioProdotto3.setText(f"{risultati['capacitaGiornalieraRepartoConfezionamentoProdotto3']}")

        # Sezione per la gestione della visualizzazione del tempo complessivo di produzione
        tempoMinuti = int(risultati['tempoProduzioneTotale']) # Assegno alla variabile i minuti totali di produzione come da generazione
        giorni = tempoMinuti // (24 * 60) # Calcolo dei giorni di produzione dell'intero lotto
        oreRestanti = (tempoMinuti % (24 * 60)) // 60 # Calcolo delle ore di produzione rimanenti
        minutiRestanti = tempoMinuti % 60 # Calcolo dei minuti di produzione rimanenti
        self.testoTempoProduzioneTotale.setText(
            f"{giorni} giorni {oreRestanti} ore e {minutiRestanti} minuti"
            if giorni > 0
            else f"{oreRestanti} ore e {minutiRestanti} minuti"
        ) # Aggiorno casella di testo "Tempo di produzione totale" con i valori calcolati

    # Gestione del posizionamento della finestra nello schermo
    def center(self):
        geometriaFinestra = self.frameGeometry() # Ottengo lo spazio utilizzato attualmente della finestra
        centroSchermo = QDesktopWidget().availableGeometry().center() # Ottengo lo spazio disponibile sullo schermo
        geometriaFinestra.moveCenter(centroSchermo) # Sposto il centro della geometria della finestra al centro dello schermo
        self.move(geometriaFinestra.topLeft()) # Sposto la finestra alla posizione calcolata

# Funzione per avviare la gui
def gui():
    app = QApplication(sys.argv) # Creo un'istanza dell'applicazione passando gli argomenti
    ex = Gui() # Creo un'istanza della classe Gui
    sys.exit(app.exec_()) # Avvio il ciclo degli eventi dell'applicazione
