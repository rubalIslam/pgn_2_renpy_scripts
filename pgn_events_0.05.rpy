
label pgn_schgames_01:
    scene bg my_room_punishment_liza_07
    l emo-41 "[pname_max[0]]..."
    m emo-1 "Да, что такое?"
    l emo-48 "Как тебе сказать… Я хочу чего-то новенького, новых ощущений, что-то экстремальное и захватывающее… Не знаю даже как правильно описать."
    m emo-4 "Намекаешь, что уже пора лишиться девственности? Тебе понравится, как раз новые ощущения."
    l emo-42 "Нет, я не про это… И нет, [pname_max[0]], пока нет, моя киска тебе не достанется."
    m emo-0 "Тогда что? Я не понимаю тебя."
    l emo-49 "Допустим заняться сексом в публичном месте, где нас могут заметить... Ну… ты подумай."
    m emo-3 "Хорошо, я понял. Постараюсь."
    $ liza_path = 6
    $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
    $ qtime += 1
    $ lizasex_alice = True
    $ liza_sex_bj = 4
    $ veranda_punishment_liza_no = False
    $ liza_homework_error = False
    jump loc_my_room


label pgn_schgames_02:
    scene bg other_location_school_visit_01
    m emo-3 "{i}Школа... Моя школа не была такой большой, но нам хватало, бегали по этажам и коридорам, девчонкам юбки задирали...\nХватит воспоминаний, напишу [pname_liza[2]].{/i}"
    m emo-8 "{i}Блин. Её телефон недоступен. Попробую найти её класс.{/i}"
    scene bg other_location_school_visit_02
    other emo-999 "Молодой человек, куда мы направляемся?"
    scene bg other_location_school_visit_03
    m emo-3 "О... Здравствуйте. Здесь учится моя сестра и мне нужно ей кое-что сообщить."
    other emo-999 "Почему бы вам не отправить ей СМС или позвонить?"
    m emo-13 "Дело в том, что её телефон недоступен, видимо разряжен, поэтому не могу до неё дозвониться."
    other emo-999 "Простите, но я не могу позволить вам разгуливать по школе без разрешения учителя или директора."
    m emo-0 "Тогда извините, я пойду.\n {i}Блин, нужно придумать способ, как получить это разрешение.{/i}"
    $ liza_path = 8
    jump loc_pool_move

label pgn_schgames_03:
    if qtime != 17:
        scene bg pgn_home_momroom_01
        m emo-123 "..."
        m emo-123 "{i}Всё так же, ничего... совсем...{/i}"
        $ qtime += 1
        jump loc_my_room
    if qtime == 17 and liza_path == 9:
        scene bg pgn_home_momroom_01
        m emo-123 "..."
        m emo-123 "{i}Всё так же, ничего... совсем...{/i}"
        play sound "content/audio/confident.mp3" noloop
        m emo-123 "{i}Так, стоп! Мама направляется к столу. Думал ей по почте пришлют, хотя ноут только у меня и у...{/i}"
        scene bg pgn_home_momroom_phone_01
        $ renpy.pause ( 2, 0)
        scene bg pgn_home_momroom_phone_02
        m emo-123 "{i}Отлично, теперь знаю, где лежит мамин телефон и... теперь есть время. Но лучше мне для подстраховки ещё раз проверить, всегда ли в 17:00 приходит сообщение.{/i}"
        $ ivent24.append("лизашкола_слежка_за_мамой")
        $ liza_path, qtime = 10, qtime+1
        jump loc_my_room
    if qtime == 17 and liza_path == 10:
        scene bg pgn_home_momroom_01
        m emo-123 "..."
        m emo-123 "{i}Всё так же, ничего... совсем...{/i}"
        play sound "content/audio/confident.mp3" noloop
        m emo-123 "{i}СМС снова пришло в 17:00.{/i}"
        scene bg pgn_home_momroom_phone_01
        $ renpy.pause ( 2, 0)
        scene bg pgn_home_momroom_phone_02
        if daysn < 5:
            m emo-123 "{i}Тогда сегодня последний раз пишем домашку с ошибками, а завтра в это же время Маму нужно будет чем-то отвлечь.{/i}"
        if daysn == 5:
            m emo-123 "{i}Тогда сегодня последний раз пишем домашку с ошибками, а в понедельник в это же время Маму нужно будет чем-то отвлечь.{/i}"
        $ ivent24.append("лизашкола_слежка_за_мамой")
        $ liza_path, qtime = 11, qtime+1
        jump loc_my_room


