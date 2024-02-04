from datetime import date

class File:
    def __init__(self, name: str, file_format: str) -> None:
        self.__name = name
        self.__date = date.today()
        self.__file_format = file_format
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date
        
    @property
    def file_format(self):
        return self.__file_format
    
    @file_format.setter
    def file_format(self, file_format):
        self.__file_format = file_format
        
    def __str__(self) -> str:
        return f"{self.name} - ({self.file_format}) - date: {self.date}"
