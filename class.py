# class Fan:
#     def __init__(self,color,type):
#         self.color=color
#         self.type=type 
#         print(color,type)
# fanobj=Fan("grey","AC")

# class Fan:
#     def __init__(self,color,type):
#         self.color=color
#         self.type=type 
#         self._company="GFC"
#         print(color,type)
#     def showcompany(self):
#         print(self._company)
# fanobj=Fan("grey","AC")
# fanobj.showcompany()

# class Fan:
#     def __init__(self,color,type):
#         self.color=color
#         self.type=type 
#         self._company="GFC"   #protected
#         self.__price=11000    #private
#         print(color,type)
#     def showcompany(self):
#         print(self._company)
#     def getprice(self):
#         self.__price=10000
#         return(self.__price)
#     def setprice(self,month):
#         if month>=4 and month<=8:
#             self.__price=12000
#             return(self.__price)
# fanobj=Fan("grey","AC")
# fanobj.showcompany()
# x=fanobj.getprice()
# print(x)s
# y=fanobj.setprice(3)
# print(y)

class QuizSession:
    def __init__(self,max_point=100,):
        self.__score=0
        self.___max_possible=max_point
    @property
    def score(self):
        percentage= (self.__score*100)/self.___max_possible
        return(f"your percentage is {percentage} %")
    
    @score.setter
    def score(self,value):
        self.__score=value
session=QuizSession(100)
session.score=97
x=session.score
print(x)
90