lang_dict = {
    'gameName': 'TEST game name',
    'player': {
        'name': ['Как вас зовут? ', str],
        'old': ['Сколько вам лет? ', int],
        'sex': ['Ваш пол? (м/ж)', str],
        'pet': ['Имя питомца:', str],
        'hobby': ['Играть любишь? (да/нет)', bool]
    },
    'type': {
        int: 'целым числом!',
        bool: '(да/нет)'
    },
    'exception': {
        'old': {
            'false': 18,
            'confirm': 90
        },
        'gameplay': {
            'false': 'stop'
        }
    },
    'steps': {
        'old': {
            'false': {
                'text': 'Наша игра для взрослых. от 18 лет!',
                'res': False
            },
            'confirm': {
                'text': 'это для него может быть утомительно!',
                'res': False
            }
        }
    }
}

print(lang_dict['gameName'])

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
        print('Вам меньше < 18 прощайте')
        break

    if player['old'][1] > 90:

        user_result = input('Вы уверены? (да/нет)').lower()

        if (user_result == 'да') or (user_result =='нет'):
            if user_result == 'нет':
                break
        else:
            continue

        user_result = input('Вы точно уверены? (да/нет)').lower()

        if (user_result == 'да') or (user_result =='нет'):
            if user_result == 'нет':
                break
            else:
                print('Хорошо, тогда начнём игру!')
        else:
            continue


    print('Я могу назвать буквы алфавита, которых нет в твоем имени (',player['name'][1],')\n')

    rus_symbols = ''.join([chr(i) for i in range(ord('а'),ord('а')+32)])
    res = ''

    for num_str in str(rus_symbols):
        if num_str not in player['name'][1].lower():
            res = res + num_str

    print('Ответ: ', res)
    break


print('Выход из игры!')
