






label frederi_autosalon_dialogue_driver_license_no:
    m emo-13 "И о чем мне с менеджером разговаривать. Если у меня прав водительских нет."
    jump loc_autosalon_consult


label pgn_road_rules_frederico:
    $ ivent24.append("Road rules")
    if qtime >= 6 and qtime <= 16:
        scene pgn_maxcompsits_01
    if qtime >= 17 and qtime <= 19:
        scene pgn_maxcompsits_01
    if (qtime >= 0 and qtime <= 3) or (qtime >= 21 and qtime <= 23):
        scene pgn_maxcompsits_03
    $ qtime += 2
    if qtime == 24:
        $ daysnchange()
    if qtime > 24:
        $ qtime -= 24
        $ daysnchange()
    $ renpy.pause (5, hard=True)
    $ frederico_path += 0.1
    jump loc_my_room


label pgn_frederico_driving_practice:
    $ ivent24.append("max_driving_practice")
    m emo-3 "Привет Мам. Я готов к практике."
    mom emo-62 "Хорошо. Иди одевайся и жди меня у гаража. Мне нужно переодеться."
    if frederico_path == 0.6:
        scene pgn_max_driving_practice_01
        $ renpy.pause(3,0)
        scene pgn_max_driving_practice_02
        mom emo-68 "В спешке забыла трусики надеть. А ну и ладно, мне же не придётся юбку снимать."
        scene pgn_max_driving_practice_03
        m emo-4 "Мама. Ты отлично выглядишь!"
        mom emo-79 "Спасибо. Я же должна выглядеть соответствующе. Пойдём."
    scene pgn_max_driving_practice_04
    mom emo-77 "Минуточку. Приберусь немного."
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random == 1:
        m emo-4 "{i}Класс! Вот это попка.{/i}"
    if label_random == 2:
        m emo-6 "{i}А может сегодня не будем практиковаться в вождении. А по-практикуем в чём-нибудь другом.{/i}"
    if label_random == 3:
        m emo-3 "{i}Может быть...{/i}"
    mom emo-77 "Всё, готово, садись."
    if frederico_path >= 1.5:
        m emo-0 "Может я сяду за руль?"
        mom emo-78 "Вот когда получишь права, тогда сядешь. Я буду за рулём, пока не выедем за территорию города."
    scene pgn_max_driving_practice_05
    menu:
        "Достать член":
            m emo-4 "Мама, может ты покажешь мне свои навыки в кое-чём другом?"
            scene pgn_max_driving_practice_05b
            mom emo-77 "[pname_max[0]]! Убери! Давай лучше продолжим твою учёбу."
            menu:
                "Ладно":
                    pass
                "Проблема, есть проблема":
                    m emo-2 "Я не смогу нормально учиться, когда вся кровь ушла вниз."
                    m emo-2 "Может поможешь мне сейчас с этой проблемой?"
                    mom emo-60 "Не хочешь, как хочешь. Свою проблему можешь решить в душе."
                    jump loc_pool
        "Лучше продолжить занятия":
            pass
    scene pgn_max_driving_practice_06
    mom emo-77 "Ну, поехали."
    scene pgn_max_driving_practice_06
    scene black with dissolve
    $ renpy.pause(5)
    scene pgn_max_driving_practice_06 with dissolve
    mom emo-79 "Надеюсь ты запомнил всё что сегодня прошли."
    m emo-3 "Конечно. Ты же меня знаешь."
    $ frederico_path += 0.1
    $ qtime += 2
    jump loc_pool


label pgn_frederico_driving_test:
    if frederico_path >= 0.7 and frederico_path < 1:
        $ label_random = renpy.random.randint ( 1, 5)
    if frederico_path >= 1 and frederico_path <= 1.5:
        $ label_random = renpy.random.randint ( 1, 4)
    if frederico_path >= 1.6 and frederico_path < 2:
        $ label_random = renpy.random.randint ( 1, 3)
    if frederico_path >= 2:
        $ label_random = 2
    scene pgn_max_driving_practice_07
    other emo-999 "Если хорошо подготовились к экзамену, то у вас не должно быть проблем. Удачи!"
    m emo-13 "Спасибо."
    scene pgn_max_driving_practice_07
    scene black with dissolve
    $ renpy.pause(3, hard=True)
    scene black
    if label_random != 2:
        scene pgn_max_driving_practice_08 with dissolve
        other emo-999 "Ничего страшного, попробуете в другой день."
        $ ivent24.append("max_driving_test")
        $ qtime += 2
    if label_random == 2:
        scene pgn_max_driving_practice_09 with dissolve
        m emo-3 "Да, я сдал. Теперь у меня есть права."
        $ accessiv.append("driver's license")
        $ qtime += 2
        $ frederico_path = 3
    jump loc_pool


