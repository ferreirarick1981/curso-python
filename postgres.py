import psycopg2
try:
    con = psycopg2.connect('host=127.0.0.1 dbname=projeto user=admin password=4linux')
    print('conexão efetuada com sucesso')
    cur=con.cursor()
    cur.execute("insert into usuarios(nome, email, idade)\
                    values('renato','renato@gmail.com',30)")
    cur.execute("select * from usuarios")
    dados = cur.fetchall()
    for x in dados:
        print (x)
    con.commit()
except Exception as e:
    print('erro:{}'.format(e))