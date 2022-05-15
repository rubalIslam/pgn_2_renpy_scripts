






label pgn_events_13_momkate_01:
    scene f95_papersand_cici-show-1
    m emo-3 "Здравствуйте."
    scene f95_papersand_cici-show-3
    momk emo-320 "Здравствуй, [pname_max[0]]. Мне нужно с тобой серьезно поговорить."
    m emo-0 "Да, конечно. О чём?"
    scene f95_papersand_cici-show-2
    momk emo-320 "Этот разговор требует личной встречи. Так что будет лучше, если заглянешь ко мне в Клуб."
    menu:
        "Хорошо":
            m emo-0 "Хорошо. Я приеду."
        "Постараюсь не забыть":
            m emo-3 "Постараюсь не забыть и если найду время."
            momk emo-325 "Надеюсь, что увижу тебя совсем скоро, иначе..."
            scene pgn_maxcompsits_03
            m emo-6 "..."
            m emo-6 "{i}Звонок прервался. Что значит иначе?{/i}"
        "А если меня не впустят?":
            m emo-13 "А если меня охрана не впустит?"
            momk emo-321 "Я об этом позабочусь, не волнуйся."
            m emo-0 "Хорошо. Я приеду."
    $ momkate_path, qtime, days_momkate = 2, qtime+1, days+7
    jump jump_dialogue


label pgn_events_13_momkate_02:
    scene black
    if ("loc_club") not in location:
        ukn "\"{i}Звуки Машины{/i}\""
    m emo-9 "{i}Меня похитили? Во блин! Куда они меня ведут?{/i}"
    if ("loc_club") not in location:
        m emo-2 "{i}Куда-то приехали.{/i}"
    m emo-2 "{i}Мама, сестрёнки, простите меня за всё. Похоже я серьезно влип.{/i}"
    m emo-6 "{i}Так, меня усадили на что-то мягкое и кажется они ушли.{/i}"
    scene pgp_club_firstvisit_05
    momk emo-321 "Привет, [pname_max[0]]. С нашего последнего разговора прошло много времени и ты ко мне не заходил."
    m emo-13 "Извините, всё же я забыл. Забывчивый."
    jump pgn_events_13_momkate_03_next



label pgn_events_13_momkate_03:
    scene pgn_club_dancefloor_01
    m emo-1 "О! Так этот тот самый клуб, в который ходят [pname_alice[0]] с [pname_kira[4]]."
    scene pgp_club_firstvisit_01
    $ renpy.pause(5)
    scene pgp_club_firstvisit_02
    other emo-998 "[pname_max[0]], да? Пройдёмте за мной."
    scene pgp_club_firstvisit_03
    $ renpy.pause(5)
    scene pgp_club_firstvisit_04
    m emo-0 "Здравствуйте."
    momk emo-321 "Присаживайся, [pname_max[0]]."
label pgn_events_13_momkate_03_next:
    scene pgp_club_firstvisit_06
    m emo-2 "{i}Что-то у меня предчувствие нехорошее.{/i}"
    scene pgp_club_firstvisit_07
    m emo-1 "{i}О! Может быть я зря переживал.{/i}"
    scene pgp_club_firstvisit_08
    if ("erik_momkate") in accessiv:
        momk emo-320 "Помнишь, я помогла тебе с твоей проблемой?"
        m emo-13 "С... Эр...иком?"
        scene pgp_club_firstvisit_09
        momk emo-320 "Я что-то упоминала, об отношениях моей дочери с твоей сестрой, Алисой?"
        menu:
            "Что-то такое припоминанию":
                m emo-2 "Да, кажется вспоминаю. То, что вас не устраивает, что они встречаются и... сексом занимаются."
            "Эм... нет":
                m emo-6 "Что-то такое было?"
                scene pgp_club_firstvisit_10
                m emo-2 "{i}Блин! Мои яйца!{/i}"
                m emo-13 "Да, да, да, я вспомнил."
        momk emo-321 "Ты мне ещё должен."
        m emo-6 "{i}Должен!? Я же выполнил её условия и ещё $5000 заплатил.{/i}"
        scene pgp_club_firstvisit_11
        momk emo-325 "Моя дочка до сих пор встречается с твоей сестрой и мне нужно, чтобы ты их разлучил."
        menu:
            "Я не могу этого сделать":
                $ ivent24.append("отказ_маме_кати")
                m emo-8 "[pname_alice[0]], моя сестра, я не хочу делать ей больно."
                momk emo-321 "Если ты откажешься, то составишь компанию своему старому другу. Он часто о тебе вспоминает."
            "Как?":
                m emo-0 "Что мне нужно сделать? Я не знаю, как. Они давно любят друг друга."
        scene pgp_club_firstvisit_12
        momk emo-320 "Заставь влюбить Катю в тебя, а потом порви с ней отношения."
        menu pgn_events_13_momkate_03_choice1:
            "Это жестоко":
                m emo-8 "Это очень жестоко будет по отношению к Кате."
                momk emo-324 "Я мать и я знаю, что будет для неё лучше. Так что не разочаруй меня и сделай, что от тебя требуют."
                m emo-8 "Ладно."
            "Я не буду" if ("отказ_маме_кати") not in ivent24:
                $ ivent24.append("отказ_маме_кати")
                m emo-8 "[pname_alice[0]], моя сестра, я не буду этого делать."
                momk emo-321 "Если ты откажешься, то составишь компанию своему старому другу. Он часто о тебе вспоминает."
                jump pgn_events_13_momkate_03_choice1
            "Постараюсь":
                m emo-0 "Я постараюсь. Всё что в моих силах."
                momk emo-321 "Вот и хорошо."

    elif ("erik_mob") in accessiv:
        scene pgp_club_firstvisit_09
        momk emo-321 "Некоторое время назад я получила один интересный подарок от знакомых."
        menu:
            "А что за подарок?":
                m emo-3 "А это что за подарок такой?"
                scene pgp_club_firstvisit_10
                m emo-2 "{i}Блин! Мои яйца!{/i}"
                m emo-2 "Извините, продолжайте."
            "Молча слушать дальше":
                pass
        scene pgp_club_firstvisit_11
        momk emo-325 "Моя дочка давно встречается и занимается сексом с твоей сестрой. И меня это не устраивает."
        menu:
            "А причём тут подарок?":
                scene pgp_club_firstvisit_10
                m emo-2 "{i}Блин! Мои яйца!{/i}"
                m emo-2 "Извините, продолжайте."
            "Вы против их секса?":
                m emo-6 "Вы против лесбийского секса?"
                momk emo-325 "Нет. И не только, я против любви как таковой."
        scene pgp_club_firstvisit_12
        momk emo-320 "Мне нужно, чтобы ты любым способ влюбил Катю в себя. Тогда она расстанется с твоей сестрой. А после, ты разорвёшь отношения с моей дочерью."
        menu:
            "Согласиться":
                m emo-2 "{i}Видимо у меня нет выбора.{/i}"
                m emo-2 "Хорошо. Я постараюсь."
            "А если не буду делать этого?":
                m emo-6 "А если я откажусь? Я не хочу делать больно ни своей сестре и не Кате."
                momk emo-321 "Тогда ты тоже станешь моим подарком и приносить мне прибыль."
                m emo-2 "Тогда, я постараюсь."
    scene pgp_club_firstvisit_13
    m emo-2 "{i}Только не сейчас... Что она делает?{/i}"
    scene pgp_club_firstvisit_14
    momk emo-323 "Какой же он большой вблизи. Снимай штаны!"
    m emo-0 "Эм... Хорошо."
    scene pgp_club_firstvisit_15
    m emo-13 "{i}Крепко вцепилась ногами, как птица когтями в жертву.{/i}"
    scene pgp_club_firstvisit_16
    $ renpy.pause()
    scene pgp_club_firstvisit_17
    $ PGN_Achadd(pgnach_158, 158)
    $ renpy.pause()
    scene pgp_club_firstvisit_18
    $ renpy.pause()
    scene pgp_club_firstvisit_19
    momk emo-320 "Достаточно!"
    momk emo-320 "Катя, подойди к нам и встань на колени."
    m emo-9 "{i}Что!? Я не ослышался. Она сказала, Катя!?{/i}"
    scene pgp_club_firstvisit_20
    momk emo-327 "Катя, обслужи клиента, после отведи его в белую комнату."
    ka emo-153 "Да, моя госпожа."
    m emo-9 "{i}Что, госпожа? Ничего себе у них отношения в семье.{/i}"
    $ label_random = 0
    if label_random != 0:
        menu pgn_events_13_momkate_03_choice2:
            "Тебе не обязательно это делать, если не хочешь" if ("momkate_03_choice2_1") not in ivent24:
                ka emo-153 "Мама всё видит и обо всём всегда знает"
                ka emo-154 "Пожалуйста помолчи"
                $ ivent24.append("momkate_03_choice2_1")
                return
            "Я не знал, что ты здесь работаешь" if ("momkate_03_choice2_2") not in ivent24:
                ka emo-156 "Не говори об этом [pname_alice[2]], пожалуйста."
                m emo-0 "А она не знает? Она же бывает здесь каждую пятницу."
                ka emo-153 "Я с ней не вижусь. Выполнишь мою просьбу?"
                m emo-0 "Хорошо"
                $ ivent24.append("momkate_03_choice2_2")
                return
            "Что за \"белая комната\"?" if ("momkate_03_choice2_3") not in ivent24:
                ka emo-150 "Скоро сам всё узнаешь"
                $ ivent24.append("momkate_03_choice2_3")
                return
    scene pgp_club_firstvisit_21
    call pgn_events_13_momkate_03_choice2 from _call_pgn_events_13_momkate_03_choice2
    scene pgp_club_firstvisit_22
    $ renpy.pause()
    scene pgp_club_firstvisit_23
    $ renpy.pause()
    scene pgp_club_firstvisit_24
    call pgn_events_13_momkate_03_choice2 from _call_pgn_events_13_momkate_03_choice2_1
    scene pgp_club_firstvisit_25
    $ renpy.pause()
    scene pgp_club_firstvisit_26
    call pgn_events_13_momkate_03_choice2 from _call_pgn_events_13_momkate_03_choice2_2
    $ renpy.pause()
    scene pgp_club_firstvisit_27
    $ renpy.pause()
    scene pgp_club_firstvisit_28
    $ renpy.pause()
    scene pgp_club_firstvisit_29
    m emo-10 "{i}Я почти.{/i}"
    scene pgp_club_firstvisit_30
    m emo-12 "Аррггхххх!!!"
    scene pgp_club_firstvisit_31
    menu:
        "Сперма на полу":
            m emo-13 "А не чего, что мы тут пол напачкали?"
            ka emo-150 "После нас сразу всё уберут."
        "Спасибо":
            m emo-3 "Спасибо. Это было круто. Не знал, что здесь так классно бывает."
    ka emo-150 "Надевай штаны и идём за мной."
    scene pgp_club_firstvisit_32
    m emo-6 "{i}Знакомые картины. Такие весят у нас дома.{/i}"
    scene pgp_club_firstvisit_33
    ka emo-151 "Не подсматривай."
    m emo-0 "Ок."
    scene pgp_club_firstvisit_34
    m emo-9 "О! Мы прям над комнатой, где только что были? Мы здесь что-то будем делать или просто смотреть что будет внизу?"
    ka emo-152 "Да. Раздевайся."
    scene pgp_club_firstvisit_35
    m emo-6 "Ногами?"
    ka emo-159 "Тебе понравится. Наблюдай, она обычно в это время уже здесь."
    m emo-6 "Кто?"
    scene pgp_club_firstvisit_36
    m emo-9 "{i}[pname_kira[0]]! Она что тут делает? И что это за мужик с ней?{/i}"
    scene pgp_club_firstvisit_37
    m emo-0 "Ничего не слышно о чём они болтают."
    scene pgp_club_firstvisit_38
    ka emo-150 "Они нас тоже не услышат. Это место для подглядываний."
    scene pgp_club_firstvisit_39
    m emo-13 "{i}Что она там вытворяет с ним?{/i}"
    menu:
        "Наблюдать":
            if pgn_ach_repeat ==  0:
                $ accessiv.append("spykiraclub")
            scene pgp_club_firstvisit_40
            m emo-3 "{i}Тетя показывает свои прелести. Да, её попка это класс.{/i}"
            scene pgp_club_firstvisit_41
            m emo-4 "{i}Наконец-то перешла к действиям.{/i}"
            other emo-999 "Аргххх!!!"
            scene pgp_club_firstvisit_42
            m emo-13 "{i}Слабак. Она даже минет не сделала, а он уже кончил.{/i}"
            scene pgp_club_firstvisit_43
            $ renpy.pause()
            scene pgp_club_firstvisit_44
            $ renpy.pause()
            scene pgp_club_firstvisit_45
            $ renpy.pause()
            scene pgp_club_firstvisit_46
            m emo-6 "{i}Она ему свой номер телефона дала?{/i}"
        "Какого черта он вытворяет с ней?":
            scene pgp_club_firstvisit_40
            m emo-11 "{i}Этот гандон смотрит на неё и дрочит.{/i}"
            scene pgp_club_firstvisit_41
            m emo-9 "{i}Она сейчас будет ему сосать!?{/i}"
            scene pgp_club_firstvisit_35
            ka emo-156 "[pname_max[0]]? Всё хорошо? Тебе что-то не нравится?"
            menu:
                "Там моя тётя":
                    m emo-13 "Там внизу моя тётя с каким-то мужиком."
                    ka emo-154 "Это твоя Тётя? Не нравится когда кто-то трахает твою тётю?"
                    m emo-1 "Да."
                    ka emo-156 "Извини, не знала. Тогда закрой глаза и представляй что-нибудь хорошее и сексуальное."
                "Всё нормально":
                    if pgn_ach_repeat ==  0:
                        $ accessiv.append("spykiraclub")
                    m emo-0 "Всё нормально. Продолжай."
                    scene pgp_club_firstvisit_42
                    m emo-3 "{i}На неё уже кончили. А был бы и я там, то на её лице и пустого места не было.{/i}"
                    scene pgp_club_firstvisit_43
                    $ renpy.pause()
                    scene pgp_club_firstvisit_44
                    $ renpy.pause()
                    scene pgp_club_firstvisit_45
                    $ renpy.pause()
                    scene pgp_club_firstvisit_46
                    m emo-6 "{i}Она ему свой номер телефона дала?{/i}"
    scene pgp_club_firstvisit_47
    $ renpy.pause()
    scene pgp_club_firstvisit_48
    $ renpy.pause()
    scene pgp_club_firstvisit_49
    $ renpy.pause()
    scene pgp_club_firstvisit_50
    m emo-10 "Ох! Блин. Я почти."
    ka emo-157 "Наполнишь девушке рот горячей спермой?"
    menu:
        "Кончить на неё":
            scene pgp_club_firstvisit_51
            ka emo-154 "[pname_max[0]]!!!"
            scene pgp_club_firstvisit_52
            ka emo-158 "Какого черта?"
            menu:
                "Что?":
                    m emo-9 "А что такого? Ты внизу лежишь и дрочила ногами, кончить на тебя удобнее."
                    ka emo-157 "Охренеть! Придётся в потратить время на душ из-за тебя."
                    m emo-3 "Да не чё, смоется."
                    ka emo-158 "..."
                "Извини":
                    m emo-2 "Извини. Не успел среагировать."
                    ka emo-157 "Хм... Прощаю, на этот раз."
        "Кончить в рот":
            scene pgp_club_firstvisit_54
            m emo-10 "Кончаю!!!"
            scene pgp_club_firstvisit_55
            m emo-12 "Аргххх!!!"
            scene pgp_club_firstvisit_56
            ka emo-159 "Спасибо."
    menu:
        "Ты не будешь с меня брать деньги?":
            ka emo-156 "Нет. Это за бесплатно. Только..."
            m emo-1 "Что?"
            ka emo-155 "Мама просто так ни чего не делает и наверное у неё есть какие виды на тебя. Если она чего-то хочет, то получает."
            m emo-0 "Понятно. {i}Кажется это было что-то типа аванса.{/i}"
        "Мы ещё куда-то пойдём?":
            ka emo-150 "Нет, это всё. На этом экскурсия закончена."
            m emo-4 "А потом может ещё что-нибудь покажешь?"
            ka emo-155 "[pname_max[0]], всё! Меня работа ждёт и так много времени на тебя потратила."
    ka emo-156 "[pname_max[0]]. У меня есть к тебе просьба."
    m emo-0 "И какая?"
    ka emo-158 "Не приходи больше. Если не хочешь проблем."
    m emo-6 "Проблем?"
    ka emo-158 "Будь осторожен с моей мамой и лучше быть тебе подальше от этого клуба."
    m emo-0 "Ясно."
    ka emo-152 "Потом ещё увидимся."
    m emo-3 "Да. Увидимся."
    if pgn_ach_repeat == 158:
        jump table_pgn_achievement
    $ qtime, momkate_path = qtime+2, 3
    $ PGN_Addstatsex(stat_kate, 0, 0, 0, 0, 1)
    jump loc_club_dancefloor_01


label pgn_events_13_kate_01:
    m emo-2 "{i}Блин! И что же мне делать теперь?{/i}"
    m emo-6 "{i}Если подумать, то у меня есть несколько идей или всё что в голову сейчас может прийти.{/i}"
    m emo-13 "{i}Если мне нужно, чтобы [pname_alice[0]] рассталась с Катей, то могу ей рассказать, что Катя в клубе работает и то что она там делает.{/i}"
    m emo-6 "{i}Или мне может просто взять и признаться в любви Кате? Ну а вдруг сработает.{/i}"
    m emo-6 "{i}И что ещё? Хм...{/i}"
    m emo-6 "{i}Может мне как-то её лучше познакомить с Мамой? Не знаю, как это поможет. Предложу Кате или через Маму, чтобы оставалась у нас на завтрак.{/i}"
    m emo-1 "{i}Вроде есть план. Попробую что-нибудь сделать.{/i}"
    $ kate_path = 3
    jump loc_my_room



label pgn_breakfast_with_kate:
    if ("катя_завтрак_1") not in accessiv:
        scene pgn_breakfast_with_kate_01
        $ renpy.pause()
        scene pgn_breakfast_with_kate_02
        ka emo-153 "Здравствуйте. Извините, задержалась."
        mom emo-62 "Ничего, всё хорошо, мы только сели, ещё не начинали."
        scene pgn_breakfast_with_kate_03
        m emo-9 "{i}Ого! Да эта рубашка почти прозрачная, она видела, что на себя надела?{/i}"
        a emo-20 "[pname_max[0]]! Сбегаешь вниз за стулом?"
        menu:
            "Ок":
                pass
            "Места много":
                m emo-0 "У вас там на диване много места."
                a emo-28 "[pname_max[0]]!"
                mom emo-62 "[pname_max[0]], ну ты чего? Сходи за стулом, а я на твоём месте посижу."
                m emo-0 "Ладно."
            "Принести Кате?":
                m emo-6 "Мне Кате принести?"
                a emo-29 "Себе. А Мама на твоё место сядет."
        scene pgn_breakfast_with_kate_04
        $ renpy.pause()
        scene pgn_breakfast_with_kate_05
        m emo-1 "{i}Кто-нибудь кроме меня заметил, во что она одета? Мама ни чего не сказала совсем.{/i}"
        scene pgn_breakfast_with_kate_06
        a emo-21 "А что это на тебе одето? Это моя рубашка?"
        m emo-13 "{i}Неужели заметила!?{/i}"
        ka emo-152 "Ах да, извини, не спросила. Мне нечего было надеть для такого повода, надела первое что попалось в твоём гардеробе."
        a emo-21 "Носи сколько хочешь. Могу одолжить. Всё равно почти не надеваю."
        scene pgn_breakfast_with_kate_07
        l emo-41 "Катя, а ты нудистка?"
        mom emo-63 "[pname_liza[0]]! Как тебе не стыдно такое спрашивать."
        mom emo-69 "Катя, извини за неё."
        ka emo-152 "Всё хорошо. [pname_liza[0]], как тебе сказать. Я ни разу не раздевалась полностью перед незнакомыми людьми, но дома предпочитаю ходить без верха."
        scene pgn_breakfast_with_kate_08
        mom emo-60 "Подружка [pname_liza[1]], Оливия, она и её мама относится к этой группе людей, к нудистам. Иногда к нам приходит по выходным и загорают у бассейна. И совсем не стесняется."
        mom emo-62 "Катя, ты для нас тоже не чужая, можешь чувствовать себя как дома. Если тебе будет удобно без одежды, то мы не будем против."
        ka emo-152 "Спасибо."
        scene pgn_breakfast_with_kate_09
        l emo-48 "А может мы все будем так же, без верха?"
        mom emo-74 "[pname_liza[0]]!"
        k emo-101 "[pname_mom[6]]. А почему бы и нет. Мы все друг друга видели без одежды, да и тут постоянно солнечно. Можно совместить приятное с полезным. Солнечные ванны, загар и твоя вкусная готовка."
        a emo-21 "Отличная идея. Только кое-кому придётся тогда завтракать отдельно."
        menu:
            "Почему мне?":
                m emo-6 "И почему это я должен быть отдельно от вас?"
                a emo-21 "Потому что чья-то штучка будет постоянно нас отвлекать."
            "И кому?":
                m emo-6 "И кто это будет?"
                a emo-22 "Не догадываешься? Школу бросил и мозгов совсем нет?"
        mom emo-63 "[pname_alice[0]], хватит! Пока что можно только Кате, остальным, поживём и увидим. И мы семья, должны быть всегда вместе."
        a emo-20 "Прости."
        mom emo-62 "Ну всё. Приятного аппетита и Катя, спасибо что к нам присоединилась."
        ka emo-159 "Это вам спасибо."
        $ accessiv.append("катя_завтрак_1")
    elif ("катя_завтрак_2") not in accessiv or ("катя_завтрак_3") not in accessiv:
        scene pgn_breakfast_with_kate_10
        m emo-4 "{i}О! Катя совсем без верха, с голыми сиськами. Класс!{/i}"
        menu:
            "Пялиться на сиськи":
                m emo-3 "{i}Пока все увлечены разговором. Полюбуюсь голыми сиськами.{/i}"
                scene pgn_breakfast_with_kate_11
                m emo-4 "{i}Класс!{/i}"
                scene pgn_breakfast_with_kate_12
                m emo-3 "{i}Вот бы все были голыми.{/i}"
                menu:
                    "Продолжить":
                        scene pgn_breakfast_with_kate_13
                        m emo-0 "{i}Она потянулась за фруктами.{/i}"
                        m emo-3 "{i}Не я один любуюсь видом. [pname_alice[0]] тоже.{/i}"
                        scene pgn_breakfast_with_kate_14
                        m emo-4 "{i}У неё обзор ещё лучше. Прям слюни потекли.{/i}"
                        scene pgn_breakfast_with_kate_15
                        m emo-6 "{i}Мама тоже возбудилась? Неужели он хочет прямо здесь, перед всеми, мой член? Вау! Спасибо тебе Катя.{/i}"
                        menu:
                            "Продолжить":
                                scene pgn_breakfast_with_kate_16
                                m emo-1 "{i}Ни разу ещё так пристально не наблюдал как едят банан.{/i}"
                                scene pgn_breakfast_with_kate_17
                                m emo-3 "{i}Давай. Засунь его себе в рот.{/i}"
                                scene pgn_breakfast_with_kate_18
                                m emo-4 "{i}Ну же. Ещё ближе!{/i}"
                                scene pgn_breakfast_with_kate_19
                                m emo-4 "{i}Ещё чуть-чуть.{/i}"
                                scene pgn_breakfast_with_kate_20
                                m emo-3 "{i}Отлично! А теперь глубже.{/i}"
                                scene pgn_breakfast_with_kate_21
                                m emo-2 "{i}Ай! Блин! Мой бананчик!{/i}"
                                scene pgn_breakfast_with_kate_22
                                m emo-13 "{i}По маминому выражению лица понятно, что достаточно.{/i}"
                            "Остановиться":
                                pass
                    "Остановиться":
                        pass
            "Нет. Вдруг кто заметит, мне ещё прилетит":
                pass
        if ("катя_завтрак_2") not in accessiv:
            $ accessiv.append("катя_завтрак_2")
        else:
            $ accessiv.append("катя_завтрак_3")
    elif ("катя_завтрак_4") not in accessiv:
        scene pgn_breakfast_with_kate_23
        m emo-3 "{i}Ого! [pname_alice[0]] тоже сняла с себя вверх.{/i}"
        m emo-9 "{i}Но [pname_alice[0]] же в одной майке ходила и без трусиков. Она сейчас что, совсем голая сидит? И Мама никак не реагирует?{/i}"
        m emo-9 "{i}Это сон? Или всё же мечты постепенно становятся явью?{/i}"
        $ accessiv.append("катя_завтрак_4")
    elif ("катя_завтрак_5") not in accessiv:
        scene pgn_breakfast_with_kate_23
        l emo-41 "Мама. А можно я тоже разденусь?"
        if daysn != 6 and daysn != 7:
            mom emo-63 "[pname_liza[0]]! Сиди ешь, тебе скоро в школу идти."
        else:
            mom emo-60 "Нет."
        m emo-0 "{i}Видно Мама пока ещё против того, чтобы [pname_liza[0]] раздевалась.{/i}"
        $ accessiv.append("катя_завтрак_5")
    elif (("катя_завтрак_6") not in accessiv or kate_path <= 4) and "катя_лесбосмамой" not in accessiv:
        scene pgn_breakfast_with_kate_24
        if ("катя_завтрак_6") not in accessiv:
            $ accessiv.append("катя_завтрак_6")
            m emo-3 "{i}О! Теперь и [pname_kira[0]] с голыми сиськами сидит. Круто!{/i}"
            m emo-4 "{i}Осталась только [pname_liza[0]] с Мамой.{/i}"
            m emo-3 "{i}Спасибо тебе. Кать.{/i}"
        else:
            m emo-3 "Всем приятного аппетита!"
    elif (("катя_завтрак_7") not in accessiv or ("катя_завтрак_8") not in accessiv or ("катя_завтрак_9") not in accessiv) and "катя_лесбосмамой" in accessiv:
        scene pgn_breakfast_with_kate_24
        m emo-3 "Всем приятного аппетита!"
        if ("катя_завтрак_7") not in accessiv:
            $ accessiv.append("катя_завтрак_7")
        elif ("катя_завтрак_8") not in accessiv:
            $ accessiv.append("катя_завтрак_8")
        elif ("катя_завтрак_9") not in accessiv:
            $ accessiv.append("катя_завтрак_9")
    elif (("катя_завтрак_10") not in accessiv or ("завтрак_голыесиськи") in accessiv) and "катя_лесбосмамой" in accessiv:
        scene pgn_breakfast_with_kate_25
        if ("катя_завтрак_10") not in accessiv:
            $ accessiv.append("катя_завтрак_10")
            m emo-4 "{i}Наконец-то настал тот день, когда все они с голыми сиськами сидят за столом. Катя, спасибо тебе!{/i}"
        menu:
            "Посмотреть на сиськи":
                menu:
                    "Сиськи Мамы":
                        scene pgn_breakfast_with_kate_26
                        $ renpy.pause()
                        scene pgn_breakfast_with_kate_27
                        $ renpy.pause()
                    "Сиськи [pname_kira[1]]":
                        scene pgn_breakfast_with_kate_28
                        $ renpy.pause()
                        scene pgn_breakfast_with_kate_29
                        $ renpy.pause()
                    "Сиськи [pname_alice[1]]":
                        scene pgn_breakfast_with_kate_30
                        $ renpy.pause()
                        scene pgn_breakfast_with_kate_31
                        $ renpy.pause()
                    "Сиськи Кати":
                        scene pgn_breakfast_with_kate_32
                        $ renpy.pause()
                        scene pgn_breakfast_with_kate_33
                        $ renpy.pause()
                    "Сиськи [pname_liza[1]]":
                        scene pgn_breakfast_with_kate_34
                        $ renpy.pause()
                        scene pgn_breakfast_with_kate_35
                        $ renpy.pause()
            "Продолжить завтрак":
                mom emo-62 "Всем приятного аппетита."
    jump veranda_breakfast_next


label pgn_events_13_momkate_04:
    scene pgn_club_momkate_02_bar
    $ renpy.pause()
    scene pgn_club_momkate_03_bar
    $ renpy.pause()
    scene pgn_club_momkate_04_bar
    momk emo-321 "Привет [pname_max[0]]."
    m emo-0 "Здравствуйте."
    momk emo-320 "Катя, что-то стала сильно у вас задерживаться. Это часть твоего плана?"
    m emo-13 "Да..."
    momk emo-325 "И когда перейдёшь к серьезным действиям? Она всё ещё встречается с твоей сестрой."
    menu:
        "Я думаю":
            m emo-0 "Я думаю, что делать дальше."
        "В процессе":
            m emo-0 "Всё идёт по плану."
    momk emo-320 "Хорошо. Не буду мешать. Но тебе лучше поторопиться. А не то..."
    scene pgn_club_momkate_05_bar
    momk emo-327 "Ты станешь моей новой игрушкой. Не разочаруй меня."
    $ accessiv.append("momkate_katebreakfast")
    jump loc_club_bar


label pgn_events_13_alice_kateclub:
    m emo-0 "[pname_alice[0]], я тут кое-что узнал и хотел бы рассказать, только не знаю, как ты на это отреагируешь."
    a emo-20 "Что? Рассказывай."
    m emo-0 "Это касается Кати."
    a emo-32 "Что с ней? Если бы что-то произошло, она бы мне всё рассказала, мы ничего не скрываем друг от друга."
    m emo-13 "Как раз таки скрывает. Она в клубе по ночам танцует стриптиз и оказывает сексуальные услуги."
    a emo-33 "Я об этом давно знаю. Да, она мне не рассказывала, но я не один раз в клубе была."
    if ("коуб_фдшса_спалила") not in accessiv:
        a emo-26 "Подожди, а ты от куда это знаешь? Ты был в клубе? А ты знаешь, что тебе ещё рано там находиться?"
    else:
        a emo-26 "Подожди, а ты от куда это знаешь?"
    menu:
        "Да. Я сам видел":
            m emo-0 "Да. Я там был и видел всё сам, какие развратные танцы она танцует и делает всякое."
        "Ничего мне не рано, я взрослый" if ("коуб_фдшса_спалила") not in accessiv:
            m emo-11 "Почему это рано? Я вовсю уже сексом занимаюсь и видел много голых женщин, и я уже взрослый."
            a emo-26 "Ага, конечно, взрослый. Пипирка только выросла, а ведешь себя всё ещё как ребёнок."
            m emo-9 "Эээ..."
    a emo-23 "Я не понимаю, как ты туда попал. Ты там алкогольные напитки пьёшь? Если Мама узнает, то влетит не только тебе, но и мне с [pname_kira[4]], т.к. в первую очередь она подумает на нас, что это мы тебя с собой взяли."
    menu:
        "Я не пью":
            m emo-0 "Спиртные напитки я не пью."
            m emo-13 "{i}Точнее мне их не продают.{/i}"
        "Есть у меня связи":
            m emo-0 "Есть у меня связи в клубе."
            a emo-28 "Связи, да? Тогда если что, мы с [pname_kira[4]] тут не при чём. Ясно?"
            m emo-0 "Да, понятно."
    a emo-20 "Ладно, ясно всё с тобой. Про Катю мне ничего нового не рассказал и так знаю. И что ты хотел, рассказав мне об этом?"
    menu:
        "Расстанься с ней":
            m emo-13 "{i}Не буду ей такого говорить. Ещё и разозлится на меня, будет только хуже.{/i}"
            if ("катя_завтрак_3") in accessiv:
                m emo-13 "{i}Ничего не остаётся, как рассказать им обеим.{/i}"
            else:
                m emo-6 "{i}Нужно придумать тогда другой способ.{/i}"
        "Просто":
            pass
    m emo-0 "Просто узнал и хотел поделиться."
    a emo-20 "Тогда спасибо и иди куда шёл. Или хочешь о чём-то ещё со мной поговорить?"
    m emo-0 "Нет. Это всё."
    $ kate_path = 3.1
    jump jump_dialogue


label pgn_events_13_aliceandkate:
    if "loc_pool" in location:
        m emo-0 "Пойдём в комнату [pname_alice[1]], есть разговор."
    else:
        m emo-0 "Нужно поговорить о кое-чем важном."
    scene pgn_events_13_aliceroom_alicekate_01
    a emo-20 "Так о чём хотел поговорить? Только давай побыстрей."
    m emo-0 "Я недавно виделся с Мамой Кати. И она попросила меня ей помочь в одном деле."
    ka emo-158 "Я же говорила тебе держаться от неё подальше."
    if ("momkate_katebreakfast") in accessiv:
        $ accessiv.remove("momkate_katebreakfast")
        m emo-2 "Ну так получилось"
    else:
        m emo-0 "Это ещё тогда."
        a emo-23 "Когда?"
        ka emo-156 "Потом расскажу."
    m emo-15 "Она попросила, сделать всё, чтобы вы перестали встречаться."
    scene pgn_events_13_aliceroom_alicekate_02
    a emo-23 "[pname_max[0]]! Это ты так шутишь что ли?"
    a emo-20 "Подожди. А то что Катю Мама неожиданно предложила оставаться на завтрак. Это твоих рук дело?"
    a emo-32 "[pname_max[0]]! Это как понимать? Чем тебе Катя не угодила?"
    ka emo-150 "[pname_alice[0]]! [pname_max[0]] тут не при чём."
    a emo-30 "О чём ты говоришь?!"
    a emo-32 "Он сделал специально, ради своей извращенной выгоде."
    a emo-32 "Он думал, что я разозлюсь, узнав, что ты работаешь по ночам в клубе."
    ka emo-151 "Эм..."
    a emo-33 "Не переживай, я и так об этом знаю. И я тебя поддержу и не хочу с тобой расставаться."
    scene pgn_events_13_aliceroom_alicekate_03
    ka emo-157 "[pname_alice[0]]! Ты не знаешь мою мать. Она... Как тебе проще сказать. Мама владеет клубом, но в действительности там ещё предоставляют... {i}особые услуги{/i} для знаменитостей и богачей. Может что-то ещё, мама точно от меня что-то ещё скрывает."
    if ("erik_momkate") in accessiv:
        ka emo-150 "И Эрик ваш тоже у Мамы."
    if ("erik_mob") in accessiv:
        m emo-13 "И Эрик видимо теперь у неё."
    a emo-32 "А Эрик как там оказался? Он же ведь бросил маму или это не так, [pname_max[0]]?"
    scene pgn_events_13_aliceroom_alicekate_01
    m emo-8 "Ну так он мошенник и хотел отобрать у нас дом. И он не тот, за кого себя выдавал."
    a emo-32 "И с чего это ты взял?"
    m emo-11 "Он сразу мне показался странным типом."
    a emo-27 "Странным? Он за нами и мамой ухаживал, дарил подарки."
    m emo-0 "Но не за просто так..."
    a emo-27 "Что?"
    m emo-0 "Он не Эрик, а Виктор Моро. Так было написано на его правах и они настоящие. И ещё подслушал разговор, как он с кем-то общался и назвал нашу мать {i}собачонкой{/i}."
    a emo-30 "Ох! А Мама в курсе?"
    m emo-8 "Нет. Не знаю, как лучше это сказать и когда."
    a emo-20 "Понятно. Лучше пока ничего не рассказывай."
    if ("erik_momkate") in accessiv:
        a emo-20 "А то, что вы его упрятали куда подальше. Это вы молодцы."
    if ("erik_mob") in accessiv:
        a emo-23 "[pname_max[0]], ты молодец. Ни за что бы не подумала, что он такой плохой человек."
    scene pgn_events_13_aliceroom_alicekate_03
    a emo-20 "Тогда, что нам делать? Катя, она же не сделает ни чего [pname_max[2]]?"
    menu:
        "Ты меня любишь?":
            scene pgn_events_13_aliceroom_alicekate_01
            m emo-3 "Ты меня любишь и не хочешь расстаться?"
            a emo-28 "[pname_max[0]]! Нечего тут себе напридумывать. Ты мой и брат и я волнуюсь за тебя, как сестра."
            m emo-13 "{i}Ну да, ну да...{/i}"
        "Промолчать":
            pass
    scene pgn_events_13_aliceroom_alicekate_01
    ka emo-157 "Не знаю... [pname_max[0]], она тебе давала сроки?"
    m emo-13 "Эм... нет, вроде."
    ka emo-158 "Мама не любит ждать, она не из терпеливых и всегда получает желаемое. У тебя есть какой-нибудь план или идея?"
    m emo-6 "Хм... Есть!"
    m emo-0 "Может как-нибудь показать, что ты со мной встречаешься, а не с [pname_alice[4]]?"
    a emo-20 "И где и как ты предлагаешь это сделать?"
    m emo-0 "В клубе. В пятницу. Когда ты бываешь в клубе."
    ka emo-150 "В этот день я не работаю, но прийти смогу."
    ka emo-152 "Хорошо. [pname_max[0]], напиши мне, когда будешь в клубе и я подойду."
    $ kate_path = 3.2
    $ qtime += 1
    jump jump_dialogue



label pgn_events_13_club_datekate_01:
    scene pgn_club_date_kate_01
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random == 3:
        if ("alice_club_choco") not in ivent24:
            scene pgn_club_date_kate_02
            a emo-22 "[pname_max[0]]!"
            m emo-9 "Ай!"
            scene pgn_club_date_kate_03
            a emo-21 "Катю ждёшь?"
            m emo-0 "Ага."
            a emo-23 "Пообещай мне, что не будешь пить. Хорошо?"
            m emo-0 "Ок. {i}Наверное...{/i}"
            a emo-22 "Хорошо вам повеселиться, а я пойду... Тёте сообщу, что за тобой присмотрит Катя."
            m emo-0 "{i}Не такой уж я и маленький.{/i}"
            $ ivent24.append("wrongclub_approved")
        else:
            $ ivent24.append("wrongclub_approved")
            scene pgn_club_date_kate_04
            a emo-22 "Ой! Ик! Ммм... братик... Ик!"
            scene pgn_club_date_kate_05
            m emo-0 "Ого! Какая ты пьяная. Выпила всё что было в баре?"
            a emo-24 "Я не пьяная. Ик!"
            a emo-25 "Может пойдём и потрахаемся? Ик!"
            menu:
                "Пошли":
                    $ ivent24.append("aliceclub_restinvit")
                    jump pgn_club_restw_alicedrink
                "Я жду Катю":
                    m emo-0 "Вообще-то Катю жду, а вот тебе пара завязывать с напитками и ехать домой."
                    a emo-25 "Я ещё не настолько пьяная. Я хочу ещё веселиться!"
                    scene pgn_club_date_kate_06 with dissolve
                    a emo-21 "Ну так пойдёшь или твой инструмент не встанет на меня?"
                    menu:
                        "Где [pname_kira[0]]?":
                            m emo-6 "А где [pname_kira[0]]? Почему не с ней?"
                            scene pgn_club_date_kate_05
                            a emo-23 "Не знаю. Она с кем-то разговаривала, и после ушла, оставив меня одну."
                            a emo-23 "Ладно. Не хочешь, как хочешь."
                        "Ах так!":
                            m emo-4 "Ах так! Тогда пошли, и трахну тебя как следует."
                            $ ivent24.append("aliceclub_restinvit")
                            jump pgn_club_restw_alicedrink
                        "Я пасс":
                            m emo-13 "Лучше подожду Катю."
                            a emo-23 "Как знаешь, тогда я пойду и поищу себе партнёра получше."
                            menu:
                                "Отвести в туалет и трахнуть её":
                                    m emo-0 "Ладно. Пошли."
                                    a emo-22 "Ты мой любимый братик."
                                    $ ivent24.append("aliceclub_restinvit")
                                    jump pgn_club_restw_alicedrink
                                "Отвезти домой":
                                    m emo-11 "Так не пойдёт. Ты слишком пьяна, поедем домой."
                                    a emo-32 "Не хочу..."
                                    $ ivent24.append("wrongclub_kira_and_alice")
                                    $ accessiv.append("mapmax_off")
                                    jump loc_pool_move
                                "Оставить её в покое":
                                    pass
label pgn_events_13_club_datekate_01_next:
    if ("aliceclub_restinvit") in ivent24:
        if renpy.random.randint ( 1, 3) == 2:
            scene pgn_club_dancefloor_01
            m emo-6 "Хм... А где Катя?"
            if date_kate > 0:
                $ date_kate -= 1
            jump loc_club_dancefloor_01
    scene pgn_club_date_kate_07
    $ renpy.pause()
    scene pgn_club_date_kate_08
    ka emo-152 "Привет."
    if kate_path == 3.2:
        menu pgn_club_datekate_d1m1:
            "Комплимент" if ("свидкатя_комплимент") not in ivent24:
                m emo-3 "Ты хорошо выглядишь. Даже очень."
                ka emo-152 "Спасибо."
                $ date_kate += 1
                $ ivent24.append("свидкатя_комплимент")
                jump pgn_club_datekate_d1m1
            "Прижать к себе":
                scene pgn_club_date_kate_09
                ka emo-158 "[pname_max[0]]! Отпусти меня. Не забывай, что мы здесь только притворяемся парой."
                menu:
                    "Поцеловать":
                        scene pgn_club_date_kate_10
                        ka emo-154 "Ммм..."
                        scene pgn_club_date_kate_09
                        ka emo-155 "Ты охренел что ли!?"
                        m emo-6 "А что? Парочки ведь так делают."
                        ka emo-155 "Но не на первом же свидании."
                        m emo-3 "Ну они и не такое делают..."
                        ka emo-158 "Надеюсь в следующий раз ты будешь думать, перед тем что-то делать."
                        scene pgn_club_date_kate_01
                        m emo-13 "Блин."
                        $ date_kate -= 1
                        jump loc_club_dancefloor_01
                    "Ухватиться за попку":
                        scene pgn_club_date_kate_11
                        ka emo-157 "Руку убрал! Я думала ты нормальный."
                        m emo-13 "Ладно, прости, не удержался."
                        ka emo-158 "Живо меня отпустил. Я тебе не шлюха."
                        $ date_kate -= 1
                        jump pgn_club_datekate_d1m1
                    "Отпустить":
                        scene pgn_club_date_kate_08
                        jump pgn_club_datekate_d1m1
            "В бар":
                $ location = ["loc_club", "loc_club_bar"]
                call loc_club_locchr from _call_loc_club_locchr_1
    elif kate_path == 3.3:
        menu pgn_club_datekate_d2m1:
            "Комплимент" if ("свидкатя_комплимент") not in ivent24:
                m emo-4 "Ты всё так же очень красива."
                ka emo-152 "Спасибо."
                $ date_kate += 1
                $ ivent24.append("свидкатя_комплимент")
                jump pgn_club_datekate_d2m1
            "Прижать к себе":
                if date_kate == 2:
                    scene pgn_club_date_kate_09b
                else:
                    scene pgn_club_date_kate_09
                ka emo-158 "[pname_max[0]]! Отпусти меня. Не забывай, что мы здесь только притворяемся парой."
                menu:
                    "Поцеловать":
                        scene pgn_club_date_kate_10
                        ka emo-154 "Ммм..."
                        scene pgn_club_date_kate_09
                        ka emo-155 "Ты охренел что ли!?"
                        m emo-6 "А что? "
                        ka emo-158 "Надеюсь в следующий раз ты будешь думать, перед тем что-то делать"
                        scene pgn_club_date_kate_01
                        m emo-13 "Блин."
                        $ date_kate -= 1
                        jump loc_club_dancefloor_01
                    "Ухватиться за попку":
                        scene pgn_club_date_kate_11
                        ka emo-157 "Руку убрал!"
                        m emo-13 "Прости, не удержался."
                        ka emo-158 "Живо меня отпустил. Я тебе не шлюха."
                        $ date_kate -= 1
                        jump pgn_club_datekate_d2m1
                    "Отпустить":
                        scene pgn_club_date_kate_08
                        jump pgn_club_datekate_d2m1
            "В бар":
                $ location = ["loc_club", "loc_club_bar"]
                call loc_club_locchr from _call_loc_club_locchr_2
    elif kate_path >= 3.4 and kate_path <= 3.6:
        menu pgn_club_datekate_d3m1:
            "Комплимент" if ("свидкатя_комплимент") not in ivent24:
                m emo-4 "Ты очень сексуально выглядишь."
                ka emo-153 "Спасибо."
                $ ivent24.append("свидкатя_комплимент")
                jump pgn_club_datekate_d3m1
            "Прижать к себе" if ("свидкатя_прижатьксебе") not in ivent24:
                $ ivent24.append("свидкатя_прижатьксебе")
                scene pgn_club_date_kate_09b
                ka emo-151 "[pname_max[0]]! Отпусти меня. Не забывай, что мы здесь только притворяемся парой."
                menu:
                    "Поцеловать":
                        scene pgn_club_date_kate_10
                        ka emo-154 "Ммм..."
                        scene pgn_club_date_kate_09
                        ka emo-155 "Ты охренел что ли!?"
                        m emo-6 "А что? "
                        ka emo-158 "Надеюсь в следующий раз ты будешь думать, перед тем что-то делать"
                        m emo-13 "Извини."
                        $ date_kate -= 1
                        if kate_path == 3.4:
                            jump loc_club_dancefloor_01
                    "Ухватиться за попку":
                        scene pgn_club_date_kate_11b
                        ka emo-156 "[pname_max[0]]."
                        m emo-4 "У тебя классная и упругая попка. Сложно удержаться."
                        if ("свидкатя_комплимент") in ivent24:
                            $ date_kate += 1
                        jump pgn_club_datekate_d3m1
                    "Отпустить":
                        $ ivent24.remove("свидкатя_прижатьксебе")
                        scene pgn_club_date_kate_08
                        jump pgn_club_datekate_d3m1
            "В бар":
                $ location = ["loc_club", "loc_club_bar"]
                call loc_club_locchr from _call_loc_club_locchr_3
    elif kate_path >= 3.7:
        menu pgn_club_datekate_d4m1:
            "Комплимент" if ("свидкатя_комплимент") not in ivent24:
                m emo-3 "Ты прекрасно выглядишь. Секси."
                ka emo-159 "Спасибо."
                $ ivent24.append("свидкатя_комплимент")
                jump pgn_club_datekate_d4m1
            "Прижать к себе" if ("свидкатя_прижатьксебе") not in ivent24:
                $ ivent24.append("свидкатя_прижатьксебе")
                scene pgn_club_date_kate_09b
                menu:
                    "Поцеловать":
                        scene pgn_club_date_kate_10b
                        ka emo-152 "Ммм..."
                        scene pgn_club_date_kate_09b
                        if ("свидкатя_комплимент") in ivent24:
                            $ date_kate += 1
                        $ renpy.pause()
                        jump pgn_club_datekate_d4m1
                    "Ухватиться за попку":
                        scene pgn_club_date_kate_11b
                        ka emo-152 "[pname_max[0]]."
                        m emo-4 "У тебя классная и упругая попка. Сложно удержаться..."
                        jump pgn_club_datekate_d4m1
            "В бар":
                $ location = ["loc_club", "loc_club_bar"]
                call loc_club_locchr from _call_loc_club_locchr_4

label pgn_events_13_club_datekate_02_bar:
    scene pgn_club_date_kate_12_vadx
    $ clubdrink_max = clubdrink_kate = scene_random = 0
    ka emo-151 "Что будешь пить?"
    scene pgn_location_club_bar_men_01
    if kate_path == 3.2:
        menu:
            "Сок":
                m emo-0 "Я сок попью."
                $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
            "Спиртные напитки":
                m emo-3 "Мы клубе и на свидании. Так что почему бы и не выпить."
                ka emo-150 "Мы типа на свидании. И [pname_alice[0]] сказала, что тебе нельзя алкоголь."
                m emo-2 "Ну может немного?"
                ka emo-150 "Будешь сок."
                m emo-0 "Ладно."
                $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
    else:
        menu:
            "Сок":
                $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
            "Алкогольный напиток":
                m emo-1 "Мне пожалуйста..."
                other emo-999 "Предъявите права или удостоверение, чтобы удостовериться, что вы можете покупать алкоголь."
                m emo-13 "Эм... {i}всё равно возраст у меня не подходящий.{/i}"
                ka emo-150 "Налейте ему сока."
                $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
            "Попросить Катю":
                m emo-5 "Катя, можешь мне заказать выпивку? Пожалуйста."
                if (kate_path >= 3.4 and kate_path <= 3.6):
                    ka emo-150 "Хорошо. Но только одну."
                    $ ivent24.append("клуб_макс_алкоголь")
                    $ clubdrink_max, clubdrink_kate = clubdrink_max+30, clubdrink_kate+30
                elif kate_path >= 3.6:
                    ka emo-150 "Налей ему."
                    $ ivent24.append("клуб_макс_алкоголь")
                    $ clubdrink_max, clubdrink_kate = clubdrink_max+30, clubdrink_kate+30
                else:
                    ka emo-150 "Налейте ему сока."
                    $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
