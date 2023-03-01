#محمود أسامة محمد 125
#محمود عبد الرحمن محمود بدر 128
#ياسر وليد مراد محمد 141
#خالد محمد السيد احمد46
from tkinter import *


fraction_dict={3:"الثمن",#انصبة كل وارث في هيئة كسور عشرية (المفتاح هنا هو رقم البسط على المقام 24)
               4:"السدس",
               6:"الربع",
               8:"الثلث",
               12:"النصف",
               16:"الثلثين",
               0:"محجوب",
               -1:"الباقي تعصيبا",
               -3:"السدس + الباقي",
               -2:"الباقي للذكر مثل حظ الانثيين",
               -4:"الباقي للذكر مثل حظ الانثيين",}
fraction_list=[]


heirs_dict = {#قاموس الورثة
    'son': 0,
    'son\'s son': 0,
    'father': 0,
    'grandfather': 0,
    'husband': 0,
    'brother': 0,
    'brother\'s son': 0,
    'father\'s brother':0,
    'father\'s brother\'son': 0,
    'mother\'s brother & mother\'s sister': 0,
    'sister': 0,
    'father\'s sister': 0,
    'uncle': 0,
    'father\'s uncle': 0,
    'uncle\'s son': 0,
    'father\'s uncle\'s son': 0,
    'daughter': 0,
    'son\'s daughter': 0,
    'mother': 0,
    'grandmother': 0,
    'wife': 0,
}
def sherch(dict,num=-3):#دالة تقوم بالبحث عن قيمة معينة في القاموس المعطى لها كبارمييتر
    for di in dict:
        if dict[di]==num:
            return True

    return False
def indx(dict,element):#دالة ترجع ترتيب قيمة ما في قاموس معطى كبارميتر وان لم تجدها ترجع -1
    p=0
    for d in dict:
        if d==element:
            return  p
        else:
            p+=1
    return -1
def sum(dict):#دالة ترجع مجموع القيم في القاموس
    s=0
    for d in dict:
        s+=dict[d]
    return s
def dev(am={},dict={}):#تحديد نصيب الوارثون بالعصبة
    for u in am:
        fraction_list.append(fraction_dict[am[u]])#هنا نقوم بملئ ليست الانصبة

    bool=True #لا يوجد توريث بالعصبة
    for a in am:
        if am[a]<0:
            bool=False
    if(bool):
        return am
    else :
        b=True#العصبة ليس بها الذكر مثل حظ الانثيين
        for aa in am:
            if am[aa]<-1:
                 b=False
        if(b):
            for aaa in am:
                if am[aaa]==-1:
                    if 24-sum(am)-1<0:
                       am[aaa]=0
                    else:
                        am[aaa]=24-sum(am)-1
        elif(sherch(am,-3)):#هناك اب او جد يرث السدس + الباقي

            if(sum(am)+7>=24):
                if(heirs_dict["father"]==1):
                    am["father"]=4
                else:
                    am["grandfather"]=4
            else:
                if (heirs_dict["father"]==1):
                    am["father"]=24-sum(am)-3
                else:
                    am["grandfather"]=24-sum(am)-3
        else:#العصبة بها الذكر مثل حظ الانثيين
            remain=24-sum(am)-6
            if remain<0:
                remain=0

            male=0
            female=0
            for i in am:
                if am[i]==-2:
                    male=dict[i]
                if am[i]==-4:
                    female=dict[i]
            arrow=remain/(male*2+female)
            # print(remain,arrow)
            for j in am:
                if am[j]==-2:
                    am[j]=2*arrow*heirs_dict[j]
                if am[j]==-4:
                    am[j]=arrow*heirs_dict[j]
    return am
def recalc(am):# دالة الرد (اذا كان مجموع الفرائض اقل من الواحد الصحيح)
    n=24
    s=sum(am)
    for y in am:
        if y=="wife":#الزوجة والزوج ممنوعون من الرد
            n=24-am["wife"]
            s=s-am["wife"]
        if y == "husband":
            n = 24 - am["husband"]
            s = s - am["husband"]
    for u in am:
        if(u!="wife"and u!="husband"):

            am[u]=am[u]*n/s
    return am
