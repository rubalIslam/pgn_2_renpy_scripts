






label pgn_events_12_maxclinic_01:
    scene pgn_maxliza_analbalcony_01
    m emo-0 "Чем бы заняться."
    scene pgn_maxliza_analbalcony_02
    m emo-1 "О! [pname_liza[0]]! А ты чего тут стоишь?"
    l emo-41 "Тебя ждала. У меня к тебе дело. Пойдём."
    m emo-0 "Какое? Куда?"
    scene pgn_maxliza_analbalcony_03
    m emo-1 "[pname_liza[0]]?!"
    scene pgn_maxliza_analbalcony_04
    m emo-6 "Зачем мы здесь?"
    l emo-49 "Ммм... Снимай шорты и займёмся сексом."
    m emo-1 "Я не против, только пойдём обратно, а то тут становится прохладно."
    l emo-43 "Хм... Я слышала, что у мальчиков пиписька от холода уменьшается. Т.е. получается он у тебя такой большой, только когда жарко?"
    m emo-11 "Ничего подобного, он у меня всегда большой."
    l emo-41 "Тогда докажи и трахни сестрёнку в попку, а то я замерзну."
    scene pgn_maxliza_analbalcony_05
    l emo-49 "Ты там скоро? Согрей сестрёнку своей горячей палочкой."
    l emo-41 "Кажется, у кого-то там проблемы. Он там сильно уменьшился?"
    m emo-1 "Ах ты! Ну держись, сестрёнка."
    scene pgn_maxliza_analbalcony_06
    $ PGN_Achadd(pgnach_148, 148)
    m emo-4 "Ну что, почувствовала, всё такой же большой?"
    l emo-49 "Да, большой. Но мне уже холодно, согрей меня своим теплом."
    scene animated pgn_maxliza_analbalcony_07
    $ renpy.pause()
    l emo-50 "Мм... Ахххх... Ммм, как хорошо... Не останавливайся..."

    if pgn_ach_repeat == 148:
        scene pgn_maxliza_analbalcony_07_15
        m emo-12 "Аргх... Ахх..."
        scene pgn_maxliza_analbalcony_05
        l emo-41 "Ой! Ты уже кончил? Как-то быстро."
        m emo-13 "Ах так! Тогда кто-то сегодня точно спать не будет."
        jump table_pgn_achievement

    scene pgn_maxliza_analbalcony_08
    mom emo-60 "Ох! Как же я устала. И за что мне всё это. Постоянно моей попке достаётся, шлёпают и шлёпают. Может [pname_kira[3]] попросить? Напишет другой сценарий."
    scene animated pgn_maxliza_analbalcony_07
    l emo-49 "Мм..."
    mom emo-60 "[pname_liza[0]]? Это ты?"
    scene pgn_maxliza_analbalcony_09
    l emo-50 "Ой! Мама..."
    m emo-8 "Э... Э... Э..."
    l emo-40 "Прячься, она не должна нас увидеть."
    scene pgn_maxliza_analbalcony_10
    mom emo-60 "Кто там с тобой? [pname_max[0]]?"
    m emo-2 "Куда?"
    l emo-46 "Не знаю. Она вот-вот поднимется."
    scene pgn_maxliza_analbalcony_11
    l emo-50 "Эээ..."
    scene pgn_maxliza_analbalcony_12
    $ renpy.pause(1.5)
    scene pgn_maxliza_analbalcony_13 with dissolve
    m emo-8 "Ай!"
    scene pgn_maxliza_analbalcony_14
    mom emo-69 "[pname_liza[0]], ты что там делаешь и... голая?"
    scene pgn_maxliza_analbalcony_15
    l emo-41 "Ой! Мам. Привет."
    mom emo-63 "Жду объяснений."
    l emo-40 "Ну, я решила выйти погулять немного."
    mom emo-64 "В таком виде? Почему это без юбки, хотя бы трусики надела и вообще, ночью прохладно, так можно и простудиться."
    l emo-46 "Прости, я не подумала."
    mom emo-60 "Ладно. На первый раз прощаю. А кто-то тут ещё был? Я слышала звуки."
    scene pgn_maxliza_analbalcony_16
    l emo-41 "Нет, Мам, я тут была одна и... И вспоминала наши уроки."
    mom emo-68 "Доченька, ну не здесь же. Это можно и в ванной, если [pname_max[0]] дома, чтобы его не \"отвлекать\"."
    scene pgn_maxliza_analbalcony_15
    mom emo-60 "Ну всё, бегом к себе. Не хватало, чтобы ты ещё заболела и занятия в школе пропускала."
    scene pgn_maxliza_analbalcony_16
    m emo-8 "{i}Вроде бы ушли. Фух... пронесло.{/i}"
    scene pgn_maxliza_analbalcony_17
    m emo-0 "{i}Пойду я, пока не заметили пропажу.{/i}"
    scene pgn_maxliza_analbalcony_18
    m emo-9 "{i}Ай! Блин! Нога. Чёрт!{/i}"
    scene pgn_maxliza_analbalcony_19
    m emo-8 "{i}Кажется я сильно ушиб ногу. Попробую медленно дойти до комнаты и лягу спать, завтра всё будет нормально.{/i}"
    $ max_path = 3.5
    jump loc_my_room_sleep


label pgn_events_12_maxclinic_02:
    scene pgn_maxhometrauma_01_vezdessushij
    m emo-8 "Как-то плохо я себя чувствую. С чего бы это."
    scene pgn_maxhometrauma_02_vezdessushij
    m emo-6 "Странно, а где [pname_liza[0]]? И сколько уже времени?"
    m emo-9 "9:24? Да я же проспал завтрак! Надо побыстрее вставать."
    scene pgn_maxhometrauma_03_vezdessushij
    m emo-8 "Ай! Блин, блин, блин, блин! Как же больно."
    m emo-8 "Не надо было прыгать. Блин! Ладно, попробую так дойти, может никто не заметит."
    scene pgn_maxhometrauma_04_vezdessushij
    l emo-41 "Мама, Мама! [pname_max[0]] пришёл!"
    mom emo-60 "[pname_max[0]], садись, мы уже заждались, а то всё спал и спал."
    scene pgn_maxhometrauma_05_vezdessushij
    mom emo-60 "Ты неважно выглядишь. Всё хорошо?"
    m emo-0 "Да."
    mom emo-60 "Уверен?"
    m emo-0 "Вполне."
    mom emo-60 "Хорошо, поверю на слово. Приятного аппетита."
    scene pgn_maxhometrauma_06_vezdessushij
    m emo-3 "Спасибо, я поел. И спасибо, было вкусно."
    scene pgn_maxhometrauma_05_vezdessushij
    mom emo-60 "[pname_max[0]], подожди."
    m emo-0 "Что такое?"
    mom emo-71 "Ты точно ничего не хочешь мне сказать?"
    m emo-2 "Эм... нет."
    mom emo-68 "Я видела, как ты всё это время держался за ногу. Если болит, то сейчас же поедем в клинику."
    menu:
        "Всё в порядке, просто чесалась":
            m emo-0 "Всё нормально, просто чешется."
            mom emo-60 "А, ну тогда в ванную сходи. Прими душ, а то ты только по утрам моешься, да и то не часто. А мы и утром и вечером перед сном."
            m emo-0 "Ладно, я пойду"
            scene pgn_maxhometrauma_07_vezdessushij
            mom emo-63 "[pname_max[0]]. Я прекрасно вижу, что у тебя какие-то проблемы, что тебе сложно встать. Может всё же сядешь и объяснишь мне."
            m emo-2 "Ну ладно."
        "Рассказать":
            pass
    scene pgn_maxhometrauma_05_vezdessushij
    m emo-0 "Наверное вчера сильно ударился. И теперь нога сильно болит."
    mom emo-68 "Как это произошло?"
    m emo-2 "Ну... как-то... дома..."
    mom emo-68 "Как-то?"
    m emo-0 "..."
    mom emo-60 "Ладно, не буду докучать вопросами. Помогу тебе дойти до комнаты, переоденешься и поедем."
    l emo-40 "А можно с вами?"
    mom emo-60 "Хорошо."
    scene animated pgn_transp_city_mom_day
    $ renpy.pause(3, hard=True)
    scene pgn_maxhometrauma_08_vezdessushij
    mom emo-60 "Приехали. Так, [pname_max[0]], сиди здесь, а я за коляской."
    m emo-0 "Я дойду сам."
    mom emo-63 "Нет, сиди и жди меня."
    a emo-21 "Мы за ним присмотрим, никуда он не денется."
    scene pgn_maxhometrauma_09_vezdessushij
    a emo-20 "Ну так, рассказывай, как ногу себе повредил."
    m emo-1 "Я просто сильно ударился."
    a emo-20 "Ага, ага. [pname_liza[0]], может ты что-то знаешь?"
    l emo-46 "Я... Ну..."
    scene pgn_maxhometrauma_10_vezdessushij
    a emo-24 "Понятно. Что-то скрываете от меня. Снова развлекались и без меня."
    scene pgn_maxhometrauma_09_vezdessushij
    a emo-25 "[pname_max[0]] уже получил своё, что заслужил. А с тобой, [pname_liza[0]], когда приедем домой..."
    l emo-46 "Может не надо?"
    scene pgn_maxhometrauma_11_vezdessushij
    mom emo-60 "[pname_max[0]], пересаживайся, только аккуратно."
    m emo-0 "Да, Мам."
    scene pgn_maxhometrauma_12_vezdessushij
    other emo-998 "Заполните бланк и ожидайте. Вас скоро примут."
    scene pgn_maxhometrauma_13_vezdessushij
    mom emo-60 "Ева, ну что с ним, не томи?"
    eva emo-128 "[pname_mom[7]], не волнуйся, ничего страшного. Перелома нет. На снимке видна небольшая трещина, так что полежит у нас недельку или чуть более и всё будет хорошо."
    m emo-13 "А можно в домашних условиях лечиться?"
    mom emo-60 "[pname_max[0]], Еве лучше знать. Раз сказала, что будешь здесь, значит тут и останешься."
    eva emo-130 "[pname_max[0]], желательно поменьше нагрузок на ногу. А так отдохнёшь и легче будет за твоим состоянием понаблюдать."
    m emo-0 "Ладно."
    mom emo-71 "Ева, нужно какие-то вещи ему привезти или что-то купить?"
    eva emo-131 "[pname_mom[6]], всё нормально. Сейчас только парочку документов заполним и всё. Одежду, в которой он будет ходить, выдадим, больничную."
    mom emo-60 "А ну тогда ладно."
    eva emo-131 "[pname_max[0]], в следующий раз будь осторожен. Не надо свою маму заставлять так переживать."
    m emo-2 "Понял. Прости Мам."
    mom emo-60 "Прощаю. В следующий сразу говори, не нужно тянуть до последнего."
    scene pgn_maxhometrauma_14_vezdessushij
    m emo-1 "А вы будете меня навещать?"
    a emo-26 "Зачем? Мы тебя здесь оставим, навсегда. \"Ты слабое звено – прощай\"."
    mom emo-62 "[pname_alice[0]]! [pname_max[0]], конечно мы будем навещать тебя."
    m emo-3 "Я постараюсь побыстрей выздороветь и вернуться."
    mom emo-63 "[pname_max[0]], вот как получше станет, и что скажет врач, тогда тебя и выпишут, а притворяться, только хуже будет."
    m emo-0 "Ладно."
    a emo-24 "Может тебе журнальчики какие-то принести? Или игрушки?"
    mom emo-64 "[pname_alice[0]]!"
    a emo-31 "Всё, всё, всё, молчу."
    mom emo-62 "Хорошо, [pname_max[0]]. Мы пойдём не скучай. Каждый день будем тебя навещать."
    a emo-21 "Пока"
    l emo-41 "Пока"
    m emo-0 "Пока."
    $ max_path, qtime = 4, 13
    $ accessiv.append("mapmax_off")
    $ ivent24.append("clinic_maxinroom_bed")
    $ ivent24.append("clinic_firstday")
    jump pgn_events_12_maxclinic_inroom


