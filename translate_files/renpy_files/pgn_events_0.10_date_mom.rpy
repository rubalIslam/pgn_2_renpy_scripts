






label pgn_mominvitinrestgn:
    m emo-3 "Сегодня вечером пойдём в ресторан?"
    if mom_path < 13 and daysn != 1 and daysn != 4:
        mom emo-62 "[pname_max[0]], тебе не обязательно водить меня по ресторанам. Я и так знаю, что ты меня любишь."
        m emo-2 "Поэтому и хочу сводить тебя куда-нибудь. А то ты постояно или дома или на работе."
        mom emo-75 "Это очень мило, спасибо. Ну раз такой кавалер приглашает даму, то почему бы и нет."
    if daysn == 1 or daysn == 4:
        mom emo-62 "Спасибо конечно за предложение, но у меня сегодня съёмки."
        m emo-13 "А может отменишь их? Подумаешь один раз не придёшь?"
        mom emo-60 "[pname_max[0]], я так не могу. Если не приду, то возьмут каку-то другую актрису, а нам всё ещё нужны деньги."
        m emo-0 "Ладно."
    else:
        m emo-0 "Время ещё есть."
        mom emo-67 "Хорошо. К тому времени я буду готова. Самое главное сам не забудь и будь к этому времени дома."
    $ ivent24.append("restgn_mom_true")
    jump jump_dialogue


label pgn_goldenight_date_mom_rest:
    scene black
    $ renpy.pause(3)
    if transport3.use == True or transport1.use == True or transport2.use == True:
        $ label_random = renpy.random.randint ( 1, 2)
        if label_random == 1:
            scene pgn_hotel_gn_transport_mom_petruha with dissolve
        if label_random == 2:
            scene pgn_hotel_gn_transport_none_petruha with dissolve
    if transport4.use == True:
        scene pgn_hotel_gn_transport_max1_petruha with dissolve
    if transport5.use == True:
        scene pgn_hotel_gn_transport_max2 with dissolve
    $ renpy.pause(2)
    scene pgn_hotel_goldennight_adm_01
    other hemo-61 "Здравствуйте. Приветствую вас. У вас столик заказан, на чьё имя?"
    scene pgn_hotel_gn_mom_01_petruha
    m emo-0 "[pname_max[0]]."
    scene pgn_hotel_goldennight_adm_02
    $ renpy.pause(2)
    scene pgn_hotel_gn_mom_01_petruha
    other hemo-61 "Всё верно, вы есть в списке. Ваш столик готов. Желаю вам приятно провести время."
    scene pgn_hotel_gn_mom_02_petruha
    $ renpy.pause(2)
    scene pgn_hotel_gn_mom_03_petruha
    mom emo-62 "В прошлый раз всё было очень вкусным."
    m emo-3 "Ага, мне понравилось."
    scene pgn_hotel_gn_mom_04_petruha
    other emo-999 "Здравствуйте. Для вашего стола уже готовятся блюда, минут через 10-15 вам принесу. Пока вы ждёте ваш заказ, не желаете чего-нибудь выпить?"
    menu:
        "Один бокал вина":
            $ restgn_wine += 1
            $ restgn_drunkalc += 1
        "Два бокала вина":
            $ restgn_wine += 1
            $ restgn_drunkalc += 1
            m emo-0 "Нам два бокала вина..."
            mom emo-62 "Один, бокал. Ему нельзя, он плохо переносит спиртное."
            scene pgn_hotel_gn_mom_03_petruha
            m emo-6 "Мам!?"
            mom emo-64 "Мы уже об этом говорили. И кто-то из нас должен быть с трезвой головой."
            if ("driver's license") in accessiv and (transport3.use == True or transport1.use == True or transport2.use == True)  and label_random == 1:
                mom emo-62 "И раз у тебя есть права, то сам сможешь меня отвезти домой."
            if ("driver's license") in accessiv and (transport4.use == True or transport5.use == True):
                mom emo-62 "И за руль, нетрезвым, нельзя садится."
            m emo-2 "Ладно, как скажешь."
            mom emo-62 "Вот и хорошо."
        "Одну бутылку вина":
            $ restgn_wine += 3
            $ restgn_drunkalc += 6
            mom emo-73 "[pname_max[0]], я не смогу столько выпить."
            m emo-2 "Что останется, домой заберем. И раз я пригласил, то я плачу."
    scene black
    $ renpy.pause(1)
    scene pgn_hotel_gn_mom_05_petruha with dissolve
    $ renpy.pause(1)
    mom emo-62 "Спасибо"
    scene pgn_hotel_gn_mom_06_petruha
    $ renpy.pause(2)
    scene pgn_hotel_gn_mom_07_petruha with dissolve
    jump pgn_goldenight_date_mom_rest_dialogue
