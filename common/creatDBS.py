# -*- coding: utf-8 -*-
'''
    @读取EXCEL文件，并写入数据库中
    @pandas + mysql
    @January, 1, 8
    @author: lc
'''

from sqlalchemy import Column,String,create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from common.config import Code_dict
from sqlalchemy.sql import exists

#创建对象的基类：
Base = declarative_base()

class User( Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    username = Column(String(64))
    password = Column(String(64))
    def __repr__(self):
        return 'id:%s,name:%s'%(self.id,self.username,self.password)

class Role(Base):
    #定义表名
    __tablename__ = 'roles'
    #定义列对象
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True)

def get_session(user,password):
    try:
        user = str(user)
        password = str(password)
        engine = create_engine(
                "mysql+pymysql://%s:%s@localhost:3306/tashan?charset=utf8"%(user,password),encoding="utf-8",convert_unicode=True)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session
    except Exception as ex:
        print('账户名或密码不对，出现如下错误：%s'%ex)

def get_table_name(session):
    try:
        cursor = session.execute("select table_name from information_schema.tables where table_schema = 'tashan';")
        tables = cursor.fetchall()
        tables = list(tables)
        if len(tables) == 0:
            print('没有找到您想要的数据！')
        else:
            print(tables)
            return tables
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________cab_____________________
def key_word_query_CAB(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(客户,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________cap_____________________
def key_word_query_CAP(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(耐压,'%s') or "
            "INSTR(精度,'%s') or INSTR(容值,'%s') or INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
            table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word,key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________cnl_____________________
def key_word_query_CNL(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(品牌,'%s') or "
            "INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________cov_____________________
def key_word_query_COV(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') or "
            "INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________cpu_____________________
def key_word_query_CPU(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________crt_____________________
def key_word_query_CRT(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________cry_____________________
def key_word_query_CRY(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________dio_____________________
def key_word_query_DIO(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________dyn_____________________
def key_word_query_DYN(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________esd_____________________
def key_word_query_ESD(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________fus_____________________
def key_word_query_FUS(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________hus_____________________
def key_word_query_HUS(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________ice_____________________
def key_word_query_ICE(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR('日期','%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________kgcl_____________________
def key_word_query_KGCL(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute("SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s')>0 or INSTR(品名,'%s')>0 or INSTR(规格参数,'%s')>0 or "
                                 "INSTR(客户,'%s')>0;"%(table_name,key_word,key_word,key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________lab_____________________
def key_word_query_LAB(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________lbc_____________________
def key_word_query_LBC(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________ls_____________________
def key_word_query_LS(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s') or INSTR(部门,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________mfc_____________________
def key_word_query_MFC(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________mpz_____________________
def key_word_query_MPZ(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________pas_____________________
def key_word_query_PAS(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格型号,'%s')or "
            "INSTR(客户,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________pcb_____________________
def key_word_query_PCB(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________pkg_____________________
def key_word_query_PKG(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________rel_____________________
def key_word_query_REL(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________res_____________________
def key_word_query_RES(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(品牌,'%s') or INSTR(日期,'%s');" % (
            table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________rfc_____________________
def key_word_query_RFC(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or  INSTR(型号,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(日期,'%s') or INSTR(品牌,'%s');" % (table_name, key_word, key_word, key_word, key_word, key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________sen_____________________
def key_word_query_SEN(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or  INSTR(规格参数,'%s') or INSTR(封装,'%s') or "
            "INSTR(日期,'%s') or INSTR(品牌,'%s');" % (table_name, key_word, key_word, key_word, key_word, key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________sft_____________________
def key_word_query_SFT(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or  INSTR(版本号,'%s') or "
            "INSTR(日期,'%s') or INSTR(客户,'%s');" % (table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s' % ex)

#__________________sma_____________________
def key_word_query_SMA(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute("SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or  INSTR(规格参数,'%s') or "
                                 "INSTR(日期,'%s') or INSTR(品牌,'%s');"%(table_name,key_word,key_word,key_word,key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________sor_____________________
def key_word_query_SOR(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') or "
            "INSTR(日期,'%s') or INSTR(品牌,'%s');" % (
                table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________std_____________________
def key_word_query_STD(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(日期,'%s') or INSTR(品牌,'%s');" % (
            table_name, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________sup_____________________
def key_word_query_SUP(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') or INSTR(规格参数,'%s') or "
            "INSTR(封装,'%s') or INSTR(日期,'%s') or INSTR(品牌,'%s');" % (
            table_name, key_word, key_word, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________tub_____________________
def key_word_query_TUB(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute(
            "SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s')  or INSTR(规格参数,'%s') or "
            "INSTR(日期,'%s') or INSTR(品牌,'%s');" % (
            table_name, key_word, key_word, key_word, key_word, key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________vrt_____________________
def key_word_query_VRT(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute("SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') or INSTR(规格参数,'%s') or "
                                 "INSTR(封装,'%s') or INSTR(日期,'%s') or INSTR(品牌,'%s');"%(table_name,key_word,key_word,key_word,key_word,key_word,key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________whs_____________________
def key_word_query_WHS(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute("SELECT * FROM tashan.%s WHERE INSTR(零件号,'%s')>0 or INSTR(品名,'%s')>0 or INSTR(规格参数,'%s')>0 or "
                                 "INSTR(客户,'%s')>0 or INSTR(日期,'%s') or INSTR('备注','%s');"%(table_name,key_word,key_word,key_word,key_word,key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________编码汇总_____________________
def key_word_query_BMHZ(table_name,table_name_z,key_word):
    try:
        table_name = str(table_name)
        table_name_z = str(table_name_z)
        cursor = session.execute("SELECT * FROM tashan.%s WHERE INSTR(序号,'%s')>0 or INSTR(代码,'%s')>0 or INSTR(名称,'%s')>0 or "
                                 "INSTR(备注,'%s')>0;"%(table_name,key_word,key_word,key_word,key_word))
        result = cursor.fetchall()
        result = list(result)
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________更改和添加记录_____________________
def key_word_query_jl(table_name,table_name_z,key_word):
    try:
        table_name_z = str(table_name_z)
        table_name = str(table_name)
        cursor = session.execute("SELECT * FROM tashan.%s WHERE INSTR(编号,'%s') or INSTR(品名,'%s') or INSTR(型号,'%s') OR INSTR(参数,'%s') or "
                                 "INSTR(封装,'%s') or INSTR(厂家,'%s') or INSTR(日期,'%s') or INSTR(版本,'%s');"%(table_name,key_word,key_word,key_word,key_word,key_word,key_word,key_word,key_word))
        result = cursor.fetchall()

        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[1:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#__________________壳体总成___________________
def key_word_query_SKT(table_name,table_name_z,key_word):
    try:
        table_name = '壳体总成'
        table_name_z = str(table_name_z)
        cursor = session.execute("SELECT * FROM tashan.%s WHERE INSTR(品名,'%s')>0 or "
                                 "INSTR(规格参数,'%s')>0 or INSTR(封装,'%s')>0 or INSTR(品牌,'%s')>0  or INSTR('备注','%s') or INSTR(日期,'%s')>0;"%(table_name,key_word,key_word,key_word,key_word,key_word,key_word))
        result = cursor.fetchall()
        data_dict = {}
        for row in result:
            index_id = table_name_z+'_'+str(row[0])
            values = row[2:]
            data_dict[index_id] = list(values)
        print(data_dict)
        return  data_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#_________________所有表中查询_____________
def key_word_query_all(key_word):
    try:
        datas_dict = {}
        for table_name_z,value in Code_dict.items():
            table_name = Code_dict[table_name_z]
            y_name = 'key_word_query_' + table_name
            data_dict = eval(y_name)(table_name,table_name_z,key_word)
            datas_dict.update(data_dict)
        print(datas_dict)
        return  datas_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#_________________单个表查询_____________
def key_word_query_table(table_name_z,key_word):
    try:
        datas_dict = {}
        table_name = Code_dict[table_name_z]
        y_name = 'key_word_query_' + table_name
        data_dict = eval(y_name)(table_name,table_name_z,key_word)
        datas_dict.update(data_dict)
        #print(datas_dict)
        return  datas_dict
    except Exception as ex:
        print('出现如下异常：%s'%ex)

#______________查询用户名和密码____________
def Is_login_in(username,password):
    session = get_session('root','123456')
    re_str = '用户名不存在或密码错误'
    code = '0'
    is_user = session.query(exists().where(User.username == username)).scalar()
    if is_user is True:
        is_passwd = session.query(exists().where(User.password == password)).scalar()
        if is_passwd is True:
            re_str = '登录成功!'
            code = 1
    return code,re_str
####test####
user = 'root'
password = '123456'
session = get_session(user,password)

#value = key_word_query_table('二极管','黑色')

#get_table_name(session)
#key_word_query_cab('cab','新鸿兴')
#key_word_query_ktzc('壳体总成','金马')
#key_word_query_jl('更改和添加记录','纸盒')
#key_word_query_bmhz('编码汇总','电容')
#key_word_query_whs('whs','新增加')
#key_word_query_vrt('vrt','二极管')
#key_word_query_tup('tub','套管')
#key_word_query_sup('sup','扎扣')
#key_word_query_std('std','2AA')
#key_word_query_sor('sor','汉腾')
#key_word_query_ICE('ICE','微芯')
