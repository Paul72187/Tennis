from tennis import Player, Match

nadal = Player("Rafael Nadal", 2000)
djokovic = Player("Novak Djokovic", 2000)

print(nadal.name)
print(nadal.ranking_points)
print(djokovic.name)
print(djokovic.ranking_points)

nadal.update_ranking_points(125)
print(nadal.ranking_points)
djokovic.update_ranking_points(75)
print(djokovic.ranking_points)
