from tennis import Player, Match, Set, Game

nadal = Player("Rafael Nadal", 2000)
djokovic = Player("Novak Djokovic", 2000)

test_match = Match(nadal, djokovic)
test_set = Set(test_match)
test_game = Game(test_set)

test_game.score_point(nadal)

print(test_game.players)
print(test_game.is_running())
print(test_game.get_winner())
