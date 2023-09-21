import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


PATH = '/Applications/chromedriver'
driver = webdriver.Chrome(PATH)


def page_loader(url, iteration_num):

    driver.get(url)

    for i in range(iteration_num):
        try:
            time.sleep(2)
            try:
                button = driver.find_element(By.XPATH, "//button[text()='Load More']")
                print(button.text)
                button.click()
            except:
                print(i)
            time.sleep(10)
        except Exception as e:
            print(e)
            break
    print("Complete!")
    time.sleep(5)


def crawler(movie_num, url):
    if movie_num == 1:
        page_loader(url, 200)
    if movie_num == 2:
        page_loader(url, 120)
    if movie_num == 3:
        page_loader(url, 40)
    scores = driver.find_elements(By.XPATH, '//span[@class="rating-other-user-rating"]/span[1]')
    print('number of scores retrieved:', len(scores))

    dates = driver.find_elements(By.XPATH, '//span[@class="review-date"]')
    print('number of dates retrieved:', len(dates))

    criticisms = driver.find_elements(By.XPATH, '//div[@class="text show-more__control"]')
    print('number of Criticisms retrieved:', len(criticisms))

    spoilers = driver.find_elements(By.XPATH, '//span[@class="spoiler-warning"]')
    print('number of Spoilers retrieved:', len(spoilers))

    f = open('Dataset/scores_' + str(movie_num) + '.txt', 'w', encoding='utf-8')
    for score in scores:
        f.write(f'{score.text}\n')
    f.close()

    f = open('Dataset/dates_' + str(movie_num) + '.txt', 'w', encoding='utf-8')
    for date in dates:
        f.write(f'{date.text}\n')
    f.close()

    f = open('Dataset/criticisms_' + str(movie_num) + '.txt', 'w', encoding='utf-8')
    for crit in criticisms:
        f.write(f'{crit.text}\n')
    f.close()

    f = open('Dataset/spoilers_' + str(movie_num) + '.txt', 'w', encoding='utf-8')
    for spoiler in spoilers:
        f.write(f'{spoiler.text}\n')
    f.close()


godfather1_url = "https://www.imdb.com/title/tt0068646/reviews?ref_=tt_urv"
crawler(1, godfather1_url)

print("end 1")

godfather2_url = "https://www.imdb.com/title/tt0071562/reviews?ref_=tt_urv"
crawler(2, godfather2_url)

print("end 2")

godfather3_url = "https://www.imdb.com/title/tt0099674/reviews?ref_=tt_urv"
crawler(3, godfather3_url)

print("end 3")