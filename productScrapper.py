from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Product:

    def __init__(self,brand,name):
        self.brand = brand
        if "double knit" in name:
            self.name = name.replace("double knit", "DK")
        else:
            self.name = name
        self.price = ""
        self.delivery_time = ""
        self.needle_size = ""
        self.composition = ""

    def getdata(self):
        try:
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("https://www.wollplatz.de/")
            driver.maximize_window()
            driver.find_element_by_xpath('//*[@id="searchSooqrTop"]').send_keys(self.brand+" "+self.name)
            driver.implicitly_wait(5)
            driver.find_element_by_id("AcceptReload").click()
            driver.implicitly_wait(5)
            link = driver.find_element_by_xpath("//*[@title='" + self.brand + " " + self.name + "']").get_property('href')
            driver.get(link)
            driver.implicitly_wait(5)
            self.price = driver.find_element_by_class_name("product-price").text[2:].replace(',','.')
            l = driver.find_elements_by_xpath ("//*[@id='pdetailTableSpecs']/table")
            for i in l:
                data = (i.text).split("\n")
            for d in data:
                if "Zusammenstellung" in d:
                    self.composition = " ".join(d.split(" ")[1:])
                if "Nadelstärke" in d:
                    self.needle_size = " ".join(d.split(" ")[1:])
            self.delivery_time = "2-3 Days"
        except:
            self.price = "Not Available"
            self.delivery_time = "Not Available"
            self.needle_size = "Not Available"
            self.composition = "Not Available"