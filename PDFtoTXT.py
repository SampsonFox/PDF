# coding = utf-8
import sys
import pdfplumber
import json
import xlrd

#读取pdf文件
url = 'D:/OneDrive - The University of Melbourne/Unimelb_S2_done/000_Intership/笔试/新致软件-复星集团/PDF.pdf'
pdf = pdfplumber.open(url)
page = pdf.pages[0]
table_1 = page.extract_table()

#得到纳税人名称和纳税人识别号
word_1 = page.extract_text(x_tolerance=0, y_tolerance=0)
name_code = word_1[32:]
comp_name = {}
comp_code = {}
comp_period = {}
print(table_1)

# 判断公司名字是否结束
# 返回公司名称和代码
for i in range(len(name_code)):
    if word_1[i] == '纳':
        comp_name['TaxpayerName'] = name_code[i-6:i+6]
        comp_code['TaxpayerCode'] = name_code[i+14:i+32]
        comp_period['period'] = name_code[i+69:i+77]

        for i in table_1:
            with open('chart.json','w') as c:
                json.dump(comp_name,c)
                json.dump(comp_code,c)
                json.dump(comp_period,c)

        break

# 打开Excel文件读取数据每个格子的名字
# 由于直接在excel中读取格子名称较为困难，所以这里 PDF_1.xls 中手动把格子名字放到了格子上
data = xlrd.open_workbook('D:/OneDrive - The University of Melbourne/Unimelb_S2_done/000_Intership/笔试/新致软件-复星集团/PDF_1.xls')

# 合并数据和格子名字
#选取需要的表格
sheet_name_1 = data.sheet_names()[-2]
sheet_1 = data.sheet_by_name(sheet_name_1)

line_count = 0

# 找到所需要数字在数组中的位置
# 建立行列计数器
position = [4,5,6,8]
line_count = 0
colum_count = 4
#建立后面的data字典
data = {}

#逐行遍历从pdf文件扒下来的表格并和excel里面读取的数据组成字典
try:
    for line in table_1:
        if line_count >= 5:
            colum_count = 3
            for pos in position:
                #print(sheet_1.cell(line_count,colum_count).value)
                data[str(sheet_1.cell(line_count,colum_count).value)] = line[pos]
                colum_count += 1
        print(data)

        line_count += 1

except:
    with open('chart.json','a') as c:
        json.dump(data,c)

