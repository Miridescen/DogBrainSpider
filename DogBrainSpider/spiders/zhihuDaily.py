import scrapy

from DogBrainSpider import items

class zhihuDaily(scrapy.Spider):

    name = 'zhihuDaily'
    start_urls = [
        'http://daily.zhihu.com/',
        'https://www.ifanr.com/',
        'https://www.toodaylab.com/'

    ]



    def parse(self, response):

        item = items.DogbrainspiderItem()
        if response.url == 'http://daily.zhihu.com/':

            basurl = response.url
            boxs = response.xpath("//div[@class='box']")

            boxs.reverse()

            for box in boxs:

                item['media'] = '知乎日报'.encode('utf-8')
                item['media_url'] = basurl

                url = box.xpath("a/@href").extract_first()
                if url:
                    item["url"] = url.encode('utf-8')
                    item['full_url'] = ('http://daily.zhihu.com' + url).encode('utf-8')

                title = box.xpath("a//span[@class='title']/text()").extract_first()
                if title:
                    item['title'] = title.encode('utf-8')

                image_url = box.xpath("a//img/@src").extract_first()
                if image_url:
                    item['image_url'] = image_url.encode('utf-8')

                # print(item)

                yield item

        if response.url == 'https://www.ifanr.com/':

            basurl = response.url
            boxs = response.xpath("//div[@class='article-item article-item--list ']")
            boxs.reverse()

            for box in boxs:

                item['media'] = '爱范儿'.encode('utf-8')
                item['media_url'] = basurl

                url = box.xpath("div[@class='article-info js-transform']//h3//a/@href").extract_first()
                if url:
                    item["url"] = url.encode('utf-8')
                    item['full_url'] = url.encode('utf-8')

                title = box.xpath("div[@class='article-info js-transform']//h3//a/text()").extract_first()
                if title:
                    item['title'] = title.encode('utf-8')

                image_url = box.xpath("div[@class='article-image cover-image']//a[@class='article-link cover-block']/@style").extract_first()
                if image_url:
                    subStrArr = image_url.split("'")
                    if len(subStrArr) >= 3:
                        item['image_url'] = subStrArr[1].encode('utf-8')

                # print(item)

                yield item

        if response.url == 'https://www.toodaylab.com/':

            basurl = response.url
            boxs = response.xpath("//div[@class='single-post clearfix']")
            boxs.reverse()


            for box in boxs:

                item['media'] = '理想生活实验室'.encode('utf-8')
                item['media_url'] = basurl

                url = box.xpath("div[@class='post-info']//p[@class='title']//a/@href").extract_first()
                if url:
                    item["url"] = url.encode('utf-8')
                    item['full_url'] = ('https://www.toodaylab.com' + url).encode('utf-8')

                title = box.xpath("div[@class='post-info']//p[@class='title']//a/text()").extract_first()
                if title:
                    item['title'] = title.encode('utf-8')

                image_url = box.xpath("div[@class='post-pic']//a[@class='slide']/@style").extract_first()
                if image_url:
                    subStrArr = image_url.split("url")
                    if len(subStrArr) >= 2:
                        originalStr = subStrArr[1][1:-1]
                        if originalStr.startswith('http'):
                            item['image_url'] = originalStr.encode('utf-8')
                        else:
                            item['image_url'] = ('http:' + originalStr).encode('utf-8')


                print(item)

                yield item