label pgn_events_13_club_datekate_02_bar_next:
    scene pgn_club_date_kate_13_vadx
    $ renpy.pause()
    scene pgn_club_date_kate_14_vadx
    $ renpy.pause()
    scene pgn_club_date_kate_15_vadx
    $ renpy.pause()
    if ("клуб_макс_алкоголь_2") in ivent24:
        scene pgn_club_date_kate_19_vadx
        ka emo-154 "[pname_max[0]], всё хорошо?"
        scene black with dissolve
        $ renpy.pause(5, hard=True)
        $ qtime, currency = qtime+1, currency-(clubdrink_max+clubdrink_kate)
        jump pgn_club_max_alcogol
    menu:
        "Положить руку на ногу Кати":
            scene pgn_club_date_kate_18_vadx
            if kate_path < 3.5:
                ka emo-155 "[pname_max[0]]!!!"
                menu:
                    "Убрать руку":
                        pass
                    "Проигнорировать":
                        m emo-3 "Да ладно тебе, что такого?"
                        ka emo-158 "Руку убрал!"
                        m emo-0 "Ладно. Извини."
                        $ date_kate -= 1
            else:
                ka emo-159 "..."
        "Не делать этого":
            pass
    scene pgn_club_date_kate_16_vadx
    $ renpy.pause()
    scene pgn_club_date_kate_17_vadx
    if ("клуб_макс_алкоголь") not in ivent24:
        ka emo-152 "Ещё или пойдём потанцуем?"
    else:
        scene pgn_club_date_kate_19_vadx
        ka emo-155 "Ты как, может домой поедешь?"
    menu:
        "Заказать ещё напитков":
            m emo-0 "Давай ещё немного посидим."
            if kate_path == 3.2:
                $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
            else:
                menu:
                    "Сок":
                        $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
                    "Алкогольный напиток":
                        m emo-1 "Мне пожалуйста..."
                        ka emo-150 "Налейте ему сока."
                        m emo-2 "{i}Чёрт!{/i}"
                        $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
                    "Попросить Катю":
                        m emo-5 "Катя, можешь мне заказать ещё выпивку? Пожалуйста."
                        if (kate_path >= 3.4 and kate_path <= 3.6):
                            ka emo-157 "Нет. Договорились только на одну."
                            $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
                        elif kate_path >= 3.6:
                            ka emo-150 "Хорошо."
                            $ ivent24.append("клуб_макс_алкоголь_2")
                        else:
                            ka emo-157 "Налейте ему сока."
                            $ clubdrink_max, clubdrink_kate = clubdrink_max+20, clubdrink_kate+30
            jump pgn_events_13_club_datekate_02_bar_next
        "Танцпол":
            call pgn_events_13_club_datekate_pay from _call_pgn_events_13_club_datekate_pay
            if ("клуб_макс_алкоголь") in ivent24:
                m emo-5 "Да, не всё нормально, танцевать могу"
            $ location = ["loc_club", "loc_club_dancefloor_01"]
            call loc_club_locchr from _call_loc_club_locchr_5
            scene pgn_club_date_kate_25
            $ renpy.pause()
            scene pgn_club_date_kate_20_vadx
            if kate_path == 3.3 and ("свидкатя_максплатит_бар") in ivent24:
                scene pgn_club_date_kate_21_vadx
                $ renpy.pause()
                scene pgn_club_date_kate_22_vadx
            if (kate_path >= 3.4 and kate_path <= 3.6) and ("свидкатя_максплатит_бар") in ivent24:
                scene pgn_club_date_kate_23_vadx
            if kate_path >= 3.7 and ("свидкатя_максплатит_бар") in ivent24:
                scene pgn_club_date_kate_21_vadx
                $ renpy.pause()
                scene pgn_club_date_kate_22_vadx
                $ renpy.pause()
                scene pgn_club_date_kate_23_vadx
                $ renpy.pause()
                scene pgn_club_date_kate_24
            $ renpy.pause()
        "Стриптиз":
            call pgn_events_13_club_datekate_pay from _call_pgn_events_13_club_datekate_pay_1
            m emo-4 "Может посмотрим, как другие танцуют."
            ka emo-150 "Эм... Ладно. Пойдём."
            scene pgn_club_date_kate_25
            $ location = ["loc_club", "loc_club_dancefloor_01"]
            call loc_club_locchr from _call_loc_club_locchr_6
            menu:
                "Стриптизерша 1":
                    scene pgn_club_striptease_girl1_01
                    menu:
                        "$100":
                            $ stripgirlm1 += 100
                            $ currency -= 100
                            $ date_kate += 1
                            $ screennotify("$", 11, 100)
                            $ ivent24.append("свидкатя_максплатит_стриптиз")
                        "$300":
                            $ stripgirlm1 += 300
                            $ currency -= 300
                            $ date_kate += 1
                            $ screennotify("$", 11, 300)
                            $ ivent24.append("свидкатя_максплатит_стриптиз")
                        "$500":
                            $ stripgirlm1 += 500
                            $ currency -= 500
                            $ date_kate += 1
                            $ screennotify("$", 11, 500)
                            $ ivent24.append("свидкатя_максплатит_стриптиз")
                        "Денег нет" if kate_path < 3.6:
                            m emo-13 "У мен денег нет. Можешь заплатить?"
                            ka emo-158 "..."
                            $ date_kate -= 1
                        "Оплатить по полам":
                            $ stripgirlm1 += 300
                            m emo-13 "Может поделим счёт по полам?"
                            ka emo-157 "Хорошо. Давай сделаем так."
                            $ currency -= 150
                            $ screennotify("$", 11, 150)
                    scene pgn_club_date_kate_30
                    if (kate_path >= 3.5 and (("свидкатя_максплатит_стриптиз") in ivent24 or ("свидкатя_максплатит_бар") in ivent24)) or (("свидкатя_максплатит_стриптиз") in ivent24 and ("свидкатя_максплатит_бар") in ivent24):
                        scene pgn_club_date_kate_31
                    $ renpy.pause()
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
                        scene pgn_club_date_kate_30
                        if (kate_path >= 3.5 and (("свидкатя_максплатит_стриптиз") in ivent24 or ("свидкатя_максплатит_бар") in ivent24)) or (("свидкатя_максплатит_стриптиз") in ivent24 and ("свидкатя_максплатит_бар") in ivent24):
                            scene pgn_club_date_kate_31
                        $ renpy.pause()
                        scene pgn_club_striptease_girl1_07
                        $ renpy.pause()
                        scene pgn_club_striptease_girl1_08
                        $ renpy.pause()
                    if stripgirlm1 >= 150 and stripgirlm1 < 500:
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
                        scene pgn_club_date_kate_30
                        if (kate_path >= 3.5 and (("свидкатя_максплатит_стриптиз") in ivent24 or ("свидкатя_максплатит_бар") in ivent24)) or (("свидкатя_максплатит_стриптиз") in ivent24 and ("свидкатя_максплатит_бар") in ivent24):
                            scene pgn_club_date_kate_31
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
                        scene pgn_club_date_kate_30
                        if (kate_path >= 3.5 and (("свидкатя_максплатит_стриптиз") in ivent24 or ("свидкатя_максплатит_бар") in ivent24)) or (("свидкатя_максплатит_стриптиз") in ivent24 and ("свидкатя_максплатит_бар") in ivent24):
                            scene pgn_club_date_kate_31
                        $ renpy.pause()
                        scene pgn_club_striptease_girl1_16
                        $ renpy.pause()
                        scene pgn_club_striptease_girl1_17
                        $ renpy.pause()
                "Стриптизерша 2":
                    scene pgn_club_date_kate_26
                    $ renpy.pause()
                    scene pgn_club_striptease_girl2_01
                    menu:
                        "$100":
                            $ stripgirlm2 += 100
                            $ currency -= 100
                            $ date_kate += 1
                            $ screennotify("$", 11, 100)
                            $ ivent24.append("свидкатя_максплатит_стриптиз")
                        "$300":
                            $ stripgirlm2 += 300
                            $ currency -= 300
                            $ date_kate += 1
                            $ screennotify("$", 11, 300)
                            $ ivent24.append("свидкатя_максплатит_стриптиз")
                        "$500":
                            $ stripgirlm2 += 500
                            $ currency -= 500
                            $ date_kate += 1
                            $ screennotify("$", 11, 500)
                            $ ivent24.append("свидкатя_максплатит_стриптиз")
                        "Денег нет" if kate_path < 3.6:
                            m emo-13 "У мен денег нет. Можешь заплатить?"
                            ka emo-158 "..."
                            $ date_kate -= 1
                        "Оплатить по полам":
                            $ stripgirlm2 += 300
                            m emo-13 "Может поделим счёт по полам?"
                            ka emo-157 "Хорошо. Давай сделаем так."
                            $ currency -= 150
                            $ screennotify("$", 11, 150)
                    scene pgn_club_date_kate_27
                    if (kate_path >= 3.5 and (("свидкатя_максплатит_стриптиз") in ivent24 or ("свидкатя_максплатит_бар") in ivent24)) or (("свидкатя_максплатит_стриптиз") in ivent24 and ("свидкатя_максплатит_бар") in ivent24):
                        scene pgn_club_date_kate_28
                    $ renpy.pause()
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
                        scene pgn_club_date_kate_27
                        if (kate_path >= 3.5 and (("свидкатя_максплатит_стриптиз") in ivent24 or ("свидкатя_максплатит_бар") in ivent24)) or (("свидкатя_максплатит_стриптиз") in ivent24 and ("свидкатя_максплатит_бар") in ivent24):
                            scene pgn_club_date_kate_28
                        $ renpy.pause()
                        scene pgn_club_striptease_girl2_07
                        $ renpy.pause()
                        scene pgn_club_striptease_girl2_08
                        $ renpy.pause()
                    if stripgirlm1 >= 150 and stripgirlm1 < 500:
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
                        scene pgn_club_date_kate_27
                        if (kate_path >= 3.5 and (("свидкатя_максплатит_стриптиз") in ivent24 or ("свидкатя_максплатит_бар") in ivent24)) or (("свидкатя_максплатит_стриптиз") in ivent24 and ("свидкатя_максплатит_бар") in ivent24):
                            scene pgn_club_date_kate_28
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
                        scene pgn_club_date_kate_27
                        if (kate_path >= 3.5 and (("свидкатя_максплатит_стриптиз") in ivent24 or ("свидкатя_максплатит_бар") in ivent24)) or (("свидкатя_максплатит_стриптиз") in ivent24 and ("свидкатя_максплатит_бар") in ivent24):
                            scene pgn_club_date_kate_28
                        $ renpy.pause()
                        scene pgn_club_striptease_girl2_15
                        $ renpy.pause()
                        scene pgn_club_striptease_girl2_16
                        $ renpy.pause()
                        scene pgn_club_striptease_girl2_17
                        $ renpy.pause()
        "Домой на такси" if ("клуб_макс_алкоголь") in ivent24:
            call pgn_events_13_club_datekate_end from _call_pgn_events_13_club_datekate_end
            scene animated pgn_transp_city_taxi_night
            $ renpy.pause(5, hard=True)
            if transport1.use != True and transport2.use != True:
                $ currency -= 50
                $ screennotify("$",18,50)
            jump loc_pool
    scene pgn_club_date_kate_08
    ka emo-152 "Спасибо тебе."
    m emo-3 "В следующую пятницу?"
    ka emo-159 "Да. Буду ждать от тебя сообщения."
    call pgn_events_13_club_datekate_end from _call_pgn_events_13_club_datekate_end_1
    if kate_path == 3.7:
        jump pgn_events_13_momkate_06
    jump loc_club_dancefloor_01

label pgn_events_13_club_datekate_pay:
    menu pgn_club_datekate_paym:
        "Оплатить за себя и Катю":
            m emo-3 "Я оплачу."
            ka emo-152 "Ох! Спасибо. Из тебя бы вышел хороший парень."
            $ date_kate += 1
            $ currency -= clubdrink_max+clubdrink_kate
            $ screennotify("$", 11, str(clubdrink_max+clubdrink_kate))
            $ clubdrink_max = clubdrink_kate = 0
            $ ivent24.append("свидкатя_максплатит_бар")
        "Каждый за себя":
            m emo-0 "Каждый за себя оплачивает. Да? У нас ж всё понарошку."
            ka emo-157 "Дааа..."
            $ currency -= clubdrink_max
            $ screennotify("$", 11, str(clubdrink_max))
            $ clubdrink_max = 0
        "Денег нет" if kate_path < 3.6:
            m emo-5 "Эм... я забыл взять свой бумажник."
            ka emo-155 "..."
            $ date_kate -= 1
            $ clubdrink_max = clubdrink_kate = 0
    return

label pgn_events_13_club_datekate_end:
    $ qtime += 2

    if kate_path == 3.2:
        $ kate_path = 3.3
    elif kate_path == 3.3:
        $ kate_path = 3.4
    elif kate_path == 3.4:
        $ kate_path = 3.5

    if kate_path == 3.4 and date_kate < 4:
        $ kate_path = 3.3
    if kate_path == 3.5 and date_kate < 6:
        $ kate_path = 3.4
    return


label pgn_events_13_momkate_05:
    scene black with dissolve
    $ renpy.pause(4)
    scene pgn_club_momkate_01_bar
    m emo-9 "{i}Эм... Что я тут делаю?{/i}"
    scene pgn_club_momkate_03_bar
    $ renpy.pause(5)
    scene pgn_club_momkate_04_bar
    momk emo-321 "Привет [pname_max[0]]."
    m emo-0 "Здравствуйте."
    momk emo-320 "Я наблюдала за вами. [pname_alice[0]] была рядом, но Катя совсем не смотрела на неё, а смотрела только на тебя и была только с тобой. Про [pname_alice[3]] она уже мало что говорит. Молодец."
    m emo-13 "Спасибо."
    momk emo-325 "А вне клуба встречаетесь? Что делаете дома? Вы вместе спите или она всё ещё с [pname_alice[4]]?"
    m emo-2 "{i}Блин! Она поняла, что мы притворяемся!?{/i}"
    momk emo-324 "[pname_max[0]]?"
    m emo-1 "Ах, да... т.е. нет. Эм... мы вместе спим... в одной кровати."
    scene pgn_club_momkate_06_bar
    momk emo-321 "Сейчас у вас, молодёжи, модно постоянно делать фотографии. Может покажите мне, как вы проводите время вместе, у тебя дома?"
    m emo-0 "Эм да, конечно, хорошо, я сделаю."
    momk emo-321 "Буду ждать."
    $ momkate_path = 4
    jump jump_dialogue


label pgn_events_13_aliceandkate_02:
    $ kate_path = 3.6
    scene pgn_events_13_aliceroom_alicekate_01
    a emo-20 "Она обо всём узнала?"
    m emo-0 "Вроде нет."
    a emo-20 "А что тогда?"
    m emo-0 "Она попросила прислать несколько фотографий с Катей."
    a emo-22 "У меня много их на телефоне, могу отправить."
    m emo-13 "Нет, не эти."
    m emo-4 "А есть голые фото?"
    a emo-32 "Обломишься. Тогда какие нужны?"
    m emo-0 "Фотографии, где я с Катей вместе... Где мы вместе спим и что-то делаем, пока она у нас дома."
    ka emo-150 "Надеюсь она не догадываемся, что мы притворяемся. Есть идеи?"
    m emo-6 "Ну... Может быть..."
    menu pgn_events_13_aliceandkate_02m:
        "Ложимся спать":
            m emo-6 "Можем вместе лечь спать. Я твоей маме сказал, что спим вместе, а не раздельно."
            a emo-27 "Чего?"
            m emo-13 "Ладно, ладно. Притворимся, что ложимся спать."
            ka emo-150 "Я приду. Когда мне подойти?"
            $ ivent24.append("событие_катяфотодома_nightsleep")
            menu:
                "Сейчас" if qtime >= 0 and qtime < 6:
                    jump pgn_events_13_katewithmax_nightsleep_next
                "00:00" if qtime >= 20 and qtime <= 23:
                    $ ivent24.append("событие_катяфотодома_nightsleep_0")
                "01:00" if (qtime >= 20 and qtime <= 23) or qtime == 0:
                    $ ivent24.append("событие_катяфотодома_nightsleep_1")
                "02:00" if (qtime >= 20 and qtime <= 23) or qtime == 0 or qtime == 1:
                    $ ivent24.append("событие_катяфотодома_nightsleep_2")
                "03:00" if (qtime >= 20 and qtime <= 23) or (qtime >= 0 and qtime <= 2):
                    $ ivent24.append("событие_катяфотодома_nightsleep_3")
        "Просыпаемся вместе":
            m emo-6 "Можем вместе лечь спать. Я твоей маме сказал, что спим вместе, а не раздельно."
            a emo-27 "Чего?"
            m emo-13 "Ладно, ладно. Притворимся. Можешь утром прийти и сделаем фотографии."
            ka emo-152 "Постараюсь не проспать."
            if ("утро_завтракдома_катя") not in accessiv:
                $ accessiv.append("утро_завтракдома_катя")
            $ accessiv.append("событие_катяфотодома_утровместе")
        "Целуемся на веранде":
            m emo-6 "Можем на веранде поцеловаться."
            a emo-27 "А больше ничего не хочется?"
            ka emo-150 "[pname_max[0]], я не могу. Может быть, потом, но не сейчас."
            m emo-0 "Ладно. Тогда..."
            jump pgn_events_13_aliceandkate_02m
        "ТВ перед сном":
            m emo-6 "Можно перед сном посмотреть телевизор. Типа романтика."
            a emo-20 "И чего тут романтичного?"
            ka emo-152 "Я приду. Во сколько?"
            $ ivent24.append("событие_катяфотодома_tv")
            menu:
                "Сейчас" if qtime >= 0 and qtime < 6:
                    jump pgn_events_13_katewithmax_tv_photo
                "00:00" if qtime >= 20 and qtime <= 23:
                    $ ivent24.append("событие_катяфотодома_tv_0")
                "01:00" if (qtime >= 20 and qtime <= 23) or qtime == 0:
                    $ ivent24.append("событие_катяфотодома_tv_1")
                "02:00" if (qtime >= 20 and qtime <= 23) or qtime == 0 or qtime == 1:
                    $ ivent24.append("событие_катяфотодома_tv_2")
        "Загораем":
            m emo-6 "Можем вместе позагорать."
            a emo-22 "Ты в курсе, что сейчас ночь?"
            m emo-0 "Ну так утром же загорают, когда солнце."
            ka emo-152 "Постараюсь прийти, если не просплю."
            if ("утро_завтракдома_катя") not in accessiv:
                $ accessiv.append("утро_завтракдома_катя")
            $ accessiv.append("событие_катяфотодома_sunyoga")
    $ qtime += 1
    jump loc_my_room

label pgn_events_13_katephoto_dialogue:
    m emo-3 "Сделаем ещё несколько фотографий?"
    ka emo-152 "Что предлагаешь?"
    menu pgn_events_13_katephoto_dialoguem:
        "Ложимся спать" if ("катядомфото_nightsleep") not in accessiv:
            m emo-6 "Можем вместе лечь спать. Я твоей маме сказал, что спим вместе, а не раздельно. Притворимся, что ложимся спать."
            ka emo-150 "Я приду. Когда мне подойти?"
            $ ivent24.append("событие_катяфотодома_nightsleep")
            menu:
                "Можно сейчас" if qtime >= 0 and qtime < 6:
                    jump pgn_events_13_katewithmax_nightsleep_next
                "00:00" if qtime >= 20 and qtime <= 23:
                    $ ivent24.append("событие_катяфотодома_nightsleep_0")
                "01:00" if (qtime >= 20 and qtime <= 23) or qtime == 0:
                    $ ivent24.append("событие_катяфотодома_nightsleep_1")
                "02:00" if (qtime >= 20 and qtime <= 23) or qtime == 0 or qtime == 1:
                    $ ivent24.append("событие_катяфотодома_nightsleep_2")
                "03:00" if (qtime >= 20 and qtime <= 23) or (qtime >= 0 and qtime <= 2):
                    $ ivent24.append("событие_катяфотодома_nightsleep_3")
        "Просыпаемся вместе" if ("катядомфото_mornigbed") not in accessiv:
            m emo-6 "Можешь утром прийти ко мне и сделаем фотографии. Как будто вместе в одной кровате проснулись."
            ka emo-152 "Постараюсь не проспать."
            if ("утро_завтракдома_катя") not in accessiv:
                $ accessiv.append("утро_завтракдома_катя")
            $ accessiv.append("событие_катяфотодома_утровместе")
        "На веранде" if ("катядомфото_kissveranda") not in accessiv:
            m emo-6 "Можем на веранде, перед завтраком сделать фото."
            if ("катядомфото_nightsleep") in accessiv and ("катядомфото_morningbed") in accessiv and ("катядомфото_tv") in accessiv and ("катядомфото_sunyoga") in accessiv:
                ka emo-152 "Буду тебя ждать."
                if ("утро_завтракдома_катя") not in accessiv:
                    $ accessiv.append("утро_завтракдома_катя")
                $ accessiv.append("событие_катяфотодома_kissveranda")
            else:
                ka emo-150 "[pname_max[0]], я не могу. Может быть, потом, но не сейчас."
        "ТВ перед сном" if ("катядомфото_tv") not in accessiv:
            m emo-6 "Можно перед сном посмотреть телевизор. Типа романтика."
            ka emo-152 "Я приду. Во сколько?"
            $ ivent24.append("событие_катяфотодома_tv")
            menu:
                "Сейчас" if qtime >= 0 and qtime < 6:
                    jump pgn_events_13_katewithmax_tv_photo
                "00:00" if qtime >= 20 and qtime <= 23:
                    $ ivent24.append("событие_катяфотодома_tv_0")
                "01:00" if (qtime >= 20 and qtime <= 23) or qtime == 0:
                    $ ivent24.append("событие_катяфотодома_tv_1")
                "02:00" if (qtime >= 20 and qtime <= 23) or qtime == 0 or qtime == 1:
                    $ ivent24.append("событие_катяфотодома_tv_2")
        "Загораем" if ("катядомфото_sunyoga") not in accessiv:
            m emo-6 "Можем вместе утром, до того как мама займётся своей йогой, позагорать."
            ka emo-152 "Постараюсь прийти, если не просплю."
            if ("утро_завтракдома_катя") not in accessiv:
                $ accessiv.append("утро_завтракдома_катя")
            $ accessiv.append("событие_катяфотодома_sunyoga")
    jump jump_dialogue



label pgn_events_13_katewithmax_nightsleep:
    if kate_path == 3.6 and pgn_ach_repeat == 0:
        scene pgn_events13_hone_katewithmax_04
        ka emo-150 "Я пришла."
        m emo-3 "Отлично. А чего ты одетая?"
        ka emo-154 "У [pname_alice[1]] одолжила... А вот ты и..."
        label pgn_events_13_katewithmax_nightsleep_next:
            scene pgn_events13_hone_katewithmax_05
            ka emo-154 "Твоя сестра тоже голая. В одной комнате брат с сестрой и совсем голые спят?!"
            m emo-4 "Да. А нам нечего стесняться."
            ka emo-153 "И правда... Сниму лифчик."
            scene pgn_events13_hone_katewithmax_06
            m emo-3 "Ложись ко мне ближе."
            ka emo-150 "Лучше притворись спящим."
            ka emo-150 "..."
            m emo-0 "Ладно."
            scene pgn_events13_hone_katewithmax_07
            $ renpy.pause()
            scene pgn_events13_hone_katewithmax_08
            $ renpy.pause()
            scene pgn_events13_hone_katewithmax_09
            m emo-9 "Куда ты?"
            ka emo-152 "Я сделала, что нужно. На большее не рассчитывай."
            m emo-2 "Блин! Я думал ты останешься."
            $ accessiv.append("катядомфото_nightsleep")
            jump loc_my_room_sleep
    else:
        scene pgn_events13_hone_katewithmax_10
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_11
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_12
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_13
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_14
        m emo-7 "Ммм... [pname_alice[0]]... Братик тебя согреет."
        ka emo-151 "{i}Разве мы так похожи с ней?{/i}"
        if renpy.random.randint ( 1, 2) == 2:
            ka emo-158 "{i}Не могу заснуть, очень странное ощущение, словно...{/i}"
            scene pgn_events13_hone_katewithmax_15
            ka emo-151 "{i}Понятно. Заявилась на чужую территорию.{/i}"
            scene pgn_events13_hone_katewithmax_16
            $ renpy.pause()
        scene pgn_events13_hone_katewithmax_17
        $ PGN_Achadd(pgnach_168, 168)
        m emo-4 "{i}Вот это сюрприз.{/i}"
        $ scene_random = 0
        menu pgn_events_13_katewithmax_nightsleepm:
            "Потрогать сиську":
                $ scene_random += 1
                scene pgn_events13_hone_katewithmax_18
                m emo-3 "{i}Мягкая...{/i}"
                if scene_random != 3:
                    jump pgn_events_13_katewithmax_nightsleepm
            "Засунуть палец в рот":
                $ scene_random += 1
                scene pgn_events13_hone_katewithmax_19
                m emo-5 "Открой ротик..."
                scene pgn_events13_hone_katewithmax_20
                $ renpy.pause()
                if scene_random != 3:
                    jump pgn_events_13_katewithmax_nightsleepm
            "Потрогать живот":
                $ scene_random += 1
                scene pgn_events13_hone_katewithmax_21
                m emo-4 "{i}Теплый животик.{/i}"
                if scene_random != 3:
                    jump pgn_events_13_katewithmax_nightsleepm
            "Потрогать киску":
                $ scene_random += 1
                scene pgn_events13_hone_katewithmax_22
                $ renpy.pause()
                if scene_random != 3:
                    menu:
                        "Засунуть палец в киску":
                            scene pgn_events13_hone_katewithmax_23
                            m emo-3 "{i}Влажно и горячо.{/i}"
                        "назад":
                            jump pgn_events_13_katewithmax_nightsleepm
        scene pgn_events13_hone_katewithmax_24
        ka emo-152 "С добрым утром. Уже проснулся."
        m emo-3 "И не только я, но и мой друг. Мы оба рады такому сюрпризу."
        ka emo-153 "У [pname_alice[1]] стало прохладно, а в гостиной диван занят."
        scene pgn_events13_hone_katewithmax_25_01
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_25_02
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_25_03
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_25_02
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_25_01
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_25_02
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_25_03
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_26
        m emo-12 "Аррргххх!"
        m emo-4 "Спасибо."
        ka emo-152 "Отдыхай, а я в душ."
        if pgn_ach_repeat != 0:
            jump table_pgn_achievement
        $ PGN_Addstatsex(stat_kate, 0, 0, 0, 0, 1)
        if kate_path == 3.6:
            call max_sleep_reset from _call_max_sleep_reset_11
            $ qtime = 7
        else:
            scene black with dissolve
            $ renpy.pause(3)
            $ qtime = 8
        jump loc_my_room

label pgn_events_13_katewithmax_morningbed:
    if ("катяждётутромвкомнате") not in ivent24:
        scene pgn_events13_hone_katewithmax_27
        m emo-3 "Готова к нашей фотосессии?"
        ka emo-150 "Ни о какой фотосессии речи не шло, нужна одна фотография."
        m emo-0 "Да, точно. "
    else:
        scene pgn_events13_hone_katewithmax_28
        ka emo-151 "Я уже заждалась. Давай быстрее."
    m emo-6 "Может быть разденешься?"
    ka emo-151 "Зачем?"
    m emo-13 "Твоя Мама поверит, что ты спишь в белье?"
    ka emo-156 "Ох ладно."
    scene pgn_events13_hone_katewithmax_29
    $ renpy.pause()
    $ accessiv.append("катядомфото_mornigbed")
    if ("событие_катяфотодома_утровместе") in accessiv:
        $ accessiv.remove("событие_катяфотодома_утровместе")
    $ accessiv.append("катядомфото_morningbed")
    jump loc_my_room

label pgn_events_13_katewithmax_kissveranda:
    if kate_path == 3.6:
        scene pgn_events13_hone_katewithmax_30
        m emo-3 "Ну что, готова?"
        ka emo-150 "Да. Давай побыстрее это сделаем."
        scene pgn_events13_hone_katewithmax_31
        $ renpy.pause()
        $ accessiv.append("катядомфото_kissveranda")
    else:
        m emo-4 "Можно мне составить тебе компанию?"
        ka emo-152 "Садись."
        scene pgn_events13_hone_katewithmax_32
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_33
        $ renpy.pause()
        $ qtime += 1
    if ("событие_катяфотодома_kissveranda") in accessiv:
        $ accessiv.remove("событие_катяфотодома_kissveranda")
    jump veranda_breakfast

label pgn_events_13_katewithmax_tv:
    scene pgn_events13_hone_katewithmax_34
    menu pgn_events_13_katewithmax_tv_m0:
        "Присоединиться":
            m emo-6 "Можно с тобой посмотреть?"
            ka emo-150 "Это ты здесь живёшь, так что тебе всё можно. Присаживайся."
            scene pgn_events13_hone_katewithmax_35
            $ renpy.pause()
            menu pgn_events_13_katewithmax_tv_m1:
                "Ещё посидеть посмотреть":
                    if kate_path == 3.6:
                        scene pgn_events13_hone_katewithmax_35
                        $ qtime += 1
                        $ renpy.pause()
                        if qtime == 3:
                            scene pgn_events13_hone_katewithmax_41
                            k emo-104 "Приветики. А почему не спим? Уже позднее время, пора ложиться спать."
                            menu:
                                "Согласиться":
                                    pass
                                "Мы уже взрослые":
                                    scene pgn_events13_hone_katewithmax_42
                                    ka emo-152 "[pname_max[0]]! Твоя тётя к тебе обращалась. Я с ней согласна, тебе пора уже спать."
                                    m emo-1 "Но..."
                                    k emo-103 "Давай, давай, поднимай свою попу с дивана, пока твоя мама не пришла и не наругала."
                                    m emo-0 "Блин!"
                            jump loc_my_room_sleep
                        else:
                            jump pgn_events_13_katewithmax_tv_m1
                    else:
                        scene pgn_events13_hone_katewithmax_36
                        menu pgn_events_13_katewithmax_tv_m2:
                            "Посмотреть на киску":
                                label pgn_events_13_katewithmax_tv_pussy:
                                    scene pgn_events13_hone_katewithmax_38
                                    m emo-3 "{i}Сейчас бы её трахнул.{/i}"
                                    menu:
                                        "Трахнуть":
                                            scene pgn_events13_hone_katewithmax_43
                                            ka emo-159 "Эй! [pname_max[0]]! Ты чего это?"
                                            m emo-0 "Хочу секса."
                                            if alice_sex_kate == 3 and pgn_ach_repeat == 0:
                                                ka emo-152 "У тебя недавно был секс."
                                                m emo-3 "А я постоянно этого хочу."
                                            label pgn_events_13_katewithmax_tv_sex:
                                                if pgn_ach_repeat == 0:
                                                    $ qtime = 3
                                                if stat_kate.stsex_anal < stat_alice.stsex_anal and pgn_ach_repeat == 0:
                                                    ka emo-153 "Давай. Но только анал. В попке [pname_alice[1]] ты был чаще, чем в моей."


                                                menu:
                                                    "Анал":
                                                        label pgn_events_13_katewithmax_tv_anal:
                                                            scene pgn_events13_hone_katewithmax_44
                                                            m emo-3 "{i}Рабочая попка. Вошёл легко.{/i}"
                                                            scene pgn_events13_hone_katewithmax_45
                                                            $ renpy.pause()
                                                            scene pgn_events13_hone_katewithmax_46_01
                                                            ka emo-152 "..."
                                                            scene pgn_events13_hone_katewithmax_46_15
                                                            ka emo-154 "Аах..."
                                                            scene pgn_events13_hone_katewithmax_46_01
                                                            ka emo-152 "..."
                                                            scene pgn_events13_hone_katewithmax_46_15
                                                            ka emo-154 "Аах..."
                                                            scene pgn_events13_hone_katewithmax_45
                                                            m emo-10 "Сейчас кончу!"
                                                            ka emo-154 "В попку, кончи мне в внутрь!"
                                                            menu:
                                                                "В попу":
                                                                    scene pgn_events13_hone_katewithmax_47
                                                                    m emo-12 "Аррргххх!!!"
                                                                    scene pgn_events13_hone_katewithmax_48
                                                                    $ renpy.pause()
                                                                    scene pgn_events13_hone_katewithmax_49
                                                                    m emo-3 "Твоя попка немного испачкалась."
                                                                    ka emo-152 "Придётся тебя оставить и бежать в душ. Спасибо."
                                                                "На спину":
                                                                    scene pgn_events13_hone_katewithmax_50
                                                                    m emo-12 "Аррргххх!!!"
                                                                    scene pgn_events13_hone_katewithmax_51
                                                                    m emo-3 "Как тебе мои теплые сливки на твоём теле?"
                                                                    ka emo-156 "[pname_max[0]]..."
                                                                    scene pgn_events13_hone_katewithmax_52
                                                                    ka emo-150 "Доволен?"
                                                                    m emo-3 "Ага"
                                                                    ka emo-152 "Приятных снов, а я пойду, мне срочно в душ."
                                                            if pgn_ach_repeat != 0:
                                                                jump table_pgn_achievement
                                                            $ PGN_Addstatsex(stat_kate, 1, 0, 0, 0, 0)
                                                    "Вагинал":
                                                        scene pgn_events13_hone_katewithmax_53
                                                        $ renpy.pause()
                                                        scene pgn_events13_hone_katewithmax_54
                                                        ka emo-154 "Ахх... Большой..."
                                                        m emo-3 "{i}Катя глубоко насаживается{/i}"
                                                        scene pgn_events13_hone_katewithmax_55
                                                        $ PGN_Achadd(pgnach_170, 170)
                                                        ka emo-154 "Ааахх... Ахх... Ааххх..."
                                                        m emo-10 "..."
                                                        ka emo-154 "[pname_max[0]], подожди, не кончай..."
                                                        m emo-10 "... Аррргххх!!!"
                                                        scene pgn_events13_hone_katewithmax_56
                                                        ka emo-156 "..."
                                                        scene pgn_events13_hone_katewithmax_57
                                                        m emo-9 "Ты же на таблетках?"
                                                        ka emo-152 "Да. С тобой нужно быть всегда наготове."
                                                        if pgn_ach_repeat != 0:
                                                            jump table_pgn_achievement
                                                        $ PGN_Addstatsex(stat_kate, 0, 0, 0, 1, 0)
                                        "Продолжить" if pgn_ach_repeat == 0:
                                            $ qtime = 3
                                            $ renpy.pause()
                                            ka emo-150 "Я пойду спать. Спокойной ночи."
                                            m emo-1 "И тебе того же."
                                            scene pgn_events13_hone_katewithmax_61
                                            jump pgn_events_13_katewithmax_tv_kira
                            "Продолжить":
                                scene pgn_events13_hone_katewithmax_37
                                $ renpy.pause()
                                scene pgn_events13_hone_katewithmax_58
                                $ renpy.pause()
                                scene pgn_events13_hone_katewithmax_59
                                ka emo-151 "Хочешь кончить?"
                                menu:
                                    "Может секс?":
                                        m emo-13 "Может сексом займёмся?"
                                        if renpy.random.randint ( 1, 3) == 1:
                                            jump pgn_events_13_katewithmax_tv_sex
                                        else:
                                            jump pgn_events_13_katewithmax_tv_leave
                                    "Да":
                                        $ label_random, qtime = renpy.random.randint ( 1, 3), 3
                                        if kateorder > 0:
                                            scene pgn_events13_hone_katewithmax_64
                                            m emo-10 "Сейчас кончу. Катя, Катя! Я..."
                                            scene pgn_events13_hone_katewithmax_65
                                            m emo-9 "Ааа! Блин!"
                                            scene pgn_events13_hone_katewithmax_66
                                            m emo-9 "Я кончил на себя!"
                                            ka emo-159 "Хахаха."
                                            m emo-2 "Ничего смешного."
                                            ka emo-157 "В следующий раз будешь меня слушать."
                                            scene pgn_events13_hone_katewithmax_60
                                            m emo-9 "Ты о чём?"
                                            ka emo-152 "Спокойной ночи."
                                            scene pgn_events13_hone_katewithmax_61
                                            $ kateorder = 0
                                            if daysn == 2 or daysn == 4 or daysn == 7:
                                                k emo-101 "Ой, [pname_max[0]]! А ты чего здесь?"
                                                if daysn == 7:
                                                    scene pgn_events13_hone_katewithmax_63
                                                    show pgn_events13_hone_katewithmax_62_cum
                                                else:
                                                    scene pgn_events13_hone_katewithmax_62
                                                    show pgn_events13_hone_katewithmax_63_cum
                                                m emo-1 "А эм..."
                                                k emo-103 "Мммм... Малыш, ты меня ждал и не дождался?"
                                                m emo-13 "Ну это..."
                                                k emo-101 "Вставай, иди в ванную и тебе уже пора ложиться спать."
                                                m emo-0 "{i}Блин!{/i}"
                                            $ PGN_Addstatsex(stat_kate, 0, 0, 0, 0, 1)
                                        elif label_random == 2:
                                            label pgn_events_13_katewithmax_tv_leave:
                                                scene pgn_events13_hone_katewithmax_60
                                                m emo-9 "Эээ... Ты куда? А как же мне помочь?"
                                                ka emo-152 "Я устала и хочу спать. Помоги себе сам."
                                                scene pgn_events13_hone_katewithmax_61
                                                m emo-2 "Блин! И как теперь мне быть."
                                                label pgn_events_13_katewithmax_tv_kira:
                                                    if daysn == 2 or daysn == 4:
                                                        k emo-101 "Ой, [pname_max[0]]! А ты чего здесь?"
                                                        scene pgn_events13_hone_katewithmax_62
                                                        m emo-1 "А эм..."
                                                        k emo-104 "Аааа... [pname_liza[0]] выгнала?"
                                                        m emo-11 "Ничего она меня не выгнала."
                                                        k emo-100 "М... Ясно."
                                                        menu:
                                                            "Идти спать":
                                                                pass
                                                            "Остаться":
                                                                jump menu_living_room_kira_night_next
                                                    elif daysn == 7:
                                                        scene pgn_events13_hone_katewithmax_63
                                                        k emo-101 "Меня ждёшь?"
                                                        m emo-9 "А, [pname_kira[0]]! Привет."
                                                        menu:
                                                            "Идти спать":
                                                                pass
                                                            "Остаться":
                                                                jump menu_living_room_kira_night_next
                                        else:
                                            scene pgn_events13_hone_katewithmax_64
                                            m emo-7 "Катя, я почти, уже, сейчас..."
                                            scene pgn_events13_hone_katewithmax_67
                                            m emo-10 "Ааргх..."
                                            scene pgn_events13_hone_katewithmax_68
                                            m emo-3 "Спасибо..."
                                            $ PGN_Addstatsex(stat_kate, 0, 0, 0, 0, 1)
                "Фото" if ("катядомфото_tv") not in accessiv:
                    label pgn_events_13_katewithmax_tv_photo:
                        scene pgn_events13_hone_katewithmax_35
                        $ accessiv.append("катядомфото_tv")
                        ka emo-151 " И как предлагаешь сделать?"
                        menu pgn_events_13_katewithmax_tv_m3:
                            "Сядь на коленки":
                                m emo-6 "Можешь сесть ко мне на колени."
                                ka emo-150 "На фото нужно показать, как мы вместе смотрим и что ты за моей спиной увидишь?"
                                m emo-4 "Твою спину и попку."
                                ka emo-150 "Не подходит."
                                jump pgn_events_13_katewithmax_tv_m3
                            "Как сидим":
                                m emo-0 "Я думаю и так сойдёт, как сидим."
                                ka emo-150 "Это не похоже на то, что мы пара."
                                jump pgn_events_13_katewithmax_tv_m3
                            "Обнять сзади":
                                m emo-3 "Ты или я могу зайти сзади за диван и обнять."
                                ka emo-150 "Не то."
                                m emo-6 "{i}Нормально. Что не так?!{/i}"
                                jump pgn_events_13_katewithmax_tv_m3
                            "Секс на диване":
                                m emo-3 "Может притвориться, что занимаемся сексом?"
                                ka emo-155 "[pname_max[0]]! Я... Я не буду отправлять своей маме фото, как мы занимаемся сексом."
                                m emo-0 "Ну так не по-настоящему, а как бы. И на фото всё равно ты будешь голой."
                                ka emo-150 "Нет"
                                jump pgn_events_13_katewithmax_tv_m3
                            "Ляг на колени":
                                m emo-0 "Можешь просто лечь на мои колени."
                                ka emo-152 "Согласна."
                                scene pgn_events13_hone_katewithmax_39
                                $ renpy.pause()
                            "Ко мне на ручки":
                                m emo-0 "Сядешь ко мне на коленки, а я тебя руками буду поддерживать."
                                ka emo-151 "Сложно представить... Хорошо, показывай как и делаем фото."
                                scene pgn_events13_hone_katewithmax_40
                                $ renpy.pause()
                        $ qtime += 1
                "уйти":
                    scene pgn_events13_hone_katewithmax_34
                    call screen location_living_room
        "Фото" if ("катядомфото_tv") not in accessiv:
            if renpy.random.randint ( 1, 3) == 3:
                m emo-0 "Ну что, сфоткаемся?"
                ka emo-152 "Садись."
                scene pgn_events13_hone_katewithmax_35
                jump pgn_events_13_katewithmax_tv_photo
            m emo-3 "Ну что, сделаем совместное фото?"
            ka emo-150 "Пока нет. Тут фильм интересный."
            m emo-13 "Значит мне потом прийти?"
            ka emo-150 "Сядь и жди."
            m emo-0 "Ладно."
            ka emo-155 "И помолчи."
            scene pgn_events13_hone_katewithmax_36
            $ renpy.pause(5, hard=True)
            jump pgn_events_13_katewithmax_tv_photo
        "уйти":
            call screen location_living_room
    if qtime > 3:
        $ qtime = 3
    jump loc_my_room_sleep

label pgn_events_13_katewithmax_sunyoga:
    if kate_path == 3.6:
        $ accessiv.append("катядомфото_sunyoga")
        scene pgn_events13_hone_katewithmax_69
        ka emo-150 "Я пришла. И..."
        m emo-0 "Пока мама не пришла ложись со мной."
        ka emo-150 "Я не буду лежать с тобой на одной кушетке."
        m emo-0 "Ладно, ладно, на разных, но рядом."
        scene pgn_events13_hone_katewithmax_70
        m emo-3 "И ещё один снимок."
        ka emo-150 "Одного снимка достаточно."
        m emo-0 "Сама потом выберешь, какой отправить."
        scene pgn_events13_hone_katewithmax_71
        $ renpy.pause()
        scene pgn_events13_hone_katewithmax_72
        mom emo-60 "Я вам не помешаю?"
        scene pgn_events13_hone_katewithmax_73
        m emo-0 "А, Мам! Ты пришла заниматься?"
        mom emo-60 "Ты же знаешь, я каждый день."
        scene pgn_events13_hone_katewithmax_74
        mom emo-62 "А вы тут чем занимались?"
        m emo-0 "Эм..."
        ka emo-152 "Решила немного позагорать. Извините, что без одежды, у вас в гостях и..."
        mom emo-60 "Ничего страшного. [pname_max[0]], а ты чего тут?"
        m emo-0 "Ну я..."
        ka emo-152 "Он помог мне сделать несколько личных фотографий."
        mom emo-62 "Ясно. [pname_max[0]], поможешь мне убрать кушетки?"
        if (Max.strength[3] + Max.strength[4]) < 7:
            scene pgn_events13_hone_katewithmax_75
        else:
            scene pgn_events13_hone_katewithmax_76
        $ renpy.pause()
        $ accessiv.remove("событие_катяфотодома_sunyoga")
    else:
        label pgn_events_13_katewithmax_sunyoga_v2:
            scene pgn_events13_hone_katewithmax_77
            menu pgn_events_13_katewithmax_sunyoga_m1:
                "Подойти ближе" if pgn_ach_repeat == 0:
                    scene pgn_events13_hone_katewithmax_78
                    $ renpy.pause()
                    $ scene_random = 0
                    menu pgn_events_13_katewithmax_sunyoga_m2:
                        "Киска":
                            scene pgn_events13_hone_katewithmax_79
                            $ renpy.pause()
                            $ scene_random += 1
                            if scene_random == 2:
                                pass
                            else:
                                jump pgn_events_13_katewithmax_sunyoga_m2
                        "Сиськи":
                            scene pgn_events13_hone_katewithmax_80
                            $ renpy.pause()
                            $ scene_random += 1
                            if scene_random == 2:
                                pass
                            else:
                                jump pgn_events_13_katewithmax_sunyoga_m2
                        "Рот":
                            scene pgn_events13_hone_katewithmax_82
                            $ renpy.pause()
                            $ scene_random += 1
                            if scene_random == 2:
                                pass
                            else:
                                jump pgn_events_13_katewithmax_sunyoga_m2
                        "Просто смотреть на неё":
                            scene pgn_events13_hone_katewithmax_81
                            $ renpy.pause()
                            $ scene_random += 1
                            if scene_random == 2:
                                pass
                            else:
                                jump pgn_events_13_katewithmax_sunyoga_m2
                        "уйти":
                            scene pgn_events13_hone_katewithmax_77
                            call screen location_pool
                    ka emo-157 "[pname_max[0]], уйди! Не мешай мне загорать."
                "Лечь рядом":
                    scene pgn_events13_hone_katewithmax_83
                    $ renpy.pause()
                    scene pgn_events13_hone_katewithmax_80
                    $ renpy.pause()
                    scene pgn_events13_hone_katewithmax_82
                    $ renpy.pause()
                    menu:
                        "Загорать":
                            pass
                        "Сиськи":
                            scene pgn_events13_hone_katewithmax_80
                            $ renpy.pause()
                        "Рот":
                            scene pgn_events13_hone_katewithmax_82
                            $ renpy.pause()
                    scene pgn_events13_hone_katewithmax_84
                    $ renpy.pause()
                    scene pgn_events13_hone_katewithmax_85
                    $ renpy.pause()
                    scene black with dissolve
                    $ renpy.pause(5)
                    $ label_random = renpy.random.randint ( 2, 4)
                    if label_random == 4:
                        ka emo-157 "[pname_max[0]]! Ты опять стоишь, я же попросила тебя... Ой!"
                        scene pgn_events13_hone_katewithmax_86
                        m emo-1 "А, Мама, ты пришла заниматься йогой?"
                        scene pgn_events13_hone_katewithmax_87
                        mom emo-73 "Да. Не хотела вам мешать, думала..."
                    else:
                        mom emo-71 "Слишком долго лежать вредно. Может разомнётесь со мной немного?"
                        scene pgn_events13_hone_katewithmax_88
                        m emo-9 "А, Мама!"
                    ka emo-152 "Присоединитесь?"
                    menu:
                        "Я пойду" if pgn_ach_repeat == 0:
                            m emo-13 "Я пойду, а то чёт всё затекло."
                            mom emo-75 "Со мной не позанимаешься?"
                            m emo-0 "Нет, может потом."
                            $ qtime += 1
                        "Присоединяйся":
                            if pgn_ach_repeat == 0:
                                $ qtime = 8
                            m emo-3 "Да, Мам, давай тоже с нами полежишь, позагораешь."
                            mom emo-60 "[pname_max[0]], ты же знаешь, что я слежу за своей формой каждый день."
                            ka emo-151 "По вам это видно, наверное от мужчин отбоя нет."
                            m emo-11 "{i}Я её единственный мужчина, больше ей никто не нужен.{/i}"
                            mom emo-67 "Ой! Спасибо."
                            m emo-0 "Ведь ничего плохо не случится, если один день пропустишь."
                            mom emo-62 "Хорошо."
                            scene pgn_events13_hone_katewithmax_89
                            $ renpy.pause()
                            scene pgn_events13_hone_katewithmax_90
                            $ renpy.pause()
                            scene pgn_events13_hone_katewithmax_91
                            $ renpy.pause()
                            scene pgn_events13_hone_katewithmax_92
                            m emo-6 "{i}Что она делает?{/i}"
                            scene pgn_events13_hone_katewithmax_93
                            $ renpy.pause()
                            scene pgn_events13_hone_katewithmax_94
                            $ renpy.pause()
                            scene pgn_events13_hone_katewithmax_95
                            m emo-9 "{i}Офигеть! Мама тоже возбудилась.{/i}"
                            scene pgn_events13_hone_katewithmax_96
                            m emo-1 "{i}Что ей нужно от меня?{/i}"
                            menu:
                                "Взяться за руки" if pgn_ach_repeat == 0:
                                    scene pgn_events13_hone_katewithmax_97
                                    m emo-13 "{i}Я что-то не то сделал.{/i}"
                                    ka emo-151 "Кажется [pname_max[0]] перегрелся."
                                    mom emo-60 "[pname_max[0]], аккуратно вставай и иди в дом."
                                "Я всё" if pgn_ach_repeat == 0:
                                    m emo-0 "Я всё."
                                    mom emo-60 "Хорошо, милый, иди в дом."
                                "Лечь ближе":
                                    scene pgn_events13_hone_katewithmax_98
                                    m emo-0 "{i}О чём она думает. Моя мама же рядом.{/i}"
                                    scene pgn_events13_hone_katewithmax_99
                                    m emo-10 "Ох, Катя, я....."
                                    scene pgn_events13_hone_katewithmax_100
                                    $ PGN_Achadd(pgnach_169, 169)
                                    m emo-7 "Ай! ААаргх!! Аа..."
                                    scene pgn_events13_hone_katewithmax_101
                                    $ renpy.pause()
                                    scene pgn_events13_hone_katewithmax_102
                                    $ renpy.pause()
                                    if pgn_ach_repeat != 0:
                                        jump table_pgn_achievement
                                    $ PGN_Addstatsex(stat_kate, 0, 0, 0, 0, 1)
                "уйти" if pgn_ach_repeat == 0:
                    call screen location_pool

    if ("событие_катяфотодома_sunyoga") in accessiv:
        $ accessiv.append("событие_катяфотодома_sunyoga")
    jump loc_pool


label pgn_events_13_shower_katealicekira:
    menu:
        "Продолжить наблюдать":
            $ label_random = renpy.random.randint ( 10, 12)
            if label_random == 10 and pgn_ach_repeat == 0:
                scene pgn_events_13_bath_alicekirakate_03_vadx
                $ renpy.pause()
                scene pgn_events_13_bath_alicekirakate_04_vadx
                $ renpy.pause()
                scene pgn_events_13_bath_alicekirakate_05_vadx
                m emo-0 "{i}Похоже мне ни чего не перепадёт.{/i}"
                scene bg door_01
                call screen location_bathroom 
            else:
                scene pgn_events_13_bath_alicekirakate_06_vadx
                $ renpy.pause()
                scene pgn_events_13_bath_alicekirakate_07_vadx
                m emo-6 "{i}О чём они там говорят?{/i}"
                scene pgn_events_13_bath_alicekirakate_08_vadx
                m emo-0 "{i}Ничего не слышно из-за шума воды.{/i}"
                scene pgn_events_13_bath_alicekirakate_09_vadx
                $ PGN_Achadd(pgnach_164, 164)
                m emo-3 "{i}Ого! Попки в ряд.{/i}"
                scene pgn_events_13_bath_alicekirakate_10_vadx
                m emo-6 "{i}Они меня заметили? Если да, тогда может мне стоит зайти или это ловушка?{/i}"
                scene pgn_events_13_bath_alicekirakate_11_vadx
                menu:
                    "Войти":
                        scene pgn_events_13_bath_alicekirakate_12
                        m emo-3 "Привет. А что вы тут делаете и в таких сексуальных позах?"
                        k emo-102 "Мы не могли не заметить, как ты за нами подглядывал и решили устроить тебе сюрприз."
                        ka emo-152 "Выбери любую из этих попок, какую хочешь трахнуть."
                        k emo-103 "Только решай быстрей."
                        menu pgn_events_13_shower_katealicekira_m1:
                            "[pname_alice[0]]":
                                scene pgn_events_13_bath_alicekirakate_24
                                if pgn_ach_repeat == 0:
                                    if renpy.random.randint ( 1, 2) == 1:
                                        ka emo-152 "[pname_max[0]]. [pname_alice[0]] хочет, чтобы ты её трахнул в анал."
                                        $ ivent24.append("катя_приказ_анал")
                                    else:
                                        ka emo-152 "[pname_max[0]]. Заполни её рот спермой"
                                        $ ivent24.append("катя_приказ_врот")
                                a emo-24 "Катя!"
                                ka emo-151 "Ты меня понял?"
                                m emo-13 "Эм... да."
                                k emo-101 "Развлекайтесь."
                                scene pgn_events_13_bath_alicekirakate_25
                                menu:
                                    "В анал":
                                        scene pgn_events_13_bath_alicekirakate_26
                                        a emo-30 "Ааааай... Ммм... Ааххх..."
                                        scene pgn_events_13_bath_alicekirakate_27
                                        a emo-29 "[pname_max[0]], не порви мою попку, ей ещё работать и работать."
                                        m emo-3 "Расслабься, ничего с ней не случится."
                                        scene pgn_events_13_bath_alicekirakate_28
                                        a emo-26 "Аа... Ааах... Ааа..."
                                        scene pgn_events_13_bath_alicekirakate_29
                                        a emo-22 "Аааххх... Ммм... Ахх..."
                                        m emo-10 "Сейчас кончу..."
                                        scene pgn_events_13_bath_alicekirakate_30
                                        m emo-12 "Аррргххх!!!"
                                        scene pgn_events_13_bath_alicekirakate_31
                                        $ renpy.pause()
                                        if pgn_ach_repeat == 0:
                                            if ("катя_приказ_анал") not in ivent24:
                                                $ kateorder += 1
                                            else:
                                                $ kateorder -= 1
                                            $ PGN_Addstatsex(stat_kate, 1, 0, 0, 0, 0)
                                    "Подрочить и кончить в рот":
                                        m emo-0 "Сядь."
                                        scene pgn_events_13_bath_alicekirakate_32
                                        m emo-3 "{i}[pname_alice[0]] послушная. Это из-за Кати или хочет, чтобы я кончил в неё?{/i}"
                                        scene pgn_events_13_bath_alicekirakate_33
                                        $ renpy.pause()
                                        scene pgn_events_13_bath_alicekirakate_34
                                        m emo-10 "Готовься. Я уже почти... Вот вот... Пошло..."
                                        scene pgn_events_13_bath_alicekirakate_35
                                        m emo-12 "Аррргххх!!!"
                                        scene pgn_events_13_bath_alicekirakate_36
                                        m emo-3 "Вкусно?"
                                        a emo-22 "..."
                                        if pgn_ach_repeat == 0:
                                            if ("катя_приказ_врот") not in ivent24:
                                                $ kateorder += 1
                                            else:
                                                $ kateorder -= 1
                            "Катя":
                                m emo-3 "Хочу тебя."
                                ka emo-151 "Только две попки на выбор. Мне потом ещё домой ехать. Так что я пас."
                                jump pgn_events_13_shower_katealicekira_m1
                            "[pname_kira[0]]":
                                scene pgn_events_13_bath_alicekirakate_13
                                k emo-114 "Аааххх! [pname_max[0]]!"
                                ka emo-159 "Мы оставим вас здесь одних. Пойдём [pname_alice[0]], не будем им мешать."
                                scene pgn_events_13_bath_alicekirakate_14
                                k emo-103 "Ммм... Трахнешь тётину киску?"
                                menu pgn_events_13_shower_katealicekira_m2:
                                    "Анал":
                                        m emo-6 "Может анальный секс?"
                                        k emo-101 "Моя попка не подготовлена."
                                        jump pgn_events_13_shower_katealicekira_m2
                                    "Орал":
                                        m emo-6 "Минет?"
                                        k emo-104 "У тебя очень много спермы. Решил меня накормить спермой, а потом получить маминой добавки?"
                                        m emo-0 "Ммм... нет. Я об этом и не думал."
                                        k emo-103 "Так что, может всё же в киску?"
                                        jump pgn_events_13_shower_katealicekira_m2
                                    "Согласиться":
                                        scene pgn_events_13_bath_alicekirakate_15
                                        k emo-114 "Аххх... [pname_max[0]], нежнее и не так быстро."
                                        scene pgn_events_13_bath_alicekirakate_16
                                        $ renpy.pause()
                                        scene pgn_events_13_bath_alicekirakate_17
                                        m emo-3 "{i}Эх жаль нельзя в попку её трахнуть. А то бы сейчас так её сзади.{/i}"
                                        scene pgn_events_13_bath_alicekirakate_18
                                        k emo-114 "Аххх... [pname_max[0]]! Аааххх..... Мммм..."
                                        k emo-103 "Ммм... Ты меня сильно прижал, дышать сложно."
                                        m emo-3 "Ты от меня ни куда не денешься."
                                        k emo-106 "Ммм... Аахх... Ахх..."
                                        scene pgn_events_13_bath_alicekirakate_19
                                        $ renpy.pause()
                                        menu:
                                            "Кончить на неё":
                                                scene pgn_events_13_bath_alicekirakate_20
                                                m emo-12 "Аррргххх!!!"
                                                scene pgn_events_13_bath_alicekirakate_21
                                                $ renpy.pause()
                                            "Кончить в киску":
                                                m emo-12 "Аррргххх!!!"
                                                scene pgn_events_13_bath_alicekirakate_22
                                                k emo-106 "Ох! Малыш. Ты молодец. Хороший мальчик."
                                                scene pgn_events_13_bath_alicekirakate_23
                                                $ renpy.pause()
                                if pgn_ach_repeat == 0:
                                    $ PGN_Addstatsex(stat_kira, 0, 0, 0, 1, 0)
                            "Всех":
                                m emo-4 "Я хочу вас всех."
                                k emo-101 "Нет, так не пойдёт, нам ещё всем на завтрак идти. Времени мало."
                                ka emo-152 "Только одну можешь выбрать."
                                jump pgn_events_13_shower_katealicekira_m1
                    "уйти" if pgn_ach_repeat == 0:
                        scene bg door_01
                        call screen location_bathroom 
        "уйти" if pgn_ach_repeat == 0:
            scene bg door_01
            call screen location_bathroom
    if pgn_ach_repeat != 0:
        jump table_pgn_achievement
    $ qtime = 9
    jump loc_veranda



label pgn_events_13_pool_katekira:
    m emo-3 "Привет"
    scene pgn_poolnight_13_katewithkira_39
    m emo-3 "Чего не спите?"
    k emo-103 "Это мы должны спрашивать. Мы взрослые, а тебе молодому организму нужен сон."
    menu:
        "И секс":
            scene pgn_poolnight_13_katewithkira_40
            m emo-4 "И секс тоже нужен. Особенно перед сном."
            k emo-100 "[pname_max[0]]! Я тебе не раз говорила, что я прихожу уставшей и у меня нет сил на секс."
            scene pgn_poolnight_13_katewithkira_39
            ka emo-155 "Ты постоянно этим занимаешься и всё равно мало?"
            k emo-103 "Он у нас такой, в любой момент хочет что-то и кого-то."
            m emo-0 "Ну так это же, гормоны у меня. Катя, может ты поможешь?"
            ka emo-150 "Я тоже устала. С [pname_alice[4]] многое вытворяли."
            $ ivent24.append("pgn_events_13_pool_katekira_исекс")
        "Не спится":
            ka emo-151 "Почитать книжку перед сном?"
            k emo-101 "..."
            m emo-0 "Нет! Я давно вырос из этого."
            k emo-101 "Уже поздно, иди ложись спать."
    menu:
        "Может хотя бы подрочите?" if ("pgn_events_13_pool_katekira_исекс") in ivent24:
            m emo-13 "Может хотя бы рукой мне подрочите?"
            ka emo-151 "Рукой можем и сам."
            m emo-0 "У меня туннельный синдром, я не могу."
            ka emo-151 "Нет такого синдрома."
            menu:
                "Пожалуйста":
                    m emo-2 "Пожалуйста!"
                    if (renpy.random.randint ( 1, 3) == 2 and kate_path >= 3.7 and kate_path < 4) or kate_path >= 4:
                        ka emo-152 "Хорошо. Пойдём."
                    else:
                        ka emo-150 "Нет"
                        m emo-0 "Но..."
                        k emo-101 "[pname_max[0]], тебе пора спать."
                        jump loc_my_room_sleep
                "Катя. Ты же моя девушка?":
                    $ label_random = renpy.random.randint ( 1, 5)
                    if kate_path >= 4 and label_random != 5:
                        ka emo-152 "Хорошо. Пойдём."
                    else:
                        if kate_path < 4:
                            ka emo-151 "Вообще-то [pname_alice[0]] всё ещё моя девушка, а ты не мой парень."
                        else:
                            ka emo-150 "Нет. Я уже сказа, что устала."
                        menu:
                            "Пожалуйста":
                                m emo-2 "Пожалуйста!"
                                if renpy.random.randint ( 1, 2) == 2 and kate_path >= 3.7:
                                    ka emo-152 "Хорошо. Пойдём."
                                else:
                                    ka emo-150 "Нет"
                                    m emo-0 "Но..."
                                    k emo-101 "[pname_max[0]], тебе пора спать."
                                    jump loc_my_room_sleep
                            "Катя!":
                                m emo-2 "Ну Катя!"
                                ka emo-152 "Хорошо. Пойдём."
                                $ ivent24.append("pgn_events_13_pool_katekira_hard")
            jump pgn_events_13_pool_katekira_next
        "Можно просто с вами побыть немного?":
            k emo-101 "Иди спать!"
            m emo-0 "Ладно."
        "идти спать":
            pass
    jump loc_my_room_sleep

label pgn_events_13_pool_katekira_next:
    scene pgn_poolnight_13_katewithkira_41
    m emo-3 "Заранее спасибо. Хоть уснуть смогу после этого."
    $ label_random = renpy.random.randint ( 10, 11)
    if (("pgn_events_13_pool_katekira_hard") in ivent24 and pgn_ach_repeat == 0) or (kate_path >= 3.7 and kateorder > 0 and pgn_ach_repeat == 0) or pgn_ach_repeat == 165:
        scene pgn_poolnight_13_katewithkira_42
        m emo-6 "Передумала?"
        scene pgn_poolnight_13_katewithkira_43
        ka emo-151 "Да. У меня есть другая идея."
        scene pgn_poolnight_13_katewithkira_44
        m emo-2 "Ай-ай-ай! Мой член! Ты его так сломаешь!"
        m emo-6 "За что?"
        scene pgn_poolnight_13_katewithkira_45
        if ("pgn_events_13_pool_katekira_hard") in ivent24 and pgn_ach_repeat == 0:
            ka emo-151 "Раз я твоя девушка, значит должна все твои прихоти выполнять?"
            m emo-2 "Ну я же попросил помочь. Ай!"
            ka emo-157 "Так вот, помогаю тебе кончить."
            m emo-2 "Это не совсем то. Ай!"
            if kate_path < 4:
                ka emo-156 "Я с тобой, как бы встречаюсь только из Мамы и ради [pname_alice[1]]."
            m emo-14 "Ай! Ай! Понял."
        else:
            ka emo-157 "Если хочешь и дальше получать того, чего желаешь, то нужно меня слушаться."
            m emo-6 "А что я сделал? Ай!"
            ka emo-157 "Если я тебе говорю трахнуть [pname_alice[3]], значит трахнешь. Скажу трахнуть в анал, значит в анал. Кончить в рот, значит кончишь ей туда."
            ka emo-151 "И раз хочешь оставаться моим парнем. То слушайся меня. Понял?"
            m emo-2 "Да. Ай!"
        ka emo-157 "Ложись на спину"
        menu:
            "Может не надо?":
                m emo-2 "Может не надо?"
                ka emo-156 "Может мне ещё сильнее надавить?"
                m emo-2 "Нет, нет, нет! Мне он ещё нужен."
            "Согласиться":
                pass
        scene pgn_poolnight_13_katewithkira_46
        m emo-1 "Мне так неудобно."
        scene pgn_poolnight_13_katewithkira_47
        $ renpy.pause()
        scene pgn_poolnight_13_katewithkira_48
        m emo-3 "{i}А вот попкой, это хорошо.{/i}"
        scene pgn_poolnight_13_katewithkira_49
        $ renpy.pause()
        scene pgn_poolnight_13_katewithkira_50
        m emo-2 "{i}Стоп! А если я кончу, то.....{/i}"
        scene pgn_poolnight_13_katewithkira_51
        m emo-8 "Катя. Хватит, остановись! Я же так сейчас кончу на себя. Пожалуйста."
        scene pgn_poolnight_13_katewithkira_52
        $ PGN_Achadd(pgnach_165, 165)
        m emo-10 "Я почти..."
        if ("pgn_events_13_pool_katekira_hard") in ivent24 and pgn_ach_repeat == 0:
            scene pgn_poolnight_13_katewithkira_53
            m emo-2 "Ай-ай-ай! Больно!"
            if kate_path < 4:
                ka emo-151 "Перед тем как дам тебе возможность кончить. Нужно кое-что прояснить."
                m emo-8 "Согласен на что угодно. Дай мне кончить."
                ka emo-155 "Запомни, единственная моя любовь, это [pname_alice[0]]. Ты мне нужен, только чтобы решить проблему с моей мамой."
            m emo-2 "Ай-ай-ай! Сейчас член лопнет от напора!"
            if kate_path < 4:
                ka emo-151 "Ты меня понял?"
                m emo-8 "Да, да. Пожалуйста. "
            scene pgn_poolnight_13_katewithkira_54
            m emo-10 "Аргггххх!!!"
            scene pgn_poolnight_13_katewithkira_55
            ka emo-152 "Приятных снов."
        elif renpy.random.randint ( 1, 2) == 1:
            scene pgn_poolnight_13_katewithkira_53
            $ renpy.pause()
            scene pgn_poolnight_13_katewithkira_54
            $ renpy.pause()
            scene pgn_poolnight_13_katewithkira_55
            $ renpy.pause()
        else:
            scene pgn_poolnight_13_katewithkira_56
            $ renpy.pause()
            scene pgn_poolnight_13_katewithkira_57
            $ renpy.pause()
            scene pgn_poolnight_13_katewithkira_58
            $ renpy.pause()
        if pgn_ach_repeat != 0:
            jump table_pgn_achievement
        $ PGN_Addstatsex(stat_kate, 0, 0, 0, 0, 1)
        $ kateorder = 0

    elif label_random == 11 and pgn_ach_repeat == 0:
        scene pgn_poolnight_13_katewithkira_59
        $ renpy.pause()
        scene pgn_poolnight_13_katewithkira_60
        m emo-4 "{i}Как она на меня смотрит.{/i}"
        scene pgn_poolnight_13_katewithkira_61
        $ renpy.pause()
        scene pgn_poolnight_13_katewithkira_62
        m emo-10 "Катя, я почти..."
        scene pgn_poolnight_13_katewithkira_63
        m emo-2 "Ай, ай! Отпусти. Пожалуйста."
        ka emo-159 "..."
        scene pgn_poolnight_13_katewithkira_64
        m emo-10 "Аргггххх!!!"
        m emo-10 "Спасибо."
        ka emo-152 "Приятных снов."
        $ PGN_Addstatsex(stat_kate, 0, 0, 0, 0, 1)
    else:
        scene pgn_poolnight_13_katewithkira_42
        m emo-6 "Передумала?"
        scene pgn_poolnight_13_katewithkira_43
        ka emo-151 "Да. У меня есть другая идея."
        scene pgn_poolnight_13_katewithkira_65
        $ renpy.pause()
        scene pgn_poolnight_13_katewithkira_66
        m emo-3 "{i}Это лучше, чем дрочить.{/i}"
        scene pgn_poolnight_13_katewithkira_67
        ka emo-154 "Ахх..... Ааа..."
        scene pgn_poolnight_13_katewithkira_68
        m emo-4 "{i}Ох уж эти округлости.{/i}"
        scene pgn_poolnight_13_katewithkira_69
        $ PGN_Achadd(pgnach_166, 166)
        ka emo-152 "[pname_max[0]], Аахх... Мммм..."
        scene pgn_poolnight_13_katewithkira_70
        $ renpy.pause()
        m emo-12 "Аррргххх!!!"
        scene pgn_poolnight_13_katewithkira_71
        $ renpy.pause()
        scene pgn_poolnight_13_katewithkira_72
        m emo-10 "Ох блин! Не всё вышло..."
        m emo-13 "Может вылижешь?"
        $ label_random = renpy.random.randint ( 5, 7)
        if label_random != 5:
            scene pgn_poolnight_13_katewithkira_56
            $ renpy.pause()
            scene pgn_poolnight_13_katewithkira_58
            ka emo-156 "Как в тебе столько вмещается?"
            m emo-3 "Немного погодя я ещё смогу."
            ka emo-152 "Нет, всё, уже слишком поздно и пора спать."
            m emo-2 "Ну ладно. Спокой ночи."
            m emo-3 "А может вместе ляжем спать?"
        else:
            ka emo-152 "Спокойной ночи."
            m emo-2 "Катя!"
        if pgn_ach_repeat != 0:
            jump table_pgn_achievement
        $ PGN_Addstatsex(stat_kate, 1, 0, 0, 0, 0)
    jump loc_my_room_sleep


label pgn_events_13_momkate_06:
    $ kate_path = 4
    scene black with dissolve
    $ renpy.pause(4)
    scene pgn_club_momkate_01_bar
    m emo-9 "{i}Опять меня кто-то и как-то...{/i}"
    scene pgn_club_momkate_03_bar
    $ renpy.pause(5)
    scene pgn_club_momkate_04_bar
    momk emo-321 "Привет [pname_max[0]]."
    m emo-0 "Здравствуйте."
    momk emo-320 "Как твои дела с Катей?"
    m emo-3 "Эм... У нас всё прекрасно. Встречаемся."
    scene pgn_club_momkate_06_bar
    momk emo-321 "..."
    m emo-13 "Мне с ней расстаться?"
    momk emo-320 "Нет. Зачем так рано?! Вы же только начали свои отношения. Когда придёт время, я дам тебе знать."
    scene pgn_club_momkate_07_bar
    $ renpy.pause()
    scene pgn_club_momkate_08_bar
    m emo-8 "А что это?"
    momk emo-320 "Выпей их."
    menu:
        "Если не хочу?":
            m emo-8 "А если я не хочу? Да и не знаю что это."
            momk emo-320 "Таблетки, ты подобные уже принимал."
            momk emo-320 "Если сейчас не хочешь, то когда решишь, подойди к бармену. Я в клубе каждый день, буду тебя ждать."
            menu:
                "Потом":
                    m emo-8 "Я как-нибудь потом."
                    momk emo-320 "Ладно. Значит в другой раз. Только слишком не затягивай."
                    jump loc_club_dancefloor_01
                "Проглотить таблетки":
                    pass
        "Проглотить таблетки":
            pass
    scene pgn_club_momkate_06_bar
    momk emo-321 "Хороший мальчик. Через 1 час таблетка подействует и за тобой придут."
    m emo-0 "Понял."
    momk emo-321 "Скоро увидимся."
    scene black with dissolve
    $ renpy.pause()
    if stat_max.tubs1 > 0:
        jump pgn_events_13_newtubs_01

label pgn_events_13_momkate_end:
    scene pgp_club_firstvisit_02
    other emo-998 "Здравствуйте. Вас уже ждут. Идёмте за мной."
    scene pgn_club_momkate_ev13_40
    m emo-6 "{i}Хм... куда это мы идём?{/i}"
    scene pgn_club_momkate_ev13_41
    m emo-0 "{i}Тут я не был. Интересно. У меня сейчас будет что-то с ней?{/i}"
    scene pgn_club_momkate_ev13_42
    other emo-999 "Мммм... ммммммм..... мммммммм..."
    scene pgn_club_momkate_ev13_43
    m emo-8 "{i}Надеюсь мне не туда.{/i}"
    other emo-998 "Не задерживайтесь, вас ждут."
    m emo-0 "{i}Фух. Вроде пронесло.{/i}"
    scene pgn_club_momkate_ev13_44
    m emo-1 "Вау!"
    momk emo-320 "Раздевайся и устраивайся удобно на кровати."
    m emo-8 "{i}Откуда этот голос и где она сама? Что-то я немного побаиваюсь этого места. Может я зря пришёл.{/i}"
    scene pgn_club_momkate_ev13_45
    m emo-1 "{i}Тут очень просторно...{/i}"
    m emo-0 "{i}Ну разделся я и что дальше.{/i}"
    scene pgn_club_momkate_ev13_46
    $ renpy.pause()
    scene pgn_club_momkate_ev13_47
    m emo-3 "Здравствуйте."
    momk emo-321 "Я хотела бы тебя отблагодарить, как-то по-особому."
    menu:
        "Да не нужно":
            m emo-1 "Спасибо. Но я не сделал ничего такого особого."
            momk emo-321 "Ммм... скромняшка."
        "Круто":
            m emo-3 "Круто. А что сейчас будет?"
            momk emo-321 "Сейчас сам всё увидишь и почувствуешь."
        "Вы мне понравились":
            m emo-4 "Вы давно мне приглянулись и хочу познакомиться с вами поближе."
            momk emo-328 "Потом, а сначала..."
    scene pgn_club_momkate_ev13_48
    $ PGN_Achadd(pgnach_167, 167)
    momk emo-321 "Мои девочки займутся тобой. И если останутся силы, то после них буду уже я."
    scene pgn_club_momkate_ev13_49
    m emo-4 "{i}Зря я пережевал. Всё будет офегенно!{/i}"
    scene pgn_club_momkate_ev13_50
    m emo-5 "{i}О!{/i}"
    scene pgn_club_momkate_ev13_51
    m emo-1 "{i}Крепко меня сжала. Да и пофиг. Зато какой вид. Сиськи...{/i}"
    scene pgn_club_momkate_ev13_52
    m emo-3 "{i}Блондинка тщательно вылизывает ствол. Сейчас у меня будет секс! У меня будет секс!{/i}"
    scene pgn_club_momkate_ev13_53
    m emo-4 "{i}О да! Думал внутри будет иначе, но нет, киска узкая. Класс!{/i}"
    scene pgn_club_momkate_ev13_54
    $ renpy.pause()
    scene pgn_club_momkate_ev13_55
    m emo-3 "{i}Блондинка помогает подружке кончить и... Ох! Я чувствую её язычок. Вылизывает, стекающие по моему члену, соки.{/i}"
    scene pgn_club_momkate_ev13_56
    other emo-998 "Малыш. Вылежи мою попку."
    m emo-4 "С радостью."
    m emo-3 "{i}Сейчас ещё и в анал ей...{/i}"
    m emo-10 "{i}Ой! Блин... сейчас кончу.{/i}"
    m emo-12 "Аррргххх!!! Ааааахх... Аааа..."
    m emo-13 "{i}Мощно кончил. Очень сильно.{/i}"
    scene pgn_club_momkate_ev13_57
    m emo-9 "{i}Ого! Из её киски всё льётся.{/i}"
    scene pgn_club_momkate_ev13_58
    $ renpy.pause()
    scene pgn_club_momkate_ev13_59
    m emo-13 "{i}Хотя бы дали пару минут на отдых.{/i}"
    scene pgn_club_momkate_ev13_60
    m emo-9 "{i}У неё тугая дырочка. Как будто не разработанная.{/i}"
    scene pgn_club_momkate_ev13_61
    other emo-998 "Аааа... Аааааааа..."
    m emo-9 "{i}Она с силой на садилась на член! У неё был девственный анал? Серьезно?{/i}"
    other emo-998 "Ааахх... Ммм... Ааахх..."
    scene pgn_club_momkate_ev13_62
    m emo-1 "{i}Вау!{/i}"
    scene pgn_club_momkate_ev13_63
    other emo-998 "Глубже! Глубже! Я кончаю!"
    scene pgn_club_momkate_ev13_64
    other emo-998 "Аааа! Ааааа!"
    scene pgn_club_momkate_ev13_65
    m emo-12 "Аррргххх! Блин! Аррргххх!"
    m emo-10 "{i}Снова кончил. Это что за таблетка такая?!{/i}"
    scene pgn_club_momkate_ev13_66_asanosakura
    other emo-998 "Ммм... Ох, малыш, ты всю мою попку заполнил спермой."
    scene pgn_club_momkate_ev13_67_asanosakura
    m emo-5 "{i}Фцх! Вау! Из меня ещё так много за короткое время не выходило спермы.{/i}"
    m emo-10 "{i}Да! Минет, это то что мне нужно. Нежный минет...{/i}"
    scene black with dissolve
    m emo-10 "{i}Как же хорошо...{/i}"
    scene pgn_club_momkate_ev13_68_asanosakura with dissolve
    m emo-2 "Ай!!! \n{i}Блин! Они с силой сжали мой член!{/i}"
    scene pgn_club_momkate_ev13_69_asanosakura
    m emo-8 "{i}Они собираются выдоить из меня всё до самой капли.{/i}"
    scene pgn_club_momkate_ev13_70
    m emo-9 "{i}Ох чёрт! Они ускорились. От такой жесткой мастурбации мой член оторвётся.{/i}"
    scene pgn_club_momkate_ev13_71
    m emo-10 "Аррргххх!"
    scene pgn_club_momkate_ev13_72
    m emo-7 "{i}Это всё, мой предел, больше не могу...{/i}"
    scene pgn_club_momkate_ev13_73
    $ renpy.pause()
    scene pgn_club_momkate_ev13_74_vadx
    $ renpy.pause()
    scene pgn_club_momkate_ev13_75_vadx
    momk emo-321 "Девочки."
    scene pgn_club_momkate_ev13_76_vadx with dissolve
    momk emo-321 "[pname_max[0]], тебе понравилось?"
    menu:
        "Да. Но устал":
            m emo-7 "Да. Это было круто. Спасибо."
            m emo-10 "Они из меня всё выжали, сил больше нет."
            scene pgn_club_momkate_ev13_77_vadx
            momk emo-326 "Прямо все?"
            m emo-9 "{i}Это не ещё всё?{/i}"
        "Ещё хочу":
            m emo-3 "Да. Но я бы ещё повторил. А куда они ушли?"
            scene pgn_club_momkate_ev13_77_vadx
            momk emo-326 "Ещё хочется. А ты выносливый. Моя очередь."
    scene pgn_club_momkate_ev13_78_vadx
    momk emo-327 "Он у тебя слегка размяк. Это поправимо."
    momk emo-321 "Отлично."
    scene pgn_club_momkate_ev13_79_vadx
    momk emo-330 "Да, молодец. Язычок натренирован."
    scene pgn_club_momkate_ev13_80_vadx
    m emo-8 "{i}Блин! Задыхаюсь.{/i}"
    momk emo-329 "Аххх! Аххх! Хороший мальчик. Ты мне нравишься. Лижи."
    m emo-13 "{i}Нравлюсь? Она в меня влюбилась?{/i}"
    momk emo-328 "Отлично. Ты заслужил вознаграждения."
    menu:
        "Член болит":
            m emo-8 "Может не надо больше? У меня член болит после всего."
            momk emo-325 "Это не то, чего я ожидала услышать. "
            momk emo-327 "Возбудил меня и не хочешь продолжить. Плохой мальчик. Тебя придётся наказать."
        "Готов":
            m emo-4 "Я готов продолжить."
            momk emo-321 "Хороший мальчик."
    scene pgn_club_momkate_ev13_81_vadx
    m emo-9 "{i}В этой киске точно давно ничего не было.{/i}"
    momk emo-330 "Ох! [pname_max[0]]. Он у тебя действительно огромный. Ммм..."
    scene pgn_club_momkate_ev13_82_vadx
    momk emo-331 "И гибкий, но не мягкий. Отлично!"
    scene pgn_club_momkate_ev13_83_vadx
    m emo-10 "Сейчас кончу!"
    momk emo-328 "Кончай!"
    scene pgn_club_momkate_ev13_84_vadx
    m emo-9 "Ааааааа!"
    momk emo-332 "Аааххх!"
    scene pgn_club_momkate_ev13_85_vadx
    momk emo-321 "Молодец. Хороший мальчик."
    scene pgn_club_momkate_ev13_86_vadx
    momk emo-328 "Ох [pname_max[0]], у меня на тебя большие планы."
    m emo-7 "Мхм... Мама... Мхм..."
    if pgn_ach_repeat != 0:
        jump table_pgn_achievement
    scene black with dissolve
    $ renpy.pause(3)
    $ PGN_Addstatsex(stat_momk, 0, 1, 0, 1, 0)
    $ momkate_path = 5
    if qtime <= 23:
        $ qtime, days, daysn = 1, days+1, daysn+1
    jump loc_my_room_sleep



label pgn_events_13_katewithmom:
    scene bg door_02
    m emo-6 "{i}Хм... Кажется с Мамой кто-то ещё. Не знаю о чём болтают, но там точно с мамой Катя.{/i}"
    menu:
        "Приоткрыть дверь":
            scene pgn_events_13_katewithmom_73
            m emo-6 "{i}О чём они там болтают?{/i}"
            scene pgn_events_13_katewithmom_74
            m emo-1 "{i}Мама заметила{/i}"
            scene pgn_events_13_katewithmom_75
            ka emo-152 "[pname_max[0]]. А ты знаешь, что подглядывать и подслушивать не хорошо."
            menu:
                "О чём разговариваете?":
                    m emo-6 "А о чём вы болтаете? Можно с вами."
                "Я к Маме":
                    m emo-0 "Я к маме пришёл по одному делу."
            ka emo-151 "Выйди и закрой дверь."
            m emo-0 "{i}Блин{/i}"
            scene bg door_02
            call screen location_mom_room
        "Подсмотреть с балкона":
            scene pgn_events_13_katewithmom_76
            m emo-6 "{i}Хм... о чём они там болтают?{/i}"
            scene pgn_events_13_katewithmom_77
            m emo-0 "{i}Мама совсем не стесняется и не против, что они обе голые.{/i}"
            scene pgn_events_13_katewithmom_78
            if "катя_лесбосмамой" not in accessiv:
                m emo-9 "{i}Какого!? Катя взялась за мамину попку! А Мама ей это позволяет. Что происходит?{/i}"
            else:
                $ renpy.pause()
            scene pgn_events_13_katewithmom_79
            if "катя_лесбосмамой" not in accessiv:
                m emo-9 "{i}Ох, чёрт! Вау! Как... как... как она это сделала!? Мама!{/i}"
            else:
                $ renpy.pause()
            scene pgn_events_13_katewithmom_80
            if "катя_лесбосмамой" not in accessiv:
                m emo-2 "{i}Как Кате это удалось?{/i}"
            else:
                $ renpy.pause()
            scene pgn_events_13_katewithmom_81
            m emo-9 "{i}Охренеть!{/i}"
            scene pgn_events_13_katewithmom_82
            if "катя_лесбосмамой" not in accessiv:
                m emo-3 "{i}Сейчас бы к ним. Но кто знает, что будет если зайду. Так что подожду и посмотрю, что будет дальше.{/i}"
            else:
                m emo-3 "{i}Сейчас бы к ним. Но кто знает, что будет если зайду. Дождусь, когда Катя уйдёт.{/i}"
            scene pgn_events_13_katewithmom_83
            if "катя_лесбосмамой" not in accessiv:
                m emo-6 "{i}Уже всё? Думал будет продолжение.{/i}"
            else:
                m emo-3 "{i}Катя завела Маму, остаётся только мне появиться.{/i}"
            scene pgn_events_13_katewithmom_84
            menu:
                "Зайти":
                    scene pgn_events_13_katewithmom_85
                    m emo-4 "Мам..."
                    scene pgn_events_13_katewithmom_86
                    mom emo-66 "Ой! [pname_max[0]]! А ты чего этот тут? И почему не через дверь?"
                    mom emo-62 "А! Понятно. Снова подглядывал. Подойди ко мне."
                    if "катя_лесбосмамой" not in accessiv:
                        $ accessiv.append("катя_лесбосмамой")
                        scene pgn_events_13_katewithmom_87
                        m emo-13 "Мама! А что ты... Как... Эм... С Катей ты..."
                        mom emo-60 "[pname_max[0]]! Не говори [pname_alice[2]] и [pname_kira[2]]. Хорошо?"
                        menu:
                            "Ладно":
                                m emo-0 "Ладно."
                                mom emo-62 "Спасибо."
                            "Я подумаю":
                                m emo-6 "Я подумаю."
                                mom emo-68 "[pname_max[0]]! Ну нельзя же так. Я твоя Мама. Я по-хорошему прошу."
                                mom emo-69 "Ты свою Маму не любишь?"
                                m emo-5 "Люблю конечно."
                                m emo-2 "Извини."
                                mom emo-60 "[pname_alice[0]] на тебя плохо влияет."
                        scene pgn_events_13_katewithmom_88
                        mom emo-69 "Сама не знаю как так вышло. Просто разговаривали и... Вот."
                        m emo-6 "{i}Что вот? Что она этим хочет сказать, она ей понравилась, не понимаю.{/i}"
                    scene pgn_events_13_katewithmom_89
                    mom emo-67 "Сынок. Трахнешь меня? Я сейчас хочу от тебя секса. Мм?"
                    menu:
                        "С радостью":
                            m emo-3 "С радостью и с удовольствием."
                            scene pgn_events_13_katewithmom_91
                            m emo-1 "Мама, можешь пониже опуститься? Я не достаю."
                            mom emo-75 "Конечно. Забыла, что ты у меня маленький."
                            m emo-8 "Я ещё выросту."
                            mom emo-75 "Конечно, малыш."
                            scene pgn_events_13_katewithmom_92
                            mom emo-68 "Ааахх... Ммм... Продолжай сынок."
                            scene pgn_events_13_katewithmom_93
                            $ renpy.pause()
                            scene pgn_events_13_katewithmom_94
                            mom emo-73 "Мммм..."
                            m emo-3 "{i}У Мамы очень горячая киска и мокрая. Это наверное из-за Кати.{/i}"
                            scene pgn_events_13_katewithmom_95
                            mom emo-62 "[pname_max[0]], ляг. Мамочка хочет сверху."
                            menu:
                                "Лечь":
                                    $ label_random = renpy.random.randint ( 1, 3)
                                    label pgn_events_13_katewithmom_again:
                                        scene pgn_events_13_katewithmom_101
                                        $ renpy.pause()
                                        scene pgn_events_13_katewithmom_102
                                        mom emo-71 "Сейчас. Мама всё сделает сама. От тебя требуется только продержаться и не кончить раньше меня."
                                        scene pgn_events_13_katewithmom_103
                                        $ renpy.pause()
                                        scene pgn_events_13_katewithmom_104
                                        $ renpy.pause()
                                        scene pgn_events_13_katewithmom_105
                                        $ renpy.pause()
                                        scene pgn_events_13_katewithmom_106
                                        $ renpy.pause()
                                        scene pgn_events_13_katewithmom_107
                                        $ renpy.pause()
                                        scene pgn_events_13_katewithmom_108
                                        if label_random == 2:
                                            $ label_random = 0
                                            m emo-10 "Мама, я уже почти... Сейчас кончу."
                                            scene pgn_events_13_katewithmom_109
                                            mom emo-69 "Потерпи! Мама ещё не кончила. Рано тебе ещё кончать."
                                            scene pgn_events_13_katewithmom_110
                                            mom emo-75 "Продолжим."
                                            jump pgn_events_13_katewithmom_again
                                        else:
                                            scene pgn_events_13_katewithmom_111
                                            m emo-12 "Аррргххх!!!"
                                            scene pgn_events_13_katewithmom_112
                                            mom emo-68 "Ааааахххх! [pname_max[0]]! Ааааххх!"
                                            scene pgn_events_13_katewithmom_113
                                            m emo-5 "Мама. Я люблю тебя."
                                            mom emo-67 "И я тебя. Спасибо тебе, сынок."
                                        scene pgn_events_13_katewithmom_114
                                        $ renpy.pause()
                                "Отказаться и продолжить":
                                    m emo-3 "Нет. Я хочу тебя сзади."
                                    scene pgn_events_13_katewithmom_96
                                    mom emo-75 "Ох! [pname_max[0]]."
                                    scene pgn_events_13_katewithmom_97
                                    $ renpy.pause()
                                    scene pgn_events_13_katewithmom_98
                                    $ renpy.pause()
                                    scene pgn_events_13_katewithmom_99
                                    m emo-10 "Аррргххх!"
                                    scene pgn_events_13_katewithmom_100
                                    mom emo-73 "[pname_max[0]]! Ты тяжелый, слезай с меня."
                                    m emo-7 "Я... люблю... тебя... мааа..."
                                    mom emo-73 "[pname_max[0]]!"
                                    mom emo-73 "Уснул... Спасибо тебе."
                                    scene pgn_events_13_katewithmom_115
                                    $ renpy.pause()
                                    $ ivent24.append("макс_уснул")
                            $ PGN_Addstatsex(stat_mom, 0, 0, 0, 1, 0)
                        "Уйти":
                            m emo-3 "Мама. Я бы с радостью, но у меня некоторые дела..."
                            scene pgn_events_13_katewithmom_90
                            mom emo-69 "Может всё же передумаешь? Мама так сильно возбуждена, ей сейчас очень нужен твой член в киске."
                            menu:
                                "Остаться":
                                    jump pgn_events_13_katewithmom_again
                                "уйти":
                                    m emo-0 "Я пойду."
                "уйти":
                    m emo-3 "{i}Не буду ей мешать, пойду.{/i}"
        "уйти":
            scene bg door_02
            call screen location_mom_room
    $ qtime = 1
    if ("макс_уснул") in ivent24:
        jump loc_my_room_sleep
    jump loc_my_room


label veranda_breakfast_13_boobs:
    scene pgn_breakfast_with_kate_36
    if ("завтрак_голыесиськи") not in accessiv:
        menu:
            "Может полностью раздернитесь?":
                $ accessiv.append("завтрак_голыесиськи")
                scene pgn_breakfast_with_kate_37
                m emo-3 "А почему бы нам вообще не сидеть голыми?"
                mom emo-68 "[pname_max[0]]! Нет! Ты сюда пришёл завтракать, а не..."
                scene pgn_breakfast_with_kate_36
                a emo-22 "А я и так совсем без одежды."
                mom emo-63 "[pname_alice[0]]!"
                a emo-20 "А что? [pname_max[2]] всё равно ничего не видно. Да, [pname_max[0]]?"
                mom emo-60 "Давайте не будем пока поднимать подобные темы. И [pname_max[0]], всему своё время. К таким переменам нужно привыкнуть."
                mom emo-62 "Всем приятного аппетита."
            "Продолжить завтрак":
                pass
    else:
        k emo-113 "Всем приятного аппетита! А вы знаете, что если во время завтрака не отвлекаться на беседы, то можно сосредоточиться на вкусе еды и получить гораздо больше удовольствия!"
        m emo-3 "А ты разбираешься в удовольствиях..."
    jump veranda_breakfast_next


label pgn_club_max_alcogol:
    if qtime >= 21 and qtime <= 24:
        $ days, daysn = days+1, daysn+1
        if qtime == 24:
            $ qtime = 0
    jump loc_my_room_sleep
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