label pgn_goldenight_date_mom_rest_next:
    scene pgn_hotel_gn_mom_08_petruha
    if restgn_drunk < 5:
        mom emo-75 "[pname_max[0]], пока ты ждёшь счёт, мне нужно отойти в дамскую комнату."
        m emo-3 "Как оплачу, встречу тебя."
    if restgn_drunk >= 5:
        mom emo-75 "Мамочка сходит пописать. Не подглядывай."
        m emo-1 "Я и не... Тебя проводить?"
    scene pgn_hotel_gn_mom_09
    if mom_path < 13:
        m emo-6 "{i}Блин! Никак не могу не насмотреться на эту попку. В этом платье я ещё больше её хочу.{/i}"
    if mom_path >= 13:
        m emo-4 "{i}У мамы попка супер.{/i}"
    scene pgn_hotel_gn_mom_10a_petruha
    m emo-0 "Так посмотрим..."
    scene pgn_hotel_gn_mom_10b_petruha with dissolve
    if ("restgn_vip_19") in ivent24 or ("restgn_vip_20") in ivent24 or ("restgn_vip_21") in ivent24 or ("restgn_vip_22") in ivent24 or ("restgn_vip_23") in ivent24:
        $ shopping_pay = 200
    if ("restgn_19") in ivent24 or ("restgn_20") in ivent24 or ("restgn_21") in ivent24 or ("restgn_22") in ivent24 or ("restgn_23") in ivent24:
        $ shopping_pay = renpy.random.randint ( 30, 70)
        $ shopping_pay = (shopping_pay*2)+(restgn_wine*10)
    call screen hotel_goldennight_chek
    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[11])+" $"+str(shopping_pay))
    $ bill_goldennight += shopping_pay
    $ currency -= shopping_pay
    scene pgn_hotel_gn_mom_11_petruha
    $ renpy.pause(3)
    $ ivent24.append("gn_mom_date")
    if restgn_drunk < 4:
        scene pgn_hotel_gn_mom_12_petruha
        mom emo-62 "О! [pname_max[0]]. Уже оплатил?"
        m emo-3 "Да, мы можем идти."
        if ("restgn_pool") in ivent24:
            m emo-0 "Я забронировал бассейн."
            mom emo-62 "Но дома же есть у нас бассейн."
            m emo-3 "Этот больше и мы будем совсем одни."
            mom emo-62 "Ну хорошо. Пойдём."
            jump pgn_goldenight_date_mom_pool
        if ("restgn_room_b&w") in ivent24:
            m emo-0 "Я забронировал номер в отеле. Так что можем там продолжить."
            mom emo-62 "Ну пойдём, мой мужчина."
            jump pgn_goldenight_date_mom_hotelroom
        mom emo-62 "Хорошо. А то уже поздно."
    if restgn_drunk == 4 or restgn_drunk == 5:
        $ label_random = renpy.random.randint ( 1, 5)
        if label_random != 2:
            scene pgn_hotel_gn_mom_13
            m emo-1 "Тебе помочь?"
            mom emo-62 "Малыш. Мама немного перебрала. Не обнимешь мамочку."
            m emo-1 "Да... Коне..."
            scene pgn_hotel_gn_mom_14
            mom emo-69 "Вот так. Ммм... Возьми меня за попу... Ммм... Хороший мальчик."
            m emo-13 "Мам. Мы всё ещё в ресторане и нас могут неправильно понять."
            mom emo-62 "Ты и так непереставая называешь меня Мамой. Сейчас мне без разницы. Особенно после случая в кинотеатре."
            m emo-1 "Мам..."
            mom emo-69 "Просто побудь со мной немного."
            if ("restgn_pool") in ivent24:
                m emo-0 "Не хочешь сходить и искупаться в бассейне? Я забронировал его для нас.."
                if restgn_drunk == 5:
                    $ label_random = renpy.random.randint ( 1, 2)
                    if label_random == 1:
                        pass
                    else:
                        mom emo-73 "Ты меня прости, но я сейчас еле-еле на ногах стою, так плавать ну ни как не смогу."
                        if ("restgn_room_b&w") in ivent24:
                            m emo-0 "Тогда пойдём в отель."
                            mom emo-62 "Хорошо, только помоги мне."
                            m emo-3 "Конечно"
                            jump pgn_goldenight_date_mom_hotelroom
                        else:
                            $ qtime += 1
                            if qtime >= 24:
                                $ qtime = qtime - 24
                                $ daysnchange()
                            jump loc_pool
                mom emo-62 "Спасибо. Ты мой любимый."
                jump pgn_goldenight_date_mom_pool
            if ("restgn_room_b&w") in ivent24:
                m emo-0 "Я забронировал номер в отеле. Так что можем там продолжить."
                jump pgn_goldenight_date_mom_hotelroom
        else:
            scene pgn_hotel_gn_mom_15
            m emo-1 "Мам! Ты ещё там?"
            m emo-0 "..."
            m emo-1 "Я войду?"
            m emo-0 "{i}Ладно. Вхожу.{/i}"
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random == 3:
                jump pgn_goldenight_date_mom_rest_bath
            else:
                scene pgn_hotel_gn_mom_16_petruha
                m emo-0 "Эх.. Уснула. Придётся как-то самому её тащить."
                $ ivent24.append("restgn_mom_sleep")
                if ("restgn_room_b&w") in ivent24:
                    jump pgn_goldenight_date_mom_hotelroom
    if restgn_drunk >= 6:
        scene pgn_hotel_gn_mom_15
        m emo-1 "Мам! Ты ещё там?"
        m emo-0 "..."
        m emo-1 "Я войду?"
        m emo-0 "{i}Ладно. Вхожу.{/i}"
        $ label_random = renpy.random.randint ( 1, 3)
        if label_random == 3:
            jump pgn_goldenight_date_mom_rest_bath
        else:
            scene pgn_hotel_gn_mom_16_petruha
            m emo-0 "Эх.. Уснула. Придётся как-то самому её тащить."
            $ ivent24.append("restgn_mom_sleep")
            if ("restgn_room_b&w") in ivent24:
                jump pgn_goldenight_date_mom_hotelroom
    $ qtime += 1
    if qtime >= 24:
        $ qtime = qtime - 24
        $ daysnchange()
    jump loc_pool


