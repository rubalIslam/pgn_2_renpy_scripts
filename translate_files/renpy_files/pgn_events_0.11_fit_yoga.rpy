







label pgn_alice_room_dressing:
    scene pgn_alice_drassing_city_01
    a emo-24 "[pname_max[0]]! Я вообще-то здесь переодеваюсь."
    m emo-0 "Переодевайся, а я посмотрю."
    scene pgn_alice_drassing_city_02
    m emo-3 "Ты же не против?"
    a emo-20 "Делай что хочешь, только мне не мешай."
    scene pgn_alice_drassing_city_03
    m emo-4 "Секси, сейчас бы тебя..."
    a emo-29 "[pname_max[0]]!"
    m emo-1 "Что? Я же тебе не мешаю."
    scene pgn_alice_drassing_city_04
    m emo-4 "Ух... Хорошая попка..."
    a emo-21 "Спасибо."
    scene pgn_alice_drassing_city_05
    if alice_path == 18 and blackcard.have == True:
        m emo-6 "{i}Она постоянно куда-то уходит, только неизвестно куда. Может спросить?{/i}"
        menu:
            "Узнать":
                m emo-6 "А ты сейчас куда идёшь?"
                a emo-20 "Не твоё дело."
                m emo-8 "Почему это? Мы теперь партнёры по бизнесу и я твой брат, так что должен знать. Вдруг что случится."
                a emo-22 "Ой! Кто себя тут считает старшим, хотя младше меня и даже школу не закончил."
                m emo-1 "Ну так, скажешь?"
                a emo-33 "К Кате иду. Больше ничего не скажу."
                m emo-1 "А что вы будете делать, можно с вами?"
                a emo-33 "Всё я побежала, позже увидимся."
                $ alice_path = 18.1
                $ qtime = 12
                jump loc_alice_room
            "В другой раз":
                pass
    a emo-33 "Ну всё, я готова. Как я тебе?"
    m emo-3 "Выглядишь отлично!"
    a emo-21 "Ладно, мне пора. Без меня не скучай!"
    m emo-3 "Ага..."
    $ qtime = 12
    jump loc_alice_room


label pgn_events_11_alicefitness_01:
    scene pgn_11_alicespyfit_01
    m emo-0 "{i}[pname_alice[0]] вышла из комнаты, попробую за ней незаметно проследить.{/i}"
    scene pgn_11_alicespyfit_02
    m emo-0 "{i}Я тень, тень.{/i}"
    scene pgn_11_alicespyfit_03
    if alice_path == 18.1:
        m emo-6 "{i}Она кого-то ждёт или ждёт автобус? Она же знает, что у меня есть транспорт, могла бы попросить подбросить, всё равно делать мне нечего.{/i}"
    if alice_path == 18.2:
        m emo-0 "{i}Зачем тратить деньги на проезд, когда есть я?{/i}"
    scene pgn_11_alicespyfit_04
    m emo-1 "{i}Садится в автобус... Блин, блин.... Мне же тоже нужно.{/i}"
    scene pgn_11_alicespyfit_05
    m emo-3 "{i}Успел{/i}"
    scene pgn_11_alicespyfit_06
    if alice_path == 18.1:
        m emo-8 "{i}Блин, встала тут, места много, а она именно тут в стала и обзор весь закрыла{/i}"
    if alice_path == 18.2:
        m emo-8 "{i}Опять{/i}"
    other emo-998 "Проезд оплачиваем."
    scene pgn_11_alicespyfit_07
    $ screennotify("$",6,5)
    $ currency -= 5
    $ renpy.pause(5)
    scene pgn_11_alicespyfit_08
    if alice_path == 18.1:
        other emo-998 "Понарожали извращенцев..."
    if alice_path == 18.2:
        other emo-998 "Извращенец."
    scene pgn_11_alicespyfit_05
    $ renpy.pause(4, hard=True)
    if daysn != 1 and daysn != 3 and daysn != 5:
        scene pgn_11_alicespyfit_16
        m emo-0 "{i}Снова ничего не вижу.{/i}"
        other emo-998 "Привет."
        m emo-0 "Привет."
        other emo-998 "Ты не против, если я..."
        scene pgn_11_alicespyfit_17
        m emo-9 "{i}Ох... нифига себе. Вот это безбашенная. Совсем не стесняясь показывает свои прелести.{/i}"
        scene pgn_11_alicespyfit_18
        m emo-9 "{i}Охренеть, ещё и мастурбирует.{/i}"
        scene pgn_11_alicespyfit_16
        other emo-998 "Спасибо"
        scene pgn_11_alicespyfit_05b
        m emo-8 "Блин! Я пропустил, когда она вышла. Попробую в другой день."
        $ alice_path = 18.2
        $ qtime = 13
        $ PGN_Transport_None()
        jump loc_mall
    scene pgn_11_alicespyfit_09
    m emo-6 "{i}Выходит. Только я не заметил, куда мы приехали.{/i}"
    scene pgn_11_alicespyfit_10
    m emo-0 "{i}И куда это мы идём?{/i}"
    scene pgn_11_alicespyfit_11
    m emo-1 "{i}Она входит в здание... Так, стоп, это же...{/i}"
    scene pgn_hotel_day
    m emo-6 "{i}Отель! Что она там забыла!? Всё интересней и интересней. Она там работает или что?{/i}"
    scene pgn_11_alicespyfit_12
    m emo-6 "{i}Хм... и от куда у неё доступ к лифту? Кажись и правда, работает. А тогда зачем скрывать об этом, от нас?{/i}"
    scene pgn_11_alicespyfit_13
    m emo-0 "{i}Поднялась до 2-го этажа. Значит не горничная и не в чей-то номер. Жаль... а так бы мог заснять её в форме горничной.{/i}"
    scene pgn_11_alicespyfit_14
    m emo-8 "{i}Блин. Я её потерял. Куда она ушла?{/i}"
    victor emo-400 "Что-то потерял?"
    scene pgn_hotel_2et_recep_admin_02
    m emo-8 "Эм..."
    victor emo-401 "Ты здесь чтобы подкачаться? По тебе видно, что этого не хватает. Накачаешь мышцы и от тёлок отбоя не будет."
    m emo-6 "{i}У меня и так проблем с этим нет. Нафиг мне качаться...{/i}"
    victor emo-401 "Ну так что, будем оформляться?"
    m emo-13 "Нет... Спасибо..."
    ka emo-151 "[pname_alice[0]], тебе нужно побольше тренироваться. Мне нужно быть с тобой по строже."
    m emo-6 "{i}Знакомый голос...{/i}"
    scene pgn_11_alicespyfit_15
    m emo-3 "{i}И знакомые попки...{/i}"
    a emo-29 "Так я занимаюсь спортом."
    ka emo-157 "Спорт по сексу? Секс это хорошо, но нужно и другие мышцы тренировать."
    a emo-20 "Да, ты права."
    scene pgn_hotel_2et_recep_admin_02
    m emo-0 "Пожалуй я возьму абонемент."
    menu:
        "Неделя - $150":
            $ Max.strength[0] = 5
            $ screennotify("$",11,150)
            $ currency -= 150
        "Две недели - $250":
            $ Max.strength[0] = 10
            $ screennotify("$",11,250)
            $ currency -= 250
        "Месяц - $400":
            $ Max.strength[0] = 20
            $ screennotify("$",11,400)
            $ currency -= 400
    victor emo-401 "Отлично. Правильный выбор. С завтрашнего дня можешь приходить."
    m emo-6 "А сегодня нельзя?"
    victor emo-400 "Нужно утрясти и ещё несколько моментов с оформлением, так что завтра или в любой другой день, когда удобно."
    $ ivent24.append("фитнес_куплен_абонемент")
    $ qtime = 13
    $ alice_path = 19
    jump loc_hotel_2et_recept


