import model.Sql as Sql
import server as se
from model import UsefulFunc


#用来手动修改数据库
s = Sql.SqlOp()
print(s.select('USER'))
