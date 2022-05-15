






label pgn_events_11_alicecam_01:
    scene n-cam-1
    a emo-21 "Приветик, Майк! Соскучился?"
    m emo-3 "Ага... Что сегодня покажешь?"
    a emo-31 "Как обычно... Что захочешь, только в разумных пределах..."
    m emo-0 "..."
    scene n-cam-2
    a emo-20 "Майк! Ты здесь?"
    m emo-0 "..."
    a emo-20 "Не молчи."
    m emo-0 "Я видел тебя на другом ресурсе. И ты там за меньшее готова показать всё своё тело и заняться сексом. А мне, в привате, даже киску не показала."
    a emo-30 "Ох! Майк! Прости... я..."
    m emo-0 "{i}Да, да, ой прости, я не хотела и что-то в этом роде. И так ясно, что пытаешь развести лоха на деньги... Хотя это я, блин.{/i}"
    m emo-0 "Тогда может наконец-то покажешь мне всю себя. Я точно этого заслужил."
    a emo-20 "Так то да... но..."
    m emo-6 "{i}Но?!{/i}"
    scene n-cam-3
    a emo-21 "Давай так поступим. Ты же знаешь, я... "
    m emo-0 "{i}Снова думала сказать, что бедная и нужно больше денег, но ты уже спалилась.{/i}"
    a emo-21 "Может быть купишь мне что-то, что доставит мне удовольствие и что-то, что сильно не шумит, тогда, специально для тебя, буду устраивать бесплатные шоу."
    a emo-21 "Как тебе такое?"
    m emo-0 "{i}Блин. Ладно, попробуем по твоим правилам.{/i}"
    m emo-0 "Хорошо, я куплю. Но ты обещаешь, что не обманешь меня снова?"
    a emo-25 "Обещаю."
    m emo-0 "Тогда покажешь мне сейчас, хоть что-нибудь?"
    scene n-cam-2
    a emo-24 "Ой! У меня больше нет времени, прости. И увидимся, когда пришлёшь мне что-нибудь."
    m emo-0 "{i}Эм...{/i}"
    a emo-21 "Пока."
    $ alice_path = 15
    $ qtime += 1
    jump jump_dialogue



label pgn_events_11_alicecam_02:
    python:
        for i in pink_unicorn:
            if i.buy == True and i.have == True:
                i.have = False
                accessiv.append("секс-игрушка_у_алисы")
    if (sexitem_vibroedge1.buy == True and sexitem_vibroedge1.instore == False and sexitem_vibroedge1.have == False and sexitem_vibroedge1.dostavka == 0) and (sexitem_analdildo1.buy == True and sexitem_analdildo1.instore == False and sexitem_analdildo1.have == False and sexitem_analdildo1.dostavka == 0) and (sexitem_cowgirl1.buy == True and sexitem_cowgirl1.instore == False and sexitem_cowgirl1.have == False and sexitem_cowgirl1.dostavka == 0):
        $ accessiv.append("камшоу_алиса_011_все_игрушки")
    m emo-0 "Сделано. Осталось дождаться, когда смогу посмотреть."
    jump jump_dialogue


label pgn_events_11_alicecam_03:
    m emo-0 "Тут тебе, на твоё имя, пришла посылка."
    a emo-31 "Вау! Класс!!!"
    m emo-0 "А что там?"
    a emo-20 "Не твоё дело. Свободен."
    m emo-0 "Хотя бы спасибо сказала."
    a emo-21 "Спасибо, что не поленился и принёс его мне. Молодец, молодец. А теперь оставь меня одну."
    python:
        for i in pink_unicorn:
            if i.buy == True and i.have == True:
                i.have = False
                accessiv.append("секс-игрушка_у_алисы")
    if (sexitem_vibroedge1.buy == True and sexitem_vibroedge1.instore == False and sexitem_vibroedge1.have == False and sexitem_vibroedge1.dostavka == 0) and (sexitem_analdildo1.buy == True and sexitem_analdildo1.instore == False and sexitem_analdildo1.have == False and sexitem_analdildo1.dostavka == 0) and (sexitem_cowgirl1.buy == True and sexitem_cowgirl1.instore == False and sexitem_cowgirl1.have == False and sexitem_cowgirl1.dostavka == 0):
        $ accessiv.append("камшоу_алиса_011_все_игрушки")
    jump jump_dialogue


label pgn_events_11_alicecam_homecam:
    $ ivent24.append("камшоу_алисы")
    scene pgn_11_aliceroom_camshow_01
    a emo-21 "Майк. Привет. Я тебя ждала."
    if ("секс-игрушка_у_алисы") in accessiv and ("камшоу_алиса_011_все_игрушки") not in accessiv:
        $ accessiv.remove("секс-игрушка_у_алисы")
        m emo-0 "Получила мой подарок?"
        scene pgn_11_aliceroom_camshow_02
        a emo-20 "Да. Сейчас его найду."
        if sexitem_vibroedge1.buy == True and ("алиса_сексигрушка1") not in accessiv:
            jump pgn_events_11_alicecam_homecam_vibroedge1
        elif sexitem_analdildo1.buy == True and ("алиса_сексигрушка2") not in accessiv:
            jump pgn_events_11_alicecam_homecam_analdildo1
        elif sexitem_cowgirl1.buy == True and ("алиса_сексигрушка3") not in accessiv:
            jump pgn_events_11_alicecam_homecam_cowgirl1
    else:
        scene pgn_11_aliceroom_camshow_02
        a emo-20 "Что выбирешь?"
        menu:
            "Виброяйцо" if sexitem_vibroedge1.buy == True and sexitem_vibroedge1.instore == False and sexitem_vibroedge1.have == False and sexitem_vibroedge1.dostavka == 0:
                jump pgn_events_11_alicecam_homecam_vibroedge1
            "Анальная цепочка" if sexitem_analdildo1.buy == True and sexitem_analdildo1.instore == False and sexitem_analdildo1.have == False and sexitem_analdildo1.dostavka == 0:
                jump pgn_events_11_alicecam_homecam_analdildo1
            "Секс-машина Cowgirl" if sexitem_cowgirl1.buy == True and sexitem_cowgirl1.instore == False and sexitem_cowgirl1.have == False and sexitem_cowgirl1.dostavka == 0:
                jump pgn_events_11_alicecam_homecam_cowgirl1


