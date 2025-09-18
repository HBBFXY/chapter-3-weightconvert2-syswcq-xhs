earth_weight=40
moon_weight=earth_weight*0.165
for i in range[1,11]:
    earth_weight=earth_weight+0.5
print(f"第{i}年：地球体重{earth_weight}kg，月球体重{moon_weight:.2f}kg")
