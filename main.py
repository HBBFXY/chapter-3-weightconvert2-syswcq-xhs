initial_weight = float(input("请输入您在地球上的初始体重(kg)：")
weight_earth=initial_weight
for year in range(1，11):
    weight_earth += 0.5
    weight_moon = weight_earth * 0.165
    print(f"第{year}年 - 地球体重：{weight_earth}kg，月球体重：{weight_moon：.2f}kg")
