from typing import Union
class Contact(object):

    def __init__(self):
        self.__conID = None
        self.__fname = ""
        self.__lname = ""
        self.__priphone = None
        self.__secphone = None


    @property
    def conID(self) -> int:
        return self.__conID

    @conID.setter
    def conID(self, num) -> None:
        if not isinstance(num, int):
            raise TypeError("This should be an integer set by the database")
        self.__conID = num

    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError("This should be a string!")
        self.__fname = name

    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError("This should be a string!")
        self.__lname = name

    @property
    def priphone(self) -> int:
        return self.__priphone

    @priphone.setter
    def priphone(self, num) -> None:
        if not isinstance(num, int):
            raise TypeError("This should be an integer set by the database")
        self.__priphone = num

    @property
    def secphone(self) -> int:
        return self.__secphone

    @secphone.setter
    def secphone(self, num) -> None:
        if not isinstance(num, Union[int, None]):
            raise TypeError("This should be an integer set by the database")
        self.__secphone = num
