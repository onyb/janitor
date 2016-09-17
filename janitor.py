from django.http import HttpResponse

from utils.Exceptions import IncorrectResponseError
from utils.HTMLParser import HTMLParser


class janitor(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        resp = self.f(*args)
        if isinstance(resp, HttpResponse):
            html = resp.content.decode()
            parser = HTMLParser(html)
            parser.js_parser()
            parser.css_parser()

            return HttpResponse(parser.soup)
        else:
            raise IncorrectResponseError
