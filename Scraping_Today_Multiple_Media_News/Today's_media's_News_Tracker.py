import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# Creating the Scrapper

# url definition
# url1 = "https://timesofindia.indiatimes.com/india/andhra-pradesh"
url2 = "https://www.thenewsminute.com/section/Andhra%20Pradesh"
url3 = "https://www.thehansindia.com/andhra-pradesh"
url4 = "https://english.sakshi.com/andhrapradesh"
url5 = "https://www.sakshi.com/andhra-pradesh"
url6 = "http://www.prajasakti.com/WEBSECTION/AndhraPradesh"
url7 = "https://www.thehindu.com/news/national/andhra-pradesh"
url8 = "https://www.deccanherald.com/tag/andhra-pradesh"
url9 = "https://www.deccanchronicle.com/south/andhra-pradesh"
url10 = "https://www.andhrajyothy.com/pages/andhrapradesh/latest-news"
url11 = "https://www.eenadu.net/andhra-pradesh"
#url11 = "https://www.eenadu.net/apmukyamshalu"
#url12 = "https://www.eenadu.net/appolitics"
url13 = "https://timesofindia.indiatimes.com/city/amaravati"
url14 = "https://timesofindia.indiatimes.com/city/vijayawada"
url15 = "https://timesofindia.indiatimes.com/city/visakhapatnam"




# Requests
# r1 = requests.get(url1)
r2 = requests.get(url2)
r3 = requests.get(url3)
r4 = requests.get(url4)
r5 = requests.get(url5)
r6 = requests.get(url6)
r7 = requests.get(url7)
r8 = requests.get(url8)
r9 = requests.get(url9)
r10 = requests.get(url10)
r11 = requests.get(url11)
#r12 = requests.get(url12)
r13 = requests.get(url13)
r14 = requests.get(url14)
r15 = requests.get(url15)

# Save in cover pages the cover page content
# coverpage1 = r1.content
coverpage2 = r2.content
coverpage3 = r3.content
coverpage4 = r4.content
coverpage5 = r5.content
coverpage6 = r6.content
coverpage7 = r7.content
coverpage8 = r8.content
coverpage9 = r9.content
coverpage10 = r10.content
coverpage11 = r11.content
#coverpage12 = r12.content
coverpage13 = r13.content
coverpage14 = r14.content
coverpage15 = r15.content

# Soup Creation
# soup1 = BeautifulSoup(coverpage1, 'html5lib')
soup2 = BeautifulSoup(coverpage2, 'html5lib')
soup3 = BeautifulSoup(coverpage3, 'html5lib')
soup4 = BeautifulSoup(coverpage4, 'html5lib')
soup5 = BeautifulSoup(coverpage5, 'html5lib')
soup6 = BeautifulSoup(coverpage6, 'html5lib')
soup7 = BeautifulSoup(coverpage7, 'html5lib')
soup8 = BeautifulSoup(coverpage8, 'html5lib')
soup9 = BeautifulSoup(coverpage9, 'html5lib')
soup10 = BeautifulSoup(coverpage10, 'html5lib')
soup11 = BeautifulSoup(coverpage11, 'html5lib')
#soup12 = BeautifulSoup(coverpage12, 'html5lib')
soup13 = BeautifulSoup(coverpage13, 'html5lib')
soup14 = BeautifulSoup(coverpage14, 'html5lib')
soup15 = BeautifulSoup(coverpage15, 'html5lib')
#print(soup14)
#print(soup10)




# Empty List
list_link = []
list_titles = []
list_source = []
list_posting_time = []
list_tags = []

# News Identification "Times of India
# homepage_news_toi = soup1.find('ul', class_='top-newslist clearfix')
# news_recent = homepage_news_toi.find_all('span', class_='w_tle')
# recent_articles = len(news_recent)
# coverpage_news_toi = soup1.find('div', id='c_articlelist_stories_2')
# news_all = coverpage_news_toi.find_all('span', class_='w_tle')
# all_articles = len(news_all)
# total_articles = recent_articles + all_articles
# print(total_articles)
#
# for n in np.arange(0, all_articles):
#     # Getting the link to article
#     link_all = "https://timesofindia.indiatimes.com" + news_all[n].find('a')['href']
#     list_link.append(link_all)
#
#     # Getting the title
#     title_all = news_all[n].find('a').get_text().replace('\n', '')
#     list_titles.append(title_all)
#
#     # Getting the source
#     source_all = "Times of India"
#     list_source.append(source_all)
#
#     # Getting the posting time
#     posting_time_all = "NA"
#     list_posting_time.append(posting_time_all)
#
#     # Getting the tags
#     tags_all = "NA"
#     list_tags.append(tags_all)
#
# for n in np.arange(0, recent_articles):
#     # Getting the link to article
#     link_recent = "https://timesofindia.indiatimes.com" + news_recent[n].find('a')['href']
#     list_link.append(link_recent)
#
#     # Getting the title
#     title_recent = news_recent[n].find('a').get_text().replace('\n', '')
#     list_titles.append(title_recent)
#
#     # Getting the source
#     source_recent = "Times of India"
#     list_source.append(source_recent)
#
#     # Getting the posting time
#     posting_time_recent = "NA"
#     list_posting_time.append(posting_time_recent)
#
#     # Getting the tags
#     tags_recent = "NA"
#     list_tags.append(tags_recent)

