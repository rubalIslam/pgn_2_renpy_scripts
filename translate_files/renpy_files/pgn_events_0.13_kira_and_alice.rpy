






label pgn_events_13_kira_bar_kiraclub_casting:
    $ qtime += 1
    if "kiraclub_g1" in ivent24:
        scene pgn_events_13_kiracast_g1_01
        $ renpy.pause()
        scene pgn_events_13_kiracast_g1_02
        m emo-1 "{i}Большая у неё задница.{/i}"
        scene pgn_events_13_kiracast_g1_03
        m emo-3 "{i}Тёте её попа тоже приглянулась.{/i}"
    elif "kiraclub_g2" in ivent24:
        scene pgn_events_13_kiracast_g2_01
        m emo-1 "{i}Пацанка-лесбиянка...{/i}"
        scene pgn_events_13_kiracast_g2_02
        m emo-1 "{i}Не стесняясь, сразу показывает свои намерения и желания.{/i}"
        scene pgn_events_13_kiracast_g2_03
        m emo-6 "{i}Зачем так спешить?!{/i}"
    elif "kiraclub_m1" in ivent24:
        scene pgn_events_13_kiracast_m1_01
        m emo-0 "{i}Это мужик мне сильно кое-кого напоминает...{/i}"
        scene pgn_events_13_kiracast_m1_02
        if ("spykiraclub") in accessiv:
            m emo-3 "{i}Тётя, да ты шлюшка. Набросилась на мужика.{/i}"
        else:
            m emo-11 "{i}Чёрт! Тётя, ну что же ты делаешь?! Меня тебе мало?!{/i}"
        m emo-0 "{i}Они уходят.{/i}"
        scene pgn_events_13_kiracast_m1_03
    elif "kiraclub_m2" in ivent24:
        scene pgn_events_13_kiracast_m2_01
        m emo-6 "{i}О чём-то разговаривают. Ничего не слышно.{/i}"
        scene pgn_events_13_kiracast_m2_02
        m emo-1 "{i}Закончили общение.{/i}"
        scene pgn_events_13_kiracast_m2_03
        m emo-6 "{i}Даже не знаю, стоит ли за ними проследить.{/i}"
    m emo-1 "{i}За ними дальше проследовать не смогу. Единственное место от куда могу, это посмотреть с той комнате, что над VIP.{/i}"
    if momkate_path >= 5:
        menu:
            "Подняться в \"Белую комнату\"":
                if "kiraclub_g1" in ivent24:
                    jump pgn_events_13_kiracast_g1
                elif "kiraclub_g2" in ivent24:
                    jump pgn_events_13_kiracast_g2
                elif "kiraclub_m1" in ivent24:
                    jump pgn_events_13_kiracast_m1
                elif "kiraclub_m2" in ivent24:
                    jump pgn_events_13_kiracast_m2
            "уйти":
                jump jump_dialogue

label pgn_events_13_kira_bar_kiraclub_casting_next:
    if "kiraclub_g1" in ivent24:
        jump pgn_events_13_kiracast_g1
    elif "kiraclub_g2" in ivent24:
        jump pgn_events_13_kiracast_g2
    elif "kiraclub_m1" in ivent24:
        jump pgn_events_13_kiracast_m1
    elif "kiraclub_m2" in ivent24:
        jump pgn_events_13_kiracast_m2
    jump loc_club_dancefloor_02

label pgn_events_13_kiracast_g1:
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_34
        ka emo-152 "Раздевайся."
    else:
        scene pgn_events_13_kiracast_max
        m emo-0 "Понаблюдаю один. Но с Катей было бы поинтереснее."
    scene pgn_events_13_kiracast_g1_04
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_05
    m emo-3 "{i}Секси, мне бы к ним.{/i}"
    scene pgn_events_13_kiracast_g1_06
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_07
    m emo-4 "{i}Пристроился бы сзади.{/i}"
    scene pgn_events_13_kiracast_g1_08
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_09
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_47
        ka emo-151 "..."
        m emo-3 "{i}Катя не сводит глаза с моего члена. Видно, что хочет его.{/i}"
    scene pgn_events_13_kiracast_g1_10
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_11
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_12
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_13
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_14
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_15
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_16
    m emo-9 "{i}Ого! Вот это струя!{/i}"
    scene pgn_events_13_kiracast_g1_17
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_18
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_19
    m emo-3 "{i}Эх... меня бы вместо этой игрушки.{/i}"
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_48
        ka emo-153 "[pname_max[0]], опиши, что там происходит."
        m emo-0 "Тётя взяла в рот большой дилдо. И сейчас засунет женщине в попу."
        scene pgp_club_firstvisit_49
        ka emo-151 "Ммм..."
        m emo-3 "{i}Кажись Катька завелась{/i}"
        menu:
            "Секс":
                m emo-0 "Может сексом займёмся?"
                ka emo-153 "Сейчас не могу, только ножками."
                m emo-2 "Жаль. А то я бы сейчас трахнул тебя."
                ka emo-152 "..."
            "Продолжить":
                pass
    scene pgn_events_13_kiracast_g1_20
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_21
    m emo-9 "{i}Без всякой разминки, сразу в попу!{/i}"
    scene pgn_events_13_kiracast_g1_22
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_23
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_24
    m emo-3 "{i}Классная дырочка, заполнил бы её спермой до краёв.{/i}"
    scene pgn_events_13_kiracast_g1_21
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_22
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_23
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_47
        m emo-10 "{i}Блин! Я так скоро уже кончу. Анал, ножки, анал...{/i}"
    scene pgn_events_13_kiracast_g1_22
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_23
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_25
    m emo-9 "{i}Снова мощный оргазм.{/i}"
    scene pgn_events_13_kiracast_g1_26
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_47
        ka emo-153 "Кончи мне в рот."
    scene pgn_events_13_kiracast_g1_27
    $ renpy.pause()
    scene pgn_events_13_kiracast_g1_28
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        jump pgn_events_13_kiracast_kateend

    $ qtime += 1
    jump loc_club_floor2_01