label pgn_schgames_04:
    m emo-0 "Ты же помнишь, о чём просила меня недавно?"
    l emo-41 "Да. А при чём тут моя домашняя работа?"
    m emo-0 "Так надо, так что сделай как можно больше ошибок в своем задании."
    l emo-46 "[pname_max[0]], нет! Не знаю, что ты там придумал, но я не хочу, чтобы Мама шлепала меня по попе."
    m emo-11 "Если не сделаешь, я сам тебя сильно отшлепаю."
    l emo-50 "Ладно, ладно, хорошо. Сделаю, как ты скажешь."
    m emo-3 "Вот и умничка."
    $ liza_homework_error = True
    $ qtime += 1
    jump loc_my_room


label pgn_schgames_05:
    m emo-0 "[pname_liza[0]], тебе снова нужно сделать ошибки."
    l emo-42 "Сколько ещё это будет продолжаться? Мама больно бьёт, я не хочу больше."
    m emo-11 "[pname_liza[0]]!"
    l emo-42 "Нет!"
    m emo-8 "Аргх… Давай я тебе сделаю куни, а ты ошибки в задании. Так пойдёт?"
    l emo-49 "В попу…"
    m emo-0 "Что в попу?"
    l emo-49 "Я сделаю так, как ты сказал, а в замен трахнешь меня в попу."
    m emo-3 "Хорошо. Договорились."
    $ liza_homework_error = True
    jump loc_myroom_liza_homework_lazyharry_lpath


label pgn_schgames_06a:
    scene bg pgn_home_livroom_maxpfilm17t_a
    m emo-6 "{i}Так, чтобы такое включить, эротику или жесткое порно. Но так как мне нужно отвлечь Маму, то...{/i}"
    scene bg pgn_home_livroom_maxpfilm17t_b
    m emo-4 "{i}Поставлю это и звук погромче.{/i}"
    scene bg pgn_home_momroom_01
    m emo-123 "{i}...{/i}"
    mom emo-60 "Что за шум? Доносится с гостиной."
    scene bg pgn_home_momroom_02
    m emo-123 "{i}Она выходит и теперь мой выход.{/i}"
    scene bg pgn_home_momroom_maxtable17
    m emo-123 "{i}Где же он тут... А вот! Посмотрим.{/i}"
    play sound "content/audio/confident.mp3" noloop
    m emo-0 "А вот и СМС..."
    $ label_random = 1
    jump sms_olga_d1

label pgn_schgames_06a_next:
    scene bg pgn_home_momroom_maxtable17
    m emo-3 "{i}Отлично! Надо поскорее отсюда убираться и вечером сообщу [pname_liza[2]] хорошие новости.{/i}"
    $ qtime += 1
    $ liza_homework_error = False
    $ liza_path = 12
    jump loc_my_room


label pgn_schgames_06b:
    scene bg mom_room_massage_m2_10
    mom emo-69 "Ох, сынок... Кажется, я могу кончить за несколько секунд, если ты будешь продолжать..."
    play sound "content/audio/confident.mp3" noloop
    mom emo-60 "О, СМС пришло. Можешь посмотреть, что там?"
    m emo-3 "Да, конечно, сейчас."
    $ label_random = 2
    jump sms_olga_d1

