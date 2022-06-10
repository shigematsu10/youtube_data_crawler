import pandas as pd

class Video():
    def __init__(self, youtube):
        self.youtube = youtube

    def  get_video_info(self, part,q,regionCode,num):
        dic_list=[]
        search_responce = self.youtube.search().list(part=part, q=q, order='viewCount', regionCode=regionCode, type='video')
        output=self.youtube.search().list(part=part, q=q, order='viewCount', regionCode=regionCode, type='video').execute()
    
        for i in range(num):
            dic_list = dic_list+output['items']
            search_responce = self.youtube.search().list_next(search_responce, output)
            output = search_responce.execute()
        
        df = pd.DataFrame(dic_list)
        df1 = pd.DataFrame(list(df['id']))['videoId']
        df2 = pd.DataFrame(list(df['snippet']))[['title', 'channelTitle', 'channelId']]
        ddf = pd.concat([df1,df2], axis=1)
        
        ddf1 = ddf.drop(['channelTitle', 'title', 'videoId'], axis=1)
        dic_list2 = []
        for s in range(num*5):
            channelid = ddf1.iat[s, 0]
            request = self.youtube.channels().list(part='snippet,contentDetails,statistics', id=channelid)
            output2 = self.youtube.channels().list(part='snippet,contentDetails,statistics', id=channelid).execute()
            dic_list2 = dic_list2+output2['items']
            
        ddfa=pd.DataFrame(dic_list2)
        ddfb=pd.DataFrame(list(ddfa['statistics']))[['subscriberCount', 'viewCount', 'videoCount']]
        ddfc=pd.concat([ddf,ddfb], axis=1)
        ddfc['videoId']='https://youtube.com/watch?v='+ddfc['videoId']
        return ddfc