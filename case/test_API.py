import xlrd

dir_case = '/home/huang/桌面/test3.xlsx'
data = xlrd.open_workbook(dir_case)
table = data.sheets()[1]
nor = table.nrows
nol = table.ncols
print(nol,"列",nor,"行")
dict = {}
for i in range(1, nor):
    for j in range(nol):
        title = table.cell_value(0, j)
        value = table.cell_value(i, j)
        dict[title] = value
    print(dict)