label pgn_fitness_max_coach_men_alicekate:
    $ Max.strength[0] -= 1
    $ Max.strength[4] += 1
    $ Max.strength[2] += 1
    $ ivent24.append("фитнес_занятия_были")
    scene pgn_fitness_max_coach_men_01_vezdessushij
    victor emo-400 "Привет [pname_max[0]]! Сейчас никак не могу провести с тобой занятия, у меня тут две клиентки. Так что извиняй. Можешь сам потренироваться. Только ничего себе не сломай."
    m emo-1 "Ок."
    if alice_path == 19:
        scene pgn_fitness_max_coach_men_alicekate_01
        a emo-24 "[pname_max[0]]!? Ты что тут делаешь?"
        ka emo-151 "О! А ты что здесь делаешь? Ты за нами шпионил?"
        m emo-8 "Я... Нет, нет, что ты. Вот захотелось подкачаться немного."
        ka emo-156 "Ну одна мышца у тебя очень хорошо натренирована."
        scene pgn_fitness_max_coach_men_alicekate_02
        m emo-1 "..."
        m emo-1 "[pname_alice[0]], а зачем ты от меня скрывала, что ходишь в фитнес-зал?"
        a emo-23 "Ну... это... Почему я должна тебе обо всём говорить?"
        ka emo-152 "Я согласна с тобой, [pname_alice[0]]. [pname_max[0]]. У девочек должны быть секреты. Если обо всём рассказывать, то будет совсем не интересно."
        ka emo-153 "Ладно. Поговорили немного, если захотите поговорите, то потом. А сейчас, [pname_alice[6]], нам нужно заняться укреплением своего тела."
        a emo-24 "Да, Катя. Конечно."
        ka emo-151 "[pname_max[0]]. Занимайся на тренажерах, и делай что хочешь, только нам не мешай."
        m emo-0 "Ок."
    scene pgn_fitness_max_coach_men_alicekate_03
    $ label_random = renpy.random.randint ( 1, 3)
    if label_random == 3:
        victor emo-401 "Девчонки. Ну что, начнём тренировку ваших попок."
        a emo-21 "Мы не против..."
        ka emo-152 "Но мы говорили и не раз, что мы лесбиянки."
        victor emo-401 "Да, да, помню. Начнём."
    else:
        victor emo-401 "Девчонки продолжим."
        ka emo-157 "Тренер, без тебя мы и не начинали. Нам не хватает сильной и мужской руки."
    m emo-8 "{i}Эх... жаль нельзя с ними, я бы их так натренировал, что в раздевалке сами накинутся на меня.{/i}"
    ka emo-157 "Ммм... Тренер. Продолжай."
    if alice_path == 19:
        m emo-6 "{i}Что он там с ней делает!?{/i}"
    scene pgn_fitness_max_coach_men_alicekate_04
    ka emo-156 "Ммм..."
    scene pgn_fitness_max_coach_men_alicekate_05
    victor emo-401 "Вставай на четвереньки, помогу с упражнением. Здесь потребуется поддержка."
    ka emo-151 "Если только это будут ваши мускулистые и крепкие руки."
    scene pgn_fitness_max_coach_men_alicekate_06
    victor emo-401 "Молодец. Так держать."
    scene pgn_fitness_max_coach_men_alicekate_07
    ka emo-159 "Без вас, тренер, у меня бы ничего не получилось."
    if alice_path == 19:
        m emo-11 "{i}Чёрт. Да он её лапает во всю. Да какой нахер он тренер!?{/i}"
    scene pgn_fitness_max_coach_men_alicekate_08
    victor emo-401 "Отлично, отлично. Класс. У тебя всё хорошо получается."
    scene pgn_fitness_max_coach_men_alicekate_09
    a emo-20 "Тренер. Я же всё правильно делаю? Тренер?"
    victor emo-400 "Эм... да, да, сейчас."
    if alice_path == 19:
        m emo-11 "{i}Блин! Сейчас он [pname_alice[3]] начнёт лапать. Вот гнида.{/i}"
    scene pgn_fitness_max_coach_men_alicekate_10
    if alice_path == 19:
        m emo-0 "{i}Фух! Вроде пронесло, он не трогает её за попу или сиськи. А не то бы я не выдержал и врезал ему по этой довольной роже.{/i}"
    else:
        m emo-0 "{i}Мне бы на его место.{/i}"
    scene pgn_fitness_max_coach_men_alicekate_11
    victor emo-401 "Отлично девочки. Давайте, нашу последнюю позу и на этом закончим."
    a emo-21 "Да тренер."
    ka emo-159 "Сейчас."
    scene pgn_fitness_max_coach_men_alicekate_12
    victor emo-401 "Отлично, отлично, молодцы... У вас всё лучшее и лучше получатся."
    if alice_path == 19:
        m emo-13 "{i}Ага, блин. Пялится через зеркало на их попки.{/i}"
        $ alice_path = 20
    victor emo-401 "На этом всё. До следующего раза."


    scene pgn_hote_women_locker_alicekate_01
    m emo-4 "{i}О! [pname_alice[0]] с Катей снова веселятся вместе, а меня даже не позвали.{/i}"
    ka emo-152 "Нам бы сейчас не помешала крепкая мужская рука. Да, [pname_alice[6]]?"
    m emo-6 "{i}Это они про своего тренера. Нет, нет, я [pname_alice[3]] никому не отдам.{/i}"
    menu:
        "Войти":
            $ scene_random = Max.strength[3] + Max.strength[4]
        "уйти":
            jump pgn_fitness_max_coach_end
