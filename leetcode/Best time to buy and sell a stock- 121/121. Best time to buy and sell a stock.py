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


# Example usage
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

"""
Notes:
- The function `maxProfit` determines the maximum profit that can be achieved by buying and selling a stock on different days.
- The algorithm uses a two-pointer approach to traverse the list of prices, where `l` represents the buying day and `r` represents the selling day.
- If the selling price is greater than the buying price, it calculates the profit and updates the maximum profit encountered so far.
- If the selling price is less than or equal to the buying price, the buying day is updated to the current selling day.

Time Complexity:
- The time complexity of this approach is O(n), where n is the number of days (i.e., the length of the prices list). This is because the list is traversed once.

Space Complexity:
- The space complexity is O(1), as only a constant amount of extra space is used for variables (`l`, `r`, and `maxProfit`).

Test Cases:
1. **Input:** prices = [7, 1, 5, 3, 6, 4]
   - **Output:** 5
   - **Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

2. **Input:** prices = [7, 6, 4, 3, 1]
   - **Output:** 0
   - **Explanation:** In this case, no transactions are done and the max profit = 0.
"""
