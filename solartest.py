##
import urllib2

var target_url = http://pvoutput.org/service/r2/getstatus.jsp?sid=41079&key=333e82f10971475dc09a0e88ee4a78eaf13f4a66
for line in urllib2.urlopen(target_url):
    print line
