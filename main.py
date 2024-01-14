#main.py
import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Cliente

# Crear las tablas en la base de datos si no existen
from models import Base
Base.metadata.create_all(bind=engine)

# Leer el DataFrame Clientes
df_cliente = pd.read_csv('datasets/cliente.csv', sep=',', decimal=',', encoding='latin-1')

# Leer el DataFrame Otros 
df_compra = pd.read_csv('datasets/compra.csv', sep=';', decimal=',', encoding='latin-1')
df_gasto = pd.read_csv('datasets/gasto.csv', sep=',', encoding='latin-1')
df_tipos_gasto = pd.read_csv('datasets/tipo_gasto.csv', sep=',', decimal=',', encoding='latin-1')
df_venta = pd.read_csv('datasets/venta.csv', sep=',', decimal=',',encoding='latin-1')
df_sucursal = pd.read_csv('datasets/sucursal.csv', sep=',', encoding='latin-1')

df_calendario = pd.read_csv('datasets/calendario.csv', sep=',', decimal=',',encoding='latin-1')
df_canal_venta = pd.read_csv('datasets/canal_venta.csv', sep=',', encoding='latin-1')
df_empleado = pd.read_csv('datasets/empleado.csv', sep=',', encoding='latin-1')
df_localidad = pd.read_csv('datasets/localidad.csv', sep=',', encoding='latin-1')
df_producto = pd.read_csv('datasets/producto.csv', sep=',', encoding='latin-1')
df_provincia = pd.read_csv('datasets/provincia.csv', sep=',', encoding='latin-1')

df_comision_c = pd.read_csv('datasets/c_centro.csv', sep=',', encoding='latin-1')
df_comision_r = pd.read_csv('datasets/c_crosas.csv', sep=',', encoding='latin-1')
df_comision_q = pd.read_csv('datasets/c_quiroz.csv', sep=',', encoding='latin-1')
# Concatenar los DataFrames verticalmente
df_comision = pd.concat([df_comision_c, df_comision_r, df_comision_q], ignore_index=True)

# Tratamiento de datos
df_cliente['Latitud'] = df_cliente['Latitud'].astype(float)
df_cliente['Longitud'] = df_cliente['Longitud'].astype(float)
df_cliente['Telefono'] = df_cliente['Telefono'].astype(str)

df_tipos_gasto['Monto_Aproximado'] = df_tipos_gasto['Monto_Aproximado'].astype(float)

df_gasto['Fecha'] = pd.to_datetime(df_gasto['Fecha'], format='%Y-%m-%d')


df_venta['Fecha'] = pd.to_datetime(df_venta['Fecha'], format='%Y-%m-%d')
df_venta['Fecha_Entrega'] = pd.to_datetime(df_venta['Fecha_Entrega'], format='%Y-%m-%d')
df_venta['Precio'] = df_venta['Precio'].astype(float)

df_calendario.rename(columns={'IdFecha': 'idcalendario'}, inplace=True)
df_calendario['fecha'] = pd.to_datetime(df_calendario['fecha'], format='%Y-%m-%d')



# Inicializar la sesión
db = SessionLocal()

try:
    # Migrar DataFrame a la base de datos MySQL
    df_cliente.to_sql(name='cliente', con=engine, if_exists='replace', index=False)

    df_compra.to_sql(name='compra', con=engine, if_exists='replace', index=False)
    df_gasto.to_sql(name='gasto', con=engine, if_exists='replace', index=False)
    df_tipos_gasto.to_sql(name='tipos_gastos', con=engine, if_exists='replace', index=False)
    df_venta.to_sql(name='venta', con=engine, if_exists='replace', index=False)
    df_sucursal.to_sql(name='sucursal', con=engine, if_exists='replace', index=False)

    df_calendario.to_sql(name='calendario', con=engine, if_exists='replace', index=False)
    df_canal_venta.to_sql(name='canal_venta', con=engine, if_exists='replace', index=False)
    df_empleado.to_sql(name='empleado', con=engine, if_exists='replace', index=False)
    df_localidad.to_sql(name='localidad', con=engine, if_exists='replace', index=False)
    df_producto.to_sql(name='producto', con=engine, if_exists='replace', index=False)
    df_provincia.to_sql(name='provincia', con=engine, if_exists='replace', index=False)
    df_comision.to_sql(name='comision', con=engine, if_exists='replace', index=False)

    # Confirmar los cambios en la base de datos
    db.commit()
    print("Migración exitosa del DataFrame a la base de datos.")

except Exception as e:
    # En caso de error, hacer rollback
    db.rollback()
    print(f"Error durante la migración del DataFrame a la base de datos: {e}")

finally:
    # Cerrar la sesión
    db.close()

