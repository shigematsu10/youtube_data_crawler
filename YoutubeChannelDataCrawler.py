#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:52:26 2020

@author: shigematsuyuuki
"""

""""検索したいキーワードについての動画を検索し再生回数が多い順にリストアップ
　　　チャンネル名、動画URL、登録者数、チャンネルを開設した日付け"""
import pandas as pd
from googleapiclient.discovery import build

YOUTUBE_API_KEY='AIzaSyDkk2CIROIS5iDXxXktsDWEY_2JY4k4GUI'

youtube=build('youtube','v3',developerKey=YOUTUBE_API_KEY)


def  get_video_info(part,q,regionCode,num):
    dic_list=[]
    search_responce=youtube.search().list(part=part,q=q,order='viewCount',regionCode=regionCode,type='video')
    output=youtube.search().list(part=part,q=q,order='viewCount',regionCode=regionCode,type='video').execute()
  
    for i in range(num):
        dic_list=dic_list+output['items']
        search_responce=youtube.search().list_next(search_responce,output)
        output=search_responce.execute()
    
        
    df=pd.DataFrame(dic_list)
    df1=pd.DataFrame(list(df['id']))['videoId']
    df2=pd.DataFrame(list(df['snippet']))[['title','channelTitle','channelId']]
    ddf=pd.concat([df1,df2],axis=1)
    
    ddf1=ddf.drop(['channelTitle','title','videoId'],axis=1)
    dic_list2=[]
    for s in range(num*5):
        channelid=ddf1.iat[s,0]
        request=youtube.channels().list(part='snippet,contentDetails,statistics',id=channelid)
        output2=youtube.channels().list(part='snippet,contentDetails,statistics',id=channelid).execute()
        dic_list2=dic_list2+output2['items']
        
    ddfa=pd.DataFrame(dic_list2)
    ddfb=pd.DataFrame(list(ddfa['statistics']))[['subscriberCount','viewCount','videoCount']]
    ddfc=pd.concat([ddf,ddfb],axis=1)
    ddfc['videoId']='https://youtube.com/watch?v='+ddfc['videoId']
    return ddfc

sh=input('検索したいキーワドを入力:')

result=get_video_info(part='snippet',q=sh,regionCode='JP',num=20)

result.to_csv(f'/Users/shigematsuyuuki/pyauto/{sh}の検索結果.csv',index=False)