label pgn_events_13_kiracast_g2:
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_34
        ka emo-152 "Готовься."
    else:
        scene pgn_events_13_kiracast_max
        m emo-0 "Понаблюдаю один. Но с Катей было бы поинтереснее."
    scene pgn_events_13_kiracast_g2_04
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_05
    m emo-13 "{i}Вот же сучка!{/i}"
    scene pgn_events_13_kiracast_g2_06
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_07
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_08
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_09
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_47
        ka emo-151 "..."
        m emo-3 "{i}Катя не сводит глаза с моего члена. Видно, что хочет его так же, как той девчонке и тёте не хватает члена.{/i}"
    scene pgn_events_13_kiracast_g2_10
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_11
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_12
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_13
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_14
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_15
    m emo-2 "{i}Зачем? Нет бы поставить эту пацанку на место.{/i}"
    scene pgn_events_13_kiracast_g2_16
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_48
        ka emo-153 "[pname_max[0]], опиши, что там происходит."
        m emo-0 "На девушке надет страпон, а Тётя его берет в рот."
        scene pgp_club_firstvisit_49
        ka emo-151 "Ммм..."
        m emo-3 "{i}Кажись Катька завелась{/i}"
        menu:
            "Секс":
                m emo-0 "Может сексом займёмся?"
                ka emo-153 "Сейчас не могу, только ножками."
                m emo-2 "Жаль. А то я бы сейчас трахнул тебя."
                ka emo-152 "..."
            "Продолжить":
                pass
    scene pgn_events_13_kiracast_g2_17
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_18
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_19
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_47
        $ renpy.pause()
    scene pgn_events_13_kiracast_g2_20
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_21
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_22
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_23
    $ renpy.pause()
    scene pgn_events_13_kiracast_g2_24
    $ renpy.pause()
    m emo-6 "{i}Ясно, почему она постоянно без сил, когда приходит ночью домой.{/i}"
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        jump pgn_events_13_kiracast_kateend

    $ qtime += 1
    jump loc_club_floor2_01


label pgn_events_13_kiracast_m1:
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_34
        $ renpy.pause()
    else:
        scene pgn_events_13_kiracast_max
        m emo-0 "Понаблюдаю один. Но с Катей было бы поинтереснее."
    scene pgn_events_13_kiracast_m1_04
    $ renpy.pause()
    scene pgn_events_13_kiracast_m1_05
    m emo-3 "{i}Дразнит его{/i}"
    scene pgn_events_13_kiracast_m1_06
    $ renpy.pause()
    scene pgn_events_13_kiracast_m1_07
    if ("spykiraclub") in accessiv:
        m emo-3 "{i}Старается как может, но он не кончает.{/i}"
    else:
        $ renpy.pause()
    scene pgn_events_13_kiracast_m1_08
    if ("spykiraclub") in accessiv:
        $ renpy.pause()
    else:
        m emo-2 "{i}У меня ведь больше.{/i}"
    scene pgn_events_13_kiracast_m1_09
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_47
        ka emo-151 "..."
        m emo-3 "{i}Катя не сводит глаза с моего члена.{/i}"
    scene pgn_events_13_kiracast_m1_10
    if ("spykiraclub") in accessiv:
        m emo-16 "{i}Да, давай, глубже проталкивай ей в рот. Разрабатывай её ротик.{/i}"
    else:
        m emo-2 "{i}Вот гнида. Что он с ней делает.{/i}"
    scene pgn_events_13_kiracast_m1_11
    $ renpy.pause()
    scene pgn_events_13_kiracast_m1_12
    $ renpy.pause()
    scene pgn_events_13_kiracast_m1_13
    if ("spykiraclub") in accessiv:
        m emo-4 "{i}Сейчас оттрахает её в рот.{/i}"
    else:
        m emo-2 "{i}...{/i}"
    scene pgn_events_13_kiracast_m1_14
    $ renpy.pause()
    scene pgn_events_13_kiracast_m1_15
    $ renpy.pause()
    scene pgn_events_13_kiracast_m1_16
    if ("spykiraclub") in accessiv:
        m emo-16 "{i}Извивается, значит нравится.{/i}"
    else:
        m emo-2 "{i}Чёрт! Тётя...{/i}"
    scene pgn_events_13_kiracast_m1_17
    $ renpy.pause()
    scene pgn_events_13_kiracast_m1_18
    $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_48
        ka emo-153 "[pname_max[0]], опиши, что там происходит."
        m emo-0 "Мужик повалил тётю и трахает её грубо."
        scene pgp_club_firstvisit_49
        ka emo-151 "Ммм..."
        m emo-3 "{i}Катька завелась. Тоже хочет чтобы я её жестко?{/i}"
        menu:
            "Секс":
                m emo-0 "Может сексом займёмся? Хочешь ведь?"
                ka emo-153 "Хочу, но сейчас не могу, только ножками."
                ka emo-152 "..."
            "Продолжить":
                pass
    scene pgn_events_13_kiracast_m1_19
    $ renpy.pause()
    $ label_random = renpy.random.randint ( 1, 2)
    if label_random == 1:
        scene pgn_events_13_kiracast_m1_20
        $ renpy.pause()
        scene pgn_events_13_kiracast_m1_21
        $ renpy.pause()
        scene pgn_events_13_kiracast_m1_26
        $ renpy.pause()
    if label_random == 2:
        scene pgn_events_13_kiracast_m1_23
        $ renpy.pause()
        scene pgn_events_13_kiracast_m1_24
        $ renpy.pause()
        scene pgn_events_13_kiracast_m1_25
        $ renpy.pause()
        scene pgn_events_13_kiracast_m1_27
        $ renpy.pause()
        scene pgn_events_13_kiracast_m1_28
        $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        jump pgn_events_13_kiracast_kateend

    $ qtime += 1
    jump loc_club_floor2_01


