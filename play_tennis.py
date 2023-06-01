from tennis import Player, Match, Set

nadal = Player("Rafael Nadal", 2000)
djokovic = Player("Novak Djokovic", 2000)

test_match = Match(nadal, djokovic)
test_set = Set(test_match)

while test_set.is_running():
    test_set.play_game()
    print(str(test_set))
print(test_set.winner)
