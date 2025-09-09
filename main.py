# 在这个文件下编写代码，题目具体要求见README.md文件
input_str = input()

num = float(input_str[:-2])

unit = input_str[-2:]

if unit == "kg":
    
    pound = num * 2.2046
    print(f"对应的英制重量为{pound:.3f}磅")
elif unit == "pd":
    
    kg = num / 2.2046
    print(f"对应的公制重量为{kg:.3f}公斤")
else:
    print("输入单位错误，请输入'kg'或'pd'")
