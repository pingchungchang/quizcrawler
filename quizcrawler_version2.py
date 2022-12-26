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
        self.ans = []
ansurl = 'https://docs.google.com/forms/d/e/1FAIpQLSfTOgVK3fmXrUGOJAHfny4AteeJHK4P35J98RKThfITgalRfA/viewanalytics'
ansurl = 'https://docs.google.com/forms/d/e/1FAIpQLSch4RRpXGUeCN4PArZg0b3KbSj4tZVCsiDX9j7n5bJ2Ggv3yA/viewanalytics'
formurl = 'https://docs.google.com/forms/d/e/1FAIpQLSegyf-MI5anXBWz8l1BWC7VfhPeB3S7zlrzdeo5a14TZyyOAA/viewform?hr_submission=ChkIvsOd5-YKEhAI18nrm-0PEgcIhoa65-YKEAA'
formurl = 'https://docs.google.com/forms/d/e/1FAIpQLSch4RRpXGUeCN4PArZg0b3KbSj4tZVCsiDX9j7n5bJ2Ggv3yA/viewform'
email = 'ck1100890@gl.ck.tp.edu.tw'
password = 'hjecha1018'
titleclass = 'M7eMe'


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
    global chrome
    chrome.get(url)
    input('press enter when done')
    soup = BeautifulSoup(chrome.page_source,'html.parser')
    arr = []
    details = soup.find_all(class_ = 'Aovyg')
    dels = []
    for i in range(len(details)):
        if len(details[i].find_all('table')) == 0 and len(details[i].find_all(class_ = 'NC79P')) == 0:
            dels.append(i);
    dels.reverse()
    for i in dels:
        details.pop(i)
    print(len(details))
    for i in details:
        print(i.text)
        print('')

    for i in details:
        tmp = Q()
        tmp.title = i.find(class_ = 'myXFAc RjsPE').text.replace(u'\xa0',u' ')
        print(tmp.title)
        isbox = False
        if i.find('table') != None:
            for j in i.find('table').find('tbody').find_all('tr'):
                tmp.ans.append([])
                for k in j.find_all('td'):
                    tmp.ans[-1].append(k.text)
                if len(tmp.ans[-1]) >2:
                    isbox = True
        else:
            tmp.tpe = 'long'
            tmp.ans = i.find(class_='NC79P').text+' ';
        if isbox:
            tmp.tpe = 'box'
            choices = []
            for j in i.find('table').find('thead').find_all('th'):
                if len(j.text) == 0:
                    continue
                choices.append(j.text)
            for j in range(len(tmp.ans)):
                biggest = 1
                for k in range(1,len(tmp.ans[j]),1):
                    if int(tmp.ans[j][k])>int(tmp.ans[j][biggest]):
                        biggest = k
                tmp.ans[j] = [tmp.ans[j][0],biggest-1]
        arr.append(tmp);
    for i in arr:
        print(i.tpe,i.ans)
        print('')
    return arr

def WaitForKey():
    input('press enter to continue')
    return;

def FillIn(now,re):
    global chrome
    print(re.tpe)
    if re.tpe == 'long':
        blank = now.find_element_by_class_name('KHxj8b tL9Q4c')
        blank.send_keys(re.ans)
    elif re.tpe == 'box':
        rows = now.find_elements_by_class_name('ssX1Bd')
        rows.pop(0)
        rows.pop(0)
        print(len(rows))
        for i in rows:
            choices = i.find_elements_by_xpath('.//[@click]')
            print(len(choices))
            for j in choices:
                print(j.text)
            print()
            choices[int(re.ans[0][1])].click()
            re.ans.pop(0)
    elif len(now.find_elements_by_class_name('docssharedWizToggleLabeledContainer Yri8Nb')) > 0:
        re.tpe = 'multi';
        choices = []
        big = 0;
        for i in re.ans:
            big = max(big,int(i[1]))
        for i in re.ans:
            if int(i[1])>big*0.8:
                choices.append(i[0])
        selections = i.find_elements_by_xpath('.//*[@role="list"]//label')
        for i in selections:
            if i.find_element_by_class_name('ulDsOb').text in choices:
                button = i.find_element_by_xpath('.//*[@id]')
                button.click()
    elif len(now.find_elements_by_class_name('docssharedWizToggleLabeledContainer ajBQVb')) > 0:
        re.tpe = 'choice'
        big = re.ans[0];
        for i in re.ans:
            if int(big[1])<int(i[1]):
                big = i
        # print('choice in')
        selections = now.find_elements_by_xpath('.//span//label')
        for i in selections:
            # print(k.find_element_by_class_name('ulDsOb').text)
            if i.find_element_by_class_name('ulDsOb').text == big[0]:
                button = k.find_element_by_xpath('.//*[@id]')
                button.click()        
    elif len(now.find_elements_by_class_name('jgvuAb ybOdnf cGN2le t9kgXb llrsB iWO5td')) > 0:
        re.tpe = 'list'
        big = re.ans[0]
        for i in re.ans:
            if int(big[1])<int(i[1]):
                big = i;
        # print('list in')
        first_one = now.find_element_by_xpath('.//*[@class = "MocG8c HZ3kWc mhLiyf LMgvRb KKjvXb DEh1R"]')
        first_one.send_keys(Keys.ENTER)
        time.sleep(0.3)
        # choices = i.find_elements_by_xpath('.//*[@class = "MocG8c HZ3kWc mhLiyf LMgvRb"]')
        choices = now.find_elements_by_xpath('.//*[@class = "MocG8c HZ3kWc mhLiyf OIC90c LMgvRb"]')
        for c in choices:
            # print(c.find_element_by_xpath('.//span').text)
            if c.find_element_by_xpath('.//span').text == big[0]:
                c.send_keys(Keys.ENTER)
    elif len(now.find_elements_by_class_name('whsOnd zHQkBf')) > 0:
        re.tpe = 'cloze'
        big =re.ans[0];
        for i in re.ans:
            if int(big[1])<int(i[1]):
                big = i
        blank = now.find_element_by_xpath('.//input')
        blank.send_keys(Keys.BACK_SPACE)
        blank.send_keys(big[0])
        blank.send_keys(Keys.ENTER)
    else:
        print("ERROR")
    return
        
def FillAns(url,refer):
    global chrome
    chrome.get(url)
    WaitForKey()
    all = chrome.find_elements_by_class_name('Qr7Oae')
    for now in all:
        tar = now.find_element_by_class_name(titleclass).text.replace(u'\xa0',u' ')
        tar = tar.replace(u'\n',u'')
        for j in range(len(refer)):
            if refer[j].title == tar:
                FillIn(now,refer[j])
                refer.pop(j)
                break
    return

if __name__ == '__main__':
    Login()
    WaitForKey()
    arr = GetAns(ansurl)
    WaitForKey()
    FillAns(formurl,arr)
