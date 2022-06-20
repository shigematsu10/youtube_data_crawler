# YoutubeDataCrawler

## Motivation
A variety of videos are being posted, and many videos are hit for a single keyword.  
We thought that by saving these numerous videos as a list, it could be used for various purposes, such as market analysis and analysis of the characteristics of popular videos.

## System Details
Search for videos for the keyword you want to search for and list them in order of most viewed.  
The information to be obtained is as follows  
・Video title  
・Video URL  
・Channel name  
・Number of subscribers  
・Date the channel was established  

## Method used
1. Create API key  
Please refer to the following site to generate the API key.  
[create API key](https://qiita.com/shinkai_/items/10a400c25de270cb02e4)

2. Enter API key in crawler.py  
Please enter the API key you generated on line 6 of [crawler.py](crawler.py)  

3. Install the library  
Run the following code to install library.  
```
pip install pandas
pip install google-api-python-client
```

4. Crawling  
Run the following code, and you will be prompted to enter the keyword.  
When you enter a keyword, the video information about the keyword is stored in the result.  
```
python crawler.py
```
