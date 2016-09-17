from optimizers.SimpleJSOptimizer import SimpleJSOptimizer

import unittest
from textwrap import dedent


class TestSimpleJSOptimizer(unittest.TestCase):
    def setUp(self):
        self.opt = SimpleJSOptimizer()

    def test_variable_condensation(self):
        code = 'var i = 0; var x = 1;'
        response = self.opt.process(code)
        assert response == 'var i=0,x=1;'

    def test_variable_rename(self):
        code = dedent('''
        var x =function(i_am_a_variable, i_am_another_variable){
            alert(i_am_a_variable);
            alert(i_am_another_variable);
        };
        ''')
        response = self.opt.process(code)
        assert response == 'var x=function(a,b){alert(a);alert(b)};'

    def test_constant_expressions(self):
        code = 'var n = 2 + 2;'
        response = self.opt.process(code)
        assert response == 'var n=4;'
