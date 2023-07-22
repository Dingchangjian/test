import json

# 打开JSON文件
with open('thumos_anno_eval.json', 'r') as f:
    # 读取文件内容
    data = json.load(f)
data =data['database']
num_0 =0
num_1 =0
num_2 =0
num_3=0
num_4=0
for key in data:
    an = data[key]['annotations'] 
    for i in an:
        l = (i['segment'][1] - i['segment'][0])*28
        if (l>0 and l<=30):
            num_0+=1
        if (l>30 and l<=60):
            num_1+=1
        if (l>60 and l<=120):
            num_2+=1
        if (l>120 and l<=180):
            num_3+=1
        if (l>180):
            num_4+=1
print(num_0)
print(num_1)
print(num_2)
print(num_3)
print(num_4)



