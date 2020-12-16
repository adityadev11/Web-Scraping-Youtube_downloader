import bs4,requests
import webbrowser,re,time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

inp=input('Enter your search: ')
a='https://www.youtube.com/results?search_query='
inp=inp.replace(' ','+')
final=a+inp
print(final)

txt=requests.get(final).text
soup=bs4.BeautifulSoup(txt,features="html.parser")

tgt_list = [a['href'] for a in soup.find_all('a', href=True)]
tgt_list = [n for n in tgt_list if re.search('watch',n)]
new=('https://youtube.com'+tgt_list[0])
print(new)

chromedriver = "C:\\Users\\crazy\\Desktop\\chromedriver"
print(chromedriver)
browser=webdriver.Chrome(chromedriver)
browser.get(final)
browser.get(new)
browser.get('https://ytmp3.cc/en13/')
songurl = browser.find_element_by_id("input")
songurl.send_keys(new)
submit = browser.find_element_by_id("submit")
submit.click()

element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")))

element.click()




