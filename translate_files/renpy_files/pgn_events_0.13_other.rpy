label pgn_events_13_erikwhere:
    scene black
    menu:
        "Вы играли в оригинальную игру \"Большой Брат\" (Unity)?"
        "Да, играл":
            menu:
                "Что вы сделали с Эриком?"
                "Сдал его мафии":
                    $ accessiv.append("erik_mob")
                "Избавился с помощью Мамы Кати":
                    $ accessiv.append("erik_momkate")
        "Нет (А что это за игра?)":
            $ label_random = renpy.random.choice(["erik_mob", "erik_momkate"])
            $ accessiv.append(str(label_random))
    return


label pgn_events_13_newporn:
    scene bg pool_kira_swimming
    k emo-101 "[pname_max[0]], после клиники чувствуешь себя хорошо?"
    m emo-3 "Отлично."
    k emo-101 "Хорошо."
    k emo-100 "Студия попросила меня поговорить с вами об участии в одной сценке."
    m emo-13 "Опять учить диалоги..."
    k emo-100 "Ничего учить не придётся."
    a emo-20 "Т.е. это не как обычно, от нас требуется только секс?"
    k emo-103 "Совершенно верно. И... в основном только анальный."
    m emo-4 "Класс!"
    a emo-23 "Легко тебе говорить, тебе просто всунуть и кончить, а мне после ещё этим местом сидеть придётся."
    k emo-101 "И нужна ещё актриса. Есть идеи?"
    menu menu_pgn_events_13_newporn:
        "[pname_liza[0]]":
            k emo-100 "Нет, не подойдёт. Тут нужен кто-нибудь взрослый."
            jump menu_pgn_events_13_newporn
        "Мама":
            k emo-103 "От неё потребуется участие с тобой в другом проекте, так что её попку нужно пока поберечь."
            jump menu_pgn_events_13_newporn
        "Ты, тётя":
            k emo-114 "Ты действительно, хочешь, чтобы это была я?"
            m emo-13 "{i}А у меня был выбор?{/i}"
            k emo-114 "Я благодарна тебе. Хорошо, тогда я вас жду в пятницу в 18:00 в гримёрной."
            a emo-28 "Блин! А в другой день или время нельзя? В этот же день поход в клуб."
            m emo-4 "Ха-ха, обломалась."
            a emo-27 "Иди ты."
            k emo-108 "Если [pname_max[0]] справится быстро, успеем подготовиться и сходим в клуб."
            m emo-3 "И меня возьмёте?"
            a emo-20 "Нет"
            k emo-100 "Нет"
            k emo-101 "Ну всё, я вам сообщила. Буду ждать. И, [pname_alice[0]], вот тебе флешка, посмотри, к чему нужно подготовиться."
    $ pornstudio_path = 9
    jump loc_pool









label pgn_bonus_home_vengeancealice_00:
    m emo-13 "{i}Блин! [pname_alice[0]]! Мои шорты в сперме, мне нужно срочно в ванну.{/i}"
    return



label pgn_bonus_home_vengeancealice_shower:
    $ ivent24.remove("punishmax_shortscum")
    m emo-13 "Я пил молоко и нечаянно облился."
    mom emo-73 "А, ясно..."
    m emo-0 "Я быстро, мешать не буду."
    scene e-mom-bath-undress5-1
    $ renpy.pause(5, hard=True)
    if liza_path == 44 and alice_path == 22 and "bonusev_venalice_1" not in accessiv:
        jump pgn_bonus_home_vengeancealice_01
    jump loc_my_room



label pgn_bonus_home_vengeancealice_01:
    $ accessiv.append("bonusev_venalice_1")
    scene pgn_bonus_vengeancealice_01
    l emo-41 "[pname_max[0]], а почему ты голый? Ждал меня?"
    m emo-8 "Из-за кое-кого мне пришлось идти в ванную."
    m emo-0 "Пытаюсь найти свои запасные шорты."
    l emo-41 "Внизу смотрел?"
    m emo-0 "А точно! Ты лучше знаешь, где что лежит, чем я."
    scene pgn_bonus_vengeancealice_02
    m emo-8 "Блин! [pname_alice[0]] вообще не знает меры. Как она вообще до такого додумалась?!"
    l emo-46 "И моя попка болит сильно от её шлепаний."
    scene pgn_bonus_vengeancealice_03
    l emo-43 "А давай мы ей отомстим!"
    m emo-6 "Что ты предлагаешь? "
    m emo-6 "Ааа! Может я Маме расскажу, что она всё ещё занимается своим блогом?"
    l emo-49 "Хм... мне кажется после этого она вообще не будет с тобой разговаривать."
    m emo-13 "Наверное."
    l emo-41 "У меня есть одна идея. Я буду в комнате с [pname_alice[4]], а тебе нужно будет только прийти к нам..."
    m emo-1 "И когда?"
    if daysn == 2 or daysn == 4 or daysn == 7:
        $ ivent24.append("bonusev_venalice_night")
        l emo-41 "Можно сегодня ночью. Примерно к 02:00 подходи."
    else:
        l emo-40 "Сегодня не получится. Приходи ночью, когда [pname_alice[0]] будет дома и Кати не будет, подойди."
    m emo-0 "Хорошо. Приду."
    $ qtime += 1
    jump loc_my_room



label pgn_bonus_home_vengeancealice_spy:
    if qtime == 1:
        scene pgn_bonus_vengeancealice_04_vezdessushij
        if ("bonusev_venalice_2") not in accessiv:
            m emo-0 "{i}Они просто сидят вместе и разговаривают. Ни единой мысли, что задумала [pname_liza[0]].{/i}"
        else:
            $ renpy.pause()
        scene pgn_bonus_vengeancealice_05_vezdessushij with dissolve
        if ("bonusev_venalice_2") not in accessiv:
            m emo-13 "{i}И долго мне ждать?{/i}"
        else:
            $ renpy.pause()
        scene pgn_bonus_vengeancealice_06_vezdessushij with dissolve
        if ("bonusev_venalice_2") not in accessiv:
            m emo-8 "{i}Блин! Они уснули.{/i}"
            menu:
                "уйти":
                    $ ivent24.append("bonusev_venalice_night_pass")
                    $ ivent24.remove("bonusev_venalice_night")
                    $ qtime += 1
                    jump loc_my_room
                "Остаться":
                    if ("bonusev_venalice_2") not in accessiv:
                        m emo-0 "{i}Не знаю, чего я жду.{/i}"
                    else:
                        $ renpy.pause()
        else:
            $ renpy.pause()
    scene pgn_bonus_vengeancealice_07_vezdessushij
    if ("bonusev_venalice_2") not in accessiv:
        m emo-6 "{i}Похоже это знак.{/i}"
    else:
        m emo-3 "{i}Я пришёл вовремя.{/i}"
    jump pgn_bonus_home_vengeancealice_sex



