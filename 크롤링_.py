from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

start = time.time()
#검색 키워드 설정
keyword = '과일'
#저장할 디렉토리 설정
target_dir = '../Train_4데이터량일치/_garbage/'


##웹 브라우저 실행
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

##스크롤
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try :
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

count = 0
times = 0
beforeoccur = time.time()

for image in images:

    try : 
        image.click()
        driver.implicitly_wait(10)
        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, target_dir + '/'+ str(count) + ".jpg")

        print(str(count)+"번째 이미지 저장완료")
        count += 1
        
    except ElementClickInterceptedException:
        print("ECIE error at : "+str(count))
        if((time.time() - beforeoccur) < 7):
            time.sleep(5)
            beforeoccur = time.time()
        else:
            time.sleep(2)
        continue

    except NoSuchElementException:
        print("NSEE error at : "+str(count))
        count -= 1
        continue
    
    except ElementNotInteractableException:
        print("ENIE error at : "+str(count))
        init_count = count
        init_times = times
        if((init_count == count)&((times-init_times)>3)):
            count += 1
        times += 1
        time.sleep(5)
        continue
    
    times=0


t = time.time()-start
driver.close()

print(keyword+" 이미지 크롤링 완료")
print("소요된 시간 : {0} min {1} sec".format(int(t/60), int(t%60))) 


