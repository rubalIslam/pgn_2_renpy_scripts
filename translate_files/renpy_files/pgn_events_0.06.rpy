







label pgn_aptkira_dinner:
    scene pgn_dinner_kira_01_vadx
    mom emo-60 "[pname_kira[0]], неожиданно тебя видеть с нами за ужином, что-то случилось? Плохое или хорошее?"
    k emo-114 "Хорошее... За мою хорошую работу, компания приобрела мне квартиру."
    m emo-4 "У тебя появилась собственная квартира?"
    k emo-113 "Технически пока она не моя, а компании. И если и далее буду так хорошо работать, то она обязательно станет моей."
    l emo-41 "Тётя, а где ты работаешь?"
    mom emo-68 "..."
    k emo-101 "В сфере развлечений. Придумываю сценарии и устраиваю мероприятия."
    l emo-41 "Понятно. Видимо компания успешная и работает с состоятельными людьми, раз может позволить себе купить квартиру."
    mom emo-60 "А где она находится, квартира, далеко от нас?"
    k emo-101 "Нет, не так уж и далеко, рядом с пляжем. И..."
    k emo-101 "И, я там ещё не была, буквально недавно сообщили."
    a emo-24 "Очень хочется увидеть."
    k emo-113 "Мне тоже... И да, [pname_max[0]], у меня есть для тебя подарочек."
    m emo-4 "Ваау, круто!!!"
    mom emo-60 "[pname_kira[0]], не надо делать ему дорогие подарки, пусть сам зарабатывает."
    k emo-113 "[pname_mom[6]], всё хорошо. Скажем так, он и так на него заработал. Только, подарок прибудет завтра, утром."
    $ kira_path = 4
    if pornstudio_path == 5:
        k emo-101 "[pname_max[0]], останься пожалуйста, нужно поговорить."
    $ qtime += 1
    jump loc_veranda


label pgn_aptkira_pornbonus:
    m emo-3 "Отдыхаешь?"
    if daysn < 6:
        k emo-101 "Да. Твоя сестра очень вкусно готовит. Так наелась, что и двигаться не могу."
    if daysn == 6 or daysn == 7:
        k emo-101 "Да. Твоя мама очень вкусно готовит. Так наелась, что и двигаться не могу."
    k emo-100 "[pname_max[0]], мне нужно тебе сообщить ещё одну хорошую новость."
    $ scenevar("kira_veranda_evedial")
    k emo-113 "Я тебе как-то говорила уже, что ты сейчас не можешь иметь контракт со студией. Поэтому не можешь получать проценты с продаж. Но я всё же поговорила с руководством и теперь я официально твой агент. И т.к. ты желаешь оставаться анонимным..."
    m emo-6 "Анонимным!?"
    k emo-105 "[pname_max[0]], ты уже забыл? Что будет, если узнают, что [pname_mom[7]] твоя настоящая Мама?"
    m emo-0 "Ах, да, точно."
    k emo-100 "Ну так вот, раз ты, мой клиент, и желаешь оставаться анонимным, то ты можешь получать максимум 10%% от максимальной оплаты за съёмку в фильме."
    k emo-100 "Т.е. если снялся успешно несколько раз в первом фильме, то максимум можешь получать по 50$ в неделю, если ещё успешно снимешься в 6 или 7, то дополнительно ещё 60$."
    m emo-4 "Круто!"
    k emo-100 "Но это только если в этих и других фильмах будешь говорить все правильные реплики, а не что придёт в голову."
    m emo-0 "Понял."
    $ pornstudio_path = 6
    k emo-101 "Не хочешь проводить свою любимую тётю до её новой квартиры?"
    $ menu_hbox = True
    menu:
        "Всегда готов.":
            k emo-101 "Отлично. Тогда одевайся. Я вызвала такси."
            jump pgn_aptkira_home_hotel
        "Не сегодня.":
            m emo-0 "Прости, сегодня не могу."
            k emo-100 "Ладно. Тогда может в другой день."
            $ qtime += 1
            jump loc_veranda

