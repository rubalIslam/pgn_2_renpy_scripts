






label pgn_events_13_newtubs_01:
    if pgn_ach_repeat == 0:
        m emo-8 "{i}Блин! Что-то мне стало плохо. Пойду прилягу.{/i}"
        scene pgn_club_eva_badtubs_01
        m emo-8 "{i}От чего мне так хреново!? Голова и...{/i}"
        scene pgn_club_eva_badtubs_02
        m emo-13 "{i}Ох, блин! Мои яйца! Сейчас лопнут{/i}"
        scene pgn_club_eva_badtubs_03
        m emo-8 "{i}Даже встать не могу... Ничего не вижу...{/i}"
        if eva_path >= 4.1:
            jump pgn_events_13_newtubs_01_repeat
        scene pgn_club_eva_badtubs_03
        show pgn_club_eva_badtubs_04
        m emo-13 "{i}О! Кто-то подошёл. Может быть мне помогут...{/i}"
        scene animated pgn_club_eva_badtubs_05
        other emo-998 "[pname_max[0]]! Что с тобой?"
        m emo-8 "Кто это?\n{i}Откуда она меня знает? Не вижу её лица.{/i}"
        scene animated pgn_club_eva_badtubs_06
        m emo-13 "{i}Заметила мою эрекцию. Как не заметить, от такого напора штаны порвутся.{/i}"
        scene pgn_club_eva_badtubs_07
        m emo-2 "Куда мы?"
        other emo-998 "Пойдём. Я тебе помогу."
    scene pgn_club_eva_badtubs_08
    m emo-13 "{i}Кажется я в приватной комнате. Зачем? Я думал мы направлялись к выходу.{/i}"
    m emo-14 "Эм... А..."
    scene pgn_club_eva_badtubs_09
    $ renpy.pause()
    scene pgn_club_eva_badtubs_10
    m emo-8 "Ай! Больно!"
    scene pgn_club_eva_badtubs_11
    m emo-10 "Ох! Так лучше."
    scene pgn_club_eva_badtubs_12
    m emo-10 "{i}Глубоко берет в рот.{/i}"
    scene pgn_club_eva_badtubs_13
    $ renpy.pause()
    scene pgn_club_eva_badtubs_14
    $ renpy.pause()
    scene pgn_club_eva_badtubs_15
    m emo-12 "Аргх! Аааахх! Чёрт! Ааааа!!!!"
    m emo-0 "{i}Охренеть! Вот это залп!{/i}"
    scene pgn_club_eva_badtubs_13
    m emo-10 "{i}Блин! Мне всё равно хреново. Кажется этого недостаточно. И я... засыпаю..{/i}"
    if pgn_ach_repeat == 0:
        scene animated pgn_club_eva_badtubs_16
    else:
        scene pgn_club_eva_badtubs_16_01
    other emo-998 "[pname_max[0]]! [pname_max[0]]! Не теряй создание. Я не смогу тебе помочь, если ты потеряешь сознание."
    scene pgn_club_eva_badtubs_17
    m emo-8 "{i}Блин! Ещё хуже стало.{/i}"
    scene pgn_club_eva_badtubs_18
    $ PGN_Achadd(pgnach_174, 174)
    m emo-13 "{i}Кто эта девушка или женщина?{/i}"
    if (qtime >= 21 and qtime <= 23 and (daysn == 1 or daysn == 3 or daysn == 6 or daysn == 5)) or (qtime >= 0 and qtime <= 3 and (daysn == 2 or daysn == 4 or daysn == 7 or daysn == 6)):
        m emo-13 "{i}Может быть Катя?{/i}"
        m emo-0 "{i}Нет. Сегодня же она не работает.{/i}"
        m emo-6 "{i}Тогда может быть [pname_alice[0]] и она скрывает, что тоже подрабатывает?{/i}"
    else:
        m emo-6 "{i}По фигуре напоминает мне [pname_alice[3]]. Но и Катя может быть, она сегодня работает.{/i}"
    scene animated pgn_club_eva_badtubs_19
    $ renpy.pause()
    scene pgn_club_eva_badtubs_20
    m emo-12 "Аргх!!! Аааа!!!"
    if pgn_ach_repeat == 0:
        scene animated pgn_club_eva_badtubs_21
    else:
        scene pgn_club_eva_badtubs_21_01
    other emo-998 "[pname_max[0]]! Потерпи ещё немного."
    m emo-2 "{i}Ещё? Чёрт! Да меня насилуют.{/i}"
    scene animated pgn_club_eva_badtubs_23a
    $ renpy.pause()
    if pgn_ach_repeat == 0:
        scene animated pgn_club_eva_badtubs_23b
        $ renpy.pause()
        scene animated pgn_club_eva_badtubs_23c
        $ renpy.pause()
    if pgn_ach_repeat != 0:
        jump table_pgn_achievement
label pgn_events_13_newtubs_01_repeat:
    scene black with dissolve
    $ renpy.pause(4, hard=True)
    scene pgn_clinic_maxafterclub_01_vadx with dissolve
    m emo-9 "{i}Я в клинике? Как тут оказался?{/i}"
    eva emo-128 "[pname_max[0]]! Привет. Ты проснулся?"
    scene pgn_clinic_maxafterclub_02
    eva emo-133 "Как себя чувствуешь?"
    menu:
        "Нормально":
            m emo-13 "Эм... Нормально."
            eva emo-130 "Ну и хорошо."
        "Как я здесь оказался?" if eva_path < 4.2:
            m emo-6 "А как я сюда попал, что произошло?"
            eva emo-131 "А ты не помнишь? Тебя привезла девушка. Сказала, что случайно тебя обнаружила и сразу привезла к нам."
            if eva_path == 4:
                $ eva_path = 4.1
                m emo-0 "Ясно."
                m emo-13 "{i}Я помню, что на моём члене какая-то девушка активно скакала до потери сознания.{/i}"
                m emo-8 "{i}Только из-за чего мне так хреново было, не понятно.{/i}"
                m emo-6 "{i}Надо будет ещё расспросить девчонок, кто из них это был.{/i}"
            elif eva_path >= 4.1 and ("club_secretwaitress_alice_true" not in accessiv or "club_secretwaitress_kate_true" not in accessiv):
                if "club_secretwaitress_kate_false" in accessiv and "club_secretwaitress_kate_true" not in accessiv:
                    $ accessiv.remove("club_secretwaitress_kate_false")
                    $ accessiv.append("club_secretwaitress_kate_true")
                    m emo-6 "Это была Катя?"
                    eva emo-131 "Катя? Не знаю, девушка себя не назвала."
                if "club_secretwaitress_alice_false" in accessiv and "club_secretwaitress_alice_true" not in accessiv:
                    $ accessiv.remove("club_secretwaitress_alice_false")
                    $ accessiv.append("club_secretwaitress_alice_true")
                    m emo-6 "Это была [pname_alice[0]]?"
                    eva emo-128 "Нет, не [pname_alice[0]]. [pname_alice[3]] я знаю в лицо."
            if eva_path == 4.1 and "club_secretwaitress_alice_true" in accessiv and "club_secretwaitress_kate_true" in accessiv:
                $ eva_path = 4.2
                m emo-6 "{i}Кто же эта загадочная спасительница? Попробую в клубе её найти.{/i}"
    eva emo-128 "Твоей маме ничего не сообщала. Не будем её тревожить, хорошо?"
    m emo-13 "{i}Маме лучше не знать, где я был, а то точно буду сидеть только дома.{/i}"
    eva emo-133 "Полежи ещё немного, после можешь ехать домой."
    m emo-3 "Ага, спасибо."
    if qtime >= 6 and qtime <= 23:
        $ daysn, days = daysn+1, days+1
    call max_sleep_reset from _call_max_sleep_reset_9
    $ qtime = 12
    jump loc_clinic_registration



