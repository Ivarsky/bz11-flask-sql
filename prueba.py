from balance.models import DBManager

manager = DBManager('data/balance.db')
sql = "SELECTid, fecha, concepto, tipo, cantidad FROM movimientos ORDER BY cantidad DESC"
manager.consultaSQL(sql)
