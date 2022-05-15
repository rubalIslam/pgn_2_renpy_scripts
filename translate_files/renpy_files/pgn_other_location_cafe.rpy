label loc_cafe_time:
    $ qtime += 1
    jump loc_cafe

label loc_cafe_var:
    if ((qtime >= 18 and daysn != 6) or (qtime >= 17 and daysn == 6)) and olivia_path < 6:
        $ location = ["loc_cafe"]
        jump table_pgn_map
    if ((qtime >= 18 and daysn != 6) or (qtime >= 17 and daysn == 6)) and olivia_path >= 6:
        jump loc_olivhomenew

    if vicky_path == 8 and qtime == 16 and daysn == 6:
        jump vicky_path_09_lazyharry
    if vicky_path == 11 and qtime == 16 and daysn == 6:
        jump vicky_path_12_lazyharry
    if vicky_path == 14 and qtime == 17 and daysn != 6:
        jump vicky_path_15_lazyharry
    if vicky_path == 14 and qtime == 16 and daysn == 6:
        jump vicky_path_15_lazyharry
    if vicky_path >= 15 and ("vickyhome_sex") in ivent24 and daysn != 6 and qtime == 17:
        jump vicky_path_sex_lazyharry
    if vicky_path >= 15 and ("vickyhome_sex") in ivent24 and daysn == 6 and qtime == 16:
        jump vicky_path_sex_lazyharry

    if olivia_path == 2 and qtime == 15:
        jump pgn_newolivhome_03
    scene bg pgn_loc_cafe_liza_04
    call screen loc_cafe

label loc_cafe_choice:
    scene bg pgn_loc_cafe_liza_01
    v emo-168 "Приветик, [pname_max[0]]! Очень рада тебя видеть. Чего бы ты хотел сегодня?"
    $ menu_hbox = True
    menu:
        "Выпить кофе":
            jump pgn_loc_cafe_solo
        "{color=#87c500}МОД_04 :{/color} Хм, ещё не знаю" if vicky_path == 0:
            jump vicky_path_01_lazyharry
        "{color=#87c500}МОД_04 :{/color} Насчет свидания" if vicky_path == 10:
            jump vicky_path_11_lazyharry
        "{color=#87c500}МОД_04 :{/color} Насчет свидания" if vicky_path == 13 and qtime >= 12 and qtime <= 17 and daysn != 6:
            jump vicky_path_14_lazyharry
        "{color=#87c500}МОД_04 :{/color} Насчет свидания" if vicky_path == 13 and qtime >= 12 and qtime <= 16 and daysn == 6:
            jump vicky_path_14_lazyharry
        "{color=#87c500}МОД_04 :{/color} Сегодня у тебя?" if vicky_path >= 15 and ("vickyhome_sex") not in ivent24:
            jump vicky_path_sex_lazyharry_time
        "Кофе с собой":
            jump loc_cafe_buy
        "Назад":
            jump loc_cafe

screen loc_cafe:
    add "gui/loc_nav_bottom.png"
    vbox:
        xalign 0.5
        text _("{size=40}{color=#ffffff}{font=hermes.ttf}ДЕНЬ [days]{/font}{/color}{/size}") xalign 0.5
        text "{size=30}{color=#ffffff}{font=hermes.ttf}[daysweek]{/font}{/color}{/size}" xalign 0.5 ypos -3
        textbutton "{size=53}{color=#ffffff}{font=hermes.ttf}[qtime]:00{/font}{/color}{/size}" xalign 0.5 ypos -13
    hbox:
        xalign 0.98
        if currency_color == False:
            text "{size=80}{color=#ffffff}{font=hermes.ttf}$[currency]{/font}{/color}{/size}"
        if currency_color == True:
            text "{size=80}{color=#c21f1f}{font=hermes.ttf}$[currency]{/font}{/color}{/size}"

    hbox:
        align (0.98, 0.95)
        imagebutton idle "images/nav/nav_time_a.png" hover "images/nav/nav_time_b.png" action Jump("loc_cafe_time")


    if olivia_path >= 6:
        hbox:
            align (0.02, 1.0)
            if _preferences.language is None:
                imagebutton idle "nav_olivhome_a" hover "nav_olivhome_b" action Jump("loc_olivhomenew")
            if _preferences.language == "en":
                imagebutton idle "en_nav_olivhome_a" hover "en_nav_olivhome_b" action Jump("loc_olivhomenew")


    hbox:
        align (1.0, 0.95)
        imagebutton idle "images/nav/nav_speak_a.png" hover "images/nav/nav_speak_b.png" action Jump("loc_cafe_choice") xpos -166
        imagebutton idle "images/nav/nav_phone_a.png" hover "images/nav/nav_phone_b.png" action Jump("table_main") xpos -166
    hbox:
        align (0.98, 1.0)
        imagebutton idle "images/nav/nav_map_a.png" hover "images/nav/nav_map_b.png" action Jump("table_pgn_map") ypos -178
    hbox:
        align (0.98, 1.0)
        imagebutton idle "images/nav/nav_inventory_a.png" hover "images/nav/nav_inventory_b.png" action Jump("table_pgn_inventory") ypos -312