label pgn_events_13_newtubs_dial_kate:
    m emo-3 "Спасибо. За тот случай в клубе."
    ka emo-151 "За какой?"
    m emo-13 "Ну тот, когда мне было плохо."
    if ("club_gh_firstkatehelp") in accessiv:
        ka emo-151 "Когда ты не мог кончить? Пожалуйста."
    else:
        ka emo-154 "Тебе было плохо? [pname_max[0]], не пей спиртное. У тебя организм слабый."
        m emo-13 "Да нет, я о..."
        ka emo-151 "Не понимаю о чём ты?"
    m emo-0 "Эм... ладно. Просто спасибо."
    m emo-0 "{i}Значит не она.{/i}"
    $ accessiv.append("club_secretwaitress_kate_false")
    jump jump_dialogue

label pgn_events_13_newtubs_sms_kate:
    hide screen sms_kate_menu
    "{#r=Спасибо. За тот случай в клубе.}"
    "{#l=За какой?}"
    "{#r=Ну тот, когда мне было плохо.}"
    if ("club_gh_firstkatehelp") in accessiv:
        "{#l=Когда ты не мог кончить? Пожалуйста.}"
    else:
        "{#l=Тебе было плохо? [pname_max[0]], не пей спиртное. У тебя организм слабый.}"
        "{#r=Да нет, я о...}"
        "{#l=Не понимаю о чём ты?}"
    "{#r=Эм... ладно. Просто спасибо.}"
    $ accessiv.append("club_secretwaitress_kate_false")
    jump phone_max

label pgn_events_13_newtubs_dial_alice:
    m emo-3 "Спасибо. За тот случай в клубе."
    a emo-20 "Ну пожалуйста."
    menu:
        "Значит ты?":
            m emo-4 "Значит это ты была. А что скрываешь, что там тоже работаешь?"
            a emo-24 "Не понимаю о чём ты. Головой где-то ударился?"
            m emo-13 "{i}Нет, всё же это не она.{/i}"
        "Не она":
            m emo-13 "{i}Нет, это не она, это уж точно.{/i}"
    $ accessiv.append("club_secretwaitress_alice_false")
    jump jump_dialogue



label pgn_clinic_max_afterclub:
    scene pgn_clinic_maxafterclub_01_vadx with dissolve
    if "club_gh_sex_girl1_vaginal" in ivent24:
        m emo-13 "Блин! Что произошло. Как я тут оказался?"
    elif "club_gh_katehelp" in ivent24:
        m emo-13 "Блин! Катя! Я из-за неё оказался здесь."
    elif eva_path >= 4.4:
        m emo-13 "{i}Снова из-за этих таблеток.{/i}"
    $ renpy.pause(3)
    eva emo-130 "[pname_max[0]], ты проснулся?"
    scene pgn_clinic_maxafterclub_02
    if "club_gh_sex_girl1_vaginal" in ivent24:
        m emo-0 "Привет. А как я тут?"
        eva emo-131 "Тебя вчера привезли работники клуба \"Электра\". Сообщили, что нашли тебя без сознания."
        eva emo-130 "Не могу сказать, как это случилось. Но у тебя наблюдается лёгкое сотрясение мозга."
        m emo-13 "Мама в курсе?"
        eva emo-128 "Твоей маме ничего не говорила. Ещё немного полежишь в клинике и отпущу тебя домой."
        m emo-1 "Спасибо."
    elif "club_gh_katehelp" in ivent24:
        eva emo-130 "Мне твоя девушка сообщила, что ты не смог кончить и довёл себя до такого."
        m emo-13 "Да..."
        if eva_path < 100:
            eva emo-131 "[pname_max[0]] ты снова принял таблетку? Перестань принимать их, я не знаю, к чему может это привести."
            m emo-2 "Хорошо."
    elif eva_path >= 4.4:
        eva emo-133 "[pname_max[0]]..."
        m emo-13 "Забыл, что нельзя их вместе принимать. Точнее забыл, когда в последний раз принимал те старые таблетки."
        eva emo-130 "..."
    eva emo-130 "Будь в следующий раз поосторожнее."
    m emo-13 "Хорошо, постараюсь."
    if qtime >= 6 and qtime <= 23:
        $ daysn, days = daysn+1, days+1
    call max_sleep_reset from _call_max_sleep_reset_10
    $ qtime = 10
    jump loc_clinic_registration


