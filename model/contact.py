class Contact(object):

    def __init__(self):
        # self.__conID = None
        self.__fname = ""
        self.__lname = ""
        self.__priphone = None
        self.__secphone = None

    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, name) -> None:
        self.__fname = name

    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, name) -> None:
        self.__lname = name

    @property
    def priphone(self) -> int:
        return self.__priphone

    @priphone.setter
    def priphone(self, num) -> None:
        self.__priphone = num

    @property
    def secphone(self) -> int:
        return self.__secphone

    @secphone.setter
    def secphone(self, num) -> None:
        self.__secphone = num