label pgn_events_13_kiracast_m2:
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        scene pgp_club_firstvisit_34
        $ renpy.pause()
    else:
        scene pgn_events_13_kiracast_max
        m emo-0 "Понаблюдаю один. Но с Катей было бы поинтереснее."
    scene pgn_events_13_kiracast_m2_04
    $ renpy.pause()
    scene pgn_events_13_kiracast_m2_05
    $ renpy.pause()
    scene pgn_events_13_kiracast_m2_06
    $ renpy.pause()
    scene pgn_events_13_kiracast_m2_07
    $ renpy.pause()
    $ label_random = renpy.random.randint ( 1, 6)
    if label_random == 4:
        scene pgn_events_13_kiracast_m2_08
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_09
        m emo-13 "Как то быстро всё закончилось."
    if label_random == 6:
        scene pgn_events_13_kiracast_m2_10
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_11
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_12
        m emo-13 "Как то быстро всё закончилось."
    else:
        scene pgn_events_13_kiracast_m2_10
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_11
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_07
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_13
        $ renpy.pause()
        if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
            scene pgp_club_firstvisit_47
            ka emo-151 "..."
            m emo-3 "{i}Катя не сводит глаза с моего члена.{/i}"
        scene pgn_events_13_kiracast_m2_14
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_15
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_16
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_17
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_18
        $ renpy.pause()
        scene pgn_events_13_kiracast_m2_19
        $ renpy.pause()
    if (qtime == 0 and ("kiralubcasting_withkate_23") in ivent24) or (qtime == 2 and ("kiralubcasting_withkate_1") in ivent24):
        jump pgn_events_13_kiracast_kateend

    $ qtime += 1
    jump loc_club_floor2_01

label pgn_events_13_kiracast_kateend:
    scene pgp_club_firstvisit_50
    menu:
        "Кончить на неё":
            scene pgp_club_firstvisit_51
            m emo-12 "Аррггххх!!! Аааааа!!!"
            if kate_path < 3.7:
                scene pgp_club_firstvisit_52
                ka emo-157 "[pname_max[0]]! Что ты наделал?"
                m emo-3 "Я кончил."
                ka emo-156 "Потрачу много времени, чтобы всё смыть."
                m emo-4 "И так сойдёт."
                ka emo-157 "Извини."
            else:
                scene pgp_club_firstvisit_53
                ka emo-153 "Спасибо."
        "Кончить в рот":
            scene pgp_club_firstvisit_54
            m emo-10 "Кончаю!!!"
            scene pgp_club_firstvisit_55
            m emo-12 "Аррггххх!!! Аааааа!!!"
            scene pgp_club_firstvisit_56
            m emo-3 "Спасибо! Это было круто."
    $ PGN_Addstatsex(stat_kate, 0, 0, 0, 0, 1)
    $ qtime += 1
    jump loc_club_floor2_01







label loc_club_bar_alicekira:
    if ("alice_club_choco") not in ivent24:
        if qtime == 21:
            scene pgn_club_bar_chocono_alicekira_01_vadx
            $ renpy.pause()
            scene pgn_club_bar_chocono_alicekira_02_vadx
            $ renpy.pause()
        if qtime == 2:
            scene pgn_club_bar_chocono_alicekira_03_vadx
            m emo-3 "{i}Тётя уже перепила, распускает руки и лапает племянницу.{/i}"
            scene pgn_club_bar_chocono_alicekira_04_vadx
            $ renpy.pause()
            scene pgn_club_bar_chocono_alicekira_05_vadx
            m emo-6 "{i}Куда это она руку просунула?{/i}"
            scene pgn_club_bar_chocono_alicekira_06_vadx
            m emo-3 "{i}[pname_alice[0]] видно даже не против.{/i}"
            scene pgn_club_bar_chocono_alicekira_07_vadx
            $ renpy.pause()
            scene pgn_club_bar_chocono_alicekira_08_vadx
            $ renpy.pause()
    elif ("alice_club_choco") in ivent24:
        if qtime == 21:
            scene pgn_club_bar_chocoyes_alicekira_01
            $ renpy.pause()
            scene pgn_club_bar_chocoyes_alicekira_02
            m emo-6 "{i}Не слышно, кто и что там говорит. Но видно тёте очень стыдно за племянницу.{/i}"
        if qtime == 23:
            scene pgn_club_bar_chocoyes_alicekira_03
            m emo-3 "{i}Подойти бы к ней сзади и присунуть.{/i}"
            scene pgn_club_bar_chocoyes_alicekira_04
            $ renpy.pause()
        if qtime == 2:
            if scene_random == 1:
                scene pgn_club_bar_chocoyes_alicekira_10
                m emo-3 "{i}Вау! [pname_alice[0]] совсем в стельку пьяная.{/i}"
                scene pgn_club_bar_chocoyes_alicekira_11
                $ renpy.pause()
                scene pgn_club_bar_chocoyes_alicekira_12
                $ renpy.pause()
                scene pgn_club_bar_chocoyes_alicekira_13
                $ renpy.pause()
                scene pgn_club_bar_chocoyes_alicekira_14
                $ renpy.pause()
            if scene_random == 2:
                scene pgn_club_bar_chocoyes_alicekira_06
                m emo-13 "{i}[pname_alice[0]] видимо ошиблась местом, это бар, а не танцпол.{/i}"
                scene pgn_club_bar_chocoyes_alicekira_07
                m emo-3 "{i}Похоже всем на это пофиг, веселятся и подбадривают.{/i}"
                scene pgn_club_bar_chocoyes_alicekira_08
                m emo-9 "{i}И [pname_kira[0]] туда же?!{/i}"
                scene pgn_club_bar_chocoyes_alicekira_09
                $ renpy.pause()
    $ qtime += 1
    jump loc_club_bar