# News Identification "Times of India Amaravati
homepage_news_toi = soup13.find('ul', class_='top-newslist clearfix')
news_recent = homepage_news_toi.find_all('span', class_='w_tle')
recent_articles = len(news_recent)
coverpage_news_toi = soup13.find('div', id='c_articlelist_stories_2')
news_all = coverpage_news_toi.find_all('span', class_='w_tle')
all_articles = len(news_all)
total_articles = recent_articles + all_articles
print(total_articles)

for n in np.arange(0, all_articles):
    # Getting the link to article
    link_all = "https://timesofindia.indiatimes.com" + news_all[n].find('a')['href']
    list_link.append(link_all)
    

    # Getting the title
    title_all = news_all[n].find('a').get_text().replace('\n',' ')
    list_titles.append(title_all)
    #print( list_titles)

    # Getting the source
    source_all = "Times of India"
    list_source.append(source_all)

    # Getting the posting time
    posting_time_all = "NA"
    list_posting_time.append(posting_time_all)

    # Getting the tags
    tags_all = "NA"
    list_tags.append(tags_all)


for n in np.arange(0, recent_articles):
    # Getting the link to article
    link_recent = "https://timesofindia.indiatimes.com" + news_recent[n].find('a')['href']
    list_link.append(link_recent)

    # Getting the title
    title_recent = news_recent[n].find('a').get_text().replace('\n', '')
    list_titles.append(title_recent)

    # Getting the source
    source_recent = "Times of India"
    list_source.append(source_recent)

    # Getting the posting time
    posting_time_recent = "NA"
    list_posting_time.append(posting_time_recent)

    # Getting the tags
    tags_recent = "NA"
    list_tags.append(tags_recent)

# News Identification "Times of India Vijayawada
"""homepage_news_toi = soup14.find('div', class_='row')
#print(homepage_news_toi)
news_recent1 = homepage_news_toi.find_all('figure', class_='ZbcY0')
news_recent2 = homepage_news_toi.find_all('figure', class_='_1Fkp2')
news_recent = news_recent1+news_recent2
#print(news_recent)
#print(news_recent)
recent_articles = len(news_recent)
#print(recent_articles)"""
homepage_news_toi = soup14.find('div', class_='_2ZXWE')
#print(homepage_news_toi)
news_recent1 = homepage_news_toi.find_all('figure', class_='ZbcY0')
news_recent2 = homepage_news_toi.find_all('figure', class_='_1Fkp2')
news_recent = news_recent1+news_recent2
recent_articles = len(news_recent)
#print(recent_articles)
news_recent3 = soup14.find('div', class_='_2ofaX')
#print(news_recent3)
news_all = news_recent3.find_all('figure', class_='_1Fkp2')
all_articles = len(news_all)
total_articles = recent_articles + all_articles
print(total_articles)

"""coverpage_news_toi = soup14.find('div', class_='_2V609')
#print(coverpage_news_toi)
coverpage_news_toiN = coverpage_news_toi.find('div', class_='row')
news_all = coverpage_news_toiN.find_all('figure', class_='_1Fkp2')
#print(news_all)
all_articles = len(news_all)
total_articles = recent_articles + all_articles
print(total_articles)"""

for n in np.arange(0, all_articles):
    # Getting the link to article
    link_all = news_all[n].find('a')['href']
    list_link.append(link_all)

    # Getting the title
    title_all = news_all[n].find('figcaption').get_text().replace('\n', '')
    list_titles.append(title_all)

    # Getting the source
    source_all = "Times of India"
    list_source.append(source_all)

    # Getting the posting time
    posting_time_all = "NA"
    list_posting_time.append(posting_time_all)

    # Getting the tags
    tags_all = "NA"
    list_tags.append(tags_all)

