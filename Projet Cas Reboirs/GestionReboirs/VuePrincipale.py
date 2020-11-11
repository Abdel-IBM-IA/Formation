import csv
import json
import sys

from PyQt5 import QtWidgets, uic
from VueDetail import VueDetail


class VuePrincipale(QtWidgets.QMainWindow):
    MaTable = []
    filesav = "SaveLivraison.csv"

    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('VuePrincipale.ui', self)
        self.btnLivraison.clicked.connect(self.openVueDetail)
        self.btnQuitter.clicked.connect(self.closeVue)
        self.btnSauverHistorique.clicked.connect(self.saveDataInFile)
        self.importData()

    def openVueDetail(self):
        self.hide()
        vueDetail = VueDetail(self)
        vueDetail.show()

    def closeVue(self):
        self.close()

    def importData(self):
        """ Importe la liste des livraisons du fichier texte vers une collection """
        with open(self.filesav) as fp:
            line = fp.readline()

            while line:
                line = fp.readline()
                if len(line) > 0:
                    ligneImport = line.split(";")
                    ligneImport[len(ligneImport) - 1] = ligneImport[len(ligneImport) - 1].replace('\n', '')
                    self.MaTable.append(ligneImport)
            self.afficherDataOnQtable()

    def afficherDataOnQtable(self):
        """ Affiche les données de la collection dans la Qtable """
        self.qTblFromArray(self.MaTable, self.tableWidgetEntrees)

    def saveDataInFile(self):
        """ Sauvegarde la liste des livraisons de la collection vers le fichier texte """
        with open(self.filesav, 'wt') as file:
            livraisonCSV = csv.writer(file, delimiter=";")
            livraisonCSV.writerows(self.MaTable)
            # for item in self.MaTable :
            # file.write(f'{item}\n')

    @staticmethod
    def qTblFromArray(array, qtable):
        if array is not None:
            nbRow = len(array)
            nbCol = len(array[0])
            qtable.setRowCount(nbRow)
            qtable.setColumnCount(nbCol)
            for i in range(nbRow):
                for j in range(nbCol):
                    item = QtWidgets.QTableWidgetItem(str(array[i][j]))
                    qtable.setItem(i, j, item)
            qtable.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VuePrincipale()
    window.show()
    sys.exit(app.exec_())