label pgn_frederico_momcar_01:
    a emo-20 "Мам, а кто там приезжал к нам?"
    mom emo-60 "А это за машиной приезжали и отвезли в авто-мастерскую."
    m emo-0 "Сломалась?"
    mom emo-60 "Не думаю, что что-то серьёзное, но я давно стала замечать, что-то неладное. Решила перестраховаться."
    m emo-3 "Так у меня есть права, мог бы сам отвезти."
    mom emo-64 "[pname_max[0]]! Не хватало мне, чтобы ты ещё в аварию какую-то попал."
    a emo-22 "Ага. Права недавно получил и думаешь управишься с любой машиной."
    m emo-11 "..."
    mom emo-60 "И да, [pname_max[0]]. Можешь съездить и узнать на счёт ремонта машины?"
    m emo-0 "Хорошо, как будет время, съезжу."
    $ ivent24.append("momcar_fix_today")
    $ frederico_path = 3.5
    jump veranda_breakfast_next

label pgn_frederico_momcar_01b:
    mom emo-60 "[pname_max[0]]. Сегодня утром доставили машину, сообщили, что неисправность была несерьёзной."
    m emo-0 "Этой хорошо."
    mom emo-63 "Да, но я просила тебя съездить и узнать."
    a emo-21 "Он наверное только и рад тому, что никуда ездить не пришлось, т.к. его пятая точка присосалась к стулу."
    m emo-0 "Ха-ха"
    mom emo-60 "Только вот на счёт оплаты ничего не сказали. Очень странно."
    mom emo-64 "Так что, [pname_max[0]], съезди и узнай, что стоит ремонт."
    m emo-0 "Ладно"
    jump veranda_breakfast_next


label pgn_frederico_momcar_02:
    scene pgn_autosalon_visit_derector_01
    m emo-6 "{i}Странно, я тут впервые и сразу к директору...{/i}"
    scene pgn_autosalon_visit_derector_02
    ang emo-301 "Проходите, присаживайтесь."
    scene pgn_autosalon_visit_derector_03
    ang emo-301 "Здравствуйте. Я Анжелика Фредерико, директор компании \"Frederi\"."
    m emo-0 "Приятно познакомиться. Я [pname_max[0]]."
    menu:
        "Пялиться на её сиськи":
            $ accessiv.append("frederi_dialogue_boobs_1")
            scene pgn_autosalon_visit_derector_04
        "Ничего не делать":
            scene pgn_autosalon_visit_derector_03
    ang emo-301 "Я хочу вас поздравить. Вы у нас юбилейный клиент."
    if ("momcar_fix_today") in ivent24:
        ang emo-301 "Поэтому ремонт вашей машины обойдётся вам бесплатно."
    else:
        ang emo-301 "Поэтому ремонт был произведён абсолютно бесплатно."
    m emo-5 "Ого! Круто, спасибо. Но это не моя машина, а Мамы."
    m emo-1 "Своей у меня нет."
    ang emo-301 "Ничего страшного. Кроме того, что ремонт бесплатный, вы так же сможете купить у нас свою первую машину, со скидкой."
    ang emo-303 "Использовать скидку можете в любое время. Необязательно на первую покупку, можете приобрести со скидкой вторую машину, если пожелаете."
    m emo-3 "Спасибо."
    $ qtime += 1
    $ accessiv.append("frederi_discount")
    $ frederico_path = 4
    if ("momcar_fix_today") in ivent24:
        ang emo-301 "Сейчас можете спуститься вниз и вас дооформят."
        if label_random == "women":
            jump pgn_frederico_momcar_02_nextw
        if label_random == "men":
            jump pgn_frederico_momcar_02_nextm
    else:
        jump loc_autosalon_consult


label pgn_frederico_firstcar:
    $ ivent24.append("frederico_firstbuycar")
    if label_random == "women":
        scene pgn_autosalon_consult_woman_01
        other femo-11 "Хороший выбор"
        play sound "content/audio/call_me_maybe.mp3" noloop
        other femo-10 "Минуточку..."
        stop sound
        scene pgn_autosalon_consult_woman_02
        $ renpy.pause(3)
        scene pgn_autosalon_consult_woman_01
        other femo-11 "Не могли бы подняться в офис. У директора к вам несколько вопросов."
    if label_random == "men":
        scene pgn_autosalon_consult_man_01
        other femo-01 "Хороший выбор."
        scene pgn_autosalon_consult_man_02
        other femo-00 "..."
        other femo-00 "Извините за задержку. Технические проблемы."
        m emo-0 "Ладно, подожду"
        other femo-01 "Пока ждёте, поднимитесь на второй этаж. У директора к вам несколько вопросов."
    scene pgn_autosalon_visit_derector_02
    m emo-1 "Здравствуйте."
    ang emo-301 "[pname_max[0]], присаживайтесь. Я хочу задать вам несколько вопросов."
    scene pgn_autosalon_visit_derector_03
    menu:
        "Сиськи, сиськи":
            $ accessiv.append("frederi_dialogue_boobs_2")
            scene pgn_autosalon_visit_derector_04
        "Нет, нет":
            scene pgn_autosalon_visit_derector_03
    ang emo-301 "Вы где-нибудь сейчас учитесь, в школе или в колледже?"
    m emo-13 "Нет. Дома помогаю родным."
    scene pgn_autosalon_visit_derector_05
    ang emo-304 "О! Вы очень хозяйствены и наверное родные очень рады, что вы у них есть."
    m emo-4 "{i}Да, хозяйство у меня очень большое и ему они очень рады. Только к чему эти вопросы?{/i}"
    menu:
        "Продолжить смотреть на буфера":
            $ accessiv.append("frederi_dialogue_boobs_3")
            scene pgn_autosalon_visit_derector_06
        "Это уже через-чур":
            scene pgn_autosalon_visit_derector_07
    ang emo-301 "Что вас сподвигло купить свою машину? Как я помню, у вашей мамы есть машина."
    menu:
        "Скорость":
            m emo-4 "Хочу почувствовать скорость. Да и в машине побезопаснее, чем на скутере."
            ang emo-304 "Понятно"
            scene pgn_autosalon_visit_derector_08
        "Быть независимым":
            m emo-0 "Хочу быть самостоятельным. Поэтому решил начать с покупки своего личного автомобиля."
            m emo-0 "Потом может буду жить отдельно."
            ang emo-301 "Молодец."
            scene pgn_autosalon_visit_derector_08
        "Для семьи":
            m emo-0 "Не вечно же Маме нас возить, так и я могу помочь и часть обязанностей взять на себя."
            ang emo-301 "Это похвально"
    ang emo-301 "Где-нибудь работаете?"
    menu:
        "В кафе":
            ang emo-304 "О! И в кафе так много платят, что вам удалось накопить на машину!?"
        "Порнофильмы":
            ang emo-303 "Ммм... Ясно. И в каких фильмах можно увидеть ваш... вашу актёрскую игру?"
        "Актёр":
            ang emo-304 "Да? А в каких фильмах снимаетесь?"
    play sound "content/audio/confident.mp3" noloop
    scene pgn_autosalon_visit_derector_07
    if label_random == "men":
        ang emo-304 "Ой! Жаль, не хватило времени. Можете спуститься и завершить процедуру оформления."
    if label_random == "women":
        ang emo-304 "Ой! Жаль, не хватило времени. Можете спуститься и все документы готовы."
    m emo-0 "Конечно, спасибо."
    ang emo-303 "В следующий раз надеюсь у нас будет больше времени. Хочу побольше узнать о вас."
    if label_random == "women":
        scene pgn_autosalon_consult_woman_01
        other femo-11 "Вот ваши документы и ключи от новой машины. Будем рады снова видеть у нас."
    if label_random == "men":
        scene pgn_autosalon_consult_man_01
        other femo-01 "Извините за заминку. Вот ваши документы и ключи."
        m emo-3 "Спасибо."
    $ frederico_path = 5
    $ qtime += 1
    jump loc_autosalon_consult


label pgn_frederico_secondvisit:
    scene pgn_autosalon_privskype_01
    ang emo-300 "Он снова пришёл."
    scene pgn_autosalon_privskype_02
    other emo-998 "Когда ты уже сможешь посмотреть на него, в живую?"
    ang emo-303 "Он тебе понравился, что так неймётся узнать про его размеры?"
    other emo-998 "У него очень интересная семья, неудивительно, что они все без ума от него. Но хотелось бы знать, каков его монстр в реальности."
    ang emo-303 "А что тебе самой не пригласить его к себе или фильмы его не видела?"
    other emo-998 "Я не могу по экрану ТВ определить реальные размеры. И у меня не так много времени. Сама знаешь."
    ang emo-304 "Слабо верится, что ты не можешь определить. Из нас троих, только у тебя больше всего мужчин, было и есть."
    other emo-998 "Давай не будем мериться количеством."
    other emo-998 "Ну так, когда поделишься своими впечатлениями?"
    ang emo-300 "Не могу же я прям сейчас и просто так его снова затащить к себе, без повода."
    ang emo-304 "Может смогу, когда подумает о ещё одной покупке. Тогда хорошенько обслужу важного клиента."
    other emo-998 "Жду от тебя новостей."
    ang emo-300 "Пока."
    $ frederico_path = 6
    jump jump_dialogue


label pgn_frederico_secondcar:
    if label_random == "women":
        scene pgn_autosalon_consult_woman_01
        other femo-11 "Вас снова просят подняться наверх."
    if label_random == "men":
        scene pgn_autosalon_consult_man_01
        other femo-01 "Вас снова просят подняться наверх."
    m emo-13 "Опять!?"
    scene pgn_autosalon_secondvisit_01
    ang emo-301 "[pname_max[0]], здравствуйте. Спасибо, что пришли."
    m emo-13 "Снова вопросы будете задавать?"
    scene pgn_autosalon_secondvisit_02
    ang emo-303 "Есть один вопрос, что меня интересует. Подойдите ближе."
    scene pgn_autosalon_secondvisit_03
    ang emo-302 "Ближе! Я не кусаюсь."
    scene pgn_autosalon_secondvisit_04
    m emo-9 "О! Может не надо..."
    ang emo-301 "Пожалуйста. Удовлетворите любопытство зрелой и одинокой дамы."
    m emo-6 "{i}Она так всех клиентов обслуживает?{/i}"
    scene pgn_autosalon_secondvisit_05
    ang emo-304 "Ого! Вот это да, какой большой. {i}Она была права, у него большой.{/i}"
    scene pgn_autosalon_secondvisit_06
    $ renpy.pause(2)
    scene pgn_autosalon_secondvisit_07
    $ renpy.pause(2)
    scene pgn_autosalon_secondvisit_08
    ang emo-303 "Ммм..."
    m emo-3 "Извините..."
    ang emo-303 "Всё хорошо. Ложись на диван. {i}Надеюсь она сильно не разозлится, если я первой протестирую член этого мальчишки.{/i}"
    scene pgn_autosalon_secondvisit_09
    menu:
        "VIP Клиент":
            m emo-4 "Вы всех клиентов так обслуживаете?"
            ang emo-301 "Только самых важных."
            menu:
                "Мои условия":
                    m emo-4 "Тогда может лучше покажите свои прелести и займёмся сексом? Может даже добавлю сверху, к стоимости авто."
                    ang emo-304 "Ооо... А ты дерзкий паренёк."
                    ang emo-300 "Только... здесь условия задаю я. И если будешь продолжать ввести себя плохо, то охрана мигом выкинет из салона с голым задом и с приличным долгом на счёте."
                    if ("frederi_dialogue_boobs_1") in accessiv:
                        $ accessiv.remove("frederi_dialogue_boobs_1")
                    if ("frederi_dialogue_boobs_2") in accessiv:
                        $ accessiv.remove("frederi_dialogue_boobs_2")
                    if ("frederi_dialogue_boobs_3") in accessiv:
                        $ accessiv.remove("frederi_dialogue_boobs_3")
                    menu:
                        "Глубоко засунуть в горло":
                            scene pgn_autosalon_bj_bedend_01
                            ang emo-305 "Ты чего это задумал?"
                            m emo-12 "А я хочу так. Ротик шире открываем, глотай!"
                            scene pgn_autosalon_bj_bedend_02
                            m emo-10 "Соси, глотай, мне нужно кончить. Я VIP клиент, а клиент всегда прав, так что обслужи мой член хорошенько."
                            $ anim_speed = 0.05
                            scene animated pgn_autosalon_frederico_bj
                            $ renpy.pause()
                            menu menu_autosalon_bj_bedend:
                                "Пусть дальше сосёт":
                                    scene animated pgn_autosalon_frederico_bj2
                                    $ renpy.pause()
                                    jump menu_autosalon_bj_bedend
                                "Ускорить" if anim_speed > 0.03:
                                    $ anim_speed -= 0.02
                                    scene animated pgn_autosalon_frederico_bj2
                                    $ renpy.pause()
                                    jump menu_autosalon_bj_bedend
                                "Замедлить":
                                    $ anim_speed += 0.02
                                    scene animated pgn_autosalon_frederico_bj2
                                    $ renpy.pause()
                                    jump menu_autosalon_bj_bedend
                                "Кончить":
                                    scene pgn_autosalon_frederico_bj_bedend_15
                                    m emo-12 "Да... Класс! Глотай, глотай..."
                            scene pgn_autosalon_bj_bedend_03
                            ang emo-307 "Он.. он... он слишком большой."
                            m emo-4 "Понравилось? В другой раз повторим?"
                            scene pgn_autosalon_bj_bedend_04
                            ang emo-305 "Вот мелкий говнюк."
                            m emo-9 "Больно!"
                            ang emo-305 "Думаешь, купил у меня две машины, так теперь ты тут стал кем-то особенным."
                            ang emo-306 "Охрана!!!"
                            scene pgn_autosalon_bj_bedend_05
                            $ renpy.pause(2)
                            scene black with dissolve
                            $ renpy.pause(3)
                            scene pgn_autosalon_bj_bedend_06 with dissolve
                            $ renpy.pause(5)
                            scene pgn_autosalon_bj_bedend_07
                            m emo-9 "Где это я? И почему я голый!?"
                            scene pgn_autosalon_bj_bedend_08
                            m emo-13 "Дерьмо."
                            scene black with dissolve
                            $ renpy.pause(3)
                            $ renpy.full_restart()
                        "Смириться":
                            pass
                "Промолчать":
                    pass
        "Не спрашивать":
            pass
    $ frederico_path = 7
    m emo-13 "Если кто-то придёт..."
    ang emo-301 "Не переживай. Если кто-то увидит, то потом навсегда забудет про какую-либо карьеру."
    $ label_random = 0
    if ("frederi_dialogue_boobs_1") in accessiv:
        $ label_random += 1
        $ accessiv.remove("frederi_dialogue_boobs_1")
    if ("frederi_dialogue_boobs_2") in accessiv:
        $ label_random += 1
        $ accessiv.remove("frederi_dialogue_boobs_2")
    if ("frederi_dialogue_boobs_3") in accessiv:
        $ label_random += 1
        $ accessiv.remove("frederi_dialogue_boobs_3")
    if label_random > 1:
        scene pgn_autosalon_fredricobobsjob_01
        ang emo-304 "Сложно было не заметить, как ты смотрел своими голодными глазами на мои груди."
        ang emo-303 "Хочешь увидеть их вблизи?"
        m emo-4 "О да..."
        $ label_random = "v1"
        scene animated pgn_autosalon_fredricobobsjob_v1a
        $ anim_speed = 0.05
        $ renpy.pause()
        menu menu_autosalon_fredricobobsjob:
            "Ускорить" if anim_speed > 0.03:
                $ anim_speed -= 0.02
                if label_random == "v1":
                    scene animated pgn_autosalon_fredricobobsjob_v1b
                if label_random == "v2":
                    scene animated pgn_autosalon_fredricobobsjob_v2b
                $ renpy.pause()
                jump menu_autosalon_fredricobobsjob
            "Замедлить":
                $ anim_speed += 0.02
                if label_random == "v1":
                    scene animated pgn_autosalon_fredricobobsjob_v1b
                if label_random == "v2":
                    scene animated pgn_autosalon_fredricobobsjob_v2b
                $ renpy.pause()
                jump menu_autosalon_fredricobobsjob
            "Смена вида":
                if label_random == "v1":
                    $ label_random = "v2"
                    scene animated pgn_autosalon_fredricobobsjob_v2b
                elif label_random == "v2":
                    $ label_random = "v1"
                    scene animated pgn_autosalon_fredricobobsjob_v1b
                $ renpy.pause()
                jump menu_autosalon_fredricobobsjob
            "Кончить":
                if label_random == "v1":
                    scene pgn_autosalon_fredricobobsjob_v1_15cum
                if label_random == "v2":
                    scene pgn_autosalon_fredricobobsjob_v2_15cum
                m emo-12 "Арргх.... Ммм... Ахххх..."
                scene pgn_autosalon_fredricobobsjob_02
                $ PGN_Addstatsex(stat_angfred, 0, 0, 0, 0, 1)
                ang emo-302 "Молодец. Хороший мальчик."
                m emo-3 "В следующий раз ещё будет?"
                ang emo-301 "Даже и не знаю. Я человек занятой, но думаю смогу уделить время и внимание."
    ang emo-303 "Не против, если я разденусь, а то стало очень жарко."
    m emo-3 "Да, т.е нет... Эм..."
    scene pgn_autosalone_frederibj_01
    m emo-4 "{i}Классное бельишко. Я был бы не против, если она всё с себя сняла.{/i}"
    scene animated pgn_autosalone_frederibja
    $ anim_speed = 0.05
    $ renpy.pause()
    menu menu_autosalon_fredricobj:
        "Ускорить" if anim_speed > 0.03:
            $ anim_speed -= 0.02
            scene animated pgn_autosalone_frederibjb
            $ renpy.pause()
            jump menu_autosalon_fredricobj
        "Замедлить":
            $ anim_speed += 0.02
            scene animated pgn_autosalone_frederibjb
            $ renpy.pause()
            jump menu_autosalon_fredricobj
        "Кончить":
            scene pgn_autosalone_frederibj_cum_00
            m emo-12 "Арргх.... Ммм... Ахххх..."
            scene pgn_autosalone_frederibj_cum_00
            show pgn_autosalone_frederibj_cum_04
            $ renpy.pause(1)
            hide pgn_autosalone_frederibj_cum_04
            $ renpy.pause(1)
            show pgn_autosalone_frederibj_cum_04
            $ renpy.pause(1)
            hide pgn_autosalone_frederibj_cum_04
            $ renpy.pause(1)
            show pgn_autosalone_frederibj_cum_03
            $ renpy.pause(3)
            scene pgn_autosalon_secondvisit_09
            $ PGN_Addstatsex(stat_angfred, 0, 0, 1, 0, 0)
            m emo-3 "В следующий раз ещё будет?"
            ang emo-301 "Даже и не знаю. Я человек занятой, но думаю смогу уделить время и внимание."
    $ qtime += 1
    $ ivent24.append("frederico_sex")
    jump loc_autosalon_consult


label pgn_frederico_coffee_office:
    scene pgn_autosalon_visit_derector_09
    m emo-3 "Здравствуйте."
    ang emo-301 "Привет, [pname_max[0]]. Что тебя привело?"
    if (v_coffee_1.have == False and cycle_latte.have == False and cycle_americano.have == False and cycle_meadraf.have == False) or frederico_path == 7:
        ang emo-304 "..."
        ang emo-301 "Присаживайся."
        scene pgn_autosalon_visit_derector_07
        ang emo-301 "Ну..."
        m emo-4 "А какое кофе вам нравится?"
        if frederico_path == 7:
            ang emo-300 "Честно сказать, не помню как называется. Кофе редко пью, но не откажусь, особенно в загруженные дни."
            $ label_random = renpy.random.choice (["angfred_cycle_latte", "angfred_cycle_americano", "angfred_cycle_meadraf"])
            $ accessiv.append(label_random)
            $ frederico_path = 7.1
        elif frederico_path == 7.1:
            ang emo-304 "Ты уже спрашивал."
            m emo-13 "Да, точно, забыл."
        elif frederico_path == 7.2:
            ang emo-301 "Ты же мне недавно приносил. Уже забыл, что покупал."
            m emo-13 "Да"
            ang emo-301 "Извини, но ты мне называл название кофе. Напомнить не смогу."
            m emo-0 "Ладно."
        ang emo-301 "Есть ещё какие вопросы?"
        m emo-0 "Нет."
    elif ("angfrederi_coffee") not in ivent24 and frederico_path == 7.1:
        m emo-4 "Будете кофе?"
        ang emo-301 "Буду очень благодарна, сама хотела уже перерыв сделать небольшой."
        menu:
            "Кофе \"Вики\"" if v_coffee_1.have == True:
                $ v_coffee_1.have = False
                $ v_coffee_1.numbsuse -= 2
            "Латте" if cycle_latte.have == True:
                $ cycle_latte.have = False
                $ cycle_latte.numbsuse -= 2
                if ("angfred_cycle_latte") in accessiv:
                    jump pgn_frederico_coffee_contune
            "Американо" if cycle_americano.have == True:
                $ cycle_americano.have = False
                $ cycle_americano.numbsuse -= 2
                if ("angfred_cycle_americano") in accessiv:
                    jump pgn_frederico_coffee_contune
            "Медовый Раф" if cycle_meadraf.have == True:
                $ cycle_meadraf.have = False
                $ cycle_meadraf.numbsuse -= 2
                if ("angfred_cycle_meadraf") in accessiv:
                    jump pgn_frederico_coffee_contune
        scene pgn_autosalon_angelfcoffee_04
        $ renpy.pause(3)
        m emo-3 "Как вам кофе, я угадал со вкусом?"
        ang emo-301 "Ммм... нет."
        m emo-1 "Блин."
        ang emo-301 "Всё равно спасибо. Теперь энергии достаточно для работы."
        m emo-4 "А может..."
        ang emo-300 "Извини, но дел много."
    elif ("angfrederi_coffee") not in ivent24 and frederico_path == 7.2:
        m emo-4 "Будете кофе?"
        menu:
            "Кофе \"Вики\"" if v_coffee_1.have == True:
                $ v_coffee_1.have = False
                $ v_coffee_1.numbsuse -= 2
            "Латте" if cycle_latte.have == True:
                $ cycle_latte.have = False
                $ cycle_latte.numbsuse -= 2
                if ("angfred_cycle_latte") in accessiv:
                    $ label_random = "good"
            "Американо" if cycle_americano.have == True:
                $ cycle_americano.have = False
                $ cycle_americano.numbsuse -= 2
                if ("angfred_cycle_americano") in accessiv:
                    $ label_random = "good"
            "Медовый Раф" if cycle_meadraf.have == True:
                $ cycle_meadraf.have = False
                $ cycle_meadraf.numbsuse -= 2
                if ("angfred_cycle_meadraf") in accessiv:
                    $ label_random = "good"
    elif v_coffee_1.have == False and cycle_latte.have == False and cycle_americano.have == False and cycle_meadraf.have == False and frederico_path > 7.1:
        m emo-4 "Будете кофе?"
        ang emo-301 "А ты принёс?"
        m emo-13 "Нет."
        ang emo-304 "..."
        m emo-4 "Ухожу, не буду мешать."
    elif ("angfrederi_coffee") in ivent24:
        m emo-4 "Будете кофе?"
        ang emo-301 "Спасибо тебе, [pname_max[0]]. Но мы сегодня уже пили кофе."
    jump jump_dialogue


label pgn_frederico_coffee_contune:
    scene pgn_autosalon_angelfcoffee_04
    $ renpy.pause(3)
    if frederico_path == 7.1:
        m emo-3 "Как вам кофе, я угадал со вкусом?"
        ang emo-302 "Да, тот самый вкус, что мне нравится."
        $ renpy.pause(3)
    if frederico_path > 7.1 and label_random == "good":
        ang emo-301 "Спасибо, что принёс. Мне этого очень нехватало."
    m emo-3 "Тогда может..."
    ang emo-300 "Извини, но работы много."
    $ ivent24.append("angfrederi_coffee")
    $ qtime += 1
    if frederico_path == 7.1:
        $ frederico_path = 7.2
    if qtime == 19:
        jump loc_autosalon_consult
    jump jump_dialogue


label pgn_frederico_coffee_consult:
    scene pgn_autosalon_angelfcoffee_01
    ang emo-302 "Ох! [pname_max[0]], рада тебя видеть и с кофе."
    m emo-3 "Вот как раз и вам принёс. Хотите?"
    menu:
        "Кофе \"Вики\"" if v_coffee_1.have == True:
            $ v_coffee_1.have = False
            $ v_coffee_1.numbsuse -= 2
        "Латте" if cycle_latte.have == True:
            $ cycle_latte.have = False
            $ cycle_latte.numbsuse -= 2
            if ("angfred_cycle_latte") in accessiv:
                $ label_random = "good"
        "Американо" if cycle_americano.have == True:
            $ cycle_americano.have = False
            $ cycle_americano.numbsuse -= 2
            if ("angfred_cycle_americano") in accessiv:
                $ label_random = "good"
        "Медовый Раф" if cycle_meadraf.have == True:
            $ cycle_meadraf.have = False
            $ cycle_meadraf.numbsuse -= 2
            if ("angfred_cycle_meadraf") in accessiv:
                $ label_random = "good"
    if label_random != "good":
        ang emo-301 "Это то кофе, что мне нравится?"
        m emo-13 "Вроде."
        ang emo-304 "А если быть точным?"
        m emo-2 "Нет. Извините, забыл."
        ang emo-301 "Спасибо за кофе, но попить со сладеньким не получится."
        if frederico_path == 7.2:
            m emo-8 "{i}Со сладеньким!? Это она обо мне или у неё в офисе есть что-то сладкое.{/i}"
        jump pgn_frederico_coffee_consult_end
    else:
        ang emo-302 "Отлично. Пойдём ко мне в офис."
        scene black
        $ renpy.pause(2)
        scene pgn_autosalon_angelfcoffee_02 with dissolve
        ang emo-301 "Я у тебя возьму... стаканы из твоих рук. Сейчас они только будут мешать."
        if frederico_path == 7.2:
            m emo-6 "{i}Мешать!?{/i}"
        scene pgn_autosalon_angelfcoffee_03
        ang emo-303 "[pname_max[0]]. Снимай штаны и устраивайся поудобнее на диване."
        if frederico_path == 7.2:
            m emo-16 "{i}Да! Цель достигнута.{/i}"
        scene pgn_autosalon_secondvisit_09
        if stat_angfred.stsex_bj > 2:
            ang emo-303 "Чего хочется моему дорогому клиенту?"
            menu:
                "Между сисек":
                    $ PGN_Addstatsex(stat_angfred, 0, 0, 0, 0, 1)
                    label pgn_frederico_coffee_boobsjob:
                        scene pgn_autosalon_fredricobobsjob_01
                        ang emo-303 "Устраивайся поудобнее."
                        $ label_random = "v1"
                        scene animated pgn_autosalon_fredricobobsjob_v1a
                        $ anim_speed = 0.05
                        $ renpy.pause()
                        menu menu_pgn_frederico_coffee_boobsjob:
                            "Ускорить" if anim_speed > 0.03:
                                $ anim_speed -= 0.02
                                if label_random == "v1":
                                    scene animated pgn_autosalon_fredricobobsjob_v1b
                                if label_random == "v2":
                                    scene animated pgn_autosalon_fredricobobsjob_v2b
                                $ renpy.pause()
                                jump menu_pgn_frederico_coffee_boobsjob
                            "Замедлить":
                                $ anim_speed += 0.02
                                if label_random == "v1":
                                    scene animated pgn_autosalon_fredricobobsjob_v1b
                                if label_random == "v2":
                                    scene animated pgn_autosalon_fredricobobsjob_v2b
                                $ renpy.pause()
                                jump menu_pgn_frederico_coffee_boobsjob
                            "Смена вида":
                                if label_random == "v1":
                                    $ label_random = "v2"
                                    scene animated pgn_autosalon_fredricobobsjob_v2b
                                elif label_random == "v2":
                                    $ label_random = "v1"
                                    scene animated pgn_autosalon_fredricobobsjob_v1b
                                $ renpy.pause()
                                jump menu_pgn_frederico_coffee_boobsjob
                            "Кончить":
                                if label_random == "v1":
                                    scene pgn_autosalon_fredricobobsjob_v1_15cum
                                if label_random == "v2":
                                    scene pgn_autosalon_fredricobobsjob_v2_15cum
                                m emo-12 "Арргх.... Ммм... Ахххх..."
                                scene pgn_autosalon_fredricobobsjob_02
                                if pgnach_115.aopen == False:
                                    $ PGN_Achadd(pgnach_115, 115)
                                if pgn_ach_repeat == 115:
                                    jump table_pgn_achievement
                                $ qtime += 1
                                if frederico_path == 7.3:
                                    $ frederico_path = 8
                                jump pgn_frederico_coffee_consult_end
                "Минет":
                    pass
        $ PGN_Addstatsex(stat_angfred, 0, 0, 1, 0, 0)
        label pgn_frederico_coffee_bj:
            scene animated pgn_autosalone_frederibja
            $ anim_speed = 0.05
            $ renpy.pause()
            menu menu_pgn_frederico_coffee_bj:
                "Ускорить" if anim_speed > 0.03:
                    $ anim_speed -= 0.02
                    scene animated pgn_autosalone_frederibjb
                    $ renpy.pause()
                    jump menu_pgn_frederico_coffee_bj
                "Замедлить":
                    $ anim_speed += 0.02
                    scene animated pgn_autosalone_frederibjb
                    $ renpy.pause()
                    jump menu_pgn_frederico_coffee_bj
                "Кончить":
                    scene pgn_autosalone_frederibj_cum_00
                    $ label_random = renpy.random.randint ( 1, 3)
                    if label_random == 3:
                        show animated pgn_autosalone_frederibj_cum01
                    if label_random != 3:
                        show animated pgn_autosalone_frederibj_cum02
                    m emo-12 "Арргх.... Ммм... Ахххх..."
                    scene pgn_autosalon_secondvisit_09
                    if label_random != 3:
                        ang emo-301 "Ого! Это было много."
                        m emo-4 "Через час могу ещё."
                        ang emo-301 "Этого достаточно и мне работать нужно."
                        m emo-3 "Тогда до следующего раза."
                    else:
                        ang emo-303 "Теперь можно и кофе попить."
                    $ qtime += 1
                    if frederico_path == 7.2:
                        $ frederico_path = 7.3
                    if pgnach_114.aopen == False:
                        $ PGN_Achadd(pgnach_114, 114)
                    if pgn_ach_repeat == 114:
                        jump table_pgn_achievement
label pgn_frederico_coffee_consult_end:
    $ ivent24.append("angfrederi_coffee")
    jump jump_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
