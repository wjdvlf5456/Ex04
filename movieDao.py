import cx_Oracle


def insert(movieVo):
    conn = cx_Oracle.connect("admin", "^^65Rhcemdtla", "/Users/choijungphil/jungphil/Wallet_webdb")
    cs = conn.cursor()

    sql = '''
        insert into movie values(seq_movie_no.nextval, :rank, :title, :filePath)
    '''

    cs.execute(sql, rank=movieVo[0], title=movieVo[1], filePath=movieVo[2])

    conn.commit()

    cs.close()
    conn.close()

    return cs.rowcount


'''
movieVo = [1, "외계+인 1부", "C:\\javaStudy\\upload\\movie\\0d90ba8a-8670-4e11-8f22-14e428c53a42.jpg"]
count = insert(movieVo)
print(count)
'''


def select_all():
    conn = cx_Oracle.connect("admin", "^^65Rhcemdtla", "/Users/choijungphil/jungphil/Wallet_webdb")
    cs = conn.cursor()

    sql = '''
            select no,
                   rank,
                   name,
                   filePath
            from movie
        '''
    rs = cs.execute(sql)

    for movie in rs:
        print(movie[0])
        print(movie[1])
        print(movie[2])
        print(movie[3])


# select_all()

def update():
    pass


def delete():
    pass
