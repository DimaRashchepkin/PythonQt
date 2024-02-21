class Book:
    def __init__(self, title, author, pages, cover_file):
        if not (isinstance(title, str) and isinstance(author,
                                                      str) and isinstance(pages, int) and isinstance(cover_file, str)):
            raise TypeError('Book constructor takes another types')
        self.__title = title
        self.__author = author
        self.__pages = str(pages)
        self.__cover_file = cover_file

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        self.__author = author

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError("Pages must be a integer")
        self.__pages = str(pages)

    @property
    def cover_file(self):
        return self.__cover_file

    @cover_file.setter
    def cover_file(self, cover_file):
        if not isinstance(cover_file, str):
            raise TypeError("Cover file must be a string")
        self.__cover_file = cover_file

    def get_info(self):
        return str(self.__title + " " + self.__author + " " + self.__pages + " " + self.__cover_file)
