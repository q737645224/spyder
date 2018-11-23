import pymysql

class DBHelper:

    def __init__(self, host='127.0.0.1',
                 user='root', pwd='123456',
                 db='MaoYan', port=3306,
                 charset='utf8'
                 ):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = port
        self.charset = charset
        self.conn = None
        self.cur = None 

    def connetDataBase(self):
        try:
            self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.pwd, 
                                    db=self.db,
                                    charset=self.charset,
                                    port=self.port)
        except:
            print("connetDataBase error")
            return False

        self.cur = self.conn.cursor()
        return True

    def execute(self, sql, params=None):
        if self.connetDataBase() == False:
            #print("connect Database")
            return False

        #print("connect Ok")
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as e:
            print(e)
            #print("execute: "+sql+" error")
            return False
        return True

    def  fetchCount(self, sql):
        if self.connetDataBase() == False:
            return -1
        self.execute(sql)
        return self.cur.fetchone()[0]

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True



if __name__ == '__main__':
    dbhelper = DBHelper()
    #print(dbhelper.connetDataBase())

    #INSERT INTO `MaoYan`.`film`(`name`,`star`,`time`)VALUES(

    # title = '蚁人'
    # star = '汤姆克鲁斯'
    # time = '2017'
    # sql = "INSERT INTO MaoYan.Film2(title,star,releasetime)VALUES(%s,%s,%s);" 
    # params = (title, star, time)
    # if dbhelper.execute(sql, params) == True:
    #     print("插入成功")
    # dbhelper.close()

    Am=dbhelper.fetchCount("SELECT count(*) FROM `MaoYan`.`Film` WHERE releasetime like '%美国%';")
    print(Am)