import os
from height_weight_validator import validate_height, validate_weight

try:
    # 環境変数から取得してfloatに変換
    height = validate_height(float(os.getenv("HEIGHT")))
    weight = validate_weight(float(os.getenv("WEIGHT")))

    # BMI計算
    bmi = weight / ((height / 100) ** 2)
    print(f"BMIは {bmi:.2f}")

except Exception as e:
    print(f"エラー: {e}")