label loc_club_dancefloor_alicekira:
    if (("alice_club_choco") not in ivent24 and pgn_ach_repeat == 0) or pgn_ach_repeat == 159:
        if qtime == 22 and pgn_ach_repeat == 0:
            scene pgn_club_dance_chocono_alicekira_01
            $ renpy.pause()
            scene pgn_club_dance_chocono_alicekira_02
            $ renpy.pause()
        if (qtime == 0 and pgn_ach_repeat == 0) or pgn_ach_repeat == 159:
            scene pgn_club_strip_chocono_alicekira_01
            if ("kiraaliceclubnight") not in accessiv and pgn_ach_repeat == 0:
                m emo-6 "{i}Куда она уходит?{/i}"
            else:
                $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_02
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_03
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_04
            if ("kiraaliceclubnight") not in accessiv and pgn_ach_repeat == 0:
                m emo-1 "{i}Блин! Да это же мужской стриптиз.{/i}"
            else:
                $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_10_vadx
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_05
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_06
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_11_vadx
            m emo-0 "{i}[pname_kira[0]] за двоих напивается.{/i}"
            scene pgn_club_strip_chocono_alicekira_07
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_12_vadx
            m emo-6 "{i}Хм... [pname_alice[2]] нравится мужской стриптиз!? Может мне попробовать.{/i}"
            m emo-13 "{i}Да не, навряд ли, ещё и засмеёт меня.{/i}"
            scene pgn_club_strip_chocono_alicekira_08
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_13_vadx
            m emo-13 "{i}Блин! Он к ним идёт{/i}"
            scene pgn_club_strip_chocono_alicekira_14_vadx
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_15_vadx
            m emo-1 "{i}Ни чего, я накачаюсь и у меня будет такое же тело и больше сюда ходить не будете.{/i}"
            if ("kiraaliceclubnight") not in accessiv and pgn_ach_repeat == 0:
                m emo-6 "{i}Ничего не слышно. О чём они там болтают?{/i}"
                m emo-13 "{i}По их громкому смеху ясно, что снова про меня вспомнили.{/i}"
                scene pgn_club_strip_chocono_alicekira_16_vadx
                m emo-6 "{i}Зачем она снимает трусики? И как она это без стеснения делает в людном месте?{/i}"
                scene pgn_club_strip_chocono_alicekira_17_vadx
                m emo-1 "{i}Вот куда все трусы пропадают. Они достаются этому извращенцу.{/i}"
            else:
                m emo-13 "Опять Тётя [pname_kira[0]] уговаривает [pname_alice[3]] это сделать."
                scene pgn_club_strip_chocono_alicekira_16_vadx
                $ renpy.pause()
                scene pgn_club_strip_chocono_alicekira_17_vadx
                $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_18_vadx
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_19_vadx
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_20_vadx
            m emo-2 "{i}Наверное с этим неудобно и больно...{/i}"
            scene pgn_club_strip_chocono_alicekira_21_vadx
            other emo-999 "Аааа!"
            m emo-13 "{i}Не хотел бы я оказаться на его месте, с этой штуковиной.{/i}"
            if ("kiraaliceclubnight") not in accessiv and pgn_ach_repeat == 0:
                m emo-6 "{i}Они снова о чём-то шепчутся. Снова обо мне?{/i}"
            else:
                menu:
                    "Остаться":
                        pass
                    "уйти" if pgn_ach_repeat == 0:
                        jump loc_club_dancefloor_alicekira_end
            scene pgn_club_strip_chocono_alicekira_22_vezdessushij
            $ PGN_Achadd(pgnach_159, 159)
            m emo-0 "{i}А вот и он стриптиз, от [pname_kira[1]].{/i}"
            scene pgn_club_strip_chocono_alicekira_23_vezdessushij
            if ("kiraaliceclubnight") not in accessiv and pgn_ach_repeat == 0:
                m emo-9 "{i}Ох блин! Что происходит. [pname_kira[0]] разделась полностью и танцует перед ним стриптиз.{/i}"
                m emo-13 "{i}Хотя это тётя и по всей видимости такое здесь привычное, что никто не обращает внимание.{/i}"
            else:
                m emo-1 "{i}Блин! Они над ним издеваются. [pname_kira[0]] как-то раз предлагала меня с собой взять. Но я такого не хочу.{/i}"
            m emo-0 "{i}А [pname_alice[2]] нравится.{/i}"
            if ("kiraaliceclubnight") not in accessiv and pgn_ach_repeat == 0:
                m emo-6 "{i}Помнится она упоминала, что ей бывает стыдно. Интересно за что.{/i}"
            scene pgn_club_strip_chocono_alicekira_24_vezdessushij
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_25_vezdessushij
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_26_vezdessushij
            $ renpy.pause()
            scene pgn_club_strip_chocono_alicekira_27_vezdessushij
            m emo-2 "{i}Блин! Жесть. Это кажется очень больно.{/i}"
            scene pgn_club_strip_chocono_alicekira_28_vezdessushij
            if ("kiraaliceclubnight") not in accessiv and pgn_ach_repeat == 0:
                $ accessiv.append("kiraaliceclubnight")
                m emo-2 "{i}После такого мне не захочется с ними ходить в клуб.{/i}"
            else:
                $ renpy.pause()
            if pgn_ach_repeat != 0:
                jump table_pgn_achievement
        if qtime == 1:
            scene pgn_club_dance_chocono_alicekira_03
            $ renpy.pause()
            scene pgn_club_dance_chocono_alicekira_04
            $ renpy.pause()
    elif (("alice_club_choco") in ivent24 and pgn_ach_repeat == 0) or pgn_ach_repeat == 160:
        if qtime == 22 and pgn_ach_repeat == 0:
            scene pgn_club_dance_chocoyes_alicekira_01
            $ renpy.pause()
            scene pgn_club_dance_chocoyes_alicekira_02
            $ renpy.pause()
            scene pgn_club_dance_chocoyes_alicekira_03
            $ renpy.pause()
        if (qtime == 0 and pgn_ach_repeat == 0) or pgn_ach_repeat == 160:
            scene pgn_club_strip_chocono_alicekira_10_vadx
            $ renpy.pause()
            scene pgn_club_striptease_girl2_03
            $ renpy.pause()
            scene pgn_club_striptease_girl2_05
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_02
            $ renpy.pause()
            scene pgn_club_striptease_girl2_08
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_01
            k emo-111 "[pname_alice[0]], может достаточно с тебя?"
            a emo-24 "Нет. Хочу ещё, оно такое вкусное."
            scene pgn_club_striptease_girl2_12
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_02
            m emo-13 "{i}Ох! И много же она пьёт.{/i}"
            if ("kiraaliceclubnight_choco") not in accessiv and pgn_ach_repeat == 0:
                m emo-13 "{i}Может мне не стоило давать ей конфеты.{/i}"
            scene pgn_club_striptease_girl2_13
            $ renpy.pause()
            scene pgn_club_striptease_girl2_15
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_03
            a emo-29 "Мне скучно. Эй! Слезай, моя очередь!"
            if ("kiraaliceclubnight_choco") not in accessiv and pgn_ach_repeat == 0:
                $ accessiv.append("kiraaliceclubnight_choco")
                m emo-6 "{i}Очередь?!{/i}"
            scene pgn_club_strip_chocono_alicekira_01
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_04
            a emo-24 "Еле-еле, но забралась."
            k emo-103 "[pname_alice[0]]! Тебе помочь?"
            a emo-28 "Не, не, не я сама."
            scene pgn_club_strip_chocoyes_alicekira_05
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_06
            a emo-26 "Ой!"
            k emo-100 "Ты в порядке?"
            a emo-31 "Да. Я ещё не всё."
            scene pgn_club_strip_chocoyes_alicekira_07
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_08
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_09
            $ renpy.pause()
            scene pgn_club_strip_chocoyes_alicekira_10
            $ PGN_Achadd(pgnach_160, 160)
            a emo-22 "Ой! Опять упала. Моя попка."
            $ label_random = renpy.random.randint ( 1, 2)
            if label_random == 1:
                scene pgn_club_strip_chocoyes_alicekira_11
                $ renpy.pause()
                scene pgn_club_strip_chocoyes_alicekira_12
                $ renpy.pause()
                scene pgn_club_strip_chocoyes_alicekira_13
                $ renpy.pause()
                scene pgn_club_strip_chocoyes_alicekira_14
                $ renpy.pause()
            if label_random == 2:
                scene pgn_club_strip_chocoyes_alicekira_15
                $ renpy.pause()
                scene pgn_club_strip_chocoyes_alicekira_16
                $ renpy.pause()
                scene pgn_club_strip_chocoyes_alicekira_17
                $ renpy.pause()
                scene pgn_club_strip_chocoyes_alicekira_18
                $ renpy.pause()
                scene pgn_club_strip_chocoyes_alicekira_19
                $ renpy.pause()
            if pgn_ach_repeat != 0:
                jump table_pgn_achievement
        if qtime == 1:
            scene pgn_club_dance_chocoyes_alicekira_04
            $ renpy.pause()
            scene pgn_club_dance_chocoyes_alicekira_05
            $ renpy.pause()
            scene pgn_club_dance_chocoyes_alicekira_06
            $ renpy.pause()
