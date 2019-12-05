
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser=init_browser()
    mars = {}
    
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    
    mars["title"]=soup.find("div", class_="content_title").get_text()
    mars["p"]=soup.find("div", class_="rollover_description_inner").get_text()
   
    image_url = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17550_ip.jpg"
    browser.visit(image_url)
    time.sleep(1)
    image_html = browser.html
    image_soup = bs(image_html, "html.parser")
    mars["mars_image"]=soup.find_all("img", style="-webkit-user-select: none;margin: auto;cursor: zoom-out;")
   

    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    time.sleep(1)
    weather_html = browser.html
    weather_soup = bs(weather_html, "html.parser")
    mars["mars_weather"] =weather_soup.find("p", class_="tweet-text").get_text()
    
    
    
    mars_facts_url="https://space-facts.com/mars/"
    browser.visit(mars_facts_url)
    time.sleep(1)
    facts_html = browser.html
    facts_soup = bs(facts_html, "html.parser")
    mars["mars_facts"] =facts_soup.find_all("table").get_text()
    
    return mars
    browser.quit()
    
    
    tables=pd.read_html(mars_facts)
    browser.quit()
    mars_facts= tables[0]
    return mars
    browser.quit()
    
    hemisphere_image = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
    ]
    browser.quit()
    return hemisphere_image

    
mars = {
        "title": title,
        "summary":p,
        "image": mars_image,
        "weather": mars_weather,
        "facts": mars_facts,
        "hemispheres": hemisphere_image} 
return mars
