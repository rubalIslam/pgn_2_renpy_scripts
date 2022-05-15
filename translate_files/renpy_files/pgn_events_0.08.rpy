










label pgn_newmaxward_01:
    m emo-8 "Сегодня снова у вас шоппинг. А вам это не надоело?"
    a emo-22 "Нам!? Надоест!? Да не за что, это самый лучший способ отдохнуть и купить что-нибудь себе любимым красивое."
    a emo-21 "Разве тебе не хочется посмотреть на нас в чём-то новеньком?"
    m emo-0 "{i}Лучше, если бы вы вообще без одежды были.{/i}"
    mom emo-69 "Хм... действительно, каждую субботу и покупаем только себе. Ты может, тоже хочешь?"
    m emo-0 "Я!? Да не, мне и так нормально. Нигде не жмёт."
    k emo-104 "А что, давайте съездим, а то у него наверное одежда ещё со школы."
    mom emo-67 "Хорошо, тогда доедаем, одеваемся и все вместе поедем покупать [pname_max[2]] одежду."
    $ max_path = 1
    jump loc_veranda

label pgn_dressing_kira_mom_room:
    scene bg pgn_dressing_mom_and_kira_01
    mom emo-64 "[pname_kira[0]], ну блин, ты чего? Одевайся, уже ехать пора."
    k emo-101 "Успеем, ещё много времени. И... Подглядывать за дамами, как они переодеваются куда интереснее. Не так ли, [pname_max[0]]?"
    m emo-13 "А, эм..."
    scene bg pgn_dressing_mom_and_kira_02
    mom emo-63 "[pname_max[0]]! И ты ещё не готов, бегом в свою комнату."
    m emo-8 "Но там сейчас [pname_liza[0]]!"
    mom emo-64 "И... Ты же можешь..."
    mom emo-73 "..."
    mom emo-60 "Хорошо, тогда подожди её. Тебе же не долго одеваться."
    m emo-0 "Ладно."
    $ qtime += 1
    jump loc_pool

label pgn_newmaxward_02:
    scene bg pgn_carmom_allch_01
    $ renpy.pause (3, hard=True)
    scene bg pgn_maxnewclothing_01
    a emo-20 "Мама, а можно мы с [pname_liza[4]] отойдём ненадолго?"
    mom emo-64 "Так, девочки, мы вообще-то дём покупать одежду [pname_max[2]]. Может ни кто и никуда не будет уходить, а вместе поможем ему с выбором!?"
    l emo-49 "Пожалуйста!"
    a emo-24 "Между прочим, вы старше и у вас опыта больше, и вам лучше знать, что ему лучше подойдёт."
    a emo-22 "Так что, Мам?"
    mom emo-72 "..."
    mom emo-69 "Ну хорошо, ладно. Только не долго, иначе без вас уедем домой."
    l emo-41 "Спасибо."
    scene bg pgn_maxnewclothing_02
    other emo-984 "Здравствуйте. Чем могу вам помочь?"
    mom emo-60 "Не могли бы что-нибудь присмотреть для моего сына. А то ходит всё в одном и том же больше года."
    other emo-985 "Думаю, что смогу что-нибудь подобрать."
    mom emo-60 "Спасибо."
    other emo-984 "Вы можете пройти в следующую комнату, а ваш сын может подождать в одной из кабинок. Скоро принесу."
    scene bg pgn_maxnewclothing_03
    m emo-3 "Может я прям тут и буду переодеваться?"
    k emo-114 "Ага, ты ещё разденься полностью и пробегись по всему ТРЦ."
    mom emo-60 "Давай, как нормальные люди, переодеваться будешь в кабинке, а как будешь готов, выйдешь и нам покажешься."
    scene bg pgn_maxnewclothing_04
    $ renpy.pause (3)
    scene bg pgn_maxnewclothing_05
    other emo-984 "Вот, возьмите. Если мало по размеру, или вам не понравилось, сообщите и я принесу другое."
    m emo-3 "Ок"
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_07
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_06
    m emo-0 "Я выхожу."
    scene bg pgn_maxnewclothing_08
    mom emo-72 "Хм... где-то я это уже видела."
    k emo-104 "Я тоже уже припоминаю. И... кажется чего-то здесь не хватает."
    mom emo-62 "Кубиков на животе."
    scene bg pgn_maxnewclothing_14
    m emo-8 "Ну Мама!!!"
    mom emo-60 "[pname_max[0]], нет. Давай что-нибудь другое. По городу в таком ходить тебе не разрешу."
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_07
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_06
    m emo-0 "Готов."
    scene bg pgn_maxnewclothing_09
    mom emo-71 "А, жарко в этом не будет? Сейчас лето, зима не скоро."
    k emo-101 "Здесь такой климат, что холодно, как было у вас там... Забыла, где вы там жили? Ай ладно, тут так холодно точно не будет."
    m emo-0 "Ок, примерю следующее."
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_07
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_10
    m emo-3 "Ну как?"
    scene bg pgn_maxnewclothing_14
    mom emo-62 "Смотрится не плохо. [pname_kira[0]], что думаешь?"
    k emo-109 "Согласна, это получше."
    mom emo-60 "Простите! Не могли бы подойти."
    scene bg pgn_maxnewclothing_11
    other emo-984 "Выбрали?"
    mom emo-62 "Да. А можно что-нибудь из летнего? Чтобы было в чём на пляж сходить, допустим."
    other emo-985 "Конечно. Сейчас, посмотрю."
    scene bg pgn_maxnewclothing_04
    $ renpy.pause (3)
    scene bg pgn_maxnewclothing_05
    m emo-0 "Спасибо."
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_07
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_12
    k emo-112 "Расцветка мне не нравится."
    mom emo-60 "Есть что-то такое, старческое. Может что-нибудь по молодёжнее!?"
    scene bg pgn_maxnewclothing_14
    m emo-8 "Мам, я устал. Может в следующий раз?"
    mom emo-60 "Так хватит. Переодевайся."
    m emo-8 "Ну блин."
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_07
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_13
    k emo-102 "Какой красавец. Сестрёнка, может познакомишь меня с ним. Хахаха"
    mom emo-62 "Мне нравится. А тебе, [pname_max[0]]?"
    m emo-2 "Хм... главное, что вам нравится. Мне и в старом нормально было."
    mom emo-72 "..."
    mom emo-62 "Хорошо. Пойдём на кассу."
    m emo-0 "Подождите, я сейчас, переоденусь."
    mom emo-60 "Можешь и в этом пойти... Хорошо. Будем ждать."
    scene bg pgn_maxnewclothing_15
    a emo-24 "А вот и [pname_max[0]]. Это что ты выбрал, а по лучше ни чего не было?"
    m emo-9 "Эээ... Нормальная одежда, Маме понравилось."
    mom emo-68 "[pname_alice[0]], ну ты чего? Хорошо смотрится."
    mom emo-64 "А если не нравится, нечего было уходить."
    a emo-22 "Я шучу. Поздравляю тебя, наконец в чем-то новом будешь ходить."
    other emo-984 "Спасибо вам за покупку. Приходите ещё."
    scene bg pgn_carmom_allch_02
    $ renpy.pause (3)
    $ max_path = 2
    $ qtime = 13
    jump loc_pool






