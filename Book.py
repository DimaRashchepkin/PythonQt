class Book:
    def __init__(self, title, author, pages, cover_file):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__cover_file = cover_file

    def get_info(self):
        return str(self.__title + " " + self.__author + " " + self.__pages + " " + self.__cover_file)
