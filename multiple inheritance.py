#Multiple Inheritance==>
class SubMarks: #class 1
    TOC=int(input("Enter paper marks of TOC:"))
    DBMS=int(input("Enter paper marks of DBMS:"))
    NM=int(input("Enter paper marks of NM:"))
class PractMarks: #class 2
    DbmsPract=int(input("Enter DBMS marks:"))
class Result(SubMarks,PractMarks):
    def total(self):
        if self.TOC>=17 and self.DBMS>=17 and self.NM>=17:
            print("PASS")
        else:
            print("FAIL")
obj= Result()
obj.total()