label pgn_schgames_06b_next:
    scene bg mom_room_massage_m2_10
    m emo-3 "{i}Отлично! Надо заканчивать и вечером сообщу [pname_liza[2]] хорошие новости.{/i}"
    scene bg mom_room_massage_m2_10
    mom emo-60 "Что там было?"
    m emo-0 "Да так, спам из \"Richman\"."
    scene bg mom_room_massage_m1_05
    mom emo-60 "[pname_max[0]], ты опять так возбуждён... Как твои руки? Мази и таблетки помогают?"
    m emo-2 "Нет, всё ещё болят кисти рук..."
    mom emo-73 "Сочувствую тебе, сынок. Ладно, давай иди сюда, садись ко мне спиной. Помогу, раз тебе это доставляет такие боли. Даже не представляю как это неприятно..."
    m emo-2 "Угу..."
    scene bg mom_room_massage_m1_06
    mom emo-69 "Хоть бы никто не вошёл в комнату, пока мы тут с тобой. Даже не представляю как это всё объяснить... Поэтому, давай ускоримся. Ты готов?"
    m emo-3 "Конечно, мам!"
    scene bg mom_room_massage_m1_07
    mom emo-60 "Так хорошо, [pname_max[0]]? Может быть, чуть ускориться? Ты ко мне так прижимаешься... [pname_max[0]], надеюсь ты думаешь не обо мне? Хотя, ты не сознаешься... ладно, думай что хочешь..."
    m emo-4 "{i}Если бы я знал, что так можно, этот синдром у меня появился бы очень очень давно... Интересно, теперь мама всегда это будет делать? А может быть, будет и какое-то... развитие? Ох...{/i}"
    scene bg mom_room_massage_m1_08
    mom emo-75 "[pname_max[0]], я просто удивляюсь откуда в тебе столько спермы! Всю меня испачкал. Но не переживай, мама всё уберёт. Надевай свои шорты и иди, а я наведу порядок... И никому ни слова!"
    m emo-3 "Спасибо, мам!"
    $ liza_path = 12
    $ liza_homework_error = False
    $ PGN_Addstatsex(stat_mom, 0, 0, 0, 0, 1)
    $ ivent24.append("massage_m1")
    $ qtime += 1
    jump loc_mom_room


label pgn_schgames_07:
    scene bg my_room_punishment_liza_01
    l emo-40 "Странно, в этот раз Мама меня не наказывала, хотя я сделала всё, как ты просил."
    m emo-3 "Да, всё идёт по плану. Учительница вызвала Маму для разговора…"
    l emo-44 "Какого черта! Мне же влетит, ты всё только испортил."
    m emo-3 "Всё будет хорошо, вместо неё пойду я и уже всё схвачено."
    l emo-48 "А…. Да…. Скажи мне, что ты задумал."
    m emo-0 "Нет, пока это всё ещё секрет."
    if daysn < 5:
        l emo-40 "Ладно, тогда увидимся завтра в школе."
    if daysn >= 5:
        l emo-40 "Ладно, тогда увидимся на следующей неделе в школе."
    $ liza_path = 13
    jump loc_my_room


label pgn_schgames_08:
    scene bg other_location_school_visit_04
    other emo-999 "Пройти могут только учащиеся или работники школы."
    m emo-0 "Здесь учится моя сестра и сегодня меня вызвали в школу для разговора с учителем."
    other emo-999 "Даже если так, меня ни кто не предупреждал, так что всё равно пропустить вас не могу."
    m emo-11 "{i}Блин, ладно, напишу [pname_liza[2]], может он хотя бы ей поверит.{/i}"
    jump phone_max