totalMoney=24#مجموع التركة

from tkinter import messagebox
arbic_hiers=['ابن', 'ابن الابن', 'اب', 'جد', 'زوج', 'اخ', 'ابن الاخ', 'اخ لاب', "ابن الاخ لاب", 'اخ لام او اخت لام', 'اخت',
'اخت لاب','عم','عم لاب','ابن العم','ابن العم لاب','بنت','بنت الابن','ام','جدة',"زوجة"]
english_heirs=['son',
    'son\'s son',
    'father',
    'grandfather',
    'husband',
    'brother',
    'brother\'s son',
    'father\'s brother',
    'father\'s brother\'son',
    'mother\'s brother & mother\'s sister',
    'sister',
               'father\'s sister',
               'uncle',
               'father\'s uncle',
               'uncle\'s son',
               'father\'s uncle\'s son',
               'daughter',
               'son\'s daughter',
               'mother',
               'grandmother',
               'wife']




from abc import ABC, abstractmethod


################################# abstract class of Heir #################


class Heir(ABC):
    def __init__(self, heirsDict, number=0):
        self.heirsDict = heirsDict
        self.number = number

    @abstractmethod
    def isBlocked(self):
        pass

    @abstractmethod
    def amount(self):
        pass

# son ################################3


class Son(Heir):

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        return 0

    def amount(self):
        if Son.isBlocked(self) == False:
            if (self.heirsDict["daughter"] > 0):
                return -2
            else:
                return -1

######################################### sons of sons ##########################