label pgn_events_13_newtubs_workwaiter:
    if ("club_eva_waiter_walk") in ivent24:
        if "loc_club_dancefloor_03" in location:
            if renpy.random.randint (1,2) == 1:
                jump pgn_events_13_newtubs_workwaiter_clL
            else:
                jump pgn_events_13_newtubs_workwaiter_clR
        else:
            m emo-1 "{i}Она направляется к бару{/i}"
            scene pgn_club_eva_badtubs_30
            $ renpy.pause()
            menu:
                "Спасибо":
                    jump pgn_events_13_newtubs_workwaiter_thanks
                "Спрятаться в мужском туалете" if eva_path == 4.3:
                    jump pgn_events_13_newtubs_spy_menrest
                "Спрятаться в женском туалете" if eva_path == 4.3:
                    jump pgn_events_13_newtubs_spy_womenrest
                "Продолжить наблюдение":
                    if renpy.random.randint (1,2) == 1:
                        jump pgn_events_13_newtubs_workwaiter_clL
                    else:
                        jump pgn_events_13_newtubs_workwaiter_clR
                "уйти":
                    jump jump_dialogue

    elif ("club_eva_waiter_client_L") in ivent24:
        label pgn_events_13_newtubs_workwaiter_clL:
            if qtime == 1 or qtime == 25:
                label pgn_events_13_newtubs_workwaiter_clL_01:
                    scene pgn_club_eva_badtubs_27
                    call pgn_events_13_newtubs_workwaiter_clL_stripgirl from _call_pgn_events_13_newtubs_workwaiter_clL_stripgirl
                    show pgn_club_eva_badtubs_27_sprite_01_eva
                    show pgn_club_eva_badtubs_27_sprite_05_men
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_27
                    call pgn_events_13_newtubs_workwaiter_clL_stripgirl from _call_pgn_events_13_newtubs_workwaiter_clL_stripgirl_1
                    show pgn_club_eva_badtubs_27_sprite_06_meneva
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_33
                    $ renpy.pause()
                    show pgn_club_eva_badtubs_33_sprite
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_27
                    show pgn_club_eva_badtubs_27_sprite_08_men
                    show pgn_club_eva_badtubs_27_sprite_07_eva
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_29
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_40
                    $ renpy.pause()
                    menu pgn_events_13_newtubs_workwaiter_clL_m1:
                        "Спасибо":
                            jump pgn_events_13_newtubs_workwaiter_thanks
                        "Спрятаться в мужском туалете" if eva_path == 4.3:
                            jump pgn_events_13_newtubs_spy_menrest
                        "Спрятаться в женском туалете" if eva_path == 4.3:
                            jump pgn_events_13_newtubs_spy_womenrest
                        "Продолжить наблюдение":
                            $ qtime += 1
                            scene pgn_club_eva_badtubs_42
                            $ renpy.pause()
                            scene pgn_club_eva_badtubs_43
                            $ renpy.pause()
                            m emo-9 "{i}Блин! Она в мою сторону направляется.{/i}"
                            scene pgn_club_eva_badtubs_45
                            $ renpy.pause()
                            scene pgn_club_eva_badtubs_46
                            show pgn_club_eva_badtubs_46_cum
                            if eva_path < 4.3:
                                m emo-6 "{i}Так. Она не в бар идёт. А куда?{/i}"
                            else:
                                $ renpy.pause()
                            scene pgn_club_eva_badtubs_47
                            m emo-13 "{i}Не видно, что она там делает. Нужен другой угол обзора, но сейчас мне ни как не увидеть.{/i}"
                            if eva_path == 4.2:
                                $ eva_path = 4.3
                        "уйти":
                            pass
            else:
                label pgn_events_13_newtubs_workwaiter_clL_02:
                    if (qtime >= 4 and qtime <= 6) or qtime >= 28:
                        if transport1.use == True:
                            $ transport1.use = False
                            $ transport2.use = True
                        jump loc_pool_move
                    scene pgn_club_eva_badtubs_27
                    call pgn_events_13_newtubs_workwaiter_clL_stripgirl from _call_pgn_events_13_newtubs_workwaiter_clL_stripgirl_2
                    show pgn_club_eva_badtubs_27_sprite_02_couple
                    show pgn_club_eva_badtubs_27_sprite_01_eva
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_29
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_30
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_42
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_27
                    call pgn_events_13_newtubs_workwaiter_clL_stripgirl from _call_pgn_events_13_newtubs_workwaiter_clL_stripgirl_3
                    show pgn_club_eva_badtubs_27_sprite_01_eva
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_43
                    $ renpy.pause()
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_30
                    $ renpy.pause()
                    $ qtime += 1
                    menu pgn_events_13_newtubs_workwaiter_clL_m2:
                        "Спасибо":
                            jump pgn_events_13_newtubs_workwaiter_thanks
                        "Спрятаться в мужском туалете" if eva_path == 4.3:
                            jump pgn_events_13_newtubs_spy_menrest
                        "Спрятаться в женском туалете" if eva_path == 4.3:
                            jump pgn_events_13_newtubs_spy_womenrest
                        "Продолжить наблюдение":
                            $ label_random = renpy.random.randint ( 1, 2)
                            if qtime == 1 or qtime == 25:
                                jump pgn_events_13_newtubs_workwaiter_clL_01
                            elif label_random == 2:
                                jump pgn_events_13_newtubs_workwaiter_clR
                            jump pgn_events_13_newtubs_workwaiter_clL_02
                        "уйти":
                            pass
    elif ("club_eva_waiter_client_R") in ivent24:
        $ ivent24.remove("club_eva_waiter_client_R")
        label pgn_events_13_newtubs_workwaiter_clR:
            if qtime == 1 or qtime == 25:
                label pgn_events_13_newtubs_workwaiter_clR_01:
                    scene pgn_club_eva_badtubs_36
                    show pgn_club_eva_badtubs_36_sprite_01_eva
                    show pgn_club_eva_badtubs_36_sprite_03_men
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_36
                    show pgn_club_eva_badtubs_36_sprite_04_evamen
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_38
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_39
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_28
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_40
                    $ renpy.pause()
                    menu pgn_events_13_newtubs_workwaiter_clR_m1:
                        "Спасибо":
                            jump pgn_events_13_newtubs_workwaiter_thanks
                        "Спрятаться в мужском туалете" if eva_path == 4.3:
                            jump pgn_events_13_newtubs_spy_menrest
                        "Спрятаться в женском туалете" if eva_path == 4.3:
                            jump pgn_events_13_newtubs_spy_womenrest
                        "Продолжить наблюдение":
                            $ qtime += 1
                            scene pgn_club_eva_badtubs_41
                            $ renpy.pause()
                            scene pgn_club_eva_badtubs_44
                            show pgn_club_eva_badtubs_44_cum
                            if eva_path < 4.3:
                                m emo-6 "{i}Хм... в стакане что-то белое. Молоко?{/i}"
                            else:
                                $ renpy.pause()
                            scene pgn_club_eva_badtubs_46
                            show pgn_club_eva_badtubs_46_cum
                            if eva_path < 4.3:
                                if qtime < 24:
                                    m emo-0 "{i}Она идёт в бар...{/i}"
                                if qtime >= 24:
                                    m emo-13 "{i}Она снова возвращается в бар... Опять.{/i}"
                                m emo-6 "{i}Так. Она не в бар идёт. А куда?{/i}"
                            else:
                                $ renpy.pause()
                            scene pgn_club_eva_badtubs_47
                            m emo-13 "{i}Не видно, что она там делает. Нужен другой угол обзора, но сейчас мне ни как не увидеть.{/i}"
                            if eva_path == 4.2:
                                $ eva_path = 4.3
                        "уйти":
                            pass
            else:
                label pgn_events_13_newtubs_workwaiter_clR_02:
                    if (qtime >= 4 and qtime <= 6) or qtime >= 28:
                        if transport1.use == True:
                            $ transport1.use = False
                            $ transport2.use = True
                        jump loc_pool_move
                    scene pgn_club_eva_badtubs_36
                    show pgn_club_eva_badtubs_36_sprite_02_couple
                    show pgn_club_eva_badtubs_36_sprite_01_eva
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_28
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_30
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_41
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_36
                    show pgn_club_eva_badtubs_36_sprite_01_eva
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_44
                    $ renpy.pause()
                    scene pgn_club_eva_badtubs_30
                    $ renpy.pause()
                    $ qtime += 1
                    menu pgn_events_13_newtubs_workwaiter_clR_m2:
                        "Спасибо":
                            jump pgn_events_13_newtubs_workwaiter_thanks
                        "Спрятаться в мужском туалете" if eva_path == 4.3:
                            jump pgn_events_13_newtubs_spy_menrest
                        "Спрятаться в женском туалете" if eva_path == 4.3:
                            jump pgn_events_13_newtubs_spy_womenrest
                        "Продолжить наблюдение":
                            $ label_random = renpy.random.randint ( 1, 2)
                            if qtime == 1 or qtime == 25:
                                jump pgn_events_13_newtubs_workwaiter_clR_01
                            elif label_random == 2:
                                jump pgn_events_13_newtubs_workwaiter_clL
                            jump pgn_events_13_newtubs_workwaiter_clR_02
                        "уйти":
                            pass
    jump jump_dialogue

