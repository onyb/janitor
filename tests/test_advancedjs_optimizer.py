from optimizers.AdvancedJSOptimizer import AdvancedJSOptimizer

import unittest
from textwrap import dedent


class TestSimpleJSOptimizer(unittest.TestCase):
    def setUp(self):
        self.opt = AdvancedJSOptimizer()

    def test_inlining(self):
        code = dedent('''
        var i_dont_know_how_to_name_variables = function() {
            var i = 0;
            alert(i);
        };
        i_dont_know_how_to_name_variables();
        ''')
        response = self.opt.process(code)
        assert response == 'alert(0);'

    def test_dead_code_removal(self):
        code = dedent('''
        var p = function(){
            alert('DEAD');
        };

        var q = function() {
            var i = 0;
            alert(i);
        };
        q();
        ''')
        response = self.opt.process(code)
        assert response == 'alert(0);'