label pgn_hote_women_locker_alicekate_arch:
    scene pgn_hote_women_locker_alicekate_02
    if scene_random < 8 and pgn_ach_repeat == 0:
        m emo-4 "Может быть лучше я вам предложу большой и крепкий член?"
        a emo-20 "[pname_max[0]]! Стучать нужно. И как ты открыл дверь?"
        m emo-0 "Она и была открыта."
        ka emo-150 "Спасибо за предложение, но мы тут сами."
        m emo-13 "А если хорошо подумать?"
        ka emo-151 "Хочешь, чтобы мы закричали, тогда тебе нехило достанется. А мы уж посмотрим, что с тобой будут делать."
        m emo-8 "Э-э-э... полегче. Ладно. Ухожу."
        ka emo-152 "Но... если хочешь в следующий раз составить нам компанию, то не помешало бы мышцы накачать."
        $ label_random = renpy.random.randint ( 1, 2)
        if label_random == 1:
            m emo-1 "Да есть у меня мышцы, подойди ближе и покажу."
        else:
            m emo-6 "А они тут причём? Дома же я вас устраиваю, а здесь что не так?"
        a emo-20 "[pname_max[0]]! Катя сказала тебе выйти, не слышал?"
        m emo-0 "Ухожу. Развлекайтесь."
        jump pgn_fitness_max_coach_end
    if scene_random >= 8 and alice_sex_kate > 0 and pgn_ach_repeat == 0:
        m emo-4 "Девчонки, не хотите поиграть с моим членом?"
        ka emo-155 "[pname_alice[0]]!"
        a emo-21 "[pname_max[0]]. Ты же знаешь, что секс с нами только раз в 3 дня."
        m emo-6 "Я думал, что это правило распространяется только на наш дом."
        ka emo-155 "Всё, уйди и не мешай. [pname_alice[6]] сейчас будет старательно лизать мою киску."
        m emo-1 "А можно хотя бы посмотреть?"
        a emo-20 "Нет."
        m emo-8 "Вот блин."
        jump pgn_fitness_max_coach_end
    ka emo-151 "О! Кто пришёл. Заходи, только дверь закрой."
    m emo-4 "Может с меня начнёте?"
    if scene_random >= 8 and scene_random < 12 and pgn_ach_repeat == 0:
        ka emo-153 "Тебе сейчас разрешается только смотреть и дрочить."
    if scene_random >= 12 or pgn_ach_repeat == 134:
        $ label_random = renpy.random.randint ( 1, 4)
        ka emo-153 "Тебе сейчас разрешается только смотреть и дрочить. А если не кончишь, то может что-нибудь и переподёт."
    m emo-3 "Ладно."
    scene pgn_hote_women_locker_alicekate_03
    ka emo-152 "Я от этих тренировок так перевозбудилась, что мне очень срочно нужно кончить. [pname_alice[0]], полижи мою киску."
    scene animated pgn_hote_women_locker_alicekate_04
    $ renpy.pause()
    if ((scene_random >= 8 and scene_random < 12) or (scene_random >= 12 and label_random == 4)) and pgn_ach_repeat == 0:
        m emo-7 "Девчонки. Сейчас кончу."
        a emo-20 "Не обкончай всю раздевалку."
        m emo-2 "А куда мне..."
        ka emo-153 "На нас, всё равно после в душ пойдём."
        scene pgn_hote_women_locker_alicekate_06
        m emo-12 "Аргх... Ааааа..."
        scene pgn_hote_women_locker_alicekate_05
        m emo-7 "О да... Ооооххх..."
        scene pgn_hote_women_locker_alicekate_07
        m emo-4 "Продолжим?"
        ka emo-151 "Хочешь продолжения?"
        m emo-3 "Да, я могу ещё, особенно с такими красивыми и сексуальными кисками."
        ka emo-152 "Спасибо, но продолжишь сам, в душе, один и своей рукой."
        m emo-13 "Может всё же?"
        ka emo-157 "[pname_alice[0]], решай, оставляем его или прогоняем?"
        a emo-22 "Ты знаешь, я сделаю всё, что ты пожелаешь."
        ka emo-151 "Значит, на выход. Мы тут дальше без тебя обойдёмся."
    else:
        ka emo-157 "[pname_alice[6]] не останавливайся, продолжай... Ещё немного..."
        scene pgn_hote_women_locker_alicekate_08
        ka emo-154 "Ааахххх... Аааа...."
        scene pgn_hote_women_locker_alicekate_03
        ka emo-159 "[pname_max[0]], теперь твоя очередь, заставить меня кончить."
        a emo-20 "Но я..."
        ka emo-151 "Ты молодец. Но если не против, я одолжу член твоего брата."
        a emo-20 "Хорошо."
        ka emo-152 "Давай [pname_max[0]], трахни меня в киску."
        scene pgn_hote_women_locker_alicekate_09
        m emo-6 "А если я хочу не только в киску?"
        ka emo-151 "Хочешь уйти от сюда со стояком?"
        m emo-2 "..."
        ka emo-151 "Так что давай, оттрахай меня"
        scene animated pgn_hote_women_locker_alicekate_10_1
        $ PGN_Achadd(pgnach_134, 134)
        $ renpy.pause()
        ka emo-156 "[pname_max[0]]... [pname_max[0]]... Трахай меня глубже и быстрее."
        scene animated pgn_hote_women_locker_alicekate_10_2
        $ renpy.pause()
        m emo-10 "Блин, блин, больше не могу..."
        ka emo-159 "Ехоу! Вот так, да, да, да..."
        scene pgn_hote_women_locker_alicekate_10_anim_01
        m emo-7 "Аааа... Аааххх... Оооххх..."
        scene pgn_hote_women_locker_alicekate_11
        ka emo-159 "Фух. Это было классно, а теперь свободен и оставь нас наедине."
        m emo-4 "Ладно, ладно. Мне тоже понравилось."
        if pgn_ach_repeat == 134:
            jump table_pgn_achievement
        if pgn_ach_repeat == 0:
            $ PGN_Addstatsex(stat_kate, 0, 0, 0, 1, 0)
    jump pgn_fitness_max_coach_end