label pgn_goldenight_date_mom_rest_bath:
    scene pgn_hotel_gn_mom_bath_bj_01
    m emo-9 "Ой! Ты занята. Я подожду за дверью..."
    mom emo-73 "Подожди, не уходи."
    scene pgn_hotel_gn_mom_bath_bj_02
    if pgnach_119.aopen == False:
        $ PGN_Achadd(pgnach_119, 119)
    if restgn_drunk < 6:
        mom emo-73 "Подойди ко мне. Мне нужна помощь."
        m emo-13 "Может я всё же подожду за дверью?"
        mom emo-71 "Закрой дверь на защёлку и подойди к мамочке."
        m emo-0 "Хорошо."
    if restgn_drunk >= 6:
        mom emo-68 "Мамочке нужен твой член. Так что подойди и удовлетвори моё желание."
    scene pgn_hotel_gn_mom_bath_bj_03
    if restgn_drunk < 6:
        mom emo-68 "[pname_max[0]], давай, доставай его быстрее, мне он сейчас очень нужен."
        m emo-2 "Может где-нибудь в другом месте? Вдруг нас заметят?"
        mom emo-64 "Если не хочешь, чтобы нас заметили, то тебе лучше поторопиться, пока я не разорвала эту молнию."
        m emo-9 "Хорошо, хорошо... сейчас."
    if restgn_drunk >= 6:
        mom emo-69 "Ну же, быстрее."
        m emo-1 "Да, да, сейчас."
    scene pgn_hotel_gn_mom_bath_bj_04_1
    mom emo-69 "Какой он горячий, так и манит взять его в рот."
    scene animated pgn_goldenight_date_mom_rest_bath_bj_01a
    $ renpy.pause()
    if restgn_drunk >= 6:
        scene pgn_hotel_gn_mom_bath_bj_04_1
        mom emo-68 "Ммм... Отлично..."
    scene animated pgn_goldenight_date_mom_rest_bath_bj_01b
    $ renpy.pause()
    mom emo-68 "Малыш. Кончи на меня, облей маму горячей спермой. Ну же..."
    scene black
    m emo-12 "Аргх..."
    scene pgn_hotel_gn_mom_bath_bj_05
    mom emo-62 "Теперь я довольна. Спасибо."
    if pgn_ach_repeat == 119:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 0, 0, 1, 0, 0)
    $ ivent24.append("gn_bath_bj")
    if ("restgn_pool") in ivent24:
        m emo-0 "Как насчёт того, чтобы искупаться в бассейне?"
        if restgn_drunk == 4:
            mom emo-62 "Не против."
            jump pgn_goldenight_date_mom_pool
        if restgn_drunk == 5 or restgn_drunk == 6:
            mom emo-69 "Не хочу. Я больше ни на что негодна, мне нужен отдых."
        if restgn_drunk > 6:
            mom emo-69 "Мамочка хочет спать."
    if ("restgn_room_b&w") in ivent24:
        m emo-0 "Я забронировал номер в отеле. Так что можем там продолжить."
        if restgn_drunk >= 5:
            mom emo-62 "Продолжить? Не уверена, что смогу найти силы на что-то ещё. Если только лечь спать."
        else:
            mom emo-62 "Ну пойдём, мой мужчина."
        jump pgn_goldenight_date_mom_hotelroom
    $ qtime += 2
    if qtime >= 24:
        $ qtime = qtime - 24
        $ daysnchange()
    jump loc_pool


