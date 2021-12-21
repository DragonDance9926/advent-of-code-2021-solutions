from itertools import product,cycle
from functools import lru_cache

roll = tuple(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))


p1 = 8
p2 = 5
@lru_cache(maxsize=None)
def play2(my_pos, my_score, other_pos, other_score):
	if my_score >= 21:
		return 1, 0

	if other_score >= 21:
		return 0, 1

	my_wins = other_wins = 0

	for die in roll:
		new_pos   = (my_pos + die) % 10
		new_score = my_score + new_pos + 1

		ow, mw = play2(other_pos, other_score, new_pos, new_score)
		my_wins    += mw
		other_wins += ow

	return my_wins, other_wins



wins = play2(p1, 0, p2, 0)
best = max(wins)
print(best)