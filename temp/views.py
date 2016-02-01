from django.shortcuts import render
from django.http import HttpResponse
import json
import MySQLdb

# Create your views here.

def chart(request, mac):
    return render(request, 'chart.html', {'mac':mac})

def history(request, mac):
    return render(request, 'history.html', {'mac':mac})

def rtlist(request):
    retjson = {}
    maclist = []
    try:
        conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'ssol', port = 3306)
        cur = conn.cursor()
        cur.execute('select mac,count(*) from t_data group by mac')
        results = cur.fetchall()
        if cur.rowcount == 0:
            retjson['result'] = 'fail'
            retjson['rowcount'] = 0
            return HttpResponse(json.dumps(retjson), content_type = 'application/json')
        for one in results:
            maclist.append(one[0])
        cur.close()
        retjson['list'] = maclist
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    except MySQLdb.Error,e:
        retjson['result'] = 'error'
        retjson['msg'] = e[1]
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    finally:
        conn.close()

def rttemp(request, mac, length):
    retjson = {}
    try:
        conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'ssol', port = 3306)
        cur = conn.cursor()
#        cur.execute('select * from t_data where mac = %s order by time desc limit 1', mac)
#        cur.execute('select t_data.id,t_data.mac,t_data.pmac,t_data.value,t_sensorlist.unit,t_data.time from t_data,t_sensorlist where t_data.tid = t_sensorlist.tid;')
        sql = 'select t_data.id,t_data.mac,t_data.pmac,t_data.value,t_sensorlist.unit,t_data.time from t_data,t_sensorlist where t_data.mac=\'%s\' && t_data.tid=2 && t_data.tid=t_sensorlist.tid order by time desc limit %d;' % (mac, int(length))
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        if results == None:
            retjson['result'] = 'fail'
            return HttpResponse(json.dumps(retjson), content_type = 'application/json')
        datalist = []
        mac = ''
        pmac = ''
        unit = ''
        for one in results:
            dict = {}
            id = one[0]
            mac = one[1]
            pmac = one[2]
            value = one[3]
            unit = one[4]
            time = one[5]
            dict['id'] = int(id)
            dict['value'] = float(value)
            dict['time'] = str(time)
            datalist.append(dict)
        retjson['result'] = 'success'
        retjson['mac'] = mac
        retjson['pmac'] = pmac
        retjson['unit'] = unit
        retjson['datalist'] = datalist
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    except MySQLdb.Error,e:
        mysql = []
        for one in e:
            mysql.append(str(e))
        retjson['mysql'] = mysql
        retjson['result'] = 'error'
        retjson['sql'] = sql
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    finally:
        conn.close()

def rtvdd(request, mac, length):
    retjson = {}
    try:
        conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'ssol', port = 3306)
        cur = conn.cursor()
#        cur.execute('select * from t_data where mac = %s order by time desc limit 1', mac)
        sql = 'select t_data.id,t_data.mac,t_data.pmac,t_data.value,t_sensorlist.unit,t_data.time from t_data,t_sensorlist where t_data.mac=\'%s\' && t_data.tid=1 && t_data.tid=t_sensorlist.tid order by time desc limit %d;'% (mac, int(length))
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        if results == None:
            retjson['result'] = 'fail'
            return HttpResponse(json.dumps(retjson), content_type = 'application/json')
        datalist = []
        mac = ''
        pmac = ''
        unit = ''
        for one in results:
            dict = {}
            id = one[0]
            mac = one[1]
            pmac = one[2]
            value = one[3]
            unit = one[4]
            time = one[5]
            dict['id'] = int(id)
            dict['value'] = float(value)
            dict['time'] = str(time)
            datalist.append(dict)
        retjson['result'] = 'success'
        retjson['mac'] = mac
        retjson['pmac'] = pmac
        retjson['unit'] = unit
        retjson['datalist'] = datalist
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    except MySQLdb.Error,e:
        rmysql = []
        for one in e:
            mysql.append(str(e))
        retjson['mysql'] = mysql
        retjson['result'] = 'error'
        retjson['sql'] = sql
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    finally:
        conn.close()

def rttemp_all(request, mac):
    retjson = {}
    try:
        conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'ssol', port = 3306)
        cur = conn.cursor()
#        cur.execute('select * from t_data where mac = %s order by time desc limit 1', mac)
#        cur.execute('select t_data.id,t_data.mac,t_data.pmac,t_data.value,t_sensorlist.unit,t_data.time from t_data,t_sensorlist where t_data.tid = t_sensorlist.tid;')
        sql = 'select t_data.id,t_data.mac,t_data.pmac,t_data.value,t_sensorlist.unit,t_data.time from t_data,t_sensorlist where t_data.mac=\'%s\' && t_data.tid=2 && t_data.tid=t_sensorlist.tid order by time desc;' % (mac)
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        if results == None:
            retjson['result'] = 'fail'
            return HttpResponse(json.dumps(retjson), content_type = 'application/json')
        datalist = []
        mac = ''
        pmac = ''
        unit = ''
        for one in results:
            dict = {}
            id = one[0]
            mac = one[1]
            pmac = one[2]
            value = one[3]
            unit = one[4]
            time = one[5]
            dict['id'] = int(id)
            dict['value'] = float(value)
            dict['time'] = str(time)
            datalist.append(dict)
        retjson['result'] = 'success'
        retjson['mac'] = mac
        retjson['pmac'] = pmac
        retjson['unit'] = unit
        retjson['datalist'] = datalist
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    except MySQLdb.Error,e:
        mysql = []
        for one in e:
            mysql.append(str(e))
        retjson['mysql'] = mysql
        retjson['result'] = 'error'
        retjson['sql'] = sql
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    finally:
        conn.close()

def rtvdd_all(request, mac):
    retjson = {}
    try:
        conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'ssol', port = 3306)
        cur = conn.cursor()
#        cur.execute('select * from t_data where mac = %s order by time desc limit 1', mac)
        sql = 'select t_data.id,t_data.mac,t_data.pmac,t_data.value,t_sensorlist.unit,t_data.time from t_data,t_sensorlist where t_data.mac=\'%s\' && t_data.tid=1 && t_data.tid=t_sensorlist.tid order by time desc;'% (mac)
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        if results == None:
            retjson['result'] = 'fail'
            return HttpResponse(json.dumps(retjson), content_type = 'application/json')
        datalist = []
        mac = ''
        pmac = ''
        unit = ''
        for one in results:
            dict = {}
            id = one[0]
            mac = one[1]
            pmac = one[2]
            value = one[3]
            unit = one[4]
            time = one[5]
            dict['id'] = int(id)
            dict['value'] = float(value)
            dict['time'] = str(time)
            datalist.append(dict)
        retjson['result'] = 'success'
        retjson['mac'] = mac
        retjson['pmac'] = pmac
        retjson['unit'] = unit
        retjson['datalist'] = datalist
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    except MySQLdb.Error,e:
        rmysql = []
        for one in e:
            mysql.append(str(e))
        retjson['mysql'] = mysql
        retjson['result'] = 'error'
        retjson['sql'] = sql
        return HttpResponse(json.dumps(retjson), content_type = 'application/json')
    finally:
        conn.close()