label loc_clinic_4f_recept_girlskirt:
    scene pgn_clinic_4f_recept_girlass
    m emo-3 "{i}Отличный вид.{/i}"
    jump loc_clinic_4f_recept


label pgn_events_12_maxclinic_events:

    if max_path == 4.8 and qtime >= 13:
        jump pgn_events_12_maxclinic_03

    if qtime >= 17 and clinic_time <= 0:
        if (eva_path <= 2 or eva_path == 2.3) and ("clinic_firstday") not in ivent24 and (daysn == 1 or daysn == 3 or daysn == 5 or daysn == 7) and ("maxclinic_evacum") not in ivent24:
            jump pgn_events_12_maxclinic_eva_01
        if eva_path == 2.1 and ("clinic_firstday") not in ivent24 and (daysn == 2 or daysn == 4 or daysn == 6) and ("maxclinic_evacum") not in ivent24:
            jump pgn_events_12_maxclinic_eva_02
        if eva_path == 2.2 and ("clinic_firstday") not in ivent24 and ("maxclinic_evacum") not in ivent24:
            jump pgn_events_12_maxclinic_eva_03

    if (qtime == 13 or qtime == 14) and max_path == 4.1 and ("loc_clinic_4f_hallway_02") in location:
        jump pgn_events_12_maxclinic_boobspatient_02
    if (qtime == 15 or qtime == 16) and max_path == 4.5 and ("loc_clinic_4f_hallway_02") in location:
        jump pgn_events_12_maxclinic_boobspatient_04
    if max_path == 4.6 and days_max == days:
        $ max_path = 4.7

    if ("clinic_firstday") not in ivent24:
        if eva_path < 2.2:

            if ((daysn == 1 and qtime >= 16) or (daysn == 3 and qtime >= 16) or (daysn == 5 and qtime >= 16) or (daysn == 7 and qtime >= 15)) and ("maxclinic_visit_liza") not in ivent24:
                call pgn_events_12_maxclinic_visit_liza from _call_pgn_events_12_maxclinic_visit_liza

            if qtime >= 17 and (daysn == 2 or daysn == 4 or daysn == 6) and ("maxclinic_visit_alice") not in ivent24:
                call pgn_events_12_maxclinic_visit_alice from _call_pgn_events_12_maxclinic_visit_alice
        elif ("pgn_events_12_maxclinic_inroom") in location:

            if ((daysn == 1 and qtime == 16) or (daysn == 3 and qtime == 16) or (daysn == 5 and qtime == 16) or (daysn == 7 and qtime == 15)) and ("maxclinic_visit_liza") not in ivent24:
                call pgn_events_12_maxclinic_visit_liza from _call_pgn_events_12_maxclinic_visit_liza_1

            if qtime == 17 and (daysn == 2 or daysn == 4 or daysn == 6) and ("maxclinic_visit_alice") not in ivent24:
                call pgn_events_12_maxclinic_visit_alice from _call_pgn_events_12_maxclinic_visit_alice_1

    if qtime >= 9 and ("maxclinic_break") not in ivent24 and ("clinic_firstday") not in ivent24:
        scene black with dissolve
        $ renpy.pause(1)
        scene pgn_maxinclinic_inroom_breakfast with dissolve
        m emo-3 "Хорошо поел."
        scene black with dissolve
        $ renpy.pause(1)
        $ ivent24.append("maxclinic_break")
        if qtime == 9:
            $ qtime = 10
        jump pgn_events_12_maxclinic_inroom
    if qtime >= 19 and ("maxclinic_dinner") not in ivent24:
        scene black with dissolve
        $ renpy.pause(1)
        scene pgn_maxinclinic_inroom_dinner with dissolve
        m emo-3 "Хорошо поел."
        scene black with dissolve
        $ renpy.pause(1)
        $ ivent24.append("maxclinic_dinner")
        if qtime == 19:
            $ qtime = 20
        jump pgn_events_12_maxclinic_inroom
    return

label pgn_events_12_maxclinic_sleep:
    scene pgn_maxinclinic_inroom_04_vadx
    $ renpy.pause(2)
    scene black with dissolve

    if eva_path >= 2.2:
        if max_path == 4:
            call pgn_events_12_maxclinic_boobspatient_01 from _call_pgn_events_12_maxclinic_boobspatient_01
        elif max_path >= 4.2 and ("maxclinic_pillssleep") not in ivent24 and ("maxclinic_nosleep") not in ivent24:
            call pgn_events_12_maxclinic_boobspatient_night from _call_pgn_events_12_maxclinic_boobspatient_night

    call max_sleep_reset from _call_max_sleep_reset_8
    scene black
    $ renpy.pause(2)
    scene pgn_maxinclinic_inroom_04_vadx with dissolve

    if qtime == 0:
        $ qtime = 6
    elif qtime == 1:
        $ qtime = 7
    elif qtime > 1:
        $ qtime = 8

    if ("clinic_maxinroom_bed") not in ivent24:
        $ ivent24.append("clinic_maxinroom_bed")
    jump pgn_events_12_maxclinic_inroom


label pgn_events_12_maxclinic_visit_liza:
    scene black
    scene pgn_maxinclinic_visit_liza with dissolve
    $ label_random = renpy.random.randint ( 1, 2)
    if label_random == 1:
        l emo-41 "Привет, [pname_max[0]]. Как тут тебе? Не скучно?"
        m emo-0 "Привет. Немного"
    if label_random == 2:
        l emo-41 "Как дела у моего извращенного братика?"
    menu:
        "Как дела в школе?" if daysn != 7:
            l emo-41 "Всё хорошо. Оливка передавала тебе привет."
            m emo-0 "А она заглянет?"
            l emo-40 "Не о чем таком она не говорила."
            m emo-0 "Жаль."
        "Займёмся сексом":
            m emo-13 "Давай сексом займёмся, хочу тебя."
            l emo-49 "[pname_max[0]], я тоже уже соскучилась по твоему члену, но не здесь. Потом дома, как выздоровеешь."
            m emo-2 "Пожалуйста..."
            l emo-43 "Прости, не могу. Так что выздоравливай, моя попка тебя ждёт."
        "Может минет сделаешь?":
            m emo-2 "Сделай мне минет. Пожалуйста."
            l emo-49 "Я очень хочу, но мне Мама не разрешила. Да и вдруг нас заметят. Нет."
        "Разденешься?":
            m emo-3 "[pname_liza[0]], а покажи сиськи или попку, я хотя бы подрочу."
            l emo-40 "Нет [pname_max[0]], потерпи, дома всё будет, сейчас нет."
        "Просто поговорить":
            $ renpy.pause(2)
    if (qtime == 16 and (daysn == 1 or daysn == 3 or daysn == 5)) or (qtime == 15 and daysn == 7):
        $ qtime += 1
    $ ivent24.append("maxclinic_visit_liza")
    jump pgn_events_12_maxclinic_inroom