label pgn_events_11_alicefitness_02:
    m emo-6 "Так зачем было скрывать, что ты ходишь в фитнес-зал? В этом же нет ничего, за что можно стыдиться."
    a emo-20 "Ты видел, как мы занимаемся?"
    menu:
        "Я ничего не видел":
            m emo-1 "Я был занят, так что ничего не видел и не подсматривал."
            a emo-22 "Да, да, так и поверила. Что бы ты, не упустил шанс посмотреть на нас в облегающей одежде."
            m emo-3 "Ладно. У вас классные попки."
            a emo-22 "..."
        "Мне понравилось":
            m emo-4 "Наблюдать за вами, в удовольствие. Ещё лучше, если я был вашим тренером."
            a emo-26 "Ты? Приведи себя в форму, выучись и посмотрим."
    a emo-20 "У нашего тренера немного подпорченная репутация. По слухам часто домогается до клиенток."
    m emo-6 "А почему бы не сменить или пожаловаться? Есть ещё девушка."
    a emo-20 "Ну так то он не плохой, как тренер. И в другой день и время мы не можем. И Катя всё уладила."
    m emo-6 "{i}Ясно. Поэтому он лапает только Катю, а с [pname_alice[4]] осторожен.{/i}"
    m emo-0 "Необязательно заниматься только с Катей."
    a emo-20 "Я ей пообещала, что мы будет только в месте ходить. Так что я не могу."
    m emo-6 "Хм..."
    m emo-3 "У меня есть идея."
    a emo-20 "Какая?"
    m emo-3 "А может ты с нами? Т.е. я, ты и Мама, утром будем заниматься йогой?"
    a emo-25 "А ты сам то, часто с Мамой занимаешься?"
    m emo-0 "Ну когда как, если не просплю."
    a emo-20 "Вот, для меня это слишком рано."
    m emo-0 "Да, ты всегда дрыхнешь всё утро."
    a emo-24 "Я... Если сам не проспишь, то меня разбудишь, тогда может и присоединюсь к вам."
    m emo-3 "Ок."
    $ alice_path = 21
    jump jump_dialogue



