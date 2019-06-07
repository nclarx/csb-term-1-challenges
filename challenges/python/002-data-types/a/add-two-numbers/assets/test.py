#require_relative '../index.rb'

import answer

assert answer.add_two_numbers(10,20) == 30, "Should be 20"
assert answer.add_two_numbers(100,50) == 150, "Should be 100"
print("All tests passed! Well done")
