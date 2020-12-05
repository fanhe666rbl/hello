# Create your views here.
import pymysql
from django.http import JsonResponse
import django


def test(request):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="rbl991020", database="test", charset="utf8")
    cur = con.cursor()
    name = request.POST['name']
    # id = request.POST['id']
    # print(id)
    sql = "select num from test1 where name = \"" + str(name) + "\""
    cur.execute(sql)

    # sql = "insert into test1 values (\"sss\", 777);"
    # cur.execute(sql)

    num = cur.fetchall()
    con.close()
    # print(num)
    return JsonResponse(num, safe=False)
