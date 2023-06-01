from tennis import Player, Match, Set, Game

nadal = Player("Rafael Nadal", 2000)
djokovic = Player("Novak Djokovic", 2000)

test_match = Match(nadal, djokovic)
test_set = Set(test_match)
test_game = Game(test_set)

print(test_game.score)
test_game.score_point(nadal)
print(test_game.score)

test_game.score_point(nadal)
print(test_game.score)

test_game.score_point(djokovic)
print(test_game.score)

