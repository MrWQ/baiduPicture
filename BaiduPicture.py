import re,requests,os,json,threading


# rn表示图片个数，最大60张
# pn表示从第几张图片开始
# word表示关键字
# 必填字段tn=resultjson_com，ipn=rj，确保编码字段ie,oe虽然编码不影响，以防万一还是用上
# https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ie=utf-8&oe=utf-8&word=炮姐&pn=0&rn=2
# 从第0张图片开始，返回包含2张（即0与1的图片）数据的json 注：实际返回的json中data列表中包含3个，最后一个为空，前两个为第0与1图片的对象




if __name__== '__main__':
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ie=utf-8&oe=utf-8&word=炮姐&pn=0&rn=2'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'}
    text = requests.get(url=url,headers=headers).text
    # print(text)
    jsonobj = json.loads(text)
    data =jsonobj['data']
    # print(data)
    # print(type(data))
    # print(len(data))
    # 获取所有图片的url，组成list
    pictureList =[]
    for i in range(0,len(data)-1):
        # print(i)
        data0 = data[i]
        pictureList.append(data0['thumbURL'])
    print(pictureList)
    for count in range(0,len(pictureList)):
        eachUrl = pictureList[count]
        content= requests.get(url=eachUrl,headers=headers).content
        name = str(count)
        type ='.jpg'
        f= open(name+type,'wb')
        f.write(content)
        f.close()