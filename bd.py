import pymysql

#Desarrollo
def obtener_conexion():
    return pymysql.connect(host='127.0.0.1',
                                port=3306,
                                user='root',
                                password='',
                                db='bdcalidad')


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