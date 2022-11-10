

import urllib
import urllib3
import  requests
url = "http://qa-soda-static.snow.me/soda/style/101443/101443_8.zip"
download_path = "a.zip"
# style id /
#result_file_path, header = urllib.urlretrieve(url, download_path)
r= requests.get(url, stream=True)
with open(download_path, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)



