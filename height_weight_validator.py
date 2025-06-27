def validate_height(value):
    if value < 100 or value > 200:
        raise ValueError(f"{value}cmは無効です。身長は100〜200cmの間で指定してください。")
    return value

def validate_weight(value):
    if value < 30 or value > 150:
        raise ValueError(f"{value}kgは無効です。体重は30〜150kgの間で指定してください。")
    return value
