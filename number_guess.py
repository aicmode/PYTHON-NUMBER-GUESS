import random

answer = random.randint(1, 100)
count = 0

print("=== 数当てゲーム ===")
print("1〜100の数字を当ててください！")

while True:
    guess = int(input("数字を入力："))
    count += 1

    if guess < answer:
        print("もっと大きい！")
    elif guess > answer:
        print("もっと小さい！")
    else:
        print("正解です！")
        print(f"{count}回目で当たりました！")
        break