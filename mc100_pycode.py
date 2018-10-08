import urllib.request
from bs4 import BeautifulSoup
#url 추출
parameter = []
for i in range(1,10):
    list_url = 'http://mc.netease.com/forum.php?mod=forumdisplay&fid=42&filter=typeid&typeid='+str(i)
    
    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url, timeout=100).read()  #timeout
    soup= BeautifulSoup(res, "html.parser")
        
    for link in soup.select('th > a.s'):
        parameter.append('http:'+link.get('href'))  
parameter

#텍스트추출
txt= []
for j in parameter:
    print(j)
    url = urllib.request.Request(j)
    res = urllib.request.urlopen(url).read()
    soup= BeautifulSoup(res, "html.parser")
    result = soup.select('.t_f')
    #pid1769859 > tbody > tr:nth-child(1) > td.plc > div.pct > div > div.t_fsz
    
    for j in result:
        txt.append(j.text)
#멀티프로세싱 
# =============================================================================
# from multiprocessing import Pool      
# p= Pool(processes=2) 
# p.map(get_content, parameter)
# =============================================================================
# #pool을 써서 해보았으나 pool을 쓰면 계속 컴퓨터가 멈추고 잘 되지않아 다른방식으로 멀티프로세싱 해보았습니다 
# import urllib.request
# from bs4 import BeautifulSoup
# #url 추출
# parameter = []
# for i in range(1,10):
#     list_url = 'http://mc.netease.com/forum.php?mod=forumdisplay&fid=42&filter=typeid&typeid='+str(i)
#     
#     url = urllib.request.Request(list_url)
#     res = urllib.request.urlopen(url, timeout=100).read()  #timeout
#     soup= BeautifulSoup(res, "html.parser")
#         
#     for link in soup.select('th > a.s'):
#         parameter.append('http:'+link.get('href'))  
# 
# parameter
# #텍스트추출
# x=int(len(parameter)/2)
# y=int(len(parameter))
# #session1
# txt= []
# for j in parameter[0:x]:
#     print(j)
#     url = urllib.request.Request(j)
#     res = urllib.request.urlopen(url).read()
#     soup= BeautifulSoup(res, "html.parser")
#     result = soup.select('.t_f')
#     #pid1769859 > tbody > tr:nth-child(1) > td.plc > div.pct > div > div.t_fsz
#     
#     for j in result:
#         txt.append(j.text)
# 
# with open('C:/data/mc1.txt','w',encoding='UTF8') as file:
#     for i in range(0,len(new_txt)):
#         file.write(new_txt[i])           
# #session2   
# from bs4 import BeautifulSoup
# #url 추출
# parameter = []
# for i in range(1,10):
#     list_url = 'http://mc.netease.com/forum.php?mod=forumdisplay&fid=42&filter=typeid&typeid='+str(i)
#     
#     url = urllib.request.Request(list_url)
#     res = urllib.request.urlopen(url, timeout=100).read()  #timeout
#     soup= BeautifulSoup(res, "html.parser")
#         
#     for link in soup.select('th > a.s'):
#         parameter.append('http:'+link.get('href'))          
# for j in parameter[x+1:y]:
#     print(j)
#     url = urllib.request.Request(j)
#     res = urllib.request.urlopen(url).read()
#     soup= BeautifulSoup(res, "html.parser")
#     result = soup.select('.t_f')
#     #pid1769859 > tbody > tr:nth-child(1) > td.plc > div.pct > div > div.t_fsz
#     
#     for j in result:
#         txt.append(j.text)
# 
#         
# with open('C:/data/mc2.txt','w',encoding='UTF8') as file:
#     for i in range(0,len(new_txt)):
#         file.write(new_txt[i])      
# #session3(mc1+mc2)
# mc1=open('c:/data/mc1.txt',encoding='utf-8').read()     
# mc1   
# mc2=open('c:/data/mc2.txt',encoding='utf-8').read()   
# mc2
# type(mc1)
# mc3=mc1+mc2
# mc3
# =============================================================================


#정제전 원본텍스트 
txt
#string화 new_txt
new_txt="".join(txt)


#url 정제
import re
for i in re.findall('https',new_txt,re.I):
    new_txt =re.sub(i,'',new_txt)
re.findall(r'https\:\/\/.*[\r\n]*',new_txt,re.I) 
re.findall('\:\/\/.*[\r\n]*',new_txt,re.I) 
re.findall('\:\/\/.*[\r\n]*',new_txt,re.I) 
for i in re.findall(r'https\:\/\/.*[\r\n]*',new_txt,re.I):
    new_txt =re.sub(i,'',new_txt)