label pgn_loc_cafe_liza:
    scene bg pgn_loc_cafe_liza_04
    l emo-43 "Привет, Вика! [pname_max[0]], возьми кофе, я за столиком подожду..."
    m emo-0 "Ага, хорошо..."
    scene bg pgn_loc_cafe_liza_01
    v emo-168 "Приветик, [pname_max[0]]! Очень рада вас снова видеть... Как обычно, два кофе?"
    m emo-0 "А что насчёт десертов?"
    v emo-164 "Всё ещё не рекомендую... Но кофе, как и прежде, отличный. Так что, два?"
    m emo-0 "Ага, спасибо..."
    v emo-165 "Если что, зови."
    m emo-3 "Спасибо!"
    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[11])+" $"+"20")
    $ currency -= 20
    scene bg pgn_loc_cafe_liza_02
    m emo-0 "Как дела в школе?"
    l emo-41 "Нормально, учусь хорошо. Новых друзей завожу."
    m emo-5 "Парня себе присматриваешь?"
    l emo-50 "[pname_max[0]]! Ну ты же знаешь, что ты... мой парень. Так что зачем мне искать другого."
    if vicky_path == 0:
        l emo-41 "Как продвигается с Викой?"
        m emo-0 "Пока ни как."
        l emo-43 "Ну ты давай думай, интересно, получится ли у тебя что-то с ней или... нет."
    if vicky_path == 4:
        l emo-41 "Как продвигается с Викой?"
        m emo-3 "В процессе."
        l emo-43 "Хорошо. Интересно, получится ли у тебя что-то с ней или... нет."
    if vicky_path == 9:
        l emo-41 "Как продвигается с Викой?"
        m emo-3 "У нас было первое свидание."
        l emo-43 "Молодец и как всё прошло?"
        m emo-4 "Да так, ничего особенного, поговорили, выпили и разошлись."
        l emo-41 "Давай дерзай... У меня есть на вас планы, так что дерзай."
        m emo-13 "Планы!? Какие планы?"
        l emo-43 "Тебе пока рано знать. Допивай кофе."
    $ label_random = renpy.random.randint ( 1, 2)
    if label_random != 2:
        $ label_random = 0
        pass
    if label_random == 2:
        $ label_random = 0
        l emo-41 "[pname_max[0]], можешь купить мне ещё кофе? Уж очень вкусно."
        $ menu_hbox = True
        menu:
            "Да":
                $ menu_hbox = True
                menu:
                    "Один кофе":
                        m emo-0 "Вика! Принеси пожалуйста ещё один стаканчик кофе."
                        play sound "content/audio/long_expected.mp3" noloop
                        $ renpy.notify(str(task_notifi[11])+" $"+"10")
                        $ currency -= 10
                    "Два кофе":
                        m emo-0 "Вика! Принеси нам пожалуйста ещё по стаканчику."
                        play sound "content/audio/long_expected.mp3" noloop
                        $ renpy.notify(str(task_notifi[11])+" $"+"20")
                        $ currency -= 20
                scene bg pgn_loc_cafe_liza_03
                v emo-161 "Вот ваш заказ."
                l emo-41 "Спасибо."
                scene bg pgn_loc_cafe_liza_02
                $ renpy.pause ( 3, 0)
            "Нет":
                m emo-0 "Извини, но нет. Ты и так очень активная и много кофе пить вредно."
    l emo-40 "Мы тут уже засиделись, так что пойдем домой."
    scene bg pgn_loc_cafe_liza_04
    l emo-41 "Вика, пока!"
    m emo-3 " Пока!"
    v emo-173 "До свидания [pname_max[0]] и [pname_liza[0]]. Приходите ещё!"
    $ qtime += 1
    $ location = ["loc_cafe"]
    jump loc_pool_move

