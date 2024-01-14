#models.py
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date, func
from database import Base, engine
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = 'cliente'

    IdCliente = Column(Integer, primary_key=True)
    Nombre_y_Apellido = Column(String(500))
    Domicilio = Column(String(500))
    Telefono = Column(String(100))
    Edad = Column(Integer)
    Rango_Etario = Column(String(255))
    IdLocalidad = Column(Integer)
    Latitud = Column(Float)
    Longitud = Column(Float)

class Compra(Base):
    __tablename__= 'compra'
    IdCompra = Column(Integer, primary_key=True)
    Fecha = Column(Date) 
    IdProducto = Column(Integer)
    Cantidad= Column(Integer)
    Precio = Column(Float)
    IdProveedor = Column(Integer)


class Gasto(Base):
    __tablename__ = 'gasto'

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
    __tablename__ = 'venta'

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
    __tablename__ = 'sucursal'

    IdSucursal = Column(Integer, primary_key=True)
    Sucursal = Column(String(255))
    Domicilio = Column(String(255))
    IdLocalidad = Column(Integer)
    Latitud = Column(Float)
    Longitud = Column(Float)

class Calendario(Base):
    __tablename__ = 'calendario'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    anio = Column(Integer)
    mes = Column(Integer)
    dia = Column(Integer)
    trimestre = Column(Integer)
    semana = Column(Integer)
    dia_nombre = Column(String(100))
    mes_nombre = Column(String(100))

class CanalVenta(Base):
    __tablename__ = 'canal_venta'
    id = Column(Integer, primary_key=True)
    Canal = Column(String(150))

class Empleado(Base):
    __tablename__ = 'empleado'

    id = Column(Integer, primary_key=True)
    codigo_empleado = Column(Integer)
    apellido = Column(String(300))
    nombre = Column(String(255))
    id_sucursal = Column(Integer)
    id_sector = Column(Integer)
    id_cargo = Column(Integer)
    salario = Column(Float)

class Localidad(Base): 
    __tablename__ = 'localidad'

    id = Column(Integer, primary_key=True)
    localidad = Column(String(255))
    id_provincia = Column(Integer)
    latitud = Column(Float)
    longitud = Column(Float)

class Producto(Base): 
    __tablename__ = 'producto'

    id = Column(Integer, primary_key=True)
    producto = Column(String(300))
    precio = Column(Float)
    id_tipo_producto = Column(Integer)

class Proveedor(Base): 
    __tablename__ = 'proveedor'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(150))
    domicilio = Column(String(500))
    id_localidad = Column(Integer)

class Provincia(Base): 
    __tablename__ = 'provincia'

    id = Column(Integer, primary_key=True)
    provincia = Column(String(255))


class Comision(Base): 
    __tablename__ = 'comision'

    id = Column(Integer, primary_key=True)
    codigo_empleado = Column(Integer)
    id_sucursal = Column(Integer)
    apellido_y_nombre = Column(String(500))
    sucursal = Column(String(255))
    anio = Column(Integer)
    mes = Column(Integer)
    porcentaje = Column(Float)