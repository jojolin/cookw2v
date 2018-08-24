# coding: utf8
'''
http://www.zhms.cn/cp/_1_1/
'''
import requests
import re
import logging
import time

DOMAIN = 'http://www.zhms.cn'

def gen_url():
    for i in range(1, 6889):
        yield 'http://www.zhms.cn/cp/_1_%s' % i
        # TODO: break
        # break

def crawl():
    dish_urls_fp = open('dish_urls.txt', 'w')
    zf_urls_fp = open('zf_urls.txt', 'w')
    dish_crawled = set()
    zf_crawled = set()

    for url in gen_url():
        logging.info('url: %s' % url)
        try:
            resp = requests.get(url)
            dish_urls = set(re.findall('href="/cp/\d+/"\>', resp.text))
            logging.debug(dish_urls)

            for dish_url in dish_urls:
                time.sleep(0.5)   # be polite

                dish_url = dish_url.split('"')[1]
                logging.info('dish_url: %s' % dish_url)
                dish_urls_fp.write(dish_url+'\n')
                if dish_url in dish_crawled:
                    continue

                zuofa_urls = set()
                for i in range(1, 100):
                    time.sleep(0.3)   # be polite
                    url2 = DOMAIN + dish_url + '0_%s' % i
                    logging.info('url2: %s' % url2)
                    resp2 = requests.get(url2)
                    zuofa_urls2 = set(re.findall('href="/zf/\d+.html"',resp2.text))

                    if len(zuofa_urls2) < 1:
                        break

                    zuofa_urls.update(zuofa_urls2)

                if len(zuofa_urls) < 1:
                    continue

                for zuofa_url in zuofa_urls:
                    zuofa_url = DOMAIN + zuofa_url.split('"')[1]
                    if zuofa_url in zf_crawled:
                        continue

                    zf_urls_fp.write(zuofa_url+'\n')

                    logging.info('zf url: %s' % zuofa_url)
                    # zf_resp = requests.get(zuofa_url)
                    # logging.info(zf_resp.text)

                    zf_crawled.add(zuofa_url)

                    # TODO: break
                    # break

                dish_crawled.add(dish_url)
                zf_urls_fp.flush()

            dish_urls_fp.flush()

        except Exception as ex:
            logging.error(ex)

    dish_urls_fp.close()
    zf_urls_fp.close()


def main():
    logging.basicConfig(level=logging.INFO)
    crawl()

if __name__ == '__main__':
    main()


