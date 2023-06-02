import matplotlib.pyplot as plt

from tennis import Player, Match

n_simulations = 100

n_player_1_wins = []
n_3_set_matches = []

nadal = Player("Rafael Nadal", 2000)
djokovic = Player("Novak Djokovic", 2000)

winners = {nadal: 0, djokovic: 0}
n_sets = {3: 0, 4: 0, 5: 0}

for _ in range (n_simulations):
    match = Match(nadal, djokovic)
    match.simulate_match()
    match.suppress_output()
    match.play_match()

    print(match, match.winner)

    winners[match.winner] += 1
    n_sets[len(match.sets)] += 1

print(winners)
print(n_sets)

ranking_percentages = range(40, 60)
for ranking_percentage in ranking_percentages:
    nadal = Player("Rafael Nadal", ranking_percentage)
    djokovic = Player("Novak Djokovic", 100-ranking_percentage)
    winners = {nadal: 0, djokovic: 0}
    n_sets = {3: 0, 4: 0, 5: 0}
    for _ in range(n_simulations):
        match = Match(nadal, djokovic)
        match.simulate_match()
        match.suppress_output()
        match.play_match()
        winners[match.winner] += 1
        n_sets[len(match.sets)] += 1
    print(f"\nRanking ratio: {match.ranking_ratio}")
    print(f"Player 1 winning percentage: {winners[nadal] / n_simulations * 100}%")
    print(f"Percentage of 3-set matches: {n_sets[3] / n_simulations * 100}%")
    print(f"Percentage of 4-set matches: {n_sets[4] / n_simulations * 100}%")
    print(f"Percentage of 5-set matches: {n_sets[5] / n_simulations * 100}%")
    print(f"\nRanking ratio: {match.ranking_ratio}")
    print(f"Player 1 winning percentage: {winners[djokovic] / n_simulations * 100}%")
    print(f"Percentage of 3-set matches: {n_sets[3] / n_simulations * 100}%")
    print(f"Percentage of 4-set matches: {n_sets[4] / n_simulations * 100}%")
    print(f"Percentage of 5-set matches: {n_sets[5] / n_simulations * 100}%")

    print(f"\nRanking ratio: {match.ranking_ratio}")
    n_player_1_wins.append(winners[nadal] / n_simulations * 100)
    print(f"Player 1 winning percentage: {n_player_1_wins[-1]}%")
    n_3_set_matches.append(n_sets[3] / n_simulations * 100)
    print(f"Percentage of 3-set matches: {n_3_set_matches[-1]}%")

plt.style.use("Solarize_Light2")
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
ax1.plot(ranking_percentages, n_player_1_wins)
ax1.set_xlabel("Point win likelihood (%)")
ax1.set_ylabel("Match win likelihood (%)")
ax2.plot(ranking_percentages, n_3_set_matches)
ax2.set_xlabel("Point win likelihood (%)")
ax2.set_ylabel("3 set likelihood (%)")
plt.show()

