#******************************************#
#              EvenPay(v1)                 #
#                                          #
#             participant.py               #
#          created by Renjie Zhu           #
#              on 7/20/16                  #
#******************************************#

# class definition
class Participant:

    def __init__(self,name,paid):
        self.__name = name
        # money already paid, set to negative for addition
        self.__paid = paid
        self.__pays = 0.0
        self.__take = True # true means to take, not to pay

    def get_name(self):
        return self.__name

    def get_paid(self):
        return self.__paid

    def get_pays(self):
        return self.__pays

    def set_paid(self,paid):
        self.__paid = paid
        return

    def set_pays(self,pays):
        self.__pays = pays
        return

    def difference(self,average):
        self.set_pays(round(self.get_paid() - average,2))
        # __pays >= 0 : no need to pay
        # __pays < 0  : need to pay
        return
