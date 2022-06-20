from googleapiclient.discovery import build
from src.get_video_information import Video

if __name__ == '__main__':
    # Enter your youtube_api_key
    YOUTUBE_API_KEY = ''

    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    search_word = input('Enter Searching key words : ')

    video_info_processor = Video(youtube = youtube)
    result = video_info_processor.get_video_info(part='snippet', q=search_word, regionCode='JP', num=20)

    result.to_csv(f'./result/result_of_{search_word}.csv', index=False)
    print('crawling finished.')
