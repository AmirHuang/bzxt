from django.test import TestCase

# Create your tests here.

a = 'http://sense-hn1-ad.oss-cn-shenzhen.aliyuncs.com/862ec0ec8382e6a8133c42d9aac3ecde?Expires=1575162683&OSSAccessKeyId=LTAIX9G5qsIV7aRa&Signature=SV3pLBT5p5JwFwL3SVj%2B%2BNm%2B4qg%3D'
b = 'http://oss-senseu.sensetime.com'

c = a.replace('http://sense-hn1-ad.oss-cn-shenzhen.aliyuncs.com', b)
print(c)