label pgn_schgames_08_next:
    scene bg other_location_school_visit_04
    m emo-0 "Сейчас, она придёт сюда."
    scene bg other_location_school_visit_05
    l emo-41 "[pname_max[0]]!"
    m emo-3 "А вот и она."
    scene bg other_location_school_visit_06
    l emo-41 "Здравствуйте, это мой старший брат. Не могли бы его пропустить. Его вызывали для разговора с учительницей."
    other emo-999 "Хорошо, проходите. Но вы как-то слишком молоды для взрослого."
    m emo-0 "Спасибо. У каждого по-своему идут биологические часы..."
    scene bg school_addlessons_01
    $ renpy.pause ( 3, 0)
    m emo-13 "Она вообще придёт?"
    l emo-40 "Да"
    scene bg school_addlessons_02
    olga emo-182 "Простите! Навалилось много дел, совсем замоталась, чуть не забыла, что должна прийти. И так. Спасибо, что при…"
    scene bg school_addlessons_03
    olga emo-186 "[pname_max[7]]!?"
    scene bg school_addlessons_04
    m emo-3 "Здравствуйте Ольга Алексеевна. А вы тут какими судьбами и в этом городе?"
    olga emo-184 "Эм… ну… а… А ты почему здесь и как ты?"
    m emo-0 "Мама сообщила вам, что не сможет прийти и вместо неё придёт её сын. Ну вот, я здесь."
    scene bg school_addlessons_05
    olga emo-180 "Л-л-ладно. Не будем терять время. Думаю, ты в курсе, что твоя сестра идёт на золотую медаль, но если она и далее будет получать плохие оценки по моему предмету, то медали ей не видать. Чтобы как-то её снова вытянуть, ей потребуется ходить на дополнительные занятия и будет лучше, если будет присутствовать кто-нибудь из семьи."
    m emo-0 "У меня найдется свободное время и буду присутствовать на всех занятиях."
    scene bg school_addlessons_04
    olga emo-180 "Хорошо, тогда всё, так же по будням в 15:00. Буду ждать."
    m emo-3 "Не переживайте, я прослежу, чтобы она посещала эти занятия."
    $ PGN_Moveement_events (2, 6)
    scene bg pool_liza_swimming
    l emo-41 "[pname_max[0]], а откуда тебя знает Ольга Алексеевна?"
    m emo-0 "Помнишь, меня со школы выгнали, где мы раньше жили?"
    l emo-48 "Немного припоминаю."
    m emo-0 "Так вот, меня выгнали из-за неё. Из-за якобы приставаний, хотя это она положила глаз на меня. Всё так обыграла, будто это я был виноват. Наверное её оттуда уволили или сама ушла."
    l emo-44 "Ты смотри, чтобы меня не выгнали, а то уж точно поедешь служить в каких-то военных войсках за океаном."
    m emo-13 "Так, так, полегче, всё будет нормально, обещаю."
    l emo-40 "Ну, ну."
    $ qtime += 2
    $ liza_path = 14
    jump loc_pool


label pgn_schgames_09:
    scene bg other_location_school_visit_04
    m emo-0 "Я, на…"
    other emo-999 "Можете проходить, меня предупредили."
    m emo-4 "{i}Отлично, теперь могу без проблем заходить в школу. Осталось сделать задуманное, начну со следующего учебного дня.{/i}"
    scene bg school_addlessons_06
    m emo-3 "Здравствуйте, Ольга Алексеевна."
    olga emo-181 "Привет, [pname_max[0]]."
    m emo-0 "Где мне сесть?"
    olga emo-180 "Можешь сесть позади [pname_liza[1]]. И… пожалуйста, выключи телефон."
    m emo-0 "Хорошо. Поставлю на беззвучный режим."
    scene bg school_addlessons_07
    $ renpy.pause ( 4, 0)
    scene bg school_addlessons_07 with dissolve
    $ qtime += 2
    $ liza_school_addles -= 1
    $ liza_school_addles_fail = 0
    $ liza_path = 15
    $ PGN_Moveement_events (2, 6)
    jump loc_pool


label pgn_schgames_10:
    scene bg school_corridor2_firstmasha_01
    $ renpy.pause()
    scene black
    "БАМ!!!"
    m emo-0 "{i}Блин! Врезался во что-то мягкое...{/i}"
    scene bg school_corridor2_firstmasha_02
    m emo-3 "{i}О... Сиськи, большие, для школьницы...{/i}"
    ma emo-202 "Слышь, ты, глаза вверх поднял!"
    scene bg school_corridor2_firstmasha_03
    ma emo-200 "Ты не из нашей школы. Что здесь делаешь?"
    m emo-0 "С чего взяла?"
    ma emo-201 "Я бы не пропустила мимо себя такого красавчика."
    m emo-3 "Тут учится моя..."
    ma emo-200 "Мне без разницы кто. У меня сейчас нет времени на разговоры. В следующий раз увижу, так просто не отделаешься."
    scene bg school_corridor2_firstmasha_04
    m emo-6 "{i}Хм... Давно разрешено ходить в такой школьной, сексуальной форме!? Ладно, хватит фантазировать, я здесь для другого дела.{/i}"
    jump phone_max
