class Producto:

    def __init__(self, código, nombre, precio ):
        self.__código = código
        self.__nombre = nombre
        self.__precio = precio

    @property
    def código(self):
        return self.__código
    
    @código.setter
    def código(self, valor):
        self.__código = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @código.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio
    
    @código.setter
    def precio(self, valor):
        self.__precio = valor

    def calcular_total(self, unidades):
        return self.__precio * unidades
        
    def __str__(self):
        return "Código: " + str(self.__código) + ", nombre: " + self.__nombre + ", precio: " + str(self.__precio) + "€"

p1 = Producto(123, "Agua Micelar", 5)
p2 = Producto(456, "Protector solar", 25)
p3 = Producto(789, "Ácido hialurónico", 11)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(2))
print(p2.calcular_total(1))
print(p3.calcular_total(2))