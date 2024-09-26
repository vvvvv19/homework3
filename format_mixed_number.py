# 格式化分数为带分数形式
def format_mixed_number(fraction):
    if fraction.denominator == 1:
        return str(fraction.numerator)  # 如果是整数，直接返回整数
    whole = fraction.numerator // fraction.denominator
    remainder = abs(fraction.numerator) % fraction.denominator
    if whole == 0:
        return str(fraction)  # 如果没有整数部分，直接返回分数
    elif remainder == 0:
        return str(whole)  # 如果没有余数，返回整数部分
    else:
        return f"{whole}'{remainder}/{fraction.denominator}"  # 返回带分数形式