label pgn_schgames_10_next:
    scene bg school_corridor2_liza_01
    $ renpy.pause(3, hard=True)
    scene bg school_corridor2_liza_02
    l emo-40 "[pname_max[0]], чего хотел? У меня идёт урок."
    m emo-0 "Пойдём."
    l emo-40 "Куда?"
    m emo-0 "Всё поймешь. Пойдём, пойдем."
    scene bg school_toilet_liza_01
    m emo-3 "Заходи..."
    l emo-41 "Чего задумал?"
    scene bg school_toilet_liza_02
    m emo-4 "Ты хотела острых ощущений и смены обстановки, ну так вот, давай займемся сексом прям в школьном туалете."
    l emo-40 "Я не могу."
    scene bg school_toilet_liza_03
    m emo-8 "Постой, ты же этого хотела или я не прав?"
    l emo-49 "Всё так, но мы не дома и у меня здесь нет возможности подготовить попу. Если только у тебя нет с собой презервативов. Или есть?"
    m emo-15 "Блин... Нет… "
    scene bg school_toilet_lizabj_01
    l emo-43 "Но я могу сделать тебе минет, всё же ты старался и придумал такой план. Только… моя попка пострадала от маминых шлепков... \nИ пожалуйста, не кончай мне на лицо, не могу ведь со спермой на лице пойти в класс."
    m emo-4 "Всё зависит о тебя, сможешь ли всё проглотить. А твоей маленькой пострадавшей попкой, займусь в следующий раз."
    scene animated school_toilet_lizabj_1
    m emo-10 "О да... Охх... Молодец сестренка... Как же хорошо..."
    m emo-4 "[pname_liza[0]], будь умницей, глубже..."
    scene animated school_toilet_lizabj_2
    m emo-7 "О-о-о даааа... Ммм... Как глубоко..."
    m emo-10 "{i}От ощущений, что нас могут поймать за этим делом... Как же меня это возбуждает... Больше не могу...{/i}"
    scene bg school_toilet_lizabj_anim_06
    m emo-12 "Ааахх... Дааа... Аааа..."
    m emo-4 "Открой ротик и покажи мне..."
    scene bg school_toilet_lizabj_02
    if pgnach_95.aopen == False:
        $ PGN_Achadd(pgnach_95, 95)
    m emo-3 "Отлично! А теперь проглоти..."
    scene bg school_toilet_lizabj_03
    m emo-4 "Умничка"
    l emo-41 "Ммм... горячее и вкусное. Спасибо [pname_max[0]]! Мне очень понравилось. Надеюсь в следующий раз не забудешь взять презервативы."
    scene bg school_toilet_liza_04
    m emo-4 "Может забудешь, что здесь произошло и не расскажешь об этом [pname_alice[2]]?"
    l emo-41 "Согласна. Но ни чего не обещаю, что может случиться дома."
    scene bg school_toilet_liza_03
    m emo-3 "Ну всё, беги на урок."
    if liza_path == 15:
        play sound "content/audio/long_expected.mp3" noloop
        $ renpy.notify(str(task_notifi[12])+": "+str(condom.name))

        $ condom.instore = True
    if liza_school_addles > 0 and liza_schaddles == True and pgn_ach_repeat == 0:
        l emo-41 "Ты же придёшь сегодня на дополнительные? Мне осталось занятий [liza_school_addles]."
        m emo-0 "Конечно, сестрёнка."
    if pgn_ach_repeat == 95:
        jump table_pgn_achievement
    $ qtime += 1
    $ liza_sex_bj = 4
    $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
    $ liza_path = 16
    jump loc_school_et1_toilet_g


