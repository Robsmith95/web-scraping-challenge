#!/usr/bin/env python
# coding: utf-8

# In[135]:


from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time
import os


# In[ ]:


# NASA Mars News


# In[29]:


#ChromeDriver
executable_path = {'executable_path': '/Users/robertsmith/.wdm/drivers/chromedriver/mac64/87.0.4280.88/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[30]:


url = ('https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')
browser.visit(url)


# In[41]:


#Soup Parsing
html = browser.html
soup = BeautifulSoup(html, "html.parser")
time.sleep(5)
soup_slide = soup.select_one("ul.item_list li.slide")
soup_slide.find("div", class_="content_title")


# In[40]:


#Use Soup to scrape the first News Title/Paragraph
news_title = soup_slide.find("div", class_="content_title").get_text()
news_paragraph = soup_slide.find("div", class_="article_teaser_body").get_text()


# In[39]:


print(news_title)
print(news_paragraph)


# In[98]:


#JPL Mars Space Images - Featured Image/*


# In[99]:


executable_path = {'executable_path': '/Users/robertsmith/.wdm/drivers/chromedriver/mac64/87.0.4280.88/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[100]:


print(soup.prettify())


# In[101]:


url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[104]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[105]:


#Beautiful Soup to find feaured image
featured_image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + featured_image


# In[106]:


print(featured_image_url)


# In[107]:


#Mars Facts


# In[109]:


url = 'https://space-facts.com/mars/'
browser.visit(url)


# In[110]:


mars_info = pd.read_html(url)
mars_info = pd.DataFrame(mars_info[0])
url = mars_info.to_html(header = False, index = False)


# In[113]:


#Information regarding Mars (Diameter, Mass, Moons, Orbit, Temperature, Record Date/Name)
print(mars_info)


# In[114]:


#Mars Hemispheres


# In[126]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[127]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[128]:


hemisphere_image_urls = []


# In[129]:


products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")


# In[130]:


for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    hemisphere_image_urls.append({"title": title, "img_url": image_url})


# In[134]:


#Hemispheres image results of Cerberus, Schiaparelli, Syrtis Major & Valles Marineris Hemispheres
hemisphere_image_urls


# In[ ]:





# In[ ]:




