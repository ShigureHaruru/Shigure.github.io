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

    # 判断当前时间段
    current_hour = time.hour
    
    if 6 <= current_hour < 12 :
        time_of_day = "早上"
    elif 12 <= current_hour < 18:
        time_of_day = "下午"
    else :
        time_of_day = "晚上"

    # 返回当前时间段
    return time_of_day


# 调用大模型
def llm(name,time,sc,fg,weather):

    # 初始化
    client = openai.OpenAI(

        base_url = "https://api.deepseek.com/v1",

        api_key = ""
        )


    # 构建prompt
    prompt = f"""
    请根据以下给出的信息生成一段不超过30字的问候语：
    - 1.现在是一天当中的 : {time}
    - 2.用户名 : {name}
    - 3.用户现在在 : {sc}
    - 4. 当前天气情况为 : {weather}
    - 5. 问候语的风格为 : {fg}

    要求：
    1.不超过20字
    2.自然融入所有要素
    3.必须出现用户名
    4.问候语言风格为{fg}
    5.仅输出问候语

    """
    
    # 发送请求
    response = client.chat.completions.create(
        # 指定模型
        model = "deepseek-chat",
    
        messages = [{"role" : "user" , "content" : prompt}],

        # 文本随机性
        temperature = 0.7,

        # 最大tokens数 
        max_tokens = 80,

        # 关闭流式传输
        stream = False 
        )

    #  strip移除文本开头和结尾的所有空白字符
    response = response.choices[0].message.content.strip()

    # 返回结果
    return response


# 主程序
print("===欢迎使用问候语生成器===")
print()

# 获取用户名 :
name = input("请输入您的用户名:")

# 获取用户当前场景及所期望的回复风格
sc = input("你现在在什么地方？(学校/公司/足球场...)：")

fg = input("你希望获得什么风格的问候语(温馨/幽默/励志...):")

# 执行函数获取时间及天气
weather = Get_Weather()

time = Get_time()

# 传参调用大模型
response = llm(name,time,sc,fg,weather)

# 输出结果
print("===已为您生成专属问候语!===")
print(response)






