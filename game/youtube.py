from json import loads
from subprocess import check_output, CalledProcessError
import re

from aniso8601 import parse_duration
from tlslite import HTTPTLSConnection


google_domain = 'www.googleapis.com'
url_fmt = (
    '/youtube/v3/videos?'
    'alt=json&'
    'part=snippet%2Cstatistics%2CcontentDetails&'
    'id={id}'
    '&key=AIzaSyDLcq3oxp3VFhFJlQKZqqmeSrB7xoizkx8'
)


class Video(object):
    @classmethod
    def from_url(cls, url):
        return cls.from_id(
            re.search(r'(/|\bv=)(?P<id>[a-zA-Z0-9_-]{11})\b', url).group('id')
        )

    @classmethod
    def from_id(cls, video_id):
        connection = HTTPTLSConnection(google_domain, 443)
        connection.request('GET', url_fmt.format(id=video_id))
        result = loads(connection.getresponse().read())
        return cls(result['items'][0])

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


def paste():
    for binary, args in [
        ('xclip', ['-o']),
        ('pbpaste', []),
    ]:
        try:
            check_output(['which', binary])
        except CalledProcessError:
            continue

        return from_url(check_output([binary] + args))


def from_url(url):
    return Video.from_url(url)


if __name__ == '__main__':
    print(Video.from_id('wZZ7oFKsKzY'))
    print(Video.from_url('woofaiodsjae/wZZ7oFKsKzY jiaosjdosa'))
    print(Video.from_url('/wZZ7oFKsKzY'))
    print(Video.from_url(
        'https://www.youtube.com/watch?v=yCOJwZzBiVo&list=PLDEA007FAB5D8F479'))