label pgn_events_11_alicecam_homecam_vibroedge1:
    a emo-20 "Где он тут у меня... Минуту... А вот, нашла."
    scene pgn_11_aliceroom_camshow_03
    a emo-22 "Вот он маленький негодник."
    if ("алиса_сексигрушка1") not in accessiv:
        $ accessiv.append("алиса_сексигрушка1")
        if alice_path == 15:
            m emo-0 "Ты же покажешь свою киску или мне снова только на твоё лицо смотреть?"
            a emo-24 "Не переживай, всё увидишь, скрывать больше ничего не буду."
    scene pgn_11_aliceroom_camshow_04
    a emo-20 "Сейчас настрою камеру и сам всё увидишь."
    scene animated pgn_events_11_alicecam_homecam_vibroedge1_01
    $ renpy.pause()
    a emo-33 "Ммм... Легко вошло."
    m emo-3 "..."
    scene pgn_11_aliceroom_camshow_06_anim_01
    a emo-21 "И так, управлять игрушкой будешь ты. Просто нажимай на кнопку."
    m emo-0 "Понял."
    $ scene_random, label_random = 1, 0
    call pgn_ev11_alicecamhome_vibroedge1_speed from _call_pgn_ev11_alicecamhome_vibroedge1_speed

label pgn_ev11_alicecamhome_vibroedge1_speed:
    if scene_random == 1:
        scene animated pgn_events_11_alicecam_homecam_vibroedge1_02_1
    elif scene_random == 2:
        scene animated pgn_events_11_alicecam_homecam_vibroedge1_02_2
    elif scene_random == 3:
        scene animated pgn_events_11_alicecam_homecam_vibroedge1_02_3
    show screen pgn_ev11_alicecamhome_time()
    while label_random < 350:
        $ renpy.pause(1)
        $ label_random += scene_random
    jump pgn_ev11_alicecamhome_vibroedge1_end

screen pgn_ev11_alicecamhome_time():

    vbox:
        align (0.8, 0.3)
        button:
            maximum (90, 270)
            xalign 0.5
            has vbox
            if scene_random == 1:
                add "vibroegg_speed_1_c"
            if scene_random != 1:
                imagebutton idle "vibroegg_speed_1_a" hover "vibroegg_speed_1_a" action [SetVariable("scene_random", 1), Jump("pgn_ev11_alicecamhome_vibroedge1_speed")]

            if scene_random == 1:
                imagebutton idle "vibroegg_speed_2_b" hover "vibroegg_speed_2_a" action [SetVariable("scene_random", 2), Jump("pgn_ev11_alicecamhome_vibroedge1_speed")]
            if scene_random == 2:
                add "vibroegg_speed_2_c"
            if scene_random == 3:
                imagebutton idle "vibroegg_speed_2_a" hover "vibroegg_speed_2_a" action [SetVariable("scene_random", 2), Jump("pgn_ev11_alicecamhome_vibroedge1_speed")]

            if scene_random == 3:
                add "vibroegg_speed_3_c"
            if scene_random != 3:
                imagebutton idle "vibroegg_speed_3_b" hover "vibroegg_speed_3_a" action [SetVariable("scene_random", 3), Jump("pgn_ev11_alicecamhome_vibroedge1_speed")]
        null height 50
        button:
            maximum (287, 268)
            xpadding 71
            imagebutton idle "vibroegg_a" hover (im.MatrixColor("images/mods/pgn/renders/home/aliceroom/camshow/gui/vibroegg_a.png",im.matrix.opacity(0.60))) action [SetVariable("label_random", label_random+5), Hide("pgn_ev11_alicecamhome_vibroedge1"), Show("pgn_ev11_alicecamhome_vibroedge1"), Play("sound", "/content/audio/chat_tip_sound.ogg")]
            background "animated pgn_events_11_alicecam_homecam_vibroedge1_vibr"

screen pgn_ev11_alicecamhome_vibroedge1:
    if scene_random == 1:
        add "animated pgn_events_11_alicecam_homecam_vibroedge1_03_1"
    if scene_random != 1:
        add "animated pgn_events_11_alicecam_homecam_vibroedge1_03_2"

    use pgn_ev11_alicecamhome_time

    timer 2.0 action [Hide("pgn_ev11_alicecamhome_vibroedge1"), Jump("pgn_ev11_alicecamhome_vibroedge1_speed")]

label pgn_ev11_alicecamhome_vibroedge1_end:
    $ screenhide()
    a emo-26 "Я кончаю."
    scene pgn_11_aliceroom_camshow_08
    $ PGN_Achadd(pgnach_129, 129)
    a emo-30 "Ааааххх..."
    m emo-0 "Раздвинь ноги, мне ничего не видно..."
    a emo-28 "Ох... Спасибо, это было круто. Может даже лучше члена внутри."
    if alice_path >= 17:
        m emo-6 "В смысле, лучше?"
    else:
        m emo-6 "{i}Лучше?! Видно кого-то я мало трахаю, сестрёнка.{/i}"
    scene pgn_11_aliceroom_camshow_09
    if (("алиса_сексигрушка1") not in accessiv or ("алиса_сексигрушка2") not in accessiv or ("алиса_сексигрушка3") not in accessiv) and alice_path < 16:
        a emo-31 "Спасибо. С нетерпением буду ждать следующего раза с другим подарком."
    if pgn_ach_repeat == 129:
        jump table_pgn_achievement
    if alice_path >= 17:
        call pgn_events_11_alicecam_homecam2_bill from _call_pgn_events_11_alicecam_homecam2_bill
    else:
        a emo-31 "Спасибо. С нетерпением буду ждать следующего раза с другой игрушкой."
        m emo-0 "Может повторим?"
        a emo-21 "Может быть, но в другой раз. Пока."
    $ qtime += 1
    jump loc_my_room_comp


