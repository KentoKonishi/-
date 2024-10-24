def calculate_change(payment, price):
    # おつりの計算
    change = payment - price

    # 硬貨の種類（高額な順）
    coins = [500, 100, 50, 10]
    coin_count = {}

    # おつりが0以上の場合に処理
    if change > 0:
        print(f"おつり: {change}円")

        for coin in coins:
            # 硬貨の枚数計算
            count = change // coin
            if count > 0:
                coin_count[coin] = count
                change -= coin * count

        # 結果の表示
        for coin, count in coin_count.items():
            print(f"{coin}円: {count}枚")
    else:
        print("おつりはありません。")

def vending_machine():
    # 入力を受け付ける
    try:
        price = int(input("商品の価格を入力してください（円）: "))
        payment = int(input("支払い金額を入力してください（円）: "))

        if payment < price:
            print("支払い金額が不足しています。")
        else:
            calculate_change(payment, price)

    except ValueError:
        print("有効な金額を入力してください。")

# 自動販売機システムの実行
if __name__ == "__main__":
    vending_machine()
