from urllib.request import urlopen
import os

# for pythn 3.9 under pure IPv6 network
proxy = 'http://kmolab:kmolab10@[2001:288:6004:17::42]:3128'
  
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

cd_2a= "https://nfulist.herokuapp.com/?semester=1102&courseno=0752&column=True"

f = urlopen(cd_2a)
# decode, split and drop the last vacent element
data = f.read().decode().split("</br>")[:-1]
#print(myfile)
for i in data:
    print(i)
