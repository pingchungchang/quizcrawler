from xml.sax import default_parser_list
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import maskpass

class Q:
    def __init__(self):
        self.title = 'UN'
        self.tpe = 'UN'
        self.ans = 'UN'
ansurl = 'https://docs.google.com/forms/d/e/1FAIpQLSegyf-MI5anXBWz8l1BWC7VfhPeB3S7zlrzdeo5a14TZyyOAA/viewscore?viewscore=AE0zAgCbk8sdnMXCuigucnVfqClfiLCS4LIrEQ5XbfT3qs3v3rflicc_EL5E4QIGyJgowJs'
formurl = 'https://docs.google.com/forms/d/e/1FAIpQLSegyf-MI5anXBWz8l1BWC7VfhPeB3S7zlrzdeo5a14TZyyOAA/viewform?hr_submission=ChkIvsOd5-YKEhAI18nrm-0PEgcIhoa65-YKEAA'
email = 'ck1100890@gl.ck.tp.edu.tw'
password = 'hjecha1018'


chrome = webdriver.Chrome('./chromedriver')
def Login():
    global email,password
    chrome.get('https://accounts.google.com/v3/signin/identifier?dsh=S-972875933%3A1672013913036171&hl=zh-tw&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh6IJsqhC3os63jQ9MkZ2jtQJNLUYO1qh5WOTOs-_ezdN_HpCqAcDI6UUqX-MjuTm_K5nvF7')
    usrname = chrome.find_element_by_id('identifierId')
    usrname.send_keys(email)
    usrname.send_keys(Keys.ENTER)
    input('press enter when at password page')
    psw = chrome.find_element_by_name('Passwd')
    psw.send_keys(password)
    psw.send_keys(Keys.ENTER)

def GetAns(url):
    global ansurl
    chrome.get(ansurl)
    input('press enter when done')
    soup = BeautifulSoup(chrome.page_source,'html.parser')
    arr = []
    details = soup.find_all('script')[4].string
    print(soup.text)
    print(len(details))

    with open("output.txt", mode = "w", encoding = "utf-8") as file: file.write(details)

    return;
def FillAns(url):
    return;

def WaitForKey():
    input('press enter to continue')
if __name__ == '__main__':
    Login()
    WaitForKey()
    GetAns(ansurl)
    WaitForKey()
    FillAns(formurl)
