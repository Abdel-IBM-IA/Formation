from collections import defaultdict

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime


class VueDetail(QtWidgets.QMainWindow):
    filepath = "producteurs.txt"
    dicoList = {}
    lstViticulteur = {}
    lstCepage = {'Pinot noir': 1, 'Merlot': 2, 'Malbec': 3, 'Trousseau': 4, 'Gamay': 5, 'Chardonnay': 6,
                 'Sauvignon': 7, 'Grenache': 8, 'Savagnin': 9, 'Chenin': 10}

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('VueDetail.ui', self)
        self.btnRetour.clicked.connect(self.retour)
        self.btnAjouter.clicked.connect(self.ajouterLivraison)
        self.importDataFromFile()
        self.importViticulteur()
        for val in self.lstViticulteur:
            self.comboBoxViticulteur.addItem(str(val[0]))
        # La sélection dun viticulteur lance la requête pour recupérer sa liste de parcelle
        self.comboBoxViticulteur.currentIndexChanged.connect(self.importLstParcelle)
        # La sélection d'une parcelle permet de recupérer la liste de cepage correspondante
        self.comboBoxParcelle.currentIndexChanged.connect(self.importLstCepage)

    def importViticulteur(self):
        self.lstViticulteur = sorted(self.dicoList.items())

    def importLstParcelle(self):
        lst = []
        self.comboBoxParcelle.clear()
        viticulteur = self.comboBoxViticulteur.currentText()
        dataViticulteur = self.dicoList[viticulteur]
        for val in dataViticulteur:
            for x in val:
                lst = x
            self.comboBoxParcelle.addItem(str(lst[0]))

    def importLstCepage(self):
        self.comboBoxCepage.clear()
        viticulteur = self.comboBoxViticulteur.currentText()
        parcelleSelected = self.comboBoxParcelle.currentText()
        tuplesViticulteur = self.dicoList[viticulteur]
        for tupleData in tuplesViticulteur:
            for x in tupleData:
                lst = x
                if str(lst[0]) == parcelleSelected:
                    lstnumcepage = lst[1].replace(' ', '')
                    lstnumcepage = lstnumcepage.split(',')
                    for num in lstnumcepage:
                        for nom, nb in self.lstCepage.items():
                            if int(num) == int(nb):
                                self.comboBoxCepage.addItem(str(nom))

    def importDataFromFile(self):
        """ Importe la liste des viticulteurs et de leurs parcelles respectives depuis la liste des livraisons """
        filepath = "producteurs.txt"

        dicoList = defaultdict(list)
        # Utiliser pour le regroupement d'une séquence de paires clé-valeur en un dictionnaire de listes
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                line = fp.readline()
                if len(line) > 0:
                    ligneImport = line.split(";")
                    # Suppression du retour à la ligne présent en fin de chaque ligne du fichier
                    ligneImport[len(ligneImport) - 1] = ligneImport[len(ligneImport) - 1].replace('\n', '')
                    variabl = {(ligneImport[1], ligneImport[2])}
                    dicoList[str(ligneImport[0])].append(variabl)
        self.dicoList = dicoList

    def retour(self):
        self.parent().show()
        self.parent().afficherDataOnQtable()
        self.close()

    def ajouterLivraison(self):
        """ Recupere la saisie de l'utilisateur dans le formulaire 
        Ajoute l'enregistrement dans une collection"""
        detailLivraison = []

        viticulteur = self.comboBoxViticulteur.currentText()
        detailLivraison.append(viticulteur)

        parcelle = self.comboBoxParcelle.currentText()
        detailLivraison.append(parcelle)

        cepage = self.comboBoxCepage.currentText()
        detailLivraison.append(cepage)

        poids = self.spinBoxPoids.value()
        detailLivraison.append(poids)

        now = QDate.currentDate()
        date = now.toString('d.M.yy')
        detailLivraison.append(str(date))

        time = QTime.currentTime()
        heure = time.toString('h.m.s')
        detailLivraison.append(heure)

        # Met à jour la collection
        self.parent().MaTable.append(detailLivraison)

        # Met à jour la Qtable
        self.parent().afficherDataOnQtable()