label pgn_events_11_alicecam_homecam_analdildo1:
    if ("алиса_сексигрушка2") not in accessiv:
        $ accessiv.append("алиса_сексигрушка2")
    scene pgn_11_aliceroom_camshow_10
    a emo-24 "Он больше, стандартных размеров."
    m emo-3 "Специально взял именно такой."
    if alice_path >= 17:
        m emo-4 "Всё самое лучшее для твоей попки."
        a emo-20 "Ну хорошо, сделаю, раз так этого хочешь."
    else:
        a emo-20 "И куда хочешь, чтобы его всунула?"
        m emo-4 "Я думал ты догадливая... в твою попку."
        a emo-25 "Тебе повезло, моя дырочка разработанная. Иначе бы не согласилась."
        m emo-4 "Рад стараться"
        a emo-29 "А?"
        m emo-3 "{i}Блин{/i}.\nТ.е. старался найти, именно такой... Ну так что, выполнишь мою просьбу?"
    scene animated pgn_events_11_alicecam_homecam_analdildo1_11_1
    $ renpy.pause()
    scene animated pgn_events_11_alicecam_homecam_analdildo1_11_2
    $ renpy.pause()
    m emo-4 "Давай глубже."
    a emo-22 "Не торопи, мне нужно привыкнуть."
    scene animated pgn_events_11_alicecam_homecam_analdildo1_11_3
    $ renpy.pause()
    scene animated pgn_events_11_alicecam_homecam_analdildo1_11_4
    $ renpy.pause()
    m emo-3 "Приблизь камеру."
    a emo-20 "Сейчас покажу ближе."
    scene pgn_11_aliceroom_camshow_012_anim_01
    m emo-3 "Я хочу видеть, как он из тебя выходит."
    scene animated pgn_events_11_alicecam_homecam_analdildo1_12_1
    $ renpy.pause()
    scene animated pgn_events_11_alicecam_homecam_analdildo1_12_2
    $ renpy.pause()
    a emo-21 "Ой..."
    scene animated pgn_events_11_alicecam_homecam_analdildo1_12_3
    $ renpy.pause()
    scene animated pgn_events_11_alicecam_homecam_analdildo1_12_4
    $ renpy.pause()
    scene pgn_11_aliceroom_camshow_13
    $ PGN_Achadd(pgnach_130, 130)
    a emo-24 "Упс!"
    a emo-33 "Мне ещё поиграть с попкой?"
    menu menu_pgn_events_11_alicecam_homecam_analdildo1:
        "Повторить":
            scene animated pgn_events_11_alicecam_homecam_analdildo1_11_1
            $ renpy.pause()
            scene animated pgn_events_11_alicecam_homecam_analdildo1_11_2
            $ renpy.pause()
            scene animated pgn_events_11_alicecam_homecam_analdildo1_11_3
            $ renpy.pause()
            scene animated pgn_events_11_alicecam_homecam_analdildo1_11_4
            $ renpy.pause()
            scene animated pgn_events_11_alicecam_homecam_analdildo1_12_1
            $ renpy.pause()
            scene animated pgn_events_11_alicecam_homecam_analdildo1_12_2
            $ renpy.pause()
            scene animated pgn_events_11_alicecam_homecam_analdildo1_12_3
            $ renpy.pause()
            scene animated pgn_events_11_alicecam_homecam_analdildo1_12_4
            $ renpy.pause()
            scene pgn_11_aliceroom_camshow_13
            jump menu_pgn_events_11_alicecam_homecam_analdildo1
        "Хватит":
            pass
    scene pgn_11_aliceroom_camshow_14
    if alice_path >= 17 and pgn_ach_repeat == 0:
        call pgn_events_11_alicecam_homecam2_bill from _call_pgn_events_11_alicecam_homecam2_bill_1
    if pgn_ach_repeat == 0 and ("алиса_сексигрушка1") in accessiv and ("алиса_сексигрушка2") in accessiv and ("алиса_сексигрушка3") in accessiv:
        a emo-25 "Надеюсь тебе понравилось. До следующего раза, пока."
    elif (("алиса_сексигрушка1") not in accessiv or ("алиса_сексигрушка2") not in accessiv or ("алиса_сексигрушка3") not in accessiv) and alice_path < 16:
        a emo-25 "Спасибо за подарок. Спасибо. С нетерпением буду ждать следующего раза с другим подарком."
    if pgn_ach_repeat == 130:
        jump table_pgn_achievement
    $ qtime += 1
    jump loc_my_room_comp


label pgn_events_11_alicecam_homecam_cowgirl1:
    if ("алиса_сексигрушка3") not in accessiv:
        $ accessiv.append("алиса_сексигрушка3")
        scene pgn_11_aliceroom_camshow_02
        a emo-20 "Он такой большой и тяжёлый. Он точно сильно не шумит?"
        m emo-4 "Да.\n{i}Ты будешь стонать гораздо громче.{/i}"
        scene pgn_11_aliceroom_camshow_15
        a emo-25 "Я никогда такого не видела в живую, всегда мечтала о таком устройстве. Спасибо."
        m emo-6 "Ну так?"
        a emo-21 "Да, да, сейчас."
    scene pgn_11_aliceroom_camshow_16
    $ PGN_Achadd(pgnach_131, 131)
    a emo-21 "Скоростью ты будешь управлять. Так что, позаботься обо мне."
    m emo-16 "{i}Конечно{/i}"
    $ scene_random, label_random, countdown = 1, 0, 0
