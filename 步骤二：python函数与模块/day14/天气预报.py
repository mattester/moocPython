#北京,2019年1月12日,多云,8°C,-4°C,南风3级~上海,2019年1月12日,小雨,9°C,6°C,北风2级~广州,2019年1月12日,阵雨转多云,22°C,15°C,持续无风向微风
weath_str = "北京,2019年1月12日,多云,8°C,-4°C,南风3级~上海,2019年1月12日,小雨,9°C,6°C,北风2级~广州,2019年1月12日,阵雨转多云,22°C,15°C,持续无风向微风"
city_list = weath_str.split("~")
weath_date = {}
for i in range(0,len(city_list)):
    w = city_list[i].split(",")
weath = {
    "name" : w[0],"date":w[1],"weater":w[2],"max":w[3],"min":w[4],"wind":w[5]}
weath_date[weath["name"]] = weath