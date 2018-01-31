class Contact(object):

    def __init__(self):
        # self.__conID = None
        self.__fname = ""
        self.__lname = ""
        self.__priphone = None
        self.__secphone = None

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, name):
        self.__fname = name

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, name):
        self.__lname = name

    @property
    def priphone(self):
        return self.__priphone

    @priphone.setter
    def priphone(self, num):
        self.__priphone = num

    @property
    def secphone(self):
        return self.__secphone

    @secphone.setter
    def secphone(self, num):
        self.__secphone = num
