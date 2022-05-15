







label pgn_veranda_punishment_liza:

    $ liza_homework_error = False
    if veranda_punishment_liza_no == True:
        $ veranda_punishment_liza_no = False
    if ("homework_liza_наказание_макса") in accessiv:
        $ accessiv.remove("homework_liza_наказание_макса")
    $ ivent24.append("veranda_punishment")

    scene bg veranda_punishment_01
    l emo-46 "Я не виновата."
    mom emo-64 "А кто тогда виноват?"
    l emo-49 "[pname_max[0]]. Он меня отвлекал и не давал сосредоточится."
    mom emo-63 "Вот оно что. [pname_max[0]], как это понимать, зачем ты мешаешь [pname_liza[2]]?"
    menu:
        "Признать вину":
            m emo-2 "Да, я виноват."
            l emo-48 "Мама, а можно тогда я его накажу?"
            mom emo-60 "Хорошо."
            scene pgn_home_punishment_liza_max_01
            l emo-41 "Братик, ложись ко мне на коленки."
            m emo-0 "А тяжело не будет?"
            l emo-43 "Ну же, давай быстрее, ложись."
            scene pgn_home_punishment_liza_max_02
            $ renpy.pause(2)
            scene pgn_home_punishment_liza_max_03
            $ renpy.pause(2)
            scene pgn_home_punishment_liza_max_04
            $ renpy.pause(2)
            scene pgn_home_punishment_liza_max_05
            mom emo-63 "[pname_max[0]], извинись перед ней."
            m emo-1 "Прости, меня."
            l emo-41 "Прощаю."
        "Возразить":
            m emo-1 "Она врёт. Я ей наоборот помогал и не понимаю, как она допустила ошибку."
            mom emo-63 "[pname_liza[0]], ответь мне честно."
            $ label_random = renpy.random.randint ( 1, 2)
            if label_random == 1:
                l emo-46 "Отвлекал постоянно, ничего он мне не помогал. Да и ещё это он мне дал неправильный ответ."
                mom emo-64 "Значит [pname_max[0]] сейчас от меня получит."
                $ label_random = renpy.random.randint ( 1, 3)
                if label_random == 3 and ("kira_aptsex") in ivent24:
                    jump pgn_veranda_punishment_kira_max
                else:
                    scene pgn_home_punishment_mom_max_01
                    $ renpy.pause(2)
                    scene pgn_home_punishment_mom_max_02
                    mom emo-73 "Эм..."
                    scene pgn_home_punishment_mom_max_03
                    $ renpy.pause(2)
                    scene pgn_home_punishment_mom_max_04
                    m emo-2 "Ай!"
                    scene pgn_home_punishment_mom_max_03
                    $ renpy.pause(2)
                    scene pgn_home_punishment_mom_max_04
                    m emo-2 "Ай!!!"
                    $ label_random = renpy.random.randint ( 1, 3)
                    if label_random == 1 or ("punishm_mom_maxcum") not in accessiv:
                        if ("punishm_mom_maxcum") not in accessiv:
                            $ accessiv.append("punishm_mom_maxcum")
                        mom emo-63 "Этого недостаточно, так что терпи."
                        scene animated pgn_home_punishment_mom_max_05
                        m emo-2 "Ай!!!"
                        m emo-2 "Больно! Мама!"
                        mom emo-63 "Так и должно быть."
                        $ renpy.pause(4)
                        m emo-8 "{i}Хм... Какого черта?! Ещё немного и ...{/i}"
                        scene pgn_home_punishment_mom_max_07
                        m emo-9 "{i}Я кончил. Что за?{/i}"
                        scene pgn_home_punishment_mom_max_08
                        mom emo-73 "А... "
                        m emo-8 "..."
                        mom emo-69 "Больше ничего такого не делай, за что я могла тебя наказать. Хорошо?"
                        m emo-2 "Да... Прости..."
                        mom emo-73 "Надевай шорты и присаживайся за стол... аккуратно."
                    elif label_random == 2:
                        scene animated pgn_home_punishment_mom_max_05
                        m emo-8 "{i}Снова? Опять кончу.{/i}"
                        scene pgn_home_punishment_mom_max_10
                        m emo-8 "{i}Ай! Мама сильно сжала мой член. Сейчас он лопнет от большого напора.{/i}"
                        scene pgn_home_punishment_mom_max_11
                        mom emo-60 "Больше не будешь так делать?"
                        m emo-8 "Да, т.е нет, не буду... {i}Больно! Больно!{/i}"
                        scene pgn_home_punishment_mom_max_12
                        m emo-10 "{i}Ааахх.... Как хорошо...{/i}"
                        scene pgn_home_punishment_mom_max_13
                        l emo-48 "Мама, всё или его ещё недостаточно наказала?"
                        scene pgn_home_punishment_mom_max_14
                        $ renpy.pause(2)
                        scene pgn_home_punishment_mom_max_15
                        $ renpy.pause(2)
                        scene pgn_home_punishment_mom_max_09
                        mom emo-73 "Всё. Надеюсь... этого больше не... повторится. Да, [pname_max[0]]?"
                        m emo-3 "Да... Мама."
                    elif label_random == 3:
                        scene pgn_home_punishment_mom_max_05
                        $ renpy.pause(3)
                        scene pgn_home_punishment_mom_max_09
                        mom emo-60 "Надеюсь, этого больше не повторится. А теперь, одевайся..."
                    jump veranda_punishment_choice
            if label_random == 2:
                $ label_random = renpy.random.randint ( 1, 2)
                if label_random == 1:
                    l emo-49 "Это не за домашку. [pname_max[0]] не причём. Просто не смогла ответить на вопрос, когда вызвали к доске."
                if label_random == 2:
                    l emo-49 "[pname_max[0]] помогал мне, может это я где-то ошиблась."
                mom emo-66 "Вот как. Тогда будет честно, если это сделает [pname_max[0]]."
                $ label_random = renpy.random.randint ( 1, 3)
                if label_random == 1 and ("kira_aptsex") in ivent24:
                    $ ivent24.append("veranda_punishment_kira_liza")
                    jump pgn_veranda_punishment_kira_liza
                menu:
                    "Попросить сделать это потом":
                        $ label_random = renpy.random.randint ( 1, 3)
                        if label_random == 3:
                            mom emo-63 "Нет, [pname_max[0]], сейчас!"
                            m emo-1 "Ладно, ладно."
                        else:

                            $ veranda_punishment_liza_no, liza_homework_error = True, True
                            mom emo-60 "Хорошо. Только не забудь об этом."
                            m emo-0 "Ок."
                            jump veranda_punishment_choice
                    "Отшлепать попку [pname_liza[1]]":
                        pass
                scene pgn_home_punishment_max_liza_01
                l emo-46 "[pname_max[0]], будь со мной нежен."
                mom emo-64 "Тебя нужно хорошенько наказать. Так что [pname_max[0]] будет шлепать по твоей попе, пока она не станет красной."
                scene pgn_home_punishment_max_liza_02
                m emo-3 "{i}Я ещё не начал, а киска [pname_liza[1]] уже влажная. Вот же притворяшка.{/i}"
                scene animated pgn_home_punishment_max_liza_03
                $ renpy.pause(6)
                if ("punishm_mom_lizahard") not in accessiv:
                    $ accessiv.append("punishm_mom_lizahard")
                    scene pgn_home_punishment_max_liza_05
                    mom emo-60 "Достаточно. Теперь моя очередь."
                    l emo-46 "Но... Мама..."
                    mom emo-64 "Что, Мама?! [pname_max[0]] наказал тебя за вранье, а я за плохую оценку."
                    k emo-100 "[pname_mom[6]]. Думаю с неё хватит. Если ещё и ты по попе ей надаёшь, бедненькая сидеть не сможет."
                    mom emo-60 "Зато запомнит об этом на долго."
                    scene pgn_home_punishment_mom_liza_hard_01
                    mom emo-60 "Ложись ко мне на колени."
                    scene pgn_home_punishment_mom_liza_hard_02
                    mom emo-73 "{i}Хм... Странно{/i}"
                    scene pgn_home_punishment_mom_liza_hard_03
                    mom emo-73 "{i}У моей дочери влажное влагалище. Неужели она тоже..{/i}"
                    scene pgn_home_punishment_mom_liza_hard_01
                    mom emo-60 "Ладно, на этот раз прощаю. Садись за стол."
                    l emo-46 "Спасибо."
                else:
                    scene pgn_home_punishment_max_liza_05
                    mom emo-60 "Спасибо, [pname_max[0]]. Надеюсь, [pname_liza[0]], ты усвоила."
                    l emo-46 "Да, мама."
    jump veranda_punishment_choice





