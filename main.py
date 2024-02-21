from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from Book import Book


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(800)
        self.setFixedHeight(800)

        label = QLabel("Do not share my personal information, please", self)
        label.setFixedWidth(self.width())
        label.setFixedHeight(self.height() / 4)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setWordWrap(True)
        font = QFont("Times", 16)
        font.setItalic(1)
        label.setFont(font)
        label.setMargin(10)

        label1 = QLabel("Please", self)
        label1.setFixedWidth(self.width())
        label1.setFixedHeight(self.height() / 4)
        label1.move(0, self.height() - label.height())
        label1.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        font1 = QFont("Times", 32)
        label1.setFont(font1)
        label1.setMargin(10)

        img_label = QLabel(self)
        image = QPixmap('img.png')
        image = image.scaledToHeight(200)
        img_label.setPixmap(image)
        img_label.setFixedWidth(self.width())
        img_label.setFixedHeight(self.height())
        img_label.setAlignment(Qt.AlignCenter)

        book = Book("Dark Tower", "S.King", "~3000", "cover.png")
        label2 = QLabel(book.get_info(), self)
        label2.move(0, self.height() / 2)
        label2.setFixedWidth(self.width())
        label2.setFixedHeight(self.height() / 4)
        label2.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        label2.setFont(font)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
