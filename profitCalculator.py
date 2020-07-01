def profitCalculator(arr):
  sell_price = 0
  buy_price = 0
  max_profit = -1
  change_price = True

  for i in range(0, len(arr)-1 ):
    sell_price = arr[i+1]

    if(change_price):
      buy_price = arr[i]

    if(sell_price < buy_price):
      change_price = True
      continue
    else:
      temp = sell_price - buy_price
      if(temp > max_profit):
        max_profit = temp
        change_price = False

  return max_profit

print(profitCalculator([44, 30, 24, 32, 35, 30, 40, 38, 15])) 