label pgn_bonus_home_vengeancealice_sex:
    scene pgn_bonus_vengeancealice_08_vezdessushij
    l emo-43 "Ну что, готов развлечься? [pname_alice[0]] уже готова.\n\n{color=#ccc}Сцена сделана в благодарность Vezdessushij, за помощь с рендером сцен.{/color}"
    if ("bonusev_venalice_2") not in accessiv and pgn_ach_repeat == 0:
        m emo-6 "Но она спит. А почему говорим не шопотом?"
        l emo-40 "Смотри."
        scene pgn_bonus_vengeancealice_09_vezdessushij
        l emo-41 "[pname_alice[0]]! Просыпайся! [pname_max[0]] пришёл заделывать тебе ребенка."
        m emo-8 "[pname_liza[0]]..."
        l emo-43 "Просыпайся! [pname_max[0]] нюхает твои труски!"
        m emo-0 "Я не..."
        scene pgn_bonus_vengeancealice_10_vezdessushij
        l emo-43 "Она спит крепким сном и её ни как сейчас не разбудить."
        m emo-6 "А как?"
        l emo-41 "Снотворное, которое давали Маме."
        m emo-0 "Ясно."
        m emo-6 "{i}Где она его взяла, купила? Не буду спрашивать, а то вдруг у неё много, да и ещё мне подсыпет.{/i}"
    scene pgn_bonus_vengeancealice_11_vezdessushij
    $ PGN_Achadd(pgnach_176, 176)
    l emo-43 "Решай. Что будем с ней делать."
    menu pgn_bonus_home_vengeancealice_sex_m:
        "А она не узнает?" if ("bonusev_venalice_2") not in accessiv and ("bonusev_venalice_night_q1") not in ivent24 and pgn_ach_repeat == 0:
            $ ivent24.append("bonusev_venalice_night_q1")
            m emo-8 "А она не знает, что я здесь был?"
            l emo-44 "Если не будешь кончать своей спермой из стороны в сторону, то не узнает."
            m emo-6 "А если, трахну её, то не узнает?"
            l emo-40 "Я ей скажу, что перед сном мы немного поразвлеклись с игрушками."
            jump pgn_bonus_home_vengeancealice_sex_m
        "А как мы это используем, для мести?" if ("bonusev_venalice_2") not in accessiv and ("bonusev_venalice_night_q2") not in ivent24 and pgn_ach_repeat == 0:
            $ ivent24.append("bonusev_venalice_night_q2")
            m emo-6 "А как она узнает, что мы отомстили ей за всё, что она с нами сделала?"
            l emo-40 "Она и не узнает."
            m emo-13 "А зачем тогда это всё?"
            l emo-40 "Ну, хотя бы так мы можем что-то с ней сделать и нам за это ни чего не будет. Но у неё всё равно есть то, от чего тебе будет плохо, если узнает Мама."
            m emo-3 "Может удалим всё с её телефона, пока она спит?"
            l emo-46 "Ты знаешь пароль от её телефона?"
            m emo-0 "Блин! Точно."
            l emo-41 "Пока это всё что мы можем сделать. Так что давай, предлагай, что с ней сделаем, какие извращения и пошлости."
            l emo-41 "Но несколько фотографий я всё же сделаю."
            jump pgn_bonus_home_vengeancealice_sex_m
        "Анал" if ("bonusev_venalice_2") in accessiv or ("bonusev_venalice_night_q2") in ivent24 or pgn_ach_repeat == 176:
            if ("bonusev_venalice_2") not in accessiv:
                l emo-40 "Презервативы взял?"
                m emo-13 "А эм... ну..."
                l emo-41 "Они не нужны. [pname_alice[0]] рассказала, что как только ей начал нравится анальный секс с тобой, её попка всегда наготове."
            scene pgn_bonus_vengeancealice_12_vezdessushij
            l emo-46 "Я ей немного завидую..."
            m emo-6 "Чем?"
            scene pgn_bonus_vengeancealice_13_vezdessushij
            l emo-43 "Давай, вставляй в её попку свой большущий член."
            if ("bonusev_venalice_2") not in accessiv:
                m emo-13 "А она точно не проснётся?"
                l emo-48 "А ты вставь и узнаем."
            scene pgn_bonus_vengeancealice_14
            a emo-20 "Мммхмм... "
            m emo-9 "Эээ..."
            l emo-41 "Спит она, спит. Продолжай и давай глубже. Тебе хочется сейчас её отыметь?"
            m emo-13 "Да и от куда ты такие слова знаешь и вообще как идея такая в голову пришла?"
            l emo-44 "[pname_max[0]]. Меньше слов, больше дела. Я тоже хочу спать."
            m emo-13 "Хорошо, хорошо."
            scene pgn_bonus_vengeancealice_15
            l emo-49 "Да, братик, глубже. Накажи её попку. Жёстче и глубже."
            scene pgn_bonus_vengeancealice_16
            l emo-41 "Братик, тебе нравится быть внутри её попки?"
            m emo-3 "Да."
            scene pgn_bonus_vengeancealice_17
            $ renpy.pause()
            scene pgn_bonus_vengeancealice_18
            l emo-41 "Продолжай."
            scene pgn_bonus_vengeancealice_19
            m emo-10 "Блин! [pname_liza[0]], я сейчас кончу."
            l emo-43 "Вынимай быстрее и кончай мне в ротик."
            scene pgn_bonus_vengeancealice_20
            m emo-12 "Аргххх!!! Аааа..."
            scene pgn_bonus_vengeancealice_21
            m emo-7 "{i}Сестрёнка без остановки глотает.{/i}"
            scene pgn_bonus_vengeancealice_22
            if ("bonusev_venalice_2") not in accessiv:
                l emo-41 "Понравилось?"
                m emo-4 "Ага."
                l emo-43 "Захочешь ещё, скажи мне. А теперь пойдём, я хочу спать."
            else:
                m emo-4 "У тебя на губах немного осталось."
                l emo-48 "..."
            if pgn_ach_repeat != 0:
                jump table_pgn_achievement
            $ PGN_Addstatsex(stat_alice, 1, 0, 0, 0, 0)
        "Минет" if ("bonusev_venalice_2") in accessiv or ("bonusev_venalice_night_q2") in ivent24 or pgn_ach_repeat == 176:
            l emo-44 "Хорошо. Только не кончи ей в рот, а то она всё поймёт."
            l emo-40 "А как ты это сделаешь, она же не может ничего?"
            m emo-0 "Как-нибудь."
            scene pgn_bonus_vengeancealice_23
            l emo-41 "Ты её тащешь, как куклу. Интересно на это смотреть."
            scene pgn_bonus_vengeancealice_24
            m emo-6 "Нужно только открыть её рот, а дальше дело техники."
            scene pgn_bonus_vengeancealice_25
            $ renpy.pause()
            scene pgn_bonus_vengeancealice_26
            l emo-46 "Не переборщи."
            m emo-3 "Всё под контролем."
            scene pgn_bonus_vengeancealice_27
            a emo-22 "Ммм... Мм ..."
            m emo-9 "Ого! Двигает языком."
            l emo-44 "Вот же. Ей снится эротический сон. Хм... может..."
            scene pgn_bonus_vengeancealice_28
            m emo-10 "Ох, чёрт! Ох.... Блин... Ааа!"
            l emo-46 "Ты в неё кончил?"
            m emo-4 "Нет, но скоро. Она активнее стала лизать."
            scene pgn_bonus_vengeancealice_29
            m emo-10 "[pname_liza[0]], я почти...."
            scene pgn_bonus_vengeancealice_30
            m emo-12 "Ааааа..."
            scene pgn_bonus_vengeancealice_31
            if ("bonusev_venalice_2") not in accessiv:
                l emo-41 "Понравилось?"
                m emo-4 "Ага."
                l emo-43 "Захочешь ещё, скажи мне. А теперь пойдём, я хочу спать."
            else:
                m emo-4 "Спасибо."
                l emo-41 "Пойдём спать."
            if pgn_ach_repeat != 0:
                jump table_pgn_achievement
            $ PGN_Addstatsex(stat_alice, 0, 0, 1, 0, 0)
        "Вагинал" if ("bonusev_venalice_2") in accessiv or ("bonusev_venalice_night_q2") in ivent24 or pgn_ach_repeat == 176:
            l emo-48 "Всё же решил заделать ребеночка."
            m emo-13 "Эм... нет, нет..."
            l emo-44 "Ну, ну, кто тебя знает."
            m emo-6 "{i}Да что это с [pname_liza[4]] происходит. Может Мама была права, что мы влияем на неё плохо.{/i}"
            scene pgn_bonus_vengeancealice_32
            l emo-41 "[pname_max[0]]! Давай, войди в неё."
            m emo-6 "А может мне сходить за смазкой или..."
            l emo-43 "Входи в её киску, уверена, там и так всё нормально."
            m emo-0 "Ладно."
            scene pgn_bonus_vengeancealice_33
            m emo-6 "{i}Как же в её киске узко.{/i}"
            scene pgn_bonus_vengeancealice_34
            l emo-43 "Ну как тебе?"
            m emo-6 "Сначала было сложно войти, а сейчас получше, что ли. Словно её тело понимает, что её трахают."
            scene pgn_bonus_vengeancealice_35
            m emo-10 "Её киска не отпускает мой член, затягивает и затягивает внутрь."
            l emo-40 "Поддержи её ноги, я хочу кое-что сделать."
            scene pgn_bonus_vengeancealice_36
            if ("bonusev_venalice_2") not in accessiv:
                m emo-6 "Что ты хочешь сделать?"
            l emo-49 "Не тебе же одному развлекаться, я тоже кое-чего хочу."
            scene pgn_bonus_vengeancealice_37
            l emo-48 "Поцелуй в попку."
            scene pgn_bonus_vengeancealice_38
            l emo-49 "Я чувствую попкой её горячее дыхание и нежные губки сестрёнки."
            m emo-9 "{i}Что она вытворяет. Офигеть.{/i}"
            scene pgn_bonus_vengeancealice_39
            l emo-41 "Губки большие, губки маленькие, губки влажные, ротик горячий."
            m emo-10 "[pname_liza[0]]... Я..."
            l emo-48 "Быстрее вытаскивай, у меня есть идея."
            scene pgn_bonus_vengeancealice_40
            m emo-4 "Ха... классно!"
            scene pgn_bonus_vengeancealice_41
            m emo-3 "Губы влажные... Сестренка принимай!"
            scene pgn_bonus_vengeancealice_42
            m emo-12 "Аргххх!!! Аааах..."
            scene pgn_bonus_vengeancealice_43
            m emo-4 "{i}Моя любимая младшая сестренка, обожает мою сперму. Моя маленькая спермоедка.{/i}"
            scene pgn_bonus_vengeancealice_44
            if ("bonusev_venalice_2") not in accessiv:
                l emo-41 "Понравилось?"
                m emo-4 "Ага."
                l emo-43 "Захочешь ещё, скажи мне. А теперь пойдём, я хочу спать."
            else:
                m emo-4 "Спасибо."
                l emo-41 "Пойдём спать."
            if pgn_ach_repeat != 0:
                jump table_pgn_achievement
            $ PGN_Addstatsex(stat_alice, 0, 0, 0, 1, 0)
    if ("bonusev_venalice_2") not in accessiv:
        $ accessiv.append("bonusev_venalice_2")
    $ qtime, liza_sex_bj, sexsleep_alice = 3, 4, 4
    jump loc_my_room_sleep



label pgn_bonus_home_vengeancealice_repeat:
    m emo-4 "Сегодня ещё раз займёмся сексом со спящей [pname_alice[4]]?"
    if sexsleep_alice > 0:
        l emo-46 "Нет. Мало времени прошло. Если будем часто это делать, то она может догадаться."
        m emo-6 "Да, точно, я не подумал."
    elif daysn == 5:
        l emo-40 "Сегодня же пятница. Она будет в клубе."
        m emo-0 "Блин, точно! Уже забыл какой день недели."
    elif daysn == 1 or daysn == 3 or daysn == 6:
        l emo-40 "Не получится. Катя сегодня у нас ночует."
        m emo-0 "Забыл"
    else:
        $ ivent24.append("bonusev_venalice_night")
        l emo-41 "Понравилось?"
        l emo-43 "Хорошо. Я это сделаю. Только не забудь."
    jump jump_dialogue



label pgn_bonus_home_vengeancekira_livroom:
    m emo-6 "{i}Хм...{/i}"
    m emo-6 "{i}А может попробовать сделать тоже самое с [pname_kira[4]], что и с [pname_alice[4]], когда [pname_liza[0]] подсыпала ей снотворного.{/i}"
    m emo-13 "{i}Ночью сексом занимается со всякими людьми и ещё от-то всех это скрывает.{/i}"
    $ accessiv.append("bonusev_venkira_0")
    return


