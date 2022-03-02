# Python-Project

## Background
This project studies the social contagion of cheating on the massive multiplayer online game PlayerUnknown's Battlegrounds (PUBG). Cheating in this context means the adoption of unapproved software that gives the player an unfair advantage in the game (e.g. being able to see through walls). The hypothesis is that players who observe cheating become likely to adopt cheating themselves. To test this hypothesis, we need to first count how many observers of cheaters become cheaters within a certain period of time. We will call these observer–cheater motifs. Then, to simulate alternative universes in which the players played the same game but happened to be killed by someone else. Finally, we will compare how the count of the observer–cheater motifs observed in the actual data compares to what we would expect in a "randomized" world.

## Process
Step 1: Observers of cheating start cheating<br />
Cheating players can be recognized because they exhibit abnormal killing patterns. We will assume that player A realizes that cheating occurs if either:
cheating player B kills at least 3 other players before A gets killed in the game
or
A is killed by cheating player B.
Count how many players observed at least one cheater and then started cheating within the next 5 days. We will assume here that we can only talk about a causal relationship if the two events (observing a cheater and starting to cheat) are relatively proximate in time (within 5 days of each other). In essence, we are looking for temporal motifs in which payer A observes B and then A becomes cheater, but the timing between the two events should not be more than 5 days.

Step 2: Simulating an alternative universe<br />
To establish causality, we will simulate an alternative world in which everything is the same but the events took somewhat different sequence. If observing cheating causes cheating, in the randomized world we will observe fewer observer–cheater motifs than in reality. To simulate an alternative universe, we will keep the timing and structure of interactions but randomly assign the identities of players. There are certain restrictions we need to observe, however:
Randomize within a game, not between games.Since cheaters may tend to kill more or kill at a specific period in the game, we will preserve their position in the killing network. That is, only non-cheaters should be randomly reassigned.

Step 3: Evaluating reality against alternative universes<br />
Conduct 10 randomizations for the data. Then plot the number of observer–cheater motifs observed in the actual data (use a vertical line) compared to the distribution you get in the randomized data (using a histogram)
