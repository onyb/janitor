from urllib.parse import urlencode

import requests

from optimizers.IOptimizerInterface import IOptimizerInterface


class WhitespaceRemover(IOptimizerInterface):
    def __init__(self):

        self.uri = 'http://closure-compiler.appspot.com/compile'
        self.headers = {'Content-type': 'application/x-www-form-urlencoded'}
        self.level = 'WHITESPACE_ONLY'  # Closure compilation level

    def process(self, code: str) -> str:
        params = urlencode([
            ('js_code', code),
            ('compilation_level', self.level),
            ('output_format', 'text'),
            ('output_info', 'compiled_code'),
        ])

        response = requests.post(self.uri, params=params, headers=self.headers)

        if response.status_code == 200:
            return response.text.strip()
        else:
            raise Exception
