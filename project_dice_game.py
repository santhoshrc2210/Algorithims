'''helps you select a strategy to maximise the chances
of winning for a given list of dice'''

from itertools import combinations

def count_wins(dice1, dice2):
    pos_comb=[]
    dice1_wins=0
    dice2_wins=0
    for ele in dice1:
        for ele_2 in dice2:
            if ele>ele_2:
                dice1_wins+=1
            elif ele_2>ele:
                dice2_wins+=1
    return (dice1_wins,dice2_wins)


def find_the_best_dice(dices):
    #list of indices for dices
    idx_of_dice=range(len(dices))
    #creating a list to keep scores for dice
    scores_lst=[]
    for idx in range(len(dices)):
        scores_lst.append(0)
    #list of all possible combinations
    comb = combinations(idx_of_dice, 2)
    for each_comb in list(comb):
      dices_idx=list(each_comb)
      scores=count_wins(dices[dices_idx[0]],dices[dices_idx[1]])
      a=list(scores)
      if a[0]>a[1]:
        scores_lst[dices_idx[0]]+=1
      elif a[1]>a[0]:
        scores_lst[dices_idx[1]]+=1
    max_score=len(dices)-1
    if max_score in scores_lst:
      return scores_lst.index(max_score)
    else:
      return -1

def compute_strategy(dices):
  check_strategy=find_the_best_dice(dices)
  if check_strategy!=-1:
    strategy={'choose_first': True, 'first_dice': check_strategy}
  else:
    strategy={'choose_first': False}
    #list of indices for dices
    idx_of_dice=range(len(dices))
    #creating a list to keep scores for dice
    scores_lst=[]
    for idx in range(len(dices)):
        scores_lst.append(0)
    #list of all possible combinations
    comb = combinations(idx_of_dice, 2)
    for each_comb in list(comb):
      dices_idx=list(each_comb)
      scores=count_wins(dices[dices_idx[0]],dices[dices_idx[1]])
      a=list(scores)
      if a[0]>a[1]:
        strategy = {**strategy, **{dices_idx[1]: dices_idx[0]}}
      elif a[1]>a[0]:
        strategy = {**strategy, **{dices_idx[0]:dices_idx[1]}}

  return strategy
