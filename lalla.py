import model.Sql as Sql



s = Sql.SqlOp()
# s.runSql('''create table USER(//=================================
# USERNAME TEXT NOT NULL ,
# NICKNAME TEXT NOT NULL,
# PWD TEXT NOT NULL,
# AGE TEXT NOT NULL,
# CONMENTS TEXT)
# ''')//=============================================================
# s.insert('USER',{'USERNAME':'Showi','NICKNAME':'Showi','PWD':'Showi666','AGE':'20'})

# :param table_name: 数据库的名字
#         :param kwargs: 可变参长度的参数,字典形式传入

# print(s.select('USER','username like "Showi"'))
# s.runSql('''create table BLOGS(
# ID integer primary key autoincrement,
# TITLE TEXT NOT NULL,
# CON TEXT NOT NULL,
# CONMENTS TEXT)
# ''')
# s.runSql('drop table BLOGS')
# s.insert('BLOGS',{'TITLE':'Showi小冰:每一个爱笑的灵魂背后都是一个..giao?','CON':'一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao'})