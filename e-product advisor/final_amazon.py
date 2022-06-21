from selenium import webdriver
import time
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from urllib. request import Request, urlopen
import requests
import budhii
import keyboard

lst=[]
list = []
i=1
j=1






def search(product,budget_min,budget_max):

    global i,j
    webpage = r"https://www.amazon.in/" # edit me
    driver = webdriver.Chrome("E:\driver\chromedriver.exe")
    driver.get(webpage)
    sbox = driver.find_element_by_xpath(r"//*[@id='twotabsearchtextbox']")
    sbox.send_keys(product)
    submit = driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
    submit.click()
    driver.find_element_by_xpath("//*[@id='low-price']").send_keys(budget_min)
    driver.find_element_by_xpath("//*[@id='high-price']").send_keys(budget_max)
    strUrl = driver.current_url

    driver.get(strUrl)
    driver.maximize_window()
    soup=BeautifulSoup(driver.page_source,"lxml")
    time.sleep(4)
    links =soup.find_all("a",class_="a-link-normal a-text-normal")
    for link in links:
        lst.append("https://www.amazon.in/" + link.get("href"))
    return([lst[0],lst[1],lst[2]])





def start(product,attributes , budget_min ,budget_max):
    fe = open("result.txt", "w")
    d = ""
    c = 0
    url = search(product+attributes,budget_min,budget_max)
    print(url)

    #lst_links(url)
    flip , ratings, pro_title , review = budhii.start1(url)
 # Making the website believe that you are accessing it using a mozilla browser.
    webpage = requests.get(flip, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close",
        "Upgrade-Insecure-Requests": "1"})

    soup = BeautifulSoup(webpage.content, 'lxml')
    for div in soup.findAll('span', attrs={'class': 'B_NuCI'}):  # Title of the item
        product = div.text.strip()[0:].replace(",", "")
        print(product)

    for div in soup.findAll('div', attrs={'class': '_30jeq3 _16Jk6d'}):  # Price of the item
        product1 = div.text.strip()[1:].replace(",", "")
        print("Price of product:" + product1)

    for div in soup.findAll('div', attrs={'class': '_2d4LTz'}):  # Rating as on flipkart
        product2 = div.text.strip()[0:].replace(",", "")
        print("Rating of Product:" + product2)

    try:
        Rating = soup.select('div._1uJVNT')  # Total 5 star ratings
        Ratings = [Rating1.text for Rating1 in Rating]
        print("Total Five star Rating:" + Ratings[0])
    except:
        Ratings = [0]

        print("Total Five star Rating:" + str(Ratings[0]))

    Rating = soup.select('span._2_R_DZ')  # Total Ratings
    [print (Ratings.text.strip()[1:].replace(")", "") )for Ratings in Rating]
    #print("Total Rating:" + Ratings[1])
    for i, hel , rev in zip(pro_title, ratings , review):
        print(' '.join(i.split()[:3]).upper())
        if (' '.join(i.split()[:3]).upper() in product):
            c = hel.split()[0]
            if((float(product2) - float(c)) >= 0.4) or ((float(product2) - float(c)) <= 0.4):
                d = f"U should buy {i}"
                print(f"U should buy {i}")
                print("you should choose product {")
                list.append(i)
                list.append(c)
            if(abs(float(product2) - float(c)) <= 0.4):
                print("Lets check reviews")
                #print(int(rev.split()[0]))

                if(int(rev.split()[0]) >= int(Ratings[0])):
                    d = f"\n\nYou should choose product {i}"
                    print(f"\n\nYou should choose product {i}")
                    list.append(i)
                    list.append(max(float(product2),float(c) ))
                else:
                    d = f"\n\nyou should choose product {product}"
                    print(f"\n\nyou should choose product {product}")
                    print(f"Here is the link {flip}")
                    list.append(product)
        else:
            print(f"\n\n You should choose product  {i}")
            list.append(i)
            list.append(c)


        return list