label pgn_bonus_home_vengeancekira_01:
    m emo-3 "[pname_liza[0]], а давай так же как с [pname_alice[4]], провернём с Тётей [pname_kira[4]]."
    l emo-40 "А что тебе Тётя сделала?"
    m emo-13 "Есть за что."
    l emo-46 "А за что именно, расскажешь?"
    menu:
        "Рассказать":
            m emo-0 "Она в Клубе занимается сексом с разными людьми и так каждую ночь."
            l emo-40 "Но Тётя не твоя девушка и ты же знаешь, что она порно-звезда и сценарии пишет. Наверное это по работе."
            m emo-13 "Не знаю, но всё равно. Поможешь?"
        "Промолчать":
            m emo-0 "Так она постоянно спит голой в гостиной, это не хорошо. Все в одежде, а она голая и ей можно."
            l emo-44 "Ну как хочешь, не рассказывай."
    l emo-40 "А когда Тётя [pname_kira[0]] возвращается домой?"
    m emo-0 "В 3 часа."
    l emo-46 "Хм... слишком поздно."
    m emo-13 "Значит не получится?"
    l emo-40 "Перед сном, когда делаю уроки, напомни и я придумаю, как это сделать."
    m emo-3 "Хорошо. Спасибо."
    $ accessiv.append("bonusev_venkira_1")
    jump jump_dialogue


label pgn_bonus_home_vengeancekira_repeat:
    if ("bonusev_venkira_2") not in accessiv:
        $ accessiv.append("bonusev_venkira_2")
        m emo-0 "Ты просила напомнить."
        l emo-40 "О чём?"
        m emo-6 "Ну так, о Тёте [pname_kira[2]]. Чтобы она спала крепким сном, пока я буду ею заниматься."
        l emo-46 "Ты извращенец, братик. Хорошо, я это сделаю."
        l emo-40 "А презервативы у тебя есть? Я не смогу скрыть твоего присутствия, как с [pname_alice[4]]."
        if condom.have == True:
            m emo-3 "Конечно. Они у меня всегда с собой."
            l emo-40 "Я это сделаю, а ты главное не проспи. Проспишь и придётся ждать несколько дней."
            m emo-0 "Понял."
            $ accessiv.append("bonusev_venkira_morning")
        else:
            m emo-13 "Блин! У меня нет."
            l emo-40 "Тогда приходи ко мне с просьбой, когда будут презервативы."
            m emo-0 "Хорошо."
    else:
        m emo-0 "Подготовишь Тётю к утренней разминке дырочек?"
        if sexsleep_kira > 0:
            l emo-46 "Нет. Мало времени прошло. Если будем часто это делать, то она может догадаться."
            m emo-6 "Да, точно, я не подумал."
        else:
            l emo-40 "А презервативы есть?"
            if condom.have == False:
                m emo-0 "Блин! Забыл."
                l emo-40 "Тогда в другой раз, братик."
            else:
                l emo-43 "Хорошо. Я это сделаю. Только не проспи. А если проспишь, то тогда только как-нибудь в другой раз. Тётя не [pname_alice[0]]."
                m emo-0 "Понял."
                $ accessiv.append("bonusev_venkira_morning")
    jump jump_dialogue



label pgn_bonus_home_vengeancekira_sex:
    $ PGN_Achadd(pgnach_177, 177)
    if pgn_ach_repeat == 177:
        menu:
            "Вариант 1":
                jump pgn_bonus_home_vengeancekira_sex_v1
            "Вариант 2":
                jump pgn_bonus_home_vengeancekira_sex_v2
    if "bonusev_venkira_morning_pose_1_6" in ivent24 or "bonusev_venkira_morning_pose_1_7" in ivent24:
        label pgn_bonus_home_vengeancekira_sex_v1:
            scene pgn_bonus_vengeancekira_02
            m emo-6 "{i}Хм... места на диване мало и аккуратно мне ни как её не перевернуть..\n\n{color=#ccc}Сцена сделана в благодарность Vezdessushij, за помощь с рендером сцен.{/color}{/i}"
            menu:
                "Анал":
                    scene pgn_bonus_vengeancekira_03
                    m emo-4 "{i}Тётя крепко спит, можно войти поглубже.{/i}"
                    scene pgn_bonus_vengeancekira_04
                    m emo-3 "{i}Вошёл! Она даже не пошевелилась.{/i}"
                    scene pgn_bonus_vengeancekira_05
                    $ renpy.pause()
                    scene pgn_bonus_vengeancekira_06
                    m emo-4 "{i}Разработанный анал Тёти. Класс!{/i}"
                    scene pgn_bonus_vengeancekira_07
                    m emo-3 "{i}Трахаю как хочу и сколько хочу.{/i}"
                    m emo-13 "{i}Блин! Долго не могу.{/i}"
                    scene pgn_bonus_vengeancekira_08
                    m emo-12 "Аргххх!!! Аааах... Ааа..."
                    scene pgn_bonus_vengeancekira_09
                    $ renpy.pause()
                    if pgn_ach_repeat == 0:
                        $ PGN_Addstatsex(stat_kira, 1, 0, 0, 0, 0)
                "уйти" if pgn_ach_repeat == 0:
                    jump loc_living_room
    elif "bonusev_venkira_morning_pose_2_6" in ivent24 or "bonusev_venkira_morning_pose_2_7" in ivent24:
        label pgn_bonus_home_vengeancekira_sex_v2:
            scene pgn_bonus_vengeancekira_11
            m emo-4 "{i}Горячая, очень сексуальная и ничего неподозревающая Тётя. Сейчас он как кукла для секса, только живая..\n\n{color=#ccc}Сцена сделана в благодарность Vezdessushij, за помощь с рендером сцен.{/color}{/i}"
            m emo-3 "{i}Стоял бы и смотрел на неё вечность. Но я тут, чтобы трахнуть её.{/i}"
            scene pgn_bonus_vengeancekira_12
            menu:
                "Вагинал":
                    scene pgn_bonus_vengeancekira_13
                    $ renpy.pause()
                    scene pgn_bonus_vengeancekira_14
                    m emo-6 "{i}Тётя каждый день занимается сексом, но в её киске всё равно узко.{/i}"
                    m emo-4 "{i}Не знаю, что она делает и как, но круто.{/i}"
                    scene pgn_bonus_vengeancekira_15
                    m emo-4 "{i}Ты моя, тётя!{/i}"
                    scene pgn_bonus_vengeancekira_16
                    m emo-3 "{i}Хочу кое-что сделать, всё равно она не будет против.{/i}"
                    scene pgn_bonus_vengeancekira_17
                    $ renpy.pause()
                    scene pgn_bonus_vengeancekira_18
                    m emo-7 "{i}Поцелуйчики.{/i}"
                    scene pgn_bonus_vengeancekira_19
                    m emo-10 "Аргххх!!!"
                    if pgn_ach_repeat == 0:
                        $ PGN_Addstatsex(stat_kira, 0, 0, 0, 1, 0)
                "В рот":
                    m emo-3 "{i}Откроем ротик и засунем член.{/i}"
                    scene pgn_bonus_vengeancekira_20
                    m emo-4 "{i}Мне начинает нравится. Хочу засунуть глубже.{/i}"
                    scene pgn_bonus_vengeancekira_21
                    $ renpy.pause()
                    scene pgn_bonus_vengeancekira_22
                    m emo-7 "{i}О да! Класс!{/i}"
                    scene pgn_bonus_vengeancekira_23
                    m emo-6 "{i}Полноценного минета не получу, но ротик всё равно сексуальный.{/i}"
                    scene pgn_bonus_vengeancekira_24
                    m emo-10 "{i}Ох! Чёрт! Тётя, я кончаю!{/i}"
                    m emo-12 "Аргххх!!!"
                    if pgn_ach_repeat == 0:
                        $ PGN_Addstatsex(stat_kira, 0, 0, 1, 0, 0)
                "уйти" if pgn_ach_repeat == 0:
                    jump loc_living_room
            scene pgn_bonus_vengeancekira_25
            $ renpy.pause()
    if pgn_ach_repeat != 0:
        jump table_pgn_achievement
    $ condom.numbsuse -= 1
    if condom.numbsuse == 0:
        $ condom.have = False
    $ qtime += 1
    if qtime == 7:
        scene pgn_bonus_vengeancekira_26
        $ renpy.pause()
        scene pgn_bonus_vengeancekira_27
        $ renpy.pause()
    if qtime == 8:
        scene pgn_bonus_vengeancekira_28
        $ renpy.pause()
        scene pgn_bonus_vengeancekira_29
        $ renpy.pause()
    m emo-4 "{i}Дело сделано.{/i}"
    $ ivent24.append("bonusev_venkira_morning_true")
    jump loc_living_room








label pgn_livroom_max_watchtv:
    scene pgn_livroom_max_watchtv_0a
    m emo-6 "Чтобы мне посмотреть?"
    call pgn_livroom_max_watchtv_porn from _call_pgn_livroom_max_watchtv_porn
    menu:
        "Развлекательные каналы":
            scene pgn_livroom_max_watchtv_0b
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random == 1:
                m emo-6 "{i}Познавательно.{/i}"
            if label_random == 2:
                m emo-3 "Ха-ха-ха... смешно."
            if label_random == 3:
                m emo-1 "..."
        "Порно-канал":
            $ label_random = renpy.random.randint ( 1, 8)
            if label_random >= 1 and label_random <= 4:
                $ label_random = scene_random[0]
            elif label_random == 5 or label_random == 6:
                $ label_random = scene_random[1]
            elif label_random == 7:
                $ label_random = scene_random[2]
            call pgn_livroom_max_watchtv_pornscenes from _call_pgn_livroom_max_watchtv_pornscenes
            $ renpy.pause()
            if pornfilm10.filming > 0 and "dreams_mommaid" not in accessiv:
                $ accessiv.append("dreams_mommaid")
                show pgn_livroom_max_watchtv_porn_pss
                $ renpy.pause(7, hard=True)
                m emo-13 "{i}Неожиданно! Наткнулся на рекламу.{/i}"
    $ qtime += 1
    if qtime == 4:
        jump loc_my_room_sleep
    jump loc_my_room