label pgn_events_12_maxclinic_visit_alice:
    scene black
    scene pgn_maxinclinic_visit_alice_01 with dissolve
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random == 1:
        a emo-22 "[pname_max[0]], как дела? Твои яйца ещё не лопнули?"
        m emo-13 "Ха-ха-ха."
    elif label_random == 2:
        a emo-22 "Соскучился по моим дырочкам, извращенец?"
        m emo-8 "Ничего я не извращенец. Чего пришла?"
        a emo-21 "Да так, захотелось тебя проведать."
    else:
        a emo-21 "Приветик. Нога болит ещё?"
        m emo-1 "Немного."
    menu:
        "Секс":
            m emo-3 "Не могу терпеть, хочу трахаться. [pname_alice[0]], раздевайся."
            a emo-24 "Ого! Раскомандовался. Нет."
            m emo-2 "Пожалуйста. Сделаю всё, что захочешь."
            a emo-21 "Прости, не могу. Мама сказала, что пока обломишься."
        "Покажи попку":
            m emo-4 "Покажи свою попку."
            scene pgn_maxinclinic_visit_alice_03
            a emo-24 "Вот, смотри. Нравится, нравится моя попка, мои дырочки, хочешь меня?"
            m emo-3 "Да, да. Пока никого нет, подрочу хотя бы."
            scene pgn_maxinclinic_visit_alice_01
            a emo-21 "Обломишься."
            m emo-2 "Блин."
        "Покажи сиськи":
            m emo-3 "Покажешь сиськи?"
            scene pgn_maxinclinic_visit_alice_02
            a emo-21 "Смотри, только не обкончайся."
            a emo-24 "Насмотрелся?"
            scene pgn_maxinclinic_visit_alice_01
            m emo-5 "Может ещё что-нибудь покажешь?"
            a emo-21 "Хватит тебе этого на весь день."
        "Просто поговорить":
            $ renpy.pause(2)
    if qtime == 17 and (daysn == 2 or daysn == 4 or daysn == 6):
        $ qtime += 1
    $ ivent24.append("maxclinic_visit_alice")
    jump pgn_events_12_maxclinic_inroom


label pgn_events_12_maxclinic_eva_01:
    scene pgn_maxinclinic_evacum_01_vadx
    eva emo-133 "Привет, [pname_max[0]]. Как твоё самочувствие?"
    m emo-1 "Нормально, хоть сейчас готов поехать домой."
    if eva_path != 2.3 and pgn_ach_repeat == 0:
        eva emo-128 "Что чувствуешь себя нормально, это хорошо, но нужно ещё время какое-то провести в клинике."
    eva emo-132 "[pname_max[0]]. Раз ты здесь, то может я возьму образцы твоей спермы. Ты не против?"
    menu:
        "Не против":
            pass
        "Нет настроения":
            m emo-2 "Сейчас нет настроения, кажется он у меня даже не встанет."
            eva emo-128 "Какая жалость. Ну ладно, отдыхай."
            $ ivent24.append("maxclinic_evacum")
            jump pgn_events_12_maxclinic_inroom
    if eva_path != 2.3 or pgn_ach_repeat == 149:
        m emo-1 "Мне встать или пойдём в кабинет?"
        scene pgn_maxinclinic_evacum_02_vadx
        $ PGN_Achadd(pgnach_149, 149)
        eva emo-133 "Не нужно, можно и здесь. Делать тебе ничего не придётся."
        eva emo-132 "Я сделаю всё сама."
    scene pgn_maxinclinic_evacum_03_vadx
    m emo-3 "Может тоже разденешься?"
    eva emo-128 "Хорошо. Но никакого секса."
    scene animated pgn_maxinclinic_evacum_04
    $ renpy.pause()
    m emo-10 "Я почти..."
    scene pgn_maxinclinic_evacum_05_vadx
    eva emo-133 "Спасибо. Через 3 дня приду за следующей порцией. Если не против конечно."
    m emo-0 "Мне всё равно некуда девать, пока я здесь."
    eva emo-128 "Отдыхай и поправляйся."

    if pgn_ach_repeat == 149:
        jump table_pgn_achievement

    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[1])+" $"+"100")
    $ ivent24.append("maxclinic_evacum")
    $ PGN_Addstatsex(stat_eva, 0, 0, 0, 0, 1)
    if eva_path != 2.3:
        $ eva_path = 2.1
    $ eva_cum, clinic_time, currency = eva_cum+1, 3, currency+100
    if qtime == 17:
        $ qtime += 1
    jump pgn_events_12_maxclinic_inroom


label pgn_events_12_maxclinic_eva_02:
    scene pgn_maxinclinic_visit_alice_01
    a emo-20 "Ну как ты тут?"
    m emo-0 "Очень сильно соскучился. В особенности по влажным..."
    scene pgn_maxinclinic_evacum_06_vadx
    eva emo-131 "Ой! Я не вовремя?"
    a emo-20 "Я уже ухожу. Оставлю вам, своего бр... парня."
    eva emo-132 "Может останешься и поможешь мне?"
    a emo-22 "С чем? ... А поняла, конечно, а то соскучился по моим ласкам."
    eva emo-130 "Я дверь закрою, чтобы никто нас не потревожил. И будет лучше, если снимем с себя всё лишнее."
    a emo-21 "Согласна."
    m emo-4 "У меня и так встанет, на таких красавиц."
    a emo-21 "[pname_max[0]]! Врачу виднее, так что помолчи и получай удовольствие."
    scene pgn_maxinclinic_evacum_07_vadx
    $ PGN_Achadd(pgnach_150, 150)
    a emo-33 "Есть, идеи, как мы это сделаем? Места на кровати не много."
    scene pgn_maxinclinic_evacum_08_vadx
    eva emo-129 "Хм... [pname_max[0]], может пересядешь на диван?"
    m emo-0 "Ладно."
    scene pgn_maxinclinic_evacum_09_vadx
    a emo-33 "Вот так лучше. Ну так, мы ему руками или есть предложения?"
    eva emo-130 "В прошлый раз я ему делала руками, так что давай поможем ртом. Только, [pname_max[0]], предупреди, мне нужна твоя сперма."
    a emo-22 "А мне деньги."
    m emo-0 "Понял. Да, да, хорошо."
    scene animated pgn_maxinclinic_evacum_11
    $ renpy.pause()
    a emo-24 "Ого! Ева, вы так легко заглатываете."
    eva emo-132 "Практика, много практики."
    scene pgn_maxinclinic_evacum_09_vadx
    eva emo-132 "Твоя очередь."
    scene animated pgn_maxinclinic_evacum_10
    $ renpy.pause()
    eva emo-130 "[pname_alice[0]], у тебя тоже неплохо выходит."
    m emo-10 "Сейчас кончу."
    scene pgn_maxinclinic_evacum_12_vadx
    eva emo-131 "Как много."
    a emo-24 "У него столько спермы, что можно наполнить целый бассейн."
    scene pgn_maxinclinic_evacum_13_vadx
    eva emo-128 "[pname_alice[0]], держи."
    a emo-20 "Спасибо. Больше, чем обычно."
    eva emo-128 "Так и [pname_max[0]] хорошо постарался."
    m emo-4 "[pname_alice[0]], может останешься ещё не надолго?"
    eva emo-129 "[pname_max[0]], тебе нужно отдыхать, а то так не вылечишься и будешь долго в палате лежать."
    a emo-33 "[pname_max[0]], ты слышал врача, лечись, отдыхай и копи по больше своей спермы. Мне нужно больше денег."
    m emo-6 "{i}Куда больше? И на что она так быстро их тратит?{/i}"

    if pgn_ach_repeat == 150:
        jump table_pgn_achievement

    $ ivent24.append("maxclinic_evacum")
    $ ivent24.append("maxclinic_visit_alice")
    $ PGN_Addstatsex(stat_alice, 0, 0, 1, 0, 0)
    $ PGN_Addstatsex(stat_eva, 0, 0, 1, 0, 0)
    $ eva_path, eva_cum, clinic_time = 2.2, eva_cum+1, 3
    if qtime == 17:
        $ qtime += 1
    jump pgn_events_12_maxclinic_inroom


