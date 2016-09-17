from optimizers.CSSOptimizer import CSSOptimizer
import unittest
from textwrap import dedent


class TestCSSoptimizer(unittest.TestCase):
    def setUp(self):
        self.opt = CSSOptimizer()

    def test_style_condensation(self):
        code = dedent('''
        p {color: black}
        h1 {color: black}
        h2 {color: black}
        h3 {color: gray}
        ''')

        response = self.opt.process(code)
        assert response == 'p,h1,h2{color: black} h3{color: gray}'