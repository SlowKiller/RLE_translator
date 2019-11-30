import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
import welcome


class WorkWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):  # Основное коно для кодирования
    def __init__(self, parent=None):                            # Добавлена возможность наследования
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__(parent)
        self.setupUi(self)                                      # Это нужно для инициализации нашего дизайна
        self.TransBut.clicked.connect(self.text_output)         # Привязываем функцию text_output к кнопке Translate

    def text_output(self):                                      # Выходная функция кодирования
        if self.set_direction(self.Direction.currentText()):
            self.OutText.setText(str(self.uncode(str(self.InText.toPlainText()))))
        else:
            self.OutText.setText(str(self.code(str(self.InText.toPlainText()))))

    def set_direction(self, combo_box_set):                     # Управление направлением кодирования
        if "Сжимать" == combo_box_set:
            return True
        else:
            return False

    def code(self, _str):                                       # Функция, разжимающая данные
        # Функциональная часть приложения
        count = ''
        ans = ''
        for s in _str:
            if s.isdigit():
                count = count + s
            else:
                if count == '':
                    ans += s
                else:
                    for i in range(0, int(count)):
                        ans += s
                count = ''
        return ans

    def uncode(self, _str):                                     # Функция, сжимающая данные
        count = 1
        ans = ''
        for i in range(1, len(_str)):
            if _str[i] == _str[i - 1]:
                count += 1
            else:
                if count > 1:
                    ans += str(count)
                ans += _str[i - 1]
                count = 1

        if count > 1:
            ans += str(count)
        ans += _str[-1]
        return ans


class HelloWindow(QtWidgets.QMainWindow, welcome.Ui_HelloWindow):      # Окно приветствия
    def __init__(self, parent=None):                                    # Инициализация, наследование
        super().__init__(parent)
        self.setupUi(self)
        self.WorkWin = None
        self.Code_But.clicked.connect(self.close_window_code)           # Привязываем функцию tex_output к кнопке Code
        self.Uncode_But.clicked.connect(self.close_window_uncode)       # Привязываем функцию tex_output к кнопке Uncode

    def close_window_code(self):                                        # Обработка кнопки "Сжимать"
        if not self.WorkWin:                                            # Инициализация рабочего окна
            self.WorkWin = WorkWindow(self)
        self.ind = 1
        self.close()                                                    # Закрыли окно приветствия
        self.WorkWin.show()
        self.WorkWin.Direction.setCurrentIndex(0)                       # Установили в ComboBox настройку сжимать

    def close_window_uncode(self):                                      # Обработка кнопки "Разжимать"
        if not self.WorkWin:
            self.WorkWin = WorkWindow(self)
        self.ind = 1
        self.close()
        self.WorkWin.show()
        self.WorkWin.Direction.setCurrentIndex(1)                       # Установили в ComboBox настройку разжимать


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = HelloWindow()  # Создаём объект класса HelloWindow
    window.show()  # Показываем окно
    sys.exit(app.exec_())


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