label pgn_events_12_maxclinic_eva_03:
    if ("clinic_maxinroom_bed") in ivent24 or pgn_ach_repeat == 151:
        mom emo-60 "[pname_max[0]]!"
        scene pgn_maxinclinic_evacum_14_vadx
        m emo-3 "Мама, я рад тебя видеть."
        mom emo-62 "Я тоже по тебе сильно соскучилась."
        scene pgn_maxinclinic_evacum_15_vadx
        m emo-0 "Мама, как..."
        mom emo-60 "[pname_max[0]], раздевайся. У нас мало времени."
    else:
        scene black with dissolve
        $ renpy.pause(1)
        scene pgn_maxinclinic_evacum_15_vadx with dissolve
        m emo-3 "Я рад тебя видеть и очень соскучился."
        mom emo-62 "Я тоже, я тоже. Раздевайся по скорей, мамочка очень сильно соскучилась."
    scene pgn_maxinclinic_evacum_16
    mom emo-69 "Ты прости меня, что не навещала. Я боялась, что если приду, то не смогу себя сдержать."
    mom emo-69 "Заниматься сексом здесь, было бы слишком рискованно."
    m emo-3 "Но всё же ты здесь."
    mom emo-68 "Да, [pname_max[0]], я всё же пришла. Ещё столько же, не выдержала."
    scene pgn_maxinclinic_evacum_17_vadx
    mom emo-62 "Так что, [pname_max[0]], у нас мало времени. Постарайся как можно скорее кончить мне в рот. "
    m emo-3 "Хорошо, Мам, я постараюсь."
    scene pgn_maxinclinic_evacum_18
    $ PGN_Achadd(pgnach_151, 151)
    mom emo-69 "Давай малыш, кончи мамочке в ротик. Мамочка очень соскучилась по члену во рту и твоей густой сперме."
    mom emo-75 "Ммм... Ммм..."
    scene pgn_maxinclinic_evacum_19_vadx
    mom emo-68 "Помогу ручками... Сынок, тебе уже пора кончать. Давай, будь умницей, кончи. Кончи ради мамочки."
    m emo-10 "Мама, я уже скоро."
    scene pgn_maxinclinic_evacum_18
    m emo-10 "Ох... Мама, ускорься, я уже почти..."
    scene pgn_maxinclinic_evacum_20_vadx
    $ renpy.pause(2)
    scene pgn_maxinclinic_evacum_21_vadx
    $ renpy.pause(2)
    scene pgn_maxinclinic_evacum_22_vadx
    m emo-13 "Ох.. Чёрт! ... Ммм... Обалдеть, как же приятно... Продолжай..."
    eva emo-130 "{i}Хм... [pname_alice[0]] уже здесь.{/i}"
    m emo-10 "Ещё чуть и я кончу."
    eva emo-133 "{i}[pname_alice[0]], ты же знаешь, что его сперма нужна для других целей.{/i}"
    m emo-7 "Мама, я вот вот-вот уже..."
    eva emo-131 "{i}Что он сказал, \"Мама\"? [pname_mom[7]], не ужели ты в таких отношениях с сыном?{/i}"
    mom emo-68 "[pname_max[0]], ну же кончай, кончай... Дома ты быстрее управляешься."
    eva emo-131 "{i}Так это у них не впервые?! Интересно.{/i}"
    m emo-10 "Мама, я... "
    m emo-12 "Аргххх... Аа... Ааах... Аааа..."
    scene pgn_maxinclinic_evacum_20_vadx
    eva emo-128 "{i}Мне пора уходить, будет неудобно, если меня заметят.{/i}"
    scene pgn_maxinclinic_evacum_23_vadx
    m emo-3 "Проглоти всё."
    scene pgn_maxinclinic_evacum_24_vadx
    mom emo-75 "Сыночек, спасибо. Утолил мамин голод. Мне стало полегче."
    scene pgn_maxinclinic_evacum_25_vadx
    mom emo-69 "Как твоя нога?"
    m emo-0 "Уже не болит. Думаю, меня скоро выпишут."
    mom emo-62 "Это хорошо, а то дома без тебя мне очень одиноко, нам всем тебя не хватает."
    mom emo-73 "Всё же [pname_liza[0]] была права."
    m emo-6 "Насчёт чего?"
    mom emo-62 "Что я, как женщина, нуждаюсь в тебе и...ты понял о чём я. Мне стоит помягче относится к тому, что [pname_liza[0]] тоже нуждается в мужском внимании."
    m emo-4 "У нас будет секс?"
    mom emo-64 "Так, нет, никого секса, я запрещаю. Достаточно ваших оральных тренировок."
    m emo-2 "Да, извини."
    mom emo-62 "Ну всё, я пойду. Когда тебя выпишут, заеду за тобой. Пока."
    m emo-3 "Пока Мам."

    if pgn_ach_repeat == 151:
        jump table_pgn_achievement

    $ eva_path, clinic_time = 2.3, 3
    $ ivent24.append("maxclinic_visit_liza")
    $ ivent24.append("maxclinic_visit_alice")
    $ PGN_Addstatsex(stat_mom, 0, 0, 1, 0, 1)
    if qtime == 17:
        $ qtime += 1
    jump pgn_events_12_maxclinic_inroom


label pgn_events_12_maxclinic_evacabinet:
    scene pgn_maxinclinic_inroom_evacabinet_vadx
    eva emo-128 "Чего тебе, [pname_max[0]]?"
    menu:
        "Просто":
            m emo-0 "Да так, просто."
            eva emo-128 "[pname_max[0]], я не против твоей компании, но у меня работа и дела."
            m emo-0 "Понял, не буду мешать"
        "Сдать сперму":
            m emo-0 "Пришёл сдать сперму."
            if clinic_time > 0:
                if max_path == 4:
                    eva emo-133 "Уже прошло 3 дня?"
                    m emo-13 "Н-н-нет, вроде."
                    eva emo-128 "[pname_max[0]], я помню. Когда придёт время, я сама приду."
                else:
                    eva emo-133 "[pname_max[0]], ещё время не пришло."
            else:
                eva emo-128 "Приходить не обязательно, у тебя же нога ещё до конца не зажила. Я сама приду к тебе в палату."
            m emo-0 "Ладно."
        "Таблетки" if max_path >= 4.3 and pills_sleep.numbsuse <= 1:
            if max_path == 4.3:
                m emo-0 "Можно какие-нибудь таблетки для сна?"
                eva emo-128 "Что-то болит или просто плохо спится?"
                m emo-5 "Не высыпаюсь."
                eva emo-133 "Держи. Принимай по одной капсуле."
                $ max_path = 4.4
            elif max_path > 4.3:
                m emo-1 "Можно ещё таблетки, а то они у меня закончились."
                eva emo-128 "Держи."
            m emo-3 "Спасибо."
            $ pills_sleep.numbsuse, pills_sleep.have = 2, True
    jump loc_clinic_4f_recept


label pgn_events_12_maxclinic_boobspatient_01:
    other emo-998 "Аххх... ахх... ах..."
    m emo-7 "{i}Кому-то явно сейчас очень хорошо.{/i}"
    other emo-998 "Аххх... ахх... ах..."
    m emo-10 "{i}И не дают выспаться.{/i}"
    scene pgn_maxinclinic_boobsgirl_01_vezdessushij
    m emo-6 "{i}И от куда именно эти звуки?{/i}"
    other emo-998 "Аххх... Да... Да..."
    scene pgn_maxinclinic_boobsgirl_08_vezdessushij
    m emo-13 "{i}Чёрт! Она так громко стонет, кто-то ещё кроме меня должен был услышать.{/i}"
    m emo-0 "{i}Кто-то сексом занимается, а мне сёстры отказывает. Типа нельзя, бла,бла...{/i}"
    scene pgn_maxinclinic_boobsgirl_09_vezdessushij
    other emo-998 "Аххх... ахх... ах..."
    other emo-999 "Агрх... Ааа..."
    m emo-0 "{i}Мне пора уходить.{/i}"
    $ max_path = 4.1
    return


label pgn_events_12_maxclinic_boobspatient_02:
    scene pgn_clinic_4f_hallway_02_vezdessushij
    m emo-6 "{i}Кто-то есть в соседней палате.{/i}"
    scene pgn_maxinclinic_boobsgirl_10_vezdessushij
    other emo-998 "Познакомьтесь. Это наш ведущий хирург и он будет вами заниматься."
    sv emo-421 "Здравствуйте. Рада с вами познакомиться."
    m emo-6 "{i}Мне он напоминает парня с той ночи, который её трахал.{/i}"
    other emo-999 "Значит вы хотите увеличить свою грудь?"
    m emo-1 "{i}Что не так с её сиськами? Лишь бы им всё увеличить.{/i}"
    sv emo-420 "Да, я хочу сделать их больше. Вот настолько."
    other emo-999 "Хм... Ясно. Нужно будет провести несколько обследований."
    sv emo-421 "Всё что нужно, я готова на всё."
    m emo-3 "{i}Видимо он на это и рассчитывает.{/i}"
    other emo-998 "Вы не волнуйтесь, операция пройдёт без каких-либо неприятностей. Швы будут почти не видны. Я вам гарантирую, результат вам понравится. "
    other emo-998 "Я вас оставлю. А вы поговорите."
    m emo-2 "{i}Блин, блин, блин!{/i}"
    $ max_path = 4.2
    scene pgn_maxinclinic_boobsgirl_11_vezdessushij
    $ renpy.pause(3)
    scene pgn_maxinclinic_boobsgirl_10_vezdessushij
    other emo-999 "Тебе хочется таких размеров?"
    sv emo-421 "Да доктор."
    other emo-999 "Ты знаешь, что делать."
    sv emo-424 "Конечно, всё что пожелаете, доктор..."
    scene pgn_maxinclinic_boobsgirl_12_vezdessushij
    m emo-1 "{i}Вообще ничего не видно.{/i}"
    other emo-999 "Соси сучка, соси..."
    other emo-999 "Какая-то ты вялая, выпишу витамины и пропьёшь их."
    m emo-6 "{i}Витамины? Хм...{/i}"
    other emo-999 "Бери глубже! Да, вот так, молодец. Соси..."
    m emo-0 "{i}Нечего мне тут делать, всё равно ничего не видно и ничего мне не перепадёт.{/i}"
    $ max_path, qtime = 4.2, qtime+1
    jump loc_clinic_4f_hallway_02