label pgn_events_11_alicecam_homecam_cowgirl1_speed:
    show screen pgn_events_11_alicecam_homecam_cowgirl1_speed
    if scene_random == 1:
        scene animated pgn_events_11_alicecam_homecam_cowgirl1_17_1
    if scene_random == 2:
        scene animated pgn_events_11_alicecam_homecam_cowgirl1_17_2
    if scene_random == 3:
        scene animated pgn_events_11_alicecam_homecam_cowgirl1_18_1
        if alice_path >= 17:
            a emo-26 "[pname_max[0]]! Помедленнее, пожалуйста."
        else:
            a emo-26 "Майк. Помедленнее. Пожалуйста."
            a emo-24 "Майк. Он начинает издавать много шума, снизь скорость..."
        $ renpy.pause(0.01)
        while countdown < 20:
            $ renpy.pause(1)
            $ countdown += 1
        if pgn_ach_repeat == 0 and alice_path < 16:
            jump pgn_events_11_alicecam_04
        else:
            hide screen pgn_events_11_alicecam_homecam_cowgirl1_speed
            scene pgn_11_aliceroom_camshow_19
            if alice_path >= 17:
                a emo-30 "[pname_max[0]]!!!"
            else:
                a emo-30 "Майк!!!"
            scene pgn_11_aliceroom_camshow_23
            a emo-34 "Ааааахххххх.... аааа... "
            scene pgn_11_aliceroom_camshow_24
            jump pgn_events_11_alicecam_homecam_cowgirl1_end
    if scene_random == 4:
        scene animated pgn_events_11_alicecam_homecam_cowgirl1_18_2
        if alice_path >= 17:
            a emo-26 "Аааххххх... [pname_max[0]]..."
        else:
            a emo-26 "Ааахххх... Майк..."
        while countdown < 30:
            $ renpy.pause(1)
            $ countdown += 2
        if pgn_ach_repeat == 0:
            jump pgn_events_11_alicecam_04
        else:
            hide screen pgn_events_11_alicecam_homecam_cowgirl1_speed
            scene pgn_11_aliceroom_camshow_19
            if alice_path >= 17:
                a emo-30 "[pname_max[0]]!!!"
            else:
                a emo-30 "Майк!!!"
            scene pgn_11_aliceroom_camshow_23
            a emo-34 "Ааааахххххх.... аааа... "
            scene pgn_11_aliceroom_camshow_24
            jump pgn_events_11_alicecam_homecam_cowgirl1_end
    while label_random < 120:
        $ renpy.pause(1)
        $ label_random += scene_random
    hide screen pgn_events_11_alicecam_homecam_cowgirl1_speed
    if scene_random == 1:
        scene pgn_11_aliceroom_camshow_16
        a emo-30 "Ммм... ааааххх... Ох! Вау!"
        scene pgn_11_aliceroom_camshow_16b
        if alice_path >= 17:
            a emo-22 "[pname_max[0]]. Спасибо тебе. Это самая лучшая секс-игрушка."
        else:
            a emo-22 "Майк. Спасибо тебе. Это самая лучшая секс-игрушка."
        m emo-3 "Всегда пожалуйста."
    if scene_random == 2:
        $ label_random = renpy.random.randint ( 1, 3)
        if label_random == 3:
            scene pgn_11_aliceroom_camshow_18b
            a emo-30 "Ааааааххх.... Ох! Чёрт! Аааахххх..."
            m emo-4 "{i}Класс!!!{/i}"
            scene pgn_11_aliceroom_camshow_25
            m emo-4 "Может повторим?"
            if alice_path >= 17:
                a emo-22 "[pname_max[0]], нет. Ещё дольше продержаться на этой штуковине не смогу."
            else:
                a emo-26 "Извини, Майк, моя киска горит. Ещё дольше продержаться на этой штуковине не смогу."
            a emo-31 "Спасибо тебе."
        else:
            scene pgn_11_aliceroom_camshow_16b
            a emo-26 "Фух... Чуть не кончила."
            if alice_path >= 17:
                m emo-13 "Так не пойдёт, залезай обратно."
            else:
                m emo-13 "Эээ... Какого!? Я купил, потратил деньги, хочу увидеть бурный оргазм."
            scene pgn_11_aliceroom_camshow_25
            if alice_path >= 17:
                a emo-22 "[pname_max[0]], нет. Может в следующий раз."
            else:
                a emo-22 "Майк, прости. Но мне кровать нужна сухая. Может в следующий раз."
label pgn_events_11_alicecam_homecam_cowgirl1_end:
    if (("алиса_сексигрушка1") not in accessiv or ("алиса_сексигрушка2") not in accessiv or ("алиса_сексигрушка3") not in accessiv) and alice_path < 16:
        a emo-21 "Спасибо. С нетерпением буду ждать следующего раза с другим подарком."
    if pgn_ach_repeat == 131:
        jump table_pgn_achievement
    if alice_path >= 17:
        call pgn_events_11_alicecam_homecam2_bill from _call_pgn_events_11_alicecam_homecam2_bill_2
        a emo-21 "До следующего раза, [pname_max[0]]."
    else:
        a emo-21 "Пока, Майк."
    $ qtime += 1
    jump loc_my_room_comp

screen pgn_events_11_alicecam_homecam_cowgirl1_speed:

    vbox:
        align (0.8, 0.3)
        button:
            maximum (90, 270)
            xalign 0.5
            has vbox
            if scene_random == 1:
                add "cowgirl_speed_1_c"
            if scene_random != 1:
                imagebutton idle "cowgirl_speed_1_a" hover "cowgirl_speed_1_a" action [SetVariable("scene_random", 1), SetVariable("countdown", 0), Jump("pgn_events_11_alicecam_homecam_cowgirl1_speed")]

            if scene_random == 1:
                imagebutton idle "vibroegg_speed_2_b" hover "cowgirl_speed_2_a" action [SetVariable("scene_random", 2), SetVariable("countdown", 0), Jump("pgn_events_11_alicecam_homecam_cowgirl1_speed")]
            if scene_random == 2:
                add "cowgirl_speed_2_c"
            if scene_random == 3 or scene_random == 4:
                imagebutton idle "cowgirl_speed_2_a" hover "cowgirl_speed_2_a" action [SetVariable("scene_random", 2), SetVariable("countdown", 0), Jump("pgn_events_11_alicecam_homecam_cowgirl1_speed")]

            if scene_random == 1 or scene_random == 2:
                imagebutton idle "vibroegg_speed_2_b" hover "cowgirl_speed_2_a" action [SetVariable("scene_random", 3), Jump("pgn_events_11_alicecam_homecam_cowgirl1_speed")]
            if scene_random == 3:
                add "cowgirl_speed_2_c"
            if scene_random == 4:
                imagebutton idle "cowgirl_speed_2_a" hover "cowgirl_speed_2_a" action [SetVariable("scene_random", 3), Jump("pgn_events_11_alicecam_homecam_cowgirl1_speed")]

            if scene_random == 4:
                add "cowgirl_speed_3_c"
            if scene_random != 4:
                imagebutton idle "vibroegg_speed_3_b" hover "cowgirl_speed_3_a" action [SetVariable("scene_random", 4), Jump("pgn_events_11_alicecam_homecam_cowgirl1_speed")]


