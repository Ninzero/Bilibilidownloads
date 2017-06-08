import requests,os,re

if __name__ == '__main__':
    url_input = input('请输入合集网址：')
    UserID = re.search(r'/\d{5,10}',url_input).group()[1:]
    CID = re.search(r'cid.\d{3,6}',url_input).group()[4:]
    url_try = 'http://space.bilibili.com/ajax/channel/getNewVideo?mid={0}&num=1&cid={1}&p=1'.format(UserID,CID)
    getURL_try = requests.get(url_try).json()
    channel_name = getURL_try['data']['channelInfo']['name']
    channel_num = getURL_try['data']['total']
    location = os.getcwd()+'/'+channel_name
    if not os.path.exists(location):
        os.mkdir(location)
    url = 'http://space.bilibili.com/ajax/channel/getNewVideo?mid={0}&num={1}&cid={2}&p=1'.format(UserID,channel_num,CID)
    getURL = requests.get(url).json()
    avnums = []
    for info in getURL['data']['list']:
        avnums.append(info['aid'])
    avnums=avnums[::-1]
    for avnum in avnums:
        url_video = 'http://www.bilibili.com/video/av{0}/'.format(avnum)
        command = 'cd {0}\nyou-get --debug {1}'.format(location,url_video)
        os.system(command)