label pgn_events_13_newtubs_workwaiter_clL_stripgirl:
    $ scene_random = renpy.random.randint ( 1, 3)
    if scene_random == 1:
        show pgn_club_eva_badtubs_27_sprite_03_stripgirl
    if scene_random == 2:
        show pgn_club_eva_badtubs_27_sprite_04_stripgirl
    return

label pgn_events_13_newtubs_workwaiter_thanks:
    scene pgn_club_eva_badtubs_48
    m emo-4 "Привет. Я хотел бы поблагодарить за прошлый раз. Спа..."
    scene pgn_club_eva_badtubs_49
    m emo-13 "Эм... Я..."
    m emo-0 "{i}Поговорить не удалось.{/i}"
    jump jump_dialogue


label pgn_events_13_newtubs_spy_menrest:
    $ qtime += 1
    scene pgn_club_eva_badtubs_51
    m emo-0 "{i}Пока никого нет, спрячусь.{/i}"
    scene pgn_club_eva_badtubs_52
    show pgn_club_eva_badtubs_52_men
    $ renpy.pause(5, hard=True)
    m emo-6 "{i}Так стоп! Она же была в женском туалете.{/i}"
    m emo-8 "{i}Блин!{/i}"
    jump loc_club_restr_men


label pgn_events_13_newtubs_spy_womenrest:
    scene pgn_club_eva_badtubs_51
    m emo-0 "{i}Пока никого нет, спрячусь.{/i}"
    scene pgn_club_eva_badtubs_52
    menu pgn_events_13_newtubs_spy_womenrest_m:
        "Ждать":
            $ qtime += 1
            scene pgn_club_eva_badtubs_52
            if qtime == 1 or qtime >= 25:
                show pgn_club_eva_badtubs_52_sprite_04_eva
                m emo-6 "{i}Что она там делает?{/i}"
                m emo-1 "{i}Кто-то идёт.{/i}"
                scene pgn_club_eva_badtubs_53
                other emo-998 "Я сейчас описаюсь."
                other emo-998 "Беги в первую кабинку, она всегда свободная."
                scene pgn_club_eva_badtubs_54
                other emo-998 "Я тебе говорила, не пей перед тем как пойдём развлекаться."
                other emo-998 "О! Кто-то оставил и не допил."
                scene pgn_club_eva_badtubs_55
                other emo-998 "Ммм..."
                scene pgn_club_eva_badtubs_56
                other emo-998 "Попробуй."
                other emo-998 "Это молочный коктейль?"
                scene pgn_club_eva_badtubs_57
                other emo-998 "И зачем всё разлила!"
                other emo-998 "Фу! Это сперма! Как ты можешь это спокойно глотать?"
                other emo-998 "Мне понравилось. И как ты планируешь себе партнера искать. Не понимаю."
                other emo-998 "Всё? Пойдём."
                scene pgn_club_eva_badtubs_52
                m emo-6 "{i}Сперма, сперма, сперма... Аааааа, ясно!!!{/i}"
                scene pgn_club_eva_badtubs_58
                m emo-3 "Привет, Ева!"
                eva emo-131 "[pname_max[0]]!?"
                scene pgn_club_eva_badtubs_59
                eva emo-132 "О нет! Весь материал испорчен."
                m emo-6 "А зачем тебе сперма? Если надо, я могу восполнить потерю."
                if clinic_time > 0:
                    eva emo-130 "Я бы и рада, но ещё не прошло достаточно времени с прошлой твоей сдачи спермы."
                scene pgn_club_eva_badtubs_60
                eva emo-128 "Я узнала, что таблетки, из-за которых у тебя бывают периодические проблемы, продаются в этом клубе. И то что недавно появились новые."
                eva emo-131 "Пробовала купить для исследований, но девушкам, как я поняла не продают. Поэтому договорилась с подругой и иногда заменяю её, но и так всё равно эти таблетки мне не доступны. И вот..."
                m emo-13 "Я их уже принимал."
                eva emo-128 "Да? Может это из-за них тебе было очень плохо?"
                if ("макс_новыетаблетки") in ivent24:
                    m emo-6 "Не знаю. Я недавно принял и всё Нормально."
                    eva emo-131 "Может быть это из-за влияния старой таблетки. Но без материала, я не могу гадать."
                else:
                    if momkate_path == 5:
                        m emo-1 "Не знаю почему, но иногда бывает через 1 час сразу плохо или наоборот так хорошо, что выпускаю сперму в больших количествах."
                        eva emo-131 "Тогда может быть это реакция на старую таблетку? Старые и новые возможно несовместимы. Наверное новые и вызывают эту негативную реакцию."
                        eva emo-131 "Без материалов, я не смогу ничего выяснить."
                    else:
                        m emo-13 "Не знаю, может быть."
                        eva emo-131 "А что если это из-за несовместимости старой и новой таблетки? Но без материала, я не смогу узнать."
                    m emo-13 "Я бы купил, но бармен так смотрит внимательно, что нет возможности купить и забрать с собой."
                $ eva_path = 4.4
                menu:
                    "Могу сейчас" if ("макс_новыетаблетки") in ivent24:
                        m emo-3 "Могу прям сейчас."
                        if clinic_time > 0:
                            eva emo-133 "[pname_max[0]], время ещё не прошло, но спасибо за предложение."
                            m emo-6 "Тогда в другой раз, приму таблетку и после, как обычно, приеду и сдам в Клинике."
                            jump pgn_events_13_newtubs_spy_womenrest_ans2
                        else:
                            eva emo-133 "Пойдём в кабинку, не прям здесь же."
                            jump pgn_events_13_newtubs_evarestroomcum
                    "Куплю и сдам сперму":
                        m emo-1 "Я могу сейчас или потом купить. И после, как обычно, приеду и сдам в Клинике."
                        eva emo-133 "Ох [pname_max[0]]! Спасибо тебе."
                        label pgn_events_13_newtubs_spy_womenrest_ans2:
                            eva emo-131 "Только вот я слышала, что у этой таблетки эффект не долговечен."
                            m emo-6 "Тогда, если ты будешь в клубе, то поделюсь своей спермой прям здесь."
                            eva emo-133 "Спасибо. Буду ждать."
                jump loc_club_dancefloor_03
            else:
                $ label_random = renpy.random.randint ( 1, 4)
                if label_random == 1:
                    show pgn_club_eva_badtubs_52_sprite_01
                if label_random == 2:
                    show pgn_club_eva_badtubs_52_sprite_02
                if label_random == 3:
                    show pgn_club_eva_badtubs_52_sprite_03
                $ renpy.pause(3)
                jump pgn_events_13_newtubs_spy_womenrest_m
        "уйти":
            jump loc_club_dancefloor_03

