import math
# правильных ответов
answer_count = 0
# всего ответов
answer_sum =0
# правильный ответ
answer1 = 'лампочка'
answer_u1 = None
#нет ответов
not_answer_count=0
# не правильный ответ
not_answer_1 =0



answer_u1 = input("""
напишиет ответ на загадку, для пропуска вопроса нажмите enter.
Висит груша - нельзя скушать?
""")
if bool(answer_u1) == False:
    print('Вы не стали отвечать на этот вопрос')
    not_answer_count = not_answer_count + 1
else:
    answer_sum = answer_sum + 1

if answer1.lower() == answer_u1.lower():
    print('вы ответили правильно')
    answer_count = answer_count+1
if answer1.lower() != answer_u1.lower() and bool(answer_u1) != False:
    print('вы ответили не верно')
    not_answer_1 = not_answer_1 + 1
print('всего ответов: ', answer_sum)
print('правильных ответов: ', answer_count)
print('не правильных ответов: ', not_answer_1)
print('вопросов без ответа: ', not_answer_count)