label pgn_aptkira_hotel_ivent01:
    scene pgn_aptkira_eventfirst_reception_01
    m emo-6 "Где это мы?"
    scene pgn_aptkira_eventfirst_reception_02_vezdessushij
    m emo-3 "{i}Тётя [pname_kira[0]] совсем не стыдится своего тело.{/i}"
    scene pgn_aptkira_eventfirst_reception_03_vezdessushij
    m emo-4 "{i}Короткая юбка и совсем без трусиков.{/i}"
    scene pgn_aptkira_eventfirst_reception_04_vezdessushij
    m emo-0 "А что мы делаем в отеле?"
    k emo-100 "Сядь на диван и подожди меня."
    scene pgn_hotel_reception_catrin_01
    catr emo-221 "Здравствуйте. Чем я могу вам помочь?"
    k emo-100 "Здравствуйте. Компания, в которой я работаю, приобрела на моё имя квартиру в вашем отеле."
    catr emo-221 "Назовите ваше имя."
    k emo-100 "[pname_kira[0]]."
    scene pgn_aptkira_eventfirst_reception_06_vezdessushij
    catr emo-220 "Хорошо. Сейчас посмотрим... Так..."
    scene pgn_hotel_reception_catrin_01
    catr emo-221 "Да, Мисс [pname_kira[0]], на ваше имя была приобретена квартира на предпоследнем этаже."
    scene pgn_aptkira_eventfirst_reception_05_vezdessushij
    k emo-100 "Можно вас о кое-чём попросить?"
    catr emo-221 "Конечно. Внимательно слушаю."
    scene pgn_aptkira_eventfirst_reception_07_vezdessushij
    m emo-0 "{i}Хм... шикарный холл для отеля. Только не видно никого из работников, кроме администратора. Даже носильщика нет.{/i}"
    scene pgn_aptkira_eventfirst_reception_08_vezdessushij
    m emo-0 "{i}Что-то она долго.{/i}"
    k emo-100 "[pname_max[0]]... [pname_max[7]]!!!"
    scene pgn_aptkira_eventfirst_reception_09_vezdessushij
    m emo-1 "О!"
    scene pgn_aptkira_eventfirst_reception_10_vezdessushij
    m emo-14 "Что это? Ключи?"
    k emo-101 "Да. Раз ты и вся семья помогали мне и приютили, будет честно, если этой квартирой сможете тоже пользоваться."
    m emo-3 "Спасибо."
    scene pgn_aptkira_eventfirst_reception_11_vezdessushij
    k emo-101 "Вставай, пошли. Посмотрим на мою... нашу новую квартиру."
    scene pgn_aptkira_eventfirst_reception_12_wd1_vezdessushij
    m emo-0 "Какой этаж?"
    k emo-100 "Предпоследний."
label pgn_aptkira_hotel_ivent02:
    scene pgn_aptkira_first_01_vezdessushij
    m emo-5 "Ух ты!"
    k emo-101 "Ну что ты встал, проходи, будь как дома, осмотрись."
    scene pgn_aptkira_bath_03
    m emo-0 "Мм... просторно, душевая и небольшая ванная."
    scene pgn_aptkira_liv_03
    m emo-0 "Гостиная, тоже не плохая. Большой диван, да и хороший вид из окна."
    scene pgn_aptkira_first_02_vezdessushij
    m emo-6 "Хм... интересные картины. А там что за дверью."
    scene pgn_aptkira_first_03_vezdessushij
    m emo-6 "Странно. Заперто. [pname_kira[0]], здесь дверь заперта!"
    scene pgn_aptkira_first_04_vezdessushij
    k emo-104 "Точно, заперто. Теперь ясно, почему она упомянула, что квартира ещё не до конца готова."
    m emo-0 "А что там?"
    k emo-100 "Не знаю. Может студия готовит какую-то особую комнату. Домашний кинотеатр или большой гардероб для всех моих вещей и тех что буду покупать в большом количестве... даже и не знаю."
    k emo-101 "Давай посмотрим, что у нас за другой дверью."
    scene pgn_aptkira_first_05_vezdessushij
    m emo-0 "Понятное дело, что спальня."
    k emo-106 "Моя спальня и моя личная кровать... как мягко... Аххх....."
    k emo-101 "Не хочешь остаться и посмотреть со мной какие-нибудь фильмы?"
    m emo-3 "Конечно хочу."
    k emo-101 "Тогда беги в ванную, а то за весь день наверное сильно запылился. А после я тогда."
    scene pgn_aptkira_first_06_vezdessushij
    m emo-5 "А может вместе?"
    k emo-100 "Не сейчас. Хорошо?"
    scene pgn_aptkira_first_07_vezdessushij
    m emo-15 "{i}Жаль. А тот тут много места для нас двоих. Ладно, нет, так нет.{/i}"
    scene pgn_aptkira_first_08
    $ renpy.pause ( 5, 0)
    scene pgn_aptkira_first_09_vadx
    $ renpy.pause ( 4, 0)
    scene pgn_aptkira_first_10_vadx
    $ renpy.pause ( 2, 0)
    scene pgn_aptkira_first_11_vadx
    $ renpy.pause ( 5, 0)
    scene pgn_aptkira_first_12_vadx
    m emo-9 "Аааа!!!"
    k emo-114 "Хахаха... [pname_max[0]], ну ты чего так испугался."
    m emo-0 "Это было очень неожиданно."
    m emo-3 "Ты передумала, вместе здесь... помоемся?"
    k emo-101 "Нет, не передумала, просто кто-то тут, как девочка долго моется. Давай, освобождай и включи что-нибудь интересное."
    m emo-0 "Ладно."
    scene pgn_aptkira_first_13_vadx
    m emo-0 "{i}Так много выбора, что даже и не знаю, что смотреть.{/i}"
    $ renpy.pause(3)
    m emo-6 "{i}Что она там так долго!?{/i}"
    scene pgn_aptkira_first_14_vadx
    k emo-101 "Я всё. Пришлось немного задержаться. Ну ты понимаешь, что нам, девушкам, нужно больше времени проводить в ванной."
    m emo-0 "Всё нормально."
    scene pgn_aptkira_first_15_vadx
    $ renpy.pause(4, hard=True)
    scene pgn_aptkira_first_16_vadx
    $ renpy.pause(4, hard=True)
