import logging
from mod.driver import ChromeDriver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # 1. Define process constants
    ARTICLES_SOURCE_URL = "https://www.bbc.com/news/business"
    SELECTOR_ARTICLE = "//div[@class='gs-c-promo gs-t-News nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline gs-c-promo--stacked@xl gs-c-promo--flex']"    
    
    # 2. Start driver
    driver = ChromeDriver()
    
    # 3. Generate the source URL of business articles
    driver.get_article_routes(ARTICLES_SOURCE_URL, SELECTOR_ARTICLE)
    logger.info("Article routes generated!")

    # 4. Export to JSON file each article in driver.article_routes
    driver.export_content()
    logger.info("Generating article content files...")

if __name__ == "__main__":
    print(main())