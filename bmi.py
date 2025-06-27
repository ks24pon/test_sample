import os

# 環境変数から身長と体重を取得
height_cm = float(os.getenv("HEIGHT"))
weight_kg = float(os.getenv("WEIGHT"))

# BMI計算
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

# 小数第2位まで表示
print(f"BMIは {bmi:.2f}")