label pgn_aptkira_hotel_ivent03:
    scene pgn_aptkira_first_17_vadx
    m emo-3 "Займёмся сексом?"
    k emo-101 "Да, идём в спальню."
    scene pgn_aptk_sex_bedr_01_vezdessushij
    m emo-3 "Я готов."
    if pgnach_97.aopen == False:
        $ PGN_Achadd(pgnach_97, 97)
    k emo-113 "Вижу. Но перед тем как начнём, я должна увлажнить твой большой инструмент."
    scene pgn_aptk_sex_bedr_bj_anim_01
    m emo-3 "{i}Прям уж так это нужно, сама наверное от предвкушения давно вся мокрая, просто соскучилась по чему-то большому во рту.{/i}"
    scene anim pgn_hotel_aptkira_bedroom_bj
    m emo-7 "О да... О... О..."
    m emo-10 "{i}Как же хорошо она сосёт... Продержусь ли я так.{/i}"
    scene pgn_aptk_sex_bedr_03_vezdessushij
    k emo-101 "Отлично! Теперь трахни меня в киску!"
    m emo-4 "С удовольствием."
    scene anim pgn_hotel_aptkira_bedroom_vag
    k emo-103 "Да... Да.. [pname_max[0]]... Аххх..."
    k emo-113 "Глубже мой сладенький... Аххх... Ааааххх..."
    m emo-4 "Стараюсь, как могу."
    k emo-113 "Только не смей кончать, моя попка нуждается в твоём могучем инструменте."
    m emo-3 "Хорошо."
    scene pgn_aptk_sex_bedr_07_vezdessushij
    k emo-101 "Тебе там удобно?"
    m emo-3 "Пойдёт."
    $ anim_speed = 0.07
    scene anim pgn_hotel_aptkira_bedroom_anal_1
    k emo-112 "Не торопись... вот так... хорошо... Мммм..."
    $ anim_speed = 0.03
    scene anim pgn_hotel_aptkira_bedroom_anal_1
    k emo-114 "Ахх, [pname_max[0]]... ускорься и давай глубже... Засади своей тёте по самые..."
    m emo-10 "{i}Чёрт! Я уже еле-еле сдерживаюсь...{/i}"
    scene pgn_aptk_sex_bedr_09_vezdessushij
    m emo-12 "Аргх... Аааа...."
    scene pgn_aptk_sex_bedr_10_vezdessushij
    m emo-4 "Тётя, ты супер!"
    k emo-114 "Ох, чтобы мы вытворяли, если бы встретила тебя ещё раньше, чем бы только не занимались. Ты молодец, [pname_max[0]]!"
    k emo-101 "Я в душ, потом спать."
    m emo-4 "Ок."
    if pgn_ach_repeat == 97:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_kira, 1, 0, 1, 1, 0)
    $ serialpgngame("loc_hotel_aptkira_sleep")