label pgn_goldenight_date_mom_pool:
    scene pgn_date_mom_pool_go_01
    if ("fdp_mom") not in onetevent:
        mom emo-60 "[pname_max[0]]... А мы точно направляемся к бассейну?"
        m emo-3 "Да, всё верно. Только возьму ключи от шкафчиков."
    if restgn_drunk < 4 and ("fdp_mom") in onetevent:
        mom emo-62 "Быстренько переодевайся."
    if restgn_drunk >= 4 and ("fdp_mom") in onetevent:
        mom emo-62 "Поскорее бы под холодный душе, а то я уже с ног валюсь."
        mom emo-69 "Если задержусь, то зайди за мной."
    if ("fdp_mom") not in onetevent:
        if daysn == 6 or daysn == 7:
            scene pgn_hotel_2et_recep_admin_02
            victor emo-400 "Да?"
            m emo-0 "У меня забронирован бассейн."
            victor emo-400 "Карта с собой?"
            scene pgn_date_mom_pool_go_02b
            victor emo-400 "Вот ключи от кабинок. Тебе налево, твоей спутнице направо."
        else:
            scene pgn_hotel_2et_recep_admin_01
            other hemo-81 "Здравствуйте."
            m emo-0 "У меня забронирован бассейн."
            other hemo-81 "Можете предоставить вашу карту для подтверждения?"
            scene pgn_date_mom_pool_go_02
            other hemo-81 "Вот ваши ключи от кабинок. Спасибо, что пользуетесь услугами нашего отеля."
    scene pgn_date_mom_pool_go_03
    $ renpy.pause(3)
    scene pgn_date_mom_pool_go_04
    $ renpy.pause(3)
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random != 3:
        scene pgn_date_mom_pool_go_05
        m emo-6 "Что-то её долго нет."
        menu:
            "Ждать":
                pass
            "Заглянуть":
                scene pgn_date_mom_pool_go_06
                m emo-3 "{i}Мммм...{/i}"
                scene pgn_date_mom_pool_go_07
                m emo-6 "{i}Что ж она так долго. Надеть халат и всё.{/i}"
                scene animated pgn_date_mom_pool_lockers_01
                m emo-4 "{i}Прям сейчас бы вошёл в эту попку.{/i}"
                m emo-3 "Чёрт! У меня встал."
                scene pgn_date_mom_pool_go_09
                mom emo-66 "Аааа!"
                m emo-1 "Мам, это я. Всё хорошо."
                scene pgn_date_mom_pool_go_10
                mom emo-64 "На надо меня так пугать."
                m emo-8 "Извини."
                mom emo-62 "Подожди меня снаружи, я скоро. И... с твоей проблемкой помогу потом."
                m emo-4 "Ок."
                $ ivent24.append("dp_mom_lookers_spy")
    scene pgn_date_mom_pool_in_01_arata111
    if ("fdp_mom") not in onetevent:
        mom emo-60 "[pname_max[0]]. Почему здесь больше никого нет? Пришли слишком рано или поздно?"
        m emo-3 "Нет. На целый час он весь наш."
        mom emo-60 "[pname_max[0]]! Это наверное было очень дорого?"
        m emo-2 "Для тебя мне ни каких денег не жалко."
    if ("fdp_mom") in onetevent:
        mom emo-60 "Тут точно никого не будет кроме нас."
        m emo-2 "Да точно. В прошлый раз же были одни."
    scene pgn_date_mom_pool_in_02_arata111
    $ renpy.pause(2)
    scene pgn_date_mom_pool_in_03_arata111
    m emo-3 "Мам. Запрыгивай."
    mom emo-60 "Нет уж, я прыгать не буду. Лучше по ступенькам, медленно и осторожно."
    scene pgn_date_mom_pool_in_04_arata111
    $ renpy.pause(3)
    scene pgn_date_mom_pool_in_05_arata111
    $ renpy.pause(3)
    scene pgn_date_mom_pool_in_06_arata111
    $ renpy.pause(3)
    scene pgn_date_mom_pool_in_07_arata111
    if ("fdp_mom") not in onetevent:
        mom emo-60 "Зачем было бронировать бассейн? У нас же дома свой."
        m emo-3 "Тут бассейн побольше и можешь плавать совершенно голой."
        mom emo-60 "Но мы все дома и так голыми плаваем."
        m emo-13 "Почти, голыми. Тебе ни разу не хотелось поплавать совсем без ничего?"
        mom emo-69 "Ну... а вдруг кто зайдёт."
        m emo-3 "Да ни кого не будет, мы тут только одни."
    if ("fdp_mom") in onetevent:
        m emo-3 "Мам, ты пока поплавай, а со стороны буду смотреть на тебя."
        mom emo-62 "Может вместе поплаваем?"
        m emo-4 "Мне больше всего нравится смотреть на тебя, Мам."
        scene pgn_date_mom_pool_in_08_vezdessushij
        mom emo-62 "Люблю тебя."
    scene animated pgn_date_mom_pool_swim_01
    $ renpy.pause(12)
    menu menu_pgn_goldenight_date_mom_pool_swim:
        "Подплыть":
            pass
        "Понаблюдать":
            scene animated pgn_date_mom_pool_swim_01
            $ renpy.pause(12)
            jump menu_pgn_goldenight_date_mom_pool_swim
    scene pgn_date_mom_pool_in_08_vezdessushij
    $ renpy.pause()
    scene pgn_date_mom_pool_in_07_arata111
    if ("dp_mom_lookers_spy") in ivent24:
        if ("restgn_room_b&w") in ivent24:
            mom emo-62 "Я помню про твой большой и крепкий член. Но ты как хочешь. Здесь или в номере?"
            menu menu_pgn_goldenight_date_mom_pool_choiceloc:
                "В номере отеля":
                    mom emo-62 "Тогда выходим из бассейна и бегом в номер."
                    scene pgn_date_mom_pool_in_14_vezdessushij
                    mom emo-75 "Ну же, [pname_max[0]]. Не заставляй меня ждать тебя."
                    jump pgn_goldenight_date_mom_hotelroom
                "В бассейне":
                    mom emo-62 "Хорошо. Тогда следуй за мной, мой перевозбужденный малыш."
                    jump pgn_date_mom_pool_in_sex_vaginal
        mom emo-69 "Я кажется понимаю, что у тебя на уме. Но всё же. Чего тебе хочется?"
        jump menu_pgn_goldenight_date_mom_pool_choicesex
    if ("dp_mom_lookers_spy") not in ivent24:
        menu:
            "Предложить секс":
                if ("fdp_mom") in onetevent:
                    m emo-0 "Мам!"
                    scene pgn_date_mom_pool_in_07_arata111
                    mom emo-62 "Что такое?"
                    m emo-2 "Не хочешь чего-нибудь ещё, особенного?"
                else:
                    m emo-4 "Мам. Как насчёт немного повеселиться, здесь в бассейне?"
                if ("gn_bath_bj") in ivent24:
                    mom emo-68 "[pname_max[0]]. Я тебе уже делала минет в ресторане."
                    m emo-4 "Так я ещё хочу."
                    if ("restgn_room_b&w") in ivent24:
                        mom emo-60 "Тогда выбирай. Или сейчас в бассейне и после идём спать или займёмся сексом в отеле."
                        jump menu_pgn_goldenight_date_mom_pool_choiceloc
                mom emo-62 "И чего тебе хочется?"
                jump menu_pgn_goldenight_date_mom_pool_choicesex
            "Отправиться в номер" if ("restgn_room_b&w") in ivent24:
                jump pgn_goldenight_date_mom_hotelroom
            "Отправиться домой" if ("restgn_room_b&w") not in ivent24:
                $ qtime += 3
                if qtime >= 24:
                    $ qtime = qtime - 24
                    $ daysnchange()
                jump loc_pool
    menu menu_pgn_goldenight_date_mom_pool_choicesex:
        "Куни":
            jump pgn_date_mom_pool_in_cunni
        "Вагинальный секс":
            jump pgn_date_mom_pool_in_sex_vaginal
label pgn_date_mom_pool_in_cunni:
    scene pgn_date_mom_pool_in_14_vezdessushij
    mom emo-62 "Я жду..."
    m emo-4 "Уже плыву."
    scene pgn_date_mom_pool_in_15_vezdessushij
    mom emo-68 "Малыш. Будь нежнее."
    scene animated pgn_date_mom_pool_cunni_01
    mom emo-75 "Охх.... Ммм.... [pname_max[0]]... нежнее... Ммм..."
    $ renpy.pause()
    scene pgn_date_mom_pool_in_15_vezdessushij
    mom emo-68 "Аааххх... Ммм... Не останавливайся... Я почти..."
    scene animated pgn_date_mom_pool_cunni_01
    m emo-10 "{i}Мамина киска очень приятно пахнет и из неё так и сочатся соки.{/i}"
    $ renpy.pause()
    scene pgn_date_mom_pool_in_17_vezdessushij
    if pgnach_120.aopen == False:
        $ PGN_Achadd(pgnach_120, 120)
    mom emo-66 "Ахххх...."
    scene pgn_date_mom_pool_in_18_vezdessushij
    mom emo-69 "Фух... Спасибо. Мои уроки не зря прошли."
    mom emo-62 "Ещё есть время? Я немного здесь ещё полежу... совсем немного..."
    if pgn_ach_repeat == 120:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 0, 1, 0, 0, 0)
    $ ivent24.append("dhp_mom_cunni")
    if ("restgn_room_b&w") in ivent24:
        m emo-4 "Это ещё не всё."
        jump pgn_goldenight_date_mom_hotelroom
    if ("restgn_room_b&w") not in ivent24:
        $ qtime += 3
        if qtime >= 24:
            $ qtime = qtime - 24
            $ daysnchange()
        jump loc_pool

