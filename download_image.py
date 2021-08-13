import sys
import source.mangabz_spider as spider
import source.config as config

if __name__ == '__main__':
    name, main_page_url, root_path = config.readConf()
    spider.download_image(main_page_url, name, root_path)