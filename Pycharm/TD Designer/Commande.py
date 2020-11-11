import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtCore import QTime, Qt

global MaTable
MaTable = []


def qTblFromArray(array, qtable) :
    if array is not None :
        nbRow = len(array)
        nbCol = len(array[0])
        qtable.setRowCount(nbRow)
        qtable.setColumnCount(nbCol)
        for i in range(nbRow) :
            for j in range(nbCol) :
                qtable.setItem(i, j, QtWidgets.QTableWidgetItem(str(array[i][j])))


class Commande(QtWidgets.QMainWindow) :
    liste_produits = {'iPhone x' : 870, 'Galaxy S10' : 765, 'Huawei P30' : 670}
    TotalTTC = 0

    def __init__(self) :
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('Commande.ui', self)
        self.boutonAjouter.clicked.connect(self.AjoutLigneCommande)
        self.boutonTotal.clicked.connect(self.AfficherCommandeTotale)
        self.spinBoxQuantite.valueChanged.connect(self.CalculPrixTTC)
        for val in self.liste_produits :
            self.comboBoxProduits.addItem(str(val))

    def CalculPrixTTC(self) :
        """ Affiche le prix TTC pour une ligne de commande """
        prix = self.liste_produits[self.comboBoxProduits.currentText()]
        quantite = self.spinBoxQuantite.value()
        self.textEditPrixTTC.setText(str(quantite * prix))

    def AjoutLigneCommande(self) :
        """ Genere une ligne de commande et l'ajoute au resume de commande """

        ligneCommande = []
        now = QDate.currentDate()
        date = now.toString('d.M.yy')
        ligneCommande.append(str(date))

        time = QTime.currentTime()
        heure = time.toString('h.m.s')
        ligneCommande.append(heure)

        produit = self.comboBoxProduits.currentText()
        ligneCommande.append(produit)

        quantite = str(self.spinBoxQuantite.value())
        ligneCommande.append(quantite)

        montant = int(self.textEditPrixTTC.toPlainText())
        ligneCommande.append(montant)

        MaTable.append(ligneCommande)
        self.TotalTTC += montant

    def AfficherCommandeTotale(self) :
        self.hide()
        uneCommande = ResumeCommande(self)
        uneCommande.show()


class ResumeCommande(QtWidgets.QMainWindow) :

    def __init__(self, parent=None) :
        super().__init__(parent)
        uic.loadUi('ResumeCommande.ui', self)
        self.boutonRetour.clicked.connect(self.Retour)
        self.boutonQuitter.clicked.connect(self.Quitter)
        qTblFromArray(MaTable, self.tableWidget)
        self.labelValeurTotal.setText(str(parent.TotalTTC))

    def Retour(self) :
        self.parent().show()
        self.close()

    def Quitter(self) :
        self.parent().close()
        self.close()


if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    window = Commande()
    window.show()
    sys.exit(app.exec_())