label pgn_events_12_maxclinic_boobspatient_night:
    other emo-998 "Аххх... ахх... ах..."
    if max_path == 4.6 and days_max > days:
        m emo-6 "{i}Опять?! А не рано ли ей сейчас сексом заниматься.{/i}"
        m emo-0 "{i}Блин. Тоже хочу туда, посмотреть на творение этого \"доктора\". Но дверь к ней закрыта.{/i}"
    if max_path == 4.2:
        $ max_path = 4.3
        m emo-13 "{i}Да я блин не усну. Может у Евы попросить таблетку какую-нибудь.{/i}"
    else:
        if pills_sleep.numbsuse == 0:
            m emo-13 "{i}Надо было у Евы взять таблетки.{/i}"
        else:
            m emo-13 "{i}Надо было таблетку выпить.{/i}"
    other emo-998 "Аххх... ахх... ах..."
    return


label pgn_events_12_maxclinic_inroom_choice:
    menu:
        "Выпить таблетку" if pills_sleep.numbsuse > 0:
            $ ivent24.append("maxclinic_pillssleep")
            $ pills_sleep.numbsuse -= 1
            $ serialpgngame("pgn_events_12_maxclinic_sleep")
        "Ждать поздней ночи":
            $ ivent24.append("maxclinic_nosleep")
            m emo-0 "Попробую не уснуть."
            scene pgn_maxinclinic_inroom_04_vadx
            show screen nav_time
            while qtime < 4:
                $ renpy.pause(1, hard=True)
                $ qtime += 1
            $ label_random = renpy.random.randint ( 1, 4)
            if (label_random == 4 and "walkthrough_light" not in accessiv) or (max_path == 4.6 and days_max > days):
                scene black with dissolve
                hide screen nav_time
                $ serialpgngame("pgn_events_12_maxclinic_sleep")
            else:
                if max_path < 4.6:
                    jump pgn_events_12_maxclinic_boobspatient_03
                else:
                    jump pgn_events_12_maxclinic_boobspatient_05
        "назад":
            pass
    jump pgn_events_12_maxclinic_inroom

label pgn_events_12_maxclinic_patientroom_n6_choice:
    menu:
        "Столик":
            m emo-6 "{i}Хм... Какие-то 2 капсулы. Что за таблетки она пьёт?{/i}"
            m emo-0 "{i}Только мне как-то по фигу.{/i}"
        "Подложить таблетки" if max_path >= 4.4 and pills_sleep.numbsuse > 0 and ("maxclinic_boobspatient_pillssleep_1") not in ivent24 and ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
            m emo-3 "{i}Поменяю её таблетки на свои.{/i}"
            if pills_sleep.numbsuse > 1:
                menu:
                    "Заменить 1 капсулу":
                        $ pills_sleep.numbsuse -= 1
                        $ ivent24.append("maxclinic_boobspatient_pillssleep_1")
                    "Заменить 2 капсулы":
                        $ pills_sleep.numbsuse = 0
                        $ ivent24.append("maxclinic_boobspatient_pillssleep_2")
            else:
                $ pills_sleep.numbsuse = 0
                $ ivent24.append("maxclinic_boobspatient_pillssleep_1")
    jump loc_clinic_patientroom_n6


label pgn_events_12_maxclinic_boobspatient_03:
    m emo-13 "{i}Блин, как же спать хочется. Пойду проведаю соседку.{/i}"
    hide screen nav_time
    scene pgn_maxinclinic_boobsgirl_07_vezdessushij
    m emo-3 "{i}Отлично. Она спит. Надеюсь крепко.{/i}"
    menu:
        "Включить свет":
            label pgn_events_12_maxclinic_boobspatient_03a:
                $ ivent24.append("maxclinic_boobspatient_light_on")
                if ("maxclinic_boobspatient_pillssleep_1") not in ivent24 and ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                    call pgn_events_12_maxclinic_boobspatient_03_fail1 from _call_pgn_events_12_maxclinic_boobspatient_03_fail1
                scene pgn_maxinclinic_boobsgirl_13_vezdessushij
                m emo-3 "{i}Красота! Ну как можно спать без лифчика, вдруг кто-то зайдёт.{/i}"
                menu:
                    "Раскрыть грудь":
                        scene pgn_maxinclinic_boobsgirl_14_vezdessushij
                        $ label_random = renpy.random.randint ( 1, 2)
                        if max_path == 1:
                            m emo-0 "{i}Осторожно и медленно. Мне не нужно, чтобы она проснулась.{/i}"
                        else:
                            m emo-4 "{i}Да появятся, СИСЬКИ!{/i}"
                        scene pgn_maxinclinic_boobsgirl_15_vezdessushij
                        m emo-6 "{i}Нормальные у неё сиськи. Зачем их увеличивать.{/i}"
                        scene pgn_maxinclinic_boobsgirl_15b_vezdessushij
                        $ countdown = 0
                        menu menu_ev12_boobspatient_1:
                            "Потрогать сиськи":
                                if ("maxclinic_boobspatient_pillssleep_1") not in ivent24 and ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                                    if max_path == 4.4:
                                        $ max_path = 4.45
                                    jump pgn_events_12_maxclinic_boobspatient_03_fail2
                                if countdown > 2 and ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                                    if max_path == 4.4 or max_path == 4.45:
                                        $ max_path = 4.49
                                    jump pgn_events_12_maxclinic_boobspatient_03_fail2
                                if countdown > 6 and ("maxclinic_boobspatient_pillssleep_2") in ivent24:
                                    jump pgn_events_12_maxclinic_boobspatient_03_fail2
                                $ countdown += 1
                                scene pgn_maxinclinic_boobsgirl_16_vezdessushij
                                m emo-4 "{i}Ммм... Классные сиськи. Как же подрочить захотелось.{/i}"
                                if ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                                    m emo-6 "{i}Но делать этого не буду, слишком рисковано.{/i}"
                                scene pgn_maxinclinic_boobsgirl_15b_vezdessushij
                                jump menu_ev12_boobspatient_1
                            "Стянуть трусики":
                                scene pgn_maxinclinic_boobsgirl_19_vezdessushij
                                m emo-5 "{i}Медленно и осторожно...{/i}"
                                scene pgn_maxinclinic_boobsgirl_20_vezdessushij
                                m emo-5 "{i}Ну же, [pname_max[0]], не накосячь.{/i}"
                                if ("maxclinic_boobspatient_pillssleep_1") not in ivent24 and ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                                    if max_path == 4.4:
                                        $ max_path = 4.45
                                    jump pgn_events_12_maxclinic_boobspatient_03_fail2
                                scene pgn_maxinclinic_boobsgirl_21_vezdessushij
                                m emo-4 "{i}Отлично! Получилось!{/i}"
                                menu:
                                    "Подрочить её рукой":
                                        $ label_random = renpy.random.randint ( 5, 9)
                                        if label_random == 9:
                                            "Тук-тук"
                                            m emo-9 "{i}Блин! Не вовремя.{/i}"
                                            scene pgn_maxinclinic_boobsgirl_18_vezdessushij
                                            other emo-999 "Готовь ротик, сейчас тебе придётся им поработать"
                                            other emo-999 "Эй! Проснись, сучка. Эй!"
                                            other emo-999 "Света! Звезда минета, просыпайся!"
                                            if ("maxclinic_boobspatient_pillssleep_1") in ivent24:
                                                sv emo-421 "Ой! Доктор! Здравствуйте, я что-то уснула."
                                                other emo-999 "Открывай ротик, летит большой самолётик."
                                                m emo-2 "{i}Блин! Я тут на долго.{/i}"
                                                if max_path <= 4.45:
                                                    $ max_path = 4.49
                                                $ serialpgngame("pgn_events_12_maxclinic_sleep")
                                            else:
                                                other emo-999 "Крепко спит. Фиг с ней, пойду какую-нибудь медсеструху трахну."
                                                m emo-3 "{i}Фух! Пронесло.{/i}"
                                        scene pgn_maxinclinic_boobsgirl_22_vezdessushij
                                        m emo-3 "{i}Да, вот так, крепче возьмись за мой ствол.{/i}"
                                        if ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                                            if max_path <= 4.45:
                                                $ max_path = 4.49
                                            $ ivent24.append("ev12_boobspatient_doctorfail")
                                            jump pgn_events_12_maxclinic_boobspatient_03_fail2
                                        scene animated pgn_maxinclinic_boobsgirl_22_vezdessushij
                                        m emo-4 "Класс!"
                                        m emo-10 "О... Даааа! Очень хорошо, не знаю почему, но мне нравится."
                                        m emo-7 "{i}Сейчас кончу...{/i}"
                                        scene pgn_maxinclinic_boobsgirl_24_vezdessushij
                                        m emo-3 "Суперская ночь. Хотя бы так кончил. Пойду спать."
                                        scene black with dissolve
                                        $ renpy.pause(1)
                                        scene pgn_maxinclinic_boobsgirl_25_vezdessushij
                                        sv emo-422 "Ох! Ко мне приходил доктор?!"
                                        sv emo-424 "Надеюсь в следующий раз он меня разбудит."
                                        if max_path < 4.5:
                                            $ max_path = 4.5
                                        $ serialpgngame("pgn_events_12_maxclinic_sleep")
                                    "уйти":
                                        $ serialpgngame("pgn_events_12_maxclinic_sleep")
                    "уйти":
                        $ serialpgngame("pgn_events_12_maxclinic_sleep")
        "Не включать":
            label pgn_events_12_maxclinic_boobspatient_03b:
                $ ivent24.append("maxclinic_boobspatient_light_off")
                if ("maxclinic_boobspatient_pillssleep_1") not in ivent24 and ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                    call pgn_events_12_maxclinic_boobspatient_03_fail1 from _call_pgn_events_12_maxclinic_boobspatient_03_fail1_1
                scene pgn_maxinclinic_boobsgirl_n_13_vezdessushij
                m emo-3 "{i}Красота! Ну как можно спать без лифчика, вдруг кто-то зайдёт.{/i}"
                menu:
                    "Раскрыть грудь":
                        scene pgn_maxinclinic_boobsgirl_n_14_vezdessushij
                        $ label_random = renpy.random.randint ( 1, 2)
                        if max_path == 1:
                            m emo-0 "{i}Осторожно и медленно. Мне не нужно, чтобы она проснулась.{/i}"
                        else:
                            m emo-4 "{i}Да появятся, СИСЬКИ!{/i}"
                        scene pgn_maxinclinic_boobsgirl_n_15_vezdessushij
                        m emo-6 "{i}Нормальные у неё сиськи. Зачем их увеличивать.{/i}"
                        scene pgn_maxinclinic_boobsgirl_n_15b_vezdessushij
                        $ countdown = 0
                        menu menu_ev12_boobspatient_2:
                            "Потрогать сиськи":
                                if countdown > 5 and ("maxclinic_boobspatient_pillssleep_1") in ivent24:
                                    if max_path <= 4.45:
                                        $ max_path = 4.49
                                    jump pgn_events_12_maxclinic_boobspatient_03_fail2
                                if countdown > 8 and ("maxclinic_boobspatient_pillssleep_2") in ivent24:
                                    jump pgn_events_12_maxclinic_boobspatient_03_fail2
                                $ countdown += 1
                                scene pgn_maxinclinic_boobsgirl_n_16_vezdessushij
                                m emo-4 "{i}Ммм... Классные сиськи. Как же подрочить захотелось.{/i}"
                                if ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                                    m emo-6 "{i}Но делать этого не буду, слишком рисковано.{/i}"
                                scene pgn_maxinclinic_boobsgirl_n_15b_vezdessushij
                                jump menu_ev12_boobspatient_2
                            "Стянуть трусики":
                                scene pgn_maxinclinic_boobsgirl_n_19_vezdessushij
                                m emo-5 "{i}Медленно и осторожно...{/i}"
                                scene pgn_maxinclinic_boobsgirl_n_20_vezdessushij
                                m emo-5 "{i}Ну же, [pname_max[0]], не накосячь.{/i}"
                                if ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
                                    if max_path == 4.4:
                                        $ max_path = 4.45
                                    elif max_path == 4.45:
                                        $ max_path = 4.49
                                    jump pgn_events_12_maxclinic_boobspatient_03_fail2
                                scene pgn_maxinclinic_boobsgirl_n_21_vezdessushij
                                m emo-4 "{i}Отлично! Получилось!{/i}"
                                m emo-0 "{i}Не буду дальше рисковать, пойду лучше посплю.{/i}"
                                $ serialpgngame("pgn_events_12_maxclinic_sleep")
                    "уйти":
                        $ serialpgngame("pgn_events_12_maxclinic_sleep")

label pgn_events_12_maxclinic_boobspatient_03_fail1:
    if max_path == 4.4:
        $ max_path = 4.45
    if ("maxclinic_boobspatient_light_on") in ivent24:
        $ label_random = renpy.random.randint ( 1, 3)
    if ("maxclinic_boobspatient_light_off") in ivent24:
        $ label_random = renpy.random.randint ( 1, 5)
    if label_random == 1:
        label pgn_events_12_maxclinic_boobspatient_03_fail2:
            sv emo-423 "Это вы доктор, я вас ждала."
            m emo-9 "{i}Блин{/i}"
            if ("maxclinic_boobspatient_light_on") in ivent24:
                scene pgn_maxinclinic_boobsgirl_17_vezdessushij
                sv emo-420 "Я забыла выключить свет? Не буду вставать, всё равно он скоро придёт."
            if ("maxclinic_boobspatient_light_off") in ivent24:
                scene pgn_maxinclinic_boobsgirl_n_17_vezdessushij
                sv emo-420 "Кто здесь? Доктор, это вы?"
            m emo-1 "{i}Ещё чуть-чуть. Теперь жди, когда она там уснёт.{/i}"
            $ label_random = renpy.random.randint ( 4, 6)
            if label_random == 6 and ("ev12_boobspatient_doctorfail") not in ivent24:
                "Тук-тук"
                m emo-9 "{i}Чёрт!!!{/i}"
                if ("maxclinic_boobspatient_light_on") in ivent24:
                    scene pgn_maxinclinic_boobsgirl_18_vezdessushij
                if ("maxclinic_boobspatient_light_off") in ivent24:
                    scene pgn_maxinclinic_boobsgirl_n_18_vezdessushij
                other emo-999 "Как себя чувствует моя пациентка?"
                sv emo-421 "Плохо. Но я надеюсь, доктор сейчас меня вылечит."
                sv emo-422 "Ахх... Мммм... Аааххх..."
                scene pgn_maxinclinic_boobsgirl_09_vezdessushij
                m emo-13 "{i}Я влип.{/i}"
            $ serialpgngame("pgn_events_12_maxclinic_sleep")
    return


label pgn_events_12_maxclinic_boobspatient_04:
    $ max_path, days_max = 4.6, days+4
    scene pgn_clinic_4f_hallway_02_vezdessushij
    m emo-6 "{i}К соседке снова кто-то пришёл{/i}"
    scene pgn_maxinclinic_boobsgirl_10_vezdessushij
    other emo-998 "У меня хорошие новости, все ваши анализы в порядке и сегодня вам сделают операцию."
    sv emo-421 "Спасибо."
    other emo-999 "Сейчас отдыхайте. Скоро за вами приду и мы вместе отправимся в операционную."
    sv emo-421 "Жду не дождусь."
    m emo-4 "{i}Я тоже.{/i}"
    jump loc_clinic_4f_hallway_02


label pgn_events_12_maxclinic_boobspatient_05:
    m emo-3 "{i}Немного сонный, но всё ещё готов и хочу посмотреть на сиси соседки.{/i}"
    hide screen nav_time
    scene pgn_maxinclinic_boobsgirl_26_vezdessushij
    m emo-9 "{i}Вау! Какие сисяндры! И ещё она спит совсем голой.{/i}"
    m emo-3 "{i}Мне же проще, не нужно раздевать.{/i}"
    if ("maxclinic_boobspatient_pillssleep_1") not in ivent24 and ("maxclinic_boobspatient_pillssleep_2") not in ivent24:
        m emo-6 "{i}Только вот не знаю, рискнуть или завтра подложить ей снотворное.{/i}"
    if ("maxclinic_boobspatient_pillssleep_1") in ivent24 or ("maxclinic_boobspatient_pillssleep_2") in ivent24:
        m emo-6 "{i}Надеюсь она выпила все таблетки. Ну была не была.{/i}"
    if pgn_ach_repeat == 0:
        menu:
            "Продолжить":
                pass
            "уйти":
                $ serialpgngame("pgn_events_12_maxclinic_sleep")
    scene pgn_maxinclinic_boobsgirl_27_vezdessushij
    m emo-3 "{i}Горячий ротик.{/i}"
    scene pgn_maxinclinic_boobsgirl_28_vezdessushij
    m emo-4 "{i}И влажный. О! Как ухватилась. Очень хочется кончить туда кончить.{/i}"
    m emo-3 "{i}Пока что не проснулась, тогда продолжу.{/i}"
    scene animated pgn_maxinclinic_boobsgirl_29
    $ renpy.pause()
    $ PGN_Achadd(pgnach_152, 152)
    m emo-13 "{i}Сейчас кончу... На лицо, слишком заметно, на сиськи тоже, остаётся только один вариант.{/i}"
    scene pgn_maxinclinic_boobsgirl_30_vezdessushij
    m emo-10 "{i}Аргх... Аааахх... Фух!{/i}"
    m emo-13 "{i}Так стоп. Она так не захлебнётся?{/i}"
    m emo-15 "..."
    m emo-9 "{i}Она глотает?{/i}"
    scene pgn_maxinclinic_boobsgirl_31_vezdessushij
    sv emo-424 "Ну приветик, озабоченный мальчишка."
    m emo-9 "Ааа!!! Я это... ну... блин... Я..."
    sv emo-421 "Не смог удержаться при виде этих больших малышек?"
    m emo-9 "Эм... ну..."
    sv emo-424 "Значит они действуют как нужно. Отлично."
    m emo-13 "{i}Фух! Значит раньше она не притворялась и не помнит ничего.{/i}"
    sv emo-420 "И долго будешь на мне сидеть? Слезай и уматывай отсюда, пока я шум не подняла."
    m emo-0 "Понял. Извините... Я... Пойду."

    if pgn_ach_repeat == 152:
        jump table_pgn_achievement

    $ max_path = 4.8
    $ serialpgngame("pgn_events_12_maxclinic_sleep")


label pgn_events_12_maxclinic_03:
    scene pgn_maxhometrauma_13_vezdessushij
    eva emo-128 "[pname_max[0]], как твоя нога?"
    m emo-3 "Не болит."
    eva emo-128 "Это хорошо. Только есть одно но."
    mom emo-60 "Что-то случилось, у него какая какая-то болезнь, что снова придётся ему в клинике лежать?"
    eva emo-128 "Нет, [pname_mom[6]], ни чего такого серьезно. И [pname_max[0]] может ехать домой."
    eva emo-128 "Ему только придётся недельку не заниматься сексом и после снова буду вас ждать у себя."
    m emo-9 "{i}Что?! Неделю?! Это слишком для меня.{/i}"
    mom emo-73 "Это для анализов... спермы?"
    eva emo-128 "Пока он здесь лежал, я брала, материал для анализов и... Будет лучше, если он на недельку воздержится."
    mom emo-73 "Поняла. Я постараюсь проследить за ним."
    eva emo-128 "[pname_max[0]], оставь меня с Мамой на минутку. Хорошо?"
    mom emo-60 "[pname_max[0]], собери вещи свои и буду тебя ждать в машине."
    scene pgn_maxinclinic_end_vadx
    $ renpy.pause(2)
    $ max_path, eva_path, days_eva = 5, 3, days+7
    scene animated pgn_transp_city_mom_day
    $ renpy.pause(3, hard=True)
    if ("mapmax_off") in accessiv:
        $ accessiv.remove("mapmax_off")
    jump loc_pool


label pgn_events_12_maxclinic_04a:
    l emo-40 "А сегодня мы поедем куда-нибудь?"
    mom emo-60 "Нет девочки. Мне нужно после завтрака с [pname_max[4]] съездить в клинику."
    mom emo-60 "[pname_kira[0]], может быть ты отвезёшь девочек?"
    k emo-100 "Хорошо."
    l emo-41 "А можно с вами?"
    mom emo-60 "Нет [pname_liza[0]], мы туда едем не развлекаться, а по делам, взрослым."
    m emo-3 "{i}Кто знает, кто знает.{/i}"
    mom emo-60 "Всем спасибо. [pname_max[0]], быстрее одевайся и поехали."
label pgn_events_12_maxclinic_04b:
    scene animated pgn_transp_city_mom_day
    $ renpy.pause(3, hard=True)
    scene pgn_maxassay_eventmom_01_vezdessushij
    mom emo-64 "[pname_max[0]]! Сядь нормально, ты не дома."
    m emo-0 "Но мне так удобнее."
    scene pgn_maxassay_eventmom_02_vezdessushij
    m emo-3 "{i}Мама не может отвести глаза от моих штанов. Ей хочется и мне очень хочется кончить.{/i}"
    scene pgn_maxassay_eventmom_03_vezdessushij
    eva emo-128 "Привет, [pname_mom[6]] и [pname_max[0]]. Извините за задержку."
    scene pgn_maxhometrauma_13_vezdessushij
    eva emo-129 "[pname_max[0]], надеюсь ты выполнил условие? Если нет, то придётся нам встретиться в другой раз."
    m emo-9 "{i}Ещё неделю, ну уж нет.{/i}"
    mom emo-60 "Всё нормально, иначе бы нас здесь не было."
    eva emo-128 "Ну хорошо, тогда снимай штаны."
    scene pgn_maxassay_eventmom_04_vezdessushij
    eva emo-130 "Поможешь ему? Если я правильно помню, у него болезнь с кистями рук."
    mom emo-73 "[pname_max[0]], может всё же сам попробуешь? Я твоя Мама, а не девушка, не могу же всю твою жизнь делать это за тебя."
    m emo-2 "Ну пожалуйста!"
    mom emo-69 "Хорошо, ладно."
    scene pgn_maxassay_eventmom_05_vezdessushij
    m emo-4 "{i}Наконец-то кончу, а то скопилось очень много. На всех хватит: на Маму, сестёр, девчонок...{/i}"
    m emo-7 "{i}Ммм... Мамины ручки, гладкие, нежные. Обалдеть.{/i}"
    scene pgn_maxassay_eventmom_06_vezdessushij
    mom emo-69 "Что-то не выходит у меня. Ева, может есть какой-то другой способ?"
    eva emo-129 "Надо подумать."
    m emo-8 "{i}Даже кончить нормально не могу.{/i}"
    eva emo-132 "Может стоит увлажнить член, тогда наверное получится."
    scene pgn_maxassay_eventmom_07_vezdessushij
    $ PGN_Achadd(pgnach_153, 153)
    mom emo-73 "Да, точно, не подумала..."
    scene pgn_maxassay_eventmom_08_vezdessushij
    m emo-9 "{i}Блин! Мама! Тут же Ева!{/i}"
    scene pgn_maxassay_eventmom_09_vezdessushij
    m emo-13 "М... Ма..."
    scene pgn_maxassay_eventmom_10_vezdessushij
    m emo-9 "{i}Она не удивлена? С удовольствием наблюдает, как Мама сосёт мне?{/i}"
    scene pgn_maxassay_eventmom_11_vezdessushij
    m emo-1 "М... М... Мама..."
    mom emo-62 "Что такое, [pname_max[0]]?"
    m emo-1 "Ева..."
    eva emo-130 "На меня не обращайте внимание, продолжайте."
    scene pgn_maxassay_eventmom_12_vezdessushij
    mom emo-68 "Я всё объясню. Ты же знаешь, что у него проблемы с кистями рук и он парень молодой, гормоны эти, его... потребности... мои потребности..."
    mom emo-69 "Мне нет оправдания. Знаю, что это неправильно, мама не должна такое вытворять со своим ребенком."
    eva emo-133 "Существует такое понятие, как \"Эдипов комплекс\". Но он наблюдается у детей, а в вашем случае он явно затянулся. Интересно, очень интересно. [pname_mom[6]], давно это у вас?"
    mom emo-69 "Нет, нет, у нас... Т.е это впервые, это моё решение, спонтанное. "
    eva emo-129 "[pname_mom[7]]! Не ври мне! Я не собираюсь тебя отчитывать или сообщать в органы. Скажи мне честно, как подруге."
    $ label_random = rd((days/30)+2)
    mom emo-73 "Месяцев [label_random]"
    eva emo-130 "Ясно. [pname_mom[6]], помоги своему сыну кончить. А потом с тобой пообщаемся об этом."
    scene pgn_maxassay_eventmom_13_vezdessushij
    m emo-3 "Мам, раз Ева уже знает, может всё же ртом продолжишь."
    mom emo-64 "[pname_max[0]]!"
    eva emo-132 "[pname_mom[6]], не стесняйся. Ему вредно так долго держать всё в себе."
    mom emo-69 "Хорошо."
    scene animated pgn_maxassay_eventmom_14
    m emo-3 "{i}Не ожидал от Евы такой реакции. Мне нравится этот город.{/i}"
    scene pgn_maxassay_eventmom_15_vezdessushij
    m emo-6 "{i}Еве определенно нравится на нас смотреть. Её это возбуждает или просто профессиональный интерес?{/i}"
    scene pgn_maxassay_eventmom_16_vezdessushij
    m emo-4 "{i}Всё же она тоже возбуждена.{/i}"
    scene animated pgn_maxassay_eventmom_14
    $ renpy.pause()
    m emo-10 "Я сейчас кончу... Мама..."
    scene pgn_maxassay_eventmom_17_vezdessushij
    m emo-10 "Арргх..."
    scene pgn_maxassay_eventmom_18_vezdessushij
    m emo-12 "Аааахх... Да..."
    scene pgn_maxassay_eventmom_19_vezdessushij
    m emo-13 "{i}Как же много у меня там скопилось. Чёрт!!!{/i}"
    scene pgn_maxassay_eventmom_20_vezdessushij
    mom emo-62 "[pname_max[0]], как ты себя чувствуешь?"
    m emo-7 "Намнооооого легче. Спасибо, Мам."
    mom emo-75 "Для меня это было слишком много."
    scene pgn_maxassay_eventmom_21_vezdessushij
    eva emo-133 "Незабываемое зрелище."
    mom emo-73 "Ева, прости, я совсем забыла, что его сперма нужна для анализов."
    m emo-9 "Я больше не хочу неделю сдерживаться!"
    eva emo-131 "Думаю так долго больше не потребуется. Можешь как обычно 1 раз в 3 дня."
    scene pgn_maxassay_eventmom_22_vezdessushij
    eva emo-128 "[pname_mom[6]], задержись на минутку, поговорим."
    m emo-3 "А можно я останусь?"
    mom emo-60 "[pname_max[0]], ты получил, что хотел. Так что иди к машине, а тут нам взрослым нужно поговорить."
    m emo-0 "Ладно."
    eva emo-128 "И [pname_max[0]], пока не ушёл. В следующий раз, если надумаешь приехать, прихвати с собой маму."
    m emo-13 "Постараюсь не забыть."

    if pgn_ach_repeat == 153:
        jump table_pgn_achievement

    $ eva_path, qtime, days_eva, clinic_time = 3.9, 14, 0, 3
    $ PGN_Addstatsex(stat_mom, 0, 0, 1, 0, 0)
    scene animated pgn_transp_city_mom_day
    $ renpy.pause(3, hard=True)
    jump loc_pool


