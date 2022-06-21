# importing libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import keyboard
import requests
titles = list()
prices = list()
ratings = list()
flip = list()
lst = list()
review = list()
def main2(URL):
	HEADERS = ({
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
		'Accept-Language': 'en-US, en;q=0.5'})

	# Making the HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Creating the Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")

	# retreiving product title
	try:
		# Outer Tag Object
		title = soup.find("span",
						  attrs={"id": 'productTitle'})

		# Inner NavigableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip().replace(',', '')


	except AttributeError:
		title_string = "NA"
	titles.append(title_string)
	print("product Title = ", title_string)

	# saving the title in the file

	# retreiving price
	try:
		price = soup.find(
			"span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
	# we are omitting unnecessary spaces
	# and commas form our string
	except AttributeError:
		try:
			price = soup.find("span", attrs={'id': "priceblock_dealprice"}).string.strip().replace(',', '')
		except:

			price = "NA"
	prices.append(price)
	print("Products price = ", price)

	# saving

	# retreiving product rating
	try:
		rating = soup.find("i", attrs={
			'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')

	except AttributeError:

		try:
			rating = soup.find(
				"span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
		except:
			rating = "NA"
		ratings.append(rating)
		print("Overall rating = ", rating)

	try:
		review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(",", "")

	except AttributeError:
		review_count = "NA"
	review.append(review_count)
	print("Total reviews = ", review_count)

	# print availiblility status
	try:
		available = soup.find("div", attrs={'id': 'availability'})
		available = available.find("span").string.strip().replace(',', '')

	except AttributeError:
		available = "NA"
	print("Availability = ", available)


#print(titles, prices , ratings)
	#return titles , prices , ratings





	# closing the file

def start1(lst):
	for element in lst:
		main2(element)
	print(titles, prices , ratings)
	l = lnks(titles)
	print(l)
	print(l[1])
	c = l[0]
	flip_url = flipkart(c)
	#flip_url1 = "https://www.flipkart.com" + flip_url
	print(flip_url)
	return flip_url, ratings, titles, review
def flipkart(url):
	req = requests.get(url, headers={
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"})  # Making the website believe that you are accessing it using a mozilla browser.

	soup = BeautifulSoup(req.content, 'lxml')
	possible_links = soup.find_all('a' , attrs={'class': '_1fQZEK'})
	print(soup.find('a' , attrs={'class': '_1fQZEK'}))
	try:
		for link in possible_links:
			print(link)
			lst.append(link.attrs['href'])

		return ("https://www.flipkart.com"+lst[0])
	except:
		return ("https://www.flipkart.com")

def lnks(titles):
	for title in titles:
		webpage ="https://www.flipkart.com/"
		driver = webdriver.Chrome("E:\driver\chromedriver.exe")
		driver.get(webpage)
		driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
		sbox = driver.find_element_by_xpath(r"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
		sbox.send_keys(title)
		keyboard.press("enter")
		keyboard.release("enter")
		driver.maximize_window()
		lnks_flipkart = driver.current_url
		flip.append(lnks_flipkart)
	return flip
		#flipkart_final.main()
#main2("https://www.amazon.in/Samsung-Galaxy-M12-Storage-Processor/dp/B08XJBPCTR/ref=sr_1_2_sspa?dchild=1&keywords=phone&qid=1619841033&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNksxSTYwWU44WDJTJmVuY3J5cHRlZElkPUEwMDQ2OTQ4M1NNN1ZOSE9ITFJENSZlbmNyeXB0ZWRBZElkPUEwNzUyMzY4UTlTMDhPTVA2N1hEJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
#print(t , q , r)



