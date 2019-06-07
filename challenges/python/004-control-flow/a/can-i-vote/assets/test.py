from answer import can_i_vote

assert can_i_vote(17) == "Whoops, you have to be at least 18 to vote."
assert can_i_vote(18) == "Hooray! You're old enough to have your say!"

print('Well done! All tests passed')