label pgn_events_11_alicecam_04:
    hide screen pgn_events_11_alicecam_homecam_cowgirl1_speed
    scene pgn_11_aliceroom_camshow_19
    a emo-30 "Майк!!!"
    scene pgn_11_aliceroom_camshow_20
    $ renpy.pause(5)
    scene pgn_11_aliceroom_camshow_21
    mom emo-64 "[pname_alice[0]]! Это как понимать?!"
    scene pgn_11_aliceroom_camshow_22
    a emo-30 "Мама!"
    mom emo-63 "Я слышала об этом от коллег по работе. Значит ты так зарабатываешь и давно?"
    scene pgn_11_aliceroom_camshow_23
    a emo-34 "Ааааахххххх.... аааа... "
    play sound "/content/audio/chat_tip_sound.ogg"
    mom emo-64 "[pname_alice[0]]?! А ну живо выключила!"
    stop sound
    scene pgn_11_aliceroom_camshow_24
    m emo-0 "{i}Нет, нет, я хочу послушать{/i}"
    scene black
    m emo-13 "{i}Кажется пришёл конец бизнес-плану [pname_alice[1]].{/i}"
    $ alice_path = 16
    $ qtime = 22
    jump loc_my_room_comp


label pgn_events_11_alicecam_05:
    k emo-104 "[pname_max[0]] подойди ко мне. У меня есть кое-что для тебя."
    m emo-0 "Что?"
    k emo-101 "Помнишь, когда впервые приехали в нашу квартиру, там была комната, в которую невозможно было войти?"
    m emo-0 "Вроде, да."
    k emo-101 "Вот держи ключи."
    m emo-6 "А что там, в той комнате?"
    k emo-100 "Не знаю. Съезди, узнаешь, а потом может расскажешь."
    m emo-3 "Ок. Спасибо."
    $ alice_path = 16.2
    jump jump_dialogue


label pgn_events_11_alicecam_06:
    scene pgn_11_aliceroom_camshow_27
    m emo-3 "Привет. А что одетая сидишь? Стрима сегодня не будет?"
    a emo-20 "Нет"
    m emo-0 "Что-то случилось или просто нет настроения?"
    a emo-20 "В прошлый раз, когда я вела трансляцию, Мама меня поймала за этим делом и запретила."
    m emo-0 "И что будешь делать?"
    a emo-29 "Придётся на время забыть о стримах, когда Мама дома. Чёрт! Так потеряю много клиентов."
    m emo-13 "Может я могу что-нибудь сделать?"
    a emo-28 "Ты сможешь её как-то убедить? Она большего всего рассержена не из-за того, что я этим занималась, а из-за [pname_liza[4]]"
    m emo-0 "Ну я попробую что-нибудь придумать."
    $ alice_path = 16.1
    jump jump_dialogue


label pgn_events_11_alicecam_07:
    if qtime >= 17:
        scene pgn_aptkira_first_02_vezdessushij
        $ renpy.pause(2)
        scene pgn_aptkira_first_03_vezdessushij
        m emo-0 "Посмотрим, что там."
    scene pgn_aptkira_sroom
    m emo-1 "Ого!"
    m emo-4 "Кажется у меня есть идея, как можно использовать эту комнату."
    m emo-3 "Нужно поговорить с [pname_alice[4]]"
    $ alice_path = 16.3
    jump loc_hotel_aptkira_secretroom


label pgn_events_11_alicecam_08:
    scene pgn_11_aliceroom_camshow_27
    m emo-3 "У меня есть к тебе предложение."
    a emo-20 "Выкладывай."
    m emo-4 "Могу предложить тебе место, где ты сможешь от секс-машин стонать, кончать и не бояться, что тебя кто-то заметит."
    a emo-21 "Спасибо!"
    a emo-28 "..."
    m emo-0 "Что?"
    scene pgn_11_aliceroom_camshow_28
    a emo-28 "Так, стоп. Я не говорила, что использовала на прошлом стриме и стрим был приватный."
    m emo-13 "Упс! Ну... я догадливый..."
    a emo-29 "Ясно. Значит Майк. Это ты. Нужно было и раньше об этом догадаться."
    a emo-29 "Ты специально купил, чтобы Мама застукала меня?"
    m emo-13 "Ну..."
    a emo-32 "Вот же говнюк. Может мне ей рассказать об этом? И ещё, что это ты надоумил меня на этот блог?"
    m emo-5 "Подожди, подожди. А может мне рассказать, что ты втянула меня и [pname_liza[3]] в этот бизнес?"
    a emo-28 "..."
    a emo-28 "Ну давай, расскажи ей, и посмотрим кому больше всего достанется."
    m emo-14 "Эм..."
    a emo-20 "Дошло? Болван."
    m emo-8 "Я не болван..."
    a emo-20 "Да, да."
    m emo-0 "Ну так, ты хочешь, чтобы я помог тебе с блогом, снова? Или мне уйти?"
    a emo-20 "Ладно, хорошо."
    m emo-3 "Только взамен, я буду получать свою долю."
    a emo-29 "А не приофигел случаем?"
    m emo-13 "Тогда может не будешь больше нас с [pname_liza[4]] наказывать?"
    a emo-33 "У тебя же вроде как эрекция от этих наказаний или хочешь сказать, что тебе не нравится?"
    m emo-0 "Договорились?"
    a emo-20 "Хм... Ладно, придётся согласиться. Но..."
    m emo-13 "Но?"
    a emo-21 "Занимайся с ней чем хочешь вне дома, наказывать не буду. А вот дома, про меня не забывайте. Ладно?"
    m emo-0 "Ладно..."
    a emo-20 "И что ты предлагаешь, снимать квартиру где-то?"
    m emo-4 "Снимать никакую квартиру или комнату не нужно. В квартире Тёти есть особая комната."
    a emo-25 "Особая?"
    m emo-4 "Ага. Тебе понравится. Можем прям сейчас поехать и я тебе покажу. "
    a emo-21 "Поехали"
    $ PGN_Moveement_events(2, 6, )
    scene pgn_11_hotelbdsm_first_01_vezdessushij
    a emo-20 "Тебе нравятся?"
    m emo-0 "Что?"
    a emo-20 "То что изображено на этих картинах?"
    m emo-0 "Открыл."
    scene pgn_11_hotelbdsm_first_02_vezdessushij
    a emo-30 "Вау! Вот это да!"
    scene pgn_11_hotelbdsm_first_03_vezdessushij
    m emo-5 "Хорошо получается. Где-то училась или так, навыки с прошлой работы?"
    a emo-28 "[pname_max[0]]. Ну ты блин, умеешь испортить настроение."
    scene pgn_11_hotelbdsm_first_04_vezdessushij
    a emo-33 "О! Даже это здесь есть. А что там в шкафчике, заглядывал?"
    m emo-0 "Нет."
    scene pgn_11_hotelbdsm_first_05_vezdessushij
    a emo-30 "Ого! Прям глаза разбегаются от всего этого."
    m emo-6 "Ага. Тут много всего. А это что?"
    a emo-28 "Руки убери! Не заляпай тут всё своими грязными руками."
    scene pgn_11_hotelbdsm_first_06_vezdessushij
    a emo-25 "Ну так что. Ты дашь мне ключи? А я взамен не буду тебя с [pname_liza[4]] наказывать."
    m emo-0 "Нет"
    a emo-24 "Мы же договаривались."
    m emo-0 "Ключи не дам. Если хочешь заниматься эти бизнесом, то только через меня."
    a emo-20 "Ладно. Хорошо. Только ты постоянно где-то и чем-то занят. Так что давай так. Ты заранее мне сообщишь, а потом после ужина поедем сюда."
    m emo-0 "Хорошо."
    a emo-21 "Договорились. Тогда поедем домой."
    m emo-13 "Может останемся?"
    a emo-22 "Нет, не сейчас. Если чего-то хочешь, получишь дома."
    m emo-0 "Блин."
    $ alice_path, qtime = 17, qtime+1
    $ PGN_Moveement_events(2, 6, )
    jump loc_pool