label pgn_veranda_punishment_alice:
    if veranda_punishment_alice_no == True:
        $ veranda_punishment_alice_no = False
    $ alice_cigarettes = False
    $ alice_psh += 1
    $ ivent24.append("veranda_punishment")

    scene bg veranda_punishment_01
    mom emo-64 "[pname_alice[0]], я снова нашла сигареты в твоей комнате. Ты когда собираешься бросить купить?"
    a emo-29 "Мама, я без понятий от куда сигареты, я не курю, честно."
    a emo-28 "Это наверное [pname_max[0]] их мне подбросил."
    mom emo-64 "[pname_max[0]]? Ты что, значит куришь? От куда у тебя сигареты?"
    menu:
        "Запах сигарет":
            m emo-1 "Я не курю. Это [pname_alice[0]] курила. И ещё этот противный запах от них."
            if ("smokecig_alicehome") not in ivent24 and ("smokecig_home_true") not in ivent24:
                mom emo-60 "Сегодня я никого запаха не ощущала."
                a emo-21 "Наверное это были соседи?"
                m emo-13 "Может быть."
                a emo-20 "Видишь, Мам. Он даже не уверен и ещё меня обвиняет. Это всё он."
                mom emo-63 "[pname_max[0]]! Снимай шорты, сейчас [pname_alice[0]] тебя накажет за враньё."

            if ("smokecig_alicehome") not in ivent24 and ("smokecig_home_true") in ivent24:
                mom emo-60 "Запах, да помню. Но [pname_alice[1]] дома не было."
                a emo-20 "Вот видишь, Мама, он врёт, ничего не было, так что это не мои сигареты."
                mom emo-64 "[pname_max[0]], снимай шорты. [pname_alice[0]], накажи брата, может поменьше будет врать."

            if ("smokecig_alicehome") in ivent24 and ("smokecig_home_true") in ivent24:
                mom emo-60 "Запах был и [pname_alice[0]] тоже дома была."
                a emo-29 "Мама, это не я."
                mom emo-63 "Но пачка сигарет в твоей комнате нашла, а не у [pname_max[3]]. Давай, раздевайся."
                $ label_random = renpy.random.randint ( 1, 3)
                if label_random == 1 and ("kira_aptsex") in ivent24:
                    jump pgn_veranda_punishment_kira_alice
                else:
                    menu:
                        "Наказать потом":
                            mom emo-73 "Ну... хорошо, сынок. Только если пообещал, сделай это. Не перестарайся, но пусть она это запомнит..."
                            m emo-0 "Обязательно запомнит!"

                            $ veranda_punishment_alice_no = True
                            jump veranda_punishment_choice
                        "Наказать сейчас":
                            scene pgn_home_punishment_max_alice_01
                            m emo-3 "Сейчас я отшлепаю твою попочку. Ложись ко мне на коленки."
                            scene pgn_home_punishment_max_alice_02
                            $ renpy.pause(2)
                            scene pgn_home_punishment_max_alice_03
                            $ renpy.pause(2)
                            scene pgn_home_punishment_max_alice_04
                            $ renpy.pause(2)
                            scene pgn_home_punishment_max_alice_05
                            $ renpy.pause(2)
                            scene pgn_home_punishment_max_alice_06
                            m emo-4 "Вот и всё. Попка красная."
                            mom emo-60 "Молодец, [pname_max[0]]. А ты [pname_alice[0]], не смей больше курить в моём доме."
                            a emo-20 "Хорошо, Мам."
                            jump veranda_punishment_choice
                        "Пусть Мама это сделает":
                            jump veranda_punishment_alice_next
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random == 1 and ("kira_aptsex") in ivent24:
                jump pgn_veranda_punishment_kira_max
            label pgn_veranda_punishment_alice_max:
                scene pgn_home_punishment_alice_max_01
                a emo-25 "Подставляй попку. Я буду нежной."
                scene pgn_home_punishment_alice_max_02
                $ renpy.pause(2)
                scene pgn_home_punishment_alice_max_03
                $ renpy.pause(2)
                scene pgn_home_punishment_alice_max_04
                m emo-2 "{i}Ага, как же, нежной.{/i}"
                scene pgn_home_punishment_alice_max_05
                $ renpy.pause(3)
                scene pgn_home_punishment_alice_max_06
                if lizasex_alice == True or pgn_ach_repeat == 155:
                    a emo-24 "Мама, ты не против, если я его ещё раз накажу? Он кое-что ещё сделал."
                    scene pgn_home_punishment_alice_max_07
                    m emo-9 "Э... хватит."
                    mom emo-60 "Хорошо, если он этого заслуживает."
                    m emo-9 "Мама!"
                    scene animated pgn_home_punishment_alice_max_08
                    m emo-2 "Ай, ай, ай.... {i}Странные ощущения, мне дрочит и сильно шлепает по заднице. Одновременно хорошо и...{/i}"
                    m emo-13 "{i}Ох, блин, сейчас кончу..{/i}"
                    scene pgn_home_punishment_alice_max_09
                    m emo-11 "{i}Больно, больно, [pname_alice[0]], черт тебя подери!{/i}"
                    a emo-20 "[pname_liza[0]], подай шорты, а то [pname_max[0]] сам не справится."
                    scene pgn_home_punishment_alice_max_10
                    m emo-13 "Да не так уж... и.. больно... Сам смогу надеть.."
                    mom emo-60 "У вас там всё в порядке?"
                    a emo-20 "Да, мама."
                    scene pgn_home_punishment_alice_max_10
                    m emo-6 "{i}Что они задумали?{/i}"
                    scene pgn_home_punishment_alice_max_11
                    $ PGN_Achadd(pgnach_155, 155)
                    m emo-11 "{i}Какого?{/i}"
                    scene pgn_home_punishment_alice_max_12
                    m emo-10 "{i}Чёрт!!!{/i}"
                    scene pgn_home_punishment_alice_max_13
                    $ renpy.pause(2)
                    scene pgn_home_punishment_alice_max_14
                    a emo-26 "[pname_liza[0]], спасибо за помощь. [pname_max[0]], ты можешь садится за стол."
                    m emo-11 "{i}Чтоб их.{/i}"

                    if pgn_ach_repeat == 155:
                        jump table_pgn_achievement

                    $ ivent24.append("punishmax_shortscum")
                    $ lizasex_alice, alice_psh = False, alice_psh-1
            a emo-22 "Понравилось? Ещё хочешь?"
            m emo-13 "Нет, спасибо."
        "Я не курю":
            m emo-1 "Мама, я не курю, правда."
            a emo-29 "Ага. Купил их в каком-то магазине, а к мне подкинул, чтобы меня наказали."
            mom emo-60 "Только не пойму, зачем это [pname_max[2]] делать."
            mom emo-60 "Ладно. Не буду разбираться кто виноват. Оба свободны."
    jump veranda_punishment_choice

label pgn_veranda_punishment_kira_max:
    k emo-101 "Может я [pname_max[1]] потом накажу, а? Сейчас стынет такая вкусная еда, аж слюньки потекли. Как думаешь, [pname_mom[6]]?"
    mom emo-60 "Ох! Ладно. Только не забудь."
    k emo-103 "Договорились."
    k emo-109 "[pname_max[0]]..."
    jump veranda_punishment_choice

label pgn_veranda_punishment_kira_liza:
    k emo-101 "А можно мне это сделать?"
    if ("punishm_kira_lizalight") in accessiv:
        mom emo-60 "[pname_kira[0]], мне нужно их наказать, а не гладить по попке."
        k emo-103 "У [pname_liza[1]] нежная попочка, жалко по такому хорошенькому месту сильно шлепать. "
        if ("punishm_kira_alice") in accessiv:
            a emo-24 "А моя попка?"
            k emo-104 "А ты у нас уже взрослая девочка, к этому нужно привыкать и подготавливать попку к большим приключениям."
            mom emo-63 "[pname_kira[0]]!"
            k emo-101 "Извини. Ну так, мне можно?"
            mom emo-60 "Хорошо."
    else:
        mom emo-60 "Можно. Я не против."
    scene pgn_home_punishment_kira_liza_01
    k emo-101 "Ложись ко мне на коленки, малышка."
    scene pgn_home_punishment_kira_liza_02
    k emo-102 "Расслабься, всё будет хорошо."
    scene pgn_home_punishment_kira_liza_03
    k emo-101 "Ох! Какая нежная попочка."
    scene pgn_home_punishment_kira_liza_02
    $ renpy.pause(2)
    scene pgn_home_punishment_kira_liza_03
    $ renpy.pause(2)
    scene pgn_home_punishment_kira_liza_04
    k emo-101 "{i}Ммм. Киска моей любимой племянницы вся горит.{/i}"
    scene pgn_home_punishment_kira_liza_05
    k emo-101 "Вот и всё."

    $ liza_homework_error = False
    if ("punishm_kira_lizalight") not in accessiv:
        $ accessiv.append("punishm_kira_lizalight")
    jump veranda_punishment_choice

label pgn_veranda_punishment_kira_alice:
    k emo-101 "[pname_mom[6]], давай я это сделаю."
    mom emo-60 "Хорошо."
    scene pgn_home_punishment_kira_alice_01
    k emo-101 "Подойди ближе. Я не кусаюсь."
    scene pgn_home_punishment_kira_alice_02_01
    k emo-102 "Сильно больно не будет, тебе понравится."
    scene animated pgn_home_punishment_kira_alice_02
    $ renpy.pause()
    scene pgn_home_punishment_kira_alice_03
    m emo-4 "{i}Какие румяные булочки.{/i}"
    $ alice_cigarettes = False
    $ ivent24.append("veranda_punishment")
    if veranda_punishment_alice_no == True:
        $ veranda_punishment_alice_no = False
    if ("punishm_kira_alice") not in accessiv:
        $ accessiv.append("punishm_kira_alice")
    jump veranda_punishment_choice

label pgn_veranda_punishment_kira_mom:
    k emo-113 "[pname_alice[0]], позволь своей тёте наказать твою маму."
    a emo-21 "Не против."
    m emo-1 "{i}А у меня значит не стоит спрашивать.{/i}"
    scene pgn_home_punishment_kira_mom_01
    k emo-101 "Вставай в позу. Сейчас сестрёнка тебя накажет."
    scene pgn_home_punishment_kira_mom_02
    if ("punishm_kira_mom") not in accessiv:
        k emo-114 "Уж и не помню, когда последний лупила по этой заднице."
    $ renpy.pause(2)
    scene pgn_home_punishment_kira_mom_03
    mom emo-68 "Аххх!!!"
    if ("punishm_kira_mom") not in accessiv:
        scene pgn_home_punishment_kira_mom_04
        $ accessiv.append("punishm_kira_mom")
        k emo-104 "Так за что ты так провинилась?"
        mom emo-73 "Ну... Я знаю за что."
        k emo-109 "..."
    scene pgn_home_punishment_kira_mom_02
    $ renpy.pause(2)
    scene pgn_home_punishment_kira_mom_03
    mom emo-68 "Аххх... Ммм..."
    scene pgn_home_punishment_kira_mom_04
    mom emo-69 "[pname_kira[0]]... Шлепай... по... по..."
    k emo-101 "По сильнее? Ну хорошо."
    scene pgn_home_punishment_kira_mom_02
    $ renpy.pause(2)
    scene pgn_home_punishment_kira_mom_03
    mom emo-73 "...по попе..."
    scene animated pgn_home_punishment_kira_mom_05a
    $ renpy.pause()
    mom emo-68 "Аххх... Ммм... [pname_kira[0]]..."
    scene animated pgn_home_punishment_kira_mom_05с
    $ renpy.pause()
    scene animated pgn_home_punishment_kira_mom_05a
    $ renpy.pause()
    mom emo-73 "Аххх... Ммм... Ахх..."
    scene animated pgn_home_punishment_kira_mom_06
    mom emo-73 "[pname_kira[0]], [pname_kira[0]]... Аххх..."
    scene pgn_home_punishment_kira_mom_04
    k emo-101 "Может быть сегодня ещё продолжим. Да, [pname_mom[6]]?"
    mom emo-73 "Конечно."
    scene pgn_home_punishment_kira_mom_07
    k emo-101 "[pname_mom[6]], ты сожалеешь о своём поступке?"
    scene pgn_home_punishment_kira_mom_08
    $ PGN_Achadd(pgnach_156, 156)
    mom emo-69 "Я больше не буду так делать."
    scene pgn_home_punishment_kira_mom_09
    k emo-109 "Хорошая девочка. Одевайся и садись за стол."

    if pgn_ach_repeat == 156:
        jump table_pgn_achievement

    $ alice_cigarettes = False
    $ ivent24.append("veranda_punishment")
    jump veranda_punishment_choice

label pgn_alice_home_cigarettes_veranda:
    if "loc_veranda" in locchr_loc2:
        m emo-6 "{i}Уж точно не сейчас.{/i}"
    if "loc_veranda" not in locchr_loc2:
        if locchr_mom.loc2 == "loc_mom_room":
            m emo-6 "{i}Мама может учуять запах и тогда мне будет очень плохо.{/i}"
        if locchr_alice.loc2 == "loc_mom_room":
            m emo-0 "{i}[pname_alice[0]] в своей комнате, слишком опасно это делать{/i}"
        else:
            m emo-3 "Готово. Дым от сигарет по-всюду."
            $ ivent24.append("smokecig_home_true")
            if locchr_alice.loc1 == "loc_home":
                $ ivent24.append("smokecig_alicehome")
    jump loc_veranda
label pgn_alice_home_cigarettes_pool:
    if "loc_pool" in locchr_loc2 and locchr_liza.loc2 != "loc_pool":
        m emo-6 "{i}Уж точно не сейчас.{/i}"
    if "loc_pool" not in locchr_loc2 or locchr_liza.loc2 == "loc_pool":
        if qtime >= 6 and qtime <= 16:
            scene pgn_outpool_01
        if qtime >= 17 and qtime < 20:
            scene pgn_outpool_02
        m emo-3 "Готово. Надеюсь мама почувствует запах от сигарет [pname_alice[1]]."
        $ ivent24.append("smokecig_home_true")
        if locchr_alice.loc1 == "loc_home":
            $ ivent24.append("smokecig_alicehome")
    jump loc_pool

label pgn_veranda_punishment_liza_max:
    if ("veranda_punishment") not in ivent24:
        l emo-41 "Мама. Может перед ужином проведем наказание?"
    if ("veranda_punishment") in ivent24:
        l emo-41 "Мама. Может проведем ещё одно наказание?"
    mom emo-60 "Зачем? Кто-то плохо себя ввёл?"
    l emo-40 "Да, [pname_max[0]]."
    mom emo-64 "[pname_max[0]]. Что ты натворил в этот раз?"
    m emo-9 "Я?! Ничего."
    l emo-46 "Он ночью мастурбировал и не давал мне спать. Из-за этого я не выспалась."
    m emo-9 "Ничего подобного я не делал."
    mom emo-63 "Так, живо снял шорты."
    l emo-41 "А можно я это сделаю?"
    mom emo-60 "Конечно, доченька."
    scene pgn_home_punishment_liza_max_01
    l emo-41 "Давай, ложись."
    scene pgn_home_punishment_liza_max_02
    m emo-6 "{i}С чего это [pname_liza[0]] решила меня подставить?!{/i}"
    scene pgn_home_punishment_liza_max_03
    m emo-2 "Ай!"
    scene pgn_home_punishment_liza_max_02
    $ renpy.pause(2)
    scene pgn_home_punishment_liza_max_03
    $ renpy.pause(2)
    scene pgn_home_punishment_liza_max_02
    $ renpy.pause(2)
    scene pgn_home_punishment_liza_max_03
    $ renpy.pause(2)
    scene pgn_home_punishment_liza_max_04
    $ renpy.pause(2)
    scene pgn_home_punishment_liza_max_05
    mom emo-60 "Надеюсь, что ты, [pname_max[0]], больше не будешь так делать."
    m emo-2 "Понял... {i}Только не понял за что.{/i}"
    mom emo-60 "Тогда садитесь за стол."
    $ accessiv.remove("урокисекса_практика_лиза")
    jump veranda_dinner
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
