import httplib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  

conn = httplib.HTTPSConnection("localhost", port=8888, key_file='./cert/client.crt')
conn.request('GET', '', body='payload')
retCreateCon = conn.getresponse()
print retCreateCon.read()