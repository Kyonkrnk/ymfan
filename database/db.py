import sqlite3

dbname = "database/server.db"
table_name = "ymfan"
conn = sqlite3.connect(dbname)
c = conn.cursor()
sql = f'create table if not exists {table_name}(chart_id primary key, title, composer, chart_author, difficulty, description, bgm_url, bgm_hash, jacket_url, jacket_hash, chart_url, chart_hash, post_at, update_at)'
c.execute(sql)
conn.close()

def save_chart_info(
        chart_id: str, 
        title: str, 
        composer: str, 
        chart_author: str, 
        difficulty: int, 
        description: str, 
        bgm_url: str,
        bgm_hash: str,
        jacket_url: str,
        jacket_hash: str,
        chart_url: str,
        chart_hash: str,
        post_at: str,
        update_at: str
):  
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = f'insert into {table_name} (chart_id, title, composer, chart_author, difficulty, description, bgm_url, bgm_hash, jacket_url, jacket_hash, chart_url, chart_hash, post_at, update_at) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    c.execute(sql, [chart_id, title, composer, chart_author, difficulty, description, bgm_url, bgm_hash, jacket_url, jacket_hash, chart_url, chart_hash, post_at, update_at])
    conn.commit()
    conn.close()

def get_data_from_database(limit: str):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = f'select * from {table_name} order by post_at desc limit {limit}'
    c.execute(sql)
    result = c.fetchall()
    conn.close()

    return result

def get_leveldata_from_database(chart_id: str):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = f'select * from {table_name} where chart_id = "{chart_id}"'
    c.execute(sql)
    result = c.fetchone()
    conn.close()

    return result

print(get_leveldata_from_database("0daca")[0])