import xlrd





#### 读取参数并放在一个数组里面（行，行，列，列） ####

store_data=[]
data=xlrd.open_workbook(r'C:\Users\ONE\Desktop\bb.xls',formatting_info=True)####********
sheet=data.sheet_by_index(2)  #读取第3个表单
for data in sheet.merged_cells:
    if(data[2]==1 and data[3]==2):
        store_data.append(data)



#####输入参数#######
while(1):
    stopword = '' # 输入停止符
    string = ''
    shuru=[]
    print('请输入:')
    for line in iter(input, stopword): # 输入为空行，表示输入结束
      shuru.append(line)
      string += line + '\n'
    #### 输入参数 ####


    #### 查找 ####
    judge_shuzu=[] #文档零时存放集数据

    for judge in  store_data:
        if((judge[1]-judge[0])==len(shuru)):
            judge_shuzu=[]#清空
            for value in range(judge[0],judge[1]):
                judge_shuzu.append(sheet.cell_value(value,2))

            num=0
            for  a in range(len(shuru)):
                if(shuru[a] in judge_shuzu):
                    num=num+1
                else:
                    break
            if(num==len(shuru)):
                print('存在:',sheet.cell_value(judge[0],1))

    print('执行完毕')
            
