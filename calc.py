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
        self.znak = ''

        self.flag = False
        self.flag2 = False
        self.flag3 = False
        self.flag4 = False
        self.flag5 = False
        self.flag6 = False
        self.flag7 = False
        self.flag8 = False
        self.flag9 = False

        for n in range(0, 10):
            getattr(self, 'btn%s' % n).pressed.connect(lambda number=n: self.output_of_numbers(str(number)))

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
            if not self.flag:
                self.stroka += number
                if self.stroka[0] == '0' and not self.flag3:
                    self.stroka = ''
                    self.flag9 = True

                if len(self.stroka) > 12:
                    self.stroka, self.numbers_probels, self.itog = '', '', ''
                    self.table.display('Error')
                else:
                    self.count = 1
                    self.beautiful_number()

            else:
                self.itog += number
                self.numbers_probels = self.itog
                self.stroka = self.itog.replace(' ', '')
                if len(self.itog) > 12:
                    self.stroka, self.numbers_probels, self.itog = '', '', ''
                    self.table.display('Error')
                else:
                    self.count = 1
                    self.flag8 = True
                    self.beautiful_number()

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def beautiful_number(self):
        try:
            if '.' in self.stroka and not self.flag2 and not self.flag4 and not self.flag7 and not self.flag8:
                c = self.stroka[self.stroka.index('.') + self.count:]
                self.numbers_probels += c[-1]
                self.count += 1
                self.table.display(self.numbers_probels)

            else:
                if (self.flag2 and not self.flag6) or self.flag7:
                    if 'e-' not in self.stroka:
                        if self.numbers_probels[-1] == '0':
                            while self.numbers_probels[-1] == '0' or self.numbers_probels[-1] == '.':
                                self.numbers_probels = self.numbers_probels[:-1]
                                if self.numbers_probels[-1] == '.':
                                    self.numbers_probels = self.numbers_probels[:-1]
                                    break
                            self.stroka = self.numbers_probels.replace(' ', '')

                        if '.' in self.stroka:
                            s = self.stroka[self.stroka.index('.'):]
                            self.stroka = self.stroka[:self.stroka.index('.')]
                            self.res = [''.join(self.stroka[::-1][i:i + 3])[::-1] for i in
                                        range(0, len(self.stroka), 3)]
                            self.numbers_probels = str(' '.join(self.res[::-1])) + s
                        else:
                            self.res = [''.join(self.stroka[::-1][i:i + 3])[::-1] for i in
                                        range(0, len(self.stroka), 3)]
                            self.numbers_probels = str(' '.join(self.res[::-1]))

                        self.stroka = self.numbers_probels.replace(' ', '')
                        self.table.display(self.numbers_probels)
                        self.flag2 = False
                        self.flag7 = False

                    else:
                        self.table.display(self.stroka)
                        self.numbers_probels = self.stroka
                        self.flag2 = False

                elif self.flag4:
                    if self.flag:
                        if '.' in self.itog:
                            s = self.itog[self.itog.index('.'):]
                            self.itog = self.itog[:self.itog.index('.')]
                            res = [''.join(self.itog[::-1][i:i + 3])[::-1] for i in
                                   range(0, len(self.itog), 3)]
                            self.numbers_probels = str(' '.join(res[::-1])) + s
                            self.table.display(self.numbers_probels)
                        else:
                            if self.stroka == '' and self.numbers_probels == '' and self.itog == '':
                                self.table.display('0')
                                self.flag = False
                            else:
                                res = [''.join(self.itog[::-1][i:i + 3])[::-1] for i in
                                       range(0, len(self.itog), 3)]
                                self.numbers_probels = str(' '.join(res[::-1]))
                                self.table.display(self.numbers_probels)

                        self.itog = self.numbers_probels
                        self.flag4 = False

                    else:
                        if '.' in self.stroka:
                            s = self.stroka[self.stroka.index('.'):]
                            self.stroka = self.stroka[:self.stroka.index('.')]
                            res = [''.join(self.stroka[::-1][i:i + 3])[::-1] for i in
                                   range(0, len(self.stroka), 3)]
                            self.numbers_probels = str(' '.join(res[::-1])) + s
                            self.stroka += s
                            self.table.display(self.numbers_probels)
                        else:
                            if self.stroka == '' and self.numbers_probels == '' and self.itog == '':
                                self.table.display('0')
                                self.flag = False
                            else:
                                res = [''.join(self.stroka[::-1][i:i + 3])[::-1] for i in
                                       range(0, len(self.stroka), 3)]
                                self.numbers_probels = str(' '.join(res[::-1]))
                                self.table.display(self.numbers_probels)
                        self.flag4 = False

                elif self.flag8 and ('+' not in self.itog) and ('-' not in self.itog) and ('*' not in self.itog) and (
                        '/' not in self.itog):
                    if '.' not in self.itog:
                        self.itog = self.itog.replace(' ', '')
                        res = [''.join(self.itog[::-1][i:i + 3])[::-1] for i in range(0, len(self.itog), 3)]
                        self.numbers_probels = str(' '.join(res[::-1]))
                        self.stroka = self.numbers_probels.replace(' ', '')
                        self.itog = self.numbers_probels
                    else:
                        s = self.itog[self.itog.index('.'):]
                        self.itog = self.itog[:self.itog.index('.')]
                        res = [''.join(self.itog[::-1][i:i + 3])[::-1] for i in range(0, len(self.itog), 3)]
                        self.numbers_probels = str(''.join(res[::-1])) + s
                        self.itog += s

                    self.table.display(self.numbers_probels)
                    self.flag8 = False

                elif self.flag9:
                    self.table.display('0')
                    self.flag9 = False

                else:
                    res = [''.join(self.stroka[::-1][i:i + 3])[::-1] for i in range(0, len(self.stroka), 3)]
                    self.numbers_probels = str(' '.join(res[::-1]))
                    self.table.display(self.numbers_probels)
                    self.flag4 = False
                    self.flag6 = False
                    self.flag8 = False
            print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')

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
            self.flag2 = False
            self.flag3 = False
            self.flag6 = True
            self.flag7 = False
            print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def comma(self):
        try:
            if not self.flag:
                if '.' not in self.stroka:
                    self.numbers_probels += '.'
                    self.stroka += '.'
                    if self.stroka[0] == '.':
                        self.stroka = '0.'
                        self.numbers_probels = '0.'
                    self.table.display(self.numbers_probels)
                    self.flag3 = True
                else:
                    self.stroka, self.numbers_probels, self.itog = '', '', ''
                    self.table.display('Error')
            else:
                if '.' not in self.itog:
                    self.itog += '.'
                    self.numbers_probels = self.itog
                    self.table.display(self.itog)
                    self.flag3 = True
                else:
                    self.stroka, self.numbers_probels, self.itog = '', '', ''
                    self.table.display('Error')
            print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')

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

            if self.stroka == '' and self.numbers_probels == '' and self.itog == '':
                self.table.display('Error')

            else:
                if self.flag and not self.flag2 and not self.flag7:
                    self.stroka = ''
                    self.numbers_probels = ''
                    self.itog += self.znak

                else:
                    self.stroka += self.znak
                    self.numbers_probels = ''
                    self.itog += self.stroka
                    self.stroka = ''
                    self.flag7 = False

            self.flag = False
            print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def pow(self):
        try:
            if self.flag:
                self.itog = self.itog[:-1].replace(' ', '')
                self.stroka = self.itog.replace(' ', '')
                self.numbers_probels = self.stroka
            else:
                self.stroka = self.stroka[:-1].replace(' ', '')
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
                    self.flag2 = True
                else:
                    self.flag2 = True
                    self.flag5 = True

                self.stroka = str(float(self.stroka.replace(' ', '')) / 100)
                self.numbers_probels = self.stroka
                print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
                self.beautiful_number()

            else:
                if '.' in self.itog and not self.flag5:
                    self.flag2 = True
                else:
                    self.flag2 = True
                    self.flag5 = True

                self.stroka = str(float(self.itog.replace(' ', '')) / 100)
                self.numbers_probels = self.stroka
                self.itog = self.stroka
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
                    self.stroka = str(sqrt(float(self.stroka)))
                else:
                    self.stroka = str(sqrt(int(self.stroka)))

            else:
                if '.' in self.itog:
                    self.stroka = str(sqrt(float(self.itog.replace(' ', ''))))
                else:
                    self.stroka = str(sqrt(int(self.itog.replace(' ', ''))))

            self.itog = ''
            self.stroka = self.stroka[:self.stroka.index('.') + 3]
            self.numbers_probels = self.stroka
            self.flag7 = True
            self.flag = False
            print(self.stroka, '||||', self.numbers_probels, '||||', self.itog, '\n')
            self.beautiful_number()

        except Exception as error:
            print('Ошибка:', error)
            self.stroka, self.numbers_probels, self.itog = '', '', ''
            self.table.display('Error')

    def eq(self):
        try:
            if ('+' in (self.itog or self.stroka)) or ('-' in (self.itog or self.stroka)) or (
                    '*' in (self.itog or self.stroka)) or ('/' in (self.itog or self.stroka)):
                self.itog += self.stroka
                self.itog = self.itog.replace(' ', '')
                self.itog = str(eval(self.itog))
                print('Итог посчитан', self.itog)

                if '.' in self.itog:
                    a = self.itog.index('.')
                    self.it = self.itog.split('.')[1]
                    self.itog = self.itog.split('.')[0]
                    self.result = [''.join(self.itog[::-1][i:i + 3])[::-1] for i in range(0, len(self.itog), 3)]

                    self.itog = (str(' '.join(self.result[::-1])) + '.' + self.it[:4])
                    co = self.itog.count(' ')
                    self.itog = self.itog[:co + a + 3]

                    if len(self.itog) <= 13:
                        if self.itog[-1] == '0':
                            self.itog = self.itog[:-1]
                            if self.itog[-1] == '.':
                                self.itog = self.itog[:-1]

                        self.table.display(self.itog)

                    else:
                        self.stroka, self.numbers_probels, self.itog = '', '', ''
                        self.table.display('Error')

                else:
                    result = [''.join(self.itog[::-1][i:i + 3])[::-1] for i in range(0, len(self.itog), 3)]
                    self.itog = str(' '.join(result[::-1]))

                    if len(self.itog) <= 13:
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
