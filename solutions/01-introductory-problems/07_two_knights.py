# https://cses.fi/problemset/task/1072

#   K * *   * * K   K *   * K
#   * * K   K * *   * *   * *
#                   * K   * *
# 
# * these are the 4 possible arrangements in which 
#   knights are attacking each other, which can be
#   repeatedly placed on board.
# * first two arrangements can be placed (n - 2) times
#   in one row and (n - 1) times in one column
#   last two arrangements can be placed (n - 1) times
#   in one row and (n - 2) times in one column
# * since there are such four arrangements and each 
#   arrangement can be repeated (n - 1) * (n - 2) times
#   there are 4 * (n - 1) * (n - 2) arrangements in
#   which knights are attacking each other.
# * there are total (n ^ 2) * (n ^ 2 - 1) / 2 possible
#   arrangements in which two knights can be placed on
#   n * n board.
# * by subtracting number of arrangements in which two 
#   knights are attacking each other from total number
#   of arrangements, we get number of arrangements in
#   which knights are not attacking each other.

n = int(input())
for k in range(1, n + 1):
    print(int((k ** 2) * (k ** 2 - 1) / 2) - (4 * (k - 1) * (k - 2)))
