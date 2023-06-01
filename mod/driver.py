import logging
import json
import threading
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger()

class ChromeDriver:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_article_routes(self, source_url, xpath_selector):
        """ Queries the source URL and creates a JSON file in the
            specified filename

            :param source_url: which URL to lookup for the targets
            :param xpath_selector: selector used to lookup for anchor tags
        """
        self.driver.get(source_url)
        elements = self.driver.find_elements(By.XPATH, xpath_selector)    
        article_routes = []
        for el in elements:
            a = el.find_element(By.CSS_SELECTOR, "a")
            route = a.get_attribute("href")
            article_routes.append(route)

        self.article_routes = article_routes
    
    def get_article_content(self, wait, source, filename):
        """ Queries the source URL and creates a JSON file in the
            specified filename

            :param wait: webdriverwait object
            :param source: URL source of the searched data
            :param filename: filename to output the results
        """
        self.driver.get(source)
        page_title = self.driver.title
        main_content = wait.until(EC.visibility_of_element_located((By.ID, "main-content")))
        p_text = main_content.find_elements(By.CSS_SELECTOR, "p")
        content = []
        for p in p_text:
            content.append(p.text)
        
        data = {page_title: "\n ".join(content)}
        self.driver.quit()
        with open(filename, "w+", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            logger.info(f"File for {filename} generated succesfully!")

    def export_content(self):
        """ Iterates over self.article_routes and threads
            the process of getting the article data into json file
        """
        wait = WebDriverWait(self.driver, 10)
        for route in self.article_routes:
            # generate filename
            url = route.rstrip('/')
            parts = url.split('-')
            last_part = parts[-1]
            digits = ''.join(filter(str.isdigit, last_part))
            filename = f"results/{digits}.json"

            # if file doesn't exists start the thread
            if not os.path.exists(filename):
                # thread the process
                thread = threading.Thread(target=self.get_article_content, args=(wait, route, filename))
                thread.start()