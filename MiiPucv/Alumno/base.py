import psycopg2

# Postgres
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "admin"
PSQL_PASS = "admin"
PSQL_DB   = "MII"

try:
    # Conectarse a la base de datos
    connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
    conn = psycopg2.connect(connstr)
    # Abrir un cursor para realizar operaciones sobre la base de datos
    cur = conn.cursor()
    # Ejecutar una consulta SELECT
    sqlquery = "Select nombre, apellido from 'Alumno_alumno';"
    cur.execute('Select nombre from "Direccion_comuna"')
    # Obtener los resultados como objetos Python
    rows = cur.fetchone()
    
    if rows is not None:
            print(rows)
    else:
        print("No hay datos en la tabla.")
    cur.close()
    conn.close()


    # Hacer algo con los datos

except:
    print("Error de base de datos")