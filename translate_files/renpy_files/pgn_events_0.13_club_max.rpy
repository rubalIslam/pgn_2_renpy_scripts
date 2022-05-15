











label loc_club_bar_drink:
    scene pgn_location_club_bar_men_01
    menu:
        "Спиртное":
            m emo-0 "Налейте мне чего-нибудь крепкого."
            other emo-999 "Покажи свой паспорт."
            menu:
                "Дома забыл":
                    m emo-0 "Дома забыл. Может всё же нальёте? Я же всё равно заплачу."
                "Кажусь молодым":
                    m emo-3 "По мне не скажешь, но я совершеннолетний и могу пить. В порно снимаюсь, вы может быть меня видели."
                "У меня большие связи":
                    m emo-1 "Я лично знаю директора этого клуба."
                "уйти":
                    jump loc_club_bar
            scene pgn_location_club_bar_men_02
            other emo-999 "Несовершеннолетних не обслуживаем."
            scene pgn_location_club_bar_max_01
            m emo-13 "Здравствуйте..."
        "Сок":
            $ currency -= 20
            $ screennotify("$", 11, 20)
            scene pgn_location_club_bar_max_02
            if (("катя_завтрак_2") in accessiv or ("катя_завтрак_3") in accessiv) and ("momkate_katebreakfast") not in accessiv <= 3.16:
                jump pgn_events_13_momkate_04
            $ renpy.pause(10)
        "Таблетки" if kate_path >= 4 and ("макс_новыетаблетки") not in ivent24 and eva_path >= 4:
            if momkate_path < 5:
                m emo-13 "Эм... мне это... Как бы сказать..."
                other emo-999 "Госпожа меня предупредила. Вот, прими их."
                m emo-0 "Спасибо"
                scene blur_pgn_club_bar
                m emo-0 "Осталось дождаться, когда за мной придут."
                if stat_max.tubs1 > 0:
                    jump pgn_events_13_newtubs_01
                else:
                    jump pgn_events_13_momkate_end
            else:
                m emo-0 "Можно мне таблетки?"
                other emo-999 "$50"
                menu:
                    "Заплатить":
                        $ currency, qtime = currency-50, qtime+1
                        $ screennotify("$", 11, 50)
                        $ ivent24.append("макс_новыетаблетки")
                        scene black with dissolve
                        $ renpy.pause(3)
                        if stat_max.tubs1 > 0 and eva_path < 4.4:
                            jump pgn_events_13_newtubs_01
                        if stat_max.tubs1 > 0 and eva_path >= 4.4:
                            jump pgn_clinic_max_afterclub
                    "уйти":
                        pass
        "уйти":
            pass
    jump loc_club_bar






label loc_club_dancefloor_max:
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random == 1:
        scene pgn_location_club_dancefloor_max_01
    if label_random == 2:
        scene pgn_location_club_dancefloor_max_02_vadx
    if label_random == 3:
        scene pgn_location_club_dancefloor_max_03_vadx
    if label_random == 4:
        scene pgn_location_club_dancefloor_max_04_vadx
    $ renpy.pause(10)
    $ qtime += 1
    if "loc_club_dancefloor_01" in location:
        jump loc_club_dancefloor_01
    if "loc_club_dancefloor_02" in location:
        jump loc_club_dancefloor_02
    if "loc_club_dancefloor_03" in location:
        jump loc_club_dancefloor_03





label pgn_club_striptease_girl1:
    scene pgn_club_striptease_girl1_01
    menu:
        "$100":
            $ stripgirlm1 += 100
            $ currency -= 100
            $ screennotify("$", 11, 100)
        "$300":
            $ stripgirlm1 += 300
            $ currency -= 300
            $ screennotify("$", 11, 300)
        "$500":
            $ stripgirlm1 += 500
            $ currency -= 500
            $ screennotify("$", 11, 500)
        "VIP комната" if stripgirlm1 >= 500 and stripgirlm2 >= 500 and ("stripvip_sex") not in ivent24 and "club_gh_макснекончил" not in ivent24:
            jump pgn_club_striptease_girls_viproom
        "уйти":
            jump loc_club_dancefloor_02
    $ qtime += 1
    if stripgirlm1 < 300:
        scene pgn_club_striptease_girl1_02
        $ renpy.pause()
        scene pgn_club_striptease_girl1_03
        $ renpy.pause()
        scene pgn_club_striptease_girl1_04
        $ renpy.pause()
        scene pgn_club_striptease_girl1_05
        $ renpy.pause()
        scene pgn_club_striptease_girl1_06
        $ renpy.pause()
        scene pgn_club_striptease_girl1_07
        $ renpy.pause()
        scene pgn_club_striptease_girl1_08
        $ renpy.pause()
    if stripgirlm1 >= 300 and stripgirlm1 < 500:
        scene pgn_club_striptease_girl1_02
        $ renpy.pause()
        scene pgn_club_striptease_girl1_03
        $ renpy.pause()
        scene pgn_club_striptease_girl1_04
        $ renpy.pause()
        scene pgn_club_striptease_girl1_05
        $ renpy.pause()
        scene pgn_club_striptease_girl1_06
        $ renpy.pause()
        scene pgn_club_striptease_girl1_07
        $ renpy.pause()
        scene pgn_club_striptease_girl1_08
        $ renpy.pause()
        scene pgn_club_striptease_girl1_09
        $ renpy.pause()
        scene pgn_club_striptease_girl1_10
        $ renpy.pause()
        scene pgn_club_striptease_girl1_11
        $ renpy.pause()
        scene pgn_club_striptease_girl1_12
        $ renpy.pause()
        scene pgn_club_striptease_girl1_13
        $ renpy.pause()
    if stripgirlm1 >= 500:
        scene pgn_club_striptease_girl1_05
        $ renpy.pause()
        scene pgn_club_striptease_girl1_06
        $ renpy.pause()
        scene pgn_club_striptease_girl1_07
        $ renpy.pause()
        scene pgn_club_striptease_girl1_08
        $ renpy.pause()
        scene pgn_club_striptease_girl1_09
        $ renpy.pause()
        scene pgn_club_striptease_girl1_10
        $ renpy.pause()
        scene pgn_club_striptease_girl1_11
        $ renpy.pause()
        scene pgn_club_striptease_girl1_12
        $ renpy.pause()
        scene pgn_club_striptease_girl1_13
        $ renpy.pause()
        scene pgn_club_striptease_girl1_14
        $ renpy.pause()
        scene pgn_club_striptease_girl1_15
        $ renpy.pause()
        scene pgn_club_striptease_girl1_16
        $ renpy.pause()
        scene pgn_club_striptease_girl1_17
        $ renpy.pause()
    if ("stripvip_sex") in ivent24 and ("club_gh_sex") in ivent24:
        pass
    elif (stripgirlm1 >= 400 and renpy.random.randint ( 1, 3) == 3) or stripgirlm1 >= 500:
        scene pgn_club_striptease_girl1_18
        other emo-998 "Спасибо вам за ваши щедрые чаевые. Хотите продолжения?"
        menu:
            "VIP с стриптизёршами" if stripgirlm2 >= 500 and ("stripvip_sex") not in ivent24 and "club_gh_макснекончил" not in ivent24:
                jump pgn_club_striptease_girls_viproom
            "GH" if momkate_path >= 5 and ("club_gh_sex") not in ivent24 and "club_gh_макснекончил" not in ivent24:
                jump pgn_club_striptease_girl1_gh
            "Отказаться":
                m emo-3 "Спасибо за танец. Но у меня другие планы."
                other emo-998 "Жаль."
    jump loc_club_dancefloor_02

label pgn_club_striptease_girl2:
    scene pgn_club_striptease_girl2_01
    menu:
        "$100":
            $ stripgirlm2 += 100
            $ currency -= 100
            $ screennotify("$", 11, 100)
        "$300":
            $ stripgirlm2 += 300
            $ currency -= 300
            $ screennotify("$", 11, 300)
        "$500":
            $ stripgirlm2 += 500
            $ currency -= 500
            $ screennotify("$", 11, 500)
        "VIP комната" if stripgirlm1 >= 500 and stripgirlm2 >= 500 and ("stripvip_sex") not in ivent24 and "club_gh_макснекончил" not in ivent24:
            jump pgn_club_striptease_girls_viproom
        "уйти":
            jump loc_club_dancefloor_02
    $ qtime += 1
    if stripgirlm1 < 300:
        scene pgn_club_striptease_girl2_02
        $ renpy.pause()
        scene pgn_club_striptease_girl2_03
        $ renpy.pause()
        scene pgn_club_striptease_girl2_04
        $ renpy.pause()
        scene pgn_club_striptease_girl2_05
        $ renpy.pause()
        scene pgn_club_striptease_girl2_06
        $ renpy.pause()
        scene pgn_club_striptease_girl2_07
        $ renpy.pause()
        scene pgn_club_striptease_girl2_08
        $ renpy.pause()
    if stripgirlm1 >= 300 and stripgirlm1 < 500:
        scene pgn_club_striptease_girl2_02
        $ renpy.pause()
        scene pgn_club_striptease_girl2_03
        $ renpy.pause()
        scene pgn_club_striptease_girl2_04
        $ renpy.pause()
        scene pgn_club_striptease_girl2_05
        $ renpy.pause()
        scene pgn_club_striptease_girl2_06
        $ renpy.pause()
        scene pgn_club_striptease_girl2_07
        $ renpy.pause()
        scene pgn_club_striptease_girl2_08
        $ renpy.pause()
        scene pgn_club_striptease_girl2_09
        $ renpy.pause()
        scene pgn_club_striptease_girl2_10
        $ renpy.pause()
        scene pgn_club_striptease_girl2_11
        $ renpy.pause()
        scene pgn_club_striptease_girl2_13
        $ renpy.pause()
    if stripgirlm1 >= 500:
        scene pgn_club_striptease_girl2_02
        $ renpy.pause()
        scene pgn_club_striptease_girl2_03
        $ renpy.pause()
        scene pgn_club_striptease_girl2_04
        $ renpy.pause()
        scene pgn_club_striptease_girl2_05
        $ renpy.pause()
        scene pgn_club_striptease_girl2_06
        $ renpy.pause()
        scene pgn_club_striptease_girl2_07
        $ renpy.pause()
        scene pgn_club_striptease_girl2_08
        $ renpy.pause()
        scene pgn_club_striptease_girl2_09
        $ renpy.pause()
        scene pgn_club_striptease_girl2_10
        $ renpy.pause()
        scene pgn_club_striptease_girl2_11
        $ renpy.pause()
        scene pgn_club_striptease_girl2_12
        $ renpy.pause()
        scene pgn_club_striptease_girl2_13
        $ renpy.pause()
        scene pgn_club_striptease_girl2_14
        $ renpy.pause()
        scene pgn_club_striptease_girl2_15
        $ renpy.pause()
        scene pgn_club_striptease_girl2_16
        $ renpy.pause()
        scene pgn_club_striptease_girl2_17
        $ renpy.pause()
    if ("stripvip_sex") in ivent24 and ("club_gh_sex") in ivent24:
        pass
    elif (stripgirlm2 >= 400 and renpy.random.randint ( 1, 3) == 3) or stripgirlm2 >= 500:
        scene pgn_club_striptease_girl1_18
        other emo-998 "Спасибо вам за ваши щедрые чаевые. Хотите продолжения?"
        menu:
            "VIP с стриптизёршами" if stripgirlm1 >= 500 and ("stripvip_sex") not in ivent24 and "club_gh_макснекончил" not in ivent24:
                jump pgn_club_striptease_girls_viproom
            "GH" if momkate_path >= 5 and ("club_gh_sex") not in ivent24 and "club_gh_макснекончил" not in ivent24:
                jump pgn_club_striptease_girl2_gh
            "Отказаться":
                m emo-3 "Спасибо за танец. Но у меня другие планы."
                other emo-998 "Жаль."
    jump loc_club_dancefloor_02

label pgn_club_striptease_girls_viproom:
    scene pgn_club_striptease_girls_viproom_01
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_02
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_03
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_04
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_05
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_06
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_07
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_08
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_09
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_10
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_11
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_12
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_13
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_14
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_15
    $ renpy.pause()
    scene pgn_club_striptease_girls_viproom_16
    $ renpy.pause()
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random == 1:
        scene pgn_club_striptease_girls_viproom_17
    if label_random == 2:
        scene pgn_club_striptease_girls_viproom_18
    if label_random == 3:
        scene pgn_club_striptease_girls_viproom_19
    menu:
        "Анал с азиаткой":
            label pgn_club_striptease_girls2_viproom_anal:
                scene pgn_club_striptease_girls_viproom_20
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_21
                m emo-3 "{i}Тугой анал у неё. Член еле проходит.{/i}"
                scene pgn_club_striptease_girls_viproom_22
                other emo-998 "Ааа... Аааах..."
                scene pgn_club_striptease_girls_viproom_23
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_24
                m emo-4 "{i}О да! Ещё глубже.{/i}"
                scene pgn_club_striptease_girls_viproom_25
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_26
                $ PGN_Achadd(pgnach_162, 162)
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_27
                m emo-3 "{i}Вот это вид. Супер!{/i}"
                scene pgn_club_striptease_girls_viproom_28
                other emo-998 "Аааххх!"
                scene pgn_club_striptease_girls_viproom_29
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_30
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_31
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_32
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_33
                m emo-10 "{i}Ох блин! Я уже почти на пределе.{/i}"
                scene pgn_club_striptease_girls_viproom_34
                menu:
                    "Кончить в анал":
                        scene pgn_club_striptease_girls_viproom_35
                        m emo-12 "Аррргххх!!!"
                        other emo-998 "Аааахххх!"
                        scene pgn_club_striptease_girls_viproom_36
                        $ renpy.pause()
                    "Кончить в рот блондинке":
                        scene pgn_club_striptease_girls_viproom_37
                        m emo-12 "Аррргххх!!!"
                        scene pgn_club_striptease_girls_viproom_38
                        m emo-9 "{i}Ого! Как присосалась. Высасывает до самой кали.{/i}"
                        scene pgn_club_striptease_girls_viproom_39
                        $ renpy.pause()
                        scene pgn_club_striptease_girls_viproom_40
                        $ renpy.pause()
                        scene pgn_club_striptease_girls_viproom_41
                        $ renpy.pause()
        "Вагинал с блондинкой":
            label pgn_club_striptease_girls1_viproom_vag:
                scene pgn_club_striptease_girls_viproom_42
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_43
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_44
                m emo-3 "{i}Вау!{/i}"
                scene pgn_club_striptease_girls_viproom_45
                $ PGN_Achadd(pgnach_163, 163)
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_46
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_47
                m emo-4 "{i}Классная попа. Сейчас её оттрахаю, что всю неделю будет только о моём члене думать.{/i}"
                scene pgn_club_striptease_girls_viproom_48
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_49
                other emo-998 "Аааах!"
                scene pgn_club_striptease_girls_viproom_51
                $ renpy.pause()
                scene pgn_club_striptease_girls_viproom_52
                m emo-12 "{i}Да, да, да, сейчас...{/i}"
                scene pgn_club_striptease_girls_viproom_53
                menu:
                    "Кончить в киску":
                        scene pgn_club_striptease_girls_viproom_54
                        $ renpy.pause()
                        scene pgn_club_striptease_girls_viproom_55
                        m emo-12 "Аррргххх!"
                        scene pgn_club_striptease_girls_viproom_56
                        $ renpy.pause()
                    "Кончить в рот азиатке":
                        scene pgn_club_striptease_girls_viproom_57
                        m emo-12 "Аррргххх!"
                        scene pgn_club_striptease_girls_viproom_58
                        $ renpy.pause()
    if pgn_ach_repeat != 0:
        jump table_pgn_achievement
    $ qtime += 1
    $ ivent24.append("stripvip_sex")
    jump loc_club_dancefloor_02










label pgn_cluv_gh_max_choice:
    if ("club_gh_sex") in ivent24 and stat_max.tubs1 <= 0 and ("макс_новыетаблетки") not in ivent24:
        m emo-13 "Я больше сегодня не смогу. Если только с помощью таблетки."
    elif "club_gh_макснекончил" in ivent24 and "club_gh_katehelp" not in ivent24:
        m emo-2 "Я не смог кончить и член всё ещё болит"
    elif "club_gh_макснекончил" in ivent24 and "club_gh_katehelp" in ivent24:
        m emo-13 "С меня на сегодня достаточно. А то вдруг снова не смогу кончить."
    elif ("club_gh_максраздет") not in ivent24:
        menu pgn_cluv_gh_max_choice_m1:
            "Раздеться":
                scene pgn_club_gh_max_01
                $ renpy.pause()
                scene pgn_club_gh_max_02
                $ renpy.pause()
                call pgn_cluv_gh_scene from _call_pgn_cluv_gh_scene
                jump pgn_cluv_gh_max_choice_m2
            "отмена":
                pass
    elif ("club_gh_максраздет") in ivent24:
        label pgn_cluv_gh_max_choice_m2:
            call pgn_cluv_gh_scene from _call_pgn_cluv_gh_scene_1
            menu:
                "Кабинки слева":
                    if label_random == 1 and "club_gh_sex_girl1" not in ivent24:
                        jump pgn_club_gh_cabl_girl1
                    if label_random == 2 and "club_gh_sex_girl2" not in ivent24:
                        jump pgn_club_gh_cabl_girl2
                    scene pgn_club_gh_max_03
                    m emo-0 "Никого нет."
                    jump pgn_cluv_gh_max_choice_m2
                "Кабинки справа":
                    if label_random != 3 and ("club_gh_svetabigtits") in ivent24:
                        scene pgn_club_gh_max_04
                        m emo-0 "Никого нет."
                        menu pgn_cluv_gh_max_choice_m3:
                            "Попытать счастье":
                                scene pgn_club_gh_max_05
                                $ label_random, qtime = renpy.random.randint ( 1, 3), qtime+1
                                if label_random == 3 and ("club_gh_svetabigtits") not in ivent24:
                                    $ renpy.pause(5)
                                    scene pgn_club_gh_max_06
                                    m emo-3 "{i}Свезло{/i}"
                                    jump pgn_cluv_gh_cabr_sveta
                                elif qtime >= 4 and qtime < 6:
                                    if transport1.use == True:
                                        $ transport1.use = False
                                        $ transport2.use = True
                                    jump loc_pool_move
                                else:
                                    $ renpy.pause(5)
                                    jump pgn_cluv_gh_max_choice_m3
                            "назад":
                                jump pgn_cluv_gh_max_choice_m2
                    else:
                        scene pgn_club_gh_max_04
                        show pgn_club_gh_max_04_activ
                        m emo-4 "Кто-то есть."
                        jump pgn_cluv_gh_cabr_sveta
                "уйти":
                    jump loc_club_dancefloor_02
    call pgn_cluv_gh_scene from _call_pgn_cluv_gh_scene_2
    call screen loc_club_gh

label pgn_cluv_gh_scene:
    scene pgn_club_gh
    if label_random == 1 and "club_gh_sex_girl1" not in ivent24:
        show pgn_club_gh_sprite_01
        show pgn_club_gh_sprite_03
    if label_random == 2 and "club_gh_sex_girl2" not in ivent24:
        show pgn_club_gh_sprite_02
        show pgn_club_gh_sprite_03
    return


label pgn_club_striptease_girl1_gh:
    scene pgn_club_gh_max_04
    show pgn_club_gh_max_04_activ
    $ renpy.pause(3)
    scene pgn_club_gh_max_07
    m emo-6 "Хм... горело зеленым, а ни кого."
    scene pgn_club_gh_stripgirl1_01
    m emo-6 "{i}Со стулом пришла.{/i}"
    scene pgn_club_gh_stripgirl1_02
    m emo-1 "{i}Нет бы минет сделать, сразу начала со снятия юбки.{/i}"
    scene pgn_club_gh_stripgirl1_03
    $ renpy.pause()
    scene pgn_club_gh_stripgirl1_04
    m emo-3 "{i}Хороша.{/i}"
    scene pgn_club_gh_stripgirl1_05
    m emo-4 "{i}Горячая попка.{/i}"
    scene animated pgn_club_gh_stripgirl1_06
    m emo-5 "{i}Блин! Дразнит.{/i}"
    scene animated pgn_club_gh_stripgirl1_07a
    $ renpy.pause()
    scene animated pgn_club_gh_stripgirl1_07b
    $ renpy.pause()
    if stat_max.tubs1 <= 0 and ("макс_новыетаблетки") not in ivent24:
        scene pgn_club_gh_stripgirl1_08
        m emo-12 "Аррргххх!!!"
        scene pgn_club_gh_stripgirl1_09
        $ renpy.pause()
    else:
        scene pgn_club_gh_stripgirl1_10
        other emo-998 "Ааааахххх!!!"
        scene pgn_club_gh_stripgirl1_11
        other emo-998 "Ааааа... Ааа..."
        scene pgn_club_gh_stripgirl1_12
        m emo-4 "Я ещё не всё..."
        scene pgn_club_gh_stripgirl1_13
        other emo-998 "Да, сладкий! Я не отпущу тебя, пока ты не кончишь."
        scene animated pgn_club_gh_stripgirl1_14a
        $ renpy.pause()
        scene pgn_club_gh_stripgirl1_14b_01
        other emo-998 "Глубже... Глубже..."
        scene pgn_club_gh_stripgirl1_14b_15
        $ renpy.pause()
        scene pgn_club_gh_stripgirl1_14b_01
        $ renpy.pause()
        scene pgn_club_gh_stripgirl1_14b_15
        $ renpy.pause()
        if stat_max.tubs1 > 0:
            scene pgn_club_gh_stripgirl1_15
            m emo-12 "Аррргххх!"
            scene pgn_club_gh_stripgirl1_17
            $ renpy.pause()
        if ("макс_новыетаблетки") in ivent24:
            if renpy.random.randint ( 1, 3) != 2:
                scene pgn_club_gh_stripgirl1_20
                other emo-998 "Ааааа... Ааа..."
                scene pgn_club_gh_stripgirl1_21
                $ renpy.pause()
                scene pgn_club_gh_stripgirl1_22
                $ renpy.pause()
                scene animated pgn_club_gh_stripgirl1_07a_fast
                $ renpy.pause()
                scene pgn_club_gh_stripgirl1_23
                m emo-12 "Аррргххх!"
                scene pgn_club_gh_stripgirl1_24
                other emo-998 "Ааааа..."
                scene pgn_club_gh_stripgirl1_25
                m emo-7 "Класс!"
            else:
                scene pgn_club_gh_stripgirl1_16
                m emo-12 "Аррргххх!"
                scene pgn_club_gh_stripgirl1_18
                $ renpy.pause()
                scene pgn_club_gh_stripgirl1_19
                $ renpy.pause()
    $ qtime += 1
    $ ivent24.append("club_gh_sex")
    $ ivent24.append("club_gh_максраздет")
    jump loc_club_gh


label pgn_club_striptease_girl2_gh:
    scene pgn_club_gh_max_04
    show pgn_club_gh_max_04_activ
    $ renpy.pause(3)
    scene pgn_club_gh_max_08
    m emo-6 "{i}Хм... Откуда этот стол?{/i}"
    scene pgn_club_gh_stripgirl2_01
    $ renpy.pause()
    scene pgn_club_gh_stripgirl2_02
    $ renpy.pause()
    scene pgn_club_gh_stripgirl2_03
    $ renpy.pause()
    scene pgn_club_gh_stripgirl2_04
    $ renpy.pause()
    scene pgn_club_gh_stripgirl2_05
    $ renpy.pause()
    scene pgn_club_gh_stripgirl2_06
    $ renpy.pause()
    scene pgn_club_gh_stripgirl2_07
    m emo-3 "{i}Попка как у [pname_liza[1]].{/i}"
    scene animated pgn_club_gh_stripgirl2_08
    $ renpy.pause()
    if stat_max.tubs1 <= 0 and ("макс_новыетаблетки") not in ivent24:
        scene pgn_club_gh_stripgirl2_14
        m emo-12 "Аррргххх!!!"
        scene pgn_club_gh_stripgirl2_15
        $ renpy.pause()
    else:
        scene pgn_club_gh_stripgirl2_10
        other emo-998 "Хм... почему не кончаешь?"
        m emo-3 "Так просто со мной не справиться."
        scene pgn_club_gh_stripgirl2_11
        m emo-6 "{i}Это что у неё? Лубрикант? Ей понадобится его много.{/i}"
        scene pgn_club_gh_stripgirl2_12
        other emo-998 "Я готова."
        scene pgn_club_gh_stripgirl2_13
        $ renpy.pause()
        scene animated pgn_club_gh_stripgirl2_09a
        $ renpy.pause()
        scene animated pgn_club_gh_stripgirl2_09b
        $ renpy.pause()
        if stat_max.tubs1 > 0:
            scene pgn_club_gh_stripgirl2_anim_09b_15
            m emo-12 "Аррргххх!!!"
            scene pgn_club_gh_stripgirl2_anim_09a_15
            $ renpy.pause()
            scene pgn_club_gh_stripgirl2_16
            $ renpy.pause()
        if ("макс_новыетаблетки") in ivent24:
            scene pgn_club_gh_stripgirl2_17
            m emo-12 "Аррргххх!!!"
            scene pgn_club_gh_stripgirl2_18
            other emo-998 "Ааааахх..."
            scene pgn_club_gh_stripgirl2_19
            $ renpy.pause()
    $ qtime += 1
    $ ivent24.append("club_gh_sex")
    $ ivent24.append("club_gh_максраздет")
    jump loc_club_gh






label pgn_club_gh_cabl_girl1:
    $ scene_random = 0
    scene pgn_club_gh_girl1_01
    menu pgn_club_gh_cabl_girl1_m1:
        "Какой секс?" if "club_gh_girl1_qestion1" not in ivent24 and pgn_ach_repeat == 0:
            $ ivent24.append("club_gh_girl1_qestion1")
            m emo-3 "Какой секс предпочитаете?"
            other emo-998 "Анальный, только в попку."
            jump pgn_club_gh_cabl_girl1_m1
        "Куни" if "club_gh_girl1_cuni" not in ivent24 and "club_gh_girl1_anus" not in ivent24 and pgn_ach_repeat == 0:
            label pgn_club_gh_cabl_girl1_17:
                if scene_random == 0:
                    scene pgn_club_gh_girl1_17_vezdessushij
                    show screen scene_pgn_club_gh_cabl_girl1(17)
                if scene_random == 1:
                    scene pgn_club_gh_girl1_17b
                    show screen scene_pgn_club_gh_cabl_girl1(17)
            m emo-4 "{i}Ммм... из её киски сочится сок. Она и без куни готова.{/i}"
            label pgn_club_gh_cabl_girl1_18:
                if scene_random == 0:
                    scene pgn_club_gh_girl1_18
                    show screen scene_pgn_club_gh_cabl_girl1(18)
                if scene_random == 1:
                    scene pgn_club_gh_girl1_18b
                    show screen scene_pgn_club_gh_cabl_girl1(18)
            other emo-998 "Ахх! Ммм! Я завелась, хочу анала. Может трахнешь меня в попку? Порви мою попку."
            hide screen scene_pgn_club_gh_cabl_girl1
            $ ivent24.append("club_gh_girl1_qestion1")
            jump pgn_club_gh_cabl_girl1_m1
        "Вылизать анал" if "club_gh_girl1_cuni" in ivent24 and "club_gh_girl1_anus" not in ivent24 and pgn_ach_repeat == 0:
            label pgn_club_gh_cabl_girl1_19:
                if scene_random == 0:
                    scene pgn_club_gh_girl1_19
                    show screen scene_pgn_club_gh_cabl_girl1(19)
                if scene_random == 1:
                    scene pgn_club_gh_girl1_19b
                    show screen scene_pgn_club_gh_cabl_girl1(19)
            other emo-998 "Ох да! Продолжай. Ммм..."
            label pgn_club_gh_cabl_girl1_20:
                if scene_random == 0:
                    scene pgn_club_gh_girl1_20
                    show screen scene_pgn_club_gh_cabl_girl1(20)
                if scene_random == 1:
                    scene pgn_club_gh_girl1_19b
                    show screen scene_pgn_club_gh_cabl_girl1(20)
            other emo-998 "Ох! Больше не могу. Трахни меня уже наконец. Ну же, давай!"
            hide screen scene_pgn_club_gh_cabl_girl1
            $ ivent24.append("club_gh_girl1_qestion1")
        "Подрочить" if pgn_ach_repeat == 0:
            label pgn_club_gh_cabl_girl1_2:
                if scene_random == 0:
                    scene pgn_club_gh_girl1_02
                    show screen scene_pgn_club_gh_cabl_girl1(2)
                if scene_random == 1:
                    scene pgn_club_gh_girl1_02b
                    show screen scene_pgn_club_gh_cabl_girl1(2)
            m emo-3 "{i}С чего бы не начать?{/i}"
            label pgn_club_gh_cabl_girl1_3:
                if scene_random == 0:
                    scene pgn_club_gh_girl1_03
                    show screen scene_pgn_club_gh_cabl_girl1(3)
                if scene_random == 1:
                    scene pgn_club_gh_girl1_03b
                    show screen scene_pgn_club_gh_cabl_girl1(3)
            other emo-998 "Ммм! Войди уже членом в мою попку."
            hide screen scene_pgn_club_gh_cabl_girl1
            menu pgn_club_gh_cabl_girl1_m2:
                "Анал":
                    hide screen scene_pgn_club_gh_cabl_girl1
                    jump pgn_club_gh_cabl_girl1_anal
                "Пальцы в киску":
                    label pgn_club_gh_cabl_girl1_4:
                        if scene_random == 0:
                            scene pgn_club_gh_girl1_04
                            show screen scene_pgn_club_gh_cabl_girl1(4)
                        if scene_random == 1:
                            scene pgn_club_gh_girl1_04b
                            show screen scene_pgn_club_gh_cabl_girl1(4)
                    other emo-998 "Ааа! Вынул пальцы из моей киски!"
                    hide screen scene_pgn_club_gh_cabl_girl1
                    menu:
                        "Всунуть глубже":
                            m emo-6 "{i}Хм... во что-то я уперся. Девственница? Да не может быть.{/i}"
                            label pgn_club_gh_cabl_girl1_5:
                                if scene_random == 0:
                                    scene pgn_club_gh_girl1_05
                                    show screen scene_pgn_club_gh_cabl_girl1(5)
                                if scene_random == 1:
                                    scene pgn_club_gh_girl1_05b
                                    show screen scene_pgn_club_gh_cabl_girl1(5)
                            other emo-998 "Аххх! Чёрт! Сука, ты что делаешь!"
                            hide screen scene_pgn_club_gh_cabl_girl1
                            scene pgn_club_gh_girl1_06
                            m emo-8 "Ай!"
                            scene pgn_club_gh_girl1_07
                            $ renpy.pause(5)
                            scene pgn_club_gh_girl1_08
                            $ renpy.pause(5)
                            scene black with dissolve
                            $ renpy.pause(5, hard=True)
                        "Убрать палец":
                            jump pgn_club_gh_cabl_girl1_m2
                "Пальцы в попку" if "club_gh_girl1_assfing_3" not in ivent24:
                    if "club_gh_girl1_assfing_2" not in ivent24:
                        $ ivent24.append ("club_gh_girl1_assfing_2")
                        label pgn_club_gh_cabl_girl1_12:
                            if scene_random == 0:
                                scene pgn_club_gh_girl1_12_vezdessushij
                                show screen scene_pgn_club_gh_cabl_girl1(12)
                            if scene_random == 1:
                                scene pgn_club_gh_girl1_12b
                                show screen scene_pgn_club_gh_cabl_girl1(12)
                        other emo-998 "Ох, да! Тебе нравится засовывать свои пальчики в дырочки?"
                        other emo-998 "Засунь в меня свой самый большой пальчик."
                    else:
                        label pgn_club_gh_cabl_girl1_13:
                            if scene_random == 0:
                                scene pgn_club_gh_girl1_13_vezdessushij
                                show screen scene_pgn_club_gh_cabl_girl1(13)
                            if scene_random == 1:
                                scene pgn_club_gh_girl1_13b
                                show screen scene_pgn_club_gh_cabl_girl1(13)
                        other emo-998 "Ммм! Как хорошо! Но будет ещё лучше, если трахнешь эту дырочку, мою грешную попку."
                    hide screen scene_pgn_club_gh_cabl_girl1
                    jump pgn_club_gh_cabl_girl1_m2
                "Продолжить дрочить":
                    label pgn_club_gh_cabl_girl1_9:
                        if scene_random == 0:
                            scene pgn_club_gh_girl1_09
                            show screen scene_pgn_club_gh_cabl_girl1(9)
                        if scene_random == 1:
                            scene pgn_club_gh_girl1_09b
                            show screen scene_pgn_club_gh_cabl_girl1(9)
                    other emo-998 "Ну же, оттрахай меня, порви мою анальную дырочку."
                    if renpy.random.randint ( 1, 3) != 3:
                        jump pgn_club_gh_cabl_girl1_m2
                    label pgn_club_gh_cabl_girl1_10:
                        if scene_random == 0:
                            scene pgn_club_gh_girl1_10_vezdessushij
                            show screen scene_pgn_club_gh_cabl_girl1(10)
                        if scene_random == 1:
                            scene pgn_club_gh_girl1_09b
                            show screen scene_pgn_club_gh_cabl_girl1(10)
                    m emo-3 "{i}Мне нравится это. Не нужно платить, смотри, трогай и дрочи сколько хочешь{/i}"
                    label pgn_club_gh_cabl_girl1_11:
                        if scene_random == 0:
                            scene pgn_club_gh_girl1_11_vezdessushij
                            show screen scene_pgn_club_gh_cabl_girl1(11)
                        if scene_random == 1:
                            scene pgn_club_gh_girl1_11b
                            show screen scene_pgn_club_gh_cabl_girl1(11)
                    m emo-10 "Аргххх!!!"
                    other emo-998 "А как же секс? Фрх... Надеялась на секс, а тут дрочер, только подрочить пришёл."
                    hide screen scene_pgn_club_gh_cabl_girl1
        "Вагинал" if pgn_ach_repeat == 0:
            label pgn_club_gh_cabl_girl1_14:
                if scene_random == 0:
                    scene pgn_club_gh_girl1_14_vezdessushij
                    show screen scene_pgn_club_gh_cabl_girl1(14)
                if scene_random == 1:
                    scene pgn_club_gh_girl1_05b
                    show screen scene_pgn_club_gh_cabl_girl1(14)
            other emo-998 "Нет! Никакого вагинального секса! Вытащи!"
            hide screen scene_pgn_club_gh_cabl_girl1
            menu:
                "Глубже":
                    label pgn_club_gh_cabl_girl1_15:
                        if scene_random == 0:
                            scene pgn_club_gh_girl1_15_vezdessushij
                            show screen scene_pgn_club_gh_cabl_girl1(15)
                        if scene_random == 1:
                            scene pgn_club_gh_girl1_15b
                            show screen scene_pgn_club_gh_cabl_girl1(15)
                    other emo-998 "Нет! Тварь! Мужлан, сука!"
                    hide screen scene_pgn_club_gh_cabl_girl1
                    scene pgn_club_gh_girl1_16_vezdessushij
                    $ renpy.pause(5)
                    scene pgn_club_gh_girl1_08
                    $ renpy.pause(5)
                    scene black with dissolve
                    $ renpy.pause(5, hard=True)
                    $ ivent24.append("club_gh_sex_girl1_vaginal")
                    jump pgn_clinic_max_afterclub
                "Вытащить":
                    hide screen scene_pgn_club_gh_cabl_girl1
                    jump pgn_club_gh_cabl_girl1_m1
        "Анал":
            label pgn_club_gh_cabl_girl1_anal:
                scene pgn_club_gh_girl1_21
                other emo-998 "Засовывай глубже. Ммм..."
                label pgn_club_gh_cabl_girl1_21:
                    if scene_random == 0:
                        scene pgn_club_gh_girl1_21
                        show screen scene_pgn_club_gh_cabl_girl1(21)
                    if scene_random == 1:
                        scene animated pgn_club_gh_girl1_26
                        show screen scene_pgn_club_gh_cabl_girl1(21)
                other emo-998 "Ах... Аааххх... Мммм... Аааахх..."
                other emo-998 "Большой, огромный... Класс! Продолжай малыш."
                label pgn_club_gh_cabl_girl1_22:
                    if scene_random == 0:
                        scene pgn_club_gh_girl1_22
                        show screen scene_pgn_club_gh_cabl_girl1(22)
                    if scene_random == 1:
                        scene animated pgn_club_gh_girl1_26
                        show screen scene_pgn_club_gh_cabl_girl1(22)
                other emo-998 "Ох да! Да, да! Продолжай долбить мою попку. Да!"
                label pgn_club_gh_cabl_girl1_23:
                    if scene_random == 0:
                        scene pgn_club_gh_girl1_23
                        show screen scene_pgn_club_gh_cabl_girl1(23)
                    if scene_random == 1:
                        scene animated pgn_club_gh_girl1_27
                        show screen scene_pgn_club_gh_cabl_girl1(23)
                $ renpy.pause()
                hide screen scene_pgn_club_gh_cabl_girl1
                menu:
                    "Кончить на неё":
                        if scene_random == 1:
                            scene pgn_club_gh_girl1_anim_27_01
                        m emo-12 "Аррргххх!!!"
                        scene pgn_club_gh_girl1_24
                    "Кончить в анал":
                        if scene_random == 1:
                            scene pgn_club_gh_girl1_anim_27_01
                        m emo-12 "Аррргххх!!!"
                        scene pgn_club_gh_girl1_25
                other emo-998 "Малыш. Ты супер!"
                if stat_max.tubs1 > 0 or "макс_новыетаблетки" in ivent24 or pgn_ach_repeat == 171:
                    menu:
                        "Повторим?":
                            if pgn_ach_repeat == 0:
                                $ qtime += 1
                            m emo-13 "Может быть ещё?"
                            if renpy.random.randint ( 1, 2) == 1:
                                other emo-998 "О! Готов повторить? Я согласна. Может поменяемся?"
                            else:
                                other emo-998 "О! Готов повторить? Я согласна. Поменяемся ролями?"
                            menu:
                                "В смысле?" if pgn_ach_repeat == 0:
                                    m emo-8 "Т.е. поменяемся?"
                                    other emo-998 "Не в смысле, что я тебя, у меня другие предпочтения. Тебе просто нужно будет стоять и получать удовольствие и я сама буду насаживаться на твоего большого монстра."
                                    other emo-998 "Ну так что, согласен?"
                                    menu:
                                        "Да":
                                            jump pgn_club_gh_cabl_girl1_anal_p1
                                        "Нет":
                                            jump pgn_club_gh_cabl_girl1_anal_p2
                                "Конечно":
                                    label pgn_club_gh_cabl_girl1_anal_p1:
                                        m emo-0 "Ок."
                                        other emo-998 "Хорошо. Переходи на другую сторону, вставляй своего монстра в дырку и жди меня."
                                        scene pgn_club_gh_max_05
                                        m emo-0 "Вставил и жду..."
                                        if "макс_новыетаблетки" in ivent24:
                                            m emo-5 "Чёрт! Мои яйца, сейчас взорвутся."
                                        scene pgn_club_gh_max_06
                                        other emo-998 "Я здесь, малыш."
                                        scene pgn_club_gh_girl1_43
                                        $ PGN_Achadd(pgnach_171, 171)
                                        other emo-998 "Держись крепче."
                                        label pgn_club_gh_cabl_girl1_44:
                                            if scene_random == 0:
                                                scene animated pgn_club_gh_girl1_44
                                                show screen scene_pgn_club_gh_cabl_girl1(44)
                                            if scene_random == 1:
                                                scene animated pgn_club_gh_girl1_45
                                                show screen scene_pgn_club_gh_cabl_girl1(44)
                                        $ renpy.pause()
                                        hide screen scene_pgn_club_gh_cabl_girl1
                                        if stat_max.tubs1 > 0:
                                            $ label_random = renpy.random.randint ( 3, 4)
                                            if label_random == 4:
                                                scene pgn_club_gh_girl1_anim_44_15
                                                m emo-12 "Аррргххх!!!"
                                            else:
                                                scene pgn_club_gh_girl1_anim_45_15
                                                m emo-12 "Аррргххх!!!"
                                                scene pgn_club_gh_girl1_46
                                                $ renpy.pause()
                                        elif "макс_новыетаблетки" in ivent24:
                                            scene pgn_club_gh_girl1_47
                                            m emo-12 "Аррргххх!!!"
                                            scene pgn_club_gh_girl1_48
                                            $ renpy.pause()
                                        if pgn_ach_repeat != 0:
                                            jump table_pgn_achievement
                                "Продолжить" if pgn_ach_repeat == 0:
                                    label pgn_club_gh_cabl_girl1_anal_p2:
                                        m emo-4 "Просто перевернись и я продолжу трахать."
                                        scene pgn_club_gh_girl1_28
                                        other emo-998 "Мммм... Аааххх..."
                                        label pgn_club_gh_cabl_girl1_29:
                                            if scene_random == 0:
                                                scene pgn_club_gh_girl1_29
                                                show screen scene_pgn_club_gh_cabl_girl1(29)
                                            if scene_random == 1:
                                                scene animated pgn_club_gh_girl1_31
                                                show screen scene_pgn_club_gh_cabl_girl1(29)
                                        other emo-998 "Ахх... Ах... Ммм... Аааххх..."
                                        label pgn_club_gh_cabl_girl1_30:
                                            if scene_random == 0:
                                                scene pgn_club_gh_girl1_30
                                                show screen scene_pgn_club_gh_cabl_girl1(30)
                                            if scene_random == 1:
                                                scene animated pgn_club_gh_girl1_31
                                                show screen scene_pgn_club_gh_cabl_girl1(30)
                                        $ renpy.pause()
                                        hide screen scene_pgn_club_gh_cabl_girl1
                                        $ label_random = renpy.random.randint ( 1, 3)
                                        if stat_max.tubs1 > 0 and label_random == 2:
                                            scene pgn_club_gh_girl1_32
                                            m emo-12 "Аррргххх!!!"
                                            scene pgn_club_gh_girl1_33
                                            $ renpy.pause()
                                        elif stat_max.tubs1 > 0 and label_random != 2:
                                            other emo-998 "Ааахх! Ахх..! Кончай! Кончай!"
                                            m emo-2 "{i}Блин! Я с радостью, но кажется снова эта таблетка меня подводит.{/i}"
                                            label pgn_club_gh_cabl_girl1_30a:
                                                if scene_random == 0:
                                                    scene pgn_club_gh_girl1_30
                                                    show screen scene_pgn_club_gh_cabl_girl1("30a")
                                                if scene_random == 1:
                                                    scene animated pgn_club_gh_girl1_31
                                                    show screen scene_pgn_club_gh_cabl_girl1("30a")
                                            other emo-998 "Кончи уже в мою попку! Я больше не продержусь..."
                                            hide screen scene_pgn_club_gh_cabl_girl1
                                            scene pgn_club_gh_girl1_34
                                            $ renpy.pause()
                                            scene pgn_club_gh_girl1_35
                                            other emo-998 "Аххх!"
                                            scene pgn_club_gh_girl1_36
                                            other emo-998 "Вау! Это было что-то с чем-то. Спасибо. Отлично меня оттрахал."
                                            m emo-2 "Но я ещё не кончил."
                                            other emo-998 "Ой! Да, точно, извини, но моя попка больше не сможет принять твой член."
                                            menu pgn_club_gh_cabl_girl1_m3:
                                                "Вагинал":
                                                    m emo-4 "Киску я ещё не трахнул."
                                                    other emo-998 "Даже не смей приближаться к моей киске, она не для тебя."
                                                    jump pgn_club_gh_cabl_girl1_m3
                                                "Рот":
                                                    m emo-6 "А может ртом?"
                                                    other emo-998 "Я устала и больше нет сил."
                                                    m emo-3 "Ну так я могу сам трахнуть рот."
                                                    $ label_random = renpy.random.randint ( 1, 3)
                                                    if label_random != 2:
                                                        other emo-998 "Хорошо, помогу кончить орально."
                                                        scene pgn_club_gh_girl1_37
                                                        $ renpy.pause()
                                                        scene pgn_club_gh_girl1_38
                                                        $ renpy.pause()
                                                        scene pgn_club_gh_girl1_39
                                                        m emo-12 "Аррргххх!!!"
                                                        scene pgn_club_gh_girl1_40
                                                        $ renpy.pause()
                                                    else:
                                                        other emo-998 "Извини, но не в этот раз."
                                                        m emo-2 "Блин"
                                                        $ ivent24.append("club_gh_макснекончил")
                                                "Позвать Катю":
                                                    m emo-6 "{i}Может быть позвать Катю?{/i}"
                                                    if (qtime >= 21 and qtime <= 23 and (daysn == 1 or daysn == 3 or daysn == 6 or daysn == 5)) or (qtime >= 0 and qtime <= 3 and (daysn == 2 or daysn == 4 or daysn == 7 or daysn == 6)):
                                                        m emo-13 "{i}Не получится. Сегодня она не работает.{/i}"
                                                        jump pgn_club_gh_cabl_girl1_m3
                                                    else:
                                                        jump pgn_cluv_gh_cabr_katehelp
                                                "уйти" if pgn_ach_repeat == 0:
                                                    $ ivent24.append("club_gh_макснекончил")
                                        elif "макс_новыетаблетки" in ivent24:
                                            hide screen scene_pgn_club_gh_cabl_girl1
                                            scene pgn_club_gh_girl1_41
                                            other emo-998 "Ох, ох, ох, как много! Аааххх! Моя попка!"
                                            scene pgn_club_gh_girl1_42
                                            other emo-998 "Вау! Попка заполнена на 100."
                                            m emo-10 "{i}Ну и таблетка. Я кажется почти все свои запасы спермы истратил.{/i}"
                        "уйти" if pgn_ach_repeat == 0:
                            hide screen scene_pgn_club_gh_cabl_girl1
                else:
                    hide screen scene_pgn_club_gh_cabl_girl1
                    other emo-998 "Фух! Он у тебя огроменный. Заходи почаще, мой попке нужен только такой член, как у тебя."
                    m emo-3 "Постараюсь."

    $ qtime += 1
    $ ivent24.append("club_gh_sex_girl1")
    $ ivent24.append("club_gh_sex")
    $ ivent24.append("club_gh_максраздет")
    hide screen scene_pgn_club_gh_cabl_girl1
    jump loc_club_gh

screen scene_pgn_club_gh_cabl_girl1(c):
    imagebutton:
        align (1.0, 0.5)
        idle "nav_change_a"
        hover "nav_change_b"
        if scene_random == 0:
            action SetVariable("scene_random", 1), Jump("pgn_club_gh_cabl_girl1_"+str(c))
        if scene_random == 1:
            action SetVariable("scene_random", 0), Jump("pgn_club_gh_cabl_girl1_"+str(c))


label pgn_club_gh_cabl_girl2:
    $ scene_random = 0
    scene pgn_club_gh_girl2_01_vezdessushij
    menu pgn_club_gh_cabl_girl2_m1:
        "Какой секс?" if "club_gh_girl2_qestion1" not in ivent24 and pgn_ach_repeat == 0:
            m emo-3 "Куда мне можно вставить член?"
            other emo-998 "Мальчик, только вагинальный секс. Никакого анала."
            $ ivent24.append("club_gh_girl2_qestion1")
            jump pgn_club_gh_cabl_girl2_m1
        "Куни" if "club_gh_girl2_cuni" not in ivent24 and pgn_ach_repeat == 0:
            label pgn_club_gh_cabl_girl2_2:
                if scene_random == 0:
                    scene pgn_club_gh_girl2_02
                    show screen scene_pgn_club_gh_cabl_girl2(2)
                if scene_random == 1:
                    scene pgn_club_gh_girl2_02b
                    show screen scene_pgn_club_gh_cabl_girl2(2)
            other emo-998 "Ой! Как-то неожиданно."
            label pgn_club_gh_cabl_girl2_3:
                if scene_random == 0:
                    scene pgn_club_gh_girl2_03
                    show screen scene_pgn_club_gh_cabl_girl2(3)
                if scene_random == 1:
                    scene pgn_club_gh_girl2_03b
                    show screen scene_pgn_club_gh_cabl_girl2(3)
            $ renpy.pause()
            label pgn_club_gh_cabl_girl2_4:
                if scene_random == 0:
                    scene pgn_club_gh_girl2_04
                    show screen scene_pgn_club_gh_cabl_girl2(4)
                if scene_random == 1:
                    scene pgn_club_gh_girl2_04b
                    show screen scene_pgn_club_gh_cabl_girl2(4)
            other emo-998 "Ох! Мальчик. Твой язычок волшебный."
            hide screen scene_pgn_club_gh_cabl_girl2
            $ ivent24.append("club_gh_girl2_cuni")
            jump pgn_club_gh_cabl_girl2_m1
        "Подрочить" if pgn_ach_repeat == 0:
            label pgn_club_gh_cabl_girl2_5:
                if scene_random == 0:
                    scene pgn_club_gh_girl2_05
                    show screen scene_pgn_club_gh_cabl_girl2(5)
                if scene_random == 1:
                    scene pgn_club_gh_girl2_05b
                    show screen scene_pgn_club_gh_cabl_girl2(5)
            m emo-3 "{i}Ну что ж, дрочим!{/i}"
            label pgn_club_gh_cabl_girl2_6:
                if scene_random == 0:
                    scene pgn_club_gh_girl2_06
                    show screen scene_pgn_club_gh_cabl_girl2(6)
                if scene_random == 1:
                    scene pgn_club_gh_girl2_06b
                    show screen scene_pgn_club_gh_cabl_girl2(6)
            other emo-998 "Ты что там делаешь? Мастурбируешь?"
            label pgn_club_gh_cabl_girl2_7:
                if scene_random == 0:
                    scene pgn_club_gh_girl2_07
                    show screen scene_pgn_club_gh_cabl_girl2(7)
                if scene_random == 1:
                    scene pgn_club_gh_girl2_07b
                    show screen scene_pgn_club_gh_cabl_girl2(7)
            other emo-998 "Может я помогу тебе ножками? Или сделаешь и мне приятное, потрёшься своим горячим членом о мой клитор?"
            hide screen scene_pgn_club_gh_cabl_girl2
            menu pgn_club_gh_cabl_girl2_m2:
                "Ноги":
                    label pgn_club_gh_cabl_girl2_8:
                        if scene_random == 0:
                            scene pgn_club_gh_girl2_08
                            show screen scene_pgn_club_gh_cabl_girl2(8)
                        if scene_random == 1:
                            scene pgn_club_gh_girl2_08b
                            show screen scene_pgn_club_gh_cabl_girl2(8)
                    $ renpy.pause()
                    label pgn_club_gh_cabl_girl2_9:
                        if scene_random == 0:
                            scene pgn_club_gh_girl2_09
                            show screen scene_pgn_club_gh_cabl_girl2(9)
                        if scene_random == 1:
                            scene pgn_club_gh_girl2_09b
                            show screen scene_pgn_club_gh_cabl_girl2(9)
                    $ renpy.pause()
                    m emo-12 "Аррргххх!!!"
                    label pgn_club_gh_cabl_girl2_10:
                        if scene_random == 0:
                            scene pgn_club_gh_girl2_10
                            show screen scene_pgn_club_gh_cabl_girl2(10)
                        if scene_random == 1:
                            scene pgn_club_gh_girl2_10b
                            show screen scene_pgn_club_gh_cabl_girl2(10)
                    $ renpy.pause()
                    hide screen scene_pgn_club_gh_cabl_girl2
                "Об киску":
                    label pgn_club_gh_cabl_girl2_11:
                        if scene_random == 0:
                            scene pgn_club_gh_girl2_11
                            show screen scene_pgn_club_gh_cabl_girl2(11)
                        if scene_random == 1:
                            scene animated pgn_club_gh_girl2_11b
                            show screen scene_pgn_club_gh_cabl_girl2(11)
                    other emo-998 "Ммм... Аах... Ммм..."
                    hide screen scene_pgn_club_gh_cabl_girl2
                    scene pgn_club_gh_girl2_12
                    m emo-12 "Аргххх!!!"
                    scene pgn_club_gh_girl2_13
                    $ renpy.pause()
                "Вагинал":
                    jump pgn_club_gh_cabl_girl2_vaginal
                "Анал":
                    m emo-3 "Может быть анал?"
                    other emo-998 "Нет. Нечего мою попку рвать по швам."
                    jump pgn_club_gh_cabl_girl2_m2
                "Продолжить дрочить":
                    label pgn_club_gh_cabl_girl2_6b:
                        if scene_random == 0:
                            scene pgn_club_gh_girl2_06
                            show screen scene_pgn_club_gh_cabl_girl2("6b")
                        if scene_random == 1:
                            scene pgn_club_gh_girl2_06b
                            show screen scene_pgn_club_gh_cabl_girl2("6b")
                    m emo-10 "{i}Ох, я уже почти...{/i}"
                    m emo-12 "Аррргххх!!!"
                    label pgn_club_gh_cabl_girl2_14:
                        if scene_random == 0:
                            scene pgn_club_gh_girl2_14
                            show screen scene_pgn_club_gh_cabl_girl2(14)
                        if scene_random == 1:
                            scene pgn_club_gh_girl2_14b
                            show screen scene_pgn_club_gh_cabl_girl2(14)
                    other emo-998 "Ну вот уже. Жаль."
                    hide screen scene_pgn_club_gh_cabl_girl2
        "Вагинал":
            label pgn_club_gh_cabl_girl2_vaginal:
                label pgn_club_gh_cabl_girl2_15:
                    if scene_random == 0:
                        scene pgn_club_gh_girl2_15
                        show screen scene_pgn_club_gh_cabl_girl2(15)
                    if scene_random == 1:
                        scene animated pgn_club_gh_girl2_15b
                        show screen scene_pgn_club_gh_cabl_girl2(15)
                other emo-998 "Аааххх... аааххх... Аааххх..."
                label pgn_club_gh_cabl_girl2_16:
                    if scene_random == 0:
                        scene pgn_club_gh_girl2_16
                        show screen scene_pgn_club_gh_cabl_girl2(16)
                    if scene_random == 1:
                        scene animated pgn_club_gh_girl2_16b
                        show screen scene_pgn_club_gh_cabl_girl2(16)
                $ renpy.pause()
                scene pgn_club_gh_girl2_17
                hide screen scene_pgn_club_gh_cabl_girl2
                other emo-998 "Глубже... Давай глубже!!!"
                label pgn_club_gh_cabl_girl2_18:
                    if scene_random == 0:
                        scene pgn_club_gh_girl2_18
                        show screen scene_pgn_club_gh_cabl_girl2(18)
                    if scene_random == 1:
                        scene pgn_club_gh_girl2_18b
                        show screen scene_pgn_club_gh_cabl_girl2(18)
                other emo-998 "Аааххх... аааххх... Аааххх..."
                hide screen scene_pgn_club_gh_cabl_girl2
                if ("club_gh_cabl_girl2_vag2") in ivent24 and pgn_ach_repeat == 0:
                    jump pgn_club_gh_cabl_girl2_vaginal2
                if stat_max.tubs1 == 0 and "макс_новыетаблетки" not in ivent24 and pgn_ach_repeat == 0:
                    label pgn_club_gh_cabl_girl2_vaginal_end:
                        menu:
                            "Кончить внутрь":
                                scene pgn_club_gh_girl2_19
                                m emo-12 "Аррргххх!!!"
                                scene pgn_club_gh_girl2_20
                                $ renpy.pause()
                            "Кончить на неё":
                                label pgn_club_gh_cabl_girl2_21:
                                    if scene_random == 0:
                                        scene pgn_club_gh_girl2_21
                                        show screen scene_pgn_club_gh_cabl_girl2(21)
                                    if scene_random == 1:
                                        scene pgn_club_gh_girl2_06b
                                        show screen scene_pgn_club_gh_cabl_girl2(21)
                                m emo-12 "Аррргххх!!!"
                                label pgn_club_gh_cabl_girl2_22:
                                    if scene_random == 0:
                                        scene pgn_club_gh_girl2_22
                                        show screen scene_pgn_club_gh_cabl_girl2(22)
                                    if scene_random == 1:
                                        scene pgn_club_gh_girl2_07b
                                        show screen scene_pgn_club_gh_cabl_girl2(22)
                                other emo-998 "Спасибо."
                                hide screen scene_pgn_club_gh_cabl_girl2
                else:
                    scene pgn_club_gh_girl2_23
                    other emo-998 "Аххх!!!"
                    scene pgn_club_gh_girl2_24
                    other emo-998 "Подожди, дай мне минутку, отдышаться."
                    other emo-998 "Продолжим или может трахнешь меня в рот?"
                    menu pgn_club_gh_cabl_girl2_m4:
                        "В анал" if pgn_ach_repeat == 0:
                            m emo-13 "Может всё же анал?"
                            other emo-998 "Моя попка не готова для секса."
                            m emo-13 "У меня есть презервативы."
                            other emo-998 "Нет"
                            jump pgn_club_gh_cabl_girl2_m4
                        "Продолжить здесь" if pgn_ach_repeat == 0:
                            $ qtime += 1
                            m emo-0 "И так нормально."
                            other emo-998 "Хорошо. Но только в последний раз, ещё, я не выдержу."
                            $ ivent24.append("club_gh_cabl_girl2_vag2")
                            jump pgn_club_gh_cabl_girl2_vaginal
                            label pgn_club_gh_cabl_girl2_vaginal2:
                                $ label_random = renpy.random.randint ( 2, 4)
                                if label_random == 2:
                                    m emo-8 "Блин! Не получается."
                                    other emo-998 "У тебя явные проблемы со здоровьем. Тебе обязательно нужно к врачу. Нельзя же так относиться к своему здоровью."
                                    menu:
                                        "Позвать Катю":
                                            m emo-6 "{i}Может быть позвать Катю?{/i}"
                                            if (qtime >= 21 and qtime <= 23 and (daysn == 1 or daysn == 3 or daysn == 6 or daysn == 5)) or (qtime >= 0 and qtime <= 3 and (daysn == 2 or daysn == 4 or daysn == 7 or daysn == 6)):
                                                m emo-13 "{i}Не получится. Сегодня она не работает.{/i}"
                                                $ ivent24.append("club_gh_макснекончил")
                                            else:
                                                jump pgn_cluv_gh_cabr_katehelp
                                        "уйти":
                                            $ ivent24.append("club_gh_макснекончил")
                                else:
                                    jump pgn_club_gh_cabl_girl2_vaginal_end
                        "Продолжить в другой кабинке":
                            if pgn_ach_repeat == 0:
                                $ qtime += 1
                            m emo-3 "Продолжим в другой кабинке, что напротив?"
                            other emo-998 "Хорошо. Но тебе же не будет меня видно."
                            m emo-2 "Я тут еле дотягиваюсь и неудобно."
                            other emo-998 "А, ну ладно."
                            scene pgn_club_gh_girl2_25
                            other emo-998 "Ох! Ты меня завёл. Я вся теку и этот жар."
                            scene pgn_club_gh_girl2_26
                            other emo-998 "Чувствуешь мой жар?"
                            other emo-998 "Киска жаждет члена и хорошенького траха. Можешь трахать жёстко, я не против."
                            label pgn_club_gh_sex_girl2_vagrepeat:
                                label pgn_club_gh_cabl_girl2_27:
                                    if scene_random == 0:
                                        scene animated pgn_club_gh_girl2_27a
                                        show screen scene_pgn_club_gh_cabl_girl2(27)
                                    if scene_random == 1:
                                        scene animated pgn_club_gh_girl2_27b
                                        show screen scene_pgn_club_gh_cabl_girl2(27)
                                $ renpy.pause()
                                hide screen scene_pgn_club_gh_cabl_girl2
                                $ label_random = renpy.random.randint ( 10, 13)
                                if (label_random != 12 and "club_gh_sex_girl2_vagrepeat" not in ivent24) or pgn_ach_repeat == 172:
                                    scene pgn_club_gh_girl2_28
                                    other emo-998 "Аааххх... Ааххх..."
                                    scene pgn_club_gh_girl2_29
                                    $ PGN_Achadd(pgnach_172, 172)
                                    $ renpy.pause()
                                    scene pgn_club_gh_girl2_30
                                    m emo-13 "Может быть ещё?"
                                    other emo-998 "Нет, нет, всё. Если ещё раз, то я из клуба выйти не смогу и так еле-еле держусь на ногах."
                                    scene pgn_club_gh_girl2_31
                                    menu:
                                        "Анал" if pgn_ach_repeat == 0:
                                            other emo-998 "Нет. Я уже говорила, я не готова к анальному сексу."
                                            menu:
                                                "Я не кончил":
                                                    m emo-8 "Но я ещё не кончил даже, а кто-то уже два раза."
                                                    other emo-998 "Значит кто то очень хорош в сексе, раз смог довести женщину до нескольких бурных оргазмов. Но я правда, больше не могу."
                                                    menu pgn_club_gh_cabl_girl2_m3:
                                                        "Орал":
                                                            jump pgn_club_gh_cabl_girl2_oral_next
                                                        "Позвать Катю":
                                                            m emo-6 "{i}Может быть позвать Катю?{/i}"
                                                            if (qtime >= 21 and qtime <= 23 and (daysn == 1 or daysn == 3 or daysn == 6 or daysn == 5)) or (qtime >= 0 and qtime <= 3 and (daysn == 2 or daysn == 4 or daysn == 7 or daysn == 6)):
                                                                m emo-13 "{i}Не получится. Сегодня она не работает.{/i}"
                                                                $ ivent24.append("club_gh_макснекончил")
                                                            else:
                                                                jump pgn_cluv_gh_cabr_katehelp
                                                "У меня есть презервативы" if condom.have == True:
                                                    m emo-8 "У меня есть презервативы. Готовить попку необязательно. Просто подставь и я всё сделаю сам."
                                                    other emo-998 "Тебе не терпится кончить, но мой анал под запретом. Не хочу этого секса."
                                                    jump pgn_club_gh_cabl_girl2_m3
                                                "Я заплачу":
                                                    m emo-13 "Сколько? Могу заплатить."
                                                    other emo-998 "Я не такая и чего непонятного в том, что не хочу анального секса?"
                                                    $ ivent24.append("club_gh_макснекончил")
                                                "Тебе понравится":
                                                    m emo-13 "У меня есть опыт и большой. Тебе понравится."
                                                    other emo-998 "У меня тоже есть опыт и мне этот секс не нравится совсем."
                                                    jump pgn_club_gh_cabl_girl2_m3
                                        "Может ещё раз?" if "club_gh_sex_girl2_vagrepeat" not in ivent24:
                                            m emo-13 "Может всё же ещё раз? Я точно кончу раньше тебя."
                                            $ label_random = renpy.random.randint ( 5, 6)
                                            if label_random == 5 or pgn_ach_repeat == 172:
                                                $ ivent24.append("club_gh_sex_girl2_vagrepeat")
                                                other emo-998 "Хорошо. В последний раз."
                                                jump pgn_club_gh_sex_girl2_vagrepeat
                                            else:
                                                other emo-998 "Извини. Но больше не смогу."
                                                m emo-2 "Блин!"
                                                $ ivent24.append("club_gh_макснекончил")
                                        "Орал":
                                            m emo-13 "Может ртом поможешь кончить?"
                                            jump pgn_club_gh_cabl_girl2_oral_next
                                elif stat_max.tubs1 > 0:
                                    scene pgn_club_gh_girl2_32
                                    m emo-10 "Аррргххх!!!"
                                    scene pgn_club_gh_girl2_33
                                    other emo-998 "Молодец, ты смог это сделать. А то ещё чуть-чуть и снова бы кончила."
                                elif "макс_новыетаблетки" in ivent24:
                                    scene pgn_club_gh_girl2_34
                                    m emo-12 "Ааааа! Аааахх!"
                                    scene pgn_club_gh_girl2_35
                                    other emo-998 "Аааххх... Как много... Ааааахх... Мммм..."
                                    scene pgn_club_gh_girl2_36
                                    other emo-998 "Ты необычный мальчик. Мне нравится. Буду ждать следующего раза с тобой."
                                if pgn_ach_repeat != 0:
                                    jump table_pgn_achievement
                        "Орал" if pgn_ach_repeat == 0:
                            label pgn_club_gh_cabl_girl2_oral:
                                m emo-4 "Хочу трахнуть в рот."
                                other emo-998 "Хорошо. Жди меня с другой стороны."
                                label pgn_club_gh_cabl_girl2_oral_next:
                                    scene pgn_club_gh_girl2_37
                                    other emo-998 "Давай, мальчик трахни моё горло. Тебе обязательно нужно кончить."
                                    label pgn_club_gh_cabl_girl2_38:
                                        if scene_random == 0:
                                            scene animated pgn_club_gh_girl2_38a
                                            show screen scene_pgn_club_gh_cabl_girl2(38)
                                        if scene_random == 1:
                                            scene animated pgn_club_gh_girl2_38b
                                            show screen scene_pgn_club_gh_cabl_girl2(38)
                                    $ renpy.pause()
                                    hide screen scene_pgn_club_gh_cabl_girl2
                                    scene pgn_club_gh_girl2_39
                                    m emo-12 "Аррргххх!!!"
                                    if stat_max.tubs1 > 0:
                                        scene pgn_club_gh_girl2_40
                                        $ renpy.pause()
                                    elif "макс_новыетаблетки" in ivent24:
                                        scene pgn_club_gh_girl2_41
                                        other emo-998 "Давай ещё. Я чувствую, что ещё не всё вышло из тебя. Ну же, кончай!"
                                        scene pgn_club_gh_girl2_42
                                        m emo-10 "Ааааа!!! Аааааххх!!!"
                                        scene pgn_club_gh_girl2_43
                                        other emo-999 "Я же говорила... Ммм... Хороший мальчик."
                                    if pgn_ach_repeat != 0:
                                        jump table_pgn_achievement
        "Анал" if pgn_ach_repeat == 0:
            m emo-3 "Может быть анал?"
            other emo-998 "Нет. Нечего мою попку рвать по швам."
            jump pgn_club_gh_cabl_girl2_m1

    $ qtime += 1
    $ ivent24.append("club_gh_sex_girl2")
    $ ivent24.append("club_gh_sex")
    $ ivent24.append("club_gh_максраздет")
    hide screen scene_pgn_club_gh_cabl_girl2
    jump loc_club_gh


screen scene_pgn_club_gh_cabl_girl2(c):
    imagebutton:
        align (1.0, 0.5)
        idle "nav_change_a"
        hover "nav_change_b"
        if scene_random == 0:
            action SetVariable("scene_random", 1), Jump("pgn_club_gh_cabl_girl2_"+str(c))
        if scene_random == 1:
            action SetVariable("scene_random", 0), Jump("pgn_club_gh_cabl_girl2_"+str(c))


label pgn_cluv_gh_cabr_katehelp:
    $ ivent24.append("club_gh_katehelp")
    scene pgn_club_gh_kate_01
    if ("club_gh_firstkatehelp") not in accessiv:
        ka emo-150 "[pname_max[0]], что за срочность? У меня работа..."
    else:
        ka emo-155 " Что у тебя снова произошло?"
    scene pgn_club_gh_kate_02
    if ("club_gh_firstkatehelp") not in accessiv:
        ka emo-154 "Твой член! Он покраснел."
    m emo-2 "Помоги мне кончить. Пожалуйста."
    if (("club_gh_firstkatehelp") not in accessiv and pgn_ach_repeat == 0) or pgn_ach_repeat == 173:
        scene pgn_club_gh_kate_03
        ka emo-155 "Ты принимал какие-нибудь таблетки?"
        m emo-13 "Да."
        ka emo-157 "Засунь член в любую свободную дырку и жди меня."
        m emo-2 "Может здесь мне поможешь?"
        ka emo-155 "Здесь нельзя, по правилам клуба."
        m emo-13 "{i}Правила?! А они есть?{/i}"
    elif renpy.random.randint ( 1, 4) == 2 or kateorder > 0:
        scene pgn_club_gh_kate_02
        ka emo-150 "У меня есть идея получше."
        m emo-13 "Какая?"
        scene black with dissolve
        $ renpy.pause(3, hard=True)
        jump pgn_clinic_max_afterclub
    scene pgn_club_gh_kate_04
    m emo-9 "Ай, ай, ай!"
    if ("club_gh_firstkatehelp") not in accessiv:
        ka emo-156 "Тебе больно?"
        m emo-2 "Немного. Хочу трахаться и поскорее уже кончить."
        ka emo-156 "[pname_max[0]]. Может лучше я отвезу тебя в клинику?"
        m emo-5 "Пожалуйста, помоги мне кончить... Секс, секс, секс..."
        ka emo-157 "Сексом не получится заниматься, тебе будет больно."
        m emo-2 "Ладно. Тогда на всё согласен, только помоги, пожалуйста."
    scene pgn_club_gh_kate_05
    $ renpy.pause()
    scene pgn_club_gh_kate_06
    m emo-7 "Ох! Так лучше... Приятно..."
    scene pgn_club_gh_kate_07
    m emo-10 "Ооох! Ооо..."
    scene pgn_club_gh_kate_08
    $ renpy.pause()
    scene pgn_club_gh_kate_12
    m emo-2 "Катя, пожалуйста, не останавливайся, продолжай."
    scene pgn_club_gh_kate_09
    m emo-2 "Ай!"
    scene pgn_club_gh_kate_10
    $ renpy.pause()
    scene pgn_club_gh_kate_11
    $ PGN_Achadd(pgnach_173, 173)
    m emo-10 "Катя, я чувствую, что вот скоро..."
    scene pgn_club_gh_kate_12
    ka emo-156 "Тогда может... секс... горлом?"
    m emo-4 "С радостью."
    scene animated pgn_club_gh_kate_13a
    $ renpy.pause()
    menu:
        "Кончить":
            scene pgn_club_gh_kate_14
            m emo-12 "Аррргххх!!! Аааааааа!!!"
            scene pgn_club_gh_kate_15
            m emo-10 "Спасибо, спасибо, спасибо..."
            ka emo-153 "Я не против тебе помогать, с твоей проблемой, но [pname_max[0]] будь осторожен в следующий раз с этими таблетками."
    if pgn_ach_repeat != 0:
        jump table_pgn_achievement
    if ("club_gh_firstkatehelp") not in accessiv:
        $ accessiv.append("club_gh_firstkatehelp")
    $ ivent24.append("club_gh_sex")
    $ ivent24.append("club_gh_максраздет")
    $ qtime += 1
    $ PGN_Addstatsex(stat_kate, 0, 0, 1, 0, 0)
    jump loc_club_gh



