import sys
from PyQt5 import uic, QtWidgets


class MyApp(QtWidgets.QMainWindow) :
    tab_taxes = [20, 5.5]

    def __init__(self) :
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("MyAppDesign.ui", self)
        self.boutonOK.clicked.connect(self.CalculPrixTTC)
        for val in self.tab_taxes:
            self.comboBoxTaxe.addItem(str(val))

    def CalculPrixTTC(self) :
        prix = float(self.textEditPrixHT.toPlainText())
        taxe = float(self.comboBoxTaxe.currentText())
        prixTTC = prix + ((taxe / 100) * prix)
        prixTTC_string = "Le prix total TTC est : " + str(prixTTC)
        self.labelTotalTTC.setText(prixTTC_string)


if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