label pgn_date_mom_pool_in_sex_vaginal:
    scene animated pgn_date_mom_pool_vaginal_01
    $ renpy.pause()
    $ label_random = "вид1"
    menu menu_pgn_date_mom_pool_sexvaginal:
        "Вид 1" if label_random == "вид2":
            scene animated pgn_date_mom_pool_vaginal_01
            $ renpy.pause()
            jump menu_pgn_date_mom_pool_sexvaginal
        "Вид 2" if label_random == "вид1":
            scene animated pgn_date_mom_pool_vaginal_02
            $ renpy.pause()
            jump menu_pgn_date_mom_pool_sexvaginal
        "Кончить":
            pass
    scene pgn_date_mom_pool_in_21_vezdessushij
    if pgnach_121.aopen == False:
        $ PGN_Achadd(pgnach_121, 121)
    m emo-12 "Аррггххх..."
    mom emo-75 "Ты моё солнышко, молодец."
    if pgn_ach_repeat == 121:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 0, 0, 0, 1, 0)
    $ ivent24.append("dhp_mom_sex_vaginal")
    if ("restgn_room_b&w") in ivent24:
        jump pgn_goldenight_date_mom_hotelroom
    else:
        $ qtime += 4
        if qtime >= 24:
            $ qtime = qtime - 24
            $ daysnchange()
        jump loc_pool


label pgn_goldenight_date_mom_hotelroom:
    if restgn_drunk >= 5 or ("restgn_mom_sleep") in ivent24:
        jump pgn_goldenight_date_mom_hotelroom_v1
    if restgn_drunk < 5 and ("dhp_mom_sex_vaginal") not in ivent24:
        jump pgn_goldenight_date_mom_hotelroom_v2
    if ("dhp_mom_sex_vaginal") in ivent24:
        scene pgn_horelroom_bw_mom_13_vezdessushij
        $ renpy.pause(4, hard=True)
        jump pgn_goldenight_date_mom_hotelroom_v3

label pgn_goldenight_date_mom_hotelroom_v1:
    scene pgn_horelroom_bw_mom_01_vezdessushij
    m emo-8 "Мам, ты еле-еле на ногах держишься."
    mom emo-75 "Это всё потому, что мамочка много выпила и она немного пьяная."
    m emo-0 "Извини, мне нужно было за этим проследить, но хотел, чтобы ты была довольна вечером."
    mom emo-62 "Всё хорошо... [pname_max[0]]... Мне понравилось... Мамочке просто нужно отдохнуть... Ик... Я тебя люблю."
    m emo-0 "Я тоже тебя люблю. Сейчас помогу разуться."
    scene pgn_horelroom_bw_mom_02_vezdessushij
    m emo-8 "Тебе помочь раздеться?"
    mom emo-69 "Я... могу сама..."
    m emo-0 "Эм... Ладно, тогда я пока схожу в душ."
    scene pgn_horelroom_bw_mom_03_vezdessushij
    $ renpy.pause(4)
    scene pgn_horelroom_bw_mom_04_vezdessushij
    menu:
        "Лечь спать":
            scene pgn_horelroom_bw_mom_13_vezdessushij
            $ renpy.pause(5, hard=True)
            $ daysnchange()
            call max_sleep_reset from _call_max_sleep_reset_1
            $ qtime = 8
            jump loc_pool
        "Подрочить на Маму":
            label pgn_goldenight_date_mom_hotelroom_v1_hj:
                scene pgn_horelroom_bw_mom_05_vezdessushij
                m emo-8 "{i}Прости, что без разрешения, но мне очень нужно кончить, иначе не усну.{/i}"
                scene pgn_horelroom_bw_mom_06_vezdessushij
                m emo-6 "{i}Осторожно... Хочу увидеть её прелестные сиськи{/i}"
                scene pgn_horelroom_bw_mom_07_1_vezdessushij
                if pgnach_122.aopen == False:
                    $ PGN_Achadd(pgnach_122, 122)
                m emo-3 "{i}Отлично, теперь можно и подрочить.{/i}"
                scene animated pgn_date_mom_hotelroom_bw_hj_01
                $ renpy.pause()
                m emo-5 "{i}Мам, ты всё рано очень сексуальна. Даже когда спишь.{/i}"
                m emo-10 "{i}Уже скоро... уже почти... и я...{/i}"
        "Между сисек":
            label pgn_goldenight_date_mom_hotelroom_v1_boobs:
                scene pgn_horelroom_bw_mom_06_vezdessushij
                m emo-8 "{i}Осторожно... Хочу увидеть её прелестные округлости{/i}"
                scene pgn_horelroom_bw_mom_07_1_vezdessushij
                m emo-3 "{i}Отлично, теперь можно трахнуть её сиськи.{/i}"
                scene animated pgn_date_mom_hotelroom_bw_hj_02
                if pgnach_123.aopen == False:
                    $ PGN_Achadd(pgnach_123, 123)
                $ renpy.pause()
    if restgn_drunk == 4:
        $ label_random = renpy.random.randint ( 1, 3)
        if label_random == 1:
            scene pgn_horelroom_bw_mom_21_vezdessushij
            mom emo-63 "Сынок... Не мешай маме спать..."
            m emo-2 "Мне сложно уснуть, когда рядом такая горячая и сексуальная мама."
            mom emo-72 "[pname_max[0]].... Я... Я хочу спать... Не мешай мне... Сам себе помоги, в ванной.."
            scene pgn_horelroom_bw_mom_22_vezdessushij
            m emo-2 "Но ты же знаешь, что я не могу сам, у меня..."
            mom emo-64 "Или ложись спать.... Или... Или будешь спать на полу."
            $ daysnchange()
            call max_sleep_reset from _call_max_sleep_reset
            $ qtime = 8
            jump loc_pool
    m emo-8 "{i}Так, стоп. Мне нельзя кончать на неё, иначе она поймёт, что у меня нет проблем с руками.{/i}"
    scene pgn_horelroom_bw_mom_08_vezdessushij
    m emo-3 "{i}Попытаюсь кончить в рот. Она слегка приоткрывает свой сексуальный ротик.{/i}"
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random == 2:
        mom emo-67 "Ммм... [pname_max[0]]..."
        m emo-9 "{i}Чёрт! Она проснулась!?{/i}"
        mom emo-71 "Мамочка сделает всё что ты захочешь... Ммм... Мамочка хочет быть только твоей..."
    scene pgn_horelroom_bw_mom_09_vezdessushij
    if label_random == 2:
        m emo-2 "{i}Фух! Она всё ещё спит. И она на автомате взяла член в рот и... и...{/i}"
        m emo-4 "{i}Она во сне лижет мой член!? Мам, ты супер.{/i}"
    else:
        m emo-10 "{i}Ого! Какой горячий и влажный ротик...{/i}"
        m emo-12 "Мм... Ах... Ммм... Ох... Да..."
    scene pgn_horelroom_bw_mom_10_vezdessushij
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random == 1:
        mom emo-75 "Мммм... Вкусный ужин, спасибо..."
    if label_random == 2:
        mom emo-75 "Мммм... Вкусный десерт..."
    if label_random == 1:
        mom emo-75 "Мммм... Мамочке мало, она хочет... ещё..."
        m emo-3 "Завтра, Мам, завтра..."
        mom emo-72 "Ммм..."
        m emo-9 "{i}Всё, молчу, а то проснётся... Я сплю, ничего не знаю и ничего не видел.{/i}"
    if pgn_ach_repeat == 122 or pgn_ach_repeat == 123:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 0, 0, 0, 0, 1)
    scene pgn_horelroom_bw_mom_11_vezdessushij
    $ renpy.pause(4, hard=True)
    scene pgn_horelroom_bw_mom_12_vezdessushij
    mom emo-62 "{i}Хм... Что это? На губах и во рту этот привкус. Сперма? Ничего не помню. Кажется перед сном мы немного повеселились.{/i}"
    $ daysnchange()
    call max_sleep_reset from _call_max_sleep_reset_2
    $ qtime = 8
    jump loc_pool