for i in re.findall('\:\/\/.*[\r\n]*',new_txt,re.I) :
    new_txt = re.sub(i,'',new_txt)
#정제
#1차정제 : txt만뽑기 (그림파일명, 유알엘, 이모티콘 및 이스케이프시퀀스 제거)
#이스케이프시퀀스 제거
new_txt=new_txt.replace('\n','')
new_txt=new_txt.replace('\xa0','')
new_txt=new_txt.replace('\r','')

#그림파일명제거 ex)QQ图片20181006105603.jpg (33.2 KB, 下载次数: 0)
import re
#ex)QQ图片20181006105603.jpg
for i in re.findall('QQ图片\w+\.\w+',new_txt,re.I) :
    new_txt = re.sub(i,'',new_txt)
for i in re.findall('QQ截图\w+\.\w+',new_txt,re.I) :
    new_txt = re.sub(i,'',new_txt)        

#184030yzhxjmzhhquk5h0e.gif (193.73 KB, 下载次数: 0)下载附件6小时前 上传支持
#ex 184030yzhxjmzhhquk5h0e.gif
for i in re.findall('\w+\.gif',new_txt,re.I):
    new_txt=re.sub(i,'',new_txt)
for i in re.findall('\w+\.jpg',new_txt,re.I):
    new_txt=re.sub(i,'',new_txt)
for i in re.findall('\w+\.png',new_txt,re.I):
    new_txt = re.sub(i,'',new_txt)   
#ex (33.2 KB, 下载次数: 0)
for i in re.findall('\(\w+\.\w+ KB\, 下载次数\: \w+\)',new_txt,re.I):
    new_txt =new_txt = re.sub(i,'',new_txt) 
#이모티콘으로 쓰인 qqtupian,jietu 삭제
for i in re.findall('qq图片',new_txt,re.I):
    new_txt = re.sub(i,'',new_txt)   
for i in re.findall('qq截图',new_txt,re.I):
    new_txt = re.sub(i,'',new_txt)
#이모티콘 삭제
for i in re.findall('xa\d',new_txt,re.I):
    new_txt = re.sub(i,'',new_txt)  
    
#发表于 2018-10-6 00:31
for i in re.findall('发表于 \d+[-]\d+[-]\d+ \d+[:]\d+',new_txt):
    new_txt =re.sub(i,'',new_txt)
for i in re.findall('于 \d+[-]\d+[-]\d+ \d+[:]\d+',new_txt):
    new_txt =re.sub(i,'',new_txt)

#ex 下载附件6小时前 上传   
for i in re.findall('下载附件\d+小时前 上传',new_txt,re.I):
    new_txt =new_txt = re.sub(i,'',new_txt)
new_txt    
  
#a.a2018-10-05_08.39. ()下载附件昨天09:06 上传2018-10-05_08.39. ()下载附件昨天09:06 上传2018-10-05_08.49. ()下载附件昨天09:06 上传2018-10-05_08.58. ()下载附件昨天09:06 上传
for i in re.findall('下载附件昨天\d+:\d+',new_txt):
    new_txt =re.sub(i,'',new_txt)
for i in re.findall('上传\d+-\d+-\d+_\d+.\d+.',new_txt):
    new_txt =re.sub(i,'',new_txt)
new_txt

#：/gamerule commandBlockOutput false
for i in re.findall('/gamerule commandBlockOutput false',new_txt):
    new_txt =re.sub(i,'',new_txt)
new_txt


#파일로 저장 
with open('C:/data/mc.txt','w',encoding='UTF8') as file:
    for i in range(0,len(new_txt)):
        file.write(new_txt[i])   


#jieba 형태소분석기
import nltk
import jieba
import jieba.analyse
raw=open('c:/data/mc.txt',encoding='utf-8',errors='ignore').read()
a=jieba.analyse.extract_tags(raw, topK=100, withWeight=False, allowPOS=()) #중국어 키워드 100개를 뽑아보자
print(a)

#키워드별 정확한 빈도수체크
fra = jieba.cut(raw)
fra2 = jieba.cut_for_search(raw)
def freq(arg):
    freq={}
    for c in arg:
        if c in freq:
            freq[c] +=1
        else:
            freq[c]=1
    return(freq)
freq(fra)
freq(fra2)


#2차정제 (상위빈도 관건사 보며 정제)
re.findall('\W',a)
for i in re.findall('/gamerule commandBlockOutput false',new_txt):
    new_txt =re.sub(i,'',new_txt)
re.findall('',)
new_txt
#wordcloud 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
a
a2=','.join(a)
a2
wordcloud = WordCloud(font_path = 'c://Windows//fonts//simhei.ttf',
                      background_color="white",width=1000, height=860, margin=2).generate(a2)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