for n in np.arange(0, recent_articles):
    # Getting the link to article
    link_recent = news_recent[n].find('a')['href']
    list_link.append(link_recent)

    # Getting the title
    title_recent = news_recent[n].find('figcaption').get_text().replace('\n', '')
    list_titles.append(title_recent)

    # Getting the source
    source_recent = "Times of India"
    list_source.append(source_recent)

    # Getting the posting time
    posting_time_recent = "NA"
    list_posting_time.append(posting_time_recent)

    # Getting the tags
    tags_recent = "NA"
    list_tags.append(tags_recent)

# News Identification "Times of India Vishakapatnam
"""homepage_news_toi = soup15.find('div', class_='row')
#print(homepage_news_toi)
news_recent1 = homepage_news_toi.find_all('figure', class_='ZbcY0')
news_recent2 = homepage_news_toi.find_all('figure', class_='_1Fkp2')
news_recent = news_recent1+news_recent2
#print(news_recent)
#print(news_recent)
recent_articles = len(news_recent)
#print(recent_articles)
coverpage_news_toi = soup15.find('div', class_='_2V609')
#print(coverpage_news_toi)
coverpage_news_toiN = coverpage_news_toi.find('div', class_='row')
news_all = coverpage_news_toiN.find_all('figure', class_='_1Fkp2')
#print(news_all)
all_articles = len(news_all)
total_articles = recent_articles + all_articles
print(total_articles)"""
homepage_news_toi = soup15.find('div', class_='_2ZXWE')
#print(homepage_news_toi)
news_recent1 = homepage_news_toi.find_all('figure', class_='ZbcY0')
news_recent2 = homepage_news_toi.find_all('figure', class_='_1Fkp2')
news_recent = news_recent1+news_recent2
recent_articles = len(news_recent)
#print(recent_articles)
news_recent3 = soup14.find('div', class_='_2ofaX')
#print(news_recent3)
news_all = news_recent3.find_all('figure', class_='_1Fkp2')
all_articles = len(news_all)
total_articles = recent_articles + all_articles
print(total_articles)

for n in np.arange(0, all_articles):
    # Getting the link to article
    link_all = news_all[n].find('a')['href']
    list_link.append(link_all)

    # Getting the title
    title_all = news_all[n].find('figcaption').get_text().replace('\n', '')
    list_titles.append(title_all)

    # Getting the source
    source_all = "Times of India"
    list_source.append(source_all)

    # Getting the posting time
    posting_time_all = "NA"
    list_posting_time.append(posting_time_all)

    # Getting the tags
    tags_all = "NA"
    list_tags.append(tags_all)

for n in np.arange(0, recent_articles):
    # Getting the link to article
    link_recent = news_recent[n].find('a')['href']
    list_link.append(link_recent)

    # Getting the title
    title_recent = news_recent[n].find('figcaption').get_text().replace('\n', '')
    list_titles.append(title_recent)

    # Getting the source
    source_recent = "Times of India"
    list_source.append(source_recent)

    # Getting the posting time
    posting_time_recent = "NA"
    list_posting_time.append(posting_time_recent)

    # Getting the tags
    tags_recent = "NA"
    list_tags.append(tags_recent)





# News Identification "The News Minute
coverpage_news_tnm = soup2.find_all('div', class_='card-body')
article_tnm = len(coverpage_news_tnm)
print(article_tnm)

# No of Articles
no_of_articles_tnm = article_tnm

for n in np.arange(0, no_of_articles_tnm):
    # Getting the link to article
    link_tnm = 'https://www.thenewsminute.com' + coverpage_news_tnm[n].find('a')['href']
    list_link.append(link_tnm)

    # Getting the title
    title_tnm = coverpage_news_tnm[n].find('a').get_text()
    list_titles.append(title_tnm)

    # Getting the source
    source_tnm = "The News Minute"
    list_source.append(source_tnm)

    # Getting the posting time
    posting_time_tnm = coverpage_news_tnm[n].find('span', class_='time').get_text()
    list_posting_time.append(posting_time_tnm)

    # Getting the tags
    tags_tnm = coverpage_news_tnm[n].find('span', class_='label').get_text()
    list_tags.append(tags_tnm)

# News Identification "The Hans Indian
coverpage_news_thi = soup3.find_all('div', class_='col-md-8 col-8')
article_thi = len(coverpage_news_thi)
print(article_thi)

# No of Articles
no_of_articles_thi = article_thi

