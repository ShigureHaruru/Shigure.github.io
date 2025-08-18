from os import system
import openai
import datetime


client = openai.OpenAI(
    
    api_key = "",
    base_url = "https://api.deepseek.com/v1"    # 初始化OpenAI客户端

    )


def GET_WEATHER_AND_USER(UserName,Weather):     # 获取用户姓名及当天天气
    
    current_time = datetime.datetime.now()      # 获取当前时间

    current_hour = current_time.hour            #判断当前时间段
    if 6 <= current_hour < 12 :
        time_of_day = "早上"
    elif 12 <= current_hour < 18:
        time_of_day = "下午"
    else :
        time_of_day = "晚上"

    
    # 构建Prompt
    prompt = f"""请根据以下信息生成一句简短友好的问候语：    
    - 现在是一天当中的{time_of_day}
    - 用户名叫{name}
    - 今天的天气是{Weather}

    要求：
    1.包含用户姓名
    2.提到时间或天气
    3.不超过20个字
    4. 只输出问候语，不要包含其他任何说明文字
    """


    try :
        # 调用api
        response = client.chat.completions.create(
            
            model = "deepseek-chat",
            messages = [{"role": "user" , "content" : prompt}],
            temperature=0.7,  # 文本随机性与创造性
            max_tokens=50,   # 限制最大生成长度
            stream = False    # 关闭流式传输

            )

        return response.choices[0].message.content.strip()  #  response.choices[0]  调取API返回的候选响应列表第一个
                                                            #  message.content      用于提取ai回复的文本内容
                                                            #  strip                移除文本开头和结尾的所有空白字符


    except Exception as e :          # 如果调用失败，获取错误信息并输出

        print(f"API调用失败:{e}")
        return f"非常抱歉，亲爱的{UserName},祝您生活愉快！"






print("===欢迎使用智能问候生成器===")
name = input("请输入您的用户名:")
Weather = input("今天的天气如何？(如：晴天，阴天，多云...):")
OUT = GET_WEATHER_AND_USER(name,Weather);
print("\n 已生成你的专属问候:")
print(OUT)
system("pause")



        



        



                
            


