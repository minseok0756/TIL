'''
    오라클 연동

        메모리에 영역을 할당받음 - 커서라고 한다
    1. 커서에게 요청
    2. 커서가 db에 접근해서 결과를 가져다줌
    3. 결과가 커서에 저장
    4. 응답

'''
import cx_Oracle

# 1. oracle 연결

user = "SCOTT"
pw = "TIGER"
dsn = "localhost:1521/xe" # ip번호:port번호/서비스이름

con = cx_Oracle.connect(user, pw, dsn, encoding="UTF-8")
print("Database version:", con.version)

# 2. 특정 레코드 하나 얻기. deptno=10
with con.cursor() as cur: # with문으로 커서 얻기. with문이 종료되면 자동 close
    cur.execute("select * from dept where deptno =:x", x=10) # 실행결과를 영역에 가져다 놓음
                                                             # sql에서 실행한거 확인하기
    res = cur.fetchone() # 레코드가 하나인 경우 사용
    print(res)

# 3. 멀티 레코드 얻기
with con.cursor() as cur:
    cur.execute("select * from dept order by deptno")
    res = cur.fetchall()  # list로 반환
    print(res)
    for row in res:
        print(row)

# 4. 단일 저장
# with con.cursor() as cur:
#     cur.execute( "insert into dept (deptno, dname, loc) values " \
#                  " (:deptno, :dname, :loc)", deptno=99, dname='개발', loc="서울")
#     print("저장된 레코드갯수:", cur.rowcount) # 저장된 레코드 개수를 얻어옴
#     con.commit()

# 5. 멀티 저장
# with con.cursor() as cur:
#     rows = [(1, "개발","서울"), (2, "개발","서울")]
#
#     cur.executemany("insert into dept (deptno, dname, loc) values  (:1, :2, :3)", rows)
#     print("저장된 레코드갯수:", cur.rowcount)
#     con.commit()

# 6. 수정
with con.cursor() as cur:
    cur.execute("update dept set dname = :x, loc= :y "
                " where deptno = :z", x="개발부", y="서울시", z=1)
    print("수정된 레코드갯수:", cur.rowcount)
    con.commit()

# 7. 삭제
with con.cursor() as cur:
    cur.execute("delete from dept where deptno = :z", z=2)
    print("삭제된 레코드갯수:", cur.rowcount)
    con.commit()

# 가장 마지막에 항상 자원 반납
con.close()
