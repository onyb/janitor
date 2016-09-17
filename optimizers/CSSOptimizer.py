from urllib.parse import urlencode

import requests

from optimizers.IOptimizerInterface import IOptimizerInterface
from formatters.CSSFormatter import CSSFormatter
import cssutils


class CSSOptimizer(IOptimizerInterface):
    def __init__(self):
        self.processed = []
        self.css = ''

    def process(self, code: str) -> str:
        clean_css = CSSFormatter().process(code)
        sheet = cssutils.parseString(clean_css)

        for rule in sheet:
            if rule.style.cssText in self.processed:
                continue

            idx = [
                {
                    'style': _rule.style.cssText,
                    'selector': _rule.selectorText
                }
                for _rule in sheet if _rule.style.cssText == rule.style.cssText
                ]
            print(idx)

            if len(idx) > 1:
                self.css += ' ' + ','.join([i['selector'] for i in idx]) + '{' + idx[0]['style'] + '}'
            else:
                self.css += ' ' + rule.selectorText + '{' + rule.style.cssText + '}'

            self.processed.append(rule.style.cssText)

        return self.css.strip()
