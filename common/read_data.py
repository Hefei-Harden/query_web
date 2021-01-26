# -*- coding: utf-8 -*-
'''
    @读取数据文件
    @January, 1, 8
    @author: lc
'''
import pandas as pd
import os
from common import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#获取data路径下所有数据文件名
def get_file_names():
    file_list=[]
    file_names = os.listdir(config.DATA_DIR)
    for name in file_names:
        file_list.append(os.path.join(config.DATA_DIR,name))
    return file_list

#处理EXCEL数据，将EXCEL数据写入MYSQL
class Save_data_to_sql(object):
    """读取excel数据 保存 公路舱单的基本信息"""

    def __init__(self,filename):
        self.paths = get_file_names()
        self.engine = create_engine(
            "mysql+pymysql://root:123456@localhost:3306/tashan?charset=utf8",encoding="utf-8",convert_unicode=True)
        self.file_nums = len(self.paths)
        self.sheet_names = {}
        self.filename = filename

    def hanlder_data(self,table_name,sheet_values):
        try:
            """ 处理excel 导入的数据"""
            count_row = sheet_values.shape[0]
            if table_name == 'KGCL':
                sheet_values['客户'] = ''
                kh_name = ''
                for count in range(count_row):
                    if sheet_values.iloc[count][0] in config.KH_name_list:
                        kh_name = sheet_values.iloc[count][0]
                    else:
                        sheet_values.loc[count,'客户'] = kh_name
            if table_name == 'LS':
                sheet_values['部门'] = ''
                bm_name = ''
                for count in range(count_row):
                    if sheet_values.iloc[count][2] in config.BM_name_list:
                        bm_name = sheet_values.iloc[count][0]
                        sheet_values.drop(index=count,axis=0)
                    else:
                        sheet_values.loc[count,'部门'] = bm_name
            #sheet_values.dropna(subset=['零件号'], axis=0,how='all')
            if table_name == 'CAP':
                col_name = sheet_values.columns.values
                ggcs = col_name[4]
                cap_value,intensive_value,withstand_value = ggcs[5:-1].split('/')
                sheet_values.insert(4,cap_value,'')
                sheet_values.insert(4,intensive_value,'')
                sheet_values.insert(4,withstand_value,'')
                all_data = sheet_values[ggcs] #不具有可扩展性
                sheet_values_temp = sheet_values.copy()
                for index_num in range(len(all_data)):
                    index_id = all_data.index[index_num]
                    all_string = str(all_data[index_id])
                    all_string = all_string.strip()
                    string_1,string_2,string_3 = all_string.split('/',2)
                    sheet_values[cap_value].loc[index_id] = string_1
                    sheet_values[intensive_value].loc[index_id] = string_2
                    sheet_values[withstand_value].loc[index_id] = string_3
                sheet_values_temp =sheet_values.drop(labels = ggcs,axis=1)
                sheet_values = sheet_values_temp
            return sheet_values
        except Exception as ex:
            print("出现如下异常：%s" % ex)

    def drop_tables(self):
        try:
            DBSession = sessionmaker(bind=self.engine)
            session = DBSession()
            cursor = session.execute("select table_name from information_schema.tables where table_schema = 'tashan';")
            tables = cursor.fetchall()
            if len(tables) == 0:
                print('There have no tables!')
            else:
                for table in tables:
                    cursor = session.execute("drop table `%s`;"%(table._row[0]))
                    if cursor is not None:
                        print('Drop {} tables successful!'.format(str(table._row[0])))
        except Exception as ex:
            print("出现如下异常：%s"%ex)

    def insert_data(self):
        # 将表格的数据导入数据库
        try:
            df = self.get_excel_data()
            for sheet_name,sheet_values in df.items():
                sheet_values.dropna(how='all',axis=0)
                #如电容-CAP，table_name = 电容，再config.Code_dict里找出对应的编号
                if '-' in sheet_name:
                    sheet_name,res = sheet_name.split('-',1)    #分离名称和编号
                if sheet_name in config.Code_dict:
                    table_name = config.Code_dict[sheet_name]
                else:
                    table_name = sheet_name
                table_name = table_name.strip()     #去除一些特殊符号，否则写入数据库时会报错

                if '零件号' in sheet_values:
                    nan_list = sheet_values[sheet_values['零件号'].isin([float('nan')])].index   #获取所有零件号为空的行
                    for index_id in nan_list:
                        sheet_values = sheet_values.drop(index=index_id)  #删除所有零件号为空的行

                if table_name in config.sheet_error:    #客供材料和物料需要增加一项
                    sheet_values = self.hanlder_data(table_name,sheet_values)

                for col_name in sheet_values.columns:
                    if '/' in col_name:
                        kh_1,_ = col_name.split('/',1)
                        sheet_values.rename(columns={col_name:kh_1},inplace=True)
                sheet_values.to_sql(table_name, self.engine, if_exists='replace', index=True)
                print("creat "+table_name+"successful!")
        except Exception as ex:  # 如果有异常则输出告警 EXception可以捕获python中任意异常，它属于异常基类
            print("出现如下异常：%s" % ex)
            return Exception.__cause__

    # 获取excel的表名
    def get_excel_data(self):
        if self.filename[-3:] == 'csv':
            df = pd.read_csv(self.filename,sheet_name=None,encoding='UTF-8')
        else:
            df = pd.read_excel(self.filename, sheet_name=None, encoding='UTF-8')
        return df

if __name__ == '__main__':
    object = Save_data_to_sql(filename='F:\工作日志\他山科技\公司资料/零件库-2021-1-6.xlsx')
    #object.drop_tables()
    #object.insert_data()