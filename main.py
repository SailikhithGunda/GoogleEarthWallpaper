#Modules required
import glob
import os
import time
from wallpaper import set_wallpaper, get_wallpaper
from selenium import webdriver
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

# setting the download folder 
options = webdriver.ChromeOptions() 
prefs = {'download.default_directory' : 'C:\\Users\\Likhith\\Desktop\\wallpapers\\Auto'}
options.add_argument("--headless")
options.add_experimental_option('prefs', prefs)

# visiting the website
driver = webdriver.Chrome(options=options)
driver.get("https://earthview.withgoogle.com/")

# downloading the image
element = driver.find_element_by_xpath('//*[@title="Explore Earth Views"]').click()
action = ActionChains(driver) 
action.click(on_element = element) 
action.perform()

element = driver.find_element_by_xpath('//*[@title="Download Wallpaper"]').click()
action = ActionChains(driver) 
action.click(on_element = element) 
action.perform()

time.sleep(5)
# Getting the most recent image downloaded
temt = driver.title
def latest_download_file():
    path = r'C:\Users\Likhith\Desktop\wallpapers\Auto'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]
    return newest

file = latest_download_file()

fileends = "crdownload"
while "crdownload" == fileends:
    time.sleep(1)
    if "crdownload" in file:
        fileends = "crdownload"
    else:
        fileends = "none"
        driver.close()

# renaming the file with its geo-location
text = list(temt.split("–"))
text2 = str(text[0])
a = text2.replace(", ", "_")
b = a.replace(" ", "")
new = r'C:\Users\Likhith\Desktop\wallpapers\Auto\{0}.jpg'.format(b)
os.rename(file,new)

# setting the downloaded image as wallpaper
set_wallpaper(new)
