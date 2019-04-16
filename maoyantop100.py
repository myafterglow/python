#################################################################
####################【公众号: PyShadow】#########################
#################################################################

import requests,re,time
# 导入必用的三个模块

z=re.compile('<dd>[\s\S]*?img.*?data-src="(.*?)".*?alt="(.*?)"[\s\S]*?<p.*?class="star">'
           +'([\s\S]*?)</p>[\s\S]*?<p.*?releasetime">上映时间：(.*?)</p>[\s\S]*?class="integer">'
            '+(.*?)</i><.*?class="fraction">(.*?)<[\s\S]*?</dd>')
# 设置模式对象，以便后面循环调用

def getpage(page):
    return requests.get('https://maoyan.com/board/4?offset='+page).text
# 定义getpage函数，通过传入页面参数，使其返回每个页面的源码

def getdata():
# 定义getdata函数，直接获取我们想要的数据
    p=10
    n=0
    for j in range(10):
        res=getpage(str(p*j))
        # 调用getpage函数，利用for循环传入page参数，使其获取每个页面的源码，并赋值给 res 变量
        a = re.findall(z,res)
        # 返回 源代码 中所有与 z 相匹配的全部字串，返回形式为数组

        for i in a:
            n += 1
            content='\nno.'+str(n)+'\n图片链接:'+i[0]+'\n电影:'+i[1]+'\n'+i[2].strip()+'\n上映时间:'+i[3]+'\n评分:'+i[4]+i[5]+'\n'
            # 把for循环得到的子匹配文本赋值给content变量
            with open('maoyan.txt','a') as f:
                f.write(content)
                # 每次循环完毕后，写入到同目录下的'maoyan.txt'文件，切记要修改参数为'a'，否则每次都覆盖写出
        # 利用 for 循环，获取匹配到的数据，并写出到文件
        print('已经采集到第 '+str(j+1)+' 页...')
        # 打印出当前进度
        time.sleep(2)
        # 猫眼有反爬虫，所以这里设置休息时间

if __name__=='__main__':
    getdata()
    print('采集完毕！')