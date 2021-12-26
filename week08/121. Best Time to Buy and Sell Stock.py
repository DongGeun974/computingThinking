# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：121. Best Time to Buy and Sell Stock.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-26 오후 10:37 
'''
import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
        return profit