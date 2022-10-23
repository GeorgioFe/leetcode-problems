def max_profit(prices):
  max_profit = 0
  for i in range(len(prices)):
    for j in range(1, len(prices)):
      new_max = prices[j] - prices[i]
      if new_max > max_profit and j > i:
        max_profit = new_max
        print("New Max is: " + str(max_profit))
  return max_profit