label pgn_aptkira_hotel_ivent_end:
    $ kira_path = 5
    scene pgn_aptkira_bedr_sleep_maxkira_01_vadx
    $ renpy.pause ( 4, hard=True)
    scene pgn_aptkira_bedr_sleep_maxkira_02_vadx with dissolve
    m emo-7 "{i}Ммм... уже утро... Ох... попка тёти так близка... горячая и сексуальная... Ой!{/i}"
    k emo-106 "[pname_max[0]], уже проснулся? Не хотела тебя будить, думала ты всё ещё спишь."
    m emo-3 "Может?"
    k emo-101 "Как бы я ни хотела, но нам нужно вставать и успеть к завтраку, а то твоя мама будет ругать."
    m emo-0 "Ладно."
    $ PGN_Moveement_events (0, 6, "такси", 9)
    scene bg veranda_breakfast_01
    mom emo-60 "Где вы двое были?"
    m emo-0 "А... я проводил Тётю [pname_kira[3]] до её квартиры..."
    k emo-101 "[pname_mom[6]], квартира отличная. Посмотрели фильм, но было уже слишком поздно, так что остались там на ночь."
    mom emo-60 "Ясно."
    l emo-49 "Тёть [pname_kira[6]], а ты теперь там будешь жить?"
    k emo-101 "Никуда я от вас не уеду мои любимые, с вами куда интересней, чем быть одной в большой квартире."
    $ qtime = 10
    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[3])+": "+str(varlang[16]))
    if daysn == 1:
        call max_billscore from _call_max_billscore_1
    if kira_path >= 4 and transport3.buy == False:
        jump pgn_aptkira_max_scouter
    jump loc_veranda

label pgn_aptkira_max_scouter:
    k emo-101 "Ну так что, [pname_max[0]], готов, увидеть свой подарок?"
    if kira_path == 4:
        l emo-41 "Он ждет не дождется этого с вечера."
    m emo-3 "Да."
    k emo-101 "Тогда оденьтесь и пойдем на улицу."
    scene pgn_aptkira_max_scouter_001
    m emo-12 "Вау!!! Это скутер!!!"
    k emo-101 "Теперь у тебя есть свой транспорт и не ожидая на остановках общественный, езди куда и когда захочется."
    scene pgn_aptkira_max_scouter_002
    mom emo-69 "Он наверное дорогой."
    k emo-101 "[pname_mom[6]], да брось ты. [pname_max[0]] это заслужил. И скутеры не так дорого стоят."
    l emo-46 "А что он такого сделал, что получил такой подарок?"
    k emo-111 "Я... эм... с некоторой работой не могу управиться, поэтому прошу помочь [pname_max[1]]. В моей работе [pname_max[0]] занимает важную роль."
    scene pgn_aptkira_max_scouter_003
    a emo-22 "Прокатишь сестренку?"
    m emo-0 "Может быть... Мне хотя бы привыкнуть и научиться хорошо ездить, тогда и прокачу."
    mom emo-69 "Только не разгоняйся сильно, езди аккуратно. А шлем у тебя есть?"
    k emo-108 "Ой, забыла купить."
    m emo-6 "Эм... У меня есть кое-что в моей комнате. Сейчас, приду..."
    scene pgn_aptkira_max_scouter_004_vadx
    m emo-4 "Вот! Ну как?"
    l emo-41 "[pname_max[0]]..."
    m emo-2 "Что?!"
    mom emo-60 "А он защитит твою и так испорченную голову?"
    k emo-101 "Пока не будет у него нормального шлема, это пойдет. Так что езди осторожно. Не заставляй свою маму сильно волноваться."
    m emo-3 "Хорошо. Спасибо тебе большое, Тёть [pname_kira[6]]."
    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[14])+": "+str(transport3.name))
    $ garage_home.append(transport3)
    $ transport3.buy = True
    jump loc_garage

label pgn_hotel_aptkira_sex_kira:
    scene pgn_aptkira_eventfirst_reception_12_wd1_vezdessushij
    $ scenevar("кира-сексночь-лифт")
    $ renpy.pause ( 2, hard=True)
    $ scenevar("кира-сексночь-прихожая")
    k emo-101 "Напоминать думаю не нужно?"
    m emo-0 "Да, я понял. Сначала в душ, а всё остальное потом."
    k emo-101 "Умница."
label pgn_hotel_aptkira_sex_kira_next:
    scene pgn_aptkira_first_08
    $ renpy.pause ( 3, hard=True)
    scene pgn_aptkira_first_13_vadx
    $ renpy.pause ( 4, hard=True)
    scene pgn_aptkira_first_14_vadx
    k emo-101 "Вот и я. Для разогрева хотела бы посмотреть романтический фильм. Если ты конечно не против."
    m emo-4 "Если ты так этого хочешь, ладно."
    scene pgn_aptkira_first_15_vadx
    $ renpy.pause ( 5, hard=True)
    scene pgn_aptkira_first_16_vadx
    m emo-4 "{i}Хех... кто-то уже готов для продолжения.{/i}"
    scene pgn_aptkira_first_17_vadx
    k emo-109 "Чего хочется моему любимому племяннику? Может быть хочешь минета или перейдем в спальню?"
    menu:
        "Минет":
            pass
        "В спальню":
            jump pgn_hotel_aptkira_sex_kira_bedroom
        "Выбирай сама, я на всё согласен":
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random != 3:
                k emo-101 "Иди за мной."
                jump pgn_hotel_aptkira_sex_kira_bedroom
            if label_random == 3:
                $ label_random = 0
                k emo-101 "Тогда..."
                pass
label pgn_hotel_aptkira_sex_kira_bj:
    scene pgn_hotel_aptkira_livroom_bj_01_vezdessushij
    m emo-3 "Только я не просто минет хочу."
    k emo-114 "Да? А чего тебе хочется?"
    m emo-4 "Хочу трахнуть твоё горло."
    k emo-102 "Мммм... Я не против."
    scene pgn_hotel_aptkira_livroom_bj_kira_anim_01
    m emo-4 "{i}Боже! Какая же всё же тётя сексуальная. Хоть бы не кончить сразу от такой красоты.{/i}"
    if pgnach_98.aopen == False:
        $ PGN_Achadd(pgnach_98, 98)
    m emo-3 "Я начинаю..."
    $ anim_speed = 0.05
    scene anim pgn_hotel_aptkira_livroom_bj_kira
    m emo-7 "О да, вот так... ох... {i}У тёти очень глубокая глотка.{/i}"
    m emo-4 "{i}Пора бы и ускориться...{/i}"
    $ anim_speed = 0.03
    scene anim pgn_hotel_aptkira_livroom_bj_kira
    m emo-7 "{i}Ещё немного...{/i}"
    scene pgn_hotel_aptkira_livroom_bj_02_vezdessushij
    m emo-12 "Ааааххх.... Да..."
    scene pgn_hotel_aptkira_livroom_bj_03_vezdessushij
    k emo-101 "Вот это да, [pname_max[0]], ты молодец."
    if pgn_ach_repeat == 98:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_kira, 0, 0, 1, 0, 0)
    $ label_random, location = renpy.random.randint ( 1, 4), "loc_hotel_aptkira"
    if label_random == 4:
        k emo-113 "Силы ещё остались? Продолжим в спальне или хочешь уже спать?"
        $ menu_hbox = True
        menu:
            "Продолжим":
                scene pgn_aptk_sex_bedr_01_vezdessushij
                k emo-101 "И так. Куда хочешь трахнуть свою тётю?"
                jump menu_1_pgn_hotel_aptkira_sex_kira_bedroom
            "Спать":
                $ accessiv.append("kira_aptsex_sleep_bedr")
                $ serialpgngame("loc_hotel_aptkira_sleep")
    $ accessiv.append("kira_aptsex_sleep_livr")
    $ serialpgngame("loc_hotel_aptkira_sleep")

