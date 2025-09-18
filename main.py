earth_weight = 50  
moon_rate = 0.165
yearly_growth = 0.5
print("未来10年地球与月球体重变化：")
for year in range(1, 11):
    earth_weight += yearly_growth
    moon_weight = earth_weight * moon_rate
    print(f"第{year}年：地球体重{earth_weight}kg，月球体重{moon_weight:.2f}kg")
