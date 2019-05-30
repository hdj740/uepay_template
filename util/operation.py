#coding:utf-8
import xlrd
import os
data = xlrd.open_workbook("/home/huang/桌面/PythonTest.xlsx")
print(os.path.exists("/home/huang/桌面/PythonTest.xlsx"))

table = data.sheets()[0]          #通过索引顺序获取
print(table)
table = data.sheet_by_index(0)
print(table)
table = data.sheet_by_name(u'Sheet1')
print(table)
#获取整行和整列的值
print(table.row_values(14))
print(table.col_values(1))

#获取行数和列数
print(table.nrows)
print(table.ncols)

#获取单元格
print(table.cell(14,1).value)



'''
class OperationExcel:

    def __init__(self,file_name,sheet_id):
        self.data = self.get_data(file_name,sheet_id)

    def get_data(self,file_name,sheet_id):
        xlrd.open_workbook(file_name)
        tables = data.sheets()[sheet_id]
        return tables

if __name__ == '__main__':
    opers = OperationExcel()
    opers.get_data()
'''