label pgn_events_11_alicecam_09:
    m emo-0 "Привет. Сегодня вечером поедешь со мной? Заниматься твоим блогом?"
    if daysn == 1 or daysn == 3 or daysn == 6:
        a emo-20 "Я бы хотела съездить, но сегодня Катя приедет. Так что сегодня не смогу."
        m emo-0 "Ладно"
    elif daysn == 5:
        a emo-20 "[pname_max[0]], ты же знаешь, что я по пятницам хожу в клуб."
        m emo-0 "Ладно"
    else:
        $ ivent24.append("камшоу_алисы_квартира_тёти")
        a emo-21 "С радостью."
        m emo-0 "Отлично. Тогда сегодня после ужина поедем."
    jump jump_dialogue


label pgn_events_11_alicecam_webshow:
    $ PGN_Moveement_events(2, 6)
    scene pgn_11_bdsmroom_webshow_01_vezdessushij
    a emo-20 "Куда это ты сразу пошёл. Сначала в ванную, а уже потом займёмся делом."
    scene pgn_aptkira_first_07_vezdessushij
    m emo-0 "Опять."
    scene pgn_aptkira_sroom
    a emo-20 "С чего начнём?"
    menu:
        "Шест":
            jump pgn_events_11_alicecam_webshow_pole
        "Naughty Device":
            jump pgn_events_11_alicecam_webshow_nd


label pgn_events_11_alicecam_webshow_pole:
    m emo-0 "Давай начнём с шеста."
    a emo-21 "Хорошо. А ты если что подскажешь, что делать или чего захотят зрители."
    m emo-3 "Ок."
    scene pgn_11_bdsmroom_webshow_pole_01_vezdessushij
    $ renpy.pause(10)
    scene pgn_11_bdsmroom_webshow_pole_02_vadx
    $ renpy.pause(10)
    scene pgn_11_bdsmroom_webshow_pole_03_vezdessushij
    $ renpy.pause(10)
    scene pgn_11_bdsmroom_webshow_pole_04_vadx
    $ renpy.pause(10)
    scene pgn_11_bdsmroom_webshow_pole_05_vezdessushij
    $ renpy.pause(10)
    scene pgn_11_bdsmroom_webshow_pole_06_vezdessushij
    $ renpy.pause(10)
    scene pgn_11_bdsmroom_webshow_pole_07_vezdessushij
    $ renpy.pause(10)
    scene pgn_11_bdsmroom_webshow_pole_08_vezdessushij
    $ PGN_Achadd(pgnach_132, 132)
    $ renpy.pause(10)
    scene pgn_11_bdsmroom_webshow_pole_09_vadx
    $ renpy.pause(10)
    a emo-21 "Что дальше?"
    menu menu_1_pgn_events_11_alicecam_webshow_pole:
        "Может что посложнее?" if ("камшоу_алисы_квартира_тёти_МВ1") not in ivent24:
            $ ivent24.append("камшоу_алисы_квартира_тёти_МВ1")
            a emo-20 "Я не умею."
            m emo-0 "Может тогда где-нибудь этому научишься?"
            a emo-22 "А ты готов оплатить мне занятия? Пока что буду делать всё, что в моих силах."
            jump menu_1_pgn_events_11_alicecam_webshow_pole
        "Пусть зрители выберут" if pgn_ach_repeat == 0:
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random == 2:
                m emo-3 "Зрители хотят, чтобы ты мне отсосала."
            else:
                scene pgn_11_bdsmroom_webshow_nd_01_vezdessushij
                m emo-1 "Удобно?"
                a emo-26 "Начинай, я уже потекла."
                jump pgn_events_11_alicecam_webshow_nd_next
        "Потрись попкой об шест":
            m emo-1 "Упрись попой об шест. И нагнись вперед."
            scene pgn_11_bdsmroom_webshow_pole_10_vezdessushij
            a emo-21 "Хорошо. Что дальше?"
            scene pgn_11_bdsmroom_webshow_pole_11_vezdessushij
            m emo-1 "Теперь двигай попой вверх и вниз."
            scene animated pgn_11_bdsmroom_webshow_pole_12
            $ renpy.pause(5)
            m emo-4 "Представь. Будто это мой член и дрочишь его мне своей упругой попкой."
            scene animated pgn_11_bdsmroom_webshow_pole_12
            $ renpy.pause(0)
            scene pgn_11_bdsmroom_webshow_pole_13_vadx
            m emo-3 "Достаточно. Клиент хочет следующее..."
    scene pgn_11_bdsmroom_webshow_pole_14_vadx
    a emo-25 "Ну раз клиент желает, то я не против."
    scene animated pgn_11_bdsmroom_webshow_pole_15
    $ renpy.pause()
    m emo-4 "Отлично. Соси, глубже, заглатывай..."
    m emo-3 "{i}Сестрёнка хорошо старается. Когда-нибудь может смогу трахнуть её горло. А пока и так нравится.{/i}"
    m emo-3 "Полижешь мне яйца?"
    a emo-26 "Мхмм..."
    scene pgn_11_bdsmroom_webshow_pole_16_vadx
    m emo-10 "Лижи старательно... Ммм... Класс!"
    m emo-3 "И обратно в рот"
    scene animated pgn_11_bdsmroom_webshow_pole_15
    $ renpy.pause()
    m emo-4 "Скоро кончу, продолжай."
    scene animated pgn_11_bdsmroom_webshow_pole_15
    $ renpy.pause()
    menu:
        "Кончить с расстояния":
            scene pgn_11_bdsmroom_webshow_pole_17_vadx
        "Кончит прям в рот":
            scene pgn_11_bdsmroom_webshow_pole_18_vadx
    m emo-12 "Аргхх... Аааа... Да..."
    scene pgn_11_bdsmroom_webshow_pole_19
    a emo-22 "Думаю зрителям понравилось..."
    m emo-4 "Мне тоже."
    a emo-33 "..."
    a emo-21 "На сегодня хватит. Уже поздно и нам пора."
    if pgn_ach_repeat == 132:
        jump table_pgn_achievement
    $ ivent24.append("камшоу_алисы_квартира_тёти_шест")
    $ PGN_Addstatsex(stat_alice, 0, 0, 1, 0, 0)
    if alice_path == 17:
        $ alice_path = 18
    scene pgn_11_bdsmroom_webshow_02_vezdessushij
    $ renpy.pause(5, hard=True)
    scene pgn_11_bdsmroom_webshow_03_vezdessushij with fade
    m emo-0 "Блин. Не разбудила меня."
    call next_time_days from _call_next_time_days_2
    call max_sleep_reset from _call_max_sleep_reset_4
    $ qtime = 8
    jump loc_hotel_aptkira_bedroom