label pgn_maxfamilyincinema:
    if max_path == 2:
        $ max_path = 3
        m emo-0 "А не хотите сходить в кинотеатр, и фильм какой-нибудь посмотреть?"
        mom emo-69 "Ой, сейчас такие фильмы: боевики, фантастика. Везде это насилие и убийства."
        l emo-41 "Ну почему, есть и те что тебе понравятся."
        a emo-21 "[pname_max[0]] может пойти на боевики, а мы мелодраму посмотрим или комедию."
        mom emo-60 "Будет лучше, если поедем смотреть вместе один определенный фильм. По отдельности не хочется."
        m emo-0 "Ну я тоже могу смотреть, ну эти... ваши фильмы."
        a emo-24 "Точно сможешь продержаться до конца сеанса?"
        m emo-0 "Да что там такого, что не смогу!? Фильмы, как фильмы."
        mom emo-60 "Хватит вам. Тогда одевайтесь и поедем. [pname_kira[0]], ты с нами?"
        k emo-101 "Езжайте без меня, у меня дела."
        mom emo-62 "Хорошо. Удачи тебе с твоими... делами."
    elif max_path >= 3:
        m emo-3 "Может в кино?"
        mom emo-60 "Если девочки не против, то да, конечно, поедем."
        a emo-21 "Мы за."
        m emo-3 "Вот и договорились."
    scene bg pgn_carmom_nokira_02
    $ renpy.pause(3, hard=True)
    scene bg pgn_familycinemamall_01
    mom emo-60 "Так, что сегодня будем смотреть? Есть предложения?"
    m emo-0 "Я..."
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random != 2:
        a emo-20 "[pname_max[0]], и так понятно что ты хочешь. Но я думаю, что сегодня можно посмотреть какую-нибудь мелодраму или комедию."
        $ ivent24.append("cinema_comedy")
    if label_random == 2:
        a emo-21 "Хорошо, давайте сегодня посмотрим, что выберет [pname_max[0]]."
        $ menu_hbox = False
        menu:
            "Комедия":
                $ ivent24.append("cinema_comedy")
            "Боевик":
                $ ivent24.append("cinema_action")

    mom emo-62 "Хорошо, тогда... [pname_max[0]], у тебя есть деньги? С можешь купить нам всем билеты?"
    $ menu_hbox = False
    menu:
        "Да, конечно":
            m emo-0 "Да, у меня есть. Может что ещё перекусить куплю."
            mom emo-62 "Хорошо. Тогда мы с девочками пройдём в зону ожидания. Будем тебя там ждать."
        "Мам, может ты?":
            m emo-2 "Эм... Мам. Если честно у меня недостаточно. Может ты купишь. Но в следующий раз точно я куплю."
            mom emo-69 "Ох... Ладно. Вы идите и как куплю, сразу к вам."
            jump pgn_maxfamilyincinema_all

    scene bg pgn_mall_cinema_maxbuyticket_01
    m emo-0 "Здравствуйте. Мне 4 взрослых билета на фильм."
    other emo-994 "Пожалуйста, выберите места."
    $ menu_hbox = False
    menu:
        "Для всех один ряд":
            scene bg pgn_mall_cinema_maxbuyticket_02
            m emo-0 "Давайте вот эти места."
            other emo-994 "С вас $40"
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"40")
            $ currency -= 40
            $ ivent24.append("cinema_maxbuy_ticket")
            $ menu_hbox = False
            menu:
                "Вернуться с билетами":
                    jump pgn_maxfamilyincinema_01
                "Купить напитки и попкорн":
                    pass
        "Купить себе и Маме на последнем ряду" if mom_path >= 7:
            m emo-0 "Два на вот эти места и два на последний ряд."
            scene bg pgn_mall_cinema_maxbuyticket_02
            other emo-994 "Хорошо. С вас $50. Задние стоят по $15."
            m emo-3 "{i}Видимо знают, что задние неспроста берут, специальная наценка.{/i}"
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"50")
            $ currency -= 50
            $ ivent24.append("cinema_maxbuy_ticket")
            $ ivent24.append("cinema_max_and_mom")
            $ menu_hbox = False
            menu:
                "Вернуться с билетами":
                    jump pgn_maxfamilyincinema_01
                "Купить напитки и попкорн":
                    pass
    scene bg pgn_mall_cinema_maxbuycafe
    other emo-993 "Здравствуйте."
    $ menu_hbox = False
    menu:
        "Купить попкорн и напитки всем":
            $ currency -= 40
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"40")
            $ ivent24.append("cinema_maxbuy_drinkpop_all")
        "Купить попкорн и напитки девочкам":
            $ currency -= 20
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"20")
            $ ivent24.append("cinema_maxbuy_drinkpop_girls")
        "Купить попкорн и напитки себе":
            $ currency -= 10
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"10")
        "Купить попкорн всем":
            $ currency -= 20
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"20")
            $ ivent24.append("cinema_maxbuy_popkorn_all")
        "Купить попкорн девочкам":
            $ currency -= 10
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"10")
            $ ivent24.append("cinema_maxbuy_popkorn_girls")
        "Купить попить всем":
            $ currency -= 20
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"20")
            $ ivent24.append("cinema_maxbuy_drink_all")
        "Купить попить девочкам":
            $ currency -= 10
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"10")
            $ ivent24.append("cinema_maxbuy_drink_girls")

label pgn_maxfamilyincinema_01:
    scene bg pgn_familycinemamall_02
    $ renpy.pause (3, hard=True)
label pgn_maxfamilyincinema_02:
    scene bg pgn_familycinemamall_03
    other emo-995 "Ваши билеты"
    other emo-995 "Приятного вам просмотра."
    if ("cinema_max_and_mom") in ivent24:
        if mom_path == 7:
            jump pgn_maxfamilyincinema_max_and_mom_p1
        if mom_path == 8:
            jump pgn_maxfamilyincinema_max_and_mom_p2
        if mom_path == 9:
            jump pgn_maxfamilyincinema_max_and_mom_p3
        if mom_path >= 10:
            jump pgn_maxfamilyincinema_max_and_mom_p4

label pgn_maxfamilyincinema_all:
    scene animated pgn_maxfamilyincinema_all
    $ renpy.pause(6, hard=True)
    $ renpy.pause()
    jump pgn_maxfamilyincinema_end_good



label pgn_maxfamilyincinema_onlywithmom:
    $ ivent24.append("cinema_max_and_mom_only")
    $ ivent24.append("cinema_comedy")
    scene bg pgn_carmom_max_01
    $ renpy.pause(3, hard=True)
    scene bg pgn_mall_cinema_maxbuyticket_01
    $ menu_hbox = False
    menu:
        "Попросить Маму купить билеты":
            m emo-0 "Мам, можешь ты купить билеты?"
            mom emo-72 "Сам пригласил и мне покупать. Ладно, только ни на что не надейся."
            $ ivent24.append("cinema_max_and_mom")
        "Купить билеты на последний ряд" if mom_path >= 7:
            m emo-0 "Два на последний ряд."
            scene bg pgn_mall_cinema_maxbuyticket_02
            other emo-994 "Хорошо. С вас $30. Задние стоят по $15."
            m emo-3 "{i}Видимо знают, что задние неспроста берут, специальная наценка.{/i}"
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"30")
            $ currency -= 30
            $ ivent24.append("cinema_maxbuy_ticket")
            $ ivent24.append("cinema_max_and_mom")
    jump pgn_maxfamilyincinema_02



label pgn_maxfamilyincinema_max_and_mom_p1:
    if ("cinema_comedy") in ivent24:
        scene animated pgn_maxfamilyincinema_max_and_mom_p1_01
        $ renpy.pause(5)
        scene bg pgn_familycinemamall_06
        $ renpy.pause(3)
        scene animated pgn_maxfamilyincinema_max_and_mom_p1_01
        $ renpy.pause(5)
        scene bg pgn_familycinemamall_06
        $ menu_hbox = False
        menu:
            "Дотронуться до ноги Мамы":
                pass
            "Ничего не делать":
                scene bg pgn_familycinemamall_08
                $ renpy.pause(3)
                jump pgn_maxfamilyincinema_end_good
    if ("cinema_action") in ivent24:
        scene animated pgn_maxfamilyincinema_max_and_mom_p1_02
        $ renpy.pause(4)
        scene bg pgn_familycinemamall_06
        $ renpy.pause(3)
        scene animated pgn_maxfamilyincinema_max_and_mom_p1_02
        $ renpy.pause(4)
        scene bg pgn_familycinemamall_06
        $ menu_hbox = False
        menu:
            "Дотронуться до ноги Мамы":
                pass
            "Ничего не делать":
                scene bg pgn_familycinemamall_08
                $ renpy.pause(3)
                jump pgn_maxfamilyincinema_end_good
    scene bg pgn_familycinemamall_07
    mom emo-69 "[pname_max[0]]. Давай будем спокойно смотреть фильм, раз мы сюда пришли."
    $ menu_hbox = False
    menu:
        "Убрать руку":
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
        "Продолжить":
            $ mom_path = 8
    mom emo-68 "[pname_max[0]]. Я понимаю, это всё твои гормоны. Но только не здесь. Вдруг нас поймают, тогда нас больше сюда не пустят или узнают, что я твоя мама. Так что нет."
    $ menu_hbox = False
    menu:
        "Убрать руку":
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
        "Продолжить":
            pass
    mom emo-64 "Что же ты такой не послушный. Всё, хватит. На неделю будешь наказан."
    $ fine_week_mom = True
    jump pgn_maxfamilyincinema_end_good

label pgn_maxfamilyincinema_max_and_mom_p2:
    scene bg pgn_familycinemamall_08
    mom emo-72 "{i}Ох [pname_max[0]], опять он взял последние места. Я ему снова не позволю сделать, чего ему хочется{/i}"
    mom emo-73 "{i}Дома ещё можно, там нет ни кого постороннего. Но заниматься в общественных местах...{/i}"
    mom emo-69 "{i}В магазине одежды, кабинки закрываются, а тут что, любой может увидеть. Нет, точно нет.{/i}"
    m emo-0 "{i}В прошлый раз Мама резко отреагировала, но может сейчас.{/i}"
    $ menu_hbox = False
    menu:
        "Дотронуться до ноги Мамы":
            scene bg pgn_familycinemamall_07
            mom emo-74 "[pname_max[0]], ты не понял с прошлого раза? На неделю будешь наказан."
            $ fine_week_mom = True
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
        "Ничего не делать":
            $ mom_path = 8
    scene bg pgn_familycinemamall_09
    mom emo-60 "{i}Все смотрят спокойно... К примеру эта парочка.{/i}"
    if ("cinema_comedy") in ivent24:
        scene animated pgn_maxfamilyincinema_max_and_mom_p1_01
    if ("cinema_action") in ivent24:
        scene animated pgn_maxfamilyincinema_max_and_mom_p1_02
    mom emo-69 "{i}А он только об одном и думает.{/i}"
    scene bg pgn_familycinemamall_10
    mom emo-60 "{i}О, а где девушка, не заметила, как она ушла.{/i}"
    other emo-999 "Мммм..."
    scene animated pgn_maxfamilyincinema_max_and_mom_p2
    mom emo-66 "{i}Подождите-ка... Она делает ему минет!? Они вообще в курсе, что мы тут сидим на соседнем ряду!? Молодёжь, совсем стыд потеряли.{/i}"
    other emo-999 "Мммм..."
    mom emo-68 "{i}Что же они делают, так же нельзя. Может напомнить им, где они находятся...{/i}"
    mom emo-73 "{i}Хотя... нет, не буду. Может они разозлятся... Лучше не обращать на них внимание.{/i}"
    scene bg pgn_familycinemamall_14
    other emo-999 "Ааааххх...."
    mom emo-68 "{i}Бедная девочка, схватил её за голову. Надеюсь [pname_max[0]] не заметил, чем они тут занимались{/i}"
    scene bg pgn_familycinemamall_08
    m emo-0 "{i}Блин! Вот же ему свезло, а Мама ни как не поддается, попробую в следующий раз.{/i}"
    $ mom_path = 9
    scene bg pgn_familycinemamall_08
    $ renpy.pause(3)
    jump pgn_maxfamilyincinema_end_good

label pgn_maxfamilyincinema_max_and_mom_p3:
    scene bg pgn_familycinemamall_08
    mom emo-72 "{i}У него уже вошло в привычку выбирать последний ряд. Надеется, что я займусь здесь с ним сексом. Но этому точно не бывать{/i}."
    $ menu_hbox = False
    menu:
        "Дотронуться до ноги Мамы":
            pass
        "Ничего не делать":
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
    scene bg pgn_familycinemamall_07
    m emo-6 "{i}Хм... реакции нет{/i}"
    $ menu_hbox = False
    menu:
        "Убрать руку":
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
        "Продолжить":
            pass
    mom emo-62 "{i}Какой настойчивый, прекращать даже и не собирается.{/i}"
    m emo-3 "{i}Может я попробую сейчас зайти дальше.{/i}"
    $ menu_hbox = False
    menu:
        "Убрать руку":
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
        "Дотронуться до киски":
            pass
    if ("cinema_maxbuy_ticket") not in ivent24:
        mom emo-74 "[pname_max[0]]! Руку убрал! И сиди спокойно смотри фильм."
        scene bg pgn_familycinemamall_08
        $ renpy.pause(3)
        jump pgn_maxfamilyincinema_end_good
    scene bg pgn_familycinemamall_16
    $ menu_hbox = False
    menu:
        "Убрать руку":
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
        "Продолжить":
            pass
    if ("cinema_maxbuy_popkorn_girls") in ivent24 or ("cinema_maxbuy_drink_girls") in ivent24:
        $ label_random = renpy.random.randint ( 1, 3)
    elif ("cinema_maxbuy_popkorn_all") in ivent24 or ("cinema_maxbuy_drink_all") in ivent24:
        $ label_random = renpy.random.randint ( 1, 2)
    elif ("cinema_maxbuy_drinkpop_girls") in ivent24 or ("cinema_maxbuy_drinkpop_all") in ivent24:
        $ label_random = 2
    elif ("cinema_max_and_mom_only") in ivent24:
        $ label_random = renpy.random.randint ( 1, 3)
    if label_random != 2:
        mom emo-71 "Ну всё. Кино окончено, на выход. Живо!"
        $ fine_week_mom = True
        jump pgn_maxfamilyincinema_end_bed
    m emo-4 "{i}Отлично, Мама без трусиков, тогда продолжу, может она в ответ вознаградит минетом.{/i}"
    mom emo-73 "{i}Ох сынок, что ж ты делаешь с киской мамочки.{/i}"
    mom emo-69 "Аххх... Ммм..."
    mom emo-68 "Ахххх..."
    mom emo-73 "{i}Если он так продолжит активно массировать мою киску, то не только платье, но и сиденье будет мокрым.{/i}"
    mom emo-73 "{i}Я не против, но лучше прекратить, пока не поздно.{/i}"
    scene bg pgn_familycinemamall_15
    mom emo-71 "[pname_max[0]]... пожалуйста... прекрати."
    m emo-3 "Тебе же нравится, так? Почему мне не продолжить?"
    mom emo-68 "Ты же не хочешь, чтобы Мама вышла с мокрым платьем, и люди подумали, что я описалась? Мне будет очень стыдно."
    scene bg pgn_familycinemamall_08
    mom emo-75 "Спасибо. Давай досмотрим фильм до конца."
    m emo-4 "{i}Ладно, прогресс какой-то есть. Попробую в следующий раз.{/i}"
    $ mom_path = 10
    jump pgn_maxfamilyincinema_end_good

label pgn_maxfamilyincinema_max_and_mom_p4:
    scene bg pgn_familycinemamall_08
    if mom_path == 10:
        m emo-3 "{i}Надеюсь в этот раз у меня получится{/i}"
    if pgn_ach_repeat == 0:
        $ menu_hbox = False
        menu:
            "Ничего не делать":
                scene bg pgn_familycinemamall_08
                $ renpy.pause(3)
                jump pgn_maxfamilyincinema_end_good
            "Дотронуться до киски":
                pass
    scene bg pgn_familycinemamall_16
    if pgn_ach_repeat == 0:
        if ("cinema_maxbuy_ticket") not in ivent24:
            mom emo-74 "[pname_max[0]]! Руку убрал! И сиди спокойно смотри фильм."
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
        if ("cinema_maxbuy_popkorn_girls") in ivent24 or ("cinema_maxbuy_drink_girls") in ivent24:
            $ label_random = renpy.random.randint ( 1, 3)
        elif ("cinema_maxbuy_popkorn_all") in ivent24 or ("cinema_maxbuy_drink_all") in ivent24:
            $ label_random = renpy.random.randint ( 1, 2)
        elif ("cinema_maxbuy_drinkpop_girls") in ivent24 or ("cinema_maxbuy_drinkpop_all") in ivent24:
            $ label_random = 2
        elif ("cinema_max_and_mom_only") in ivent24:
            $ label_random = renpy.random.randint ( 1, 3)
        if label_random != 2 and mom_path < 11:
            mom emo-71 "Ну всё. Кино окончено, на выход. Живо!"
            $ fine_week_mom = True
            jump pgn_maxfamilyincinema_end_bed
        if label_random != 2 and mom_path >= 11:
            mom emo-72 "Нет. Ты не заслужил. Так что посидим спокойно и досмотрим фильм до конца."
            scene bg pgn_familycinemamall_08
            $ renpy.pause(3)
            jump pgn_maxfamilyincinema_end_good
    mom emo-73 "{i}Снова он за своё...{/i}"
    mom emo-69 "Аааххх... Ммм..."
    mom emo-69 "{i}Я же так потеку. Нужно что сделать и кажется я догадываюсь, что я должна сделать.{/i}"
    scene bg pgn_familycinemamall_17
    m emo-4 "Мама, ты сделаешь мне..?"
    if pgn_ach_repeat == 0:
        if ("cinema_maxbuy_popkorn_girls") in ivent24 or ("cinema_maxbuy_drink_girls") in ivent24:
            $ label_random = renpy.random.randint ( 1, 3)
        elif ("cinema_maxbuy_popkorn_all") in ivent24 or ("cinema_maxbuy_drink_all") in ivent24:
            $ label_random = renpy.random.randint ( 1, 2)
        elif ("cinema_maxbuy_drinkpop_girls") in ivent24 or ("cinema_maxbuy_drinkpop_all") in ivent24:
            $ label_random = 1
        elif ("cinema_max_and_mom_only") in ivent24:
            $ label_random = renpy.random.randint ( 1, 3)
    if pgn_ach_repeat == 104:
        $ label_random = 1
    if label_random != 1:
        mom emo-67 "Сегодня только руками."
        scene animated pgn_maxfamilyincinema_max_and_mom_p4_hj
        m emo-7 "{i}Ох да, Мама дрочит мне в кинотеатре. Может в следующий раз мне и минет сделает.{/i}"
        $ renpy.pause()
        m emo-2 "Мама... Я..."
        mom emo-69 "Кончи Маме в руку."
        scene bg pgn_familycinemamall_20
        m emo-10 "Ааааххх..."
        mom emo-75 "Хорошо, что взяла с собой салфетки. Руки вытру и заодно твой член."
        $ PGN_Addstatsex(stat_mom, 0, 0, 0, 0, 1)
    if label_random == 1:
        mom emo-75 "{i}Заплатил за всех и девочкам что-то купил, так что моя очередь отблагодарить.{/i}"
        scene bg pgn_familycinemamall_21
        mom emo-75 "Сейчас мамочка сделает тебе приятное. Только смотри по сторонам. Хорошо?"
        m emo-3 "Конечно, Мам."
        scene animated pgn_maxfamilyincinema_max_and_mom_p4_bj
        m emo-7 "Мммм... Ооо... Да..."
        m emo-10 "Да... Мама... Скоро, уже скоро..."
        scene bg pgn_familycinemamall_27 with dissolve
        m emo-10 "Аааах..."
        scene bg pgn_familycinemamall_28
        if pgn_ach_repeat == 104:
            jump table_pgn_achievement
        if pgnach_104.aopen == False:
            $ PGN_Achadd(pgnach_104, 104)
        mom emo-75 "Доволен?"
        m emo-4 "Да"
        $ PGN_Addstatsex(stat_mom, 0, 0, 1, 0, 0)
    mom emo-62 "Ну всё, давай теперь досмотрим фильм. И поедем домой."
    m emo-3 "Спасибо тебе, Мам."
    if mom_path == 10:
        $ mom_path = 11
    jump pgn_maxfamilyincinema_end_good

label pgn_maxfamilyincinema_end_good:
    if ("cinema_max_and_mom_only") in ivent24:
        scene bg pgn_carmom_max_01
        $ qtime += 3
        $ renpy.pause(3, hard=True)
        jump loc_pool
    scene bg pgn_familycinemamall_01
    a emo-25 "Мама, ну как тебе фильм?"
    mom emo-62 "Знаешь. Мне понравилось. Давно не ходила в кинотеатры. Так что можно по выходным ходить."
    l emo-41 "Мне тоже очень понравилось."
    a emo-22 "По тебе видно, прям светишься от счастья."
    mom emo-62 "Хорошо провели время, пора нам домой отправляться."
    $ qtime += 3
    scene bg pgn_carmom_nokira_02
    $ renpy.pause(3, hard=True)
    jump loc_pool

label pgn_maxfamilyincinema_end_bed:
    if ("cinema_max_and_mom_only") in ivent24:
        scene bg pgn_carmom_max_01
        $ qtime += 3
        $ renpy.pause(3, hard=True)
        jump loc_pool
    scene bg pgn_familycinemamall_01
    l emo-50 "Мама!?"
    a emo-24 "Что случилось, что вы так резко выбежали?"
    mom emo-73 "Фильм не понравился и... Забудьте. В качестве компенсации, давайте лучше пройдёмся по магазинам."
    a emo-20 "Хорошо."
    $ qtime += 3
    scene bg pgn_carmom_nokira_02
    $ renpy.pause(3, hard=True)
    jump loc_pool





label pgn_ladefirstvisit:
    $ accessiv.append("lade_firstwithkira")
    $ ivent24.append("LaDe")
    m emo-0 "Тёть [pname_kira[6]], а почему ты не ездишь с Мамой и девочками на шоппинг?"
    mom emo-62 "Действительно. Сестрёнка, может поедешь с нами и немного развеешься?"
    k emo-102 "Спасибо за предложение, но нет."
    l emo-41 "Почему? Ты могла бы помочь нам с выбором одежды."
    a emo-24 "Да, ты всегда так красиво одеваешься."
    m emo-4 "{i}Не просто красиво, а чертовски сексуально. Да Тётю в любой одежде хочется трахнуть.{/i}"
    mom emo-62 "Ну, в самом деле, поехали с нами!"
    k emo-101 "Спасибо вам дорогие за такие теплые слова. Но... у меня и так много платьев. Может..."
    a emo-20 "Может, что?"
    k emo-113 "Не хотите съездить за покупками нижнего белья? У каждой наверняка есть кто-то, кому показать своё шикарное тело."
    l emo-48 "..."
    mom emo-72 "[pname_liza[2]] ещё рано показывать кому-то своё тело, ей учится нужно."
    k emo-101 "... Да, тут я не подумала, когда сказала. Ну, не у неё, так у вас."
    mom emo-73 "..."
    a emo-33 "..."
    m emo-3 "{i}Все точно подумали обо мне, это видно по их глазам.{/i}"
    k emo-101 "Так что, поедем?"
    mom emo-62 "Хорошо. Пойдём собираться. И поедем."
    jump loc_veranda

label pgn_shopping_lade:
    scene bg pgn_carmom_allch_02
    $ renpy.pause(3, hard=True)
    $ label_random = renpy.random.randint ( 1, 2)
    if label_random == 1:
        scene bg pgn_shopping_lade_family01
    if label_random == 2:
        scene bg pgn_shopping_lade_family03
    m emo-0 "{i}Как обычно, только приехали они сразу разбежались, кто куда.{/i}"
    $ menu_hbox = True
    menu:
        "Подслушать сестер":
            scene bg pgn_shopping_lade_family02
            l emo-50 "[pname_alice[0]]!"
            a emo-33 "Даже через эти тонкие штанишки не могу нащупать твоё бельё. Оно тоже такое тонкое или кто-то просто забыл надеть?"
            l emo-42 "Хватит меня там трогать! А если Мама увидит или кто-нибудь ещё?"
            a emo-21 "Скажу, что это всё не так выглядит, как кажется. Просто попка младшей сестрёнки оказалась рядом с моей рукой. Совершенно случайно."
            l emo-50 "Ах! [pname_alice[0]]!"
            a emo-25 "Давай твоя старшая и опытная сестра поможет тебе с выбором белья. [pname_max[0]] будет прям без ума."
            l emo-49 "Х-х-хорошо, пойдём в примерочную."
            scene bg pgn_shopping_lade_family05
            l emo-41 "Мы... мы пошли."
            a emo-22 "Да, не скучай братец. Мы пойдём примерять бельё."
        "Подслушать Маму и Тётю":
            scene bg pgn_shopping_lade_family04
            k emo-103 "[pname_mom[6]], да ладно тебе. Примерь."
            mom emo-69 "А не слишком ли вызывающе?"
            k emo-113 "В самый раз. И это не для каких-то мужчин, а лишь только для одного. Итак понятно кого я имею в виду."
            mom emo-60 "Может мне попробовать красное?"
            k emo-112 "Нет. Красное подойдёт для меня, под цвет волос. Тебе лучше подойдёт черное."
            mom emo-68 "Давай что-нибудь другое. Ну не могу я в это одеться, да и ещё показаться ему."
            k emo-104 "Вот это да! Так голой это нормально, а надеть сексуальное бельё, это уже что-то выходящее за рамки? Ты забыла про наши фотосессии?"
            k emo-109 "Или ты хочешь что-то более откровенное? А, сестренка?"
            mom emo-69 "Даже и не знаю."
            k emo-101 "Хорошо. Давай я что-нибудь присмотрю, и консультантка нам поможет подобрать тебе что-нибудь особое. Пойдём."
            scene bg pgn_shopping_lade_family06
            mom emo-60 "Сынок, м-мы пойдём в примерочную, а, а ты подожди нас здесь. Хорошо?"
            m emo-0 "Ладно."
    scene bg pgn_shopping_lade_family07
    m emo-3 "{i}Ну так что, мне сидеть и ждать всех или всё же заглянуть к кому-нибудь?{/i}"
    $ menu_hbox = True
    menu:
        "К Маме и Тёте":
            jump pgn_shopping_lade_momkira
        "Просто ждать":
            jump pgn_shopping_lade_cash
        "К сестрам":
            jump pgn_shopping_lade_sisters

label pgn_shopping_lade_sisters:
    scene bg pgn_shopping_lade_family08
    m emo-0 "Девчонки, вам моя помощь нужна?"
    a emo-20 "Сядь пока и жди. И не смей входить, иначе не будет никакого сюрприза."
    m emo-4 "{i}Сюрприз! Хм... интересно.{/i}"
    $ menu_hbox = False
    menu:
        "Заглянуть в левую кабинку":
            pass
        "Заглянуть в правую кабинку":
            scene bg pgn_shopping_lade_family10
            $ renpy.pause(2)
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random != 3:
                scene bg pgn_shopping_lade_family14
                m emo-6 "Пусто."
                $ menu_hbox = False
                menu:
                    "Заглянуть в левую кабинку":
                        pass
                    "Ждать":
                        jump pgn_shopping_lade_sisters_wait
            if label_random == 3:
                scene bg pgn_shopping_lade_family12
                m emo-4 "{i}Хехе, [pname_alice[0]] в одних трусиках.{/i}"
                a emo-28 "[pname_max[0]]! Ну, я же попросила тебя подождать."
                scene bg pgn_shopping_lade_family13
                m emo-3 "Я... это... Ты сказала, что будет какой-то сюрприз."
                a emo-21 "Ага, поняла. Твой сюрприз... какое бельё я не выберу, ты за него заплатишь."
                m emo-9 "Э..."
                a emo-25 "А надо было ждать. Всё, выходи."
                m emo-8 "{i}Блин!{/i}"
                scene bg pgn_shopping_lade_family09
                $ renpy.pause(3)
                $ ivent24.append("lade_buy_alice")
                jump pgn_shopping_lade_cash
        "Ждать":
            jump pgn_shopping_lade_sisters_wait
    scene bg pgn_shopping_lade_family11
    l emo-50 "Ай! [pname_alice[0]]! ... Ты куда свои... пальцы... Ай!"
    a emo-20 "Стой смирно и не двигайся! Я поправляю."
    m emo-3 "{i}Интересно, что там происходит.{/i}"
    scene bg pgn_shopping_lade_family15
    a emo-23 "[pname_max[0]]! Что же ты такой нетерпеливый."
    m emo-0 "Простите."
    a emo-20 "Выйди. Закончим примерку и будет твой сюрприз."
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random != 2:
        pass
    if label_random == 2:
        a emo-21 "И в качестве наказание, за непослушание, ты заплатишь за наше бельё."
        m emo-8 "Понял."
        scene bg pgn_shopping_lade_family09
        $ renpy.pause(3)
        $ ivent24.append("lade_buy_alice_and_liza")
        jump pgn_shopping_lade_cash

label pgn_shopping_lade_sisters_wait:
    scene bg pgn_shopping_lade_family09
    $ renpy.pause(3, hard=True)
    a emo-24 "[pname_liza[0]], ты готова?"
    l emo-41 "Да."
    a emo-21 "Тогда... 1..."
    l emo-41 "2..."
    a emo-21 "3!!!"
    scene bg pgn_shopping_lade_family16
    l emo-41 "Выбирай. В какую кабинку ты хочешь зайти?"
    m emo-0 "А можно, чтобы вы были вместе или сначала в одну, а потом в другую?"
    a emo-25 "Нет. Можешь выбрать только одну из нас."
    $ menu_hbox = True
    menu:
        "[pname_liza[0]]":
            jump pgn_shopping_lade_sisters_liza
        "[pname_alice[0]]":
            jump pgn_shopping_lade_sisters_alice

label pgn_shopping_lade_sisters_liza:
    scene bg pgn_shopping_lade_family17
    l emo-41 "Ох, [pname_max[0]], ты ко мне зашёл. Как тебе? Нравится?"
    m emo-5 "Ого..."
    l emo-41 "Тебе настолько нравится, что даже челюсть отвисла?"
    scene bg pgn_shopping_lade_family18
    m emo-3 "А бюстгальтер и должен быть таким... открытым?"
    l emo-43 "Да. Мне [pname_alice[0]] посоветовала это надеть."
    scene bg pgn_shopping_lade_family19
    l emo-46 "Как думаешь, стоит покупать?"
    $ menu_hbox = True
    menu:
        "Да":
            pass
        "Нет":
            l emo-40 "Ладно, тогда подожди меня снаружи."
            m emo-9 "А сюрприз?"
            l emo-42 "Жди меня снаружи!"
            scene bg pgn_shopping_lade_family09
            $ renpy.pause(3)
            jump pgn_shopping_lade_cash
    l emo-41 "Спасибо. Твоё мнение очень важно для меня."
    m emo-13 "Эм, [pname_liza[0]]!"
    l emo-48 "Что такое?"
    m emo-13 "Поможешь мне?"
    scene bg pgn_shopping_lade_family20
    l emo-41 "Твоя большая проблема требует внимания!? Конечно, снимай штаны, помогу. А то ой как будет неудобно сотрудницам магазина и Маме, когда будешь стоять возле кассы со стоячим членом."
    m emo-3 "Спасибо за понимание."
    $ ivent24.append("lade_buy_liza")
    $ menu_hbox = False
    menu:
        "Пусть продолжает":
            jump pgn_shopping_lade_sisters_liza_bj
        "Да и я могу оплатить покупку":
            l emo-41 "Вау! Спасибо."
            m emo-3 "Мне не сложно, главное, чтобы ты была счастлива."
            l emo-48 "..."
            l emo-49 "Что сейчас хочется моему щедрому парню и братишке?"
            $ menu_hbox = True
            menu:
                "Минет":
                    jump pgn_shopping_lade_sisters_liza_bj
                "Анал":
                    pass
    l emo-41 "А презервативы у тебя с собой?"
    if condom.numbsuse > 0:
        m emo-3 "Да"
        jump pgn_shopping_lade_sisters_liza_anal
    m emo-2 "Нет"
    l emo-46 "Тогда я могу предложить только минет."
    m emo-4 "Может я сбегаю в магазин и куплю?"
    l emo-44 "И заставишь сестрёнку ждать?"
    m emo-3 "Хорошо. Минет тоже подойдёт."
    jump pgn_shopping_lade_sisters_liza_bj

label pgn_shopping_lade_sisters_liza_bj:
    scene bg pgn_shopping_lade_family21
    l emo-48 "Где же эта большая палка?"
    scene bg pgn_shopping_lade_family22
    l emo-50 "Ох! Большой и твердый. Тогда начинаю."
    scene animated pgn_shopping_lade_sisters_liza_bj
    m emo-7 "О да..."
    m emo-4 "{i}Смотрит прямо на меня... молодец... Класс!!!{/i}"
    m emo-10 "Сестрёнка, я... сейчас кончу... Ааахххх!!!"
    scene bg pgn_shopping_lade_family28
    l emo-41 "Ах... Братик, ты всю меня испачкал."
    m emo-3 "Видимо мне всё же придётся купить это бельё."
    l emo-48 "Спасибо. Ты лучший."
    $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
    scene bg pgn_shopping_lade_family09
    $ renpy.pause(3)
    jump pgn_shopping_lade_cash

label pgn_shopping_lade_sisters_liza_anal:
    scene bg pgn_shopping_lade_family29
    l emo-46 "[pname_max[0]]! Только давай по осторожней, не торопись."
    m emo-3 "Ок."
    scene animated pgn_shopping_lade_sisters_liza_anal
    l emo-49 "Ааахх... Ааахх... Мммм... Братик... Да..."
    m emo-7 "{i}Который раз трахаю сестренку в попу, а она всё ещё такая тугая.{/i}"
    l emo-48 "Братик... Может... Ускоришься... Или..."
    l emo-49 "Или хотя бы войдёшь глубже..."
    l emo-48 "Бра..."
    m emo-10 " Аааххх... Извини... Больше не могу..."
    scene bg pgn_shopping_lade_family35
    l emo-48 "Ну что ж ты так слабо."
    m emo-8 "Прости."
    l emo-41 "Ладно, тогда дома наверстаешь."
    $ PGN_Addstatsex(stat_liza, 1, 0, 0, 0, 0)
    scene bg pgn_shopping_lade_family09
    $ renpy.pause(3)
    jump pgn_shopping_lade_cash

label pgn_shopping_lade_sisters_alice:
    scene bg pgn_shopping_lade_family36
    m emo-8 "Ай!"
    a emo-22 "Ммм... У моего озабоченного братика уже стоит."
    a emo-24 "А если надавлю сильнее, то вся сперма выйдет наружу?"
    m emo-8 "Не, скорее всего ты мне просто раздавишь мои яйца."
    a emo-20 "Снимай штаны."
    m emo-6 "Зачем?"
    a emo-21 "Снимай."
    scene bg pgn_shopping_lade_family37
    a emo-21 "Так что?"
    m emo-6 "Что, что?"
    a emo-21 "Как я смотрюсь в этом?"
    m emo-13 "{i}Тут и так очевидно, у меня нет выбора. С каждой секундой молчания всё сильнее и сильнее сжимает мой член.{/i}"
    a emo-20 "Не молчи, скажи уже!"
label pgn_shopping_lade_sisters_alice_choice01:
    $ menu_hbox = False
    menu:
        "Красиво. Можешь купить":
            m emo-3 "Мне нравится. Если тебе тоже нравится, бери."
            a emo-20 "Хм... ладно. Куплю."
            m emo-0 "А..."
            a emo-20 "Надевай штаны и жди меня снаружи, пока я буду переодеваться."
            m emo-0 "{i}Что я не так сказал!?{/i}"
            scene bg pgn_shopping_lade_family09
            $ renpy.pause(3)
            jump pgn_shopping_lade_cash
        "Так себе":
            scene bg pgn_shopping_lade_family38
            m emo-13 "А по лучше ни чего найти не смогла? Смотрится не очень."
            a emo-28 "Да!? А может ещё подумаешь?"
            scene bg pgn_shopping_lade_family37
            m emo-2 "Ай-ай! Не сжимай так сильно!"
            $ menu_hbox = True
            menu:
                "Передумать":
                    jump pgn_shopping_lade_sisters_alice_choice01
                "Настоять на своём":
                    m emo-0 "Я уверен. Давай схожу и выберу другое бельё, а ты его примеришь?"
                    a emo-23 "Хм... Дай подумать... Нет! Выходи, мне нужно переодеться."
                    m emo-9 "Без штанов?"
                    a emo-21 "Да. Либо выйдешь без штанов, либо заплатишь за меня."
                    m emo-0 "Ладно, хорошо, я куплю."
                    a emo-20 "Вот и отлично. Выйди, мне нужно переодеться."
                    scene bg pgn_shopping_lade_family09
                    $ renpy.pause(3)
                    $ ivent24.append("lade_buy_alice")
                    jump pgn_shopping_lade_cash
        "Отлично выглядишь. Давай куплю тебе.":
            pass
    a emo-20 "Спасибо. Правда я надела то, что сразу мне на глаза попалось."
    m emo-3 "Удачный выбор..."
    m emo-4 "Ты в любом белье будешь всё той же сексуальной старшей сестрой."
    scene bg pgn_shopping_lade_family38
    a emo-22 "Ах, [pname_max[0]], [pname_max[0]]! Даже представить сложно, если бы вторым ребенком была девочка. Я очень рада, что у меня есть брат, и ещё с таким... Большим..."
    a emo-25 "Хочешь, сестренка поможет тебе кончить? Чего тебе хочется?"
label pgn_shopping_lade_sisters_alice_choice02:
    $ menu_hbox = True
    menu:
        "Минет":
            a emo-21 "Хорошо. Только я сниму с себя всё. А то как-то будет нехорошо, когда на кассе заметят бельё испачканное белой жидкостью братика."
            jump pgn_shopping_lade_sisters_alice_bj
        "Вагинал":
            a emo-21 "Хорошо. Только я сниму с себя всё. А то как-то будет нехорошо, когда на кассе заметят бельё испачканное белой жидкостью братика."
            jump pgn_shopping_lade_sisters_alice_vaginal
        "Анал":
            if pornfilm5.filming == 0:
                a emo-28 "Нет. Анальный секс только на съёмках. Не могу, так что нет."
            if pornfilm5.filming > 0:
                a emo-23 "Прости, но нет. Я не [pname_liza[0]], я не могу настолько быть уверенной в чистоте моей попки."
                if condom.numbsuse > 0:
                    m emo-3 "У меня есть презервативы."
                    a emo-21 "...Хм... Нет, извини. Если хочешь в попу, то только дома. Ладно?"
                    m emo-0 "Ок."
            jump pgn_shopping_lade_sisters_alice_choice02

label pgn_shopping_lade_sisters_alice_bj:
    a emo-20 "Ляг, мне так будет удобнее."
    scene animated pgn_shopping_lade_sisters_alice_bj
    m emo-7 "Сестренка может возьмешь полностью..."
    m emo-8 "Ай! Не кусайся.... Ладно, я молчу..."
    m emo-10 "{i}О, да!!! Люблю я такой шоппинг, каждый по-своему получает удовольствие от похода по магазинам.{/i}"
    m emo-7 "Я сейчас..."
    scene bg pgn_shopping_lade_family44
    $ renpy.pause(0.6)
    scene bg pgn_shopping_lade_family45
    $ renpy.pause(0.6)
    scene bg pgn_shopping_lade_family44
    $ renpy.pause(0.6)
    scene bg pgn_shopping_lade_family45
    $ renpy.pause(0.6)
    scene bg pgn_shopping_lade_family46
    m emo-12 "Аааххх... Охххх..."
    a emo-21 "Спасибо. Увидимся у кассы."
    m emo-3 "Ок."
    $ PGN_Addstatsex(stat_alice, 0, 0, 1, 0, 0)
    scene bg pgn_shopping_lade_family09
    $ renpy.pause(3)
    $ ivent24.append("lade_buy_alice")
    jump pgn_shopping_lade_cash

label pgn_shopping_lade_sisters_alice_vaginal:
    scene bg pgn_shopping_lade_family47
    a emo-30 "Ай! [pname_max[0]]! Ну не так же сходу. Аккуратней, он у тебя не маленький, чтоб так резко."
    m emo-8 "Извини."
    scene animated pgn_shopping_lade_sisters_alice_vaginal
    a emo-21 "Да, вот так. Не торопись."
    a emo-33 "И... давай по... поглубже... Ааахх..."
    a emo-25 "Ааааххх... Мммм... Ох... Да..."
    m emo-7 "Больше не могу... сейчас..."
    scene bg pgn_shopping_lade_family54
    m emo-12 "Ааааргх... Ааа..."
    scene bg pgn_shopping_lade_family55
    a emo-21 "Что-то ты быстро, я даже не кончила. Значит ты мне купишь?"
    m emo-15 "Да, да, куплю."
    a emo-21 "Тогда хорошо. Надевай штаны и жди меня снаружи, мне нужно тут немного прибраться."
    $ PGN_Addstatsex(stat_alice, 0, 0, 0, 1, 0)
    scene bg pgn_shopping_lade_family09
    $ renpy.pause(3)
    $ ivent24.append("lade_buy_alice")
    jump pgn_shopping_lade_cash

label pgn_shopping_lade_momkira:
    scene bg pgn_shopping_lade_family56
    "Тук-тук"
    k emo-100 "Кто там?"
    m emo-0 "Это я"
    scene bg pgn_shopping_lade_family57
    k emo-101 "О! Решил к нам заглянуть."
    m emo-13 "Можно?"
    k emo-103 "Что, хочешь увидеть мамочку в сексуальном белье?"
    m emo-13 "Нет, мне просто одному скучно."
    k emo-114 "Да, да..."
    mom emo-60 "Кто там? Принесли бельё на примерку?"
    k emo-113 "Нет, тут [pname_max[0]]. Он хочет составить нам компанию."
    mom emo-60 "Может подождёшь нас с наружи?"
    m emo-2 "Ну пожалуйста."
    mom emo-60 "Хорошо, пусть заходит."
    m emo-3 "Спасибо."
    scene bg pgn_shopping_lade_family58
    k emo-100 "Можешь сесть или лечь на диван, как хочешь. Только обувь сними."
    m emo-0 "Понял."
    k emo-105 "[pname_max[0]], будь хорошим мальчиком и не подглядывай. Пока мы будем переодеваться, посиди спокойно на диване."
    if mom_path < 11:
        mom emo-63 "Иначе будешь наказан на неделю."
        k emo-105 "Понял?"
    m emo-0 "Ладно."
    scene bg pgn_shopping_lade_family59
    $ menu_hbox = False
    menu:
        "Подглядеть за Тётей":
            $ label_random = renpy.random.randint ( 1, 2)
            if label_random != 2:
                pass
            if label_random == 2:
                scene bg pgn_shopping_lade_family61
                m emo-4 "{i}Вот это попка. Класс!!!{/i}"
            scene bg pgn_shopping_lade_family60
            $ label_random = renpy.random.randint ( 1, 4)
            if label_random != 2:
                k emo-103 "Ох, [pname_max[0]]! ... Хорошо, притворюсь, что тебя тут не было. Если удовлетворен увиденным, то сядь на диван и подожди нас."
            if label_random == 2:
                k emo-109 "[pname_mom[7]], тут ко мне заглянул один непослушный мальчишка."
                if mom_path < 11:
                    mom emo-60 "Значит этот кое-кто будет наказан на неделю и будет ждать нас снаружи."
                    m emo-15 "Просите."
                    $ fine_week_mom = True
                    jump pgn_shopping_lade_cash
                if mom_path >= 11:
                    mom emo-62 "[pname_max[0]], зайди ко мне."
                    scene bg pgn_shopping_lade_family64
                    $ renpy.pause()
                    if pgnach_107.aopen == False:
                        $ PGN_Achadd(pgnach_107, 107)
                    scene bg pgn_shopping_lade_family62
                    mom emo-62 "Наказывать не буду, но сядь и подожди нас."
                    m emo-3 "Хорошо."
        "Подглядеть за Мамой":
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random != 2 or mom_path < 11:
                $ label_random = 0
            if label_random == 2:
                scene bg pgn_shopping_lade_family63
                m emo-9 "{i}Вау! Мама мастурбирует в кабинке. Я бы тебе сейчас помог.{/i}"
            scene bg pgn_shopping_lade_family62
            if mom_path < 11:
                mom emo-63 "Кто-то видимо не расслышал, но тебе сказали сидеть и ждать."
                m emo-15 "Прости."
                mom emo-63 "Одним \"прости\", не отделаешься. На неделю будешь наказан."
                mom emo-63 "Так что на выход и жди, когда мы закончил."
                m emo-15 "Понял."
                $ fine_week_mom = True
                jump pgn_shopping_lade_cash
            if mom_path >= 11:
                mom emo-62 "[pname_max[0]]!"
                m emo-2 "Прости! Я подожду вас на диване."
                mom emo-73 "Задержись на минутку."
                scene bg pgn_shopping_lade_family64
                m emo-3 "Вау!"
                if pgnach_107.aopen == False:
                    $ PGN_Achadd(pgnach_107, 107)
                mom emo-62 "А теперь присядь и подожди нас."
                m emo-3 "Хорошо."
        "ждать":
            pass
    scene bg pgn_shopping_lade_family59
    $ renpy.pause(3, hard=True)
    if ("lade_first_consultantwrong_01") not in onetevent:
        $ onetevent.append("lade_first_consultantwrong_01")
        scene bg pgn_shopping_lade_family65
        other emo-988 "Ох! Молодой человек, вы что тут делаете? А ну живо отсюда, пока я охрану не вызвала."
        mom emo-67 "Мисс, всё хорошо, мы ему разрешили и он нам не чужой. "
        k emo-103 "Если можно, в качестве исключения, пусть останется и не нужно ни какой охраны."
        other emo-986 "Хорошо, как пожелаете."
    scene bg pgn_shopping_lade_family66
    other emo-987 "Я принесла вам одну из коллекций нижнего белья."
    other emo-987 "Это вам. Вот возьмите. Если я вам понадоблюсь, позовите."
    scene bg pgn_shopping_lade_family59
    k emo-109 "[pname_mom[7]], ты готова?"
    mom emo-60 "Да, почти... Всё."
    scene bg pgn_shopping_lade_family67
    k emo-114 "Та-дам. Ну как?"
    mom emo-64 "[pname_kira[0]], где трусики? Ты специально попросила консультанта не приносить их мне?"
    k emo-104 "Тебе, без них даже лучше. И перестань прикрывать свою киску, здесь только [pname_max[0]]. Пойдём к зеркалу, а то так не видно ничего."
    scene bg pgn_shopping_lade_family68
    mom emo-66 "Ой, [pname_kira[0]]! Эти веревочки сзади совсем ничего не перекрывают, они здесь только для красоты."
    k emo-102 "Вот именно, а зачем скрывать такую красоту. Ведь так, [pname_max[0]]?"
    m emo-1 "А? Да, да. Всё верно Тётя."
    mom emo-68 "[pname_max[0]]!?"
    m emo-0 "А...? Что?."
    scene bg pgn_shopping_lade_family69
    k emo-109 "Только я бы ещё на трусиках сделал разрез..."
    mom emo-69 "[pname_kira[0]], я до сих пор удивляюсь тебе, совсем не стыдно говорить такие вещи в присутствии..."
    k emo-100 "Ммм!? Что? [pname_max[0]] взрослый и уже не ребенок."
    mom emo-60 "Да, но..."
    k emo-101 "Вставай, теперь мы посмотрим на тебя. И встань в какую-нибудь красивую позу."
    scene bg pgn_shopping_lade_family70
    k emo-109 "О да, сестренка!"
    k emo-109 "Что скажешь, [pname_max[0]]? Мамочка сексуальна в этом нижнем белье, хочешь её?"
    mom emo-68 "[pname_kira[0]], ну что ты!?"
    m emo-1 "Эм... э..."
    scene bg pgn_shopping_lade_family71
    k emo-103 "[pname_mom[6]], как можно быть такой сексуальной, что у собственного сына дар речи пропал от такой красоты."
    mom emo-73 "[pname_max[0]], тебе действительно нравится?"
    m emo-4 "Ух... Да, конечно."
    scene bg pgn_shopping_lade_family72
    mom emo-69 "Тогда я куплю, только не обещаю, что буду всегда в этом ходить, может по определенным поводам."
    mom emo-60 "Нам пора переодеваться, да и девочки наверное нас уже заждались."
    k emo-108 "Конечно, только у нас появилась большая проблемка, которую нам нужно уладить вместе."
    if mom_path < 11:
        k emo-109 "Давай, раздевайся."
        scene bg pgn_shopping_lade_family73
        mom emo-73 "Какая? А... поняла. Снова его гормоны."
        k emo-104 "[pname_mom[7]], при чём тут снова гормоны. Две взрослые и очень привлекательные женщины в нижнем белье, хоть у кого встанет."
        mom emo-68 "Мы же не можем заниматься здесь сексом. [pname_max[0]], может ты прикроешься и попробуем незаметно дойти до машины, а там уже дома..."
        k emo-101 "Нет, нет, нужно принять ответственность за свои действия."
        mom emo-60 "Хорошо. А вдруг нас увидят?"
        k emo-101 "Я закрыла дверь, никто нас не потревожит. И сейчас тебе нужно рот иначе использовать."
        mom emo-72 "..."
    if mom_path >= 11:
        mom emo-62 "[pname_max[0]], раздевайся, сейчас мы тебе поможем."
        scene bg pgn_shopping_lade_family73
        k emo-102 "О, [pname_mom[7]]!?"
        mom emo-62 "Что? Я же люблю своего сына и должна помочь, не выходить же ему отсюда с эрекцией."
        m emo-5 "{i}Ух ты! Мама приняла на себя инициативу. Мама, я тебя тоже очень люблю...{/i}"
label pgn_shopping_lade_momkira_bj:
    scene animated pgn_shopping_lade_momkira_bj
    $ renpy.pause()
    if pgnach_108.aopen == False:
        $ PGN_Achadd(pgnach_108, 108)
    m emo-7 "{i}Даже и не знаю, это и минетом особо не назвать. Словно они мне мастурбируют, но губами, а не руками.{/i}"
    m emo-10 "{i}Как же это круто. Ещё бы сюда кого-нибудь третьей...{/i}"
    $ menu_hbox = True
    menu:
        "Кончить в Маму":
            scene bg pgn_shopping_lade_family81
        "Кончить в Тётю":
            scene bg pgn_shopping_lade_family80
    m emo-12 "Аргх... Аааахх.... Да..."
    scene bg pgn_shopping_lade_family82
    k emo-101 "Так, [pname_max[0]], надевай штаны, и жди нас у кассы. Нам с твоей Мамой нужно ещё немного времени и будем одеваться."
    m emo-3 "Хорошо."
    if pgn_ach_repeat == 108:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 0, 0, 1, 0, 0)
    $ PGN_Addstatsex(stat_kira, 0, 0, 1, 0, 0)
    jump pgn_shopping_lade_cash

label pgn_shopping_lade_cash:
    if ("lade_buy_alice") in ivent24 or ("lade_buy_liza") in ivent24 or ("lade_buy_alice_and_liza") in ivent24:
        scene bg pgn_shopping_lade_family86
        mom emo-60 "Ну что, девочки, что-нибудь себе присмотрели?"
        if ("lade_buy_alice") in ivent24:
            a emo-22 "Мам, я дома тебе покажу. И [pname_max[0]] пообещал мне, что сам оплатит мои покупки."
            mom emo-62 "Да? Какой молодец."
            l emo-40 "А у меня в этот раз ничего."
            mom emo-62 "Не переживай, мы обязательно ещё сюда приедем."
        if ("lade_buy_liza") in ivent24:
            l emo-41 "Мама, я нашла такое красивое бельё."
            mom emo-62 "Надеюсь ты мне покажешь?"
            l emo-41 "Ммм... Да."
            l emo-41 "И [pname_max[0]]..."
            m emo-13 "Да, да, я куплю."
        if ("lade_buy_alice_and_liza") in ivent24:
            l emo-41 "Присмотрели себе пару комплектов. И [pname_max[0]], сказал, что сам заплатит."
            m emo-13 "{i}Куда же деваться, придётся потратиться.{/i}"
        scene bg pgn_shopping_lade_family83
        $ label_random = renpy.random.randint ( 1, 2)
        if label_random == 1:
            other emo-989 "Здравствуйте. Надеюсь вы не себе бельё подбирали?"
            m emo-13 "Нет, конечно нет."
        if label_random == 2:
            other emo-989 "Здравствуйте. Хороший выбор."
        scene bg pgn_shopping_lade_family85
        if ("lade_buy_alice") in ivent24 or ("lade_buy_liza") in ivent24:
            $ shopping_pay = renpy.random.randint ( 100, 600)
        if ("lade_buy_alice_and_liza") in ivent24:
            $ shopping_pay = renpy.random.randint ( 300, 1000)
        other emo-989 "Хорошо. С вас $[shopping_pay]."
        play sound "content/audio/long_expected.mp3" noloop
        $ renpy.notify(str(task_notifi[11])+" $"+str(shopping_pay))
        $ bill_LaDE += shopping_pay
        $ currency -= shopping_pay
    else:
        scene bg pgn_shopping_lade_family84
        other emo-989 "Здравствуйте. Спасибо за покупки. Приходите к нам ещё."
    $ qtime += 3
    scene bg pgn_carmom_allch_02
    $ renpy.pause(3, hard=True)
    jump loc_pool






label pgn_pbowl_lizaoliv_01:
    $ liza_path = 36
    l emo-50 "Ой, чуть не забыла. Оливия."
    ol emo-141 "А, точно. [pname_max[0]], ты не хотел бы сходить с нами в это воскресение в ТРЦ?"
    m emo-0 "Я не против. А что там будем делать?"
    ol emo-141 "Поиграем в боулинг."
    m emo-3 "Хорошо. Тогда в это воскресение. Только, где будем встречаться?"
    ol emo-140 "Хм..."
    l emo-41 "Почему бы просто не встретится около входа в боулинг?"
    ol emo-141 "Тогда там и встретимся."
    m emo-0 "Ок."
    l emo-44 "[pname_max[0]], только не забудь за мной зайти после завтрака."
    m emo-13 "Постараюсь не забыть."
    l emo-41 "Тогда всё."
jump myroom_olivia_night_3some_end


label pgn_pbowl_lizaoliv_02:
    scene bg myroom_liza_change_school_02
    l emo-41 "А, [pname_max[0]]! Молодец, что не забыл. Давай одевайся и поедем."
    scene bg myroom_liza_change_school_03
    l emo-40 "..."
    l emo-40 "Ты будешь одеваться или как?"
    m emo-3 "Я быстро оденусь, а пока посмотрю на тебя."
    scene bg myroom_liza_change_school_04
    l emo-41 "Хорошо. Но если у тебя встанет, то помогать не буду."
    m emo-3 "Хорошо, хорошо, одеваюсь."
    $ PGN_Moveement_events (2, 11)
    jump pgn_pbowl_lizaoliv_03


label pgn_pbowl_lizaoliv_03:
    scene bg pgn_pbowl_vsliazaandoliv_01
    ol emo-141 "Привет ребята!"
    l emo-41 "Привет, Оливия. Ты долго нас ждала?"
    ol emo-141 "Нет, сама только недавно приехала."
    l emo-42 "Ты в платье, а что мне не сказала, я может быть тоже что-нибудь надела."
    m emo-6 "У тебя есть платье?"
    l emo-40 "Не помню, а даже если и нет, то у меня теперь есть деньги, чтобы самой купить."
    ol emo-141 "Ну что, пойдём?"
    m emo-3 "Да."
    scene bg pgn_pbowl_vsliazaandoliv_02
    m emo-4 "{i}Вот они, две мои девушки, мои сексуальные попки. И пока могу трахнуть одну только в попку, другую только в киску...{/i}"
    m emo-6 "{i}Особо ничего не видно. Интересно, Оливия без трусиков или нет. Сестренка точно, она давно их не носит.{/i}"
    m emo-0 "{i}Всё, хватит об этом думать, здесь мы чтобы отдохнуть, как нормальные люди{/i}"
    scene bg pgn_mall_pbowl_02
    other emo-997 "Здравствуйте. Добро пожаловать в \"pBowl\". На сколько человек и часов берете дорожку?"
    scene bg pgn_pbowl_vsliazaandoliv_03
    m emo-13 "Эм..."
    m emo-0 "{i}Понятно, значит я должен платить за всех. Эх...{/i}"
    scene bg pgn_mall_pbowl_02
    m emo-0 "Здравствуйте. На один час, три человека."
    other emo-997 "С вас $60."
    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[11])+" $"+"60")
    $ currency -= 60
    scene bg pgn_pbowl_vsliazaandoliv_04
    m emo-0 "Так, дорожку оплатил на час и вот ваша обувь."
    l emo-41 "[pname_max[7]]! [pname_max[6]]! Будь хорошим мальчиком."
    ol emo-141 "Да. Купи девушкам напитки. Купишь?"
    $ menu_hbox = False
    menu:
        "Конечно":
            scene bg pgn_mall_pbowl_03
            other emo-996 "Здравствуйте. Чего желаете?"
            m emo-0 "Мне два стакана сока."
            other emo-996 "Хорошо. С вас $12."
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"12")
            $ currency -= 12
            $ ivent24.append("pbowl_battle_lizaoliv_drink")
        "Нет":
            m emo-0 "Нет. Обломитесь."
            l emo-44 "Фууу, братик."
            m emo-0 "Я и так за вас оплатил игру. Если хочется пить, купите себе сами."
    scene bg pgn_pbowl_vsliazaandoliv_05
    l emo-41 "Итак, мы тут посовещались и предлагаем тебе соревнование. Ты играешь против нас. Если побеждаешь, то получаешь награду."
    m emo-3 "Против вас... Легко. И какая награда?"
    ol emo-141 "Что за награда... секрет."
    l emo-40 "А ты хотя бы играть умеешь?"
    m emo-4 "Да что там играть, просто кинуть шар и сбить все кегли."
    l emo-49 "Хм... Может?"
    ol emo-141 "..."
    l emo-40 "Тогда, давай так. Сейчас ты будешь играть против Оливии, один на один. Если победишь, то получишь небольшую награду, а в следующий раз против меня. А когда-нибудь потом сможешь посоревноваться против нас обеих."
    m emo-3 "А может я и сейчас смогу вас обыграть."
    l emo-40 "Кто знает."
    ol emo-141 "Ты первый."
    jump games_pbowl_oliv

label pgn_pbowl_lizaoliv_04:
    scene bg pgn_pbowl_rewards_toilet_01
    l emo-41 "[pname_max[0]], не отставай."
    scene black
    ol emo-141 "Давай, снимай штаны."
    l emo-41 "Ох! Бедненький, наверное давно уже стоит."
    ol emo-143 "Сейчас мы тебе поможем кончить."
label pgn_pbowl_lizaoliv_04_next:
    scene animated pgn_pbowl_rewards_toilet_hj
    if pgnach_105.aopen == False:
        $ PGN_Achadd(pgnach_105, 105)
    m emo-4 "Может ртом сделаете?"
    l emo-40 "Нет."
    l emo-49 "Аххх... Да... Ммм..."
    m emo-13 "[pname_liza[0]], ты специально так делаешь?"
    l emo-43 "Что я делаю?"
    m emo-13 "Как в порно. Дрочишь мне, а стонешь ты, словно тебе мастурбируют."
    l emo-43 "А так."
    l emo-50 "Аааахх... Аааххх, братик... глубже."
    ol emo-146 "Аааххх... Ммм... Ах... Не останавливайся... Аааххх..."
    m emo-10 "Девчонки... Ах вы... Я... Чёрт..."
    $ menu_hbox = True
    menu:
        "Кончить в [pname_liza[3]]":
            jump pgn_pbowl_lizaoliv_04_liza
        "Кончить в Оливию":
            jump pgn_pbowl_lizaoliv_04_oliv

