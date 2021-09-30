from balance_checker import check_balance as cb
import mock
import builtins


class TestCheckBalance:

    def test_check_balance_true_1(self):
        assert cb('(((([{}]))))') == True

    def test_check_balance_true_2(self):
        assert cb('[([])((([[[]]])))]{()}') == True

    def test_check_balance_true_3(self):
        assert cb('{{[()]}}') == True

    def test_check_balance_false_1(self):
        assert cb('}{}') == False

    def test_check_balance_false_2(self):
        assert cb('{{[(])]}}') == False

    def test_check_balance_false_3(self):
        assert cb('[[{())}]') == False