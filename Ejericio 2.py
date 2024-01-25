class Pedido:

    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 0

        for(p,c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)

        return total

    def mostrar_pedido(self):

        for(p,c) in zip(self.__productos, self.__cantidades):
            print("Producto -> (", p, "), Cantidad: " + str(c))





productos = [p1, p2, p3]
cantidades = [2, 1, 2]

pedido = Pedido(productos, cantidades)

print("Total pedido: " + str(pedido.total_pedido()))

pedido.mostrar_pedido()