class Sons_son(Heir):

    blockers = ["son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Sons_son.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False

    def amount(self):
        if self.isBlocked() == False:
            if self.heirsDict["son\'s daughter"] > 0:
                return -2
            else:
                return -1
        else:
            return 0

# Father#########################################3


class Father(Heir):

    def __init__(self, heirsDict, number=1):
        Heir.__init__(self, heirsDict, number)


    def isBlocked(self):
        return 0

    def amount(self):
        if Father.isBlocked(self) == False:
            if self.heirsDict["son"] > 0 or self.heirsDict["son\'s son"] > 0:
                return 4
            else:
                return -3

###################################### Grandfather ###############################


class Grandfather(Heir):
    blockers = ["father"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Grandfather.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False

    def amount(self):
        if Grandfather.isBlocked(self) == False:
            if self.heirsDict["son"] > 0 or self.heirsDict["son\'s son"] > 0:
                return 4
            else:
                return -3  # الباقي
        else:
            return 0

#################################### Husband ############################################


class Husband(Heir):

    def __init__(self, heirsDict, number=1):
        Heir.__init__(self, heirsDict, number)


    def isBlocked(self):
        return 0

    def amount(self):

            if (self.heirsDict["son"] > 0 or self.heirsDict["son\'s son"]>0 or heirs_dict["daughter"] > 0
                    or heirs_dict["son\'s daughter"] > 0):
                return 6
            else:
                return 12

# wife ##########################3


class Wife(Heir):
    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        return 0

    def amount(self):
        if Wife.isBlocked(self) == False:
            if (self.heirsDict["son"] > 0 or self.heirsDict["son\'s son"] > 0 or heirs_dict["daughter"] > 0
                    or heirs_dict["son\'s daughter"] > 0):
                return 3
            else:
                return 6

#########################################brother###############################


class Brother(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Brother.blockers:
            if self.heirsDict[block] > 0:
                return True

        return False

    def amount(self):
        if Brother.isBlocked(self) == False:
            if (self.heirsDict["sister"] > 0):
                return -2
            else:
                return -1
        else:
            return 0

###################################brother by father##############################


class Brother_by_father(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Brother_by_father.blockers:
            if self.heirsDict[block] > 0:
                return True

        return False

        # محتاجين نعمل حجب للاخ لاب لو كانت في اخت شقيقه عصبه مع البنات او بنات الابن

    def amount(self):
        if Brother_by_father.isBlocked(self) == False:
            if ( self.heirsDict["sister"]>0) and (self.heirsDict["son\'s daughter"]>0 or self.heirsDict["daughter"]>0):
                return 0
            elif (self.heirsDict["father\'s sister"] > 0):
                return -2
            else:
                return -1
        else:
            return 0
###################################brother son#####################################


class Brother_son(Heir):
    blockers = ["father", "son", "grandfather",
                "son\'s son", "brother", 'father\'s brother']

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Brother_son.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False
        # محتاجين نعمل حجب للابن الاخ الشقيق لو كانت في اخت شقيقه او اخت لاب  عصبه مع البنات او بنات الابن

    def amount(self):
        if Brother_son.isBlocked(self) == False:
            if (self.heirsDict["father\'s sister"]>0 or self.heirsDict["sister"]>0) and (self.heirsDict["son\'s daughter"]>0 or self.heirsDict["daughter"]>0):
                return 0
            else:
                return -1
        else:
            return 0
################################ brother by father sons ######################


class Brother_by_father_son(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son",
                "brother", 'father\'s brother', "brother\'s son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Brother_by_father_son.blockers:
            if self.heirsDict[block] > 0:
                return True

        return False
        # محتاجين نعمل حجب للابن الاخ لاب لو كانت في اخت شقيقه او اخت لاب  عصبه مع البنات او بنات الابن

    def amount(self):
        if Brother_by_father_son.isBlocked(self) == False:
            if (self.heirsDict["father\'s sister"]>0 or self.heirsDict["sister"]>0) and (self.heirsDict["son\'s daughter"]>0 or self.heirsDict["daughter"]>0):
                return 0
            else:
                return -1
        else:
            return 0

#################################### uncle ################################


class Uncle (Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother",
                'father\'s brother', "brother\'s son", "father\'s brother\'son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Uncle.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False
        # محتاجين نعمل حجب للابن الاخ لاب لو كانت في اخت شقيقه او اخت لاب  عصبه مع البنات او بنات الابن

    def amount(self):
        if Uncle.isBlocked(self) == False:
            if (self.heirsDict["father\'s sister"]>0 or self.heirsDict["sister"]>0) and (self.heirsDict["son\'s daughter"]>0 or self.heirsDict["daughter"]>0):
                return 0
            else:
                return -1
        else:
            return 0

###################################### uncle by father ############################


class Uncle_by_father(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother",
                'father\'s brother', "brother\'s son", "father\'s brother\'son", "uncle"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Uncle_by_father.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False
        # محتاجين نعمل حجب للابن الاخ لاب لو كانت في اخت شقيقه او اخت لاب  عصبه مع البنات او بنات الابن

    def amount(self):
        if Uncle_by_father.isBlocked(self) == False:
            if (self.heirsDict["father\'s sister"]>0 or self.heirsDict["sister"]>0) and (self.heirsDict["son\'s daughter"]>0 or self.heirsDict["daughter"]>0):
                return 0
            else:
                return -1
        else:
            return 0

#################################### uncle son ###############################


class Uncle_son(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother", 'father\'s brother',
                "brother\'s son", "father\'s brother\'son", "uncle", "father\'s uncle"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Uncle_son.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False
        # محتاجين نعمل حجب للابن الاخ لاب لو كانت في اخت شقيقه او اخت لاب  عصبه مع البنات او بنات الابن

    def amount(self):
        if Uncle_son.isBlocked(self) == False:
            if (self.heirsDict["father\'s sister"]>0 or self.heirsDict["sister"]>0) and (self.heirsDict["son\'s daughter"]>0 or self.heirsDict["daughter"]>0):
                return 0
            else:
                return -1
        else:
            return 0

################################################### uncle by father son#######################################


class Uncle_by_father_son(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother", 'father\'s brother',
                "brother\'s son", "father\'s brother\'son", "uncle", "father\'s uncle", "uncle\'s son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Uncle_by_father_son.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False
        # محتاجين نعمل حجب للابن الاخ لاب لو كانت في اخت شقيقه او اخت لاب  عصبه مع البنات او بنات الابن

    def amount(self):
        if Uncle_by_father_son.isBlocked(self) == False:
            if (self.heirsDict["father\'s sister"]>0 or self.heirsDict["sister"]>0) and (self.heirsDict["son\'s daughter"]>0 or self.heirsDict["daughter"]>0):
                return 0
            else:
                return -1
        else:
            return 0

# daughter ##################################3


class Daughter(Heir):

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        return 0

    def amount(self):
        if Daughter.isBlocked(self) == False:
            if (self.heirsDict["son"] == 0 and heirs_dict["daughter"] == 1):
                return 12
            elif(self.heirsDict["son"] == 0 and heirs_dict["daughter"] > 1):
                return 16
            elif(self.heirsDict["son"] >= 1 and heirs_dict["daughter"] >= 1):
               return -4 # return Son.amount()/2
            else:
                return -1

################################################# daughter of sons #############################


class Daughter_of_sons(Heir):

    blockers = ["son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Daughter_of_sons.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False

    def amount(self):
        if Daughter_of_sons.isBlocked(self) == False:
            if (self.heirsDict["daughter"] >= 2 and self.heirsDict["son\'s son"] == 0):
                return 0
            elif (self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0 and self.heirsDict["son\'s son"] == 0
                  and self.heirsDict["son\'s daughter"] == 1):
                return 12
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0 and self.heirsDict["son\'s son"] == 0
                 and self.heirsDict["son\'s daughter"] > 1):
                return 16
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 1 and self.heirsDict["son\'s son"] == 0
                 and (self.heirsDict["son\'s daughter"] == 1 or self.heirsDict["son\'s daughter"] > 1)):
                return 4
            elif(self.heirsDict["son"] == 0 and  self.heirsDict["son\'s son"] >= 1
                 and self.heirsDict["son\'s daughter"] >= 1):
                return -4
            else:
                return -1
        else:
            return 0

############################################ mother ############################################


class Mother(Heir):

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        return 0

    def amount(self):
        if Mother.isBlocked(self) == False:
            if (self.heirsDict["son"] >=1or self.heirsDict["daughter"]>=1 or self.heirsDict["son\'s son"] >=1
                 or self.heirsDict["son\'s daughter"]>=1 )or(self.heirsDict["brother"]+ self.heirsDict["sister"] +
                 self.heirsDict['father\'s brother']+ self.heirsDict["mother\'s brother & mother\'s sister"]+
                 self.heirsDict["father\'s sister"]>1):

                return 4
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0 and self.heirsDict["son\'s son"] == 0
                 and self.heirsDict["son\'s daughter"] == 0 and ((self.heirsDict["brother"] == 0 and self.heirsDict["sister"] == 0)
                                                                 or (self.heirsDict["brother"] == 1 and self.heirsDict["sister"] == 0) or (self.heirsDict["brother"] == 0
                                                                                                                                           and self.heirsDict["sister"] == 1))):

                return 8
            else:
                return -1

# Grand mother########################################33


class Grand_mother(Heir):
    blockers = ["mother"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Grand_mother.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False

    def amount(self):
        if Grand_mother.isBlocked(self) == False:
            if(self.heirsDict['grandmother'] == 1):
                return 4
            else:
                return -1
        return 0

######################################sister###########################################


class Sister(Heir):

    blockers = ["father", "son", "grandfather", "son\'s son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Sister.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False

    def amount(self):
        if Sister.isBlocked(self) == False:

            if (self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0
                and self.heirsDict["son\'s son"] == 0 and self.heirsDict["son\'s daughter"] == 0
                    and self.heirsDict["brother"] == 0 and self.heirsDict["sister"] == 1):
                return 12
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0
                 and self.heirsDict["son\'s son"] == 0 and self.heirsDict["son\'s daughter"] == 0
                 and self.heirsDict["sister"] > 1 and self.heirsDict["brother"] == 0):
                return 16
            elif(
                  self.heirsDict["brother"] >= 1):
                return -4
            else:
                return -1
        else:
            return 0

##################################### sister by father ####################################


class Sister_by_father(Heir):

    blockers = ["father", "son", "grandfather", "son\'s son", "brother"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Sister_by_father.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False

    def amount(self):
        if Sister_by_father.isBlocked(self) == False:
            # هنا لازم احط شرط ان لو كان في اخت شقيقه صارت عصبه مع البنت او بنت الابن
            if ( self.heirsDict["sister"] > 0) and (
                    self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):

                return 0
            elif (self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0
                  and self.heirsDict["son\'s son"] == 0 and self.heirsDict["son\'s daughter"] == 0
                  and self.heirsDict["brother"] == 0 and self.heirsDict["sister"] == 0
                  and self.heirsDict["father\'s brother"] == 0 and self.heirsDict["father\'s sister"] == 1):
                return 12
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0
                 and self.heirsDict["son\'s son"] == 0 and self.heirsDict["son\'s daughter"] == 0
                 and self.heirsDict["sister"] == 0 and self.heirsDict["brother"] == 0
                 and self.heirsDict["father\'s brother"] == 0 and self.heirsDict["father\'s sister"] >= 2):
                return 16
            elif(self.heirsDict["son"] == 0 and self.heirsDict["son\'s son"] == 0
                 and self.heirsDict["father\'s brother"] == 0 and self.heirsDict["sister"] == 1
                 and Sister.amount() == 12):
                return 4
            elif self.heirsDict['father\'s brother']:
                return -4
            else:
                return -1
        else:
            return 0

##############################################################################################

# محتاجين نعمل حجب للاخ لاب لو كانت في اخت شقيقه عصبه مع البنات او بنات الابن

class Mother_sons(Heir):
    blockers=["son","son\'s son","daughter","son\'s daughter","father","grandfather"]
    def __init__(self, heirsDict, number=heirs_dict["mother\'s brother & mother\'s sister"]):
        Heir.__init__(self, heirsDict, number)

    def isBlocked(self):
        for block in Mother_sons.blockers:
            if self.heirsDict[block] > 0:
                return True
        return  False

    def amount(self):
            if Mother_sons.isBlocked(self) == False:
                if sum(self.heirsDict)==self.heirsDict["mother's brother & mother's sister"]:
                    return -1
                elif (self.heirsDict["mother's brother & mother's sister"]>1):
                    return 8
                else:
                    return 4
            return 0

def all_amounts(dict):#انشاء كائي من كلاسات الورثة المتواجدين في اقرباء الميت
    am={}
    for d in dict:
        if dict[d]>0:
            if d == english_heirs[0]:
                son = Son(dict)
                am[d] = son.amount()
            elif d == english_heirs[1]:
                son_son=Sons_son(dict)
                am[d]=son_son.amount()
            elif d == english_heirs[2]:
                father=Father(dict)
                am[d]=father.amount()
            elif d == english_heirs[3]:
                grandfather=Grandfather(dict)
                am[d]=grandfather.amount()
            elif d == english_heirs[4]:
                hasband=Husband(dict)
                am[d]=hasband.amount()
            elif d == english_heirs[5]:
                brohter=Brother(dict)
                am[d]=brohter.amount()
            elif d == english_heirs[6]:
                brohter_son=Brother_son(dict)
                am[d]=brohter_son.amount()
            elif d == english_heirs[7]:
                father_brohter=Brother_by_father(dict)
                am[d]=father_brohter.amount()
            elif d == english_heirs[8]:
                father_brohter_son=Brother_by_father_son(dict)
                am[d]=father_brohter_son.amount()
            elif d == english_heirs[9]:
                mohter_son=Mother_sons(dict)
                am[d]=mohter_son.amount()
            elif d == english_heirs[10]:
                sister=Sister(dict)
                am[d]=sister.amount()
            elif d == english_heirs[11]:
                father_sister=Sister_by_father(dict)
                am[d]=father_sister.amount()
            elif d == english_heirs[12]:
                uncle=Uncle(dict)
                am[d]=uncle.amount()
            elif d == english_heirs[13]:
                father_uncle=Uncle_by_father(dict)
                am[d]=father_uncle.amount()
            elif d ==english_heirs[14]:
                uncle_son=Uncle_son(dict)
                am[d]=uncle_son.amount()
            elif d == english_heirs[15]:
                father_uncle_son=Uncle_by_father_son(dict)
                am[d]=father_uncle_son.amount()
            elif d == english_heirs[16]:
                daughter=Daughter(dict)
                am[d]=daughter.amount()
            elif d ==english_heirs[17]:
                son_daughter=Daughter_of_sons(dict)
                am[d]=son_daughter.amount()
            elif d == english_heirs[18]:
                mother=Mother(dict)
                am[d]=mother.amount()
            elif d == english_heirs[19]:
                grandmother=Grand_mother(dict)
                am[d]=grandmother.amount()
            elif d == english_heirs[20]:
                wife=Wife(dict)
                am[d]=wife.amount()
    return am
# amount=all_amounts(heirs_dict)
# amount=dev(amount,heirs_dict)
#
# if sum(amount)<24:
#     amount=recalc(amount)
#for l in amount:
    # print(l,(amount[l]/sum(amount))*totalMoney)#هذه الجملة تقوم بحل العول تلقائيا ان وجد
while True:
    input_list = []  # الورثاء الذين قام المستخدم بادخالهم
    st = ''  # الوريث الذي اختاره المستخدم من القائمة


    def add(val):
        global st
        st = val


    x = 700
    y = 140
    i = 0


    def show():
        global comboBox_list
        global x
        global y
        global i
        global st
        # global input_list
        if st != '':
            input_list.append(st)

            wa = Label(fr2, font=('VEXA', 10), text=input_list[i], fg='#fed049', bg='#3d5656')
            wa.place(x=x, y=y)
            if input_list[i] == 'اب':
                comboBox_list.delete('اب')
                st = ""
            elif input_list[i] == 'جد':
                comboBox_list.delete('جد')
                st = ""
            elif input_list[i] == 'ام':
                comboBox_list.delete('ام')
                st = ''
            elif input_list[i] == 'جدة':
                comboBox_list.delete('جدة')
                st = ''
            elif input_list[i] == 'زوج':
                comboBox_list.delete('زوج')
                st = ''
            if input_list[i] == 'زوج':
                comboBox_list.delete('زوجة')
                st = ''
            elif input_list[i] == 'زوجة':
                comboBox_list.delete('زوج')
                st = ''
            i += 1
            x = x - 350
            if x <= 0:
                x = 700
                y = y + 30


    mainwind = Tk()  # النافذة الرئيسية

    mainwind.geometry('800x653+350+30')
    mainwind.config(background='#3d5656')
    #mainwind.iconbitmap('C:\\سنة رابعة\\house-insurance.ico')
    mainwind.title('مشروع المواريث')
    mainwind.resizable(False, False)

    # Frame 1 to title
    fr1 = Frame(mainwind, width=800, height=120, bg='#3d5656')
    fr1.place(x=0, y=0)
    title = Label(fr1, font=('Aviny', 30), text='لِقَوْمٍ يُوقِنُونََ', fg='#fed049', bg='#3d5656')
    title.place(x=325, y=40)
    title = Label(fr1, font=('Aviny', 20), text='وَمَنْ أَحْسَنُ مِنَ اللَّه حُكْمًاَ', fg='#fed049', bg='#3d5656')
    title.place(x=300, y=0)
    # Frame 4 as dash
    fr4 = Frame(width=200, height=2, bg='#CFFDE1')
    fr4.place(x=300, y=120)

    # frame 2 to process
    fr2 = Frame(width=800, height='430', bg='#3d5656')
    fr2.place(x=0, y=122)
    entiry = Entry(fr2, font=('VEXA', 15), fg='#000000',
                   bg='#CFFDE1', relief='groove', width="10")
    entiry.place(x=510, y=10)
    title_entiry = Label(fr2, font=('VEXA', 15),
                         text="أدخل التركة", fg='#fed049', bg='#3d5656')
    title_entiry.place(x=610, y=10)
    entiry2 = Entry(fr2, font=('VEXA', 15), fg='#000000',
                    bg='#CFFDE1', relief='groove', width="10")
    entiry2.place(x=110, y=10)
    title_entiry2 = Label(fr2, font=('VEXA', 15),
                          text="أدخل الوصية إن وجدت", fg='#fed049', bg='#3d5656')
    title_entiry2.place(x=210, y=10)
    menu_bt = Menubutton(fr2, font=('VEXA', 15), text='تحديد الورثة', fg='#3d5656', bg='#CFFDE1', relief='groove')
    menu_bt.place(x=345, y=50)
    comboBox_list = Menu(menu_bt, tearoff=0)
    menu_bt['menu'] = comboBox_list

    comboBox_list.add_radiobutton(label='ابن', font=('VEXA', 10), command=lambda: add('ابن'))
    comboBox_list.add_radiobutton(label='ابن الابن', font=('VEXA', 10), command=lambda: add('ابن الابن'))
    comboBox_list.add_radiobutton(label='اب', font=('VEXA', 10), command=lambda: add('اب'))
    comboBox_list.add_radiobutton(label='جد', font=('VEXA', 10), command=lambda: add('جد'))
    comboBox_list.add_radiobutton(label='زوج', font=('VEXA', 10), command=lambda: add('زوج'))
    comboBox_list.add_radiobutton(label='اخ', font=('VEXA', 10), command=lambda: add('اخ'))
    comboBox_list.add_radiobutton(label='ابن الاخ', font=('VEXA', 10), command=lambda: add('ابن الاخ'))
    comboBox_list.add_radiobutton(label='اخ لاب', font=('VEXA', 10), command=lambda: add('اخ لاب'))
    comboBox_list.add_radiobutton(label='ابن الاخ لاب', font=('VEXA', 10), command=lambda: add('ابن الاخ لاب'))
    comboBox_list.add_radiobutton(label='اخ لام او اخت لام', font=('VEXA', 10),
                                  command=lambda: add('اخ لام او اخت لام'))
    comboBox_list.add_radiobutton(label='اخت', font=('VEXA', 10), command=lambda: add('اخت'))
    comboBox_list.add_radiobutton(label='اخت لاب', font=('VEXA', 10), command=lambda: add('اخت لاب'))
    comboBox_list.add_radiobutton(label='عم', font=('VEXA', 10), command=lambda: add('عم'))
    comboBox_list.add_radiobutton(label='عم لاب', font=('VEXA', 10), command=lambda: add('عم لاب'))
    comboBox_list.add_radiobutton(label='ابن العم', font=('VEXA', 10), command=lambda: add('ابن العم'))
    comboBox_list.add_radiobutton(label='ابن العم لاب', font=('VEXA', 10), command=lambda: add('ابن العم لاب'))
    comboBox_list.add_radiobutton(label='بنت', font=('VEXA', 10), command=lambda: add('بنت'))
    comboBox_list.add_radiobutton(label='بنت الابن', font=('VEXA', 10), command=lambda: add('بنت الابن'))
    comboBox_list.add_radiobutton(label='ام', font=('VEXA', 10), command=lambda: add('ام'))
    comboBox_list.add_radiobutton(label='جدة', font=('VEXA', 10), command=lambda: add('جدة'))
    comboBox_list.add_radiobutton(label='زوجة', font=('VEXA', 10), command=lambda: add('زوجة'))

    add_bt = Button(fr2, font=('VEXA', 13), text='اضافه', fg='#3d5656', bg='#fed049', width=7, command=lambda: show())
    add_bt.place(x=365, y=90)

    # Frame 3 to button
    fr3 = Frame(width=800, height='85', bg='#3d5656')
    fr3.place(x=0, y=547)

    from tkinter import messagebox


    def ca(list):
        x = 550
        y = 110
        s = str(entiry.get())
        slist = s.split(sep=".")

        for sl in slist:
            if (sl.isdigit() and len(slist) <= 2) and s != "" and float(entiry.get()) > 0:
                totalMoney = float(entiry.get())
            else:
                messagebox.showerror("حدث خطأ في ادخال التركة", "الرجاء ادخال التركة في هيئة رقم صحيح او عشري")
                return None
        s = str(entiry2.get())
        slist = s.split(sep=".")
        third = totalMoney / 3
        will = 0
        for sl in slist:
            if (sl.isdigit() and len(slist) <= 2) and s != "" and float(entiry2.get()) >= 0:
                will = float(entiry2.get())
            else:
                messagebox.showerror("حدث خطأ في ادخال الوصية", "الرجاء ادخال الوصية في هيئة رقم صحيح او عشري")
                return None
        if will < third:
            totalMoney = totalMoney - will

        else:
            totalMoney = totalMoney - third
            will = third

        for l in list:
            heirs_dict[english_heirs[arbic_hiers.index(l)]] += 1

        amount = all_amounts(heirs_dict)

        amount = dev(amount, heirs_dict)

        if sum(amount) < 24:
            amount = recalc(amount)
        for o in range(0, len(list)):
            if o % 2 == 0:
                x = 550
                y = y + 30
            else:
                x = 200
            if heirs_dict[english_heirs[arbic_hiers.index(list[o])]] > 1 and (
                    fraction_list[int(indx(amount, english_heirs[
                        arbic_hiers.index(list[o])]))] != "الباقي تعصيبا") and (
                    fraction_list[int(indx(amount, english_heirs[
                        arbic_hiers.index(list[o])]))] != "الباقي للذكر مثل حظ الانثيين") and (
                    fraction_list[int(indx(amount, english_heirs[
                        arbic_hiers.index(list[o])]))] != "السدس + الباقي") and (
                    fraction_list[int(indx(amount, english_heirs[
                        arbic_hiers.index(list[o])]))] != "محجوب"):
                lb = Label(fr2, font=('VEXA', 10), text="مشترك في " + fraction_list[int(indx(amount,
                                                                                             english_heirs[
                                                                                                 arbic_hiers.index(
                                                                                                     list[o])]))],
                           fg='#212121', bg='#3d5656')
                lb.place(x=x, y=y)
                lb2 = Label(fr2, font=('VEXA', 12, "bold"), text=(round((amount[english_heirs[
                    arbic_hiers.index(list[o])]] / heirs_dict[english_heirs[arbic_hiers.index(list[o])]] / sum(
                    amount)) * totalMoney, 2)), fg='white', bg='#3d5656')
                lb2.place(x=x - 70, y=y)
            else:
                lb = Label(fr2, font=('VEXA', 10),
                           text=fraction_list[int(indx(amount, english_heirs[arbic_hiers.index(list[o])]))],
                           fg='#212121', bg='#3d5656')
                lb.place(x=x, y=y)
                lb2 = Label(fr2, font=('VEXA', 12, "bold"), text=(round((amount[english_heirs[
                    arbic_hiers.index(list[o])]] / heirs_dict[english_heirs[arbic_hiers.index(list[o])]] / sum(
                    amount)) * totalMoney, 2)), fg='white', bg='#3d5656')
                lb2.place(x=x - 70, y=y)
        fraction_list.clear()
        for dic in heirs_dict:
            heirs_dict[dic] = 0
    def cls():
        import sys
        sys.exit()


    mainwind.protocol("WM_DELETE_WINDOW", cls)
    def rest():
        fraction_list.clear()
        for dic in heirs_dict:
            heirs_dict[dic]=0

        mainwind.destroy()

    process_bt = Button(fr3, font=('VEXA', 15), text='تقسيم الميراث', fg='#3d5656', bg='#fed049', width=20,
                        command=lambda: ca(input_list))
    process_bt.place(x=150, y=30)


    reset = Button(fr3, font=('VEXA', 15), text='اعادة تعيين', fg='#3d5656', bg='#fed049', width=20,
                        command=lambda :rest())
    reset.place(x=450, y=30)

    mainwind.mainloop()



