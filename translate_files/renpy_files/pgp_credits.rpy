label pgn_credits_13_lastupdate:
    scene pgn_credits_01
    other emo-999 "Мхмм... ммммм.... Мххмм..."
    scene pgn_credits_02
    other emo-998 "У меня недавно был сумасшедший секс с одной горячей рыжей красоткой."
    other emo-998 "Я её знаю?"
    other emo-998 "Должна знать. Я тебя просила несколько раз свести меня с ней."
    other emo-998 "Сестрёнка, я пробовала с ней поговорить, но она такая занятая. А как это у тебя получилось?"
    scene pgn_credits_01
    other emo-998 "По работе, познакомилась с парнишкой, он мне всё устроил."
    other emo-998 "Кажется я догадываюсь, кто это был."
    scene pgn_credits_03
    mi emo-283 "Как поживает мой щеночек? Соскучился?"
    scene pgn_credits_04
    other emo-999 "Мхмм... ммммм.... Мххмм..."
    scene pgn_credits_05
    other emo-998 "Грхл... Ммхх... Ммм..."
    scene pgn_credits_06
    $ renpy.pause()
    scene pgn_credits_07
    other emo-998 "Грхл... Ммхх... Ммм..."
    other emo-999 "Заглатывай!!!"
    scene pgn_credits_08
    other emo-999 "Аааа... Аааргх..."
    scene pgn_credits_09
    other emo-998 "Я... Я чуть не задохнулось..."
    other emo-999 "Иди в душ."
    scene pgn_credits_10
    $ renpy.pause()
    scene pgn_credits_11
    $ renpy.pause()
    scene pgn_credits_12
    other emo-998 "Ааай! Ну хватит! Отдай и я пойду!"
    scene pgn_credits_13
    other emo-999 "Может лучше останешься и повторим?"
    other emo-998 "Мы и так всю ночь, у меня всё болит. В другой раз."
    other emo-999 "Ладно. Проваливай."
    scene pgn_credits_14
    $ renpy.pause()
    scene pgn_credits_15
    other emo-999 "Посмотрим, что нового появилось за это время."
    scene pgn_credits_14
    $ renpy.pause()
    scene pgn_credits_15
    show pgn_credits_15_01
    other emo-999 "Это горячая милашка слева мне кого-то напоминает. "
    scene pgn_credits_14
    other emo-999 "Эта попка..."
    other emo-999 "Не может быть!"
    scene pgn_credits_16
    other emo-999 "[pname_mom[7]]! А эта малышка получается, [pname_alice[0]]?!"
    other emo-999 "Долго меня не было в городе."
    other emo-999 "Стоит к ним наведаться."
    scene black with dissolve
    $ renpy.pause(3)
    scene pgn_school_et2_out_library_1_vadx
    call screen pgn_credits_13_lastupdate_01
label pgn_credits_13_lastupdate_nxt1:
    scene pgn_credits_23
    pgn "Спасибо вам, за то что играли в эту игру."
    scene pgn_credits_18
    $ renpy.pause(1)
    pgn "Спасибо тем, кто помогал с рендерингом, даже если всего 1 картинку. Но сколько бы не было сделано, это всё же очень много сэкономленного времени и благодаря вам, у меня была возможность делать эту игру. Без вас, всё бы закончилось на 6-м обновлении."
    scene pgn_credits_18
    call screen pgn_credits_13_lastupdate_02
label pgn_credits_13_lastupdate_nxt2:
    scene pgn_credits_20a at up_t(0.7)
    $ renpy.pause(0.65)
    scene pgn_credits_20b at up_t(0.3) with dissolve
    $ renpy.pause(0.3)
    scene pgn_credits_21 with dissolve
    $ renpy.pause(0.5)
    pgn "Спасибо всем тем, кто материально поддерживал, и благодаря вам я смог купить 25 апреля 2019г новую видеокарту GTX 1070 Palit. И уже на ней я мог рендерить изображения, а не процессором."
    scene pgn_credits_22 at down_t(10)
    $ renpy.pause()
    jump jump_dialogue


screen pgn_credits_13_lastupdate_01:
    add "credits_bg"
    button:
        align (0.5, 0.5)
        minimum (900, 1080)
        xmaximum 900
        has vbox:
            align (0.5,0.5)
        text _("{size=+40}Спасибо...{/size}") xalign 0.5

    button:
        align (0.05, 0.9)
        xmaximum 350
        padding (30,10)
        has vbox
        button xalign 0.5:
            ymaximum 3
            background "#f29114"
        hbox:
            xalign 0.5
            textbutton _("Вернуться\n в локацию") action Jump("jump_dialogue")
        button xalign 0.5:
            ymaximum 3
            background "#f29114"
    button:
        align (0.95, 0.9)
        xmaximum 350
        padding (30,10)
        has vbox
        button xalign 0.5:
            ymaximum 3
            background "#f29114"
        hbox:
            xalign 0.5
            textbutton _("Далее") action Jump("pgn_credits_13_lastupdate_nxt1")
        button xalign 0.5:
            ymaximum 3
            background "#f29114"


screen pgn_credits_13_lastupdate_02:
    add "credits_bg"
    button:
        align (0.5, 0.5)
        minimum (900, 1080)
        xmaximum 900
        has vbox:
            xsize 850
            align (0.5,0.3)
        text _("Никнейм (Номер Обновления):\n- Alex666 (0.06 - 0.08)\n- Vezdessushij (0.07 - 0.13)\n- VaDX (0.08 - 0.13)\n- Petruha (0.09 - 0.10)\n- Romanich (0.08)\n- goty (0.08)\n- I'm from the village (0.08, 0.13)\n- Arata111 (0.10)\n- zicado (0.12)\n- AsanoSakura (0.13)\n- dj0101 (0.13)") xalign 0.5 yalign 0.5

    button:
        align (0.05, 0.9)
        xmaximum 350
        padding (30,10)
        has vbox
        button xalign 0.5:
            ymaximum 3
            background "#f29114"
        hbox:
            xalign 0.5
            textbutton _("Вернуться\n в локацию") action Jump("jump_dialogue")
        button xalign 0.5:
            ymaximum 3
            background "#f29114"
    button:
        align (0.95, 0.9)
        xmaximum 350
        padding (30,10)
        has vbox
        button xalign 0.5:
            ymaximum 3
            background "#f29114"
        hbox:
            xalign 0.5
            textbutton _("Далее") action Jump("pgn_credits_13_lastupdate_nxt2")
        button xalign 0.5:
            ymaximum 3
            background "#f29114"


transform up_t(t):
    yalign 1.0
    linear t yalign 0.0


transform down_t(t):
    yalign 0.0
    linear t yalign 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
