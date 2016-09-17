from optimizers.WhitespaceRemover import WhitespaceRemover
import unittest
from textwrap import dedent


class TestWhitespaceRemover(unittest.TestCase):
    def setUp(self):
        self.opt = WhitespaceRemover()

    def test_single_line_comments(self):
        code = 'alert("hello");// This comment should be stripped'
        response = self.opt.process(code)
        assert response == 'alert("hello");'

    def test_multiline_comments(self):
        code = dedent('''
        /* This is a bogus comment, which
         * happens to be multiline.
         */

        alert("hello");

        /* Some more comments just to prove
         * my point.
         */
        ''')

        response = self.opt.process(code)
        assert response == 'alert("hello");'
