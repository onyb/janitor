from formatters.IFormatterInterface import IFormatterInterface
from csscompressor import compress


class CSSFormatter(IFormatterInterface):
    def __init__(self):
        pass

    def process(self, code: str) -> str:
        return compress(code)
