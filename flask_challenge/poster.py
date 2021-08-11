import requests

# the URL you wish to post to
url = 'http://10.8.77.34:2224/correct'

# the data you wish to post
ye_olde_dict = {'answer': 'squall'}

x = requests.post(url, data = ye_olde_dict)

print(x.text)
