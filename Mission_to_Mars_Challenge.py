#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Splinter and Beautiful Soup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#Visit mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
#'Optional' delay for loading page
browser.is_element_present_by_css('div.list_text', wait_time =1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


#use parent element to find first 'a' tag and save as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


#use parent elem to find paragraph txt
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


#Visit url
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


#find and click full img button
full_img_elem = browser.find_by_tag('button')[1]
full_img_elem.click()


# In[10]:


#parse resultinig html w/ soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


#find the relative img url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


#use base url to create absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


df.to_html()


# In[15]:


#close browser session
#browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[16]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[17]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for i in range (0, 4):
    #create empty dictionary to hold the url and title for each hemisphere
    img_link_and_title = {}
    #visit the home url
    browser.visit(url)
    #fint the link for each individual hemisphere (all enclosed on h3 tag)
    img_info = browser.find_by_tag('h3')[i]
    #goes to the info on each hemisphere
    img_info.click()
    #create soup object
    html = browser.html
    img_soup = soup(html, 'html.parser')
    #extract the title of the hemisphere (enclosed in h2 tag)
    img_title = img_soup.find('h2').text
    #extract the url for the image from the 'sample' link
    img_link = img_soup.find('div', class_='downloads').a['href']
    #create the full url for the image
    img_link_full = f'{url}{img_link}'
    #add the link and title to the dict
    img_link_and_title['img_url'] = img_link_full
    img_link_and_title['title'] = img_title
    #add the dict to the list
    hemisphere_image_urls.append(img_link_and_title)


# In[18]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[19]:


# 5. Quit the browser
browser.quit()


# In[ ]:




