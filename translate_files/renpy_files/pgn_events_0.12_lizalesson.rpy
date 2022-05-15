






label pgn_events_12_lizanight_00:
    $ ivent24.append("[pname_liza[0]]_ночь_маст")
    if liza_path == 40:
        jump pgn_events_12_lizanight_01
    if liza_path == 40.1:
        jump pgn_events_12_lizanight_02
    if liza_path == 40.2:
        jump pgn_events_12_lizanight_03

label pgn_events_12_lizanight_01:
    scene black with dissolve
    l emo-49 "Ах... Ммм.. Ммм..."
    m emo-1 "[pname_liza[0]]?"
    m emo-8 "{i}Показалось что ли!? Ладно, хочу спать.{/i}"
    $ liza_path = 40.1
    $ ivent24.append("лиза_ночь_маст")
    jump loc_my_room_sleep_02

label pgn_events_12_lizanight_02:
    scene black with dissolve
    l emo-49 "Мммм... Ах... Ах... Ммм..."
    scene pgn_myroom_liza_solonight_01
    m emo-1 "{i}Снова!?{/i}"
    scene pgn_myroom_liza_solonight_02
    m emo-3 "{i}Моя маленькая сестрёнка мастурбирует. Может предложить ей свою помощь?{/i}"
    scene pgn_myroom_liza_solonight_03
    menu:
        "Наблюдать":
            $ renpy.pause(5)
            l emo-49 "[pname_max[0]], [pname_max[0]]..."
            scene black with dissolve
            $ ivent24.append("лиза_ночь_маст")
            jump loc_my_room_sleep_02
        "Предложить помощь":
            pass
    m emo-13 "Помощь нужна?"
    l emo-50 "А, [pname_max[0]]. Ты, не спишь?"
    m emo-0 "С твоими возбуждающими стонами мне ни за что не уснуть"
    scene pgn_myroom_liza_solonight_04
    l emo-46 "Прости, у меня ни как не получается кончить. Мне нравится, когда ты меня трахаешь в попу, я получаю от этого удовольствие."
    l emo-46 "Но я хочу попробовать кончить сама. Ты и твой член не всегда же будете рядом."
    m emo-3 "Я всегда буду рядом."
    l emo-41 "Спасибо. "
    m emo-6 "Хм... может займёмся сексом или может я сделаю тебе куни?"
    l emo-49 "Куни. Сейчас очень поздно для анала."
    scene pgn_myroom_liza_solonight_05
    m emo-4 "Твоя киска очень мокрая. Точно не кончила или нужно было просто подольше мастурбировать?"
    scene pgn_myroom_liza_solonight_06
    l emo-43 "Не знаю. [pname_max[0]]. Заставь меня кончить или не дам тебе уснуть."
    m emo-4 "Брат обязательно поможет миленькой сестрёнке."
    scene animated pgn_myroom_liza_solonight_07
    $ renpy.pause()
    l emo-49 "[pname_max[0]], я скоро, не останавливайся."
    $ renpy.pause()
    scene pgn_myroom_liza_solonight_08
    l emo-50 "Ааххх..."
    scene pgn_myroom_liza_solonight_10
    l emo-41 "Спасибо [pname_max[0]]."
    m emo-3 "Обращайся."
    $ liza_sex_bj = 4
    $ liza_path = 40.2
    $ ivent24.append("лиза_ночь_маст")
    $ PGN_Addstatsex(stat_liza, 0, 1, 0, 0, 0)
    jump loc_my_room_sleep_02

label pgn_events_12_lizanight_03:
    scene black with dissolve
    l emo-49 "[pname_max[0]], ты спишь? [pname_max[0]]..."
    scene pgn_myroom_liza_solonight_09
    m emo-1 "Снова не получается?"
    l emo-40 "Да"
    m emo-1 "Куни?"
    l emo-46 "Сейчас что-то не хочется."
    m emo-6 "Может попросишь помощи у Тёти [pname_kira[1]]? Она в этом больше понимает."
    l emo-40 "Хм... Думаю будет лучше, если обучением займётся Мама."
    m emo-6 "Почему?"
    l emo-48 "Ну... Ты замечал, как Мама во время наших уроков по кунилингусу еле себя сдерживает? "
    m emo-3 "Вроде... Хочешь устроить тройничок?"
    l emo-49 "Нет, [pname_max[0]]. Т.е не знаю, ну не думаю, что согласится."
    l emo-40 "Ладно, давай спать. Поговорю сегодня с Мамой."
    m emo-0 "Ты только не забудь про меня, я тоже хочу поучаствовать."
    l emo-41 "Хорошо, постараюсь не забыть."
    $ liza_path = 40.3
    $ ivent24.append("лиза_ночь_маст")
    jump loc_my_room_sleep_02

label pgn_events_12_lizanight_04:
    m emo-0 "Ну как. Что сказала Мама?"
    l emo-41 "Она немного удивилась, думала что я и так это умею делать. Так что с радостью поможет мне."
    m emo-4 "Значит у нас будут новые уроки с Мамой?! Круто!"
    l emo-40 "У нас? Нет, только я и Мама."
    m emo-13 "Как так, а я? Мы же на предыдущих уроках были вместе."
    l emo-49 "Ну... Вообще-то уроки проводились для меня, как правильно делать минет, только у тебя был подходящий и доступный инструмент. Уроки по кунилингусу понадобятся обоим. А вот мастурбация, подразумевает отсутствие сексуального партнера."
    m emo-0 "Блин! А... А если не участвовать, а хотя бы смотреть со стороны."
    l emo-40 "Ладно, ладно. Поговорю ещё раз с Мамой"
    m emo-0 "Спасибо."
    $ days_liza = days+1
    $ liza_path = 40.4
    jump jump_dialogue

label pgn_events_12_lizanight_05:
    m emo-4 "И?"
    l emo-46 "Что и?"
    m emo-3 "Мама разрешила мне присутствовать на ваших уроках?"
    l emo-46 "Извини, но нет."
    m emo-1 "{i}Что же делать. Придумал.{/i}"
    m emo-3 "Слушай, [pname_liza[0]]. А может я буду смотреть удалённо?"
    l emo-41 "Это как, с балкона?"
    m emo-3 "Поставишь ноут [pname_alice[1]] на стол, включишь закрытую трансляцию, а я через свой ноут буду смотреть."
    l emo-46 "Я не умею и не знаю, как делать эти... трансляции."
    m emo-0 "Тогда я всё подготовлю и тебе останется лишь только поставить ноут на стол."
    l emo-40 "Ладно."
    $ liza_path = 41
    jump jump_dialogue



label pgn_events_12_lizasololesson_laptop_alice:
    m emo-0 "[pname_alice[0]], одолжи ноутбук на время."
    a emo-20 "Зачем он тебе?"
    m emo-0 "Надо."
    $ label_random = renpy.random.randint ( 100, 200)
    a emo-21 "$[label_random]"
    menu:
        "Согласиться":
            $ currency -= label_random
            $ renpy.notify(str(task_notifi[11])+" $"+str(label_random))
            $ renpy.play("content/audio/long_expected.mp3", "audio", fadein=0, fadeout=0)
            $ laptop_alice.have = True
            $ ivent24.append("ноут_алисы_у_макса")
        "уйти":
            pass
    jump jump_dialogue

label pgn_events_12_lizasololesson_laptop_alice_view:
    menu:
        "Урок [pname_liza[1]]" if qtime == 22 and ("лиза_урок_мастурбации_ноут_макса") in ivent24 and laptop_alice.have == False:
            jump pgn_events_12_lizasololesson_0_
        "Взять ноутбук" if laptop_alice.have == False and ("лиза_урок_мастурбации_ноут_алисы") not in ivent24:
            $ ivent24.append("ноут_алисы_у_макса")
            $ laptop_alice.have = True
        "Оставить ноутбук" if laptop_alice.have == True:
            $ laptop_alice.have = False
            $ ivent24.remove("ноут_алисы_у_макса")
        "уйти":
            pass
    jump loc_alice_room

label pgn_events_12_lizasololesson_laptop_max:
    menu:
        "Взять ноутбук" if laptop_max.have == False and ("лиза_урок_мастурбации_ноут_макса") not in ivent24:
            $ laptop_max.have = True
        "Оставить ноутбук" if laptop_max.have == True:
            $ laptop_max.have = False
        "отмена":
            pass
    jump loc_my_room

label pgn_events_12_lizasololesson_laptop:
    m emo-0 "Вот ноутбук, всё настроил, нужно только поставить на стол."
    if daysn != 2 and daysn != 5 and daysn != 7:
        l emo-41 "[pname_max[0]]. Сегодня не получится. Мама сказала, что только по определенным дням: Вторник, Пятница и Воскресение."
        m emo-2 "А почему не сегодня?"
        l emo-40 "Мама так сказала, так что я не знаю почему."
        m emo-0 "Блин. Ладно."
    else:
        if laptop_alice.have == True:
            $ laptop_alice.have = False
            $ ivent24.append("лиза_урок_мастурбации_ноут_алисы")
            $ ivent24.remove("ноут_алисы_у_макса")
        elif laptop_max.have == True:
            $ laptop_max.have = False
            $ ivent24.append("лиза_урок_мастурбации_ноут_макса")
        if liza_path >= 42:
            $ ivent24.append("лиза_спит_у_мамы")
            $ ivent24.append("мама_и_лиза_после_уроков_ванная")
            l emo-41 "А что хочешь увидеть?"
            menu menu_pgn_events_12_lizasololesson_laptop:
                "Мастурбация Мамы" if ("урок_мастурбации_лизы_мамасоло") not in ivent24:
                    $ ivent24.append("урок_мастурбации_лизы_мамасоло")
                    jump menu_pgn_events_12_lizasololesson_laptop
                "Совместная мастурбация" if ("урок_мастурбации_лизы_мамаилиза") not in ivent24:
                    $ ivent24.append("урок_мастурбации_лизы_мамаилиза")
                    jump menu_pgn_events_12_lizasololesson_laptop
                "Как ты мастурбируешь" if ("урок_мастурбации_лизы_лизасоло") not in ivent24:
                    $ ivent24.append("урок_мастурбации_лизы_лизасоло")
                    jump menu_pgn_events_12_lizasololesson_laptop
                "Больше ничего" if ("урок_мастурбации_лизы_мамасоло") in ivent24 or ("урок_мастурбации_лизы_мамаилиза") in ivent24 or ("урок_мастурбации_лизы_лизасоло") in ivent24:
                    pass
        $ ivent24.append("лиза_урок_мастурбации")
        l emo-41 "Поняла"
    jump jump_dialogue


label pgn_events_12_lizasololesson_00:
    scene pgn_momroom_lizasololesson_01_vezdessushij
    m emo-1 "{i}Мне бы к ним.{/i}"
    scene bg door_02
    call screen location_mom_room

label pgn_events_12_lizasololesson_0_:
    if liza_path == 41:
        jump pgn_events_12_lizasololesson_01
    if liza_path == 41.1:
        jump pgn_events_12_lizasololesson_02
    if liza_path == 41.2:
        jump pgn_events_12_lizasololesson_03
    if liza_path >= 42:
        jump pgn_events_12_lizasololesson_start