label pgn_events_11_alicecam_webshow_nd:
    scene pgn_11_bdsmroom_webshow_nd_01_vezdessushij
    a emo-20 "Сразу? Без всяких прелюдий?"
    m emo-6 "А они тебе нужны?"
    a emo-22 "Нет. Я давно возбуждена, моя киска готова к проникновению."
label pgn_events_11_alicecam_webshow_nd_next:
    scene animated pgn_11_bdsmroom_webshow_nd_02
    $ renpy.pause()
    if alice_path == 17:
        a emo-30 "[pname_max[0]]. Я забыла принять таблетки, только не кончай внутрь."
        m emo-3 "Это даже лучше."
        a emo-32 "Нет. Не смей. Я не хочу забеременеть."
        m emo-4 "Расслабься, всё будет нормально."
        a emo-32 "[pname_max[0]]! Нет, нет... Аааххх..."
        scene pgn_11_bdsmroom_webshow_nd_02_03
        m emo-10 "Аргх... Аааа... О да..."
        scene pgn_11_bdsmroom_webshow_nd_03_vezdessushij
        a emo-29 "Выпусти меня и так отхватишь от меня, что запомнишь навсегда."
        a emo-32 "Ты куда?"
        m emo-0 "Я за планшетом, хочу показать крупным планом."
        scene pgn_11_bdsmroom_webshow_nd_04_vezdessushij
        a emo-26 "[pname_max[0]]. Отпусти меня, мне нужно срочно в ванную."
        scene pgn_11_bdsmroom_webshow_nd_05
        $ renpy.pause()
        a emo-28 "Пожалуйста. Хватит.... Я..."
        scene pgn_11_bdsmroom_webshow_nd_06_vezdessushij
        a emo-34 "Аааааахххх...."
        scene pgn_11_bdsmroom_webshow_nd_07_vezdessushij
        a emo-30 "Аааа.... Ммммм... Ааахххх...."
    else:
        a emo-24 "Ой! [pname_max[0]]. Я опять забыла принять таблетки."
        m emo-0 "Ну и ладно. С прошлого раза ведь не забеременела?"
        a emo-22 "Хорошо. Продолжай трахать меня..."
        scene animated pgn_11_bdsmroom_webshow_nd_02
        $ renpy.pause()
        scene pgn_11_bdsmroom_webshow_nd_02_03
        m emo-10 "Аргх... Аааа... О да..."
        scene pgn_11_bdsmroom_webshow_nd_04_vezdessushij
        m emo-16 "Сестрёнка, ты суперски красивая и сексуальная."
        a emo-25 "Знаю, но спасибо. А теперь..."
        m emo-4 "Нет, нет. Не отпущу, пока ты не кончишь."
        a emo-26 "Ну [pname_max[0]]!"
        scene pgn_11_bdsmroom_webshow_nd_05
        $ renpy.pause()
        a emo-28 "Ох Боже... Ох Божечки... Ах, аххх... Я..."
        scene pgn_11_bdsmroom_webshow_nd_06_vezdessushij
        a emo-34 "Аааааахххх...."
        scene pgn_11_bdsmroom_webshow_nd_07_vezdessushij
        a emo-30 "Аааа.... Ммммм... Ааахххх...."
    scene pgn_11_bdsmroom_webshow_nd_08_vezdessushij
    a emo-26 "[pname_max[0]]! Отпусти меня, я.. больше не могу и ноги затекли."
    menu:
        "Отпустить":
            scene pgn_11_bdsmroom_webshow_nd_11_vezdessushij
            m emo-0 "Хорошо, хорошо, я отпустил. Хотя могла бы получить ещё больше ощущений."
            a emo-29 "Нет [pname_max[0]], моя киска больше бы не выдержала."
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random == 3:
                a emo-20 "И готовь свою попу. Вечером я тебя, а и заодно, за компанию, [pname_liza[3]], накажу."
                m emo-2 "Но я же как лучше хотел."
                a emo-28 "Да, да. Оставь меня."
        "Продолжить":
            scene pgn_11_bdsmroom_webshow_nd_05
            a emo-26 "[pname_max[0]]! Остановись!"
            scene pgn_11_bdsmroom_webshow_nd_09_vezdessushij
            a emo-30 "Ааахх..."
            scene pgn_11_bdsmroom_webshow_nd_10_vezdessushij
            $ PGN_Achadd(pgnach_133, 133)
            a emo-24 "Беру свои слова обратно. Это было потрясающе. Я уже думала, как тебя наказать."
            m emo-13 "Тебе как-нибудь помочь?"
            a emo-28 "Я посижу пока тут ещё немного и в душ. Больше меня ни на что не хватит. Как там с... со зрителями?"
            m emo-4 "Зрелище им очень понравилось."
            a emo-22 "Спасибо."
    if pgn_ach_repeat == 133:
        jump table_pgn_achievement
    if pgn_ach_repeat == 0:
        $ PGN_Addstatsex(stat_alice, 0, 0, 0, 1, 0)
    if alice_path == 17:
        $ alice_path = 18
    scene pgn_11_bdsmroom_webshow_02_vezdessushij
    $ renpy.pause(5, hard=True)
    scene black with fade
    m emo-7 "{i}Утренний стояк. Я и он готов к сексу.{/i}"
    m emo-3 "[pname_alice[0]]! Как насчёт..."
    scene pgn_11_bdsmroom_webshow_03_vezdessushij with fade
    m emo-2 "Её нет."
    m emo-1 "[pname_alice[0]]!"
    m emo-1 "…"
    m emo-2 "Вот блин, уже уехала, а меня не разбудила."
    call next_time_days from _call_next_time_days_3
    call max_sleep_reset from _call_max_sleep_reset_5
    $ qtime = 8
    jump loc_hotel_aptkira_bedroom




