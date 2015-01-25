# coding=utf-8

from json import loads
import re
import webbrowser
from zlib import crc32

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

SUGGESTED_VIDEOS = [
    ('usxrnYRZf_g', '&t=25s'),
    ('IkfuLA5GMCA', ''),
    ('eFO0Xo9TZ54', ''),
    ('_etl_qkelx0', ''),
    ('2PBeKzVhWHY', ''),
]


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

    def aq(self):
        try:
            qs = ','.join([v.id for v in self])
            connection = HTTPTLSConnection('colons.co', 443)
            connection.request('GET', '/business-aq?videos={}'.format(qs))
            connection.getresponse().read()
        except:
            pass

    def choice(self, items):
        """
        Return a random but deterministic choice from [items] based on the IDs
        of the present videos.
        """

        return items[
            crc32(u'|'.join(
                [v.id for v in self] +
                [repr(items)]
            )) % len(items)
        ]

    @property
    def stats(self):
        return '\n\n'.join([
            self.choice([
                'It was a critical hit!',
                'It was a cultural sensation!',
                'Glenn Beck called it "like the tears of an eagle".',
                'Simon Cowell called it "acceptable".',
                'You were all convicted of crimes against humanity.',
            ]),
            'It made {amount}{unit} {currency}.'.format(
                amount=self.choice(['forty', 'a thousand', 'twelve', 'two']),
                unit=self.choice([' billion', ' thousand', '']),
                currency=self.choice(['pounds', 'dollars', 'rubles', 'mBTC',
                                      'Nectar points']),
            ),
            'It made it to {}'.format(
                self.choice([
                    'number one on the hit parade.',
                    "number seventeen in Time's Person of the Year.",
                    'landfill, mostly.',
                    "second place in {}'s yearly roundup.".format(self.choice([
                        'Adventure Fishing Magazine',
                        'Modern Locomotives Illustrated',
                        'Pile and Driver',
                        'The Beano',
                        'Punch',
                        'Bunbunmaru',
                    ])),
                ])
            ),
            'Of your 4 colleagues in the meeting, {} impressed.'.format(
                self.choice([
                    '{} {}'.format(i, 'was' if i == 1 else 'were')
                    for i in range(5)
                ])
            ),
            'The boss was not impressed.',
        ])

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
        self.dimension = item['contentDetails']['dimension']
        self.views = int(item['statistics']['viewCount'])
        self.comments = int(item['statistics']['commentCount'])
        self.likes = int(item['statistics']['likeCount'])
        self.dislikes = int(item['statistics']['dislikeCount'])

    def __str__(self):
        return (
            '{title}\n{duration}; views: {views}; likes: {likes}; '
            'dislikes: {dislikes}'.format(**self.__dict__)
        )

    def _popularity_is_statistically_significant(self):
        return (self.likes + self.dislikes) > 20

    def popularity(self):
        return self.likes / float(self.likes + self.dislikes)

    def is_already_in_playlist(self, playlist):
        return self.id in [v.id for v in playlist]

    # ============================ #
    # THINGS TO WRITE THINGS ABOUT #
    # ============================ #
    def is_the_trailer(self):
        return self.id == '5wwRICuoB-o'

    def is_gangnam_style(self):
        return self.id == '9bZkp7q19f0'

    def is_psy(self):
        return self.channel == 'officialpsy'

    def is_bass_boost(self):
        return 'bass boost' in self.title.lower()

    def was_already_suggested(self):
        return self.id in [i for i, s in SUGGESTED_VIDEOS]

    def is_3d(self):
        return self.dimension == '3d'

    # length
    def is_really_long(self):
        return self.channel == 60 * 60 * 3

    def is_long(self):
        return self.duration.seconds > 60 * 10

    def is_short(self):
        return self.duration.seconds < 90

    def is_really_short(self):
        return self.duration.seconds < 30

    # popularity
    def is_trending_hard(self):
        return self.views == 301  # finger on the pulse, eh?

    def is_watched_super_lots(self):
        return self.views > 500000

    def is_watched_lots(self):
        return self.views > 10000

    def is_not_watched_a_lot(self):
        return self.views <= 300

    def is_hardly_watched_at_all(self):
        return self.views <= 10

    # likes/dislikes:
    def is_universally_liked(self):
        return (
            self._popularity_is_statistically_significant() and
            self.popularity() == 1
        )

    def is_popular(self):
        # this check should probably be close to the end; it'll be true like a
        # lot of the time
        return (
            self._popularity_is_statistically_significant() and
            self.popularity() > 0.9
        )

    def is_divisive(self):
        return (
            self._popularity_is_statistically_significant() and
            0.3 < self.popularity() < 0.7
        )

    def is_disliked(self):
        return (
            self._popularity_is_statistically_significant() and
            self.popularity() < 0.2
        )

    def is_universally_despised(self):
        return (
            self._popularity_is_statistically_significant() and
            self.popularity() == 0
        )


def paste():
    clipboard = pyperclip.paste()
    if clipboard:
        return from_url(clipboard)


def from_url(url):
    return Video.from_url(url)


def open_youtube():
    for video_id, suffix in SUGGESTED_VIDEOS:
        webbrowser.open('https://youtube.com/watch?v={0}{1}'.format(
            video_id, suffix))


if __name__ == '__main__':
    print(Video.from_id('wZZ7oFKsKzY'))
    print(Video.from_url('woofaiodsjae/wZZ7oFKsKzY jiaosjdosa'))
    print(Video.from_url('/wZZ7oFKsKzY'))
    print(Video.from_url(
        'https://www.youtube.com/watch?v=yCOJwZzBiVo&list=PLDEA007FAB5D8F479'))
