class MinhaLista():
    def __init__(self):
        self.__items = []
        self.__index = 0
    
    def add(self,valor):
        self.__items.append(valor)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration
            
    def __str__(self):
        return f"{self.__class__.__name__} {self.__items}"

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor
    
    def __deliten__(self, index):
        del self.__items[index]
    
    def __rp__(self):
        return self.__str__()



if __name__== "__main__":
    lista = MinhaLista()
    lista.add("Luiz")
    lista.add("Maria")

print(lista)
print(next(lista))
print(next(lista))
print(lista[1])
lista[1] = "Drica"
lista[2] = "Rayanne"
print(lista)


for nomes in lista:
    print(nomes)