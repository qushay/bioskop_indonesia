from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from flask import Flask, jsonify

app = Flask(__name__)
data = []

@app.route('/now', methods=['GET'])
def get_now():
    result = []
    for movie in data:
        jmovie = {
            'name': movie[0],
            'url': movie[1]
        }
        result.append(jmovie)
    return jsonify({'data':result})

class runSelenium(object):
    def __init__(self):
        # define a class attribute
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def isElementPresent(self, locator):
        try:
            self.driver.find_element_by_xpath(locator)
        except NoSuchElementException:
            return False
        return True

    def getJsonData(self,title,url):
        movie = {
            'name': title,
            'url': url
        }
        return movie
    
    def getElementData(self):
        html_list = self.driver.find_element_by_id("mvlist")
        movies = html_list.find_elements_by_tag_name("li")
        for result in movies:
            movie = result.find_element_by_xpath('.//div/h3/a')
            title = movie.text
            url = movie.get_attribute('href')
            print("{} ({})".format(title, url))
            data.append((title,url))
        self.goNextPage()

    def goNextPage(self):
        pagination = self.driver.find_element_by_id("top_pager")
        isElement = self.isElementPresent("//*[contains(text(), 'Next >>')]")
        if isElement:
            next_page = pagination.find_element_by_xpath("//a[contains(text(), 'Next >>')]")
            next_page.click()
            self.getElementData()   

    def selenium(self):
        self.driver.get("http://www.21cineplex.com/nowplaying")
        link_class = self.driver.find_element_by_class_name("mn2")
        link = link_class.find_element_by_xpath('.//a')
        link.click()

        self.getElementData()
        self.driver.quit()

if __name__ == '__main__':
    run = runSelenium()
    run.selenium()
    app.run(debug=False,host='0.0.0.0')