label pgn_schgames_11:
    scene black
    l emo-41 "[pname_max[0]], ты где?... Ой..."
    scene bg school_toilet_liza_02
    l emo-49 "Ну зачем так грубо?"
    scene bg school_toilet_lizaanal_01
    m emo-3 "Умничка, без трусиков..."
    l emo-41 "С того раза, как обещала их не надевать, не надеваю. А раз будешь меня ещё и в школе радовать, то уж точно они мне не понадобятся."
    l emo-49 "Презервативы у тебя?"
    m emo-0 "Конечно. В СМС написал, что есть. Снимай юбку и встань раком на унитаз."
    scene bg school_toilet_lizanl_anim1_01
    m emo-0 "Готова?"
    l emo-49 "Даааа..."
    $ anim_speed = 0.5
    scene animated school_toilet_lizanl_anim2
    l emo-49 "Аххх... Мммм... Ааааххх... Да, вот так... Мммм..."
    m emo-7 "О дааа... Люблю твою попку, сестренка, в ней очень узко... Эта маленькая дырочка обхватывает весь мой член..."
    m emo-10 "Как же я тебя люблю..."
    scene animated school_toilet_lizanl_anim2
    l emo-46 "[pname_max[0]], заткнись! Я не хочу, чтобы нас заметили, так что трахай меня... Ааххх, да, да... Аааххх..."
    l emo-49 "Поактивнее братик... Аххх..."
    $ anim_speed = 0.5
    scene animated school_toilet_lizanl_anim2
    l emo-49 " О да... Большой член братика в моей попке... Быстрее... Аааххх..."
    m emo-3 "{i}Ну [pname_liza[0]], меня заткнула, а сама говорит, да стонет громко. Хорошо, что ни кого нет кроме нас в туалете.{/i}"
    scene animated school_toilet_lizanl_anim1
    l emo-49 "Аааххх... Аааххх... Ммм..."
    m emo-10 "[pname_liza[0]]... Я... так долго не продержусь..."
    l emo-46 "Тогда... ещё быстрее и глубже, старший братик... Глуу-глу-бже..."
    $ anim_speed = 0.2
    scene animated school_toilet_lizanl_anim2_1
    l emo-50 "Аааххх... [pname_max[0]]!!! Ааааххх..."
    m emo-12 "Больше... не могу... Аааргхх..."
    scene bg school_toilet_lizanl_anim1_06
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim1_05
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim1_04
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim1_06
    if pgnach_96.aopen == False:
        $ PGN_Achadd(pgnach_96, 96)
    m emo-7 "Всё! Ухх... Жаль нельзя было кончить в попку."
    l emo-41 "Можешь, но дома. А так, спасибо и за это. И не волнуйся, [pname_alice[2]] не скажу."
    l emo-41 "Ну всё, я пошла в класс."
    if liza_school_addles > 0 and liza_schaddles == True and pgn_ach_repeat == 0:
        l emo-41 "Ты же придёшь сегодня на дополнительные? Мне осталось занятий [liza_school_addles]."
        m emo-0 "Конечно, сестрёнка."
    m emo-3 "Ещё увидимся."
    if pgn_ach_repeat == 96:
        jump table_pgn_achievement
    $ ivent24.remove("liza_schtoilet_sex")
    $ ivent24.append("liza_schtoilet_sex_day")
    $ PGN_Addstatsex(stat_liza, 1, 0, 0, 0, 0)
    $ condom.numbsuse -= 1
    if condom.numbsuse == 0:
        $ condom.have = False
    $ liza_sex_bj = 4
    $ qtime += 1
    $ liza_path = 18
    jump loc_school_et1_toilet_g


label pgn_schgames_toiletsexliza:
label a:
    scene bg school_toilet_liza_01
    l emo-41 "Почему не в кабинке меня ждешь?"
    m emo-3 "Проверял, нет ли никого здесь."
    $ label_random = renpy.random.randint ( 1, 1)
    if label_random == 1:
        scene bg school_toilet_liza_02
        l emo-41 "Аххх..."
    if label_random == 2:
        scene bg school_toilet_liza_03
    if stat_liza.stsex_all > stat_alice.stsex_all:
        m emo-4 "Чего хочется моей маленькой и самой любимой сестренке?"
    else:
        m emo-4 "Красотка, чего тебе хочется?"
    l emo-49 "Хочу в попу или твоей спермы в моём ротике, так что даже и не знаю. Решай сам."
    $ menu_hbox = True
    menu:
        "Минет":
            jump pgn_schgames_toiletsexliza_p1
        "В попу":
            jump pgn_schgames_toiletsexliza_p2
