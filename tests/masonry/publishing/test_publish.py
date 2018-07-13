from pathlib import Path

from poetry.io import NullIO
from poetry.masonry.publishing import Publisher
from poetry.poetry import Poetry


def project(name):
    return Path(__file__).parent / "fixtures" / name


def test_cannot_publish_private_package():
    poetry = Poetry.create(project("private"))
    publisher = Publisher(poetry, NullIO())
    publisher._uploader = None
    assert not publisher.publish(None, None, None)


class NullUploader:
    def auth(self, username, password):
        pass

    def upload(self, url):
        pass


def test_publish():
    poetry = Poetry.create(project("complete"))
    publisher = Publisher(poetry, NullIO())
    publisher._uploader = NullUploader()
    assert publisher.publish(None, 'foo', 'bar')
