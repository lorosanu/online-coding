#!/usr/bin/python3

def depositProfit(deposit, rate, threshold):
    money = deposit
    years = 0
    while money < threshold:
        money += (rate / 100 * money)
        years += 1
    return years

