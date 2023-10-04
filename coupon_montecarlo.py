import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def exceed_target(unique, duplicate, target):
    if target > duplicate // exchange_rate + unique:
        #print(unique, duplicate)
        return False
    else:
        #print(unique, duplicate)
        return True
def run_success_length():
    uniques = []
    duplicates = []
    run_count = 0
    while run_count < target * exchange_rate:
        new_num = random.randint(1,target)
        if new_num in uniques:
            duplicates.append(new_num)
        else:
            uniques.append(new_num)
        unique = len(uniques)
        duplicate = len(duplicates)
        run_count += 1
        if run_count >= target:
            if exceed_target(unique, duplicate, target):
                return run_count
            else:
                continue

target = int(input("target: "))
exchange_rate = int(input("exchange rate: "))
trials = 1

trials_average_list = []
for i in range(trials):
    runs_per_trial = 5000 #############
    list_of_success = []
    for i in range(runs_per_trial):
        length = 0
        length = run_success_length()
        list_of_success.append(length)
    trials_average_list.append(sum(list_of_success)/runs_per_trial)
    print("The average is", sum(list_of_success)/runs_per_trial)
    print("It is {} times the target".format(sum(list_of_success)/runs_per_trial/target))
    
    data = pd.Series(list_of_success)

    # Histogram plot
    print(data.describe())
    plt.hist(data, bins=target, color='gray', edgecolor='black', alpha=0.7)
    plt.xlabel('Total Tries')
    plt.ylabel('Frequency')
    plt.title(f'Tries to get {target} Coupons')
    plt.xlim(0, data.max())
    plt.show()

#print("Total Average is", sum(trials_average_list)/len(trials_average_list))


