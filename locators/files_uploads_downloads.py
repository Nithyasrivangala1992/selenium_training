'''upload single file'''
from locators.xpath import driver

# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# #file_path = r'"C:\Users\91949\Desktop\signup.html"'
# file_path = r'C:\Users\91949\Desktop\signup.html'
# driver.find_element('xpath','//input[@id="singleFileInput"]').send_keys(file_path)

'''upload Multiple files'''
# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# file1 = r'C:\Users\91949\PycharmProjects\selenium_training\locators\linktext.py'
# file2 = r'C:\Users\91949\PycharmProjects\selenium_training\locators\xpathattributes.py'
# file3 = r'C:\Users\91949\Desktop\signup.html'
# driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}')


'''Upload download files'''
# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get('https://demoqa.com/upload-download')
# driver.find_element('xpath', '//a[text()="Download"]').click()

##Chrome
# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# prefs = {
#     "download.default_directory":r"C:\Users\91949\PycharmProjects\selenium_training\locators_",
#     "download.prompt_for_download":False,
#     "safebrowsing.enabled":True,
#     "plugins.always_open_pdf_externally":True
# }
# opts.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(opts)
# driver.get('https://demoqa.com/upload-download')
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Download"]').click()

'''
download.default_directory  -->     Sets the folder where the downloaded files will be stored
download.prompt_for_download    --> 
safebrowsing.enabled    -->     Enables Chromes's safe browsing so it doesnt block the download
'''

##----------------------------------------------------------------------------

## Firefox
import time
from selenium import webdriver
opts = webdriver.FirefoxOptions()
opts.set_preference("browser.download.folderList", 2)
opts.set_preference("browser.download.dir", r"C:\Users\91949\PycharmProjects\selenium_training\locators_")
opts.set_preference("pdfjs.disabled", True)
driver = webdriver.Firefox(opts)
driver.get('https://demoqa.com/upload-download')
time.sleep(2)
driver.find_element('xpath', '//a[text()="Download"]').click()

