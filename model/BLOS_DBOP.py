import model.Sql as sql
def insert_blogs(title, con):
    try:
        s = sql.SqlOp()
        s.insert('BLOGS', {'TITLE': title,
                           'CON': con})
        return '1'
    except:
        return '0'