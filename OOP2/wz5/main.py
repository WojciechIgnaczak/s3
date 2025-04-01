from abc import ABC, abstractmethod
from datetime import datetime
import sqlite3

# Abstract class
class TextLines(ABC):
    # BEGIN: public method
    @abstractmethod
    def get_number_of_lines(self):
        pass

    @abstractmethod
    def read_line(self,line_number): # wiersz o zadanym numerze
        pass

    @abstractmethod
    def delete_line(self,line_number): # usuwanie wiersza i bez przenumerowanie tych poniżej
        pass
    
    @abstractmethod
    def write_line(self,text,line_number=None):
        pass


class TextLinesInDB(TextLines):
    # BEGIN: public method
    def __init__(self, db_name=None):
        if db_name is None:
            timestamp=datetime.now().strftime('%Y%m%d%H%M%S')
            self.__db_name=f"data_{timestamp}.db"
        else:
            self.__db_name=db_name

        connection = sqlite3.connect(self.__db_name)

        with open("db.sql") as script:
            connection.executescript(script.read())

        connection.commit()
        connection.close()

        self.__connection=None
        self.__cur=None


    def get_number_of_lines(self):
        sql="SELECT COUNT(*) as count FROM lines;"
        
        connection=self.__get_connection()
        connection.row_factory=sqlite3.Row
        cur=connection.cursor()
        res=cur.execute(sql)
        row=res.fetchone()
        row=dict(row)
        #connection.close()
        return row['count']

    def read_line(self,line_number): # wiersz o zadanym numerze
        
        if self.get_number_of_lines()>=line_number:

            connection=self.__get_connection()
            sql="SELECT * FROM lines WHERE id=(?);"
            connection.row_factory=sqlite3.Row
            cur=connection.cursor()
            res=cur.execute(sql,(line_number,))
            row=res.fetchone()
            row=dict(row)
            #connection.close()
            return row
        else:
            raise IndexError("index out of range")
            
    def delete_line(self,line_number):

        if self.get_number_of_lines()>=line_number and line_number >=0:
            self.__write_line_at_index("",line_number)
        else:
            raise IndexError("index out of range")
    

    def write_line(self,text,line_number=None):# dodanie wiersza w konkretnej pozycji, nie pozwalamy na dodanie wiersza z przerwą, gdy linia istnieje to zostaje nadpisany
        if line_number is None:
            self.__write_line_at_end(text)
        else:
            self.__write_line_at_index(text,line_number)  

    def dump(self):
        sql="SELECT * FROM lines;"
        connection=self.__get_connection()
        cur=connection.cursor()
        res=cur.execute(sql)
        row=res.fetchall()
        for i in row:
            print(dict(i))
        connection.close()
        
    def close_db(self):
        self.__connection.close()
        self.__connection=None

    # BEGIN: private method
    def __get_connection(self):
        if self.__connection is None:
            self.__connection = sqlite3.connect(self.__db_name)
        return self.__connection


    def __write_line_at_end(self,text):
        
        if type(text) is not str:
            raise TypeError("Text must be a text")
        sql="INSERT INTO lines (line) VALUES (?);"
        connection=self.__get_connection()
        cur=connection.cursor()
        res=cur.execute(sql,(text,))
        connection.commit()
        #connection.close()
        


    def __write_line_at_index(self,text,line_number):
        if type(text) is not str:
            raise TypeError("Text must be a text")
        if line_number>=1 and line_number<=self.get_number_of_lines():
            sql="UPDATE lines SET line=(?), modiffied=CURRENT_TIMESTAMP WHERE id=(?);"
            connection=self.__get_connection()
            cur=connection.cursor()
            res=cur.execute(sql,(text,line_number))
            connection.commit()
            #connection.close()
        else:
            for i in range(1,line_number-self.get_number_of_lines()):
                self.__write_line_at_end("")
            self.__write_line_at_end(text)







def testTextLinesInDB():
    try:
        tlidb=TextLinesInDB('line_set.db')
        print(tlidb.get_number_of_lines())
        tlidb.write_line("test text 1")
        print(tlidb.get_number_of_lines())
        print(tlidb.read_line(1))

        tlidb.write_line("test text 2")
        print(tlidb.read_line(2))

        tlidb.close_db()
        print("modyfikacja w indeksie")
        tlidb.write_line("test text 2->3",2)
        print(tlidb.read_line(2))


        print("dodanie poza indeksami")
        tlidb.write_line("test text 5",5)
        print(tlidb.read_line(2))
        print(tlidb.read_line(3))
        print(tlidb.read_line(4))
        print(tlidb.read_line(5))


        print("usuwanie 5")
        tlidb.delete_line(5)
        print(tlidb.read_line(5))


        print("dump")
        tlidb.dump()

    except Exception as er:
        print(er)
def main():
   # testIdentifiedTextLines()
    testTextLinesInDB()

if __name__ =='__main__':
    main()














class IdentifiedTextLines():
    def __init__(self):
        self.__lines=TextLinesInMemory();
        self.__ids={};

    def get_identifiers(self):
        return [d for d in self.__ids]
    def write_line(self,text,identifier):
        if identifier not in self.__ids:
            self.__ids[identifier]=[]
        self.__lines.write_line(text)
        line_number=self.__lines.get_number_of_lines()-1
        self.__ids[identifier].append(line_number)

    def read_line(self,identifier):
        if identifier not in self.__ids:
            raise KeyError("Unknown identifier")
        result=[]

        for idx in self.__ids[identifier]:
            line=self.__lines.read_line(idx)
            result.append(line)
        return result

    def delete_line(self,identifier):
        if identifier not in self.__ids:
            raise KeyError("Unknown identifier")
        for idx in self.__ids[identifier]:
            self.__lines.delete_line(idx)
            
        del self.__ids[identifier]

    def find_free_index(self):
        number_of_lines=self.__lines.get_number_of_lines()
        print(number_of_lines)
        seq=[n for n in range(number_of_lines)]
        print(seq)
        for  key in self.__ids:
            print(f"Identifier: {key}")
            for idx in self.__ids[key]:
                print(idx)
                seq.remove(idx)
        print(seq)
        if len(seq)>0:
            print(f"Use index {seq[0]}")
        else:
            print("use without index (append)")
    
def testIdentifiedTextLines():
    titl=IdentifiedTextLines()
    titl.write_line("foo1","f1")
    titl.write_line("bar1","b1")
    titl.write_line("foo2","f1")
    titl.write_line("bar2","b1")
    titl.write_line("foo3","f1")
    lines=titl.read_line("f1")
    print(titl.get_identifiers())

    for l in lines:
        print(l)
    titl.delete_line("f1")
    print(titl.get_identifiers())



