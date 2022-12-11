class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            
    def agregar(self, menu):
        id_menu = str(menu.id_menu)
        if id_menu not in self.carrito.keys():
            self.carrito[id_menu] = {
                "id_menu": menu.id_menu,
                "nombre": menu.nombre_m,
                "acumulado": menu.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id_menu]["cantidad"] += 1
            self.carrito[id_menu]["acumulado"] += menu.precio
        self.guardar_carrito()
        
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    
    def eliminar(self, menu):
        id_menu = str(menu.id_menu)
        if id_menu in self.carrito:
            del self.carrito[id_menu]
            self.guardar_carrito()
            
    def restar(self, menu):
        id_menu = str(menu.id_menu)
        if id_menu in self.carrito.keys():
            self.carrito[id_menu]["cantidad"] -= 1
            self.carrito[id_menu]["acumulado"] -= menu.precio
            if self.carrito[id_menu]["cantidad"] <= 0: self.eliminar(menu)
            self.guardar_carrito()
            
    def limpiar_carrito(self):
        self.session["carrito"] = {}
        self.session.modified = True
        
    def devolver_pedidos(self):
        return self.carrito.values()
                
                
        
        
                