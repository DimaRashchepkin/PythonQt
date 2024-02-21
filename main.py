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

        book1 = Book("The Dark Tower: Gunslinger", "S.King", 200, "cover1.png")
        book2 = Book("The Dark Tower II: The Drawing of the Three", "S.King", 350, "cover2.png")
        book3 = Book("The Dark Tower III: The Waste Lands", "S.King", 500, "cover3.png")
        data = str(book1.get_info() + "\n" + book2.get_info() + "\n" + book3.get_info())
        label2 = QLabel(data, self)
        label2.setWordWrap(True)
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
