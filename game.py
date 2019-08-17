__author__ = 'Буров А.С.'

# Вым необходимо:
# При старте игры вывести на экран Название Игры (его надо придумать)
# *Запросить у пользователя: *
#     Имя
#     Возраст
#     Пол
#     Имя питомца
#     Либит-ли игрок играть (хранить как булевое значение, но ответ принимать в виде Да/Нет)
#
# Проверить есть ли игроку 18 лет, если нет, оповестить что ему играть нельзя.
# Проверить что игроку не более 90 лет, если больше уведомить игрока что, это для него может быть утомительно и задать вопрос уверен-ли он что хочет играть (Да/Нет), если игрок ввел Да - задать вопрос снова ( да у нас перестраховывается игра), при повторном Да - сказать: Хорошо тогда начнем игру. В случае если игрок дал отказ, попрощаться по Имени, и завершить игру.
#
# Если Игрок в диапозоне 18-90: Поприветсвовать игрока по имени. !! — не корректно откидывать > 90; так что условие работает
# если от 18+
# Игра должна сказать: Я могу назвать буквы алфавита, которых нет в твоем имени. и Произнести их. (тут нужен цикл)
#
# На данном этапе игра завершается и в следующем уроке мы сделаем немного больше интерактива.

lang_dict = {
    'gameName': 'Игра от скуки!',
    'player': {
        'name': ['Как вас зовут? (рус. сим) ', str],
        'old': ['Сколько вам лет? ', int],
        'sex': ['Ваш пол? (м/ж)', str],
        'pet': ['Имя питомца:', str],
        'hobby': ['Играть любишь? (да/нет)', bool]
    },
    'type': {
        int: 'целым числом!',
        bool: '(да/нет)'
    }
}

print(lang_dict['gameName'])
print("""／ﾌﾌ 　　　　　 　　 　ム｀ヽ
/ ノ)　　 ∧　　∧　　　　）　ヽ
/ ｜　　(´・ω ・`）ノ⌒（ゝ._,ノ
/　ﾉ⌒＿⌒ゝーく　 ＼　　／
丶＿ ノ 　　 ノ､　　|　/
　　 `ヽ `ー-‘人`ーﾉ /
　　　 丶 ￣ _人’彡ﾉ
　　　／｀ヽ _/\__'""")

player = lang_dict['player']
player_counter = True;
for key in player:
    while player_counter is True:

        data_type = player[key][1]

        user_result = input(player[key][0])

        if (bool(user_result) is not True):
            print('Ответ ваш не может быть пустым!')
            continue

        if 'bool' in str(data_type):
            if user_result.lower() in '(да/yes)':
                player[key][1] = True
                break
            elif user_result.lower() in '(нет/no)':
                player[key][1] = False
                break
            else:
                print('Ответ дожен быть — ', lang_dict['type'][data_type])
                continue

        try:
            data_type(user_result)
            player[key][1] = data_type(user_result)
            break
        except ValueError:
            print('Ответ дожен быть — ', lang_dict['type'][data_type])
            continue

print(player)

while True:
    if player['old'][1] < 18:
        print('Наша игра для взрослых. от 18 лет!')
        break

    if player['old'][1] > 90:

        user_result = input('Бро, игра утомительна! Оно тебе надо? :)  (да/нет)').lower()

        if (user_result == 'да') or (user_result == 'нет'):
            if user_result == 'нет':
                break
        else:
            continue

        user_result = input('Вы точно уверены? (да/нет)').lower()

        if (user_result == 'да') or (user_result == 'нет'):
            if user_result == 'нет':
                break
            else:
                print('Хорошо, тогда начнём игру!')
        else:
            continue

    print('Я могу назвать буквы алфавита, которых нет в твоем имени (', player['name'][1], ')\n')

    rus_symbols = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])
    res = ''

    for num_str in str(rus_symbols):
        if num_str not in player['name'][1].lower():
            res = res + num_str

    print('Ответ: ', res)
    break

print('Выход из игры!')
