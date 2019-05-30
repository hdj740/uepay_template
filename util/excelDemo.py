#!/
import xlwt
import xlrd

#打开文件，获取excel文件的workbook（工作簿）对象
workbook = xlrd.open_workbook ('/home/huang/桌面/2018-2019学年度+档案是否完善下发.xlsx')

'''对workbook对象进行操作'''

#获取所有sheet的名字
names = workbook.sheet_names()
print("names:",names)

#通过sheet索引获得sheet对象

workbook = workbook.sheet_by_name("专科 (18-19学年度) 省外 ")
print("workbook:",workbook)

#由上可知，workbook.sheet_names() 返回一个list对象，可以对这个list对象进行操作
#workbook = workbook.sheet_names()[0] #通过sheet索引获取sheet名称
#print(workbook)

'''对sheet对象进行操作'''
name = workbook.name #获取表的姓名
print("name",name) #各省市

nrows = workbook.nrows #获取该表总行数
print(nrows)

ncols = workbook.ncols #获取该表总列数
print(ncols)

for i in range(nrows): #循环打印每一行
    print(workbook.row_values(i)) #以列表形式读出，列表中的每一项是str类型
    # ['各省市', '工资性收入', '家庭经营纯收入', '财产性收入', ………………]
    # ['北京市', '5047.4', '1957.1', '678.8', '592.2', '1879.0，…………]
col_data = workbook.col_values(0) #获取第一列的内容
print(col_data)

#通过坐标读取表格中的数据
cell_value1 = workbook.cell_value(0,0)
cell_value2 = workbook.cell_value(0,1)
print(cell_value1)
print(cell_value2)

cell_value3 = workbook.cell(0,0).value
cell_value4 = workbook.cell(0,1).value
print(cell_value3)
print(cell_value4)