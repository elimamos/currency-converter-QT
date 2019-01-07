import sys

from PyQt5 import QtWidgets, uic
import urllib.request
import json

from PyQt5.QtWidgets import QAction, QMainWindow, QApplication

currencies = []


class CurrencyConverter:
    rates = {}

    def __init__(self, url):
        req = urllib.request.Request(url)
        data = urllib.request.urlopen(req).read()
        data = json.loads(data.decode('utf-8'))
        self.rates = data["rates"]
        for key, value in self.rates.items():
            convertFrom.addItem(key)
            convertTo.addItem(key)

    def convert(self, amount, from_currency, to_currency):
        initial_amount = amount

        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]
        if to_currency == "EUR":
            currencyFrom.setText(str("%.2f" % initial_amount))
            rate.setText(str("%.2f" % (self.rates[to_currency] / self.rates[from_currency])))
            currencyTo.setText(str("%.2f" % amount))
        else:
            currencyFrom.setText(str("%.2f" % initial_amount))
            rate.setText(str("%.2f" % (self.rates[to_currency] / self.rates[from_currency])))
            currencyTo.setText(str("%.2f" % (amount * self.rates[to_currency])))


class Info(QMainWindow):
    def __init__(self, parent=None):
        super(Info, self).__init__(parent)
        uic.loadUi("info.ui", self)
        self.exit.clicked.connect(self.close)

    def exit(self):
        self.close()


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("konwerter.ui", self)

        bar = self.menubar

        global rate
        rate = self.rate
        global statusBar
        statusBar = self.statusbar
        global currencyTo
        currencyTo = self.currencyTo
        global currencyFrom
        currencyFrom = self.currencyFrom
        global convertFrom
        convertFrom = self.convertFrom
        global convertTo
        convertTo = self.convertTo
        self.convert.clicked.connect(self.convert_currency)
        global converter
        converter = CurrencyConverter(
            "http://data.fixer.io/api/latest?access_key=46e95190b50ac93546c5222e8e00f1ef&format=1")

        aboutButton = QAction('O PROGRAMIE', self)
        aboutButton.triggered.connect(self.open_info)
        self.window = Info(self)

        #  self.dialog = Info(self)
        bar.addAction(aboutButton)

        self.show()

    def convert_currency(self):
        statusBar.showMessage("")
        currencyTo.setText("")
        input = currencyFrom.text()
        if input is None or input == "":
            statusBar.showMessage("Proszę wprowadzić wartość do przelicznika!")
        else:
            try:
                input = input.strip()
                input = input.replace(",", ".")
                converter.convert(float(input), convertFrom.currentText(), convertTo.currentText())
            except ValueError:
                statusBar.showMessage("Podano niepoprawną wartość do przelicznika!")

    def open_info(self):

        self.window.show()


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