label pgn_events_12_lizasololesson_01:
    scene pgn_momroom_lizasololesson_02_zicado
    mom emo-60 "[pname_liza[0]], а зачем ты ноутбук сюда принесла?"
    l emo-48 "Ну я подумала, что можно как-то разнообразить уроки и сделать их поинтереснее."
    mom emo-66 "Что? Ты хочешь куда-то это транслировать. Одной уже запретила и ты туда же?"
    m emo-1 "{i}Облом.{/i}"
    l emo-40 "Нет Мам, ты что, нет. Я имела в виду, что можно музыку включить какую-нибудь расслабляющую."
    mom emo-60 "А ну тогда ладно."
    m emo-1 "{i}Фух, пронесло.{/i}"
    mom emo-62 "Хорошо. Включай, что хочешь и идём на кровать."
    scene pgn_momroom_lizasololesson_03_zicado
    mom emo-67 "И так, малышка. Различают несколько видов оргазма: клиторный, вагинальный и маточный."
    m emo-6 "{i}А анальный оргазм? Или нет, или да, или, хм...{/i}"
    mom emo-60 "Последние два не будем разбирать на этих уроках."
    l emo-40 "Почему?"
    mom emo-69 "Потому что ты девственница. Тебе ещё рано такое, вот будет у тебя парень, тогда поговорим."
    l emo-41 "А может [pname_max[0]] нам поможет?"
    mom emo-64 "[pname_liza[0]], нет! Я и так с вами провожу уроки по сексу, которых не должно быть. Нет, [pname_liza[0]], даже и не думай делать это с братом. Хорошо?"
    l emo-40 "Ладно."
    mom emo-60 "[pname_liza[0]], я просто не хочу, чтобы ты потом об этом жалела, когда у тебя будет своя семья. Будет лучше, если твой первый раз будет с кем-то, кого ты полюбишь."
    l emo-43 "Я [pname_max[1]] тоже люблю."
    mom emo-62 "Как брата, но не парня."
    mom emo-62 "Хватит на этом. Продолжим."
    scene pgn_momroom_lizasololesson_04_zicado
    mom emo-62 "На наших предыдущих уроках, с [pname_max[4]]. Ты узнала, как достичь клиторного оргазма через кунилингус. Сейчас ты хочешь научиться, как этого достичь без чей-то помощи?"
    l emo-40 "Да. Ты же не разрешаешь нам этим заниматься вне уроков."
    mom emo-69 "Извини, я не хочу чтобы вы сделали что-то о чём потом будете жалеть всю жизнь."
    m emo-3 "{i}Жалеть, да нам будет только ещё лучше.{/i}"
    scene pgn_momroom_lizasololesson_05_zicado
    mom emo-60 "Смотри внимательно. Это клитор. На самом вверху, над влагалищем. Сразу переходить к мастурбации не нужно, т.е. если ты не возбуждена, иначе можно только навредить себе."
    mom emo-60 "Перед мастурбацией тебе нужно его увлажнить. Можно или слюной или вагинальной смазкой."
    mom emo-60 "После остаётся просто его нежно ласкать и вот такими движениями делать пальцами. Сначала не торопясь, по кругу, из стороны в сторону."
    scene pgn_momroom_lizasololesson_06_zicado
    mom emo-69 "Вот так... Ммм... Медленно и осторожно..."
    mom emo-69 "Постепенно можно увеличить скорость и задействовать свободную руку."
    scene animated pgn_momroom_lizasololesson_07
    $ renpy.pause()
    scene pgn_momroom_lizasololesson_08_vezdessushij
    mom emo-68 "Ой! Прости малышка, совсем забыла про тебя. Садись ко мне поближе и покажу как надо."
    scene pgn_momroom_lizasololesson_09_vezdessushij
    mom emo-69 "Очень хорошо, у тебя там всё влажно, можно начинать."
    mom emo-75 "[pname_liza[0]], расслабься Мама тебе поможет. Не волнуйся, всё будет хорошо."
    scene pgn_momroom_lizasololesson_10_vezdessushij
    l emo-49 "Ммм... Аххх... Ммм..."
    m emo-3 "{i}Чёрт! Как же сильно хочу к ним.{/i}"
    l emo-49 "Мамочка, я люблю тебя..."
    scene pgn_momroom_lizasololesson_11_vezdessushij
    l emo-49 "Аххх... Аааахххх.. Ммм..."
    scene pgn_momroom_lizasololesson_12_vezdessushij
    l emo-50 "Аааххх... Ах, аааххх..."
    scene pgn_momroom_lizasololesson_13_vezdessushij
    l emo-41 "Спасибо Мам."
    mom emo-75 "Пожалуйста. Я всегда рада тебе помочь."
    $ liza_path = 41.1
    $ qtime = 23
    $ ivent24.append("мама_и_лиза_после_уроков_ванная")
    jump loc_my_room

label pgn_events_12_lizasololesson_02:
    scene pgn_momroom_lizasololesson_03_zicado
    mom emo-60 "[pname_liza[0]], ты пробовала сама?"
    l emo-40 "Нет."
    mom emo-68 "Как ты научишься, если даже не тренируешься."
    scene pgn_momroom_lizasololesson_14_vezdessushij
    mom emo-60 "Попробуем тогда вместе, иначе. Давай ко мне поближе, чтобы мы могли обе дотянуться."
label pgn_events_12_lizasololesson_02_next:
    scene pgn_momroom_lizasololesson_15_vezdessushij
    $ PGN_Achadd(pgnach_136, 136)
    mom emo-69 "Возьми немного смазки с моего влагалища и после дотронься пальчиками до моего клитора."
    mom emo-69 "Нащупала?"
    scene pgn_momroom_lizasololesson_16_vezdessushij
    l emo-43 "Да. У тебя там очень горячо и влажно. Классно!"
    if liza_path == 41.1 or pgn_ach_repeat == 136:
        l emo-43 "А можно попробовать сделать кунни тебе?"
        mom emo-68 "Что!? Ой! [pname_liza[0]]! Ты не должна... Нет, пока нет, сейчас мы занимаемся другим, так что не отвлекай."
    mom emo-69 "Итак, теперь медленно и аккуратно потри мой клитор. Влево, вправо, вверх, вниз..."
    scene pgn_momroom_lizasololesson_17_vezdessushij
    mom emo-62 "Да, вот, так, хорошо. Сильно не дави, будь нежней."
    mom emo-75 "У тебя хорошо получается моя дорогая. Помоги мамочке кончить, а я помогу тебе."
    scene pgn_momroom_lizasololesson_18_vezdessushij
    l emo-49 "Аххх... Мамочка... мне так приятно с тобой... Ммм..."
    if liza_path == 41.1 or pgn_ach_repeat == 136:
        mom emo-73 "Малышка... Аххх... Я... подожди... Хочу продемонстрировать тебе ещё один способ..."
        scene pgn_momroom_lizasololesson_19_vezdessushij
        mom emo-73 "Необязательно делать это рукой, можно тереться об поверхности мебели или использовать различные предметы, но только с осторожностью."
        l emo-41 "Или лучше об киску любимой мамочки..."
        mom emo-75 "Верно, доченька моя. Мы обе достаточно возбуждены. Расслабься солнце моё, тебе понравится."
    scene animated pgn_momroom_lizasololesson_20
    $ renpy.pause()
    $ label_random = renpy.random.randint ( 1, 3)
    if (liza_path == 41.1 or label_random == 3) and pgn_ach_repeat == 0:
        scene pgn_momroom_lizasololesson_20_15
        l emo-50 "Ааааххххх! Ммм... "
    else:
        scene pgn_momroom_lizasololesson_20_15
        mom emo-68 "Ааахх... Малышка, мамочка кончила... Аахх..."
        l emo-49 "Я тоже, мама, я тоже."
    scene pgn_momroom_lizasololesson_21_vezdessushij
    l emo-41 "Мама, это было классно! Я прям чувствовала твой жар между ног."
    mom emo-73 "Доченька... Мне тоже понравилось. Я согласна сделать всё, чтобы ты была довольной."
    scene pgn_momroom_lizasololesson_22_vezdessushij
    mom emo-62 "К следующим занятиям потренируйся сама. Хорошо?"
    l emo-41 "Да, Мама."
    if pgn_ach_repeat == 136:
        jump table_pgn_achievement
    $ liza_path, qtime = 41.2, 23
    $ ivent24.append("мама_и_лиза_после_уроков_ванная")
    jump loc_my_room

label pgn_events_12_lizasololesson_03:
    scene pgn_momroom_lizasololesson_03_zicado
    mom emo-62 "[pname_liza[0]], ты готова сейчас сделать всё сама?"
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random == 2 and pgn_ach_repeat == 0:
        l emo-49 "Нет. Может повторим, тоже самое, что на прошлом занятии?"
        mom emo-62 "Хорошо."
        jump pgn_events_12_lizasololesson_02_next
    l emo-49 "Да, но может всё же начнём вместе?"
    mom emo-60 "Нет, [pname_liza[0]], ты должна самостоятельно справиться. Если хочешь, могу включить порно."
    scene pgn_momroom_lizasololesson_23_vezdessushij
    m emo-9 "{i}Нет, [pname_liza[0]], останови её, она же может узнать...{/i}"
    l emo-40 "Мама!"
    mom emo-60 "Что такое, [pname_liza[0]]?"
    l emo-49 "Мне не нужно ни какое порно. Может просто... ты..."
    scene pgn_momroom_lizasololesson_24_vezdessushij
    mom emo-73 "Предлагаешь мне помастурбировать перед тобой?"
    l emo-41 "Да. Если конечно не против? "
    l emo-48 "Я не хочу смотреть на каких-то дяденек или тёть. Мама, ты очень красивая и будет лучше, если это будешь ты."
    mom emo-75 "Ох, малышка. Хорошо, я это сделаю."
    m emo-1 "{i}Фух. Пронесло{/i}"
    scene pgn_momroom_lizasololesson_25_vezdessushij
    mom emo-73 "[pname_liza[0]], может сядешь нормально и не так близко."
    scene pgn_momroom_lizasololesson_26_vezdessushij
    l emo-48 "Мне так удобнее и хорошо видно. Не хочу ничего упустить."
    mom emo-69 "Хорошо. Смотри внимательней."
    scene animated pgn_momroom_lizasololesson_27
    $ renpy.pause()
    scene pgn_momroom_lizasololesson_28_vezdessushij
    mom emo-62 "Думаю достаточно. Попробуй теперь сама."
    l emo-41 "Да, Мама."
    scene pgn_momroom_lizasololesson_30_vezdessushij
    mom emo-62 "Не забывай про смазку."
    scene pgn_momroom_lizasololesson_29_vezdessushij
    mom emo-75 "Не торопись. Продолжай."
    scene pgn_momroom_lizasololesson_31_vezdessushij
    $ PGN_Achadd(pgnach_137, 137)
    m emo-4 "{i}Ох! Я бы к ним присоединился. Пока [pname_liza[0]] занята мастурбацией, я бы занялся маминой попкой.{/i}"
    scene animated pgn_momroom_lizasololesson_32
    $ renpy.pause()
    l emo-49 "{i}Член братика. Хочу член моего любимого братика.{/i}"
    scene pgn_momroom_lizasololesson_33_vezdessushij
    l emo-50 "Ааааххх... Ммм... Аххх..."
    scene pgn_momroom_lizasololesson_34_vezdessushij
    l emo-49 "Мама, ты не против, если я сегодня посплю у тебя?"
    mom emo-75 "Доченька, конечно можно. Только сначала в ванную, а потом спать."
    m emo-8 "{i}Ээээ! А почему это ей можно, а мне до сих пор нельзя!? Это не честно.{/i}"
    if pgn_ach_repeat == 137:
        jump table_pgn_achievement
    $ liza_path, qtime, days_liza = 42, 23, days+1
    $ ivent24.append("лиза_спит_у_мамы")
    $ ivent24.append("мама_и_лиза_после_уроков_ванная")
    jump loc_my_room


label pgn_events_12_lizasololesson_start:
    scene pgn_momroom_lizasololesson_03_zicado
    mom emo-60 "[pname_liza[0]], с чего начнём?"
    if ("урок_мастурбации_лизы_мамасоло") in ivent24:
        l emo-41 "Мама, а покажи ещё раз на себе, как нужно это делать."
        mom emo-62 "Хорошо, моя дорогая."
        $ ivent24.remove("урок_мастурбации_лизы_мамасоло")
        jump pgn_events_12_lizasololesson_momsolo
    elif ("урок_мастурбации_лизы_мамаилиза") in ivent24:
        l emo-49 "Хочу как тогда, вместе."
        mom emo-62 "Конечно."
        $ ivent24.remove("урок_мастурбации_лизы_мамаилиза")
        jump pgn_events_12_lizasololesson_momliza
    elif ("урок_мастурбации_лизы_лизасоло") in ivent24:
        l emo-41 "Я попробую сама, а ты посмотришь, правильно ли я делаю."
        $ ivent24.remove("урок_мастурбации_лизы_лизасоло")
        jump pgn_events_12_lizasololesson_lizasolo


label pgn_events_12_lizasololesson_momsolo:
    scene pgn_momroom_lizasololesson_25_vezdessushij
    mom emo-73 "[pname_liza[0]], смотри внимательно."
    scene pgn_momroom_lizasololesson_26_vezdessushij
    mom emo-69 "Сначала задействую одну руку."
    scene animated pgn_momroom_lizasololesson_27
    $ renpy.pause()
    scene pgn_momroom_lizasololesson_28_vezdessushij
    mom emo-69 "Внимательно смотришь?"
    l emo-41 "Да, Мама."
    scene animated pgn_momroom_lizasololesson_27
    $ renpy.pause()
    scene pgn_momroom_lizasololesson_28_vezdessushij
    mom emo-69 "Вот так... Ммм... Медленно и осторожно..."
    mom emo-69 "Постепенно можно увеличить скорость и задействовать вторую руку."
    scene animated pgn_momroom_lizasololesson_07
    $ renpy.pause()
    mom emo-73 "Мммм... Аххх.. Аххх..."
    $ renpy.pause()
    if ("урок_мастурбации_лизы_мамаилиза") in ivent24:
        scene pgn_momroom_lizasololesson_08_vezdessushij
        l emo-41 "А давай теперь вместе?"
        mom emo-62 "Конечно, малышка."
        $ ivent24.remove("урок_мастурбации_лизы_мамаилиза")
        jump pgn_events_12_lizasololesson_momliza
    elif ("урок_мастурбации_лизы_лизасоло") in ivent24:
        scene pgn_momroom_lizasololesson_08_vezdessushij
        l emo-41 "А теперь я."
        $ ivent24.remove("урок_мастурбации_лизы_лизасоло")
        jump pgn_events_12_lizasololesson_lizasolo
    scene pgn_momroom_lizasololesson_07_15 with dissolve
    mom emo-68 "Аааххх... Аааххх..."
    scene pgn_momroom_lizasololesson_08_vezdessushij
    mom emo-73 "Надеюсь ты всё запомнила."
    l emo-41 "Всё и мне понравилось."
    mom emo-73 "Мне... тоже..."
    mom emo-62 "Пойдём в ванную."
    $ qtime = 23
    jump loc_my_room


label pgn_events_12_lizasololesson_momliza:
    scene pgn_momroom_lizasololesson_14_vezdessushij
    mom emo-60 "Давай ко мне поближе, чтобы мы могли обе дотянуться."
    scene pgn_momroom_lizasololesson_15_vezdessushij
    mom emo-69 "Возьми немного смазки с моего влагалища и после дотронься пальчиками до моего клтора."
    scene pgn_momroom_lizasololesson_16_vezdessushij
    l emo-43 "Да. У тебя там очень горячо и влажно. Классно!"
    scene pgn_momroom_lizasololesson_17_vezdessushij
    mom emo-62 "Да, вот, так, хорошо. Ласковее доченька, да вот так."
    mom emo-75 "У тебя хорошо получается моя дорогая."
    scene pgn_momroom_lizasololesson_18_vezdessushij
    l emo-49 "Аххх... Мамочка... мне так приятно с тобой... Ммм..."
    scene animated pgn_momroom_lizasololesson_20
    $ renpy.pause()
    scene pgn_momroom_lizasololesson_20_15
    if ("урок_мастурбации_лизы_лизасоло") in ivent24:
        l emo-41 "Можно теперь я сама?"
        mom emo-62 "Хорошо, а я проконтролирую."
        $ ivent24.remove("урок_мастурбации_лизы_лизасоло")
        jump pgn_events_12_lizasololesson_lizasolo
    mom emo-68 "Ааахх... Малышка, мамочка кончила... Аахх..."
    l emo-49 "Я тоже, мама, я тоже."
    scene pgn_momroom_lizasololesson_21_vezdessushij
    l emo-41 "Мама, это было классно!"
    mom emo-73 "Доченька... Мне тоже понравилось."
    scene pgn_momroom_lizasololesson_22_vezdessushij
    mom emo-62 "Пойдём в ванную."
    $ qtime = 23
    jump loc_my_room

label pgn_events_12_lizasololesson_lizasolo:
    scene pgn_momroom_lizasololesson_30_vezdessushij
    mom emo-62 "Не забывай про смазку."
    scene pgn_momroom_lizasololesson_29_vezdessushij
    mom emo-75 "Не торопись. Продолжай."
    scene pgn_momroom_lizasololesson_31_vezdessushij
    m emo-2 "{i}Какого фига я здесь, почему не с ними.{/i}"
    scene animated pgn_momroom_lizasololesson_32
    $ renpy.pause()
    l emo-49 "{i}Братик смотрит на меня. Люблю братика, люблю его большой...{/i}"
    scene pgn_momroom_lizasololesson_33_vezdessushij
    l emo-50 "Ааааххх... Ммм... Аххх..."
    scene pgn_momroom_lizasololesson_34_vezdessushij
    l emo-41 "Я всё правильно делала?"
    mom emo-62 "Раз смогла сама достигнуть оргазма, то да."
    $ qtime = 23
    jump loc_my_room

label pgn_events_12_lizasololesson_04:
    m emo-3 "Ещё будут эти ваши совместные уроки мастурбации?"
    l emo-41 "Мама сказала, что раз я смогла сама, то больше не требуется занятий."
    l emo-48 "А что? Понравилось и хочется ещё посмотреть на меня с мамой?"
    menu:
        "Да, очень":
            l emo-41 "Тогда, как обычно, вечером принеси мне ноутбук, а я Маму попрошу провести ещё одно занятие."
            m emo-3 "Договорились."
        "Мне хватило":
            l emo-40 "Ясно."
    l emo-41 "[pname_max[0]]."
    m emo-0 "Что?"
    l emo-41 "У меня есть одна идея. Можешь попросить Маму провести урок по кунилингусу?"
    m emo-3 "Да. А что за идея?"
    l emo-41 "Не скажу. Просто сделай это и потом сам всё узнаешь."
    m emo-0 "Ладно."
    $ liza_path = 42.1
    jump jump_dialogue

label pgn_events_12_lizasololesson_05:
    scene pgn_momroom_lessoncunninext_01_vezdessushij
    if liza_path == 42.1 or pgn_ach_repeat == 138:
        mom emo-68 "[pname_liza[0]], почему ты остановилась? Что-то не так?"
        l emo-49 "Мама, а ты можешь проверить?"
        mom emo-67 "Что проверить, доченька?"
        l emo-49 "Правильно ли [pname_max[0]] лижет мою киску."
        mom emo-69 "[pname_liza[0]], я... я не могу. Ну, ты же получаешь удовольствие от того что делает [pname_max[0]] языком?"
        l emo-40 "Так то да, но а вдруг он что-то не так делает, а я же не знаю как правильно. Да и в прошлых уроках ты делала ему минет, пусть в этот раз сделает тебе приятное."
        mom emo-68 "[pname_liza[0]], я провожу уроки, чтобы вы чему-то научились, до того как у вас появятся та и тот, кого вы полюбите. Уроки с целью обучения, а не получения удовольствий."
        m emo-0 "{i}Эх, Мама! Старается как может.{/i}"
        l emo-41 "Ну Мама, пожалуйста. Если он делает всё правильно, тогда уроки нам больше не нужны. И ты научила нас всему, что нужно."
        scene pgn_momroom_lessoncunninext_02_vezdessushij
        mom emo-69 "Эм... Ну... Хорошо."
        scene pgn_momroom_lessoncunninext_03_vezdessushij
        mom emo-73 "Я это делаю только в образовательных целях."
        l emo-41 "Да Мама. А я тогда продолжу делать минет братику."
    else:
        l emo-41 "Мама. Хочешь проверить [pname_max[0]]? Может он стал лучше делать."
        mom emo-68 "Хорошо, я проверю."
    scene pgn_momroom_lessoncunninext_04_vezdessushij
    if liza_path == 42.1 or pgn_ach_repeat == 138:
        m emo-4 "Мама, не стесняйся, садись мне на лицо, сейчас покажу мастер-класс."
        mom emo-68 "[pname_max[0]]!"
    else:
        m emo-1 "{i}Я бы сейчас трахнул эту попку.{/i}"
    scene pgn_momroom_lessoncunninext_05_vezdessushij
    m emo-5 "{i}Мамина киска очень мокрая. И минуты не прошло, а её соки текут мне в рот.{/i}"
    scene pgn_momroom_lessoncunninext_06_vezdessushij
    m emo-3 "{i}[pname_liza[0]] вообще ускорилась и стала активнее сосать.{/i}"
    scene pgn_momroom_lessoncunninext_07_vezdessushij
    if liza_path == 42.1 or pgn_ach_repeat == 138:
        m emo-4 "{i}Как же круто. Надеюсь так скоро и до секса дойдёт, хотя бы анального. [pname_liza[2]] нравится, а Мама бурно кончает.{/i}"
    m emo-10 "{i}Блин! Сейчас я кончу. Но не могу предупредить, рот занят{/i}"
    scene pgn_momroom_lessoncunninext_08_vezdessushij
    m emo-10 "Мммм... Мхм... Мхм..."
    scene pgn_momroom_lessoncunninext_09_vezdessushij
    l emo-48 "Мама, а братик уже кончил. Осталась только ты, Мам. [pname_max[0]] правильно всё делает?"
    mom emo-73 "Пока не знаю."
    if liza_path == 42.1 or pgn_ach_repeat == 138:
        m emo-11 "{i}Хм... Что? Ну ладно, держись мамочка.{/i}"
    scene pgn_momroom_lessoncunninext_10_vezdessushij
    $ PGN_Achadd(pgnach_138, 138)
    mom emo-68 "Аххх... [pname_max[0]]... Полегче..."
    scene pgn_momroom_lessoncunninext_11_vezdessushij
    mom emo-68 "Аааахххх... Ахххх..."
    scene pgn_momroom_lessoncunninext_12_vezdessushij
    if liza_path == 42.1 or pgn_ach_repeat == 138:
        l emo-40 "Ну как Мам, [pname_max[0]] правильно всё делает, т.е. нам больше не нужны уроки, мы всему научились?"
        m emo-5 "{i}Из маминой киски капает и она так сильно кончила, что рухнула на кровать. Так что я был супер!{/i}"
    else:
        m emo-3 "{i}На этот я точно справился на отлично.{/i}"
    scene pgn_momroom_lessoncunninext_13_vezdessushij
    mom emo-62 "Вам ещё есть чему учиться."
    if liza_path == 42.1 or pgn_ach_repeat == 138:
        mom emo-73 "[pname_max[0]]... Справился на четверку."
        m emo-9 "{i}Какого? В смысле на 4, да я тут на твердую 10-ку по 5 бальной шкале.{/i}"
    else:
        m emo-1 "{i}Ну и врунья Мама, но я не против.{/i}"
    l emo-43 "Ну вот [pname_max[0]], значит продолжим обучение."
    mom emo-69 "Я ещё немного полежу, а вы тихо, пока [pname_alice[0]] вас не увидела, идите в душ."
    l emo-41 "Да, Мама."
    if pgn_ach_repeat == 138:
        jump table_pgn_achievement
    if liza_path == 42.1:
        $ liza_path, days_liza = 42.2, days+3
    $ qtime += 1
    $ PGN_Addstatsex(stat_liza, 0, 1, 1, 0, 0)
    $ PGN_Addstatsex(stat_mom, 0, 1, 0, 0, 0)
    jump loc_my_room

label pgn_events_12_lizasololesson_06:
    scene pgn_myroom_lizaspeak_23
    l emo-41 "[pname_max[0]], я тут поговорила с Мамой о наших уроках."
    m emo-13 "А что не так с ними?"
    l emo-49 "Практика"
    m emo-6 "Что практика?"
    l emo-48 "Я уговорила Маму, что нам нужно больше практики. Так что мы можем этим заниматься вне уроков."
    m emo-9 "Да ладно. Ты шутишь? Или да, или нет? Как тебе удалось?"
    l emo-41 "Просто получилось."
    m emo-4 "Круто."
    l emo-48 "Только не забывай, что практика для нас обоих. Я по минету, а ты по лизанию моей киски."
    m emo-3 "Отличные новости."
    l emo-41 "..."
    m emo-13 "Сейчас, я?"
    l emo-49 "..."
    scene pgn_myroom_lizacunniwork_02
    l emo-48 "Ммм... [pname_max[0]], языком, без пальцев."
    scene pgn_myroom_lizacunniwork_03
    l emo-49 "Аххх... Мммм... Аааххх..."
    scene pgn_myroom_lizacunniwork_04
    m emo-3 "Твоя киска отлично смотрится."
    l emo-41 "Не болтай, а делом займись."
    m emo-1 "Да, да."
    scene pgn_myroom_lizacunniwork_05
    l emo-50 "Ааахххх... Аааааххх..."
    scene pgn_myroom_lizacunniwork_06
    l emo-41 "Спасибо. Потом моя очередь сделать тебе приятное. И иногда заглядывай к нам в ванную, после уроков."
    m emo-3 "Понял. Жду не дождусь твоего ротика. И это, ещё кое что..."
    l emo-41 "Не переживай, [pname_alice[2]] ничего не расскажу."
    l emo-41 "Ну всё, не мешай. Мне нужно ещё домашнее задание сделать."
    $ liza_path, qtime = 43, 24
    $ accessiv.append("урокисекса_практика_макс_впервые")
    jump loc_my_room


label pgn_events_12_lizasololesson_07:
    l emo-41 "И чем же?"
    scene pgn_myroom_lizacunniwork_01
    m emo-3 "Сейчас всё поймешь."
    scene pgn_myroom_lizacunniwork_02
    l emo-48 "Ой! [pname_max[0]]! Я не смогу так уроки делать."
    l emo-49 "Аххх! Ммм... [pname_max[0]]..."
    scene pgn_myroom_lizacunniwork_03
    l emo-49 "Аааахххх... Аххх... Ммм..."
    scene pgn_myroom_lizacunniwork_04
    l emo-46 "[pname_max[0]], помедленней. Ммм..."
    scene pgn_myroom_lizacunniwork_03
    l emo-49 "[pname_max[0]]! Аххх... Не останавливайся... Почти..."
    scene pgn_myroom_lizacunniwork_05
    l emo-50 "Ааааххх! Ааааахх..."
    scene pgn_myroom_lizacunniwork_01
    $ renpy.pause(1.5)
    scene pgn_myroom_lizacunniwork_06
    m emo-4 "Ну что в расчёте?"
    $ label_random = renpy.random.randint ( 1, 2)
    if label_random == 1:
        l emo-41 "Да. Спасибо. Только, может поможешь с уроками? А то ничего не успею сделать."
        menu:
            "Помочь":
                m emo-3 "Да, конечно помогу."
                l emo-41 "Спасибо"
            "Отказаться":
                m emo-0 "Извини, не могу. Есть ещё дела у меня."
                l emo-40 "Жаль."
                $ liza_homework_error = True
                $ accessiv.append("homework_liza_наказание_макса")
    else:
        l emo-41 "Да, братик. В следующий раз моя очередь."
    $ qtime += 1
    $ accessiv.remove("урокисекса_практика_лиза")
    $ accessiv.append("урокисекса_практика_макс")
    $ liza_sex_bj = 4
    $ PGN_Addstatsex(stat_liza, 0, 1, 0, 0, 0)
    jump loc_my_room


label pgn_events_12_lizasololesson_08:
    scene pgn_myroom_liza_solonight_10
    l emo-46 "[pname_max[0]]. Я хочу спать, зачем меня разбудил?"
    m emo-1 "Моя очередь сделать тебе приятное."
    l emo-46 "А после спать."
    m emo-3 "Конечно. Потом будет только приятнее сон."
    scene pgn_myroom_liza_solonight_06
    l emo-43 "Заставь меня кончить или не дам тебе уснуть, раз меня разбудил."
    m emo-4 "Брат обязательно поможет миленькой сестрёнке."
    scene animated pgn_myroom_liza_solonight_07
    $ renpy.pause()
    l emo-49 "[pname_max[0]], я скоро, не останавливайся."
    $ renpy.pause()
    scene pgn_myroom_liza_solonight_08
    l emo-50 "Ааххх..."
    scene pgn_myroom_liza_solonight_10
    l emo-41 "Спасибо [pname_max[0]]."
    m emo-3 "Обращайся."
    $ accessiv.remove("урокисекса_практика_лиза")
    $ accessiv.append("урокисекса_практика_макс")
    $ qtime, liza_sex_bj = qtime+1, 4
    $ ivent24.append("lizabracelets")
    $ PGN_Addstatsex(stat_liza, 0, 1, 0, 0, 0)
    jump loc_my_room


label pgn_events_12_lizasololesson_09:
    if ("урокисекса_практика_лиза") in accessiv and pgn_ach_repeat == 0:
        l emo-41 "Не против. Но сейчас твоя очередь сделать мне приятное."
        jump pgn_events_12_lizasololesson_09_cunni
    if ("урокисекса_практика_макс") in accessiv or ("урокисекса_практика_макс_впервые") in accessiv or pgn_ach_repeat == 140:
        if ("урокисекса_практика_макс_впервые") in accessiv:
            $ accessiv.remove("урокисекса_практика_макс_впервые")
        l emo-41 "Снимай шорты."

    scene pgn_lizabath_lessonpractice_bj_01_vadx
    menu:
        "Взяться за голову" if pgn_ach_repeat == 0:
            scene pgn_lizabath_lessonpractice_bj_02_vadx
            l emo-44 "[pname_max[0]]! Убери руки. Я должна сама все делать, без твоей помощи."
            menu:
                "Ближе к члену":
                    scene pgn_lizabath_lessonpractice_bj_03_vadx
                    m emo-4 "Давай попробуем. Я сильно и глубоко засовывать не буду."
                    l emo-40 "[pname_max[0]]. Нет. Не хочу. Отпусти!"
                    scene pgn_lizabath_lessonpractice_bj_04
                    l emo-42 "Всё! Я больше не хочу сосать твой член."
                    m emo-2 "[pname_liza[0]], прости. Я не знаю что на меня нашло."
                    scene pgn_lizabath_lessonpractice_bj_01_vadx
                    l emo-41 "Ну хорошо."
                    m emo-3 "Правда? Класс!"
                    scene pgn_lizabath_lessonpractice_bj_04
                    l emo-42 "Нет. Уходи, пока я Маму не позвала."
                    $ qtime, lizasex_alice = qtime+1, True
                    jump loc_bathroom
                "Убрать руки":
                    scene pgn_lizabath_lessonpractice_bj_01_vadx
                    l emo-40 "Спасибо. Я начинаю. Только ни каких рук. Ладно?"
                    m emo-0 "Да, извини."
        "Продолжить":
            pass
    scene animated pgn_lizabath_lessonpractice_bj_05
    menu:
        "Наблюдать за Мамой":
            scene pgn_lizabath_lessonpractice_bj_06_vadx
            m emo-3 "{i}Мама занята йогой. Думаю, [pname_liza[0]] не будет против, если некоторое время понаблюдаю за мамой.{/i}"
            scene pgn_lizabath_lessonpractice_bj_07_vadx
            $ renpy.pause(3)
            scene pgn_lizabath_lessonpractice_bj_08_vadx
            mom emo-60 "{i}Хм... [pname_max[0]] сегодня не пришёл. Ладно, тогда продолжу, как обычно.{/i}"
            scene pgn_lizabath_lessonpractice_bj_09_vadx
            $ PGN_Achadd(pgnach_140, 140)
            m emo-9 "{i}Ого! Мама снимает шорты! Блин. Я не знал что Мама занимается йогой совсем голой. Или она это недавно начала?{/i}"
            scene pgn_lizabath_lessonpractice_bj_10b_vadx
            $ renpy.pause(4)
            scene pgn_lizabath_lessonpractice_bj_10a_vadx with dissolve
            $ renpy.pause(2)
            scene pgn_lizabath_lessonpractice_bj_10b_vadx with dissolve
            $ renpy.pause(2)
            scene pgn_lizabath_lessonpractice_bj_10a_vadx with dissolve
            $ renpy.pause(2)
            scene pgn_lizabath_lessonpractice_bj_11_vadx
            m emo-4 "{i}Мамина попка шикарна.{/i}"
            scene pgn_lizabath_lessonpractice_bj_12_vadx
            $ renpy.pause(3)
            scene pgn_lizabath_lessonpractice_bj_13_vadx
            $ renpy.pause(3)
            scene pgn_lizabath_lessonpractice_bj_14_vadx
            $ renpy.pause(3)
            $ label_random = renpy.random.randint ( 1, 4)
            if label_random == 1 and pgn_ach_repeat == 0 and "walkthrough_light" not in accessiv:
                l emo-42 "[pname_max[0]], не отвлекайся"
                m emo-0 "Извини."
                scene animated pgn_lizabath_lessonpractice_bj_05
                $ renpy.pause()
            elif label_random == 2 and "walkthrough_light" not in accessiv:
                pass
            elif ((label_random != 1 and label_random != 2) or ("walkthrough_light" in accessiv and liza_path == 43)) and pgn_ach_repeat == 0:
                jump pgn_events_12_lizasololesson_09_mom
            scene pgn_lizabath_lessonpractice_bj_16_vadx
            m emo-12 "Аргхх...!!"
            scene pgn_lizabath_lessonpractice_bj_17_vadx
            l emo-48 "Ай! [pname_max[0]]!"
            scene pgn_lizabath_lessonpractice_bj_18_vadx
            m emo-2 "Извини!"
        "Не отвлекаться" if pgn_ach_repeat == 0:
            label pgn_events_12_lizasololesson_09_next:
                scene animated pgn_lizabath_lessonpractice_bj_05
                $ renpy.pause()
                menu:
                    "Кончить в рот":
                        scene pgn_lizabath_lessonpractice_bj_19_vadx
                        l emo-41 "Мхмм..."
                        scene pgn_lizabath_lessonpractice_bj_20_vadx
                        l emo-41 "Аааа..."
                        scene pgn_lizabath_lessonpractice_bj_01_vadx
                    "Кончить на неё":
                        scene pgn_lizabath_lessonpractice_bj_16_vadx
                        m emo-12 "Аргхх...!!"
                        scene pgn_lizabath_lessonpractice_bj_17_vadx
                        l emo-48 "Ай! [pname_max[0]]!"
                        scene pgn_lizabath_lessonpractice_bj_18_vadx
                        m emo-2 "Извини!"
    l emo-43 "Понравилось?"
    m emo-4 "Да. С каждым разом всё лучше и лучше. "
    m emo-2 "{i}Хотя, если бы могла ещё и глубокий минет, то цены бы не было.{/i}"

    if pgn_ach_repeat == 140:
        jump table_pgn_achievement

    $ qtime, liza_sex_bj = qtime+1, 4
    if ("урокисекса_практика_макс") in accessiv:
        $ accessiv.remove("урокисекса_практика_макс")
    $ accessiv.append("урокисекса_практика_лиза")
    $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
    jump loc_bathroom


label pgn_events_12_lizasololesson_09_mom:
    if liza_path == 43 and ("урокисекса_практика_лока_ванная_у_минет") not in accessiv and pgn_ach_repeat == 0:
        $ accessiv.append("урокисекса_практика_лока_ванная_у_минет")
        scene pgn_lizabath_lessonpractice_bj_22_vadx
        mom emo-66 "[pname_max[0]], [pname_liza[0]]! Вы что это?"
        l emo-41 "Привет Мама!"
        m emo-13 "При-и-и-вет! Как йога!?"
        mom emo-64 "Ну как так можно, [pname_max[0]], мешать [pname_liza[2]] принимать душ?"
        m emo-13 "Эм..."
        l emo-48 "Мама, он ни в чём не виноват. Ты же мне разрешила тренироваться. Вот захотелось мне совместить приятное с полезным."
        scene pgn_lizabath_lessonpractice_bj_21_vadx
        mom emo-69 "Да, но..."
        l emo-41 "А хочешь тоже? А я как раз домоюсь и пойду к себе."
        mom emo-73 "Я... я не могу. Мне ещё завтрак вам нужно приготовить."
        l emo-49 "Тогда не против, если я закончу. А то братику придётся с, этим, с нами сидеть за столом."
        mom emo-69 "Да. Конечно, продолжайте..."
        jump pgn_events_12_lizasololesson_09_next
    elif liza_path == 43 and ("урокисекса_практика_лока_ванная_у_минет") in accessiv and pgn_ach_repeat == 0:
        scene pgn_lizabath_lessonpractice_bj_22_vadx
        l emo-41 "Мам, привет! Не хочешь меня заменить?"
        mom emo-73 "[pname_liza[0]], эм... Я не могу. И при этом это ты же тренируешься делать минет."
        mom emo-68 "И... И я не должна делать это с сыном, я же мать."
        scene pgn_lizabath_lessonpractice_bj_21_vadx
        m emo-3 "{i}Да она хочет, только не может признаться [pname_liza[2]], что хочет этот член.{/i}"
        mom emo-73 "Продолжайте. Я не буду вам мешать."
        jump pgn_events_12_lizasololesson_09_next
    else:
        scene pgn_lizabath_lessonpractice_bj_21_vadx
        l emo-41 "Привет Мама!"
        mom emo-66 "Ой! Я не буду вам мешать."
        scene pgn_lizabath_lessonpractice_bj_23_vadx
        l emo-48 "Мама, постой! Я уже помылась, так что может поможешь вместо меня [pname_max[2]]? "
        mom emo-73 "Ну я..."
        l emo-40 "Всё равно мне нужно пару своих дел сделать у себя в комнате. И для [pname_max[1]] ведь вредно, если он не кончит?"
        mom emo-75 "Да, ты права, малышка. Хорошо, я помогу [pname_max[2]]. А ты [pname_max[0]], после поможешь мне потом с готовкой."
        scene pgn_lizabath_lessonpractice_bj_24_vadx
        $ PGN_Achadd(pgnach_141, 141)
        if ("ванная_утро_глубокглоткамама") not in accessiv or pgn_ach_repeat == 141:
            if pgn_ach_repeat == 0:
                $ accessiv.append("ванная_утро_глубокглоткамама")
            mom emo-68 "Мне тут [pname_liza[0]] сказала, что по твоему мнению, она стала лучше делать минеты, лучше чем я. Это так сынок?"
            m emo-1 "Эм... А... Мама! Я ничего такого не говорил, она всё придумала. Ты лучше всех."
            mom emo-75 "Спасибо, [pname_max[0]]."
            mom emo-60 "С нашего с ней последнего разговора, я поняла, что мне тоже нужно больше практики."
            m emo-0 "Практики? Ну ты и так..."
            scene pgn_lizabath_lessonpractice_bj_25_vadx
            $ renpy.pause(1)
            scene pgn_lizabath_lessonpractice_bj_26_vadx
            $ renpy.pause(1)
            scene pgn_lizabath_lessonpractice_bj_27_vadx
            m emo-9 "{i}Мама всё глубже и глубже.{/i}"
            scene pgn_lizabath_lessonpractice_bj_24_vadx
            m emo-0 "Я правильно понимаю, ты хочешь сделать..."
            mom emo-62 "Да сынок. Хочу сделать тебе глубокий минет. Но только для [pname_liza[1]] это ещё рано делать и она не сможет, так что даже не пытайтесь меня уговаривать."
            m emo-0 "Понял."
            mom emo-75 "Тогда я начинаю, а то времени не так много у меня."
            scene animated pgn_lizabath_lessonpractice_bj_28
            $ renpy.pause()
            m emo-3 "{i}Вот это неожиданность, приятный сюрприз.{/i}"
            m emo-10 "{i}Ох блин! Я на пределе.{/i}"
            scene animated pgn_lizabath_lessonpractice_bj_29
            m emo-10 "{i}Вау! Мамино горло сжимает член.{/i}"
            m emo-12 "Ох! Ааа... Ох... Ааа..."
            scene pgn_lizabath_lessonpractice_bj_30_vadx
            mom emo-75 "Спасибо тебе, сынок."
            m emo-5 "{i}Это тебе спасибо.{/i}"
        else:
            mom emo-62 "Мамочка сейчас снова сделает любимому сыну глубокий минет."
            mom emo-75 "Ты же хочешь наполнить мой животик?"
            m emo-4 "Да! Ох блин, да... Конечно!"
            scene pgn_lizabath_lessonpractice_bj_25_vadx
            $ renpy.pause(1)
            scene pgn_lizabath_lessonpractice_bj_26_vadx
            $ renpy.pause(1)
            scene pgn_lizabath_lessonpractice_bj_27_vadx
            $ renpy.pause(1)
            scene animated pgn_lizabath_lessonpractice_bj_28
            $ renpy.pause()
            scene animated pgn_lizabath_lessonpractice_bj_29
            $ renpy.pause()
            scene animated pgn_lizabath_lessonpractice_bj_28
            $ renpy.pause()
            m emo-10 "Мама, я сейчас..."
            scene pgn_lizabath_lessonpractice_bj_29_15
            m emo-12 "Арргххх! Ааааххх... Да..."
            scene animated pgn_lizabath_lessonpractice_bj_29
            m emo-10 "{i}Мама без рук выжимает остатки спермы. Ей даже этого мало.{/i}"
            scene pgn_lizabath_lessonpractice_bj_30_vadx
            mom emo-75 "Спасибо тебе, [pname_max[0]]. Я тебя очень люблю."
            m emo-4 "Я тоже."

    if pgn_ach_repeat == 141:
        jump table_pgn_achievement

    $ qtime, liza_sex_bj = qtime+1, 4
    if ("урокисекса_практика_макс") in accessiv:
        $ accessiv.remove("урокисекса_практика_макс")
    $ accessiv.append("урокисекса_практика_лиза")
    $ ivent24.append("momyogasex")
    $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
    $ PGN_Addstatsex(stat_mom, 0, 0, 1, 0, 0)
    jump loc_bathroom


label pgn_events_12_lizasololesson_09_cunni:
    scene pgn_lizabath_lessonpractice_cunni_31
    m emo-3 "У тебя там всё мокро."
    l emo-41 "Конечно, я же душ принимала, пока ты не пришёл."
    scene pgn_lizabath_lessonpractice_cunni_32
    l emo-49 "Аххх... Ахх... Ммм... Братик..."
    scene pgn_lizabath_lessonpractice_cunni_33
    l emo-49 "Братик... Мммм... [pname_max[0]]... Остановись."
    scene pgn_lizabath_lessonpractice_cunni_34
    m emo-6 "Я что-то не так делаю?"
    l emo-41 "Всё так. Просто... иди за мной."
    scene pgn_lizabath_lessonpractice_cunni_35
    m emo-3 "{i}Сестрёнка завелась и захотела секса?{/i}"
    scene pgn_lizabath_lessonpractice_cunni_36
    l emo-41 "Я готова."
    menu:
        "Секс":
            scene pgn_lizabath_lessonpractice_cunni_37
            l emo-44 "Нет, [pname_max[0]]. А иначе закричу."
            m emo-3 "Точно?"
            l emo-46 "Хорошо, не закричу. Но пожалуйста, продолжи языком."
            m emo-2 "{i}А так хотелось. Тогда отложу на потом.{/i}"
        "Мастурбировать":
            scene pgn_lizabath_lessonpractice_cunni_38
            l emo-40 "[pname_max[0]]. Я понимаю, что тебе хочется кончить, но сейчас твоя очередь доставить мне удовольствие."
        "Продолжить куни":
            pass
    scene pgn_lizabath_lessonpractice_cunni_39
    l emo-41 "Ммм... Братик, продолжай. Сестренке очень нравится."
    scene pgn_lizabath_lessonpractice_cunni_40
    l emo-49 "Мне так хорошо. Ммм... Да..."
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random == 2 or (("урокисекса_практика_лока_ванная_у_куни") not in accessiv and liza_path == 43) or pgn_ach_repeat == 142:
        scene pgn_lizabath_lessonpractice_cunni_41
        mom emo-60 "Дети!"
        l emo-41 "Привет, Мам. А мы тут..."
        mom emo-60 "Помощь нужна?"
        l emo-41 "Нет, [pname_max[0]] справляется. Но если хочешь, можешь присоединиться?"
        mom emo-62 "Нет, спасибо. Я умоюсь и пойду вам завтрак готовить."
        scene pgn_lizabath_lessonpractice_cunni_43
        $ PGN_Achadd(pgnach_142, 142)
        l emo-49 "Аааххх... Ммм... Аххх..."
        scene pgn_lizabath_lessonpractice_cunni_44
        m emo-2 "[pname_liza[0]], может поза 69? Я тоже хочу кончить."
        l emo-40 "[pname_max[0]], продолжай лизать."
        scene pgn_lizabath_lessonpractice_cunni_45
        m emo-0 "Мама?!"
        mom emo-60 "Не обращай на меня внимание, продолжай."
        m emo-0 "Ок."
        scene pgn_lizabath_lessonpractice_cunni_46
        m emo-5 "{i}О, да! Спасибо тебе Мама. Я был бы не против минета, но так тоже хорошо.{/i}"
        scene pgn_lizabath_lessonpractice_cunni_47
        l emo-49 "Аааххх... Аааххх... [pname_max[0]], не останавливайся, быстрее..."
        m emo-10 "{i}Я сам у же на пределе.{/i}"
        l emo-49 "[pname_max[0]], [pname_max[0]], [pname_max[0]]..."
        scene pgn_lizabath_lessonpractice_cunni_48
        l emo-50 "Аааахххх..."
        m emo-10 "Ааарггхх... Ааахх..."
        scene pgn_lizabath_lessonpractice_cunni_49
        m emo-3 "Мама, спасибо тебе, за... помощь."
        mom emo-62 "Не за что."
        l emo-49 "Я думала, что только я получу удовольствие. А [pname_max[2]], я бы потом помогла."

        if pgn_ach_repeat == 142:
            jump table_pgn_achievement

        $ PGN_Addstatsex(stat_mom, 0, 0, 0, 0, 1)
    else:
        scene pgn_lizabath_lessonpractice_cunni_50
        l emo-41 "Ааахх... Братик..."
        scene pgn_lizabath_lessonpractice_cunni_51
        l emo-41 "Аааххх... Ммм... Аааххх..."
        scene pgn_lizabath_lessonpractice_cunni_36
    m emo-3 "Следующая твоя очередь."
    l emo-41 "Знаю."
    if ("урокисекса_практика_лока_ванная_у_куни") not in accessiv and liza_path == 43:
        $ accessiv.append("урокисекса_практика_лока_ванная_у_куни")
    if ("урокисекса_практика_лиза") in accessiv:
        $ accessiv.remove("урокисекса_практика_лиза")
    $ accessiv.append("урокисекса_практика_макс")
    $ qtime, liza_sex_bj = qtime+1, 4
    $ PGN_Addstatsex(stat_liza, 0, 1, 0, 0, 0)
    jump loc_bathroom


label pgn_events_12_lizasololesson_10a:
    scene pgn_bath_momliza_afterlesson_02_vezdessushij
    mom emo-60 "[pname_max[0]]. Я же сказала, что мы заняты, почему вошёл?"
    m emo-3 "А чего стесняться, голыми уже видели друг друга."
    mom emo-60 "[pname_max[0]], всё равно так нельзя. Выйди, пожалуйста."
    menu:
        "[pname_liza[0]] попросила зайти":
            m emo-0 "[pname_liza[0]] просила меня зайти."
            label pgn_events_12_lizasololesson_10b:
                if liza_path >= 44  or ("урокисекса_практика_лока_ванная_в_минет") in accessiv:
                    mom emo-60 "Ладно. Делайте что хотите, я уже всё."
                    jump pgn_events_12_lizasololesson_10
                elif (("урокисекса_практика_лока_ванная_в_минет") not in accessiv and liza_path == 43) and (("урокисекса_практика_макс") in accessiv or ("урокисекса_практика_макс_впервые") in accessiv):
                    mom emo-60 "[pname_liza[0]], зачем?"
                    l emo-41 "Мам. Ну ты помнишь наш недавний разговор. Мне нужно больше практики."
                    mom emo-68 "[pname_liza[0]], ну не здесь же. Может потом, как закончим свои дела в ванной?"
                    l emo-48 "Я хочу сейчас. И если что, ты можешь если что подсказать."
                    mom emo-69 "Ох... Ладно, хорошо."
                    jump pgn_events_12_lizasololesson_10
                else:
                    mom emo-72 "[pname_liza[0]]?"
                    l emo-40 "Я не помню ни о чём таком."
                    m emo-13 "Разве?"
                    mom emo-60 "[pname_liza[0]] говорит, что не помнит, значит ты что-то напутал или нагло врёшь."
                    m emo-13 "Да, наверное я что-то напутал. Ухожу."
        "уйти":
            pass
    scene bg door_01
    call screen location_bathroom


label pgn_events_12_lizasololesson_10:
    scene pgn_bath_momliza_afterlesson_04_vezdessushij
    mom emo-60 "[pname_max[0]], ты опасно сидишь, будь осторожен и держись крепче."
    m emo-0 "Да Мама, хорошо."
    scene pgn_bath_momliza_afterlesson_05_vezdessushij
    mom emo-73 "Может лучше хорошо вымоетесь и продолжите у себя в комнате?"
    l emo-40 "Я хочу здесь."
    mom emo-60 "Как хотите."
    scene pgn_bath_momliza_afterlesson_06_vezdessushij
    $ PGN_Achadd(pgnach_139, 139)
    m emo-3 "Я готов, можешь начинать."
    l emo-41 "Крепко держись, братик."
    if (("урокисекса_практика_лока_ванная_в_минет") not in accessiv and liza_path == 43) or pgn_ach_repeat == 139:
        scene pgn_bath_momliza_afterlesson_18_vezdessushij
        mom emo-69 "..."
        scene pgn_bath_momliza_afterlesson_04_vezdessushij
        mom emo-60 "{i}Правильно ли я поступила, что позволила моей малышке тренироваться вне уроков{/i}"
        scene pgn_bath_momliza_afterlesson_18_vezdessushij
        m emo-4 "Ох... Ммм... [pname_liza[0]], не торопись..."
        l emo-41 "Разве братик не хочет побыстрее кончить?"
        l emo-49 "Ммм... ммм..."
        scene pgn_bath_momliza_afterlesson_19_vezdessushij
        mom emo-73 "{i}Что со мной не так. Их стоны меня возбуждают, мои дети меня возбуждают.{/i}"
        scene animated pgn_bath_momliza_afterlesson_07
        $ renpy.pause()
    else:
        scene animated pgn_bath_momliza_afterlesson_07
        $ renpy.pause()
    m emo-10 "[pname_liza[0]], я почти..."
    if liza_path >= 44 or (("урокисекса_практика_лока_ванная_в_минет") in accessiv and liza_path == 43) or pgn_ach_repeat == 139:
        menu:
            "Кончить в рот":
                label pgn_events_12_lizasololesson_10_cuminmouth:
                    scene pgn_bath_momliza_afterlesson_08_vezdessushij
                    m emo-12 "Аргххх..."
                    $ label_random = renpy.random.randint ( 1, 2)
                    if label_random == 1:
                        scene pgn_bath_momliza_afterlesson_09_vezdessushij
                    else:
                        scene pgn_bath_momliza_afterlesson_10_vezdessushij
                    l emo-49 "Тебе понравилось, братик?"
                    m emo-3 "О да!"
                    l emo-48 "Тогда я рада. Но всё же мне нужно больше практики."
            "Кончить на неё":
                label pgn_events_12_lizasololesson_10_cumshot:
                    scene pgn_bath_momliza_afterlesson_11_vezdessushij
                    l emo-49 "Давай братик, кончи на меня. Облей меня всю своей горячей спермой."
                    scene pgn_bath_momliza_afterlesson_12_vezdessushij
                    m emo-12 "Аргх!!"
                    scene pgn_bath_momliza_afterlesson_13_vezdessushij
                    l emo-41 "Мммм... Спасибо. Ну как я?"
                    m emo-4 "Супер!"
        jump pgn_events_12_lizasololesson_10_next
    elif ("урокисекса_практика_лока_ванная_в_минет") not in accessiv and liza_path == 43:
        scene pgn_bath_momliza_afterlesson_14_vezdessushij
        jump pgn_events_12_lizasololesson_10_cumshot

label pgn_events_12_lizasololesson_10_next:
    if (("урокисекса_практика_лока_ванная_в_минет") not in accessiv and liza_path == 43) or pgn_ach_repeat == 139:
        scene pgn_bath_momliza_afterlesson_15_vezdessushij
        l emo-40 "Мама, я же правильно всё делала?"
        mom emo-60 "Вроде, да... [pname_liza[0]]! Откуда ты таких словечек понабрала?"
        l emo-41 "Эм... Сама придумала. Главное братику понравилось."
        mom emo-60 "Да, но [pname_liza[0]]..."
        scene pgn_bath_momliza_afterlesson_16_vezdessushij
        l emo-40 "Сейчас вернусь, только смою с себя."
        mom emo-69 "[pname_liza[0]]... Ох."
    scene pgn_bath_momliza_afterlesson_17_vezdessushij
    $ renpy.pause(1.5)
    scene pgn_bath_momliza_afterlesson_20_vezdessushij
    l emo-43 "Я люблю тебя, Мама."
    mom emo-75 "Я тоже."
    scene pgn_bath_momliza_afterlesson_21_vezdessushij
    l emo-41 "{i}Ммм! Между ног мамы очень горячо.{/i}"

    if pgn_ach_repeat == 139:
        jump table_pgn_achievement

    $ qtime, liza_sex_bj = qtime+1, 4
    if ("урокисекса_практика_макс") in accessiv:
        $ accessiv.remove("урокисекса_практика_макс")
    $ accessiv.append("урокисекса_практика_лиза")

    if ("урокисекса_практика_лока_ванная_в_минет") not in accessiv and liza_path == 43:
        $ accessiv.append("урокисекса_практика_лока_ванная_в_минет")
    if ("урокисекса_практика_макс_впервые") in accessiv:
        $ accessiv.remove("урокисекса_практика_макс_впервые")
        $ accessiv.remove("урокисекса_практика_лиза")

    $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
    jump loc_bathroom



label pgn_events_12_lizasololesson_11a:
    m emo-0 "Не против если я подсяду?"
    l emo-40 "Конечно, братик. Садись."
    scene pgn_livroom_lizapractics_02
    m emo-0 "Что смотрим?"
    l emo-41 "[pname_max[0]], ты же сюда пришёл не фильмы смотреть?"
    m emo-0 "А что предлагаешь?"
    if ("урокисекса_практика_макс_впервые") in accessiv or ("урокисекса_практика_макс") in accessiv:
        jump pgn_events_12_lizasololesson_11a_p1
    if ("урокисекса_практика_лиза") in accessiv:
        l emo-49 "Как я помню, твоя очередь сделать мне приятное."
        menu:
            "У меня дела":
                m emo-2 "Блин! Извини, я забыл, мне нужно кое-что сделать."
                l emo-40 "Жаль. Иди делай свои дела."
                jump loc_living_room
            "Продолжить":
                pass
        jump pgn_events_12_lizasololesson_11a_p2

label pgn_events_12_lizasololesson_11a_p1:
    l emo-41 "Хочешь я сделаю тебе минет?"
    menu:
        "Может всё же куни?" if pgn_ach_repeat == 0:
            m emo-13 "Может я всё же сделаю тебе приятно?"
            l emo-41 "Хорошо. Раз сам предложил, не могу отказать. Хочу твой язык между ног."
            jump pgn_events_12_lizasololesson_11a_p2
        "Да":
            pass
    l emo-41 "Тогда раздевайся и я то же."
    scene pgn_livroom_lizapractics_03
    if ("урокисекса_практика_лока_гростиная_куни") not in accessiv and liza_path == 43:
        m emo-0 "Уверена. А если Мама придёт или [pname_alice[0]]?"
        l emo-48 "Хм... Ты не против, если они составят нам компанию?"
    l emo-43 "Братик. Расслабься. Твоя сестрёнка постарается сделать тебе приятное."
    scene pgn_livroom_lizapractics_04
    l emo-41 "Сначала язычком."
    scene animated pgn_livroom_lizapractics_05
    $ renpy.pause()
    m emo-3 "{i}Лижет как большой сладкий и вкусный леденец. Он ей очень нравится.{/i}"
    scene pgn_livroom_lizapractics_04
    l emo-43 "А теперь ротиком."
    scene animated pgn_livroom_lizapractics_06
    $ renpy.pause()
    m emo-6 "Мне кажется или кто-то идёт?"
    $ label_random = renpy.random.randint ( 1, 4)
    if (label_random == 1 or (("урокисекса_практика_лока_гростиная_куни") not in accessiv and "walkthrough_light" in accessiv)) and locchr_mom.loc1 == "loc_home" and pgn_ach_repeat == 0:
        scene pgn_livroom_lizapractics_11
        mom emo-60 "[pname_max[0]]. А чего ты тут один?"
        m emo-0 "Да так, смотрел фильм, а сейчас просто лежу не диване."
        scene pgn_livroom_lizapractics_12
        mom emo-60 "[pname_liza[3]] не видел?"
        m emo-0 "Нет. Может решила погулять около дома."
        mom emo-68 "На ночь глядя? Не знаю... Я пойду, поищу её. А ты не усни на диване, лучше поднимись к себе в комнату."
        m emo-0 "Хорошо."
    elif (label_random == 2 and locchr_alice.loc1 == "loc_home" and pgn_ach_repeat == 0) or pgn_ach_repeat == 144:
        m emo-8 "{i}Что-то у меня предчувствие нехорошее.{/i}"
        scene pgn_livroom_lizapractics_13
        a emo-21 "Так, так. [pname_liza[0]], это как понимать? О чём мы с тобой давно говорили?"
        scene pgn_livroom_lizapractics_14
        l emo-46 "Ну... Мне захотелось сделать [pname_max[2]] приятное."
        a emo-20 "А меня позвать?"
        l emo-46 "Я хотела, но..."
        a emo-21 "Хотела, но так увлеклась, что забыла?"
        scene pgn_livroom_lizapractics_15
        $ label_random = renpy.random.randint ( 1, 3)
        if label_random != 2 or pgn_ach_repeat == 144:
            l emo-41 "Присоединишься?"
            m emo-13 "{i}Присоединишься?! А меня спросить.{/i}"
            a emo-21 "Я не против."
        else:
            menu:
                "Предложить [pname_alice[2]]":
                    m emo-3 "Хочешь тоже сделать мне приятное?"
                    if alice_tv_round == True:
                        a emo-20 "Вообще-то твоя очередь делать мне куни, ну ладно."
                    a emo-21 "Не могу отказаться от такого предложения."
                "Продолжить без [pname_alice[1]]":
                    m emo-1 "[pname_alice[0]], я бы предложил составить нам компанию, но меня не хватит на вас двоих."
                    a emo-23 "Жаль. Тогда вы знаете, какое будет для вас наказание."
                    l emo-46 "Да, [pname_alice[0]] мы помним."
                    $ lizasex_alice = True
                    jump pgn_events_12_lizasololesson_11a_p1_next
        label pgn_events_12_lizasololesson_11a_p1_bj:
            scene pgn_livroom_lizapractics_16
            a emo-25 "В чей ротик сейчас хочешь засунуть член?"
            $ label_random = renpy.random.randint ( 1, 3)
            menu:
                "[pname_liza[0]]":
                    scene animated pgn_livroom_lizapractics_06
                    $ renpy.pause()
                    a emo-33 "[pname_liza[0]], не жадничай, а не то прям сейчас отшлепаю."
                    scene pgn_livroom_lizapractics_17
                    l emo-46 "Не надо меня шлёпать."
                    jump pgn_events_12_lizasololesson_11a_p1_alice
                "[pname_alice[0]]":
                    scene animated pgn_livroom_lizapractics_18
                    l emo-42 "[pname_alice[0]]. Я тоже хочу."
                    label pgn_events_12_lizasololesson_11a_p1_alice:
                        scene animated pgn_livroom_lizapractics_18
                        $ renpy.pause()
                        if label_random == 3 and locchr_mom.loc1 == "loc_home":
                            scene pgn_livroom_lizapractics_19
                            a emo-20 "Привет Мам."
                            mom emo-69 "Ой! А что это вы тут делаете?"
                            a emo-21 "Да вот, снова помогаю [pname_max[2]] с его проблемой."
                            mom emo-60 "Ясно. А вы [pname_liza[3]] не видели?"
                            scene pgn_livroom_lizapractics_20
                            m emo-0 "Нет. Не видели."
                            mom emo-60 "Ладно. Не буду вам мешать."
                            scene animated pgn_livroom_lizapractics_18
                            $ renpy.pause()
                        scene pgn_livroom_lizapractics_21
                        $ PGN_Achadd(pgnach_144, 144)
                        l emo-49 "[pname_alice[0]], оставь мне немного. [pname_alice[0]]!"
                        scene pgn_livroom_lizapractics_22
                        l emo-44 "Ты мне ничего не оставила. Тогда я в следующий раз..."
                        a emo-33 "Хочешь, чтобы [pname_max[0]] неделю спал в моей комнате?"
                        scene pgn_livroom_lizapractics_23
                        l emo-46 "..."

                        if pgn_ach_repeat == 144:
                            jump table_pgn_achievement

                        if ("livroom_aliceliza_tv_bj") not in ivent24:
                            a emo-21 "Спасибо хоть за это. А сейчас готовим попки, буду вас наказывать."
                            m emo-2 "Но..."
                            a emo-20 "За то, что не позвали меня."

                        $ qtime, liza_sex_bj, alice_tv_round = qtime+1, 4, True
                        if ("урокисекса_практика_макс") in accessiv:
                            $ accessiv.remove("урокисекса_практика_макс")
                        $ accessiv.append("урокисекса_практика_лиза")

                        if ("урокисекса_практика_макс_впервые") in accessiv:
                            $ accessiv.remove("урокисекса_практика_макс_впервые")
                            $ accessiv.remove("урокисекса_практика_лиза")

                        $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
                        $ PGN_Addstatsex(stat_alice, 0, 0, 1, 0, 0)
                        if ("livroom_aliceliza_tv_bj") in ivent24:
                            a emo-21 "[pname_max[0]], не забудь, в следующий раз твоя очередь."
                            m emo-13 "Да, да."
                            jump loc_my_room
                        scene b-tv-15
                        a emo-21 "Какие послушные, всегда бы так."
                        scene b-tv-17
                        m emo-2 "Ай! Больно же!"
                        scene b-tv-16
                        a emo-21 "В следующий раз не забудишь и позовёшь меня."
                        l emo-46 "Но [pname_max[0]]?"
                        scene b-tv-15b
                        a emo-20 "Значит [pname_max[0]] всё же виноват. Тогда ещё раз он получит от меня."
                        scene b-tv-17
                        m emo-2 "Ай!"
                        scene b-tv-20
                        a emo-24 "Ну всё, свободны мои любимые."
                        if ("livroom_aliceliza_noinvite") not in accessiv:
                            $ accessiv.append("livroom_aliceliza_noinvite")
                        jump loc_my_room

label pgn_events_12_lizasololesson_11a_p1_next:
    m emo-0 "А нет, показалось."
    m emo-10 "[pname_liza[0]]! Я почти уже..."
    scene pgn_livroom_lizapractics_07
    m emo-12 "Аааргх!"
    scene animated pgn_livroom_lizapractics_08
    m emo-5 "{i}Сестрёнка выжимает из меня сперму до самой капли.{/i}"
    scene pgn_livroom_lizapractics_09
    $ PGN_Achadd(pgnach_143, 143)
    l emo-43 "Я всё проглотила."
    scene pgn_livroom_lizapractics_10
    l emo-41 "Ну что, как я?"
    m emo-4 "Лучший минет."

    if pgn_ach_repeat == 143:
        jump table_pgn_achievement

    $ qtime, liza_sex_bj = qtime+1, 4
    if ("урокисекса_практика_макс") in accessiv:
        $ accessiv.remove("урокисекса_практика_макс")
    $ accessiv.append("урокисекса_практика_лиза")

    if ("урокисекса_практика_макс_впервые") in accessiv:
        $ accessiv.remove("урокисекса_практика_макс_впервые")
        $ accessiv.remove("урокисекса_практика_лиза")

    $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
    menu:
        "Предложить куни":
            m emo-3 "Сделать тебе куни?"
            $ label_random = renpy.random.randint ( 1, 4)
            if label_random == 1:
                l emo-49 "Раз у моего братика ещё остались силы, хорошо, я согласна."
                jump pgn_events_12_lizasololesson_11a_p2
            l emo-48 "Сейчас не хочу, мне нужно перерыв сделать небольшой."
            m emo-1 "Понял."
        "Закончить":
            pass
    jump loc_living_room

label pgn_events_12_lizasololesson_11a_p2:
    scene pgn_livroom_lizapractics_26
    l emo-41 "Братик, тебе так удобно?"
    scene pgn_livroom_lizapractics_27
    m emo-1 "Да, сестрёнка. Из твоей киски уже течет, хочу всю её вылизать."
    scene pgn_livroom_lizapractics_28
    l emo-48 "Сестрёнка на тебя рассчитывает, помоги мне кончить."
    scene animated pgn_livroom_lizapractics_30
    $ renpy.pause()
    scene pgn_livroom_lizapractics_29
    l emo-48 "Сестрёнке нравится... Продолжай..."
    $ label_random = renpy.random.randint ( 1, 2)
    if (locchr_mom.loc1 == "loc_home" and ((("урокисекса_практика_лока_гростиная_куни") not in accessiv and liza_path == 43) or label_random == 1)) or pgn_ach_repeat == 145:
        scene pgn_livroom_lizapractics_32
        mom emo-68 "[pname_liza[0]]!"
        l emo-41 "Привет Мама! А мы тут практикой заняты."
        scene pgn_livroom_lizapractics_33
        m emo-1 "А мам, привет."
        if ("урокисекса_практика_лока_гростиная_куни") not in accessiv and liza_path == 43 and pgn_ach_repeat == 0:
            mom emo-63 "[pname_liza[0]], ну как тебе не стыдно таким заниматься в гостиной. Ушли бы в свою комнату. Вдруг [pname_alice[0]] вас увидит."
            l emo-41 "Если увидит, тогда к нам присоединится."
        l emo-43 "Язык братика потрясающий."
        if ("урокисекса_практика_лока_гростиная_куни") not in accessiv and liza_path == 43 and pgn_ach_repeat == 0:
            scene pgn_livroom_lizapractics_34
            mom emo-64 "[pname_liza[0]]!"
            l emo-46 "Прости... Нам уйти?"
            mom emo-60 "Продолжайте, я только посижу рядом и понаблюдаю за вами"
            scene pgn_livroom_lizapractics_35
            $ renpy.pause(3)
            scene pgn_livroom_lizapractics_36
            m emo-13 "{i}Сложно описать. Но такое ощущение, что кто-то сильно хочет моего члена.{/i}"
            scene pgn_livroom_lizapractics_37
            m emo-3 "{i}Какая же всё же классная у меня младшая сестра.{/i}"
            scene pgn_livroom_lizapractics_36
            l emo-40 "Мама!"
            mom emo-60 "Что доченька?"
            l emo-41 "Одолжить тебе [pname_max[3]]?"
            mom emo-73 "Мне... Ммм... Зачем солнышка? Вы же практикуете, а я просто наблюдаю за вами..."
            l emo-48 "Так не только я учусь, но и [pname_max[0]]. Может он продолжит на тебе?"
            mom emo-71 "Нет, нет, вы продолжайте, без меня."
            $ renpy.pause(3)
            scene pgn_livroom_lizapractics_31
            l emo-50 "Аааахххх... Ммм... Аххх..."
            scene pgn_livroom_lizapractics_36
            mom emo-60 "Всё, молодцы, бегом в ванную и спать."
            l emo-41 "Мы тебя любим, мамочка."
            $ qtime, liza_sex_bj = qtime+1, 4
            if ("урокисекса_практика_лиза") in accessiv:
                $ accessiv.remove("урокисекса_практика_лиза")
            $ accessiv.append("урокисекса_практика_макс")
            $ accessiv.append("урокисекса_практика_лока_гростиная_куни")

            $ PGN_Addstatsex(stat_liza, 0, 1, 0, 0, 0)
            jump loc_my_room
        else:
            mom emo-73 "Я посижу рядом с вами."
            scene pgn_livroom_lizapractics_35
            $ renpy.pause(3)
            scene pgn_livroom_lizapractics_36
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random == 1:
                l emo-41 "Составишь нам компанию?"
                mom emo-73 "Если просишь, малышка, я не против."
            else:
                l emo-41 "Мама, может [pname_max[0]] на тебе тоже потренируется?"
                if label_random == 2:
                    mom emo-71 "Потом, ты же ещё не... Не кончила."
                    l emo-49 "Мама, ты уверена? А пока [pname_max[0]] будет тренироваться на тебе, я потренируюсь в мастурбации."
                    mom emo-62 "Хорошо, милая. Ты меня уговорила."
                    m emo-5 "{i}Уговорила?! Да Мама так завелась, что готова на мой член напрыгнуть.{/i}"
                if label_random == 3:
                    mom emo-69 "Если [pname_max[0]] ещё не устал."
                    m emo-3 "У меня много сил и мне только в радость делать вам приятное."
                    mom emo-72 "В этом я не сомневаюсь."
            scene pgn_livroom_lizapractics_38
            mom emo-69 "[pname_max[0]], не спеши. Твоему языку необходим небольшой перерыв. Так что пока можешь начать с поцелуев."
            mom emo-69 "Мммм... Аххх..."
            scene pgn_livroom_lizapractics_39
            mom emo-68 "Целуй мамину киску... Нежнее... Молодец..."
            scene pgn_livroom_lizapractics_38
            mom emo-68 "Ахх... Аххх... Мммм... Аххх..."
            scene pgn_livroom_lizapractics_40
            l emo-49 "{i}Я перевозбудилась и хочу член братика... в попку. Этот большой, крепкий и горячий.{/i}"
            scene pgn_livroom_lizapractics_41
            l emo-40 "{i}Пока мама не видит, воспользуюсь другим большим пальчиком братика.{/i}"
            scene pgn_livroom_lizapractics_42
            m emo-6 "{i}Хм... Что там делает [pname_liza[0]] с моей ногой? Она...{/i}"
            scene pgn_livroom_lizapractics_43
            m emo-4 "{i}У сестрёнки внутри горячо.{/i}"
            scene pgn_livroom_lizapractics_44
            l emo-49 "Ммм... Аааххх... Мама я скоро кончу..."
            mom emo-75 "Молодец доченька. У тебя хорошо получается, продолжай."
            m emo-3 "{i}Она даже не представляет, где сейчас мой большой палец находится и от чего [pname_liza[0]] так громко начала стонать.{/i}"
            scene pgn_livroom_lizapractics_45
            mom emo-75 "{i}Моя малышка уже такая большая, скоро познает что такое секс..{/i}"
            mom emo-73 "{i}Нет, нет, нет. Чего это я. Она моя маленькая и невинная девочка, ей рано ещё.{/i}"
            scene pgn_livroom_lizapractics_46
            mom emo-68 "{i}Но когда-нибудь у неё появится парень и они будут заниматься сексом, она не устроит его в постели, после он её бросит, уйдёт к другой, моя малышка будет одна, без мужчины... без члена, что сможет её удовлетворить.{/i}"
            mom emo-60 "{i}[pname_mom[7]], перестань думать о плохом. Всё у неё будет хорошо. Я всему научу её, о чём знаю. Я хочу быть рядом, в её первый раз...{/i}"
            scene pgn_livroom_lizapractics_47
            m emo-3 "{i}Что-то Мама притихла. Думаю Мама будет не против такой стимуляции.{/i}"
            scene pgn_livroom_lizapractics_48
            mom emo-68 "Аххх... [pname_max[0]].. ММммм.."
            scene pgn_livroom_lizapractics_49
            mom emo-69 "Мммм... Аааааххх... Аххх.."
            m emo-4 "{i}Отлично. Мама снова застонала.{/i}"
            scene pgn_livroom_lizapractics_50
            l emo-49 "Мама, я почти..."
            mom emo-68 "Я тоже, я тоже, моя дорогая..."
            scene pgn_livroom_lizapractics_51
            mom emo-68 "Ааахххх..."
            scene pgn_livroom_lizapractics_52
            l emo-50 "Аааа..."
            scene pgn_livroom_lizapractics_53
            l emo-41 "Поможем [pname_max[2]], вместе? Нельзя же так, с эрекцией его оставлять."
            mom emo-62 "Конечно, доченька..."
            scene pgn_livroom_lizapractics_54
            $ PGN_Achadd(pgnach_145, 145)
            m emo-2 "{i}Поскорее, кончить хочу.{/i}"
            scene animated pgn_livroom_lizapractics_55
            $ renpy.pause()
            m emo-10 "Я уже почти."
            scene animated pgn_livroom_lizapractics_56
            $ renpy.pause()
            m emo-2 "{i}Блин, блин, блин, ну же, сейчас...{/i}"
            $ label_random = renpy.random.randint ( 1, 5)
            if label_random == 3 or label_random == 5:
                menu:
                    "В Маму":
                        scene pgn_livroom_lizapractics_58
                        m emo-12 "Ааррргхх... Мммм... Ахх..."
                        scene pgn_livroom_lizapractics_63
                        mom emo-75 "Ох! Мама не смогла всё проглотить, слишком много спермы сынок выплеснул в мамин рот."
                        scene pgn_livroom_lizapractics_64
                        l emo-49 "..."
                        mom emo-62 "Бегом все ванную и спать."
                    "В [pname_liza[3]]":
                        scene pgn_livroom_lizapractics_60
                        m emo-12 "Ааррргжж... Мммм... Ахх..."
                        scene pgn_livroom_lizapractics_65
                        l emo-50 "Аааа..."
                        mom emo-60 "Доченька, закрой ротик, а то всё выльется"
                        mom emo-62 "Бегом все ванную и спать."
            else:
                if label_random == 1:
                    scene pgn_livroom_lizapractics_57
                    m emo-12 "Ааррргхх... Мммм... Ахх..."
                    scene pgn_livroom_lizapractics_63
                    mom emo-75 "Ох! Мама не смогла всё проглотить, слишком много спермы сынок выплеснул в мамин рот."
                    scene pgn_livroom_lizapractics_64
                    l emo-49 "..."
                    mom emo-62 "Бегом все ванную и спать."
                if label_random == 2:
                    scene pgn_livroom_lizapractics_59
                    mom emo-66 "[pname_liza[0]]!"
                    m emo-12 "Ааррргжж... Мммм... Ахх..."
                    scene pgn_livroom_lizapractics_65
                    l emo-50 "Аааа..."
                    mom emo-60 "Доченька, закрой ротик, а то всё выльется"
                    mom emo-62 "Бегом все ванную и спать."
                if label_random == 4:
                    scene pgn_livroom_lizapractics_61
                    m emo-12 "Ааррргхх... Мммм... Ахх..."
                    scene pgn_livroom_lizapractics_62
                    mom emo-62 "Ох! Испачкал маму. Ну всё, бегом в ванную, умываться и ложиться спать."

            if pgn_ach_repeat == 145:
                jump table_pgn_achievement

            $ qtime, liza_sex_bj = qtime+1, 4
            if ("урокисекса_практика_лиза") in accessiv:
                $ accessiv.remove("урокисекса_практика_лиза")
            $ accessiv.append("урокисекса_практика_макс")

            $ PGN_Addstatsex(stat_liza, 0, 1, 0, 0, 0)
            $ PGN_Addstatsex(stat_mom, 0, 1, 1, 0, 1)
            jump loc_my_room
    else:
        scene animated pgn_livroom_lizapractics_30
        $ renpy.pause()
        scene pgn_livroom_lizapractics_31
        l emo-50 "Аааахххх... Ммм... Аххх..."
        scene pgn_livroom_lizapractics_10
        l emo-41 "Спасибо, мне понравилось."
        m emo-3 "Всегда пожалуйста."
        $ qtime, liza_sex_bj = qtime+1, 4
        if ("урокисекса_практика_лиза") in accessiv:
            $ accessiv.remove("урокисекса_практика_лиза")
        $ accessiv.append("урокисекса_практика_макс")

        $ PGN_Addstatsex(stat_liza, 0, 1, 0, 0, 0)
    jump loc_living_room



label pgn_events_12_lizasololesson_11b:
    menu:
        "Что смотрите?":
            a emo-20 "Да так, всё подряд."
            m emo-0 "Можно с вами? Тоже просто посижу?"
            a emo-24 "Просто посидеть? Хм... Я сюда пришла ради чего другого и особенного. Так что предлагаешь?"
            menu menu_pgn_events_12_lizasololesson_11b:
                "Минет":
                    if ("урокисекса_практика_лиза") in accessiv:
                        l emo-44 "Я делала тебе минет, так что твоя очередь."
                    elif alice_tv_round == True:
                        a emo-21 "А ты ничего не перепутал?! Сейчас будешь лизать наши киски."
                    elif ("урокисекса_практика_макс") in accessiv or ("урокисекса_практика_макс_впервые") in accessiv:
                        $ ivent24.append("livroom_aliceliza_tv_bj")
                        jump pgn_events_12_lizasololesson_11a_p1_bj
                    m emo-8 "Блин!"
                    jump pgn_events_12_lizasololesson_11b_cunni_alice
                "Куни":
                    scene pgn_livroom_lizapractics_25
                    a emo-21 "Выбирай, чья киска будет первой."
                    menu:
                        "[pname_liza[0]]":
                            jump pgn_events_12_lizasololesson_11b_cunni_liza
                        "[pname_alice[0]]":
                            jump pgn_events_12_lizasololesson_11b_cunni_alice
        "Готовы повеселиться?":
            a emo-21 "Конечно."
            jump menu_pgn_events_12_lizasololesson_11b

