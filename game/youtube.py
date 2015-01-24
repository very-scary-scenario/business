from aniso8601 import parse_duration
from googleapiclient.discovery import build


youtube = build(
    'youtube', 'v3', developerKey='AIzaSyDLcq3oxp3VFhFJlQKZqqmeSrB7xoizkx8')


class Video(object):
    @classmethod
    def from_url(cls, url):
        raise NotImplementedError

    @classmethod
    def from_id(cls, video_id):
        return cls([
            i for i in youtube.videos().list(
                id=video_id, part='snippet,statistics,contentDetails'
            ).execute()['items']
        ][0])

    def __init__(self, item):
        self.title = item['snippet']['title']
        self.duration = parse_duration(item['contentDetails']['duration'])
        self.views = int(item['statistics']['viewCount'])
        self.comments = int(item['statistics']['commentCount'])
        self.likes = int(item['statistics']['likeCount'])
        self.dislikes = int(item['statistics']['dislikeCount'])

    def __str__(self):
        return (
            '{title}\n{duration}; views: {views}; likes: {likes}; '
            'dislikes: {dislikes}'.format(**self.__dict__)
        )


if __name__ == '__main__':
    print(Video.from_id('wZZ7oFKsKzY'))