for n in np.arange(0, no_of_articles_thi):
    # Getting the link to article
    link_thi = url3 + coverpage_news_thi[n].find('a')['href']
    list_link.append(link_thi)

    # Getting the title
    title_thi = coverpage_news_thi[n].find('a').get_text()
    list_titles.append(title_thi)

    # Getting the source
    source_thi = "The Hans Indian"
    list_source.append(source_thi)

    # Getting the time
    posting_time_thi = coverpage_news_thi[n].find('span').get_text()
    list_posting_time.append(posting_time_thi)

    # Getting the tags
    tags_thi = "NA"
    list_tags.append(tags_thi)

# News Identification
#coverpage_news_a_sp = soup4.find_all('h4', class_='field-content thumbnail-list-item-title')
#length_link_sp = len(coverpage_news_a_sp)
#print(length_link_sp)
#coverpage_news_b_sp = soup4.find_all('div', class_='views-field views-field-body')
#length_title_sp = len(coverpage_news_b_sp)
#print(length_title_sp)
#homepage_news_sp = soup4.find('div', class_='view-content')
#coverpage_news_c_sp = homepage_news_sp.find_all('div', class_='field-content')
#length_time_sp = len(coverpage_news_c_sp)
#print(length_time_sp)

#for n in np.arange(0, length_link_sp):
    # Getting the link to article
    #link_sp = "https://english.sakshi.com" + coverpage_news_a_sp[n].find('a')['href']
    #list_link.append(link_sp)

    # Getting the title
    #title_sp = coverpage_news_b_sp[n].find('span').get_text()
   # list_titles.append(title_sp)

    # Getting the source
  #  source_sp = "Sakshi Post"
 #   list_source.append(source_sp)

    # Getting the time
#    posting_time_sp = coverpage_news_c_sp[n].get_text()
#    list_posting_time.append(posting_time_sp)

    # Getting the tags
#    tags_sp = "NA"
#    list_tags.append(tags_sp)


# News Identification "Praja Sakti
coverpage_news_ps = soup6.find_all('div', class_='post-img main-sidebar-element')
article_count_ps = len(coverpage_news_ps)
print(article_count_ps)

for n in np.arange(0, article_count_ps):
    # Getting the link to article
    link_ps = "http://www.prajasakti.com" + coverpage_news_ps[n].find('a')['href']
    list_link.append(link_ps)

    # Getting the title
    title_ps = coverpage_news_ps[n].find('img')['alt']
    list_titles.append(title_ps)

    # Getting the source
    source_ps = "Prajasakti- Telugu"
    list_source.append(source_ps)

    # Getting the time
    posting_time_ps = "NA"
    list_posting_time.append(posting_time_ps)

    # Getting the tags
    tags_ps = "NA"
    list_tags.append(tags_ps)

# News Identification "The Hindu
hindu_story_card_b = soup7.find_all('div', class_='Other-StoryCard')
article_ht_b = len(hindu_story_card_b)
print(article_ht_b)
for n in np.arange(0, article_ht_b):
    # Getting the link to article
    link_ht_b = hindu_story_card_b[n].find('a')['href']
    list_link.append(link_ht_b)

    # Getting the title
    title_ht_b = hindu_story_card_b[n].find('a').get_text()
    list_titles.append(title_ht_b)

    # Getting the sorce
    source_ht_b = "The Hindu"
    list_source.append(source_ht_b)

    # Getting the time
    posting_time_th_b = hindu_story_card_b[n].find('a')['title']
    list_posting_time.append(posting_time_th_b)

    # Getting the tags
    tags_th_b = "NA"
    list_tags.append(tags_th_b)

# News Identification "Deccan Herald
coverpage_news_dh = soup8.find('div', id='general_terms')
news_articles_dh = coverpage_news_dh.find_all('div', class_='sm-hr-card__content bg-gray')
coverpage_links_dh = coverpage_news_dh.find_all('div', class_='sm-hr-card sm-hr-card--m-top')
len1_dh = len(news_articles_dh)
len2_dh = len(coverpage_links_dh)

print(len1_dh)
print(len2_dh)

for n in np.arange(0, len1_dh):
    # Getting the link to article
    link_dh = "https://www.deccanherald.com" + coverpage_links_dh[n].find('a')['href']
    list_link.append(link_dh)

    # Getting the title
    title_dh = news_articles_dh[n].find('h4').get_text()
    list_titles.append(title_dh)

    # Getting the source
    source_dh = "Deccan Herald"
    list_source.append(source_dh)

    # Getting the time
    posting_time_dh = "NA"
    list_posting_time.append(posting_time_dh)

    # Getting the tags
    tags_dh = "NA"
    list_tags.append(tags_dh)