label pgn_cluv_gh_cabr_sveta:
    if "club_gh_svetabigtits" not in accessiv:
        $ accessiv.append("club_gh_svetabigtits")
        scene pgn_club_gh_sveta_01
        m emo-6 "{i}Хм... кто это?{/i}"
        scene pgn_club_gh_sveta_02
        m emo-1 "{i}Знакомые волосы.{/i}"
        scene pgn_club_gh_sveta_03
        m emo-9 "{i}Так это же та с клиники, с новыми большими сиськами.{/i}"
        sv emo-421 "Приветик. Я этот член запомнила. Ты же тот, с Клиники, да?"
        menu:
            "Как тебе твои новые сиськи?":
                m emo-3 "Привет. Как дела? Как тебе твои новые сиськи?"
                sv emo-424 "Привлекают столько внимания, сколько хотела. Все похотливые глаза только на мне. Но..."
                m emo-6 "Но..."
                scene pgn_club_gh_sveta_04
                sv emo-424 "Твой..."
                m emo-6 "Что мой?"
            "Помолчать":
                sv emo-421 "Молчишь? Ни чего, зато твой член не скрывает, что рад меня увидеть."
                sv emo-424 "Соскучился по этим губкам?"
        jump pgn_cluv_gh_cabr_sveta_bj
    else:

        scene pgn_club_gh_sveta_01
        m emo-4 "{i}Знакомые шортики{/i}\nПривет!"
        sv emo-424 "Привет, озабоченный мальчишка. Как хочешь кончить в этот раз? Отсосать или подрочить моими большими буферами?"
    menu:
        "Минет":
            label pgn_cluv_gh_cabr_sveta_bj:
                scene pgn_club_gh_sveta_05
                sv emo-424 "Ммм..."
                scene pgn_club_gh_sveta_06
                sv emo-424 "Большой... Горячий..."
                scene animated pgn_club_gh_sveta_08a
                $ renpy.pause()
                scene animated pgn_club_gh_sveta_08b
                $ renpy.pause()
                scene animated pgn_club_gh_sveta_07
                menu:
                    "В рот":
                        scene pgn_club_gh_sveta_09
                        m emo-12 "Аррргххх!!!"
                        scene pgn_club_gh_sveta_10
                        sv emo-424 "Ммм.... Вкусно. Приходи ещё."
                    "На лицо":
                        scene pgn_club_gh_sveta_11
                        m emo-12 "Аррргххх!!!"
                        scene pgn_club_gh_sveta_12
                        sv emo-421 "Мммм... Класс! До следующего раза, парнишка."
        "Сиськи":
            scene pgn_club_gh_sveta_13
            sv emo-421 "Хочешь увидеть мои дыни?"
            scene pgn_club_gh_sveta_14
            m emo-3 "Да"
            scene pgn_club_gh_sveta_15
            $ renpy.pause()
            scene pgn_club_gh_sveta_16
            $ renpy.pause()
            scene pgn_club_gh_sveta_17
            sv emo-421 "Готов малыш?"
            scene animated pgn_club_gh_sveta_18a
            $ renpy.pause()
            scene animated pgn_club_gh_sveta_18b
            $ renpy.pause()
            menu:
                "В рот":
                    scene pgn_club_gh_sveta_09
                    $ renpy.pause()
                    scene pgn_club_gh_sveta_10
                    $ renpy.pause()
                "На лицо":
                    scene pgn_club_gh_sveta_11
                    $ renpy.pause()
                    scene pgn_club_gh_sveta_12
                    $ renpy.pause()
                "На сиськи":
                    scene pgn_club_gh_sveta_19
                    m emo-12 "Аррргххх!!!"
                    scene pgn_club_gh_sveta_20
                    sv emo-422 "Ооох!"
                    scene pgn_club_gh_sveta_21
                    $ renpy.pause()
    $ qtime += 1
    $ ivent24.append("club_gh_sex")
    $ ivent24.append("club_gh_svetabigtits")
    $ ivent24.append("club_gh_максраздет")
    jump loc_club_gh
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