label pgn_events_11_alicecam_10:
    m emo-3 "У меня есть кое-что для тебя."
    a emo-20 "И что это?"
    m emo-4 "Я просто это оставлю, потом сама посмотришь."
    python:
        for i in pink_unicorn:
            if i.buy == True and i.have == True:
                i.have = False
                accessiv.append("секс-игрушка_у_алисы")
    if (sexitem_vibroedge1.buy == True and sexitem_vibroedge1.instore == False and sexitem_vibroedge1.have == False and sexitem_vibroedge1.dostavka == 0) and (sexitem_analdildo1.buy == True and sexitem_analdildo1.instore == False and sexitem_analdildo1.have == False and sexitem_analdildo1.dostavka == 0) and (sexitem_cowgirl1.buy == True and sexitem_cowgirl1.instore == False and sexitem_cowgirl1.have == False and sexitem_cowgirl1.dostavka == 0):
        $ accessiv.append("камшоу_алиса_011_все_игрушки")
    jump jump_dialogue

label pgn_events_11_alicecam_homecam2:
    $ ivent24.append("камшоу_алисы")
    scene pgn_11_aliceroom_camshow_01
    a emo-21 "[pname_max[0]], может лучше придёшь ко мне и поможешь сестрёнке?"
    menu:
        "Хочу приватное шоу":
            m emo-3 "Не, я именно посмотреть на тебя."
        "Ладно, сейчас приду":
            $ ivent24.remove("камшоу_алисы")
            jump alice_room_blog
    if ("секс-игрушка_у_алисы") in accessiv and ("камшоу_алиса_011_все_игрушки") not in accessiv:
        $ accessiv.remove("секс-игрушка_у_алисы")
        m emo-0 "Получила мой подарок?"
        scene pgn_11_aliceroom_camshow_02
        a emo-20 "Да. Сейчас его найду."
        if sexitem_vibroedge1.buy == True and ("алиса_сексигрушка1") not in accessiv:
            jump pgn_events_11_alicecam_homecam_vibroedge1
        elif sexitem_analdildo1.buy == True and ("алиса_сексигрушка2") not in accessiv:
            jump pgn_events_11_alicecam_homecam_analdildo1
        elif sexitem_cowgirl1.buy == True and ("алиса_сексигрушка3") not in accessiv:
            jump pgn_events_11_alicecam_homecam_cowgirl1
    else:
        scene pgn_11_aliceroom_camshow_02
        a emo-20 "Тогда что мне выбрать?"
        menu:
            "Виброяйцо" if sexitem_vibroedge1.buy == True and sexitem_vibroedge1.instore == False and sexitem_vibroedge1.have == False and sexitem_vibroedge1.dostavka == 0:
                jump pgn_events_11_alicecam_homecam_vibroedge1
            "Анальная цепочка" if sexitem_analdildo1.buy == True and sexitem_analdildo1.instore == False and sexitem_analdildo1.have == False and sexitem_analdildo1.dostavka == 0:
                jump pgn_events_11_alicecam_homecam_analdildo1
            "Секс-машина Cowgirl" if sexitem_cowgirl1.buy == True and sexitem_cowgirl1.instore == False and sexitem_cowgirl1.have == False and sexitem_cowgirl1.dostavka == 0:
                jump pgn_events_11_alicecam_homecam_cowgirl1


label pgn_events_11_alicecam_homecam2_bill:
    $ label_random = renpy.random.randint ( 100, 400)
    a emo-21 "С тебя $[label_random]"
    menu:
        "С чего это?":
            m emo-11 "Почему я должен платить? Я тебе подарок на свои деньги покупал."
            a emo-20 "Вместо того, чтобы немного заработать, я потратила время на тебя."
            a emo-21 "И ты сам говоришь, что это подарок, так что ничего тебе и не должна."
            m emo-11 "{i}Блин{/i}"
        "Заплатить":
            pass
    $ currency -= label_random
    $ bill_alicecam += label_random
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
