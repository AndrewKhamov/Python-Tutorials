def rec():
    n = int(input())
    if n!=0:
        rec()
        print(n)


rec()


# 1) Запиши названное число
#
# 2) Если число не последнее – потереби следующего за тобой человека, пришла его очередь работать
#
# 3) Когда следующий за тобой человек сказал, что он закончил – назови записанное число
#
# 4) Скажи тому, кто тебя теребил (предыдущий человек), что ты закончил
#
# Формализуем задачу. Пусть задается последовательность натуральных чисел,
# заканчивающаяся нулем. Необходимо развернуть ее с помощью рекурсии.