label pgn_hotel_aptkira_sex_kira_bedroom:
    scene pgn_aptk_sex_bedr_bj_anim_01
    k emo-102 "Начнём сначала с этого..."
    scene anim pgn_hotel_aptkira_bedroom_bj
    $ renpy.pause()
    m emo-10 "{i}Класс...{/i}"
    scene pgn_aptk_sex_bedr_bj_anim_01
    k emo-101 "Достаточно. Мне не нужно, чтобы ты ещё кончил так рано."
    $ PGN_Addstatsex(stat_kira, 0, 0, 1, 0, 0)
    scene pgn_aptk_sex_bedr_03_vezdessushij
    k emo-101 "Так, чего тебе сейчас больше всего хочется?"
    m emo-5 "Даже и не знаю."
    scene pgn_aptk_sex_bedr_01_vezdessushij
    k emo-102 "Хм... Может хорошенько рассмотришь меня и подумаешь, куда хочешь всунуть своего крепыша."
    menu menu_1_pgn_hotel_aptkira_sex_kira_bedroom:
        "В киску":
            jump pgn_hotel_aptkira_sex_kira_bedroom_vaginal
        "В анал":
            jump pgn_hotel_aptkira_sex_kira_bedroom_anal
label pgn_hotel_aptkira_sex_kira_bedroom_vaginal:
    scene anim pgn_hotel_aptkira_bedroom_vag
    k emo-103 "Да, вот так, так [pname_max[0]]. Не торопись."
    k emo-106 "Ммм..."
    k emo-112 "Продолжай..."
    m emo-13 "Больше не могу... сейчас кончу..."
    menu:
        "Кончить внутрь":
            scene pgn_aptk_sex_bedr_vag_anim_15
            $ renpy.pause(2, hard=True)
            scene pgn_aptk_sex_bedr_vag_anim_09
            $ renpy.pause(1, hard=True)
            scene pgn_aptk_sex_bedr_vag_anim_15
            $ renpy.pause(3, hard=True)
            scene pgn_aptk_sex_bedr_vag_anim_01
            k emo-104 "Хотя бы спросил, принимала ли противозачаточные?"
            m emo-9 "Аааа... что делать?"
            k emo-114 "Расслабься, я же не дура, знаю, что тебе иногда так и хочется наполнить меня всю."
            k emo-101 "Хорошо. Я в душ, потом спать."
            m emo-3 "Ок."
        "Кончить на сиськи":
            scene pgn_aptk_sex_bedr_05_vezdessushij
            m emo-12 "Аргх... Ааааххх... Чёрт! Да!"
            scene pgn_aptk_sex_bedr_06_vezdessushij
            k emo-113 "Всю меня испачкал... Мммм... Я в душ и спать."
    $ accessiv.append("kira_aptsex_sleep_bedr")
    $ PGN_Addstatsex(stat_kira, 0, 0, 0, 1, 0)
    $ serialpgngame("loc_hotel_aptkira_sleep")

label pgn_hotel_aptkira_sex_kira_bedroom_anal:
    $ anim_speed = 0.07
    scene anim pgn_hotel_aptkira_bedroom_anal_1
    k emo-112 "Ахххх... Ммм... Какой большой..."
    $ renpy.pause()
    menu menu_2_pgn_hotel_aptkira_sex_kira_bedroom:
        "Ускорить" if anim_speed > 0.03:
            $ anim_speed -= 0.02
            scene anim pgn_hotel_aptkira_bedroom_anal_1
            $ renpy.pause()
            jump menu_2_pgn_hotel_aptkira_sex_kira_bedroom
        "Замедлить":
            $ anim_speed += 0.02
            scene anim pgn_hotel_aptkira_bedroom_anal_1
            $ renpy.pause()
            jump menu_2_pgn_hotel_aptkira_sex_kira_bedroom
        "Далее":
            pass
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random == 3:
        scene pgn_aptk_sex_bedr_09_vezdessushij
        m emo-12 "Аргх... Аааа...."
        scene pgn_aptk_sex_bedr_10_vezdessushij
        k emo-101 "А так надеялась, что продержишься ещё немного"
        m emo-0 "Прости... я..."
        k emo-109 "Не переживай. В душ и спать?"
        m emo-0 "Да"
    else:
        k emo-106 "Аааххх... Ааахх... [pname_max[0]]... Глубже... Ещё глубже...."
        $ anim_speed = 0.05
        scene anim pgn_hotel_aptkira_bedroom_anal_2
        k emo-114 "Не останавливайся... глубже мой племянник... Аааххх..."
        menu menu_3_pgn_hotel_aptkira_sex_kira_bedroom:
            "Ускорить" if anim_speed > 0.03:
                $ anim_speed -= 0.02
                scene anim pgn_hotel_aptkira_bedroom_anal_2
                $ renpy.pause()
                jump menu_3_pgn_hotel_aptkira_sex_kira_bedroom
            "Замедлить":
                $ anim_speed += 0.02
                scene anim pgn_hotel_aptkira_bedroom_anal_2
                $ renpy.pause()
                jump menu_3_pgn_hotel_aptkira_sex_kira_bedroom
            "Кончить":
                pass
        scene pgn_aptk_sex_bedr_anal_2_anim_12
        m emo-12 "Аргхх... Аааа... Аааа..."
        scene pgn_aptk_sex_bedr_12_vezdessushij
        k emo-103 "[pname_max[0]], [pname_max[0]]..."
        k emo-103 "Ты мой сладенький, выбился из сил и уснул."
    $ PGN_Addstatsex(stat_kira, 1, 0, 0, 0, 0)
    $ accessiv.append("kira_aptsex_sleep_bedr")
    $ serialpgngame("loc_hotel_aptkira_sleep")

