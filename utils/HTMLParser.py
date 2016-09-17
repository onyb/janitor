from bs4 import BeautifulSoup

from optimizers.AdvancedJSOptimizer import AdvancedJSOptimizer
from optimizers.CSSOptimizer import CSSOptimizer

class HTMLParser(object):
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'lxml')

    def js_parser(self):
        for script in self.soup.find_all('script'):
            opt = AdvancedJSOptimizer()
            script.string = opt.process(script.string)

    def css_parser(self):
        for style in self.soup.find_all('style'):
            opt = CSSOptimizer()
            style.string = opt.process(style.string)