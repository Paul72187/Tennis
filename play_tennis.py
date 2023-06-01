from tennis import Player, Match

nadal = Player("Rafael Nadal", 2000)
djokovic = Player("Novak Djokovic", 2000)

test_match = Match(nadal, djokovic)

while test_match.is_running():
    test_match.play_set()

