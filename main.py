#main.py
import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Cliente

# Crear las tablas en la base de datos si no existen
from models import Base
Base.metadata.create_all(bind=engine)

# Leer el DataFrame Clientes
df_clientes = pd.read_csv('clase4h/Clientes.csv', sep=';', decimal=',')

# Leer el DataFrame Otros 
df_compras = pd.read_csv('clase4h/Compra.csv', sep=';', decimal=',')
df_gastos = pd.read_csv('clase4h/Gasto.csv', sep=';', decimal=',')
df_tipos_gasto = pd.read_csv('clase4h/TiposDeGasto.csv', sep=',', decimal=',')
df_ventas = pd.read_csv('clase4h/Venta.csv', sep=',', decimal=',')
df_sucursales = pd.read_csv('clase4h/Sucursales.csv', sep=';', decimal=',')


# ... (Aquí se puede hacer cualquier manipulación necesaria en el DataFrame)
# Dataframe para tratar
print(df_clientes.head())
print(df_tipos_gasto.info())

df_clientes.drop('col10', axis=1, inplace=True)
print(df_clientes.info())
# Convertir columnas a los tipos de datos deseados
df_clientes['ID'] = df_clientes['ID'].astype(int)
df_clientes['Provincia'] = df_clientes['Provincia'].astype(str)
df_clientes['Nombre_y_Apellido'] = df_clientes['Nombre_y_Apellido'].astype(str)
df_clientes['Domicilio'] = df_clientes['Domicilio'].astype(str)
df_clientes['Telefono'] = df_clientes['Telefono'].astype(str)
df_clientes['Edad'] = df_clientes['Edad'].astype(int)
df_clientes['Localidad'] = df_clientes['Localidad'].astype(str)
df_clientes['X'] = df_clientes['X'].astype(float)
df_clientes['Y'] = df_clientes['Y'].astype(float)
df_clientes['Fecha_Alta'] = pd.to_datetime(df_clientes['Fecha_Alta'])
df_clientes['Usuario_Alta'] = df_clientes['Usuario_Alta'].astype(str)
df_clientes['Fecha_Ultima_Modificacion'] = pd.to_datetime(df_clientes['Fecha_Ultima_Modificacion'])
df_clientes['Usuario_Ultima_Modificacion'] = df_clientes['Usuario_Ultima_Modificacion'].astype(str)
df_clientes['Marca_Baja'] = df_clientes['Marca_Baja'].astype(int)


df_tipos_gasto['Monto_Aproximado'] = df_tipos_gasto['Monto_Aproximado'].astype(float)

names_columns = df_clientes.columns
print(names_columns)


# Inicializar la sesión
db = SessionLocal()

try:
    # Migrar DataFrame a la base de datos MySQL
    #df_clientes.to_sql(name='clientes', con=engine, if_exists='replace', index=False)


    # ... (Aquí podrías realizar operaciones adicionales si lo necesitas)
    df_compras.to_sql(name='compras', con=engine, if_exists='replace', index=False)
    df_gastos.to_sql(name='gastos', con=engine, if_exists='replace', index=False)
    df_tipos_gasto.to_sql(name='tipos_gastos', con=engine, if_exists='replace', index=False)
    df_ventas.to_sql(name='ventas', con=engine, if_exists='replace', index=False)
    df_sucursales.to_sql(name='sucursales', con=engine, if_exists='replace', index=False)

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

