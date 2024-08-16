
# Max Profit from Stock Prices

This guide explains how to implement the algorithm to determine the maximum profit that can be achieved by buying and selling a stock on different days. The solution is written in Python, utilizing a two-pointer technique.

## Problem Statement

Given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day, find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times), but you must sell the stock before you buy again.

### Example 1

![Max Profit Example](https://assets.leetcode.com/users/images/c0c86dc7-f7fa-4be7-85f9-61e629aa67ae_1643686591.6894035.jpeg)

**Input:**
- prices = [7, 1, 5, 3, 6, 4]

**Output:**
- 5

**Explanation:**
- Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
- Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2

**Input:**
- prices = [7, 6, 4, 3, 1]

**Output:**
- 0

**Explanation:**
- In this case, no transactions are done, and the max profit = 0.

## Code Implementation

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize two pointers
        l = 0  # Left pointer, represents the day to buy
        r = 1  # Right pointer, represents the day to sell
        maxProfit = 0  # Variable to store the maximum profit

        # Iterate through the price list
        while r < len(prices):
            # If current selling price is higher than buying price
            if prices[l] < prices[r]:
                # Calculate the profit
                profit = prices[r] - prices[l]
                # Update the maximum profit if the current profit is higher
                maxProfit = max(profit, maxProfit)
            else:
                # Move the left pointer to the current day if it's better to buy
                l = r
            # Move the right pointer to the next day
            r += 1
        
        return maxProfit
```

### Explanation:
- **Two-pointer Approach**: The algorithm uses two pointers to track the potential buying and selling days.
  - The `left` pointer (`l`) is for the day we buy the stock.
  - The `right` pointer (`r`) is for the day we sell the stock.
- If the selling price is higher than the buying price, the profit is calculated and the maximum profit is updated.
- If the selling price is lower than or equal to the buying price, the buying day is updated to the current selling day.

### Example Usage

```python
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: prices = {prices1}")
    print(f"Output: {solution.maxProfit(prices1)}")
    print("Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.")
    print()

    # Example 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Input: prices = {prices2}")
    print(f"Output: {solution.maxProfit(prices2)}")
    print("Explanation: In this case, no transactions are done and the max profit = 0.")
    print()
```

## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of days (i.e., the length of the `prices` list). This is because the list is traversed once.
- **Space Complexity:** O(1), as only a constant amount of extra space is used for variables (`l`, `r`, and `maxProfit`).

This solution is efficient and handles scenarios where no profitable transactions are possible.
