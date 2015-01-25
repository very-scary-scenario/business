from json import loads
import re

from aniso8601 import parse_duration
import pyperclip
from tlslite import HTTPTLSConnection


google_domain = 'www.googleapis.com'
url_fmt = (
    '/youtube/v3/videos?'
    'alt=json&'
    'part=snippet%2Cstatistics%2CcontentDetails&'
    'id={id}'
    '&key=AIzaSyDLcq3oxp3VFhFJlQKZqqmeSrB7xoizkx8'
)


class Playlist(list):
    @property
    def length(self):
        return len(self)

    def __str__(self):
        if len(self) > 1:
            return (
                u'{}, and {}'.format(
                    u', '.join([v.title for v in self[:-1]]),
                    self[-1].title,
                )
            )
        elif len(self) == 1:
            return self[0].title
        else:
            return 'nothing'


class Video(object):
    @classmethod
    def from_url(cls, url):
        match = re.search(r'(/|\bv=)(?P<id>[a-zA-Z0-9_-]{11})\b', url)
        if match:
            return cls.from_id(
                match.group('id')
            )

    @classmethod
    def from_id(cls, video_id):
        try:
            connection = HTTPTLSConnection(google_domain, 443)
            connection.request('GET', url_fmt.format(id=video_id))
            result = loads(connection.getresponse().read())
            item = result['items'][0]
        except:
            return
        else:
            return cls(item)

    def __init__(self, item):
        self.id = item['id']
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

    def is_already_in_playlist(self):
        return self.id in [v.id for v in playlist]

    def is_short(self):
        return self.duration.seconds < 90


def paste():
    clipboard = pyperclip.paste()
    if clipboard:
        return from_url(clipboard)


def from_url(url):
    return Video.from_url(url)


playlist = Playlist()


if __name__ == '__main__':
    print(Video.from_id('wZZ7oFKsKzY'))
    print(Video.from_url('woofaiodsjae/wZZ7oFKsKzY jiaosjdosa'))
    print(Video.from_url('/wZZ7oFKsKzY'))
    print(Video.from_url(
        'https://www.youtube.com/watch?v=yCOJwZzBiVo&list=PLDEA007FAB5D8F479'))