label pgn_loc_cafe_solo:
    scene bg pgn_loc_cafe_liza_01
    m emo-0 "Кофе, просто кофе..."
    v emo-165 "Просто кофе? А как же десерты? Шучу. Они всё ещё ужасные. Хотя, некоторым нравятся..."
    $ menu_hbox = True
    menu:
        "Тогда да, просто кофе...":
            pass
        "Может быть, попробовать?":
            v emo-170 "Не, не надо. Ты мне нужен живой. А то кто будет ходить в кафе..."

    m emo-0 "Спасибо, Вика..."
    $ currency -= 10
    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[11])+" $"+"10")
    scene bg pgn_loc_cafe_liza_04
    m emo-4 "{i}Хороша девчонка, но неприступная как дверь сейфа... Ну ничего, у меня есть к тебе ключик подходящий...{/i}"
    $ menu_hbox = True
    menu:
        "Продолжить пить кофе":
            pass
        "Позвать Вику":
            scene bg pgn_loc_cafe_liza_05
            v emo-165 "Да, [pname_max[0]], ещё кофе?"
            $ menu_hbox = True
            menu:
                "Может, поболтаем?":
                    v emo-177 "[pname_max[0]]... Мы уже это проходили. Ты всё знаешь. Могу помочь тебе только с кофе. А если будешь настаивать, накормлю десертом."
                    m emo-13 "Угрожаешь..."
                    v emo-165 "Ага. Ну так что, ещё кофе? За счёт заведения..."
                    m emo-0 "Ну давай..."
                    scene bg pgn_loc_cafe_liza_07
                    m emo-2 "{i}Эх... Но стоило попытаться. Ладно, кажется, мне пора...{/i}"
                    jump pgn_loc_cafe_solo_exit
                "Ага, если можно...":
                    v emo-165 "Конечно, можно! Это же кофейня."
                    m emo-0 "Спасибо!"
                    play sound "content/audio/long_expected.mp3" noloop
                    $ renpy.notify(str(task_notifi[11])+" $"+"10")
                    $ currency -= 10
                    scene bg pgn_loc_cafe_liza_07
                    $ renpy.pause ( 3, 0)
                    jump pgn_loc_cafe_solo_exit
    scene bg pgn_loc_cafe_liza_07
    m emo-0 "{i}Эх... Ладно, загляну в другой раз.{/i}"
label pgn_loc_cafe_solo_exit:
    scene bg pgn_loc_cafe_liza_01
    v emo-168 "Пока, [pname_max[0]]! Была рада тебя видеть. Приходи ещё!"
    m emo-3 "Обязательно!"
    $ qtime += 1
    jump table_pgn_map





label loc_cafe_buy:
    m emo-3 "Мне два кофе с собой."
    v emo-169 "Сейчас приготовлю."
    v emo-169 "Ты же обычно пьёшь здесь. Куда-то спешишь?"
    menu:
        "[pname_liza[0]] попросила":
            m emo-13 "[pname_liza[0]] попросила меня съездить и купить ей."
            v emo-172 "Передавай ей от меня привет"
            m emo-4 "Конечно."
        "Много дел":
            m emo-0 "У меня сегодня много дел, нужна подзарядка."
            v emo-160 "Ясно. Держи."
    $ v_coffee_1.have = True
    $ v_coffee_1.numbsuse += 2
    $ currency -= v_coffee_1.price*2
    jump loc_cafe
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