label loc_club_dancefloor_alicekira_end:
    $ qtime += 1
    if "loc_club_dancefloor_01" in location:
        jump loc_club_dancefloor_01
    if "loc_club_dancefloor_02" in location:
        jump loc_club_dancefloor_02
    if "loc_club_dancefloor_03" in location:
        jump loc_club_dancefloor_03







label pgn_club_restw_alicedrink:
    if ("aliceclub_restinvit") not in ivent24 and pgn_ach_repeat == 0:
        scene pgn_club_restroom_w_charin
        show pgn_club_restroom_w_chocoyes_alice_01
        menu:
            "Подойти сзади":
                scene pgn_club_restroom_w_chocoyes_alice_06
                a emo-24 "Ой! Моя попка попалась!"
                scene pgn_club_restroom_w_chocoyes_alice_07
                a emo-33 "Меня хотят изнасиловать. Ик! Хе-хе-хе. Я не против. Оттрахай меня... меня."
                m emo-3 "{i}Вот же шлюшка. Её не интересует, кто это. Тогда я накажу тебя.{/i}"
            "Подождать":
                scene pgn_club_restroom_w_charin
                $ label_random = renpy.random.randint ( 1, 3)
                if label_random == 2:
                    show pgn_club_restroom_w_chocoyes_alice_02
                    a emo-31 "Эй! Не хорошо подглядывать. Ик! Подойди ко мне. Ик!"
                    menu:
                        "Подойти":
                            jump pgn_club_restw_alicedrink_next
                        "уйти":
                            scene pgn_club_restroom_w_chocoyes_alice_05
                            a emo-31 "Эй! Куда же ты?"
                            jump loc_club_dancefloor_03
                else:
                    show pgn_club_restroom_w_chocoyes_alice_03
                    a emo-30 "Ой! Опять. Писать хочу."
                    scene pgn_club_restroom_w_chocoyes_alice_04
                    $ renpy.pause()
                    scene pgn_club_restroom_w_charin
                    call screen loc_club_restr_women
    else:
        scene pgn_club_restroom_w_chocoyes_alice_09
        a emo-25 "Трахнешь меня?"
        m emo-3 "Конечно. Иначе бы не согласился."
        scene pgn_club_restroom_w_chocoyes_alice_10
        $ PGN_Achadd(pgnach_161, 161)
        a emo-22 "Тогда сними с меня трусики, сама не смогу."
        menu:
            "Снять трусики":
                pass
            "И так пойдёт":
                m emo-0 "Они мне не мешают. Сдвинуть и делов."
                a emo-24 "[pname_max[0]]! Я возбуждена и хочу твой член, но в мокрых трусиках ходить не хочу. Сними их с меня."
        scene pgn_club_restroom_w_chocoyes_alice_11
        m emo-4 "{i}Её трусики уже мокрые. А из её киски чувствуется жар.{/i}"
        m emo-3 "{i}Вот же [pname_alice[0]], специально меня попросила это сделать.{/i}"
        scene pgn_club_restroom_w_chocoyes_alice_12
        $ renpy.pause()
