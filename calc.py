import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from math import sqrt


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('calc.ui', self)
        self.setWindowTitle('Калькулятор')
        self.table.setDigitCount(13)

        self.stroka = ''
        self.itog = ''
        self.numbers_probels = ''

        self.flag = False
        self.flag2 = False
        self.flag3 = False
        self.flag4 = False
        self.flag5 = False
        self.flag6 = False
        self.flag7 = False

        self.btn0.clicked.connect(lambda: self.output_of_numbers('0'))
        self.btn1.clicked.connect(lambda: self.output_of_numbers('1'))
        self.btn2.clicked.connect(lambda: self.output_of_numbers('2'))
        self.btn3.clicked.connect(lambda: self.output_of_numbers('3'))
        self.btn4.clicked.connect(lambda: self.output_of_numbers('4'))
        self.btn5.clicked.connect(lambda: self.output_of_numbers('5'))
        self.btn6.clicked.connect(lambda: self.output_of_numbers('6'))
        self.btn7.clicked.connect(lambda: self.output_of_numbers('7'))
        self.btn8.clicked.connect(lambda: self.output_of_numbers('8'))
        self.btn9.clicked.connect(lambda: self.output_of_numbers('9'))

        self.btn_plus.clicked.connect(lambda: self.operation_sign())
        self.btn_minus.clicked.connect(lambda: self.operation_sign())
        self.btn_mult.clicked.connect(lambda: self.operation_sign())
        self.btn_div.clicked.connect(lambda: self.operation_sign())

        self.btn_clear.clicked.connect(lambda: self.clear())
        self.btn_comma.clicked.connect(lambda: self.comma())
        self.btn_eq.clicked.connect(lambda: self.eq())
        self.btn_pow.clicked.connect(lambda: self.pow())
        self.btn_percent.clicked.connect(lambda: self.percent())
        self.btn_sqrt.clicked.connect(lambda: self.sqrt())

    def output_of_numbers(self, number):
        try:
            self.stroka += number
            if self.stroka[0] == '0' and not self.flag3:
                self.stroka = '0'

            if len(self.stroka) > 10:
                self.stroka, self.numbers_probels, self.itog = '', '', ''
                self.table.display('Error')

            self.count = 1
            self.beautiful_number()

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def beautiful_number(self):
        try:
            if '.' in self.stroka and not self.flag2 and not self.flag4 and not self.flag7:
                self.c = self.stroka[self.stroka.index('.') + self.count:]
                self.numbers_probels += self.c[-1]
                self.count += 1
                self.table.display(self.numbers_probels)
                print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')

            else:
                if (self.flag2 and not self.flag6) or self.flag7:
                    if 'e-' not in self.stroka:
                        self.s = self.stroka[self.stroka.index('.'):]
                        self.stroka = self.stroka[:self.stroka.index('.')]
                        self.res = [''.join(self.stroka[::-1][i:i + 3])[::-1] for i in range(0, len(self.stroka), 3)]
                        self.numbers_probels = str(' '.join(self.res[::-1])) + self.s
                        self.stroka += self.s
                        print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                        self.table.display(self.numbers_probels)
                        self.flag2 = False
                        self.flag7 = False

                    else:
                        self.table.display(self.stroka)
                        self.numbers_probels = self.stroka

                else:
                    self.res = [''.join(self.stroka[::-1][i:i + 3])[::-1] for i in range(0, len(self.stroka), 3)]
                    self.numbers_probels = str(' '.join(self.res[::-1]))
                    self.table.display(self.numbers_probels)
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.flag4 = False
                    self.flag6 = False

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def clear(self):
        try:
            self.stroka = ''
            self.numbers_probels = ''
            self.itog = ''
            self.table.display('0')
            self.flag = False
            self.flag6 = True
            print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def comma(self):
        try:
            self.numbers_probels += '.'
            self.stroka += '.'
            self.table.display(self.numbers_probels)
            self.flag3 = True

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def operation_sign(self):
        try:
            self.znak = self.sender().text()
            if self.znak == '×':
                self.znak = '*'

            elif self.znak == '÷':
                self.znak = '/'

            if self.flag and not self.flag2 and not self.flag7:
                self.stroka = ''
                self.numbers_probels = ''
                self.itog += self.znak
            else:
                self.stroka += self.znak
                self.numbers_probels = ''
                self.itog = self.stroka
                self.stroka = ''

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def pow(self):
        try:
            if self.flag:
                self.itog = self.itog[:-1].replace(' ', '')
                self.stroka = self.itog.replace(' ', '')
                self.flag4 = True
                self.beautiful_number()
            else:
                self.stroka = self.stroka[:-1]
                self.numbers_probels = self.numbers_probels[:-1]
                print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                self.flag4 = True
                self.beautiful_number()

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def percent(self):
        try:
            if self.itog == '':
                if '.' in self.stroka and not self.flag5:
                    self.stroka = str(float(self.stroka.replace(' ', '')) / 100)
                    self.numbers_probels = self.stroka
                    self.flag2 = True
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.beautiful_number()
                else:
                    self.stroka = str(float(self.stroka.replace(' ', '')) / 100)
                    self.numbers_probels = self.stroka
                    self.flag2 = True
                    self.flag5 = True
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.beautiful_number()

            else:
                if '.' in self.itog and not self.flag5:
                    self.stroka = str(float(self.itog.replace(' ', '')) / 100)
                    self.numbers_probels = self.itog
                    self.itog = self.stroka
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.flag2 = True
                    self.beautiful_number()
                else:
                    self.stroka = str(float(self.itog.replace(' ', '')) / 100)
                    self.numbers_probels = self.stroka
                    self.itog = self.stroka
                    self.flag2 = True
                    self.flag5 = True
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.beautiful_number()

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def sqrt(self):
        try:
            if self.itog == '':
                if '.' in self.stroka:
                    self.stroka = str(sqrt(int(self.stroka[:self.stroka.index('.')])))
                    self.stroka = self.stroka[:self.stroka.index('.') + 3]
                    self.numbers_probels = self.stroka[:-1]
                    self.flag7 = True
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.beautiful_number()
                else:
                    self.stroka = str(sqrt(int(self.stroka)))
                    self.stroka = self.stroka[:self.stroka.index('.') + 3]
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.numbers_probels = self.stroka[:-1]
                    self.flag7 = True
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.beautiful_number()

            else:
                if '.' in self.itog:
                    self.stroka = str(sqrt(int(self.itog.replace(' ', '')[:self.itog.index('.')])))
                    self.stroka = self.stroka[:self.stroka.index('.') + 4]
                    self.numbers_probels = self.stroka[:-1]
                    self.itog = self.stroka
                    self.flag7 = True
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.beautiful_number()
                else:
                    self.stroka = str(sqrt(int(self.itog.replace(' ', ''))))
                    self.stroka = self.stroka[:self.stroka.index('.') + 4]
                    self.numbers_probels = self.stroka[:-1]
                    self.itog = self.stroka
                    self.flag7 = True
                    print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                    self.beautiful_number()

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def eq(self):
        try:
            if ('+' or '-' or '*' or '/') in self.stroka or self.itog:
                self.itog += self.stroka
                self.itog = self.itog.replace(' ', '')
                self.itog = str(eval(self.itog))
                print('Итог посчитан', self.itog)

                if '.' in self.itog:
                    self.a = self.itog.index('.')
                    self.it = self.itog.split('.')[1]
                    self.itog = self.itog.split('.')[0]
                    self.result = [''.join(self.itog[::-1][i:i + 3])[::-1] for i in range(0, len(self.itog), 3)]
                    self.itog = (str(' '.join(self.result[::-1])) + '.' + self.it[:3])[:self.a + 3]

                    if len(self.itog) <= 10:
                        if self.itog[-1] == '0':
                            self.itog = self.itog[:-1]
                            self.table.display(self.itog)
                        else:
                            self.table.display(self.itog)
                    else:
                        self.stroka, self.numbers_probels, self.itog = '', '', ''
                        self.table.display('Error')

                else:
                    self.result = [''.join(self.itog[::-1][i:i + 3])[::-1] for i in range(0, len(self.itog), 3)]
                    self.itog = str(' '.join(self.result[::-1]))

                    if len(self.itog) <= 10:
                        self.table.display(self.itog)
                    else:
                        self.stroka, self.numbers_probels, self.itog = '', '', ''
                        self.table.display('Error')

                self.flag = True
                print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')

            else:
                self.stroka, self.numbers_probels, self.itog = '', '', ''
                self.table.display('Error')

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Calculator()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
