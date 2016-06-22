#Calculator v0.4
#Yarislav Povolotsky
#2016
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from math import sqrt

#Глобальные переменные
num = 0.0
newNum = 0.0
sumAll = 0.0

operator = ""
opVar = False
sumIt = 0

#Класс для графической/вычислительной части приложения
class ViewOfCalculator(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
    def initUI(self):

        self.line = QtGui.QLineEdit(self)
        self.line.move(20, 10)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)

        self.line.resize(230, 60)

        zero = QtGui.QPushButton("0", self)
        zero.move(20, 360)
        zero.resize(70, 60)

        one = QtGui.QPushButton("1", self)
        one.move(20, 290)
        one.resize(70, 60)

        two = QtGui.QPushButton("2", self)
        two.move(100, 290)
        two.resize(70, 60)

        three = QtGui.QPushButton("3", self)
        three.move(180, 290)
        three.resize(70, 60)

        four = QtGui.QPushButton("4", self)
        four.move(20, 220)
        four.resize(70, 60)

        five = QtGui.QPushButton("5", self)
        five.move(100, 220)
        five.resize(70, 60)

        six = QtGui.QPushButton("6", self)
        six.move(180, 220)
        six.resize(70, 60)

        seven = QtGui.QPushButton("7", self)
        seven.move(20, 150)
        seven.resize(70, 60)

        eight = QtGui.QPushButton("8", self)
        eight.move(100, 150)
        eight.resize(70, 60)

        nine = QtGui.QPushButton("9", self)
        nine.move(180, 150)
        nine.resize(70, 60)

        div = QtGui.QPushButton("/", self)
        div.move(260, 150)
        div.resize(70, 60)

        mult = QtGui.QPushButton("*", self)
        mult.move(260, 220)
        mult.resize(70, 60)

        minus = QtGui.QPushButton("-", self)
        minus.move(260, 290)
        minus.resize(70, 60)

        plus = QtGui.QPushButton("+", self)
        plus.move(260, 80)
        plus.resize(70, 60)

        sqrt = QtGui.QPushButton("√", self)
        sqrt.move(180, 80)
        sqrt.resize(70, 60)
        sqrt.clicked.connect(self.OnSqrtButtonClick)


        squared = QtGui.QPushButton("x²", self)
        squared.move(100, 80)
        squared.resize(70, 60)
        squared.clicked.connect(self.OnSquaredButtonClick)

        equal = QtGui.QPushButton("=", self)
        equal.move(260, 360)
        equal.resize(70, 60)


        c = QtGui.QPushButton("C", self)
        c.move(20, 80)
        c.resize(70, 60)
        c.clicked.connect(self.OnCButtonClick)

        back = QtGui.QPushButton("Back", self)
        back.move(260, 10)
        back.resize(70, 60)
        back.clicked.connect(self.OnBackButtonClick)

        switch = QtGui.QPushButton("+/-", self)
        switch.move(100, 360)
        switch.resize(70, 60)
        switch.clicked.connect(self.OnSwitchButtonClick)

        point = QtGui.QPushButton(".", self)
        point.move(180, 360)
        point.resize(70, 60)
        point.clicked.connect(self.OnPointClickedButtonClick)

# Определение типа кнопки
        nums = [zero, one, two, three, four, five, six, seven, eight, nine]

        ops = [back, c, div, mult, minus, plus, equal]

        rest = [switch, squared, sqrt, point]

        for i in nums:
            i.setStyleSheet("color:blue;")
            i.clicked.connect(self.Nums)

        for i in ops:
            i.setStyleSheet("color:red;")

        for i in ops[2:7]:
            i.clicked.connect(self.Operator)

        self.setGeometry(300, 300, 350, 440)
        self.setFixedSize(350, 440)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon("calc.jpg"))
        self.show()

    def Nums(self):
        global num
        global newNum
        global opVar

        sender = self.sender()

        newNum = int(sender.text())
        setNum = str(newNum)

        if opVar == False:
            self.line.setText(self.line.text() + setNum)


        else:
            self.line.setText(setNum)
            opVar = False

    def Operator(self):
        global num
        global opVar
        global operator
        global sumIt

        sumIt += 1

        if sumIt > 1:
            self.Equal()

        num = self.line.text()

        sender = self.sender()

        operator = sender.text()

        opVar = True

    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar
        global sumIt

        sumIt = 0

        newNum = self.line.text()

        print(num)
        print(newNum)
        print(operator)

        if operator == "+":
            sumAll = CalculatingPart.Plus(num,newNum)

        elif operator == "-":
            sumAll = CalculatingPart.Minus(num,newNum)

        elif operator == "/":
            sumAll = CalculatingPart.Del(num,newNum)

        elif operator == "*":
            sumAll = CalculatingPart.Umn(num,newNum)

        print(sumAll)
        self.line.setText(str(sumAll))
        opVar = True


    def OnBackButtonClick(self):
        self.line.backspace()

    def OnCButtonClick(self):
        self.line.setText(CalculatingPart.C(num))

    def OnPointClickedButtonClick(self):
        global opVar

        if "." not in self.line.text():
            self.line.setText(self.line.text() + CalculatingPart.PointClicked(num))

    def OnSwitchButtonClick(self):
        global num

        try:
           num = int(self.line.text())

        except:
           num = float(self.line.text())

        self.line.setText((str(CalculatingPart.Switch(num))))

    def OnSquaredButtonClick(self):
        global num
        num = float(self.line.text())
        self.line.setText(str(CalculatingPart.Squared(num)))

    def OnSqrtButtonClick(self):
        global num
        num = float(self.line.text())
        self.line.setText(str(CalculatingPart.Sqrt(num)))

class CalculatingPart():

    def Plus(num, newNum):
        return float(num) + float(newNum)

    def Minus(num, newNum):
        return float(num) - float(newNum)

    def Del(num, newNum):
        return float(num) / float(newNum)

    def Umn(num, newNum):
        return float(num) * float(newNum)

    def Squared(num):
        return num ** 2

    def Sqrt(num):
        return sqrt(num)

    def Switch(num):
        return num - num * 2

    def PointClicked(num):
        return "."

    def C(num):
        return " "


def main():
    app = QtGui.QApplication(sys.argv)
    main= ViewOfCalculator()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