label pgn_club_restw_alicedrink_next:
    scene pgn_club_restroom_w_chocoyes_alice_08
    menu:
        "Отшлепать" if pgn_ach_repeat == 0:
            $ scene_random, label_random = 0, renpy.random.randint ( 1, 3)
            label pgn_club_restw_alicedrink_punish:
                $ scene_random += 1
                scene pgn_club_restroom_w_chocoyes_alice_13
                $ renpy.pause()
                scene pgn_club_restroom_w_chocoyes_alice_14
                if ("aliceclub_restinvit") not in ivent24:
                    a emo-30 "Ааахх!"
                else:
                    a emo-30 "Ааахх! [pname_max[0]]!"
                scene pgn_club_restroom_w_chocoyes_alice_13
                $ renpy.pause()
                scene pgn_club_restroom_w_chocoyes_alice_15
                if ("aliceclub_restinvit") not in ivent24:
                    a emo-26 "Аххх! Моя попочка! Ааах!"
                else:
                    a emo-32 "[pname_max[0]]! Ай! Хватит!"
                if scene_random == 1:
                    scene pgn_club_restroom_w_chocoyes_alice_13
                if scene_random == 2:
                    scene pgn_club_restroom_w_chocoyes_alice_16
                if ("aliceclub_restinvit") in ivent24 and scene_random == 2:
                    scene pgn_club_restroom_w_chocoyes_alice_17
                    a emo-32 "Всё, с меня достаточно. Я хотела от тебя секса, а получила красную попку."
                    m emo-2 "Прости. Ну переборщил я. Хотел завести тебя."
                    a emo-23 "Я тебе не [pname_liza[0]], чтобы от твоих шлепков возбуждаться. Всё я ухожу."
                    $ accessiv.append("alicehardpunishmax")
                    $ qtime += 1
                    if ("date_club_kate") in ivent24:
                        jump pgn_events_13_club_datekate_01_next
                    jump loc_club_restr_women
                if scene_random < 3:
                    menu:
                        "Шлепнуть ещё раз":
                            jump pgn_club_restw_alicedrink_punish
                        "Заняться сексом":
                            jump pgn_club_restw_alicedrink_vaginal
            if scene_random == 3 and label_random == 3:
                scene pgn_club_restroom_w_chocoyes_alice_18
                m emo-13 "Эм... [pname_alice[0]]..."
                scene pgn_club_restroom_w_chocoyes_alice_19
                m emo-9 "{i}Ох! Блин!{/i}"
                scene pgn_club_restroom_w_chocoyes_alice_20
                m emo-13 "{i}Эм... мне кажется пора уходить.{/i}"
                $ qtime += 1
                jump loc_club_restr_women
            jump pgn_club_restw_alicedrink_vaginal
        "Вагинал":
            label pgn_club_restw_alicedrink_vaginal:
                scene pgn_club_restroom_w_chocoyes_alice_21
                m emo-0 "{i}Блин! [pname_alice[0]] такая высокая, что я не достаю до её киски.{/i}"
                if (("aliceclub_restinvit") in ivent24 and pgn_ach_repeat == 0) or pgn_ach_repeat != 0:
                    m emo-1 "[pname_alice[0]], опустись ниже, я не достаю."
                    a emo-22 "Мама верно говорила, что ещё не дорос до этого."
                    m emo-2 "[pname_alice[0]]!"
                else:
                    a emo-26 "Я готова... Ик! Трахни меня, страстный незнакомец!"
                scene pgn_club_restroom_w_chocoyes_alice_22
                m emo-3 "Вот так лучше!"
                scene pgn_club_restroom_w_chocoyes_alice_23
                $ renpy.pause()
                scene pgn_club_restroom_w_chocoyes_alice_24
                $ renpy.pause()
                scene pgn_club_restroom_w_chocoyes_alice_25
                if (("aliceclub_restinvit") not in ivent24 and pgn_ach_repeat == 0) or pgn_ach_repeat != 0:
                    a emo-22 "Этот член мне кого-то напоминает... Ик! У моего парня такой же... Ик!"
                    m emo-6 "{i}Значит я для неё парень?! Может получится и её сделать своей девушкой.{/i}"
                else:
                    $ renpy.pause()
                scene pgn_club_restroom_w_chocoyes_alice_26
                $ renpy.pause()
                scene pgn_club_restroom_w_chocoyes_alice_27
                $ renpy.pause()
                if (("aliceclub_restinvit") not in ivent24 and pgn_ach_repeat == 0) or pgn_ach_repeat != 0:
                    scene pgn_club_restroom_w_chocoyes_alice_28
                    m emo-7 "{i}Чёрт! Я уже почти.{/i}"
                    scene pgn_club_restroom_w_chocoyes_alice_29
                    $ renpy.pause()
                    scene pgn_club_restroom_w_chocoyes_alice_30
                    m emo-10 "Аррггххх!!!"
                    scene pgn_club_restroom_w_chocoyes_alice_31_dj0101
                    a emo-24 "Хочешь посмотреть, как из меня выходит сперма?"
                    menu:
                        "Да":
                            scene pgn_club_restroom_w_chocoyes_alice_32_dj0101
                            m emo-13 "{i}[pname_alice[0]] реально безбашенная.{/i}"
                            scene pgn_club_restroom_w_chocoyes_alice_33
                            a emo-26 "Ммм! А вот и сливки."
                            scene pgn_club_restroom_w_chocoyes_alice_34_dj0101
                            a emo-33 "Как много! Хм... может мне их?!"
                            m emo-13 "{i}Пора уходить, не уверен, что я готов сейчас увидеть что-то ещё более безумное.{/i}"
                        "Я пойду":
                            m emo-13 "Спасибо, я пойду в общем."
                else:
                    m emo-7 "Я почти уже..."
                    scene pgn_club_restroom_w_chocoyes_alice_35_dj0101
                    m emo-10 "Ох блин! Я... я..."
                    scene pgn_club_restroom_w_chocoyes_alice_36_dj0101
                    m emo-10 "Аррггххх!!!"
                    scene pgn_club_restroom_w_chocoyes_alice_37_dj0101
                    m emo-3 "Как тебе мои сливочки?"
                    scene pgn_club_restroom_w_chocoyes_alice_38_dj0101
                    a emo-22 "..."
                if pgn_ach_repeat != 0:
                    jump table_pgn_achievement
                $ PGN_Addstatsex(stat_alice, 0, 0, 0, 1, 0)
    $ qtime += 1
    if ("date_club_kate") in ivent24:
        jump pgn_events_13_club_datekate_01_next
    jump loc_club_restr_women