label pgn_hotel_aptkira_sex_sleep_01:
    scene pgn_aptkira_bedr_sleep_maxkira_01_vadx
    $ renpy.pause ( 4, 0)
    scene pgn_aptkira_bedr_sleep_maxkira_02_vadx with dissolve
    k emo-106 "[pname_max[0]], пора уже вставать. Давай, нужно ехать."
    m emo-10 "Мам, ещё 5 минут."
    k emo-104 "Сейчас за маму получишь. Подъём!!!"
    m emo-10 "Да, да... встаю."
    $ PGN_Moveement_events (0, 6, "такси", 9)
    call next_time_days from _call_next_time_days
    jump veranda_breakfast

label pgn_hotel_aptkira_sex_sleep_02:
    scene pgn_aptkira_liv_sleep_max_01_vadx with dissolve
    k emo-100 "[pname_max[0]], просыпайся! Одевайся и поехали домой."
    m emo-13 "{i}Блин, уснул...{/i}"
    $ PGN_Moveement_events (0, 6, "такси", 9)
    call next_time_days from _call_next_time_days_1
    jump veranda_breakfast








label pgn_aptkira_home_hotel_liza:
    scene pgn_aptkira_hometohotel_liza_01_vadx
    m emo-8 "Блин. Где же они!?"
    l emo-48 "[pname_max[0]]?"
    m emo-0 "[pname_liza[0]], ты не видела мои штаны?"
    scene pgn_aptkira_hometohotel_liza_02_vadx
    l emo-41 "А можно... ну это... С вами поехать?"
    m emo-0 "Не знаю. Нужно спросить."
    scene pgn_aptkira_hometohotel_liza_03_vadx
    l emo-41 "Спросишь?"
    m emo-8 "Где мои штаны? Такси уже скоро приедет."
    l emo-40 "На кровати лежат."
    scene pgn_aptkira_hometohotel_liza_02_vadx
    m emo-3 "Точно. Сразу не увидел."
    l emo-49 "Ну так, ты спросишь у неё? Можно ли мне с вами."
    m emo-0 "В другой раз, [pname_liza[0]], в другой раз."
    l emo-49 "Пожалуйста. Я тоже очень хочу с вами повеселиться. [pname_max[0]]!"
    m emo-3 "Потом."
    return


label pgn_aptkira_home_hotel:
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random == 2 and ("kira_aptsex") in ivent24:
        call pgn_aptkira_home_hotel_liza from _call_pgn_aptkira_home_hotel_liza
        scene pgn_aptkira_hometohotel_liza_05_vadx
        if ("kira_aptsex_wd_02") in ivent24:
            show pgn_aptkira_hometohotel_liza_wd2
        $ renpy.pause(3, hard=True)
    scene pgn_aptkira_hometohotel_liza_04_vadx
    if label_random != 2:
        show pgn_aptkira_hometohotel_without_liza
    if ("kira_aptsex_wd_02") in ivent24:
        show pgn_aptkira_hometohotel_wd2
    $ renpy.pause(2)
    $ PGN_Moveement_events (0, 6, "такси")
    if kira_path == 4:
        jump pgn_aptkira_hotel_ivent01
    if kira_path >= 5:
        jump pgn_hotel_aptkira_sex_kira







