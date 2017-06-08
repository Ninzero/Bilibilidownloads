import requests,re

if __name__ == "__main__":
    url = 'http://www.bilibili.com/video/av4722660/'
    avnum = re.search(r'av\d{5,10}',url).group()[2:]
    url_get = requests.get(url).text
    res = r'/video/av{0}/index_{1}.html'.format(avnum,r'\d{1,3}')
    cpl = re.compile(res)
    st = 1
    ur = []
    while True:
        sea = cpl.search(url_get,st)
        if sea == None:
            break
        ur.append(sea.group())
        st = sea.end()
    for x in ur:
        rl = 'http://www.bilibili.com{0}'.format(x)
        print(rl)