label pgn_livroom_max_watchtv_porn:
    $ scene_random = []
    $ label_random = [pgn_stat_sex_anal, pgn_stat_sex_cunni, pgn_stat_sex_bj, pgn_stat_sex_vaginal, pgn_stat_sex_hj]

    python:
        while len(scene_random) < 3:
            for i in label_random:
                label_random.remove(i)
                if i > max(label_random):
                    if i == pgn_stat_sex_anal:
                        scene_random.append("pgn_stat_sex_anal")
                    if i == pgn_stat_sex_cunni:
                        scene_random.append("pgn_stat_sex_cunni")
                    if i == pgn_stat_sex_bj:
                        scene_random.append("pgn_stat_sex_bj")
                    if i == pgn_stat_sex_vaginal:
                        scene_random.append("pgn_stat_sex_vaginal")
                    if i == pgn_stat_sex_hj:
                        scene_random.append("pgn_stat_sex_hj")
                else:
                    label_random.append(i)
    return


label pgn_livroom_max_watchtv_pornscenes:
    if label_random == "pgn_stat_sex_anal":
        $ label_random = renpy.random.randint ( 1, 6)
        if label_random == 1:
            show pgn_livroom_max_watchtv_porn_anal_01
        elif label_random == 2:
            show pgn_livroom_max_watchtv_porn_anal_02
        elif label_random == 3:
            show pgn_livroom_max_watchtv_porn_anal_03
        elif label_random == 4:
            show pgn_livroom_max_watchtv_porn_anal_04
        elif label_random == 5:
            show pgn_livroom_max_watchtv_porn_anal_05
        elif label_random == 6:
            show pgn_livroom_max_watchtv_porn_anal_06
    elif label_random == "pgn_stat_sex_cunni":
        $ label_random = renpy.random.randint ( 1, 6)
        if label_random == 1:
            show pgn_livroom_max_watchtv_porn_cunni_01
        elif label_random == 2:
            show pgn_livroom_max_watchtv_porn_cunni_02
        elif label_random == 3:
            show pgn_livroom_max_watchtv_porn_cunni_03
        elif label_random == 4:
            show pgn_livroom_max_watchtv_porn_cunni_04
        elif label_random == 5:
            show pgn_livroom_max_watchtv_porn_cunni_05
        elif label_random == 6:
            show pgn_livroom_max_watchtv_porn_cunni_06
    elif label_random == "pgn_stat_sex_bj":
        $ label_random = renpy.random.randint ( 1, 6)
        if label_random == 1:
            show pgn_livroom_max_watchtv_porn_bj_01
        elif label_random == 2:
            show pgn_livroom_max_watchtv_porn_bj_02
        elif label_random == 3:
            show pgn_livroom_max_watchtv_porn_bj_03
        elif label_random == 4:
            show pgn_livroom_max_watchtv_porn_bj_04
        elif label_random == 5:
            show pgn_livroom_max_watchtv_porn_bj_05
        elif label_random == 6:
            show pgn_livroom_max_watchtv_porn_bj_06
    elif label_random == "pgn_stat_sex_vaginal":
        $ label_random = renpy.random.randint ( 1, 6)
        if label_random == 1:
            show pgn_livroom_max_watchtv_porn_sex_01
        elif label_random == 2:
            show pgn_livroom_max_watchtv_porn_sex_02
        elif label_random == 3:
            show pgn_livroom_max_watchtv_porn_sex_03
        elif label_random == 4:
            show pgn_livroom_max_watchtv_porn_sex_04
        elif label_random == 5:
            show pgn_livroom_max_watchtv_porn_sex_05
        elif label_random == 6:
            show pgn_livroom_max_watchtv_porn_sex_06
    elif label_random == "pgn_stat_sex_hj":
        $ label_random = renpy.random.randint ( 1, 6)
        if label_random == 1:
            show pgn_livroom_max_watchtv_porn_hj_01
        elif label_random == 2:
            show pgn_livroom_max_watchtv_porn_hj_02
        elif label_random == 3:
            show pgn_livroom_max_watchtv_porn_hj_03
        elif label_random == 4:
            show pgn_livroom_max_watchtv_porn_hj_04
        elif label_random == 5:
            show pgn_livroom_max_watchtv_porn_hj_05
        elif label_random == 6:
            show pgn_livroom_max_watchtv_porn_hj_06
    elif label_random == 8:
        show pgn_livroom_max_watchtv_01
        m emo-2 "Блин! Невовремя."
    return


label pgn_dreams_mommaid:
    if ("dreams_mommaid_first") not in accessiv:
        mom emo-75 "[pname_max[0]]!"
        m emo-10 "Да, да встаю."
        scene pgn_myroom_liza_solonight_01
        m emo-6 "{i}Хм... тут никого нет. Посмотрю снаружи.{/i}"
    scene pgn_dreams_mommaid_01
    if ("dreams_mommaid_first") not in accessiv:
        m emo-9 "Охх блин! Где это я? Я во сне?"
    mom emo-75 "[pname_max[0]]!"
    if ("dreams_mommaid_first") not in accessiv:
        menu:
            "Открыть дверь":
                scene pgn_dreams_mommaid_02
                m emo-6 "Куда я попал?"
                scene pgn_dreams_mommaid_03
                m emo-13 "Может мне лучше выйти от сюда?"
                m emo-8 "Заперто."
                scene pgn_dreams_mommaid_04
                m emo-6 "Это туалет? Какой-то странный сон."
                mom emo-67 "[pname_max[0]], ты пришёл наказать свою любимую мамочку?"
                scene pgn_dreams_mommaid_05
                m emo-9 "Ааа?! Никого."
                mom emo-62 "Я здесь."
            "Продолжить спать":
                jump loc_my_room_sleep_02_dreamsnext
    if ("dreams_mommaid_first") not in accessiv:
        $ accessiv.append("dreams_mommaid_first")
label pgn_dreams_mommaid_ach:
    scene pgn_dreams_mommaid_06
    $ PGN_Achadd(pgnach_178, 178)
    mom emo-67 "Мамочка, ожидает..."
    scene pgn_dreams_mommaid_07
    mom emo-75 "твоих приказов.\n\n{color=#ccc}Сцена сделана в благодарность VaDX, за помощь с рендером сцен.{/color}"
    $ scene_random,label_random = [], []







label pgn_dreams_mommaid_dress:
    scene animated pgn_dreams_mommaid_dress_01
    call screen choice_mommaid_dress

screen choice_mommaid_dress:
    vbox:
        align (0.1, 0.5)
        hbox:
            button:
                padding (30, 10, 30, 12)
                if "римминг" not in scene_random:
                    text _("Римминг")
                    idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
                    hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_red.png",)
                    action Function(screenlistadd, scene_random, "append", "римминг")
                if "римминг" in scene_random:
                    text _("{outlinecolor=#fff}{color=#000}Римминг{/color}{/outlinecolor}")
                    background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_hover.png",)
                    action Function(screenlistadd, scene_random, "remove", "римминг")
            null width 50
            if "римминг" in scene_random:
                button:
                    padding (30, 10, 30, 12)
                    text _("Глубокий Минет")
                    idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
                    hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_blue.png",)
                    action Function(screenlistadd, scene_random, "append", "глубокий_минет"), Jump("pgn_dreams_mommaid_dress_rimm")
                null width 25
                button:
                    padding (30, 10, 30, 12)
                    text _("Мастурбация")
                    idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
                    hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_blue.png",)
                    action Function(screenlistadd, scene_random, "append", "мастурбация"), Jump("pgn_dreams_mommaid_dress_rimm")
        null height 40
        button:
            padding (30, 10, 30, 12)
            text _("Пописать Маме в рот")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_yellow.png",)
            action Jump("pgn_dreams_mommaid_dress_pee")
        null height 40
        button:
            padding (30, 10, 30, 12)
            text _("Унизить")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_green.png",)
            action Jump("pgn_dreams_mommaid_dress_hum")
        null height 40
        button:
            padding (30, 10, 30, 12)
            text _("Мама Писает")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_violet.png",)
            action Jump("pgn_dreams_mommaid_dress_mompee")
        null height 70
        button:
            padding (30, 10, 30, 12)
            text _("БЕЗ ОДЕЖДЫ")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_hover.png",)
            action Jump("pgn_dreams_mommaid_undress")
    hbox:
        align (1.0, 0.95)
        button xpos -166:
            minimum (130, 130)
            maximum (130, 204)
            imagebutton:
                yalign 1.0
                idle "images/nav/nav_sleep_a.png"
                hover "images/nav/nav_sleep_b.png"
                if pgn_ach_repeat == 0:
                    action Jump("loc_my_room_sleep_02_dreamsnext")
                else:
                    action Jump("table_pgn_achievement")
            add ("images/nav/nav_lvl2_empty.png")


label pgn_dreams_mommaid_dress_rimm:
    scene pgn_dreams_mommaid_dress_rim_01
    m emo-3 "Поработай язычком."
    scene pgn_dreams_mommaid_dress_rim_02
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_rim_03
    $ renpy.pause()
    if "глубокий_минет" in scene_random:
        scene pgn_dreams_mommaid_dress_rim_04
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_05
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_06
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_07
        m emo-3 "Отлично! Вылежи мой член и отсоси."
        mom emo-67 "Слушаюсь, хозяин."
        scene pgn_dreams_mommaid_dress_rim_08
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_09
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_10
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_11
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_12
        m emo-4 "Хорошо. Очень хорошо. Заглатывай его полностью."
        scene pgn_dreams_mommaid_dress_rim_13
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_14
        m emo-10 "Глубже! Ох! Сейчас кончу."
        scene pgn_dreams_mommaid_dress_rim_15
        m emo-12 "Аааррргхх!"
        scene pgn_dreams_mommaid_dress_rim_16
        m emo-7 "Ааааах! Аааа..."
        scene pgn_dreams_mommaid_dress_rim_17
        m emo-4 "Всё проглотила? Хорошая рабыня."
        scene pgn_dreams_mommaid_dress_rim_18
        $ label_random.append("римминг_глотка")
    if "мастурбация" in scene_random:
        m emo-3 "Хочу, чтобы ты мне ещё и подрочила."
        mom emo-75 "Повинуюсь."
        scene pgn_dreams_mommaid_dress_rim_19
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_20
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_21
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_22
        m emo-10 "Мастурбируй активнее. Я хочу кончить."
        scene pgn_dreams_mommaid_dress_rim_23
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_24
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_rim_25
        m emo-12 "Аргххх!!!"
        scene pgn_dreams_mommaid_dress_rim_26
        $ label_random.append("римминг_мастурбация")
    $ renpy.pause()
    call mommaid_dress_end from _call_mommaid_dress_end
    call screen choice_mommaid_dress


label pgn_dreams_mommaid_dress_mompee:
    if ("мамаписает") not in label_random:
        m emo-1 "Пописай в раковину."
        scene pgn_dreams_mommaid_dress_pee_17
        $ renpy.pause()
        scene pgn_dreams_mommaid_dress_pee_18
        $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_19
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_20
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_21
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_22
    m emo-3 "Хорошая девочка."
    scene pgn_dreams_mommaid_dress_pee_23
    $ renpy.pause()
    $ label_random.append("мамаписает")
    call mommaid_dress_end from _call_mommaid_dress_end_1
    call screen choice_mommaid_dress

label pgn_dreams_mommaid_dress_pee:
    if ("римминг_мастурбация") not in label_random and ("писсингврот") not in label_random:
        scene pgn_dreams_mommaid_dress_pee_01
        $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_02
    m emo-10 "Пись, пись, пись..."
    scene pgn_dreams_mommaid_dress_pee_03
    mom emo-69 "..."
    m emo-7 "..."
    mom emo-68 "Мм... мммм... Мммхм..."
    scene pgn_dreams_mommaid_dress_pee_04
    m emo-6 "Хочешь чтобы я пописал в тебя?"
    mom emo-67 "..."
    scene pgn_dreams_mommaid_dress_pee_05
    m emo-3 "Не глотай, пока не разрешу."
    scene pgn_dreams_mommaid_dress_pee_06
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_07
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_08
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_09
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_10
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_11
    m emo-0 "Так, снимем с тебя это."
    scene pgn_dreams_mommaid_dress_pee_12
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_13
    m emo-4 "Глотай!"
    scene pgn_dreams_mommaid_dress_pee_14
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_pee_15
    m emo-3 "Умничка! Ты моя послушная шлюшка."
    mom emo-75 "..."
    scene pgn_dreams_mommaid_dress_pee_16
    $ renpy.pause()
    $ label_random.append("писсингврот")
    call mommaid_dress_end from _call_mommaid_dress_end_2
    call screen choice_mommaid_dress


label pgn_dreams_mommaid_dress_hum:
    $ countdown = 0
    scene pgn_dreams_mommaid_dress_domin_01
    $ renpy.pause()
    scene pgn_dreams_mommaid_dress_domin_02_01
    menu pgn_dreams_mommaid_dress_hum_m1:
        "Раздеть":
            jump pgn_dreams_mommaid_undress_hum
        "Кончить на неё":
            if renpy.random.randint ( 2, 3) == 2:
                scene pgn_dreams_mommaid_dress_domin_03_cum_01a
                m emo-12 "Аргххх!!!"
                scene pgn_dreams_mommaid_dress_domin_03_cum_01b
                $ renpy.pause()
                scene pgn_dreams_mommaid_dress_domin_end_01a
            else:
                scene pgn_dreams_mommaid_dress_domin_03_cum_02a
                m emo-12 "Аргххх!!!"
                scene pgn_dreams_mommaid_dress_domin_03_cum_02b
                $ renpy.pause()
                scene pgn_dreams_mommaid_dress_domin_end_01b
        "Кончить в рот":
            scene pgn_dreams_mommaid_dress_domin_05
            m emo-12 "Аргххх!!!"
            scene pgn_dreams_mommaid_dress_domin_06
            $ renpy.pause()
            scene pgn_dreams_mommaid_dress_domin_07
            m emo-3 "Проглоти."
            scene pgn_dreams_mommaid_dress_domin_08
            mom emo-75 "Мммм..."
            scene pgn_dreams_mommaid_dress_domin_09
            $ renpy.pause()
            scene pgn_dreams_mommaid_dress_domin_end_02
        "Оскорбить или Похвалить":
            menu:
                "У меня нет туннельного синдрома":
                    m emo-0 "У меня нет ни каких проблем с кистями рук. Просто нравится, когда ты мне мастурбируешь."
                    $ countdown += 1
                    if countdown > 0:
                        scene pgn_dreams_mommaid_dress_domin_02_01
                    else:
                        scene pgn_dreams_mommaid_dress_domin_02_05
                    mom emo-62 "..."
                "Ты самая худшая мама":
                    m emo-11 "Ты самая ужасная и худшая мама на свете."
                    $ countdown -= 1
                    call pgn_dreams_mommaid_dress_hum_pbed from _call_pgn_dreams_mommaid_dress_hum_pbed
                "Не люблю":
                    m emo-0 "Я тебя не люблю и не любил."
                    $ countdown -= 1
                    call pgn_dreams_mommaid_dress_hum_pbed from _call_pgn_dreams_mommaid_dress_hum_pbed_1
                "Шлюха":
                    m emo-3 "Ты же шлюшка? Да, Мама? Ты хочешь быть моей шлюшкой и каждый день скакать на моём члене?"
                    $ countdown += 1
                    call pgn_dreams_mommaid_dress_hum_pgood from _call_pgn_dreams_mommaid_dress_hum_pgood
                "Первая эрекция":
                    m emo-4 "Моя первая эрекция появилась, когда ты, в прошлом месте где жили, вышла из ванны в одном полотенце."
                    m emo-3 "Твоё тело слегка красноватое от горячей воды, а твой ротик был слегка приоткрыт, т.к. не могла хорошо надышаться свежим и прохладным воздухом."
                    m emo-4 "Затем, подойдя к холодильнику, слегка наклонилась и полотенце задралось и я увидел твою горячую и сексуальную киску. И тогда я понял, что хочу тебя."
                    $ countdown += 2
                    if countdown < 4:
                        $ countdown = 4
                    call pgn_dreams_mommaid_dress_hum_pgood from _call_pgn_dreams_mommaid_dress_hum_pgood_1
                "Большие сиськи. Хорошо":
                    m emo-4 "Я обожаю эти большие и мягкие сиськи. Так и хочется зарыться между ними. Было бы ещё круче, если они давали молоко."
                    $ countdown += 1
                    scene pgn_dreams_mommaid_dress_domin_02_09
                    mom emo-67 "..."
                "Большие сиськи. Плохо":
                    m emo-13 "Скоро твои сиськи обвиснут и ты станешь совсем непривлекательной, а значит секса больше нет будет."
                    $ countdown -= 1
                    if countdown > 5:
                        scene pgn_dreams_mommaid_dress_domin_02_04
                        mom emo-69 "..."
                    else:
                        call pgn_dreams_mommaid_dress_hum_pbed from _call_pgn_dreams_mommaid_dress_hum_pbed_2
                "Анал":
                    m emo-6 "Мама, тебе нравится анальный секс? От анала ты бурно кончаешь."
                    $ countdown += 1
                    call pgn_dreams_mommaid_dress_hum_pgood from _call_pgn_dreams_mommaid_dress_hum_pgood_2
                    m emo-4 "Конечно нравится, иначе бы не кончала."
                    menu:
                        "[pname_liza[0]]":
                            m emo-4 "[pname_liza[2]] тоже нравится. Она так же обожает насаживаться попкой на мой член. И да, мы занимаемся с ней сексом."
                            if countdown <= 5:
                                $ countdown -= 2
                                call pgn_dreams_mommaid_dress_hum_pbed from _call_pgn_dreams_mommaid_dress_hum_pbed_3
                            else:
                                call pgn_dreams_mommaid_dress_hum_pgood from _call_pgn_dreams_mommaid_dress_hum_pgood_3
                                m emo-3 "..."
                        "назад":
                            pass
                "Моя сучка":
                    m emo-4 "Ты ебучая сучка, только моя, только для удовлетворения моих желаний. Контейнер для сбор моей спермы."
                    if countdown < 8:
                        $ countdown -= 1
                        call pgn_dreams_mommaid_dress_hum_pbed from _call_pgn_dreams_mommaid_dress_hum_pbed_4
                    else:
                        call pgn_dreams_mommaid_dress_hum_pgood from _call_pgn_dreams_mommaid_dress_hum_pgood_4
                        m emo-3 "..."
            jump pgn_dreams_mommaid_dress_hum_m1
        "Взяться за горло":
            scene pgn_dreams_mommaid_dress_domin_10
            $ countdown = 0
            menu:
                "Пустить слюну в рот":
                    m emo-0 "Держи рот открытым."
                    scene pgn_dreams_mommaid_dress_domin_11
                    $ renpy.pause()
                    scene pgn_dreams_mommaid_dress_domin_12
                    $ renpy.pause()
                    scene pgn_dreams_mommaid_dress_domin_13
                    $ renpy.pause()
                    scene pgn_dreams_mommaid_dress_domin_14
                    menu pgn_dreams_mommaid_dress_hum_m2:
                        "Глотай":
                            if renpy.random.randint ( 1, 2) == 1:
                                scene pgn_dreams_mommaid_dress_domin_17
                                if countdown < 2:
                                    show pgn_dreams_mommaid_dress_domin_17_01a
                                else:
                                    show pgn_dreams_mommaid_dress_domin_17_01b
                                $ renpy.pause()
                                scene pgn_dreams_mommaid_dress_domin_17
                                if countdown < 2:
                                    show pgn_dreams_mommaid_dress_domin_17_02a
                                else:
                                    show pgn_dreams_mommaid_dress_domin_17_02b
                                $ renpy.pause()
                                scene pgn_dreams_mommaid_dress_domin_end_02
                                if countdown > 1:
                                    show pgn_dreams_mommaid_dress_domin_end_02_red
                            else:
                                $ renpy.pause()
                                m emo-11 "Плохая шлюшка. Я сказал глотать, значит глотай."
                                jump pgn_dreams_mommaid_dress_hum_m2
                        "Шлепнуть по лицу":
                            label pgn_dreams_mommaid_dress_hum_slap:
                                scene pgn_dreams_mommaid_dress_domin_15
                                $ renpy.pause()
                                scene pgn_dreams_mommaid_dress_domin_16
                                $ renpy.pause()
                                $ countdown += 1
                                if renpy.random.randint ( 1, 4) == 3 or countdown == 4:
                                    scene pgn_dreams_mommaid_dress_domin_17
                                    if countdown < 2:
                                        show pgn_dreams_mommaid_dress_domin_17_01a
                                    else:
                                        show pgn_dreams_mommaid_dress_domin_17_01b
                                    $ renpy.pause()
                                    scene pgn_dreams_mommaid_dress_domin_17
                                    if countdown < 2:
                                        show pgn_dreams_mommaid_dress_domin_17_02a
                                    else:
                                        show pgn_dreams_mommaid_dress_domin_17_02b
                                    $ renpy.pause()
                                    scene pgn_dreams_mommaid_dress_domin_end_02
                                    if countdown > 1:
                                        show pgn_dreams_mommaid_dress_domin_end_02_red
                                else:
                                    scene pgn_dreams_mommaid_dress_domin_17
                                    if countdown > 1:
                                        show pgn_dreams_mommaid_dress_domin_17_red
                                    m emo-11 "Непослушная сучка. Ну же, глотай!"
                                    jump pgn_dreams_mommaid_undress_hum_m2
                "Пальцы в горло и кончить в рот":
                    label pgn_dreams_mommaid_dress_hum_throat:
                        scene pgn_dreams_mommaid_dress_domin_18
                        if countdown > 0:
                            show pgn_dreams_mommaid_dress_domin_18_mascara
                            m emo-3 "Ещё ра, мамочка. Заглоти пальцы."
                        mom emo-68 "..."
                        m emo-4 "Расслабь язычок."
                        scene pgn_dreams_mommaid_dress_domin_19
                        if countdown > 0:
                            show pgn_dreams_mommaid_dress_domin_19_mascara
                        mom emo-68 "Грхл... Хм... Грхл..."
                        m emo-3 "Ещё глубже..."
                        scene pgn_dreams_mommaid_dress_domin_20
                        if countdown > 0:
                            show pgn_dreams_mommaid_dress_domin_20_mascara
                        m emo-4 "Молодец..."
                        $ countdown = 1
                        menu:
                            "Ещё раз":
                                jump pgn_dreams_mommaid_dress_hum_throat
                            "Кончить в рот":
                                scene pgn_dreams_mommaid_dress_domin_05
                                show pgn_dreams_mommaid_dress_domin_05_mascara
                                m emo-12 "Аргххх!!!"
                                scene pgn_dreams_mommaid_dress_domin_06
                                show pgn_dreams_mommaid_dress_domin_06_mascara
                                $ renpy.pause()
                                scene pgn_dreams_mommaid_dress_domin_07
                                show pgn_dreams_mommaid_dress_domin_07_mascara
                                m emo-3 "Проглоти."
                                scene pgn_dreams_mommaid_dress_domin_08
                                show pgn_dreams_mommaid_dress_domin_08_mascara
                                mom emo-75 "Мммм..."
                                scene pgn_dreams_mommaid_dress_domin_09
                                show pgn_dreams_mommaid_dress_domin_09_mascara
                                $ renpy.pause()
                                scene pgn_dreams_mommaid_dress_domin_end_02
                                show pgn_dreams_mommaid_dress_domin_end_02_mascara
        "назад":
            jump pgn_dreams_mommaid_dress
    $ renpy.pause()
    $ label_random.append("унижение")
    call mommaid_dress_end from _call_mommaid_dress_end_3
    call screen choice_mommaid_dress

label pgn_dreams_mommaid_dress_hum_pbed:
    if countdown > 6:
        scene pgn_dreams_mommaid_dress_domin_02_05
        mom emo-60 "..."
    elif countdown == 5 or countdown == 6:
        scene pgn_dreams_mommaid_dress_domin_02_03
        mom emo-69 "..."
    elif countdown == 3 or countdown == 4:
        scene pgn_dreams_mommaid_dress_domin_02_02
        mom emo-69 "..."
    else:
        scene pgn_dreams_mommaid_dress_domin_02_10
        mom emo-73 "..."
    return

label pgn_dreams_mommaid_dress_hum_pgood:
    if countdown < 3:
        scene pgn_dreams_mommaid_dress_domin_02_03
        mom emo-69 "..."
    elif countdown == 4:
        scene pgn_dreams_mommaid_dress_domin_02_06
        mom emo-62 "..."
    elif countdown == 5:
        scene pgn_dreams_mommaid_dress_domin_02_07
        mom emo-67 "..."
    elif countdown == 6:
        scene pgn_dreams_mommaid_dress_domin_02_08
        mom emo-71 "..."
    elif countdown >= 7 and countdown <= 9:
        scene pgn_dreams_mommaid_dress_domin_02_11
        mom emo-75 "..."
    else:
        scene pgn_dreams_mommaid_dress_domin_02_09
        mom emo-75 "..."
    return










label pgn_dreams_mommaid_undress:
    scene animated pgn_dreams_mommaid_undress_01
    call screen choice_mommaid_undress

screen choice_mommaid_undress:
    vbox:
        align (0.1, 0.5)
        button:
            padding (30, 10, 30, 12)
            text _("Анал")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_red.png",)
            action Jump("pgn_dreams_mommaid_undress_anal")
        null height 40
        button:
            padding (30, 10, 30, 12)
            text _("Глубокий минет")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_blue.png",)
            action Jump("pgn_dreams_mommaid_undress_deepthorat")
        null height 40
        button:
            padding (30, 10, 30, 12)
            text _("Унизить")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_green.png",)
            action Jump("pgn_dreams_mommaid_undress_hum")
        null height 40
        button:
            padding (30, 10, 30, 12)
            text _("Наказать")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_black.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle_violet.png",)
            action Jump("pgn_dreams_mommaid_undress_punish")
        null height 70
        button:
            padding (30, 10, 30, 12)
            text _("В ОДЕЖДЕ")
            idle_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_idle.png",)
            hover_background Frame("images/mods/pgn/renders/home/myroom/dreams_mom/backgr_hover.png",)
            action Jump("pgn_dreams_mommaid_dress")
    hbox:
        align (1.0, 0.95)
        button xpos -166:
            minimum (130, 130)
            maximum (130, 204)
            imagebutton:
                yalign 1.0
                idle "images/nav/nav_sleep_a.png"
                hover "images/nav/nav_sleep_b.png"
                if pgn_ach_repeat == 0:
                    action Jump("loc_my_room_sleep_02_dreamsnext")
                else:
                    action Jump("table_pgn_achievement")
            add ("images/nav/nav_lvl2_empty.png")

label pgn_dreams_mommaid_undress_anal:
    if ("анал") not in label_random:
        scene pgn_dreams_mommaid_undress_anal_01
        $ renpy.pause()
    scene pgn_dreams_mommaid_undress_anal_02
    m emo-3 "Потрясающая попка"
    scene pgn_dreams_mommaid_undress_anal_03a
    mom emo-68 "Ааах... Аааах..."
    scene pgn_dreams_mommaid_undress_anal_03b
    mom emo-68 "Ммм... Аааа... Ммм... Ааа..."
    scene pgn_dreams_mommaid_undress_anal_04
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_anal_05
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_anal_06
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_anal_07
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_anal_05
    menu:
        "Кончить на спину":
            scene pgn_dreams_mommaid_undress_anal_08
            m emo-12 "Аргххх!!!"
            scene pgn_dreams_mommaid_undress_anal_09
            m emo-10 "Ааааа..."
            scene pgn_dreams_mommaid_undress_anal_10
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_end_01
        "Кончить в попу":
            scene pgn_dreams_mommaid_undress_anal_05_02
            m emo-12 "Аргххх!!!"
            scene pgn_dreams_mommaid_undress_anal_11
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_12
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_13
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_end_01
        "Кончить на неё":
            m emo-13 "Вставай быстрее!"
            scene pgn_dreams_mommaid_undress_anal_14
            m emo-10 "Я почти..."
            scene pgn_dreams_mommaid_undress_anal_15
            m emo-12 "Аргххх!!!"
            scene pgn_dreams_mommaid_undress_anal_16
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_end_01
        "Головой в унитаз":
            scene pgn_dreams_mommaid_undress_anal_17
            mom emo-66 "Аааа!"
            m emo-4 "Вниз голову!"
            scene pgn_dreams_mommaid_undress_anal_18
            m emo-3 "Ниже!"
            scene pgn_dreams_mommaid_undress_anal_19
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_20
            m emo-12 "Да, да... Глубже, по самые яйца."
            scene pgn_dreams_mommaid_undress_anal_21
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_22
            mom emo-68 "Ааах... Аааах..."
            scene pgn_dreams_mommaid_undress_anal_23
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_24
            m emo-12 "Аргххх!!! Глотай!"
            scene pgn_dreams_mommaid_undress_anal_25
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_anal_end_02
    $ renpy.pause()

    $ label_random.append("анал")
    call mommaid_dress_end from _call_mommaid_dress_end_4
    call screen choice_mommaid_undress

label pgn_dreams_mommaid_undress_deepthorat:
    scene pgn_dreams_mommaid_undress_deepthroat_01a
    m emo-3 "Мягкие губки. Очень сексуальный ротик."
    scene pgn_dreams_mommaid_undress_deepthroat_01b
    mom emo-67 "Мммм..."
    scene pgn_dreams_mommaid_undress_deepthroat_02
    m emo-4 "Лучше пососи вот этот большой палец."
    scene pgn_dreams_mommaid_undress_deepthroat_03
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_deepthroat_04
    m emo-3 "Возьми глубже, полностью."
    mom emo-68 "..."
    scene pgn_dreams_mommaid_undress_deepthroat_05
    m emo-12 "О да!"
    mom emo-68 "Мхм... Грхл... Мхм..."
    scene pgn_dreams_mommaid_undress_deepthroat_06
    mom emo-69 "..."
    scene pgn_dreams_mommaid_undress_deepthroat_07
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_deepthroat_06
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_deepthroat_09
    m emo-4 "О да! Класс!"
    scene pgn_dreams_mommaid_undress_deepthroat_10
    mom emo-69 "..."
    m emo-3 "Продолжим."
    scene pgn_dreams_mommaid_undress_deepthroat_09
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_deepthroat_11
    m emo-4 "Я рад, что тебе нравится. Из киски ручьём сочится вкусный сок."
    m emo-1 "Продолжай сосать."
    scene pgn_dreams_mommaid_undress_deepthroat_13
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_deepthroat_14
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_deepthroat_15
    mom emo-69 "..."
    scene pgn_dreams_mommaid_undress_deepthroat_14
    m emo-4 "Глубже! Ещё глубже заглатывай!"
    scene pgn_dreams_mommaid_undress_deepthroat_16
    mom emo-68 "Ааххх!"
    scene pgn_dreams_mommaid_undress_deepthroat_17
    m emo-3 "Совсем другое дело. Ох блин... Офигенно!"
    scene pgn_dreams_mommaid_undress_deepthroat_18
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_deepthroat_19
    m emo-3 "Соси. Я скоро уже кончу."
    scene pgn_dreams_mommaid_undress_deepthroat_20
    m emo-12 "Аргххх!!!"
    scene pgn_dreams_mommaid_undress_deepthroat_21a
    $ renpy.pause()
    show pgn_dreams_mommaid_undress_deepthroat_21b
    $ renpy.pause()
    scene pgn_dreams_mommaid_undress_deepthroat_end
    $ renpy.pause()

    $ label_random.append("глубокая глотка")
    call mommaid_dress_end from _call_mommaid_dress_end_5
    call screen choice_mommaid_undress

label pgn_dreams_mommaid_undress_hum:
    $ countdown = 0
    scene pgn_dreams_mommaid_undress_domin_1_02_01
    menu pgn_dreams_mommaid_undress_hum_m1:
        "Кончить на неё":
            if renpy.random.randint ( 2, 3) == 2:
                scene pgn_dreams_mommaid_undress_domin_1_03_cum_01a
                m emo-12 "Аргххх!!!"
                scene pgn_dreams_mommaid_undress_domin_1_03_cum_01b
                $ renpy.pause()
                scene pgn_dreams_mommaid_undress_domin_1_end_01a
            else:
                scene pgn_dreams_mommaid_undress_domin_1_03_cum_02a
                m emo-12 "Аргххх!!!"
                scene pgn_dreams_mommaid_undress_domin_1_03_cum_02b
                $ renpy.pause()
                scene pgn_dreams_mommaid_undress_domin_1_end_01b
        "Кончить в рот":
            scene pgn_dreams_mommaid_undress_domin_1_05
            m emo-12 "Аргххх!!!"
            scene pgn_dreams_mommaid_undress_domin_1_06
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_1_07
            m emo-3 "Проглоти."
            scene pgn_dreams_mommaid_undress_domin_1_08
            mom emo-75 "Мммм..."
            scene pgn_dreams_mommaid_undress_domin_1_09
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_1_end_02
        "Оскорбить или Похвалить":
            menu:
                "У меня нет туннельного синдрома":
                    m emo-0 "У меня нет ни каких проблем с кистями рук. Просто нравится, когда ты мне мастурбируешь."
                    $ countdown += 1
                    if countdown > 0:
                        scene pgn_dreams_mommaid_undress_domin_1_02_01
                    else:
                        scene pgn_dreams_mommaid_undress_domin_1_02_05
                    mom emo-62 "..."
                "Ты самая худшая мама":
                    m emo-11 "Ты самая ужасная и худшая мама на свете."
                    $ countdown -= 1
                    call pgn_dreams_mommaid_undress_hum_pbed from _call_pgn_dreams_mommaid_undress_hum_pbed
                "Не люблю":
                    m emo-0 "Я тебя не люблю и не любил."
                    $ countdown -= 1
                    call pgn_dreams_mommaid_undress_hum_pbed from _call_pgn_dreams_mommaid_undress_hum_pbed_1
                "Шлюха":
                    m emo-3 "Ты же шлюшка? Да, Мама? Ты хочешь быть моей шлюшкой и каждый день скакать на моём члене?"
                    $ countdown += 1
                    call pgn_dreams_mommaid_undress_hum_pgood from _call_pgn_dreams_mommaid_undress_hum_pgood
                "Первая эрекция":
                    m emo-4 "Моя первая эрекция появилась, когда ты, в прошлом месте где жили, вышла из ванны в одном полотенце."
                    m emo-3 "Твоё тело слегка красноватое от горячей воды, а твой ротик был слегка приоткрыт, т.к. не могла хорошо надышаться свежим и прохладным воздухом."
                    m emo-4 "Затем, подойдя к холодильнику, слегка наклонилась и полотенце задралось и я увидел твою горячую и сексуальную киску. И тогда я понял, что хочу тебя."
                    $ countdown += 2
                    if countdown < 4:
                        $ countdown = 4
                    call pgn_dreams_mommaid_undress_hum_pgood from _call_pgn_dreams_mommaid_undress_hum_pgood_1
                "Большие сиськи. Хорошо":
                    m emo-4 "Я обожаю эти большие и мягкие сиськи. Так и хочется зарыться между ними. Было бы ещё круче, если они давали молоко."
                    $ countdown += 1
                    scene pgn_dreams_mommaid_undress_domin_1_02_09
                    mom emo-67 "..."
                "Большие сиськи. Плохо":
                    m emo-13 "Скоро твои сиськи обвиснут и ты станешь совсем непривлекательной, а значит секса больше нет будет."
                    $ countdown -= 1
                    if countdown > 5:
                        scene pgn_dreams_mommaid_undress_domin_1_02_04
                        mom emo-69 "..."
                    else:
                        call pgn_dreams_mommaid_undress_hum_pbed from _call_pgn_dreams_mommaid_undress_hum_pbed_2
                "Анал":
                    m emo-6 "Мама, тебе нравится анальный секс? От анала ты бурно кончаешь."
                    $ countdown += 1
                    call pgn_dreams_mommaid_undress_hum_pgood from _call_pgn_dreams_mommaid_undress_hum_pgood_2
                    m emo-4 "Конечно нравится, иначе бы не кончала."
                    menu:
                        "[pname_liza[0]]":
                            m emo-4 "[pname_liza[2]] тоже нравится. Она так же обожает насаживаться попкой на мой член. И да, мы занимаемся с ней сексом."
                            if countdown <= 5:
                                $ countdown -= 2
                                call pgn_dreams_mommaid_undress_hum_pbed from _call_pgn_dreams_mommaid_undress_hum_pbed_3
                            else:
                                call pgn_dreams_mommaid_undress_hum_pgood from _call_pgn_dreams_mommaid_undress_hum_pgood_3
                                m emo-3 "..."
                        "назад":
                            pass
                "Моя сучка":
                    m emo-4 "Ты ебучая сучка, только моя, только для удовлетворения моих желаний. Контейнер для сбор моей спермы."
                    if countdown < 8:
                        $ countdown -= 1
                        call pgn_dreams_mommaid_undress_hum_pbed from _call_pgn_dreams_mommaid_undress_hum_pbed_4
                    else:
                        call pgn_dreams_mommaid_undress_hum_pgood from _call_pgn_dreams_mommaid_undress_hum_pgood_4
                        m emo-3 "..."
            jump pgn_dreams_mommaid_undress_hum_m1
        "Пустить слюну в рот":
            scene pgn_dreams_mommaid_undress_domin_1_10
            $ countdown = 0
            m emo-0 "Держи рот открытым."
            scene pgn_dreams_mommaid_dress_domin_11
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_1_12
            $ renpy.pause()
            scene pgn_dreams_mommaid_dress_domin_13
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_1_14
            menu pgn_dreams_mommaid_undress_hum_m2:
                "Глотай":
                    if renpy.random.randint ( 1, 2) == 1:
                        scene pgn_dreams_mommaid_undress_domin_1_17
                        if countdown < 2:
                            show pgn_dreams_mommaid_undress_domin_1_17_01a
                        else:
                            show pgn_dreams_mommaid_undress_domin_1_17_01b
                        $ renpy.pause()
                        scene pgn_dreams_mommaid_undress_domin_1_17
                        if countdown < 2:
                            show pgn_dreams_mommaid_undress_domin_1_17_02a
                        else:
                            show pgn_dreams_mommaid_undress_domin_1_17_02b
                        $ renpy.pause()
                        scene pgn_dreams_mommaid_undress_domin_1_end_02
                        if countdown > 1:
                            show pgn_dreams_mommaid_undress_domin_1_end_02_red
                    else:
                        $ renpy.pause()
                        m emo-11 "Плохая шлюшка. Я сказал глотать, значит глотай."
                        jump pgn_dreams_mommaid_undress_hum_m2
                "Шлепнуть по лицу":
                    label pgn_dreams_mommaid_undress_hum_slap:
                        scene pgn_dreams_mommaid_undress_domin_1_15
                        $ renpy.pause()
                        scene pgn_dreams_mommaid_undress_domin_1_16
                        $ renpy.pause()
                        $ countdown += 1
                        if renpy.random.randint ( 1, 4) == 3 or countdown == 4:
                            scene pgn_dreams_mommaid_undress_domin_1_17
                            if countdown < 2:
                                show pgn_dreams_mommaid_undress_domin_1_17_01a
                            else:
                                show pgn_dreams_mommaid_undress_domin_1_17_01b
                            $ renpy.pause()
                            scene pgn_dreams_mommaid_undress_domin_1_17
                            if countdown < 2:
                                show pgn_dreams_mommaid_undress_domin_1_17_02a
                            else:
                                show pgn_dreams_mommaid_undress_domin_1_17_02b
                            $ renpy.pause()
                            scene pgn_dreams_mommaid_undress_domin_1_end_02
                            if countdown > 1:
                                show pgn_dreams_mommaid_undress_domin_1_end_02_red
                        else:
                            scene pgn_dreams_mommaid_undress_domin_1_17
                            if countdown > 1:
                                show pgn_dreams_mommaid_undress_domin_1_17_red
                            m emo-11 "Непослушная сучка. Глотай!"
                            jump pgn_dreams_mommaid_undress_hum_m2
        "назад":
            jump pgn_dreams_mommaid_undress

    $ label_random.append("унижение")
    call mommaid_dress_end from _call_mommaid_dress_end_6
    call screen choice_mommaid_undress

