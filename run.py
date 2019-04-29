from tools.test import test_httprequest
url='http://www.baidu.com'
res=test_httprequest().request_1(url)
print(res.cookies)
print(res.status_code)