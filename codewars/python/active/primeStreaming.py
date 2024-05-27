# https://www.codewars.com/kata/5519a584a73e70fa570005f5/train/python
# Prime Streaming (PG-13)

class Primes:
    @staticmethod
    def stream():
        pass
    
"""
Create an endless generator that yields prime numbers. the generator must be able to produce a million primes in a few seconds

If this is too easy, try Prime Streaming (NC-17).


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        def verify(from_n, *vals):
            stream = Primes.stream()
            for _ in range(from_n): next(stream)
            for v in vals: test.assert_equals(next(stream), v)

        verify(0, 2,3,5,7,11,13,17,19,23,29)
        verify(10, 31,37,41,43,47,53,59,61,67,71)
        verify(100, 547,557,563,569,571,577,587,593,599,601)
        verify(1000, 7927,7933,7937,7949,7951,7963,7993,8009,8011,8017)

"""    