label pgn_schgames_toiletsexliza_p1:
    $ PGN_Addstatsex(stat_liza, 0, 0, 1, 0, 0)
    scene bg school_toilet_lizabj_01
    m emo-4 "{i}Какая же она миленькая. Нежные и мягкие губки сестренки... большая потеря, не трахнуть этот ротик.{/i}"
    scene animated school_toilet_lizabj_1
    m emo-10 "О да... Охх... Молодец сестренка... Как же хорошо..."
    m emo-3 "Если не хочешь долго задерживаться, то тебе лучше ускориться и взять поглубже..."
    scene animated school_toilet_lizabj_2
    m emo-7 "О-о-о даааа... Ммм... Как глубоко..."
    m emo-4 "{i}Мама и Тётя мастерски сосут, но вот [pname_liza[0]] делает это нижнее... Охх....{/i}"
    m emo-10 "[pname_liza[0]], я... сейчас..."
    scene bg school_toilet_lizabj_anim_06
    m emo-12 "Ааахх... Дааа... Аааа..."
    m emo-4 "Открой ротик и покажи мне..."
    scene bg school_toilet_lizabj_02
    m emo-3 "Вау, супер! Проглоти и слижи с губ..."
    scene bg school_toilet_lizabj_03
    m emo-4 "Умничка."
    l emo-41 "Ммм... горячее и вкусное. Спасибо [pname_max[0]]! Мне очень понравилось."
    if condom.have == True:
        scene bg school_toilet_liza_04
        m emo-4 "Точнее не хочешь продолжить?"
        l emo-48 "Я и так задержалась, нужно побыстрее вернуться на урок."
    else:
        scene bg school_toilet_liza_03
        m emo-3 "Ну всё, беги на урок."
    if liza_school_addles > 0 and liza_schaddles == True:
        l emo-41 "Ты же придёшь сегодня на дополнительные? Мне осталось занятий [liza_school_addles]."
        m emo-0 "Конечно, сестрёнка."
    jump pgn_schgames_toiletsexliza_end

label pgn_schgames_toiletsexliza_p2:
    $ PGN_Addstatsex(stat_liza, 1, 0, 0, 0, 0)
    $ condom.numbsuse -= 1
    if condom.numbsuse == 0:
        $ condom.have = False
    m emo-4 "{i}Ни за что бы не подумал, что когда-нибудь займусь сексом в туалете.{/i}"
    m emo-0 "Снимай юбку и встань раком на унитаз."
    scene bg school_toilet_lizanl_anim1_01
    m emo-0 "Готова?"
    l emo-49 "Даааа... Только осторожно, сразу и резко не надо."
    m emo-4 "Хорошо."
    $ menu_hbox = True
    menu:
        "Продолжить":
            pass
        "Войти грубо и глубоко":
            jump pgn_schgames_toiletsexliza_p2_grubo
    $ anim_speed = 0.6
    scene animated school_toilet_lizanl_anim1
    l emo-49 "Аххх... Мммм... Ааааххх... Да, вот так... Мммм..."
    m emo-7 "О дааа... Люблю твою попку, сестренка, в ней очень узко... Как же я тебя люблю..."
    $ anim_speed = 0.6
    scene animated school_toilet_lizanl_anim2
    l emo-49 "Поактивнее братик... Аххх..."
    $ anim_speed = 0.4
    scene animated school_toilet_lizanl_anim2
    l emo-49 " О да... Большой член братика в моей попке... Быстрее... Аааххх..."
    $ anim_speed = 0.4
    scene animated school_toilet_lizanl_anim1
    l emo-49 "Аааххх... Аааххх... Ммм..."
    m emo-10 "[pname_liza[0]]... Я... так долго не продержусь..."
    l emo-46 "Тогда... ещё быстрее и глубже, старший братик... Глуу-глу-бже..."
    $ anim_speed = 0.2
    scene animated school_toilet_lizanl_anim2_1
    l emo-50 "Аааххх... [pname_max[0]]!!! Ааааххх..."
    m emo-12 "Больше... не могу... Аааргхх..."
    scene bg school_toilet_lizanl_anim1_06
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim1_05
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim1_04
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim1_06
    m emo-7 "Всё! Ухх..."
    scene bg school_toilet_liza_04
    l emo-41 "Спасибо! Мне очень понравилось... Не буду ещё дольше задерживаться, мне пора."
    if liza_school_addles > 0 and liza_schaddles == True:
        l emo-41 "Ты же придёшь сегодня на дополнительные? Мне осталось занятий [liza_school_addles]."
        m emo-0 "Конечно, сестрёнка."
    m emo-3 "Ещё увидимся."
    jump pgn_schgames_toiletsexliza_end

