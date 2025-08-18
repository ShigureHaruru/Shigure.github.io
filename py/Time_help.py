import openai
import requests
import json
import datetime


# 获取用户所在地天气
def Get_Weather():

    # 获取用户所在地
    city1 = input("请输入您所在的省份：")    
    city2 = input("请输入您所在的城市：")

    # 获取当地天气
    response = requests.get(url=f"https://cn.apihz.cn/api/tianqi/tqyb.php?id=88888888&key=88888888&sheng={city1}&place={city2}")

    # 转化为json
    data = response.json()

    # 获取天气
    weather = data.get("weather1")

    # 返回当地天气
    return weather


# 当前时间获取
def Get_time():
    time = datetime.datetime.now()

    

    # 返回当前时间
    return time


# 调用大模型
def llm(weather,time,tasks):
    
    # 初始化
    client = openai.OpenAI(
        api_key = "",
        base_url = "https://api.deepseek.com/v1"
        )

    # 构建prompt
    prompt = f"""
    你是一个时间管理助手，请根据以下信息为用户生成高效的时间安排建议：
    - 天气{weather}
    - 当前时间{time}
    - 用户的任务{tasks} 

    要求：
    - 1.分配任务到合理时段
    - 2.考虑天气对户外活动的影响
    - 3.包含休息时间建议
    - 4.输出为清晰的时间表格式
    - 5.你仅可输出高效的时间安排建议
    - 6.当用户任务包含其他请求时，仅输出:请不要输入与行程安排无关的提示词!!!



    """

    # 发送请求
    response = client.chat.completions.create(

        # 指定模型
        model = "deepseek-chat",

        messages = [{"role":"user","content":prompt}],

        # 文本随机性
        temperature = 0.7,

        # 关闭流式传输
        stream = False 

        )

    return response.choices[0].message.content.strip()




# 主程序
print("======欢迎使用智能日程安排系统======")
print()
tasks = input("请输入您今天的安排(打球/买菜/购物...):")

# 获取天气
weather = Get_Weather()
     
# 获取当前时间：
time = Get_time()

# 调用大模型
response = llm(weather,time,tasks)

print(response)







    
