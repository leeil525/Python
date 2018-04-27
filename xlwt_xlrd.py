import xlwt
import xlrd
from xlutils.copy import copy
# workbook=xlwt.Workbook(encoding='utf-8') #创建xls
# worksheet=workbook.add_sheet('my_sheet') #创建sheet
# worksheet.write(0,0,label='this is test') #在sheet中操作
# worksheet.write_merge(1, 5, 3, 4 ,'hello') #多行合并中写入
# workbook.save('excel_test.xls')  #保存
# data=xlrd.open_workbook('excel_test.xls')  #打开文件
# sheet=data.sheet_by_index(0)  #读取第一个表单
# print(sheet.name,sheet.nrows,sheet.ncols)  #输出表单名字 行数 列数
# rows = sheet.row_values(1)  #获取整行数据
# cols = sheet.col_values(0) #获取整列 从0开始
# print(rows,cols)
#print(sheet.cell(0,0).value  ,  sheet.cell_value(1,1)  ,  sheet.row(1)[0].value ) #读取指定单元格的值
#print(sheet.cell(1,1).ctype)  #单元格类型 ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

# '''解决日期变成数字的方法'''
# from datetime import datetime,date
# date_value=xlrd.xldate_as_tuple(sheet.cell_value(1,1),data.datemode) #先判断数据类型是不是date
# print(date(*date_value[:3]).strftime('%Y/%m/%d'))  #*[] 把数组分成每一个  字典就**｛｝

# '''合并的单元格查找'''
# print(sheet.merged_cells) #返回有四个数值的元组的数组(row,row_range,col,col_range) 行高位行低位列高列低
# for(rlow, rhigh, rcol, chigh) in sheet.merged_cells:
#     sheet.cell_value(rlow, rcol)



'''追加的办法'''
data=xlrd.open_workbook('excel_test.xls')
new=copy(data) #拷贝原始数据
sheet=new.get_sheet(0)
sheet.write(1,1,'pipi')
new.save('excel_test.xls')