label pgn_events_13_newtubs_eva:
    call loc_club_locchr from _call_loc_club_locchr
    if "loc_club_restr_women" in location:
        show pgn_club_eva_badtubs_79
    else:
        show pgn_club_eva_badtubs_78
    eva emo-133 "Привет, [pname_max[0]]."
    m emo-3 "Я готов сдать сперму."
    if "loc_club_restr_women" not in location:
        eva emo-133 "Хорошо. Сейчас быстро освобожусь и пойдём в туалет."
    jump pgn_events_13_newtubs_evarestroomcum

label pgn_events_13_newtubs_evarestroomcum:
    scene pgn_club_eva_badtubs_61
    $ PGN_Achadd(pgnach_175, 175)
    eva emo-130 "Снимай штаны и начнём."
    scene pgn_club_eva_badtubs_62_asanosakura
    menu pgn_events_13_newtubs_evarestroomcum_m:
        "Продолжить":
            scene pgn_club_eva_badtubs_63_asanosakura
            $ renpy.pause()
            scene pgn_club_eva_badtubs_64_asanosakura
            m emo-10 "О да!"
            scene pgn_club_eva_badtubs_65_asanosakura
            m emo-3 "{i}Я бы сейчас хотел заняться сексом. Но минет тоже не плохо.{/i}"
            scene pgn_club_eva_badtubs_66_asanosakura
            $ renpy.pause()
            scene pgn_club_eva_badtubs_67_asanosakura
        "Трахнуть горло":
            m emo-3 "А можно я трахну тебя в рот?"
            eva emo-133 "Из-за этой латексной маски так и тянет к сексу?"
            m emo-4 "Можно?"
            eva emo-133 "Можно."
            scene pgn_club_eva_badtubs_71
            $ renpy.pause()
            scene pgn_club_eva_badtubs_72
            m emo-10 "{i}Ого! Ева! Класс!{/i}"
            scene pgn_club_eva_badtubs_73
            m emo-3 "{i}У неё рабочее горло, натренированное.{/i}"
            scene pgn_club_eva_badtubs_74
            m emo-6 "{i}А если ещё глубже?{/i}"
            scene pgn_club_eva_badtubs_75
            $ renpy.pause()
            scene pgn_club_eva_badtubs_76
            eva emo-131 "Аах... Аххх... Ммм... Ахх.."
            scene pgn_club_eva_badtubs_77
            m emo-3 "{i}Если бы не помощь ей со сбором спермы для исследований, залил бы её полностью спермой.{/i}"
            scene pgn_club_eva_badtubs_72
            $ renpy.pause()
            scene pgn_club_eva_badtubs_73
            $ renpy.pause()
            scene pgn_club_eva_badtubs_74
        "Секс":
            m emo-4 "Может займёмся сексом?"
            eva emo-132 "Вагинальная смазка может испортить анализы, и мне нужен чистый биоматериал."
            if condom.have == True:
                m emo-6 "У меня есть презервативы."
                eva emo-133 "А успеешь вытащить?"
            jump pgn_events_13_newtubs_evarestroomcum_m
    m emo-10 "Ева, я почти уже на пределе."
    scene pgn_club_eva_badtubs_68
    m emo-12 "Аргххх!"
    scene pgn_club_eva_badtubs_69
    eva emo-131 "Вау! Как много!"
    scene pgn_club_eva_badtubs_70
    if pgn_ach_repeat != 0:
        $ renpy.pause()
        jump table_pgn_achievement
    eva emo-133 "Спасибо тебе за материал. С меня оплата."
    if eva_path == 4.4:
        menu:
            "Не нужно":
                m emo-13 "Да ладно, мне не нужно."
                eva emo-133 "Бери. Хотя бы возмещу твои траты. Может что купишь ещё себе."
            "Взять":
                pass
    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[1])+" $"+"250")
    $ moneymaxik(250)
    if eva_path == 4.4:
        m emo-3 "В этот раз больше чем обычно."
    $ PGN_Addstatsex(stat_eva, 0, 0, 1, 0, 0)
    $ qtime, clinic_time = qtime+1, 3
    if eva_path == 4.4:
        $ eva_path = 5
    jump loc_club_dancefloor_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
