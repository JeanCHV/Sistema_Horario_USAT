import pymysql
#Produccion
def obtener_conexion():
    return pymysql.connect(host='monorail.proxy.rlwy.net',
                                port=40341,
                                user='root',
                                password='yXKcAWFqWCnIzFousjWLLBGabdGqOVyt',
                                db='db_calidad')
#Desarrollo
# def obtener_conexion():
#     return pymysql.connect(host='roundhouse.proxy.rlwy.net',
#                                 port=54363,
#                                 user='root',
#                                 password='UAumJRVIMWnTGqRdkZNDqvocCpHjzHKl',
#                                 db='db_calidad')


# def obtener_conexion():
#     return pymysql.connect(host='bkvjs2sg6xirjg6gaoca-mysql.services.clever-cloud.com',
#                                 port=3306,
#                                 user='ugctyihetkrc2clv',
#                                 password='BwWVzLlZ2IEbvqPx33cy',
#                                 db='bkvjs2sg6xirjg6gaoca')

# def obtener_conexion():
#     return pymysql.connect(host='127.0.0.1',
#                                 port=3306,
#                                 user='root',
#                                 password='',
#                                 db='db_calidad')