label pgn_goldenight_date_mom_hotelroom_v2:
    scene pgn_horelroom_bw_mom_15_vezdessushij
    m emo-16 "Мам, у тебя шикарная, большая, мягкая и сексуальная попка."
    mom emo-62 "[pname_max[0]], спасибо за комплименты моей... попе. Но мне нужно в ванную, подготовлюсь и сможешь делать со мной всё что захочется."
    m emo-4 "{i}Самое лучшие и приятные слова, которые можно услышать.{/i}"
    scene pgn_horelroom_bw_mom_16_vezdessushij
    mom emo-60 "Ни как не могу снять..."
    m emo-6 "Мам, может займёмся прям здесь, сексом. А то встала в такую удобную для меня позу, что хоть сейчас."
    mom emo-63 "[pname_max[0]], нет. Я пытаюсь снять туфли."
    mom emo-62 "А ты пока сбегай в душ, тебе же там быстро, чем мне."
    m emo-0 "Ок."
    scene pgn_horelroom_bw_mom_03_vezdessushij
    $ renpy.pause(4)
    scene pgn_horelroom_bw_mom_17_vezdessushij
    m emo-6 "Может ну его этот душ, только пустая трата времени. Не мог дождаться."
    mom emo-73 "Я вижу, что тебе невтерпеж, но нет. Или вообще ничего не будет."
    mom emo-60 "И убери ноги с подушек."
    scene pgn_horelroom_bw_mom_18_vezdessushij
    $ renpy.pause(3)
    scene pgn_horelroom_bw_mom_19_vezdessushij
    $ renpy.pause(3)
    scene pgn_horelroom_bw_mom_20_vezdessushij
    $ renpy.pause()
    if mom_path < 13:
        menu:
            "Предложить анальный секс":
                m emo-3 "Мам? Займёмся сегодня анальным сексом?"
                if restgn_drunk < 4:
                    if mom_path == 12.5:
                        mom emo-73 "Нет. Мне этот вид секса не нравится и он болезненный."
                        m emo-2 "Прости. просто предложил. Я не настаиваю и понимаю."
                        mom emo-69 "{i}[pname_kira[0]] была права. Ему хочется что-то новое. Нужно поскорее пройти с ней уроки.{/i}"
                    if mom_path < 12.5:
                        mom emo-68 "Сынок. Ты хочешь, чтобы маме снова было плохо?"
                        m emo-8 "Нет, я не..."
                        mom emo-60 "Давай не будем поднимать эту тему. Хорошо?"
                        m emo-2 "Прости."
                    if mom_path > 12.5:
                        mom emo-73 "..."
                        m emo-1 "Мам?"
                        m emo-0 "{i}Наверное из-за шума воды ничего не слышит.{/i}"
            "Промолчать":
                pass
    scene pgn_horelroom_bw_mom_24_vezdessushij
    mom emo-62 "Я готова. А чего тут стоишь?"
    m emo-4 "Можешь на кровати продемонстрировать себя?"
    mom emo-75 "[pname_max[0]], ты и так хорошо знаешь моё тело..."
    m emo-3 "А я тогда подумаю, что больше всего хочу..."
    mom emo-67 "Ну хорошо."
    scene pgn_horelroom_bw_mom_25_vezdessushij
    mom emo-69 "Тебе нравится мамина киска?"
    if mom_path >= 13:
        scene pgn_horelroom_bw_mom_26_vezdessushij
        mom emo-69 "А как насчёт анала? Тебе же хочется оказаться внутри этой узкой и манящей дырочки и довести свою маму до бешенного оргазма?"
    if mom_path == 12.7:
        if restgn_drunk == 1:
            $ label_random = renpy.random.randint ( 1, 5)
        if restgn_drunk == 2:
            $ label_random = renpy.random.randint ( 1, 4)
        if restgn_drunk == 3:
            $ label_random = renpy.random.randint ( 2, 3)
        if restgn_drunk == 4:
            $ label_random = 3
        if label_random == 3:
            scene pgn_horelroom_bw_mom_26_vezdessushij
            mom emo-71 "Я знаю чего хочется моему сыну. Ты хочешь мою попку?"
            m emo-16 "Да!!!"
            mom emo-62 "Тогда ложись на кровать, мой ненасытный и похотливый мальчик."
            jump pgn_goldenight_date_mom_hotelroom_anal
    if ("gn_bath_bj") not in ivent24:
        scene pgn_horelroom_bw_mom_27_vezdessushij
        mom emo-68 "Или может быть я ублажу своего любимого сына этими губками?"
    if mom_path >= 13 or ("gn_bath_bj") not in ivent24:
        mom emo-75 "В какую дырочку тебе больше всего хочется засунуть своего крепыша?"
        menu:
            "Анал" if mom_path >= 13:
                jump pgn_goldenight_date_mom_hotelroom_anal
            "Вагинал":
                jump pgn_goldenight_date_mom_hotelroom_vag
            "Минет" if ("gn_bath_bj") not in ivent24:
                scene pgn_horelroom_bw_mom_28_vezdessushij
                mom emo-67 "Хорошо. Мамочка поработает ртом и языком."
                scene pgn_horelroom_bw_mom_29_vezdessushij
                mom emo-62 "Какой он у тебя горячий."
                m emo-3 "Мам..."
                mom emo-62 "Сейчас, сейчас..."
                scene animated pgn_date_mom_hotelroom_bw_bj_01
                $ renpy.pause()
                m emo-7 "Мама.... Я уже скоро..."
                scene pgn_horelroom_bw_mom_29_vezdessushij
                m emo-2 "Зачем ты остановилась?"
                mom emo-75 "Пока всё. Мне тоже нужно кончить."
    jump pgn_goldenight_date_mom_hotelroom_vag

label pgn_goldenight_date_mom_hotelroom_vag:
    scene animated pgn_date_mom_hotelroom_bw_vag_01
    $ renpy.pause()
    mom emo-68 "Охх... Ммм.. Малыш... Глубже..."
    mom emo-75 "Кончи внутрь... Я хочу внутрь... Почувствовать всё твоё тепло внутри..."
    m emo-4 "Да, Мам..."
    scene pgn_horelroom_bw_mom_32_vezdessushij
    if pgnach_124.aopen == False:
        $ PGN_Achadd(pgnach_124, 124)
    m emo-12 "Аргхх... Ммм... Ахххх..."
    scene pgn_horelroom_bw_mom_33_vezdessushij
    mom emo-75 "Люблю тебя. Это мой лучший вечер."
    m emo-4 "И не последний. Может ещё?"
    mom emo-67 "Уже поздно и хочу спать."
    m emo-0 "Ладно."
    if pgn_ach_repeat == 124:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 0, 0, 0, 1, 0)
    scene pgn_horelroom_bw_mom_43_vezdessushij
    $ renpy.pause(5, hard=True)
    jump pgn_goldenight_date_mom_hotelroom_v3

label pgn_goldenight_date_mom_hotelroom_anal:
    scene pgn_horelroom_bw_mom_34_vezdessushij
    mom emo-62 "Устраивайся поудобнее."
    scene pgn_horelroom_bw_mom_35_vezdessushij
    mom emo-69 "Сынок. Моя попка ещё плохо натренирована, так что, входи медленно."
    mom emo-69 "Вот... Ммм... так."
    scene animated pgn_date_mom_hotelroom_bw_anal_01
    $ renpy.pause()
    mom emo-68 "[pname_max[0]]... Сынок... Трахай меня..."
    mom emo-62 "Да, да, да... Мамочке нравится.... Да..."
    mom emo-69 "Ммм... ещё чуть-чуть..."
    scene pgn_horelroom_bw_mom_37_vezdessushij
    if pgnach_125.aopen == False:
        $ PGN_Achadd(pgnach_125, 125)
    mom emo-68 "Ааааххх... Да.... Аааххх..."
    scene pgn_horelroom_bw_mom_38_vezdessushij
    mom emo-71 "О да! Ааахх... Как же это классно в попу..."
    if mom_path == 12.7:
        m emo-9 "{i}Вау! Я впервые увидел как мама так бурно кончает. От обычного секса у неё не было такого оргазма.{/i}"
        m emo-4 "{i}Класс! Значит от анального секса она не сможет больше отказываться.{/i}"
    scene pgn_horelroom_bw_mom_39_vezdessushij
    mom emo-75 "Ох... Боже... Сынок... Я кончила от анального секса."
    m emo-4 "Ага."
    mom emo-69 "Позволь мне немного отдышаться и продолжим."
    if mom_path == 12.7:
        m emo-6 "А ты справишься?"
    scene pgn_horelroom_bw_mom_40_vezdessushij
    mom emo-62 "Я должна отблагодарить тебя за этот вечер и помочь тебе кончить."
    mom emo-75 "Трахни свою сексуальную маму в попку."
    scene animated pgn_date_mom_hotelroom_bw_anal_01
    $ renpy.pause()
    m emo-10 "Мама... я сейчас кончу..."
    mom emo-62 "Кончи в мою попку."
    scene pgn_horelroom_bw_mom_36_6_vezdessushij
    m emo-12 "Аргх....Оххх..."
    scene pgn_horelroom_bw_mom_41_vezdessushij
    mom emo-62 "Спасибо. Ты доволен?"
    m emo-4 "Да."
    scene pgn_horelroom_bw_mom_42_vezdessushij
    mom emo-75 "Спокойной ночи и приятных снов, мой дорогой и любимый мальчик."
    if pgn_ach_repeat == 125:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 1, 0, 0, 0, 0)
    if mom_path == 12.7:
        $ mom_path = 13
    scene pgn_horelroom_bw_mom_43_vezdessushij
    $ renpy.pause(5, hard=True)
    jump pgn_goldenight_date_mom_hotelroom_v3

label pgn_goldenight_date_mom_hotelroom_v3:
    scene pgn_horelroom_bw_mom_44_vezdessushij
    mom emo-62 "{i}Не буду его будить, пусть спит. Он этого заслужил.{/i}"
    $ daysnchange()
    call max_sleep_reset from _call_max_sleep_reset_3
    $ qtime = 9
    jump loc_pool





label pgn_goldenight_date_mom_rest_dialogue:
    scene pgn_hotel_gn_mom_07_petruha
    mom emo-62 "О чём поговорим?"
    $ restgn_drunkalc -= 1
    $ restgn_drunk += 1
    menu:
        "Звуки из маминой комнаты" if mom_path < 13 and ("restgn_q_1") not in ivent24:
            m emo-0 "Мам, я слышал по ночам какие-то звуки из твоей комнаты."
            mom emo-60 "Звуки?"
            m emo-0 "Ты была там с [pname_kira[4]]?"
            mom emo-73 "Да, с ней..."
            m emo-3 "Что вы там делали?"
            m emo-4 "{i}Я прекрасно знаю, что. Может она всё же расскажет.{/i}"
            if restgn_drunk == 4:
                mom emo-68 "Ну сам подумай, что могут делать две голые и сексуальные дамы."
                mom emo-68 "Ик..."
                mom emo-62 "Конечно развлекаться..."
            if restgn_drunk >= 5:
                mom emo-69 "Она меня учила новому виду секса. Вот."
                mom emo-73 "А больше ничего не скажу.... Это секрет."
            else:
                mom emo-73 "Просто болтали на разные темы. Вспоминали былое."
            $ ivent24.append("restgn_q_1")
        "Сегодня, повеселимся?" if mom_path >= 13 and ("restgn_q_2") not in ivent24:
            mom emo-62 "Тсс... не нужно об этом так громко говорить."
            mom emo-73 "Если проследишь за тем, чтобы я сильно не напивалась, то думаю да, можно будет"
            $ ivent24.append("restgn_q_2")
        "Просто о чём-нибудь":
            scene pgn_hotel_gn_mom_07_petruha
            $ renpy.pause(4, hard=True)
    show pgn_hotel_gn_mom_07_wine
    jump menu_pgn_goldenight_date_mom_rest_dialogue_wine


    menu menu_pgn_goldenight_date_mom_rest_dialogue_wine:
        "Заказать ещё вина?" if restgn_drunkalc == 0:
            if restgn_drunk <= 4:
                $ label_random = renpy.random.randint ( 1, 4)
                if label_random == 4:
                    m emo-0 "Ещё вино будешь?"
                    mom emo-62 "[pname_max[0]], спасибо. Но на сегодня мне хватит, сильно напиваться не хочу."
                    jump pgn_goldenight_date_mom_rest_next
                else:
                    mom emo-62 "Даже и не знаю. Но раз предлагаешь, почему бы и нет."
                    $ restgn_drunkalc += 1
                    scene pgn_hotel_gn_mom_05_petruha with dissolve
                    $ renpy.pause(1)
                    mom emo-62 "Спасибо"
                    jump pgn_goldenight_date_mom_rest_dialogue
            if restgn_drunk > 4 and restgn_drunk < 9:
                mom emo-68 "Твоя мама уже сильно пьяненькая."
                menu:
                    "Не переживай":
                        m emo-2 "Не волнуйся, я же здесь, я смогу тебя донести."
                        mom emo-75 "Ты? Меня? Донести? А поднимешь ли такую тяжёлую мамочку? Не смеши."
                        m emo-13 "Я серьёзно."
                        m emo-0 "Нам ещё вина принесите."
                        $ restgn_drunkalc += 1
                        scene pgn_hotel_gn_mom_05_petruha with dissolve
                        $ renpy.pause(1)
                        mom emo-62 "Спасибо"
                        jump pgn_goldenight_date_mom_rest_dialogue
                    "Счёт":
                        m emo-13 "Ладно. Думаю хватит."
                        jump pgn_goldenight_date_mom_rest_next
            if restgn_drunk >= 9:
                mom emo-73 "Мамочка больше не может пить, т.к. мамочка хочет писать."
                jump pgn_goldenight_date_mom_rest_next

        "Ещё вина?" if restgn_drunkalc > 0:
            if restgn_drunk >= 2 and restgn_drunk <= 4:
                $ label_random = renpy.random.randint ( 1, 5)
                if label_random == 4:
                    m emo-0 "Ещё вино будешь?"
                    mom emo-62 "[pname_max[0]], спасибо. Но на сегодня мне хватит, сильно напиваться не хочу."
                    jump pgn_goldenight_date_mom_rest_next
                else:
                    mom emo-62 "Да, если не против."
            if restgn_drunk > 4:
                mom emo-62 "Какой ты у меня хороший. Золотце. Мамочка тебя любит."
            else:
                mom emo-62 "С удовольствием."
            scene pgn_hotel_gn_mom_05_petruha with dissolve
            $ renpy.pause(1)
            mom emo-62 "Спасибо"
            jump pgn_goldenight_date_mom_rest_dialogue
        "Счёт":
            jump pgn_goldenight_date_mom_rest_next
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
