import pymysql


def obtener_conexion():
    return pymysql.connect(host='sql3.freemysqlhosting.net',
                                port=3306,
                                user='sql3702269',
                                password='j1pBlTp3hP',
                                db='sql3702269')

""" def obtener_conexion():
    return pymysql.connect(host='127.0.0.1',
                                port=3306,
                                user='root',
                                password='',
                                db='db_calidad') """