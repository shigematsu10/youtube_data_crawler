# YoutubeDataCrawler

## Motivation

## System Details


## Method used
1. Create API key  
Please refer to the following site to generate the API key.  
[create API key](https://qiita.com/shinkai_/items/10a400c25de270cb02e4)

2. Enter API key in crawler.py  
Please enter the API key you generated on line 17 of [crawler.py](crawler.py)  

3. Install the library  
Run the following code to install library.  
```
pip install pandas
pip install google-api-python-client
```

4. Crawling  
Run the following code, and you will be prompted to enter the keyword.  
```
python crawler.py
```
When you enter a keyword, the video information about the keyword is stored in the result.  