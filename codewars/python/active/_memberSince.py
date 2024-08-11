# https://www.codewars.com/kata/58ab2ed1acbab2eacc00010e/train/python
# Scraping: Get the Year a CodeWarrior Joined

import urllib.request

def get_member_since(username):
    ans = urllib.request.urlopen('https://www.codewars.com/users/'+username)
    r = ans.read().decode('utf-8','ignore')
    pos = r.find("Member Since:") + 17
    return r[pos:pos+8]

print(get_member_since("jhoffner")  )
print(get_member_since("Sascha%20Zapf")  )

"""

>>> get_member_since('dpleshkov')
Jul 2016
>>> get_member_since('jhoffner')
Oct 2012
urllib.request.urlopen: Opens up a webpage.

"""