label loc_club_locchr:
    if ("wrongclub_approved") not in ivent24:

        if "loc_club_bar" in location and "loc_club_bar" in locchr_loc2:
            if locchr_kira.loc2 == "loc_club_bar":
                $ scene_random = "kira_wrongmax"
        if ("loc_club_dancefloor_01" in location or "loc_club_dancefloor_02" in location or "loc_club_dancefloor_03" in location) and "loc_club_dancefloor" in locchr_loc2:
            if locchr_kira.loc2 == "loc_club_dancefloor" and locchr_alice.loc2 == "loc_club_dancefloor":
                $ label_random = renpy.random.randint ( 1, 4)
                if label_random == 3:
                    $ scene_random = "kira_wrongmax"
                else:
                    $ scene_random = "alice_wrongmax"
            elif locchr_kira.loc2 == "loc_club_dancefloor":
                $ scene_random = "kira_wrongmax"
        if "loc_club_restr_women" in location and "loc_club_restr_women" in locchr_loc2:
            $ scene_random = "alice_wrongmax"
    else:
        $ scene_random = 0

    if "loc_club_bar" in location:
        scene blur_pgn_club_bar
    if "loc_club_dancefloor_01" in location:
        scene blur_pgn_club_dancefloor_01
    if "loc_club_dancefloor_02" in location:
        scene blur_pgn_club_dancefloor_02
    if "loc_club_dancefloor_03" in location:
        scene blur_pgn_club_dancefloor_03
    if "loc_club_restr_women" in location:
        scene blur_pgn_club_restroom_women

    if scene_random == "alice_wrongmax" and ("wrongclub_approved_alice") not in ivent24 and ((qtime >= 21 and qtime <= 23 and daysn == 5) or (qtime >= 0 and qtime <= 3 and daysn == 6)):
        if ("date_club_kate") in ivent24 and locchr_kate.loc1 == "loc_club":
            if ("alice_club_choco") not in ivent24:
                show maxnoticed_alice_04
                a emo-27 "[pname_max[0]]! Какого черта ты здесь?"
                hide maxnoticed_alice_04
                show maxnoticed_alice_kate
                a emo-31 "Привет. Вы вместе. Понятно."
                ka emo-152 "Привет. Я за [pname_max[0]] присмотрю, так что..."
                a emo-22 "Я пойду. Хорошо вам повеселиться."
                ka emo-152 "И тебе тоже."
                $ ivent24.append("wrongclub_approved")
            else:
                show maxnoticed_alice_01
                a emo-22 "Ммм... Мальчик. Не хочешь со мной повеселиться?"
                menu:
                    "Я не один":
                        m emo-0 "Я не один, с девушкой."
                        hide maxnoticed_alice_01
                        show maxnoticed_alice_03
                        a emo-20 "А ну тогда..."
                        hide maxnoticed_alice_01
                        m emo-6 "Хм... ушла."
                    "Да":
                        jump pgn_club_restw_alicedrink_next
        else:
            if ("alice_club_choco") not in ivent24:
                if ("коуб_фдшса_спалила") not in accessiv:
                    $ accessiv.append("коуб_фдшса_спалила")
                show maxnoticed_alice_04
                a emo-32 "[pname_max[0]]! А ты здесь какого черта делаешь?"
                menu:
                    "Просто посмотреть":
                        m emo-0 "Я просто пришёл посмотреть."
                        a emo-20 "Надеюсь. "
                    "Вы меня не берёте":
                        m emo-0 "Вы меня с собой не берёте, а мне очень хочется хоть раз вместе с вами."
                        a emo-20 "[pname_max[0]]! Ты ещё маленький."
                        m emo-11 "Ничего подобного."
                a emo-29 "И что мне с тобой делать. Если Мама узнает, то не только тебе прилетит, я тоже буду наказана."
                menu:
                    "Пожалуйста":
                        m emo-2 "Ну пожалуйста."
                        $ label_random = renpy.random.randint ( 1, 3)
                        if label_random == 2:
                            a emo-20 "Ладно, притворюсь, как будто я тебя не видела. Не попадайся на глаза тёте."
                            m emo-3 "Хорошо. Спасибо"
                            $ ivent24.append("wrongclub_approved_alice")
                        else:
                            a emo-20 "Нет. Прослежу, как ты доедешь до дома и никуда сегодня не высовывайся. Не порть мне ночь."
                            m emo-2 "Блин!"
                            $ accessiv.append("mapmax_off")
                            jump loc_pool_move
                    "Угостить выпивкой?":
                        m emo-4 "Может я тебя угощу тебя выпивкой?"
                        a emo-28 "Ты знаешь, как действует на меня алкоголь."
                        a emo-20 "Езжай домой."
                        m emo-1 "Но [pname_alice[0]]... {i}Блин!{/i}"
                        $ accessiv.append("mapmax_off")
                        jump loc_pool_move
                    "Смириться":
                        a emo-20 "Езжай домой и не высовывайся."
                        $ accessiv.append("mapmax_off")
                        jump loc_pool_move
            else:
                $ label_random = renpy.random.randint ( 1, 2)
                if label_random == 1:
                    show maxnoticed_alice_01
                    a emo-22 "Ой! А я кажется тебя где-то видела. Ик!"
                    m emo-13 "{i}Повезло, она пьяная и не узнает меня.{/i}"
                    a emo-24 "Аааааа! Ты в порно снимаешься, да? Может трахнешь меня сегодня? Ик!"
                    m emo-4 "Да, конечно."
                    a emo-28 "..."
                    m emo-13 "..."
                    a emo-28 "..."
                    a emo-20 "Ик! Я пойду. Вроде что-то хотела, но забыла. Ик!"
                else:
                    show maxnoticed_alice_02
                    a emo-22 "Привет красавчик! Я хочу спермы, много спермы. Поможешь?"
                    a emo-26 "Тебе видно скучно. Ик! А мне нужен твой член. Ик!"
                    menu:
                        "Согласиться":
                            m emo-4 "Пойдём."
                            jump pgn_club_restw_alicedrink_next
                        "Отказаться":
                            m emo-0 "Может быть, но не сейчас."
                            a emo-28 "Как хочешь. Ик! Я... Ик!"
    if scene_random == "kira_wrongmax":
        if ("date_club_kate") in ivent24 and locchr_kate.loc1 == "loc_club":
            show maxnoticed_kira_01
            k emo-104 "[pname_max[0]]! Ты почему здесь?"
            m emo-9 "А эм... Я... тут..."
            hide maxnoticed_kira_01
            show maxnoticed_kira_kate
            ka emo-152 "Здравствуйте. Это я привела [pname_max[3]], не волнуйтесь, я прослежу за ним."
            k emo-105 "А, тогда... [pname_max[0]]! Не доставляй ей проблем. Уяснил?"
            m emo-13 "Да..."
            k emo-101 "Тогда я вас оставлю, веселитесь."
            ka emo-159 "Спасибо."
            $ ivent24.append("wrongclub_approved")
        else:
            if ("wrongclub_kira") not in accessiv:
                $ accessiv.append("wrongclub_kira")
                show maxnoticed_kira_01
                k emo-105 "Так, так. [pname_max[0]]! Ты как тут оказался? Тебе ещё рано здесь быть."
                menu:
                    "Я просто посмотреть":
                        m emo-13 "Мне просто интересно было посмотреть, что здесь."
                        k emo-111 "Это место не для детей."
                        m emo-1 "Но я взрослый, я не ребенок!"
                    "Вы меня не берете":
                        m emo-2 "Вы меня с собой не берёте в клуб. А мне очень хотелось провести время с вами."
                        k emo-111 "[pname_max[0]]! Ты ещё не достиг того возраста, чтобы с нами ходить по таким местам и тебе нельзя алкоголь."
                        k emo-104 "А если Мама твоя узнает?"
                        m emo-0 "Не узнает."
                if locchr_alice.loc1 == "loc_club":
                    k emo-112 "Хватит. Сейчас найду твою сестру и отвезу вас обоих домой. И сиди дома, а не то я расскажу всё твоей маме."
                else:
                    k emo-112 "Хватит. Сейчас отвезу тебя домой. И сиди дома, а не то я расскажу всё твоей маме."
                k emo-105 "И больше сюда не ногой. Ты меня понял?"
            else:
                show maxnoticed_kira_01
                k emo-104 "[pname_max[0]], ты опять здесь!"
                m emo-13 "Ну... Эмм..."
                if ("alice_club_choco") in ivent24:
                    hide maxnoticed_kira_01
                    show maxnoticed_kira_02
                    a emo-26 "Ой! Мальчики, держите меня семеро! А лучше, приглашаю всех посетить мои сладкие дырочки."
                    k emo-103 "Опять она напилась. Жди меня здесь и отвезу вас домой."
                elif locchr_alice.loc1 == "loc_club":
                    k emo-100 "Сейчас отвезу вас обоих домой."
                else:
                    k emo-100 "Сейчас отвезу тебя домой."
                    m emo-1 "Я и сам могу."
                    k emo-100 "Нет. За тобой нужен глаз да глаз. И будешь сидеть дома до утра."
            if locchr_alice.loc1 == "loc_club":
                $ ivent24.append("wrongclub_kira_and_alice")
            $ accessiv.append("mapmax_off")
            scene animated pgn_transp_city_taxi_night
            $ renpy.pause(5, hard=True)
            if transport1.use != True and transport2.use != True:
                $ currency -= 50
                $ screennotify("$",18,50)
            jump loc_pool
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
