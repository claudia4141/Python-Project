import datetime as dt
from dateutil.parser import parse
import random
import matplotlib.pyplot as plt
import os

r_path = os.path.abspath(os.path.dirname(__file__))
CHEATERS = os.path.join(r_path, 'assignment-final-data/cheaters.txt')
KILLS = os.path.join(r_path, 'assignment-final-data/kills.txt')



class Cheater:
    """A class that stores cheaters' info."""
    def __init__(self):
        self.cheaters = {}
        self.read_cheating()

    def read_cheating(self):
        with open(CHEATERS, 'r') as f:
            for line in f.readlines():
                line = line.strip().split('\t')
                self.cheaters[line[0]] = {
                    'start': parse(line[1]), 'end': parse(line[2])}

    def is_cheater_now(self, account, now: dt.datetime):
        if account in self.cheaters:
            if self.cheaters[account]['start'] <= now:
                return True
        return False

    def is_cheater_in_5d(self, account, now: dt.datetime):
        if self.is_cheater_now(account, now):
            return False
        date = now + dt.timedelta(days=5)
        return self.is_cheater_now(account, date)


def counter(cheaters: Cheater, kills_line):
    """count the observer-cheater motif"""
    game = ''
    cheat_count = {'': 0}
    count = 0
    for line in kills_line:
        if not line:
            break
        line = line.strip().split('\t')
        if game != line[0]:
            game = line[0]
            cheat_count = {'': 0}
        winner = line[1]
        loser = line[2]
        t = parse(line[3])
        if max(cheat_count.values()) >= 3:
            if cheaters.is_cheater_in_5d(loser, t):
                count += 1
            if cheaters.is_cheater_in_5d(winner, t):
                count += 1
        elif cheaters.is_cheater_now(winner, t):
            if winner not in cheat_count:
                cheat_count[winner] = 1
            else:
                cheat_count[winner] += 1
            if cheaters.is_cheater_in_5d(loser, t):
                count += 1
    return count


def shuffle(cheaters: Cheater):
    """shuffle the players"""
    f = open(KILLS, 'r')
    fnew = []
    last_game = None
    lines = []
    no_cheaters = []
    x = 0
    for line in f.readlines():
        x += 1
        ls = line.strip().split('\t')
        game = ls[0]
        t = parse(ls[3])
        for player in ls[1:3]:
            if not cheaters.is_cheater_now(
                    player, t) and player not in no_cheaters:
                no_cheaters.append(player)
        if last_game and last_game != game:
            ori = no_cheaters[:]
            random.shuffle(no_cheaters)
            lst = ''.join(lines).split('\t')
            dic = {k: v for k, v in zip(ori, no_cheaters)}
            text = []
            for i in lst:
                if i in dic:
                    i = dic[i]
                text.append(i)
            fnew.extend('\t'.join(text).strip().split('\n'))
            lines = []
            no_cheaters = []
        lines.append(line)
        last_game = game
    ori = no_cheaters[:]
    random.shuffle(no_cheaters)
    lst = ''.join(lines).split('\t')
    dic = {k: v for k, v in zip(ori, no_cheaters)}
    text = []
    for i in lst:
        if i in dic:
            i = dic[i]
        text.append(i)
    fnew.extend('\t'.join(text).strip().split('\n'))
    f.close()
    return fnew


def main():
    """main function"""
    c = Cheater()
    with open(KILLS, 'r') as kills_file:
        kills_line = kills_file.readlines()
    n = counter(c, kills_line)
    l = []
    for i in range(10):
        lines = shuffle(c)
        l.append(counter(c, lines))
    plt.axvline([n], color='r')
    plt.hist(l)
    plt.show()
    print(l)
    print(n)


if __name__ == '__main__':
    main()
