# coding=utf-8

from json import loads
import re
import webbrowser

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


PLAYLIST_LENGTH = 5


class Playlist(list):
    @property
    def length(self):
        return len(self)

    @property
    def formatted(self):
        return u'\n'.join([u' • {}'.format(v.title) for v in self])

    @property
    def remaining(self):
        return PLAYLIST_LENGTH - self.length

    @property
    def certificate_text(self):
        return u'\n'.join([u'{}. {}'.format(i+1, v.title)
                           for i, v in enumerate(self)])

    @property
    def stats(self):
        return 'YOU SOLD FORTY BILLION COPIES'

    def is_complete(self):
        return len(self) >= PLAYLIST_LENGTH

    def with_video(self, video):
        return Playlist(self + [video])


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
        self.channel = item['snippet']['channelTitle']
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

    def is_already_in_playlist(self, playlist):
        return self.id in [v.id for v in playlist]

    def is_psy(self):
        return self.channel == 'officialpsy'

    def is_gangnam_style(self):
        return self.id == '9bZkp7q19f0'

    def is_short(self):
        return self.duration.seconds < 90


def paste():
    clipboard = pyperclip.paste()
    if clipboard:
        return from_url(clipboard)


def from_url(url):
    return Video.from_url(url)


def open_youtube():
    for video_id in [
        'usxrnYRZf_g&t=25s',
        'IkfuLA5GMCA',
        'eFO0Xo9TZ54',
        '_etl_qkelX0',
    ]:
        webbrowser.open('https://youtube.com/watch?v={0}'.format(video_id))


if __name__ == '__main__':
    print(Video.from_id('wZZ7oFKsKzY'))
    print(Video.from_url('woofaiodsjae/wZZ7oFKsKzY jiaosjdosa'))
    print(Video.from_url('/wZZ7oFKsKzY'))
    print(Video.from_url(
        'https://www.youtube.com/watch?v=yCOJwZzBiVo&list=PLDEA007FAB5D8F479'))