label pgn_events_12_maxclinic_05:
    scene pgn_maxassay_withmom_01_vezdessushij
    eva emo-133 "[pname_mom[7]], [pname_max[0]], рада вас увидеть. Устраивайтесь поудобнее."
    scene pgn_maxassay_withmom_02_vezdessushij
    eva emo-130 "[pname_mom[7]], как думаешь, [pname_max[2]] нужна визуальная стимуляция для эрекции?"
    m emo-3 "Мне это поможет быстрее кончить. А эрекция и так есть от таких сексуальных..."
    mom emo-68 "[pname_max[0]]! Ну как тебе не стыдно такое говорить вслух."
    scene pgn_maxassay_withmom_03_vezdessushij
    eva emo-132 "Вижу ты тоже подготовилась."
    mom emo-68 "Тоже? А, т.е мы..."
    m emo-4 "Вы обе очень сексуально выглядите."
    eva emo-133 "Спасибо."
    mom emo-62 "Всё ради твоего здоровья."
    scene pgn_maxassay_withmom_04_vezdessushij
    eva emo-133 "[pname_mom[7]], а ты когда последний раз была на приёме у гинеколога?"
    mom emo-60 "Давно не была. Себя прекрасно чувствую, нет повода ходить."
    eva emo-128 "[pname_liza[0]] ещё очень молодая, а ты её каждую неделю приводишь на осмотр."
    mom emo-60 "Так я же волнуюсь и переживаю за её здоровье."
    eva emo-133 "[pname_mom[6]], и о себе нужно тоже позаботиться. Как-нибудь загляни ко мне для планового осмотра."
    scene pgn_maxassay_withmom_05_vezdessushij
    m emo-3 "{i}Ох блин, это чертовски круто. Мама в одних трусиках дрочит мне, а Ева очень близко стоит и мастурбирует киску.{/i}"
    m emo-4 "{i}От такой близости ощущаю её горячую киску.{/i}"
    scene pgn_maxassay_withmom_06_vezdessushij
    m emo-3 "{i}Неожидал, что Мама специально ещё подготовится.{/i}"
    scene pgn_maxassay_withmom_07_vezdessushij
    m emo-3 "{i}Вот бы тройничок с ними.{/i}"
    eva emo-129 "Мама тебя натренировала, что не кончаешь долго или это всё ещё действие от таблетки?"
    eva emo-132 "[pname_mom[6]], ты не против если я его дополнительно простимулирую."
    mom emo-62 "Ева, делай всё что необходимо."
    scene pgn_maxassay_withmom_08_vezdessushij
    $ PGN_Achadd(pgnach_154, 154)
    eva emo-132 "[pname_max[0]], одолжи мне свою руку."
    scene animated pgn_maxassay_withmom_09
    $ renpy.pause()
    m emo-10 "Ааа... Сейчас кончу..."
    scene pgn_maxassay_withmom_10_vezdessushij
    m emo-12 "Ааааххх.."
    scene pgn_maxassay_withmom_11_vezdessushij
    eva emo-132 "Отлично. Ещё материал для исследований. [pname_max[0]], держи, это твоё."
    if pgn_ach_repeat == 0:
        $ screennotify("$", 1, 100)
    mom emo-60 "[pname_max[0]], ты счастливчик. Получаешь удовольствие и за это ещё деньги получаешь."
    eva emo-130 "Надо же как-то парня стимулировать приходить почаще. Исследование трудное и его спермы нужно много."
    eva emo-133 "Спасибо вам, приходите ещё. [pname_mom[6]], как-нибудь загляни ко мне, одна. Хорошо?"
    mom emo-62 "Если найдётся свободное время."

    if pgn_ach_repeat == 154:
        jump table_pgn_achievement

    $ eva_path, qtime, clinic_time, currency, eva_cum = 4, qtime+1, 3, currency+100, eva_cum+1
    $ PGN_Addstatsex(stat_mom, 0, 0, 0, 0, 1)
    jump loc_clinic_4f_recept



label pgn_events_12_maxclinic_06:
    scene pgn_maxassay_withmom_02_vezdessushij
    eva emo-133 "Рада снова вас видеть, вместе."
    mom emo-60 "Привет, Ева."
    eva emo-128 "Ну что, начнём?"
    mom emo-60 "Да, конечно. [pname_max[0]], снимай штаны."
    scene pgn_maxassay_eventmom_06_vezdessushij
    eva emo-131 "[pname_mom[6]], а, чего ты?"
    mom emo-60 "Для разогрева."
    eva emo-131 "У [pname_max[1]] и так, всё готово."
    mom emo-73 "Да... Я... Хорошо. Тогда начну."
    scene pgn_maxassay_eventmom_08_vezdessushij
    m emo-13 "{i}Сразу к делу.{/i}"
    scene pgn_maxassay_eventmom_08_vezdessushij
    m emo-3 "{i}Могла бы предложить Еве.{/i}"
    scene pgn_maxassay_eventmom_16_vezdessushij
    m emo-13 "{i}Ева время зря не теряет. Трахнуть бы её сейчас. Только Мама наверное не позволит.{/i}"
    scene animated pgn_maxassay_eventmom_14
    $ renpy.pause()
    menu:
        "Остановить Маму":
            scene pgn_maxassay_eventmom_15_vezdessushij
            m emo-5 "Мама! Мама... Подожди, остановись..."
            mom emo-62 "[pname_max[0]], что случилось?"
            m emo-2 "Может Ева тоже к нам присоединится?"
            eva emo-128 "[pname_max[0]], спасибо, но мне и здесь хорошо. Я совсем не против наблюдать за вами."
            menu:
                "Настоять":
                    m emo-2 "..."
                    mom emo-62 "Ева, составишь нам компанию?"
                    $ label_random = 5
                "Продолжить":
                    $ label_random = renpy.random.randint ( 1, 4)
        "Продолжить":
            $ label_random = renpy.random.randint ( 1, 3)
    if label_random == 3:
        m emo-10 "Мама! Я сейчас кончу!"
        $ scene_random = renpy.random.randint ( 1, 3)
        if scene_random == 1:
            scene pgn_maxassay_eventmom_17_vezdessushij
        if scene_random == 2:
            scene pgn_maxassay_eventmom_18_vezdessushij
        if scene_random == 3:
            scene pgn_maxassay_eventmom_19_vezdessushij
        m emo-12 "Аррггххх... Ахх... Да..."
        scene pgn_maxassay_eventmom_20_vezdessushij
        eva emo-128 "Эх, [pname_max[0]]. Снова оставил меня ни с чем."
        scene pgn_maxassay_eventmom_21_vezdessushij
        mom emo-69 "Ой! Ева прости. Это полностью моя вина."
        eva emo-133 "Ничего страшного. Да, [pname_max[0]]? Ещ раз придёшь?"
        m emo-3 "Да."
        eva emo-128 "Хорошо. Тогда до следующего раза. Пока."
    elif label_random != 3:
        if label_random == 5:
            eva emo-133 "Тогда, как в прошлый раз. [pname_mom[7]]?"
            mom emo-60 "Хорошо."
        else:
            scene pgn_maxassay_eventmom_13_vezdessushij
            mom emo-69 "Что же снова такое. Ни как не можешь кончить. Может снова рукой?"
            scene pgn_maxassay_eventmom_05_vezdessushij
            m emo-13 "{i}Ох, блин! Как же сильно Мама сжала мой член.{/i}"
            eva emo-131 "[pname_mom[7]]. [pname_mom[7]]!"
            scene pgn_maxassay_eventmom_06_vezdessushij
            eva emo-131 "Перестань. Ты так парню его инструмент сломаешь. Давай лучше я помогу. Разденемся, ты продолжишь ртом, а я буду рядом."
            mom emo-69 "Хорошо. Извини, меня [pname_max[0]]."
            m emo-13 "Всё нормально."
        scene pgn_maxassay_withmom_03_vezdessushij
        eva emo-133 "..."
        scene pgn_maxassay_withmom_05_vezdessushij
        m emo-4 "{i}Ева перевозбудилась. Руки так и тянутся к киске.{/i}"
        scene pgn_maxassay_withmom_06_vezdessushij
        m emo-5 "{i}Блин! Сейчас очень сильно захотелось секса.{/i}"
        scene pgn_maxassay_withmom_07_vezdessushij
        m emo-3 "{i}Сразу бы их обеих.{/i}"
        scene animated pgn_maxassay_withmom_09
        $ renpy.pause()
        m emo-10 "Ааа... Сейчас кончу..."
        scene pgn_maxassay_withmom_10_vezdessushij
        m emo-12 "Ааааххх.."
        scene pgn_maxassay_withmom_11_vezdessushij
        eva emo-132 "Отлично. Ещё материал для исследований. [pname_max[0]], держи, это твоё."
        $ screennotify("$", 1, 100)
        scene pgn_maxassay_withmom_02_vezdessushij
        eva emo-133 "спасибо, что пришли. Буду вас ждать, когда надумаете ещё."
    $ qtime, clinic_time = qtime+1, 3
    $ PGN_Addstatsex(stat_mom, 0, 0, 1, 0, 0)
    jump loc_clinic_4f_recept
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
