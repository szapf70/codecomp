import json

from copy import deepcopy
from datetime import datetime

import codewars_test as test

from solution import teknonymize
from preloaded import _person

def _test_teknonymize(input_, actual, expected):
    if actual != expected:
        print(f"<LOG::-Input>{input_}")
        print(f"<TAB::-Actual>{json.dumps(actual, default=str)}")
        print(f"<TAB::-Expected>{json.dumps(expected, default=str)}")
        test.fail("Test failed")
    else:
        test.assert_equals(actual, expected)


@test.describe("Sample Tests")
def _():
    def get_example():
        persons = [_person() for _ in range(8)]
        dates = ['1000-01-01', '1020-01-01', '1021-02-01', '1023-11-28', '1047-01-01', '1043-11-01', '1045-01-01', '1046-01-01']
        sexes = ['m', 'f', 'm', 'm', 'f', 'f', 'f', 'm']
        names = 'abcdhefg'
        dates = map(datetime.fromisoformat, dates)
        for p, n, d, s in zip(persons, names, dates, sexes):
            p['name'] = n
            p['date_of_birth'] = d
            p['sex'] = s
        persons[1]['children'].append(persons[4])
        persons[3]['children'].extend(persons[-3:])
        persons[0]['children'].extend(persons[1:4])
        actual = persons[0]
        expected = deepcopy(actual)
        expected['teknonym'] = 'grandfather of e'
        expected['children'][0]['teknonym'] = 'mother of h'
        expected['children'][2]['teknonym'] = 'father of e'
        return actual, expected
    
    actual, expected = get_example()

    @test.it("It should manage a person without child")
    def _():
        act = deepcopy(actual['children'][0]['children'][0])
        exp = deepcopy(expected['children'][0]['children'][0])
        input_ = deepcopy(actual)
        teknonymize(act)
        _test_teknonymize(input_, act, exp)

    @test.it("It should manage a person with children")
    def _():
        act = deepcopy(actual['children'][2])
        exp = deepcopy(expected['children'][2])
        input_ = deepcopy(actual)
        teknonymize(act)
        _test_teknonymize(input_, act, exp)

    @test.it("It should manage a family tree with three generations")
    def _():
        act = deepcopy(actual)
        exp = deepcopy(expected)
        input_ = deepcopy(actual)
        teknonymize(act)
        _test_teknonymize(input_, act, exp)

    @test.it("It should manage a family tree with five generations")
    def _():
        def get_big_tree():
            persons = [_person() for _ in range(11)]
            dates = ['1000-01-01', '1020-01-01', '1021-02-01', '1023-11-28', '1047-01-01', '1043-11-01', '1045-01-01', '1046-01-01', '1067-01-01', '1068-01-01', '1087-01-01']
            sexes = ['m', 'f', 'm', 'm', 'f', 'f', 'f', 'm', 'f', 'm', 'm']
            names = 'abcdhefgijk'
            dates = map(datetime.fromisoformat, dates)
            for p, n, d, s in zip(persons, names, dates, sexes):
                p['name'] = n
                p['date_of_birth'] = d
                p['sex'] = s
            persons[1]['children'].append(persons[4])
            persons[3]['children'].extend(persons[5:8])
            persons[0]['children'].extend(persons[1:4])
            persons[5]['children'].extend(persons[8:10])
            persons[8]['children'].append(persons[-1])
            actual = persons[0]
            expected = deepcopy(actual)
            expected['teknonym'] = 'great-great-grandfather of k'
            expected['children'][0]['teknonym'] = 'mother of h'
            expected['children'][2]['teknonym'] = 'great-grandfather of k'
            expected['children'][2]['children'][0]['teknonym'] = 'grandmother of k'
            expected['children'][2]['children'][0]['children'][0]['teknonym'] = 'mother of k'
            return actual, expected
        
        act, exp = get_big_tree()
        input_ = deepcopy(act)
        teknonymize(act)
        _test_teknonymize(input_, act, exp)

    @test.it("It should check the dates of birth properly")
    def _():
        act = {"date_of_birth": datetime.fromisoformat("1000-01-01 17:12:06.360932"), "sex": "f", "name": "a", "children": [ {"date_of_birth": datetime.fromisoformat("1030-09-17 17:12:06.360972"), "sex": "f", "name": "b", "children": [], "teknonym": ""},  {"date_of_birth": datetime.fromisoformat("1030-01-08 17:12:06.360954"), "sex": "f", "name": "c", "children": [], "teknonym": ""} ], "teknonym": ""}
        exp = deepcopy(act)
        input_ = deepcopy(act)
        exp['teknonym'] = 'mother of c'
        teknonymize(act)
        _test_teknonymize(input_, act, exp)