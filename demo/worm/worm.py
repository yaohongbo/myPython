import urllib2
import re
import os

class Spider:
    def __init__(self):
        self.siteUrl = "http://tieba.baidu.com/p/2460150866"
        self.count = 1

    def get_page(self):
        html = urllib2.urlopen(self.siteUrl)
        page = html.read()
        print page
        return page

    def get_image(self, page):
        # src is the beginning ,pic_ext is the end
        reg = r'src="(.+?\.jpg)" pic_ext'
        image = re.compile(reg)
        img_list = re.findall(image, page)
        return img_list

    def save_image(self, image):
        file_name = str(self.count) + ".jpg"
        path = r"F:\test\test" + file_name
        # path.decode('utf8')
        print "Downloading %s image" % self.count
        u = urllib2.urlopen(image)
        data = u.read()
        with open(path, 'wb') as code:
            code.write(data)
        self.count += 1


spider = Spider()
images = spider.get_image(spider.get_page())
for image in images:
    spider.save_image(image)

