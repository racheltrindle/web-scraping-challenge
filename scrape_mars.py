from splinter import Browser
from bs4 import BeautifulSoup as bs

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser=init_browser()
    news = {}
    
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    news["title"]=soup.find("div", class_="content_title").get_text()
    news["p"]=soup.find("div", class_="rollover_description_inner").get_text()

    browser.quit()
    return news


    
#     mars_pic = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17550_ip.jpg"
#     browser.visit(url)
    
#     html = browser.html
#     soup = bs(html, "html.parser")
#     browser.quit()
#     # Store data in a dictionary
#     # news_data = {
#     #     "news_title": news_title,
#     #     "news_p": news_p,
#     # }
#     return featured_image_url

#     # url1 = 'https://twitter.com/marswxreport?lang=en'
#     # response = requests.get(url1)
#     # soup1 = BeautifulSoup(response.text, 'html.parser')
#     # mars_weather=soup1.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
#     # browser.quit()
#     # return mars_weather
    
#     # url2='https://space-facts.com/mars/'
#     # tables=pd.read_html(url2)
#     # return tables

#     # hemisphere_image_urls = [
#     # {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"},
#     # {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
#     # {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
#     # {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
#     # ]
#     # return hemisphere_image_urls

