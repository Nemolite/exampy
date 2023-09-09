class Pointer:
    __total = 20
    @classmethod
    def __check_point(cls,a,b):
        cls.__total = a + b

    def pr_methd(self,a,b):
        self.__check_point(a,b)

    def get_date(self):
        return self.__total
    
pn1 = Pointer()
pn1.pr_methd(3,4)
print(pn1.get_date())