# News Identification "Deccan Chronical"
coverpage_news_dc = soup9.find_all('div', class_='col-sm-12 SunChNewListing')
len_dc = len(coverpage_news_dc)
print(len_dc)
coverpage_news_dc_time = soup9.find_all('span', class_='SunChDt2')
len1_dc = len(coverpage_news_dc_time)
print(len1_dc)

for n in np.arange(0, len_dc):
    # getting link
    thumb_dc = coverpage_news_dc[n].find('div', class_='col-sm-4 ThumbImg')
    link_dc = 'https://www.deccanchronicle.com/'+ thumb_dc.find('a')['href']
    list_link.append(link_dc)

    # getting title
    body_dc = coverpage_news_dc[n].find('div', class_='col-sm-8')
    title_dc = body_dc.find('a').get_text()
    list_titles.append(title_dc)

    # Getting the source
    source_dc = "Deccan Chronicle"
    list_source.append(source_dc)

    # Getting the time
    posting_time_dc = coverpage_news_dc_time[n].get_text()
    list_posting_time.append(posting_time_dc)

    # Getting the tags
    tags_dc = "NA"
    list_tags.append(tags_dc)
    

# News Identification "eenadu
title_news_st = soup11.find('ul', class_='cd-tabs-content no-space')
ap_news = title_news_st.find_all('aside')
title_count_st = len(ap_news)
#time_count_st = len(time_news_st)
#print(title_count_st,'a')
#print(time_count_st)
eenadu_news = soup11.find_all('aside', 'thumb-content-more')
Ap_news_eenadu = ap_news + eenadu_news
article_eenadu = len(Ap_news_eenadu)
print(article_eenadu)

for n in np.arange(0, article_eenadu):
    # Getting the link to article
    link_st = Ap_news_eenadu[n].find('a')['href']
    list_link.append(link_st)

   # Getting the title
   
    title_st = Ap_news_eenadu[n].find('h3').get_text()
    list_titles.append(title_st)

    # Getting the source
    source_st = "Eenadu"
    list_source.append(source_st)

    # Getting the time
    posting_time_een = "NA"
    list_posting_time.append(posting_time_een)
    
    # Getting the tags
    tags_st = "NA"
    list_tags.append(tags_st)
    


# News Identification "Andhra Jyothi"
coverpage_news_aj = soup10.find_all('td', class_='thumbnail w100 fl')
len_aj = len(coverpage_news_aj)
print(len_aj,"andhrajyothi")

for n in np.arange(0, len_aj):
    # Getting the link to article
    link_aj = "https://www.andhrajyothy.com" + coverpage_news_aj[n].find('a')['href']
    list_link.append(link_aj)

    # Getting the title
    title_aj = coverpage_news_aj[n].find('a').get_text()
    list_titles.append(title_aj)

    # Getting the source
    source_aj = "Andhra Jyothi"
    list_source.append(source_aj)

    # Getting the time
    posting_time_aj = "NA"
    list_posting_time.append(posting_time_aj)

    # Getting the tags
    tags_aj = "NA"
    list_tags.append(tags_aj)



# News Identification "Sakshi- Telugu
title_news_st = soup5.find_all('div', class_='views-field views-field-title')
time_news_st = soup5.find_all('div', class_='views-field views-field-changed')
title_count_st = len(title_news_st)-1
time_count_st = len(time_news_st)-1
print(title_count_st,"error")
print(time_count_st)

for n in np.arange(0, title_count_st):
    # Getting the link to article
    link_st = "https://www.sakshi.com" + title_news_st[n].find('a')['href']
    list_link.append(link_st)

    # Getting the title
    title_st = title_news_st[n].find('a').get_text()
    list_titles.append(title_st)

    # Getting the source
    source_st = "Sakshi Post- Telugu"
    list_source.append(source_st)

    # Getting the time
    posting_time_st = time_news_st[n-1].find('span').get_text()
    list_posting_time.append(posting_time_st)

    # Getting the tags
    tags_st = "NA"
    list_tags.append(tags_st)


# df_show_info
df_show_info = pd.DataFrame({
    'Title': list_titles,
    'Link': list_link,
    'Source': list_source,
    'Posted On': list_posting_time,
    'Tags': list_tags
})

df_show_info.drop_duplicates("Title", inplace=True)

#df_show_info.to_json('media tracker_11feb.json', index=True)
df_show_info.to_excel('AP_media_tracker_19_Apr.xls', index=True)
df_show_info.to_csv('AP_Media_Tracker_19_Apr.csv', index=True)







