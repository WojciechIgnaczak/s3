# składający wiersze tekstu
# wiesz posiada swój numer
# identyfikator wiersza jako napis
# identyfikator nieunikalny



# klasy abstrakcyjne
class TextLines():
    def __init__(self):
        pass
    
    def readLine(self,numerWiersza): # wiersz o zadanym numerze
        pass

    def writeLine(self,text): # dodanie wiersza na końcu
       pass
    
    def writeLine(self,text,numerWiersza):# dodanie wiersza w konkretnej pozycji, nie pozwalamy na dodanie wiersza z przerwą, gdy linia istnieje to zostaje nadpisany
       pass

    def deleteLine(self,numerWiersza): # usuwanie wiersza i bez przenumerowanie tych poniżej
        pass
        
    def getNumberOfLines():
        pass

class IdentifiedTextLines(TextLines): 
    def __init__(self):
        pass

    def readLine(self,key): # wiersze! o zadanym numerze
        pass

    def writeLine(self,key,text): # dodanie wiersza na końcu
       pass
    
    def writeLine(self,key,text,numerWiersza):# dodanie wiersza w konkretnej pozycji, nie pozwalamy na dodanie wiersza z przerwą, gdy linia istnieje to zostaje nadpisany
       pass

    def deleteLine(self,identyfikator): # usuwanie wiersza i bez przenumerowanie tych poniżej
        pass

class UniquelyIdentifiedTextLines():
    IdentifiedTextLines


# Klasy "realne"

class TextLinesInMemory(TextLines):
    def __init__(self):
        pass

class TextLinesInFile(TextLines):
    def __init__(self):
        pass

class TextLinesInDB(TextLines):
    def __init__(self):
        pass




class IdentifiedTextLinesInMemory(IdentifiedTextLines):
    def __init__(self):
        pass

class IdentifiedTextLinesInFIle(IdentifiedTextLines):
    def __init__(self):
        pass

class IdentifiedTextLinesInDB(IdentifiedTextLines):
    def __init__(self):
        pass
    


class UniquelyIdentifiedTextLinesInMemory(UniquelyIdentifiedTextLines):
    def __init__(self):
        pass

class UniquelyIdentifiedTextLinesInFIle(UniquelyIdentifiedTextLines):
    def __init__(self):
        pass

class UniquelyIdentifiedTextLinesInDB(UniquelyIdentifiedTextLines):
    def __init__(self):
        pass
    

def main():
    pass
if __name__ =='__main__':
    main()