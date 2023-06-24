
# python 개발

import cx_Oracle

def db_connect(): # oracle 연동 함수 생성
    user = "SCOTT"
    pw = "TIGER"
    dsn = "localhost:1521/xe"

    con = cx_Oracle.connect(user, pw, dsn, encoding="UTF-8")
    print("Database version:", con.version)

    return con

def init(con):
    while True:
        print("*"*40)
        print("1. 전체목록")
        print("2. 특정부서검색")
        print("3. 부서저장")
        print("0. 종료")

        # 키보드 입력
        n = int(input("메뉴입력:"))
        if n==1:
            dept_all_list(con)
        elif n==2:
            dept_by_deptno(con)
        elif n==3:
            dept_add(con)
        else:
            print("프로그램 종료")
            exit() # 프로그램 종료

# 1. 전체목록검색
def dept_all_list(con):
    with con.cursor() as cur:
        cur.execute("select * from dept order by deptno")
        res = cur.fetchall()  # list로 반환
        print(res)
        for row in res:
            print(row)

# 2. 특정부서검색
def dept_by_deptno(con):
    n=input("검색할 부서번호:")
    with con.cursor() as cur:
        cur.execute("select * from dept where deptno =:x", x=n)
        res = cur.fetchone()
        print(res)

# 3. 부서저장
def dept_add(con):
    n1 = input("저장할 부서번호:")
    n2 = input("저장할 부서명:")
    n3 = input("저장할 부서위치:")
    with con.cursor() as cur:
        cur.execute( "insert into dept (deptno, dname, loc) values " \
                     " (:deptno, :dname, :loc)", deptno=n1, dname=n2, loc=n3)
        print("저장된 레코드갯수:", cur.rowcount) # 저장된 레코드 개수를 얻어옴
        con.commit()





if __name__ == '__main__':
    con = db_connect()
    init(con)