label pgn_schgames_toiletsexliza_p2_grubo:
    if alice_path < 17:
        $ lizasex_alice = True
    $ PGN_Addstatsex(stat_liza, 1, 0, 0, 0, 0)
    $ condom.numbsuse -= 1
    if condom.numbsuse == 0:
        $ condom.have = False
    $ anim_speed = 0.2
    scene animated school_toilet_lizanl_anim3
    l emo-50 "Ай, [pname_max[0]], нет! Я же просила..."
    l emo-50 "Всё расскажу [pname_alice[2]]..."
    m emo-3 "{i}Ну и ладно пусть знает, зато отлично проведу время с этой маленькой попкой. Ооо... да...{/i}"
    m emo-16 "Класс! Тугая и очень горячая дырочка... Дааа... Аааххх..."
    call screen pgn_schgames_toiletsexliza_grubo_choicepose
label pgn_schgames_toiletsexliza_p2_grubo_01:
    scene animated school_toilet_lizanl_anim3
    l emo-46 "Глу-бо-ко... очень... Аа...Ааааа..."
    call screen pgn_schgames_toiletsexliza_grubo_choicepose
label pgn_schgames_toiletsexliza_p2_grubo_02:
    scene animated school_toilet_lizanl_anim1
    l emo-49 "Ааахх... Аааа... Больно... Аааххх..."
    call screen pgn_schgames_toiletsexliza_grubo_choicepose
label pgn_schgames_toiletsexliza_p2_grubo_03:
    scene animated school_toilet_lizanl_anim3_1
    l emo-49 "Мммм... Ааахх... Ааааххх..."
    call screen pgn_schgames_toiletsexliza_grubo_choicepose
label pgn_schgames_toiletsexliza_p2_grubo_end:
    m emo-12 "Больше... не могу... Аааргхх..."
    scene bg school_toilet_lizanl_anim3_06
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim3_05
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim3_04
    $ renpy.pause ( 1, 0)
    scene bg school_toilet_lizanl_anim3_01
    l emo-42 "За это, [pname_alice[0]], тебе по жопе надаёт..."
    m emo-4 "Беги на урок, а то всё пропустишь."
    l emo-44 "Дурак."
    jump pgn_schgames_toiletsexliza_end

label pgn_schgames_toiletsexliza_end:
    $ ivent24.remove("liza_schtoilet_sex")
    $ ivent24.append("liza_schtoilet_sex_day")
    $ liza_sex_bj = 4
    $ qtime += 1
    if olivia_path == 0 and liza_path >= 40 and pornfilm_g >= 11:
        jump pgn_newolivhome_01
    jump loc_school_et1_toilet_g

screen pgn_schgames_toiletsexliza_grubo_choicepose:
    vbox:
        xalign 1.0
        yalign 0.5
        imagebutton idle "images/nav/sex_camera1_a.png" hover "images/nav/sex_camera1_b.png" action Jump("pgn_schgames_toiletsexliza_p2_grubo_03")
        null height 20
        imagebutton idle "images/nav/sex_camera2_a.png" hover "images/nav/sex_camera2_b.png" action Jump("pgn_schgames_toiletsexliza_p2_grubo_01")
        null height 20
        imagebutton idle "images/nav/sex_camera3_a.png" hover "images/nav/sex_camera3_b.png" action Jump("pgn_schgames_toiletsexliza_p2_grubo_02")
        null height 20
        imagebutton idle "images/nav/sex_cum_a.png" hover "images/nav/sex_cum_b.png" action Jump("pgn_schgames_toiletsexliza_p2_grubo_end")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
