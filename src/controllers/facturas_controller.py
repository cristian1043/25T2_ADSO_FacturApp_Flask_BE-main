from src.models.facturas import Facturas


class FacturasController:

    @staticmethod
    def get():
        return Facturas.get()

    @staticmethod
    def get_by_id(id):
        return Facturas.get_by_id(id)
    
        if factura is None:
            return None
        
        return factura


    @staticmethod
    def create(data):

        factura = Facturas()

        factura.numero = data["numero"]
        factura.fecha = data["fecha"]
        factura.subtotal = data["subtotal"]
        factura.iva = data["iva"]
        factura.descuento = data["descuento"]
        factura.total = data["total"]
        factura.id_cliente = data["id_cliente"]
        factura.id_usuario = data["id_usuario"]
        factura.id_metodo_pago = data["id_metodo_pago"]

        factura.save()

        return factura
        
    @staticmethod
    def update(id, data):

        factura = Facturas.get_by_id(id)

        if factura is None:
            return False

        factura.numero = data["numero"]
        factura.fecha = data["fecha"]
        factura.subtotal = data["subtotal"]
        factura.iva = data["iva"]
        factura.descuento = data["descuento"]
        factura.total = data["total"]
        factura.id_cliente = data["id_cliente"]
        factura.id_usuario = data["id_usuario"]
        factura.id_metodo_pago = data["id_metodo_pago"]


        factura.update()
        
        return True

    @staticmethod
    def delete(id):

        factura = Facturas.get_by_id(id)
       
        if factura is None:
            return False
        
        factura.delete()
        
        return True