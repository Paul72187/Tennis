# Tennis

## Overview

This tennis app is split into three parts - 1. ManualScore, 2. SimulatedScore and 3. Tournament.

## 1. Aim (ManualScore)

The ManualScore is designed to follow the format of a best of 5 set tennis match between two players. Users manually input each point of each game for either Player 1 or Player 2 to determine which player wins the point and ultimately who wins each game, each set and the entire match. There is the additional feature to settle a set on a tie-break should the two players make it to 6 games all in a given set.

## 2. Aim (SimulatedScore)

The SimulatedScore is designed to follow the format of a best of 5 set tennis match between two players. Unlike the ManualScore above, the SimulatedScore uses the Random module in Python to generate game, set and match scores at random and therefore the outcome of the match is not determined by user input.

The outcome of 100 matches between the two players is simulated at random. The score for each match is listed, together the winner. At the bottom of the list of 100 matches, the total number of wins for each of the two players is displayed, together with the distribution of the matches that were won over 3, 4 or 5 sets.

The next feature takes into account the ranking points of the two players contesting the match. If the match is simulated with one player holding more ranking points than the other, the percentage chance of the player with the higher number of ranking points winning is increased. If both players enter the match with the same number of ranking points, there is an equal chance of either player emerging triumphant.

The final feature uses the matplotlib module to graphically plot the probability of Player1 winning the match (in one graph) and the probability of Player1 winning the match in 3 sets (straight sets) (in the other graph).

## How the app was built

The app was built using Python.

## To Run

Clone the repo: git clone https://github.com/Paul72187/Tennis.git

## Start Tennis app

Which version?

1. To play the ManualScore version, cd into the ManualScore folder and run python3 play_tennis.py

2. To play the SimulatedScore verison, cd into the SimulatedScore folder and run python3 play_tennis.py
