                        # append data from one list to another   
# l=[55,44,67,56]
# li=[]
# for i in l:
#     li.append(i)
# print(li)
# print(l)    
#                         now take this data and appened some other data
# houses_nested_list = [
#     [115910.26, 128.0, 4.0],
#     [48718.17, 210.0, 3.0],
#     [28977.56, 58.0, 2.0],
#     [36932.27, 79.0, 3.0],
#     [83903.51, 111.0, 3.0],
# ]

# for i in houses_nested_list:
#     print(i)
#     house=i[0]/i[1]
#     print(house)
#     i.append(house)
# print(houses_nested_list )    
#                          adding a new item in dictionary

# my_dict = {'name': 'Zain', 'age': 25}

# my_dict['city'] = 'Lahore'

# print(my_dict)
#                         separating dic from lists and the find the mean
# housing=[{'price_approx_usd': 115910.26, 'surface_covered_in_m2': 128, 'rooms': 4},
#  {'price_approx_usd': 48718.17, 'surface_covered_in_m2': 210, 'rooms': 3},
#  {'price_approx_usd': 28977.56, 'surface_covered_in_m2': 58, 'rooms': 2},
#  {'price_approx_usd': 36932.27, 'surface_covered_in_m2': 79, 'rooms': 3},
#  {'price_approx_usd': 83903.51, 'surface_covered_in_m2': 111, 'rooms': 3}]
# house_price=[]
# for house in housing:
    
#     house_price.append(house['price_approx_usd'])
# mean=sum(house_price)/len(house_price)    
# print(f"mean of housing prices {mean}")
#                                    now try to find price using this
houses_columnwise = {
    "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
} 
# price=sum(houses_columnwise["price_approx_usd"])/len(houses_columnwise["price_approx_usd"])
# print(price)
   
#                                      now calculate the price pr square inch
# houses_columnwise = {
#     "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
#     "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
#     "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
# }
# price=houses_columnwise["price_approx_usd"]
# area=houses_columnwise["surface_covered_in_m2"]
# zip(price,area)
# for p,a in zip(price,area):
#     print(f"price {p}")
#     print(f"area {a}")
#     print(f"total price per square inch {p/a} $")
#                               importing and working with pandas
# import pandas as pd
# houses_columnwise = {
#     "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
#     "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
#     "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
# }
# df_houses=pd.DataFrame(houses_columnwise)
# print(df_houses)
import pandas as pd
df1=pd.read_csv()






