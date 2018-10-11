import urllib.request
import urllib.parse
import json
import time


def translate_main(content):
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data={
    'i':content,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1505743291468',
    'sign':'046c30617c7cf09170ed77e4bc751686',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTIME',
    'typoResult':'true'
    }

    data1=urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url,data1)
    html=response.read()
    target=json.loads(html)

    return target['translateResult'][0][0]['tgt']

    print('Result：'+target['translateResult'][0][0]['tgt']+'\n')
    time.sleep(pause)

if __name__=="__main__":
    while True:
        content = input("Input cotent to translate('q' for quit): ")
        if content=='q':
            print('\nquit translating')
            break

        result = translate_main(content)
        print('Result：' + result + '\n')
        time.sleep(0.1)
    