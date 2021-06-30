import random
print(input('开始运行《帮你做选择》小程序，我们来看看今天吃什么呐！请按回车继续！'))
materials = []
material = input('我们现在的食材有：')
dishes = {'酱茄子':['蒜', '茄子','辣椒','肉末','葱'], '番茄炒鸡蛋':['鸡蛋','葱','蒜','辣椒','番茄'], '虎皮青椒': ['辣椒', '蒜', '豆豉'], '炒南瓜':['南瓜', '大蒜', '辣椒'], '炒冬瓜':['冬瓜','虾仁','葱'], '炖鸡汤': ['母鸡','葱']}
while True:
    others = input('请问还有别的食材需要添加吗？请回答:是or不用')
    if others == '是':
        more = input('请输入需要添加的食材:')
        materials.append(more)
    else:
        break
materials.append(material)
#print('我们现在有的食材是'+(','.join(materials))
#print('我们已有的菜品是:' + .join(dishes))

for i in dishes:
    a = dishes[i]
    if a in materials:
        dish=random.choice(dishes)
        print('为您挑选了：'+ dish)
        good = input('请问您满意这个为您挑选的菜品吗？（请回答：满意or不满意）')
        if good == '满意':
            print('祝您用餐愉快!')
            break
        else:
            continue
    else:
        print('对不起哦，你有的材料不在菜单所需材料中')
        continue
        
        