label pgn_events_12_lizasololesson_11b_cunni_alice:
    scene pgn_livroom_lizapractics_66
    a emo-24 "Ох, как присосался, словно год не видел мою киску."
    scene pgn_livroom_lizapractics_67
    a emo-25 "Полегче, [pname_max[0]]. Тебе ещё киску [pname_liza[1]] лизать."
    scene pgn_livroom_lizapractics_68
    a emo-24 "Натренировался на киске [pname_liza[1]] или на маминой?"
    scene pgn_livroom_lizapractics_69
    a emo-21 "У тебя хорошо получается."
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random == 4 and ("liv_aliceliza_momsearch") not in ivent24 and locchr_mom.loc1 == "loc_home":
        scene pgn_livroom_lizapractics_77
        mom emo-66 "Девочки. А что вы тут делаете? [pname_alice[0]], это что ещё за поза?"
        scene pgn_livroom_lizapractics_78
        l emo-41 "[pname_alice[0]] показывает мне, как она мастурбирует."
        mom emo-69 "Понятно. Могла меня попросить..."
        l emo-41 "Да. Но чем больше людей, тем больше опыта у меня будет."
        mom emo-60 "Помощь моя нужна?"
        l emo-41 "Мы сами справимся."
        mom emo-73 "А... Ну... Хорошо, не буду вам мешать."
        $ ivent24.append("liv_aliceliza_momsearch")
    scene pgn_livroom_lizapractics_70
    a emo-21 "Всё, [pname_max[0]], хватит. Теперь [pname_liza[2]]."
    $ ivent24.append("livroom_aliceliza_cunni_alice")
    if ("livroom_aliceliza_cunni_alice2") in ivent24 and pgn_ach_repeat == 0:
        jump pgn_events_12_lizasololesson_11b_cunni_liza_next
    menu:
        "Но ты ж ещё не кончила?" if pgn_ach_repeat == 0:
            a emo-33 "Помоги сначала [pname_liza[2]], а уже после закончишь со мной. Мне нужно немного времени отдышаться."
        "[pname_liza[0]]" if pgn_ach_repeat == 0:
            pass
        "Продолжить":
            scene pgn_livroom_lizapractics_71
            a emo-29 "Аххх... [pname_max[0]]... Остановись... Мне нужно..."
            scene pgn_livroom_lizapractics_72
            a emo-30 "[pname_max[0]]..."
            scene pgn_livroom_lizapractics_73
            a emo-26 "Пожалуйста... Я... я..."
            scene pgn_livroom_lizapractics_74
            a emo-26 "[pname_max[0]]! Аааххх... Мммм...."
            scene pgn_livroom_lizapractics_75
            $ PGN_Achadd(pgnach_146, 146)
            a emo-34 "Ааахххх... Да... Аххх..."
            scene pgn_livroom_lizapractics_76
            a emo-31 "Вау... Это было круто... "

            if pgn_ach_repeat == 146:
                jump table_pgn_achievement

            l emo-46 "Братик, у тебя остались силы на мою киску?"
            m emo-3 "Конечно. Я не уйду, пока вы обе не кончите."
            $ ivent24.append("livroom_aliceliza_cunni_alice_orgasm")
            if ("livroom_aliceliza_cunni_alice2") in ivent24:
                jump pgn_events_12_lizasololesson_11b_cunni_liza_next
label pgn_events_12_lizasololesson_11b_cunni_liza:
    l emo-41 "Только я хочу будь сверху."
    menu:
        "Согласиться":
            pass
        "Возразить":
            m emo-13 "Может выберешь другую позу? Мне так неудобно."
            l emo-49 "Я хочу... сверху..."
            a emo-29 "[pname_max[0]], не капризничай. И не трать время в пустую."
            m emo-0 "{i}Ни какой свободы выбора.{/i}"
    scene pgn_livroom_lizapractics_79
    l emo-49 "Ахх... Мммм... Аххх..."
    scene pgn_livroom_lizapractics_80
    a emo-21 "Ну как, ощущения?"
    l emo-49 "Братик хорошо лижет мою киску... Мне нравится..."
    scene pgn_livroom_lizapractics_81
    if ("livroom_aliceliza_cunni_alice_orgasm") not in ivent24:
        a emo-33 "[pname_max[0]], лижи поактивнее, а то так [pname_liza[0]] до утра не кончит и я тоже."
        m emo-1 "Я стараюсь как могу."
        a emo-28 "Тс... используй язык по назначению."
    l emo-50 "Ммммм..."
    scene pgn_livroom_lizapractics_82
    m emo-2 "Может сменим позу, у меня так шея болеть будет."
    a emo-26 "Какой ты у нас неженка. [pname_liza[0]], решай сама."
    l emo-41 "Хорошо."
    scene pgn_livroom_lizapractics_83
    a emo-26 "Не перепутай дырочку."
    m emo-13 "{i}Ха-ха. Только я не против засунуть в другую дырочку член.{/i}"
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random == 3 and ("liv_aliceliza_momsearch") not in ivent24 and locchr_mom.loc1 == "loc_home" and pgn_ach_repeat == 0:
        scene pgn_livroom_lizapractics_84
        mom emo-69 "Девочки, вы не видели [pname_max[3]]?"
        a emo-20 "Нет."
        l emo-48 "Н-н-нет..."
        mom emo-69 "Никак не могу его найти."
        a emo-20 "Может он с Тётей [pname_kira[4]] снова куда-то уехал."
        mom emo-60 "Возможно. А то его никак не могу найти."
        a emo-25 "Ему что-то передать?"
        mom emo-73 "Нет, просто искала его для... дела. Не буду вам мешать."
        $ ivent24.append("liv_aliceliza_momsearch")
    scene pgn_livroom_lizapractics_85
    l emo-49 "Аххх... Мммм..."
    scene pgn_livroom_lizapractics_86
    m emo-6 "{i}Что-то [pname_liza[0]] не кончает{/i}"
    if ("livroom_aliceliza_cunni_alice") not in ivent24 and pgn_ach_repeat == 0:
        $ ivent24.append("livroom_aliceliza_cunni_alice2")
        jump pgn_events_12_lizasololesson_11b_cunni_alice

label pgn_events_12_lizasololesson_11b_cunni_liza_next:
    scene pgn_livroom_lizapractics_89
    if ("liv_alicelizacunni_rightchoice") not in accessiv and pgn_ach_repeat == 0:
        scene pgn_livroom_lizapractics_89
        m emo-0 "Я устал. Может как-нибудь иначе?"
        a emo-22 "[pname_max[0]], не отвиливай. Ты здесь, чтобы доставить нам удовольствие своим язычком."
        a emo-21 "Так что отдохнул, продолжай."
        if ("livroom_aliceliza_cunni_alice_orgasm") not in ivent24:
            a emo-24 "И ты ещё не довёл меня до оргазма. Так что давай, не тяни время."
        menu menu_pgn_events_12_lizasololesson_11b_p2_01:
            "Продолжить с [pname_alice[4]]" if ("livroom_aliceliza_cunni_alice3") not in ivent24:
                m emo-0 "Тогда снова твоей киской займусь."
                if ("livroom_aliceliza_cunni_alice_orgasm") in ivent24:
                    a emo-20 "Ты уже довёл меня до оргазма, помоги [pname_liza[2]]."
                else:
                    scene pgn_livroom_lizapractics_87
                    a emo-26 "Аааххххх... Ох! Чёрт! Да! Лижи мою киску"
                    a emo-30 "Вот же чёрт! Я сейчас кончу!"
                    scene pgn_livroom_lizapractics_88
                    a emo-34 "Аааахххх... Мммм... Ааааххх..."
                    $ ivent24.append("livroom_aliceliza_cunni_alice_orgasm")

                $ ivent24.append("livroom_aliceliza_cunni_alice3")
                jump menu_pgn_events_12_lizasololesson_11b_p2_01
            "[pname_liza[0]] не кончает":
                m emo-0 "Я не знаю, но [pname_liza[0]] ни как не кончает."
                a emo-33 "Значит плохо это делаешь. Ну так что?"
                menu menu_pgn_events_12_lizasololesson_11b_p2_02:
                    "Секс с [pname_liza[4]]":
                        label pgn_events_12_lizasololesson_11b_p2_03:
                            scene pgn_livroom_lizapractics_90
                            m emo-3 "[pname_liza[0]], займёмся тогда сексом?"
                            l emo-48 "Хорошо. Моя попка готова."
                            a emo-32 "Ничего не хорошо, [pname_liza[0]]. [pname_max[0]], всё, вали от сюда, в следующий раз снова попробуешь."
                            m emo-2 "Эм..."
                            a emo-33 "Мы тут дальше сами справимся, без тебя."
                            $ qtime += 1
                            jump loc_living_room
                    "Секс с [pname_alice[4]]":
                        scene pgn_livroom_lizapractics_90
                        m emo-4 "Тогда [pname_alice[0]], давай сексом займёмся, а [pname_liza[0]] на нас по мастурбирует."
                        l emo-46 "Я тоже хочу сексом заниматься."
                        a emo-29 "Никто сексом заниматься не будет, по крайней мере сейчас."
                        a emo-32 "[pname_max[0]], ты не член свой доставай, а рот открывай и продолжай работать языком."
                        l emo-48 "А я бы не отказалась от члена... Это большого, толстого м горячего..."
                        a emo-33 "Ну всё, [pname_liza[0]] поплыла. [pname_max[0]], ты свободен, дальше мы сами."
                        m emo-8 "Блин..."
                        a emo-33 "В следующий раз не твоя очередь. Понял?"
                        m emo-8 "Да."
                        $ qtime += 1
                        jump loc_living_room
                    "Отшлепать [pname_liza[3]]":
                        m emo-6 "Хм... Я как помню, [pname_liza[2]] нравятся наказания. Может отшлепать немного эту нежную попку?"
                        scene pgn_livroom_lizapractics_91
                        l emo-46 "Только не шлепки по моей попке. В попку, можно и хочу, но только не это. Пожалуйста."
                        m emo-3 "Но тебе же нравится, когда я это делаю?"
                        a emo-27 "Единственный кто получит по попе, это ты [pname_max[0]]. И так отшлепаю, что сидеть не сможешь спокойно."
                        m emo-0 "Ладно, ладно. Просто предложил как вариант."
                        a emo-28 "Ну да, конечно. Что-нибудь придумаешь, но в следующий раз. А сейчас оставь нас."
                        l emo-49 "Может дадим ему ещё шанс?"
                        a emo-20 "Он упустил его."
                        $ qtime += 1
                        jump loc_living_room
                    "Самым большим пальцем в попу":
                        jump pgn_events_12_lizasololesson_11b_p2_03
                    "Пальчиком в попу":
                        m emo-4 "Есть идея."
                        l emo-41 "Какая?"
                        scene pgn_livroom_lizapractics_92
                        m emo-3 "Расслабься, тебе точно понравится."
                        scene pgn_livroom_lizapractics_93
                        a emo-24 "И что ты придумал?"
    if ("livroom_aliceliza_cunni_alice_orgasm") not in ivent24 and ("liv_alicelizacunni_rightchoice") in accessiv and pgn_ach_repeat == 0:
        m emo-0 "{i}Тогда сначала разберусь с [pname_alice[4]]{/i}"
        scene pgn_livroom_lizapractics_87
        a emo-26 "Аааххххх... Ох! Чёрт! Да! Лижи мою киску"
        a emo-30 "Вот же чёрт! Я сейчас кончу!"
        scene pgn_livroom_lizapractics_88
        a emo-34 "Аааахххх... Мммм... Ааааххх..."
        $ ivent24.append("livroom_aliceliza_cunni_alice_orgasm")
    if ("liv_alicelizacunni_rightchoice") not in accessiv and pgn_ach_repeat == 0:
        $ accessiv.append("liv_alicelizacunni_rightchoice")
    scene pgn_livroom_lizapractics_94
    l emo-49 "Аххх..."
    scene pgn_livroom_lizapractics_95
    m emo-4 "{i}Во это я понимаю. Киска [pname_liza[1]] моментально стала очень влажной{/i}"
    scene pgn_livroom_lizapractics_96
    l emo-50 "Ахх.. Ммм... Аххх..."
    scene pgn_livroom_lizapractics_97
    l emo-49 "[pname_max[0]].. Я почти..."
    scene pgn_livroom_lizapractics_98
    $ PGN_Achadd(pgnach_147, 147)
    l emo-49 "Братик..."
    scene animated pgn_livroom_lizapractics_99
    $ renpy.pause()
    l emo-49 "Ахх... Аххх..."
    scene pgn_livroom_lizapractics_100
    l emo-50 "Бра...тик..."
    scene pgn_livroom_lizapractics_101
    l emo-50 "Аааахххх..."
    if ("livroom_aliceliza_cunni_alice_orgasm") not in ivent24 and pgn_ach_repeat == 0:
        m emo-3 "А теперь ты."
        scene pgn_livroom_lizapractics_87
        a emo-26 "Аааххххх... Ох! Чёрт! Да! Лижи мою киску"
        a emo-30 "Вот же чёрт! Я сейчас кончу!"
        scene pgn_livroom_lizapractics_88
        a emo-34 "Аааахххх... Мммм... Ааааххх..."
        $ ivent24.append("livroom_aliceliza_cunni_alice_orgasm")
    scene pgn_livroom_lizapractics_90
    m emo-3 "Ну что, теперь моя очередь?"
    a emo-26 "Нет, нет... у нас больше нет сил. Ведь так, [pname_liza[0]]?"
    l emo-49 "Да..."
    m emo-2 "Блин. У меня от всего этого каменный стояк. Может всё же поможете?"
    a emo-21 "Потом, если вспомним о тебе."

    if pgn_ach_repeat == 147:
        jump table_pgn_achievement

    $ qtime, liza_sex_bj, alice_tv_round = qtime+1, 4, False
    if ("урокисекса_практика_лиза") in accessiv:
        $ accessiv.remove("урокисекса_практика_лиза")
    $ accessiv.append("урокисекса_практика_макс")

    $ PGN_Addstatsex(stat_liza, 0, 1, 0, 0, 0)
    $ PGN_Addstatsex(stat_alice, 0, 1, 0, 0, 0)
    jump loc_my_room
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
