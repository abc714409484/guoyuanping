import requests
class test_httprequest:
    def request_1(self,url):
        self.url=url
        res=requests.get(url)
        return res
if __name__ == '__main__':
    url='http://www.baidu.com'
    res=test_httprequest().request_1(url)
    print(res.cookies)
    print(res.status_code)