label pgn_events_11_alicefitness_03:
    $ scene_random = 0
    scene pgn_aliceroom_goodmorning_01
    m emo-3 "{i}Какая красота! Даже не хочется будить...{/i}"
    m emo-6 "{i}Или хочется?{/i}"
    m emo-4 "{i}Каким способом мне это сделать?{/i}"
    menu:
        "Голосом":
            scene pgn_aliceroom_goodmorning_04a
            if qtime == 6:
                $ label_random = 4
            else:
                $ label_random = renpy.random.randint ( 0, 4)
            while label_random > 0:
                $ label_random -= 1
                $ scene_random += 1
                if scene_random == 0:
                    m emo-0 "[pname_alice[0]] просыпайся!"
                if scene_random == 1:
                    m emo-0 "[pname_alice[0]] вставай!"
                if scene_random == 2:
                    m emo-0 "[pname_alice[0]]!"
                    a emo-28 "Ещё чуть-чуть"
                if scene_random == 3:
                    m emo-0 "[pname_alice[0]], ну вставай!"
                    a emo-28 "Отвянь..."
                if scene_random == 4:
                    m emo-0 "[pname_alice[0]]!!!"
                    $ ivent24.append("дом_мамайога_алиса_зла")
            if qtime == 6:
                a emo-27 "Сколько сейчас времени?"
                m emo-13 "6 утра"
                m emo-13 "Да рано, извини. Ну так, ты придёшь?"
                a emo-20 "Да, только ещё немного полежу."
            else:
                scene pgn_aliceroom_goodmorning_04b
                a emo-20 "Всё, я встала"
            $ ivent24.append("дом_мамайога_алиса_разбужена")
        "Шлепком по попе":
            scene pgn_aliceroom_goodmorning_03c
            m emo-6 "{i}Попробуем так.{/i}"
            if qtime == 6:
                $ label_random = 4
            else:
                $ label_random = renpy.random.randint ( 0, 4)
            while label_random > 0:
                $ label_random -= 1
                $ scene_random += 1
                scene pgn_aliceroom_goodmorning_03a
                $ renpy.pause()
                scene pgn_aliceroom_goodmorning_03b
                $ renpy.pause()
                if label_random > 0:
                    scene pgn_aliceroom_goodmorning_03c
                    $ renpy.pause(3)
                    m emo-0 "Видимо нужно ещё"
            if scene_random >= 1 and scene_random < 4:
                a emo-28 "Ммм... Что такое?"
                m emo-3 "Пора вставать."
                scene pgn_aliceroom_goodmorning_03d
                if qtime == 6:
                    a emo-27 "Сколько сейчас времени?"
                    m emo-13 "6 утра"
                    m emo-13 "Да рано, извини. Ну так, ты придёшь?"
                    a emo-20 "Да, только ещё немного полежу."
            if scene_random > 3:
                scene pgn_aliceroom_goodmorning_02c
                a emo-27 "[pname_max[0]]! Больно же."
                m emo-6 "Надо было сразу просыпаться. А то от этих шлепкой кисть болит."
                a emo-27 "Вот сейчас встану и у тебя будут большие проблемы."
                m emo-3 "Бегу, бегу. На йогу придёшь?"
                a emo-27 "Свалил"
                $ ivent24.append("дом_мамайога_алиса_зла")
            $ ivent24.append("дом_мамайога_алиса_разбужена")
        "Поцелуй паровозик":
            scene pgn_aliceroom_goodmorning_02a
            m emo-3 "{i}Так она 100%% проснётся.{/i}"
            scene pgn_aliceroom_goodmorning_02b
            m emo-4 ""
            scene pgn_aliceroom_goodmorning_02c
            a emo-27 "[pname_max[0]], какого хрена?"
            m emo-3 "Ну так ты просила, чтобы я тебя разбудил."
            if qtime == 6:
                a emo-27 "Сколько сейчас времени?"
                m emo-13 "6 утра"
                a emo-32 "А во сколько Мама занимается йогой?"
                m emo-13 "В... 7..."
                a emo-27 "Ну тогда, нафиг ты меня так рано разбудил?"
                m emo-1 "Ну..."
                a emo-27 "Вали из моей комнаты."
                m emo-1 "Ты придёшь?"
                a emo-27 "Приду, куда денусь. Беги от сюда, пока не сломала твою штуковину."
            else:
                a emo-29 "Ладно. Встаю."
            $ ivent24.append("дом_мамайога_алиса_разбужена")
            $ ivent24.append("дом_мамайога_алиса_зла")
    if qtime == 6:
        jump loc_my_room
    else:
        jump pgn_events_11_alicewithmom_yoga


label pgn_events_11_alicewithmom_yoga:
    scene pgn_11_yoga_momalice_01
    if alice_path == 21:
        a emo-21 "Доброе утро, Мама."
        mom emo-62 "Доброе. [pname_alice[0]], а что ты так рано встала, куда-то идёшь?"
    a emo-21 "Мам, ты не против если мы вместе с тобой позанимаемся, йогой?"
    scene pgn_11_yoga_momalice_02
    mom emo-62 "Конечно я не против. С радостью. Только..."
    if alice_path == 21:
        mom emo-75 "[pname_alice[0]], тебе не будет в этом жарко, может разденешься? Солнце как всегда светит, холодно не будет."
        a emo-20 "Эм... хорошо, сейчас сниму всё лишнее."
    else:
        mom emo-75 "Разденься, чтобы тебе ничего не мешало."
    scene pgn_11_yoga_momalice_03
    mom emo-62 "[pname_max[0]], хватит дурачиться."
    m emo-0 "Я стараюсь, как могу."
    scene pgn_11_yoga_momalice_04
    m emo-4 "{i}Сиськи, сиськи, сиськи...{/i}"
    scene pgn_11_yoga_momalice_05
    m emo-0 "Мам, я так не смогу. Я так посижу. Ладно?"
    mom emo-62 "Хорошо."
    scene pgn_11_yoga_momalice_06
    m emo-3 "{i}Отличный вид. Вот бы ещё мама шорты сняла.{/i}"
    scene pgn_11_yoga_momalice_07
    m emo-1 "Мама. Тебе помощь нужна?"
    mom emo-73 "[pname_max[0]], спасибо. Но сегодня я сама смогу."
    scene pgn_11_yoga_momalice_08
    m emo-2 "{i}Блин.{/i}"
    scene pgn_11_yoga_momalice_09
    $ renpy.pause()
    scene pgn_11_yoga_momalice_10
    $ renpy.pause()
    scene pgn_11_yoga_momalice_11
    $ renpy.pause()
    scene pgn_11_yoga_momalice_12
    $ renpy.pause()
    scene pgn_11_yoga_momalice_13
    $ renpy.pause()
    scene pgn_11_yoga_momalice_14
    if alice_path == 21:
        mom emo-62 "[pname_alice[0]], спасибо, что составила нам компанию. А то постоянно поздно ложишься и долго спишь и зарядкой не занимаешься, так можно и за фигурой не уследить."
        a emo-21 "Мам, да всё нормально у меня с фигурой. Я хожу почти каждый день в фитнес-зал."
        mom emo-60 "А, ну тогда хорошо."
        m emo-2 "{i}Да, да, всё, уйди, мне тут с Мамой нужно кое-что сделать.{/i}"
        if ("дом_мамайога_алиса_зла") in ivent24:
            mom emo-60 "[pname_alice[0]], может быть останешься?"
            a emo-20 "Зачем?"
    if alice_path >= 22 and ("дом_мамайога_алиса_зла") in ivent24 and pgn_ach_repeat == 0:
        a emo-20 "Мам, спасибо тебе. Я пойду, а то это солнце дурно на меня действует."
        m emo-3 "Может останешься?"
        a emo-27 "А тебе лучше в ванную бежать и принять ледяной душ, чтобы всё у тебя там отмерзло."
        mom emo-60 "[pname_alice[0]], ну что ты так с ним!?"
        scene pgn_11_yoga_momalice_15b
        m emo-2 "Мам, ты мне поможешь?"
        mom emo-68 "Извини, солнышко, но у меня сейчас нет времени. Может быть потом. Хорошо?"
        m emo-14 "Ладно"
        $ ivent24.append("momyogasex")
        $ qtime += 1
        jump loc_pool
    if alice_path == 21:
        scene pgn_11_yoga_momalice_15
        if ("дом_мамайога_алиса_зла") in ivent24:
            mom emo-60 "Поможешь мне с его проблемкой."
        else:
            a emo-33 "Мам..."
            mom emo-73 "..."
            mom emo-60 "А, что такое?"
            a emo-21 "Если у вас тут свои особые упражнения, то не нужно меня стесняться, я наоборот только за, поучаствовать с вами."
        scene pgn_11_yoga_momalice_16
        if ("дом_мамайога_алиса_зла") in ivent24:
            a emo-20 "Ааа, с его этой вечной проблемой. Хорошо, ради тебя, Мам."
        else:
            mom emo-69 "Мы... Нет... Мы только йогой, занимаемся...."
            a emo-25 "Да ладно тебе. По лицу Макса было видно, как он был расстроен, когда ты ему отказала. Вы явно здесь не только йогой занимаетесь. "
    else:
        scene pgn_11_yoga_momalice_16
    m emo-2 "Может поможете мне?"
    if alice_path == 21:
        mom emo-69 "Ох... хорошо. Да малыш, сейчас помогу. Только на секс и душ времени у меня нет."
        a emo-33 "У меня есть идея."
    scene pgn_11_yoga_momalice_17
    if alice_path == 21:
        a emo-21 "Это что-то типа ещё одного упражнения для ног."
        mom emo-62 "В этом есть что-то."
    else:
        a emo-33 "[pname_max[0]], только не двигайся, а то вдруг моя ножка переломает твой стручок."
        m emo-13 "П-п-понял, не двигаюсь."
        mom emo-62 "Дочка, не пугай ты его так. [pname_max[0]], ничего с твоим пенисом не случится, не волнуйся."
    scene animated pgn_11_yoga_momalice_18
    $ renpy.pause()
    m emo-7 "Блин... как же это классно..."
    a emo-20 "Э-э-э, после этого тебе тоже нужно будет потрудиться, не тебе же одному только получать удовольствие. И если захочется ещё, не забудь меня разбудить."
    m emo-3 "Ясно."
    m emo-7 "Сейчас, сейчас, сейчас кончу!"
    scene pgn_11_yoga_momalice_19
    $ PGN_Achadd(pgnach_135, 135)
    m emo-12 "Аргх... Аааааахххх..."
    scene pgn_11_yoga_momalice_20
    m emo-4 "Спасибо"
    mom emo-62 "Доченька, спасибо тебе за это упражнение. Мои ножки тоже потрудились."
    mom emo-62 "Всё, я в душ, быстренько ножки помою и побегу готовить вам завтрак."
    if pgn_ach_repeat == 135:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 0, 0, 0, 0, 1)
    $ PGN_Addstatsex(stat_alice, 0, 0, 0, 0, 1)
    $ ivent24.append("momyogasex")
    $ qtime += 1
    if alice_path == 21:
        $ alice_path = 22
    jump loc_pool
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
