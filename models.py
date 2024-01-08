#models.py
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date, func
from database import Base, engine
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = 'clientes'

    ID = Column(Integer, primary_key=True)
    Provincia = Column(String(100))
    Nombre_y_Apellido = Column(String(200))
    Domicilio = Column(String(200))
    Telefono = Column(String(20))
    Edad = Column(Integer)
    Localidad = Column(String(100))
    X = Column(Float)
    Y = Column(Float)
    Fecha_Alta = Column(Date)
    Usuario_Alta = Column(String(50))
    Fecha_Ultima_Modificacion = Column(Date)
    Usuario_Ultima_Modificacion = Column(String(50))
    Marca_Baja = Column(Integer)

"""
IdCompra,Fecha,IdProducto,Cantidad,Precio,IdProveedor
1,2015-01-30,42832,13,560.51,12
2,2015-01-30,42833,11,497.58,7
3,2015-01-30,42834,1,588.5,6
4,2015-01-30,42835,9,567.66,14
"""
class Compra(Base):
    __tablename__= 'compras'
    IdCompra = Column(Integer, primary_key=True)
    Fecha = Column(Date) 
    IdProducto = Column(Integer)
    Cantidad= Column(Integer)
    Precio = Column(Float)
    IdProveedor = Column(Integer)


class Gasto(Base):
    __tablename__ = 'gastos'

    IdGasto = Column(Integer, primary_key=True)
    IdSucursal = Column(Integer)
    IdTipoGasto = Column(Integer)
    Fecha = Column(Date)
    Monto = Column(Float)

class TipoGasto(Base):
    __tablename__ = 'tipos_gasto'
    IdTipoGasto = Column(Integer, primary_key=True)
    Descripcion = Column(String(200))
    Monto_Aproximado = Column(Float)


class Venta(Base):
    __tablename__ = 'ventas'

    IdVenta = Column(Integer, primary_key=True)
    Fecha = Column(Date)
    Fecha_Entrega = Column(Date)
    IdCanal = Column(Integer)
    IdCliente = Column(Integer)
    IdSucursal = Column(Integer)
    IdEmpleado = Column(Integer)
    IdProducto = Column(Integer)
    Precio = Column(Float)
    Cantidad = Column(Integer)
    
class Sucursal(Base):
    __tablename__ = 'sucursales'

    ID = Column(Integer, primary_key=True)
    Sucursal = Column(String(100))
    Direccion = Column(String(500))
    Localidad = Column(String(200))
    Provincia = Column(String(100))
    Latitud = Column(Float)
    Longitud = Column(Float)