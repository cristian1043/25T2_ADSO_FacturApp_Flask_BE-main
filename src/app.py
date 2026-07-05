from flask import Flask

from src.models import Base, engine

from src.models.categorias import Categorias
from src.models.clientes import Clientes
from src.models.productos import Productos
from src.models.proveedores import Proveedores
from src.models.roles import Roles
from src.models.usuarios import Usuarios
from src.models.facturas import Facturas
from src.models.detalle_facturas import DetalleFacturas
from src.models.compras import Compras
from src.models.detalle_compras import DetalleCompras

Base.metadata.create_all(bind=engine)

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)