label pgn_kiraaptsex_verandahome_v1:
    scene pgn_home_v_kiraaptsex_wd2_02_vadx
    m emo-3 "{i}О! Какая попка.{/i}"
    menu menu_1_pgn_kiraaptsex_verandahome_v1:
        "Поговорить":
            pass
        "Подойти ближе":
            scene pgn_home_v_kiraaptsex_wd2_01_vadx
            m emo-3 "{i}Медленно и незаметно.{/i}"
            scene pgn_home_v_kiraaptsex_wd2_04_vadx
            m emo-4 "{i}Отличный вид. Сейчас бы её здесь и на столе.{/i}"
            menu:
                "Поговорить":
                    pass
                "Ещё ближе":
                    scene pgn_home_v_kiraaptsex_wd2_06_vadx
                    $ renpy.pause(2)
                    scene pgn_home_v_kiraaptsex_wd2_07_vadx
                    $ renpy.pause(2)
                    scene pgn_home_v_kiraaptsex_wd2_08_vadx
                    k emo-108 "О! Что это такое большое и толстое уперлось в мою попу?"
                    m emo-4 "Этой мой член."
                    scene pgn_home_v_kiraaptsex_wd2_09_vadx
                    k emo-103 "Я так и поняла. В этом доме только у тебя одного есть эта штуковина."
                    k emo-101 "Поедешь с любимой тётей? По приезду... помогу тебе."
                    menu:
                        "Хорошо":
                            jump pgn_aptkira_home_hotel
                        "Не знаю даже":
                            m emo-0 "Даже и не знаю, ехать или нет."
                            k emo-104 "Уговаривать не буду. Так что решай."
                            menu:
                                "Ладно":
                                    jump pgn_aptkira_home_hotel
                                "Не сегодня":
                                    m emo-0 "Прости, но не сегодня."
                                    k emo-100 "Жаль. Как хочешь."
                                    $ qtime += 1
                                    jump loc_veranda
        "Наблюдать" if ("menu_pgn_kiraaptsex_verandahome_v1_3") not in ivent24:
            $ ivent24.append("menu_pgn_kiraaptsex_verandahome_v1_3")
            scene pgn_home_v_kiraaptsex_wd2_02_vadx
            m emo-6 "{i}Что она делает?{/i}"
            scene pgn_home_v_kiraaptsex_wd2_03_vadx
            m emo-4 "{i}Разминается, как будто готовится к пробежке или типа того.{/i}"
            jump menu_1_pgn_kiraaptsex_verandahome_v1
    scene pgn_home_v_kiraaptsex_wd2_01_vadx
    m emo-0 "[pname_kira[0]]"
    scene pgn_home_v_kiraaptsex_wd2_05_vadx
    k emo-102 "Скорее одевайся и поехали в отель, а то я долго ждать не буду."
    menu:
        "В путь":
            jump pgn_aptkira_home_hotel
        "Уже не хочется":
            m emo-0 "Я уже не уверен, что хочу ехать."
            k emo-103 "А что так?"
            scene anim pgn_kiraaptsex_verandahome_v1_01
            k emo-104 "Моему любимому племяннику больше не нравится эта попка!?"
            k emo-104 "Хорошенько подумай."
            menu:
                "Уже бегу одеваться":
                    jump pgn_aptkira_home_hotel
                "Ну не знаю":
                    m emo-3 "Твоя попка классная. Просто не хочется куда-то ехать."
            scene pgn_home_v_kiraaptsex_wd2_anim1_01
            k emo-101 "Как жаль. А то она такая упругая и нуждается в сильной хватке мужчины."
            scene anim pgn_kiraaptsex_verandahome_v1_02
            k emo-106 "Ммм..."
            k emo-102 "Да, вот так..."
            scene pgn_home_v_kiraaptsex_wd2_anim2_01
            k emo-109 "Ну, [pname_max[0]]. Последний раз предлагаю. Поедем или нет?"
            menu:
                "Уговорила":
                    m emo-4 "Умеешь уговаривать."
                    k emo-101 "Вот и отлично. Давай, бегом в комнату и поехали."
                    jump pgn_aptkira_home_hotel
                "Извини, но нет":
                    m emo-0 "Прости, но не сегодня."
                    k emo-100 "Жаль. Как хочешь."
                    $ qtime += 1
                    jump loc_veranda
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
