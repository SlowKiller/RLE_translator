import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
import psutil


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.TransBut.clicked.connect(self.text_output)

    def text_output(self):
        self.OutText.setText(
            str(self.serial_code(str(self.InText.toPlainText()))))

    def serial_code(self, _str):
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


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