label pgn_pbowl_lizaoliv_04_liza:
    scene bg pgn_pbowl_rewards_toilet_hj_07
    m emo-7 "Ааахх... Ааа... А..."
    scene bg pgn_pbowl_rewards_toilet_hj_09
    ol emo-142 "Ого, как много."
    l emo-48 "Ееее поогроиа..."
    ol emo-144 "Из твоего рта сейчас всё выльется."
    jump pgn_pbowl_lizaoliv_04_end

label pgn_pbowl_lizaoliv_04_oliv:
    scene bg pgn_pbowl_rewards_toilet_hj_08
    m emo-7 "Ааахх... Ааа... А..."
    scene bg pgn_pbowl_rewards_toilet_hj_10
    l emo-42 "Оливия, я тоже хочу. Мне оставь немного..."

label pgn_pbowl_lizaoliv_04_end:
    scene bg pgn_pbowl_rewards_toilet_hj_11
    m emo-3 "Ого!"
    scene bg pgn_pbowl_rewards_toilet_02
    if liza_path == 38:
        $ liza_path = 39
        l emo-41 "[pname_max[0]], как тебе наша награда?"
        m emo-3 "Спасибо. Но всё же ртом было бы лучше."
        ol emo-141 "Тогда тебе нужно победить нас обеих."
    else:
        m emo-4 "Если вам обеим нехватает, то давайте ещё, у меня много."
        l emo-41 "Ну, нет, а если хочешь ещё и больше, то нужно снова с нами поиграть и победить."
    m emo-0 "Ну ладно"
    l emo-41 "Увидимся дома."
    ol emo-142 "Пока."
    if pgn_ach_repeat == 105:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_liza, 0, 0, 0, 0, 1)
    $ PGN_Addstatsex(stat_olivia, 0, 0, 0, 0, 1)
    $ qtime += 2
    jump loc_mall_pbowl

label pgn_pbowl_lizaoliv_05:
    scene bg pgn_pbowl_rewards_toilet_01
    l emo-41 "Пойдём, только не отставай."
    m emo-3 "Я хочу получить своё, так что от вас не отстану."
    scene bg pgn_pbowl_rewards_toilet_03
    if pgnach_106.aopen == False:
        $ PGN_Achadd(pgnach_106, 106)
    ol emo-142 "Выбирай, с кого начнёшь. С анала [pname_liza[1]] или с моей киски."
    if condom.numbsuse == 0:
        m emo-13 "Вот только у меня презервативы закончились."
        ol emo-142 "Не переживай, у меня есть."
        m emo-3 "Тогда отлично."
    $ menu_hbox = True
    menu:
        "[pname_liza[0]]":
            jump pgn_pbowl_lizaoliv_05_liza
        "Оливия":
            jump pgn_pbowl_lizaoliv_05_oliv

label pgn_pbowl_lizaoliv_05_liza:
    scene animated pgn_pbowl_rewards_toilet_sex_liza_anal
    m emo-4 "{i}Оливия время даром не теряет. Смотрит, как я трахаю сестренку и заодно мастурбирует.{/i}"
    l emo-50 "Аааххх... Братик... Аххх... Ммм..."
    m emo-16 "{i}Вот бы их обеих и в одну и туже дырочку. Но увы, они мне дадут этого сделать.{/i}"
    ol emo-146 "[pname_max[0]], не останавливайся, продолжай. Ух! Я скоро кончу... В живую смотреть куда лучше, чем порно..."
    m emo-7 "Я больше не могу... сейчас..."
    scene bg pgn_pbowl_rewards_toilet_sex_liza_03
    $ renpy.pause(1)
    scene bg pgn_pbowl_rewards_toilet_sex_liza_06
    $ renpy.pause(1)
    scene bg pgn_pbowl_rewards_toilet_sex_liza_03
    $ renpy.pause(1)
    scene bg pgn_pbowl_rewards_toilet_sex_liza_06
    ol emo-147 "..."
    m emo-12 "Аааххх... Ааааргх..."
    if pgn_ach_repeat == 0:
        $ PGN_Addstatsex(stat_liza, 1, 0, 0, 0, 0)
    jump pgn_pbowl_lizaoliv_05_end

label pgn_pbowl_lizaoliv_05_oliv:
    scene animated pgn_pbowl_rewards_toilet_sex_oliv_vag
    m emo-4 "{i}Охренеть! Оливия так глубоко насаживается, что с каждым толчком чувствую её матку.{/i}"
    m emo-3 "{i}Интересно, о чём сейчас думает моя сестрёнка. Надеюсь о том, как ей тоже хочется в киску.{/i}"
    l emo-49 "{i}Моя попка зудит, мне нужен этот член... Член братика...{/i}"
    ol emo-147 "Аааххх.. Да... Да... Ммм... Аааххх..."
    ol emo-147 "Почти... уже почти... ещё чуть-чуть..."
    scene bg pgn_pbowl_rewards_toilet_sex_oliv_04
    $ renpy.pause(1)
    scene bg pgn_pbowl_rewards_toilet_sex_oliv_06
    $ renpy.pause(1)
    scene bg pgn_pbowl_rewards_toilet_sex_oliv_04
    $ renpy.pause(1)
    scene bg pgn_pbowl_rewards_toilet_sex_oliv_06
    ol emo-146 "Аааахххх..."
    m emo-12 "Я тоже... Кончаююююю... Аргхх..."
    if pgn_ach_repeat == 0:
        $ PGN_Addstatsex(stat_olivia, 0, 0, 0, 1, 0)
    jump pgn_pbowl_lizaoliv_05_end

label pgn_pbowl_lizaoliv_05_end:
    scene bg pgn_pbowl_rewards_toilet_02
    m emo-4 "У меня ещё достаточно сил на вас обеих."
    l emo-41 "Ну, нет, а если хочешь ещё и больше, то нужно снова с нами поиграть и победить."
    m emo-0 "Ну ладно"
    l emo-41 "Увидимся дома."
    ol emo-142 "Пока."
    if pgn_ach_repeat == 106:
        jump table_pgn_achievement
    $ qtime += 2
    jump loc_mall_pbowl

label pgn_pbowl_lizaoliv_06:
    scene bg pgn_pbowl_rewards_toilet_01
    l emo-41 "Пойдём, только не отставай."
    scene bg pgn_pbowl_rewards_toilet_02
    l emo-41 "Выбирай, победитель, чего хочешь."
    $ menu_hbox = False
    menu:
        "Мастурбация":
            jump pgn_pbowl_lizaoliv_04_next
        "Секс с [pname_liza[4]]":
            jump pgn_pbowl_lizaoliv_05_liza
        "Секс с Оливией":
            jump pgn_pbowl_lizaoliv_05_oliv

label pgn_pbowl_lizaoliv_07:
    scene bg pgn_pbowl_vsliazaandoliv_03
    m emo-13 "{i}Ок. Девочки уже здесь. И мне значит снова за них платить.{/i}"
    scene bg pgn_mall_pbowl_02
    other emo-997 "Здравствуйте. Добро пожаловать в \"pBowl\". На сколько человек и часов берете дорожку?"
    m emo-0 "Здравствуйте. На один час, три человека."
    if daysn != 6 or daysn != 7:
        other emo-997 "С вас $35."
        play sound "content/audio/long_expected.mp3" noloop
        $ renpy.notify(str(task_notifi[11])+" $"+"35")
        $ currency -= 35
    if daysn == 6 or daysn == 7:
        other emo-997 "С вас $60."
        play sound "content/audio/long_expected.mp3" noloop
        $ renpy.notify(str(task_notifi[11])+" $"+"60")
        $ currency -= 60
    scene bg pgn_pbowl_vsliazaandoliv_04
    m emo-0 "Так, дорожку оплатил на час и вот ваша обувь."
    l emo-41 "[pname_max[7]]! [pname_max[6]]! Будь хорошим мальчиком."
    ol emo-141 "Да. Купи девушкам напитки. Купишь?"
    $ menu_hbox = False
    menu:
        "Конечно":
            scene bg pgn_mall_pbowl_03
            other emo-996 "Здравствуйте. Чего желаете?"
            m emo-0 "Мне два стакана сока."
            other emo-996 "Хорошо. С вас $12."
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"12")
            $ currency -= 12
            $ ivent24.append("pbowl_battle_lizaoliv_drink")
        "Нет":
            m emo-0 "Нет. Обломитесь."
            l emo-44 "Фууу, братик."
            m emo-0 "Я и так за вас оплатил игру. Если хочется пить, купите себе сами."
    scene bg pgn_pbowl_vsliazaandoliv_05
    if liza_path < 40:
        l emo-41 "Ну что ж, продолжим. И против кого ты там сейчас должен играть?"
        if liza_path == 39:
            l emo-41 "Точно, против нас обеих. Удачи тебе."
            jump games_pbowl_liza_and_oliv
        if liza_path == 38:
            l emo-41 "А точно, против меня. Я не дам тебе меня победить."
            jump games_pbowl_liza
        if liza_path == 37:
            ol emo-142 "Против меня."
            l emo-42 "Не подведи меня, а то сильно обижусь."
            ol emo-144 "Постараюсь."
            jump games_pbowl_oliv
    if liza_path >= 40:
        l emo-41 "Раз ты нас победил, то будешь снова играть против нас обеих."
        m emo-4 "Тогда начнём, готовьте свои попки."
        jump games_pbowl_liza_and_oliv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