label pgn_dreams_mommaid_undress_hum_pbed:
    if countdown > 6:
        scene pgn_dreams_mommaid_undress_domin_1_02_05
        mom emo-60 "..."
    elif countdown == 5 or countdown == 6:
        scene pgn_dreams_mommaid_undress_domin_1_02_03
        mom emo-69 "..."
    elif countdown == 3 or countdown == 4:
        scene pgn_dreams_mommaid_undress_domin_1_02_02
        mom emo-69 "..."
    else:
        scene pgn_dreams_mommaid_undress_domin_1_02_10
        mom emo-73 "..."
    return

label pgn_dreams_mommaid_undress_hum_pgood:
    if countdown < 3:
        scene pgn_dreams_mommaid_undress_domin_1_02_03
        mom emo-69 "..."
    elif countdown == 4:
        scene pgn_dreams_mommaid_undress_domin_1_02_06
        mom emo-62 "..."
    elif countdown == 5:
        scene pgn_dreams_mommaid_undress_domin_1_02_07
        mom emo-67 "..."
    elif countdown == 6:
        scene pgn_dreams_mommaid_undress_domin_1_02_08
        mom emo-71 "..."
    elif countdown >= 7 and countdown <= 9:
        scene pgn_dreams_mommaid_undress_domin_1_02_11
        mom emo-75 "..."
    else:
        scene pgn_dreams_mommaid_undress_domin_1_02_09
        mom emo-75 "..."
    return


label pgn_dreams_mommaid_undress_punish:
    scene pgn_dreams_mommaid_undress_domin_2_01
    menu pgn_dreams_mommaid_undress_punish_m1:
        "Лицо":
            $ countdown = 0
            label pgn_dreams_mommaid_undress_punish_face:
                scene pgn_dreams_mommaid_undress_domin_2_02
                if countdown > 3:
                    show pgn_dreams_mommaid_undress_domin_2_02_red
                $ renpy.pause()
                scene pgn_dreams_mommaid_undress_domin_2_03
                if countdown > 3:
                    show pgn_dreams_mommaid_undress_domin_2_03_red
                $ renpy.pause()
                scene pgn_dreams_mommaid_undress_domin_2_04
                $ renpy.pause()
                $ countdown += 1
                scene pgn_dreams_mommaid_undress_domin_2_02
                if countdown > 3:
                    show pgn_dreams_mommaid_undress_domin_2_02_red
                menu:
                    "Ещё раз":
                        jump pgn_dreams_mommaid_undress_punish_face
                    "назад":
                        jump pgn_dreams_mommaid_undress_punish
        "Попка":
            $ countdown = 1
            m emo-4 "Подставляй попку."
            scene pgn_dreams_mommaid_undress_domin_2_13
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_14
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_15
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_16
            $ renpy.pause()
            label pgn_dreams_mommaid_undress_punish_ass:
                scene pgn_dreams_mommaid_undress_domin_2_17_01a
                if countdown > 3:
                    show pgn_dreams_mommaid_undress_domin_2_17_01a_red
                $ renpy.pause()
                scene pgn_dreams_mommaid_undress_domin_2_17_01b
                if countdown > 3:
                    show pgn_dreams_mommaid_undress_domin_2_17_01b_red
                mom emo-68 "Ааххх!"
                scene pgn_dreams_mommaid_undress_domin_2_17_02a
                if countdown > 3:
                    show pgn_dreams_mommaid_undress_domin_2_17_02a_red
                $ renpy.pause()
                scene pgn_dreams_mommaid_undress_domin_2_17_02b
                if countdown > 3:
                    show pgn_dreams_mommaid_undress_domin_2_17_02b_red
                mom emo-68 "Ааххх!"
                menu:
                    "Ещё раз":
                        $ countdown += 1
                        jump pgn_dreams_mommaid_undress_punish_ass
                    "Продолжить":
                        label pgn_dreams_mommaid_undress_punish_ass_2:
                            scene pgn_dreams_mommaid_undress_domin_2_17_03a
                            $ renpy.pause()
                            scene pgn_dreams_mommaid_undress_domin_2_17_03b
                            if countdown == 4:
                                show pgn_dreams_mommaid_undress_domin_2_17_03b_01
                            if countdown > 4 and countdown < 9:
                                show pgn_dreams_mommaid_undress_domin_2_17_03b_02
                            if countdown > 8:
                                show pgn_dreams_mommaid_undress_domin_2_17_03b_03
                            mom emo-71 "Мммм... Ааххх!"
                            menu:
                                "Ещё раз":
                                    $ countdown += 1
                                    jump pgn_dreams_mommaid_undress_punish_ass_2
                                "Стимуляция анала" if countdown > 4:
                                    m emo-4 "Отлично! Попка готова к продолжению."
                                    scene pgn_dreams_mommaid_undress_domin_2_18
                                    m emo-3 "Мммм... Румяные булочки."
                                    scene pgn_dreams_mommaid_undress_domin_2_19
                                    $ renpy.pause()
                                    scene pgn_dreams_mommaid_undress_domin_2_20
                                    mom emo-68 "Ааххх!"
                                    scene pgn_dreams_mommaid_undress_domin_2_21
                                    $ renpy.pause()
                                    scene pgn_dreams_mommaid_undress_domin_2_22
                                    mom emo-68 "Ах... Аааахх! Ах... Аааахх!"
                                    scene pgn_dreams_mommaid_undress_domin_2_23
                                    m emo-4 "Стони! Я знаю, тебе нравится. Я не перестану, пока ты не кончишь."
                                    scene pgn_dreams_mommaid_undress_domin_2_24
                                    mom emo-68 "Ах... Аааахх! Ах... Аааахх!"
                                    scene pgn_dreams_mommaid_undress_domin_2_25
                                    $ renpy.pause()
                                    scene pgn_dreams_mommaid_undress_domin_2_26
                                    mom emo-66 "Ааааааааа!!!"
                                    scene pgn_dreams_mommaid_undress_domin_2_27
                                    mom emo-68 "Аааахх!"
                                    scene pgn_dreams_mommaid_undress_domin_2_end_02
                                    $ renpy.pause()
        "Киска":
            $ countdown = 1
            scene pgn_dreams_mommaid_undress_domin_2_05
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_06
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_07
            m emo-4 "Нравится, когда тебя трогают за киску?"
            mom emo-67 "Да."
            scene pgn_dreams_mommaid_undress_domin_2_08
            m emo-3 "Очень хорошо. Твой клитор набух и готов."
            mom emo-75 "..."
            scene pgn_dreams_mommaid_undress_domin_2_09
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_10
            mom emo-68 "Ааххх!"
            label pgn_dreams_mommaid_undress_punish_pussy:
                scene pgn_dreams_mommaid_undress_domin_2_11_01
                if countdown == 1:
                    m emo-3 "Тебе нравится?"
                elif countdown == 2:
                    m emo-4 "Стони, Мама!"
                elif countdown == 3:
                    m emo-11 "Я не слышу. Громче!"
                elif countdown == 4:
                    m emo-12 "Ну же сучка. Кричи!"
                else:
                    $ renpy.pause()
                scene pgn_dreams_mommaid_undress_domin_2_11_02a
                if countdown == 1:
                    mom emo-68 "Да!"
                elif countdown == 2:
                    mom emo-73 "Ах..."
                elif countdown == 3:
                    mom emo-68 "Аааххх..."
                elif countdown == 4:
                    mom emo-68 "Ааааахххх!"
                else:
                    mom emo-68 "Ааааааааааа!!!"
                scene pgn_dreams_mommaid_undress_domin_2_12
                if countdown > 3:
                    show pgn_dreams_mommaid_undress_domin_2_12_red
            menu:
                "Шлепнуть":
                    $ countdown += 1
                    jump pgn_dreams_mommaid_undress_punish_pussy
                "Закончить":
                    scene pgn_dreams_mommaid_undress_domin_2_end_01
                    if countdown > 3:
                        show pgn_dreams_mommaid_undress_domin_2_end_01_red
                    $ renpy.pause()
        "Ногой на лицо":
            scene pgn_dreams_mommaid_undress_domin_2_28
            m emo-0 "Вставай раком на пол."
            mom emo-75 "Слушаюсь."
            scene pgn_dreams_mommaid_undress_domin_2_29
            m emo-0 "Живее!"
            scene pgn_dreams_mommaid_undress_domin_2_30
            mom emo-67 "Хорошо."
            scene pgn_dreams_mommaid_undress_domin_2_31
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_32
            m emo-0 "Послушная киска. А сейчас..."
            scene pgn_dreams_mommaid_undress_domin_2_33
            mom emo-68 "Ааахх!"
            scene pgn_dreams_mommaid_undress_domin_2_34
            m emo-3 "Знай своё место, шлюшка!"
            scene pgn_dreams_mommaid_undress_domin_2_35
            mom emo-69 "Да, господин."
            scene pgn_dreams_mommaid_undress_domin_2_36
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_37
            $ renpy.pause()
            scene pgn_dreams_mommaid_undress_domin_2_38
            $ renpy.pause()
            jump pgn_dreams_mommaid_undress_punish_m1

    $ label_random.append("наказание")
    call mommaid_dress_end from _call_mommaid_dress_end_7
    call screen choice_mommaid_undress

label mommaid_dress_end:
    $ scene_random = []
    if renpy.loadable ("VaDX.rpy"):
        pass
    elif len(label_random) > 2 and pgn_ach_repeat == 0:
        scene black with dissolve
        $ renpy.pause(2)
        jump loc_my_room_sleep_02_dreamsnext
    elif len(label_random) > 3 and pgn_ach_repeat != 0:
        jump table_pgn_achievement
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
