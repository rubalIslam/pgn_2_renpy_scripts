






label pgn_newolivhome_01:
    $ olivia_path = 1
    if ("CityShop") not in accessiv:
        $ accessiv.append("CityShop")
    scene bg pgn_newolivhome_01_01
    m emo-5 "{i}Фух... Это было классно. Если бы не её уроки, так бы до самого вечера с ней...{/i}"
    scene bg pgn_newolivhome_01_02
    ol emo-141 "Ой! [pname_max[0]]! Привет."
    m emo-4 "Привет."
    ol emo-141 "А что это ты из женского туалета выходишь, ошибся дверью?"
    m emo-9 "Да... да, ошибся. Так спешил, что не заметил."
    ol emo-142 "Аааа... ясно."
    ol emo-143 "Только я вот только что видела [pname_liza[3]], такая довольная..."
    m emo-8 "Эм.. Ну... Скрывать нечего, кажется ты и так поняла. Если хочешь, у меня ещё есть силы на тебя."
    ol emo-140 "Нет, спасибо. Я бы с радостью с тобой занялась сексом, только не в туалете."
    m emo-6 "Но, а как же в ТРЦ?"
    ol emo-147 "Ну там... больше негде... и награда ждать себя не заставит. Так что в качестве исключения."
    ol emo-147 "Я не могу заниматься сексом где угодно, в общественном туалете можно же ещё что-то подцепить."
    m emo-3 "Как у тебя дела?"
    ol emo-144 "Ты меня извини, но мне в туалет нужно, если хочешь поговорить, подожди меня."
    m emo-0 "Ладно"
    scene bg school_corridor2_liza_01
    $ renpy.pause(3, hard=True)
    scene bg pgn_newolivhome_01_03
    m emo-0 "Как у вас в общем дела?"
    ol emo-146 "Ох... ну..."
    m emo-0 "Рассказывай, ты моя девушка, и можешь рассказать, а если что, найду способ как помочь."
    ol emo-140 "Помнишь, где мы живём, тот дом?"
    m emo-0 "Да, тот что разделен по пополам на две семьи."
    ol emo-140 "Так вот, подняли арендную плату, и мама больше не может платить репетитору за мои занятия."
    m emo-0 "Может, как раньше, я буду с тобой заниматься?"
    ol emo-146 "Она всё ещё против того, чтобы ты к нам приходил."
    m emo-0 "Понятно, жаль. А может вам переехать в другую квартиру, где подешевле?"
    ol emo-146 "Мы с мамой искали, но или дорого, или слишком далеко от школы и от маминой работы."
    m emo-3 "Оливия, не переживай, я что-нибудь придумаю, как вам помочь."
    ol emo-142 "Спасибо тебе, Макс."
    m emo-3 "Да пока не за что, беги на урок."
    ol emo-142 "Пока."
    jump loc_school_et1_out_tg


label pgn_newolivhome_02:
    $ screenhide()
    scene chat_agent
    $ olivia_path = 2
    m emo-0 "Да. Я ищу квартиру для съёма."
    other emo-998 "В каком районе желаете?"
    m emo-0 "Точно не знаю, главное, чтобы не слишком далеко от школы и по приемлемой цене."
    other emo-998 "Хм... есть у меня одна квартира на примете. Думаю, она вам подойдёт."
    other emo-998 "Как насчёт того, чтобы встретиться завтра в городе?"
    m emo-0 "Ок. А где именно?"
    other emo-998 "Знаете, в районе школы есть одно Кафе?"
    m emo-0 "Да. Бываю там иногда."
    other emo-998 "Хорошо, тогда встретимся в 15:00 и я проведу вам осмотр."
    if sms_miranda.contact == False:
        other emo-998 "И вот вам мой номер для контакта."
        play sound "content/audio/long_expected.mp3" noloop
        $ renpy.notify(str(task_notifi[2])+": "+str(varlang[13]))
        $ renpy.pause ( 5, 0)
        $ sms_miranda.contact = True
    $ days_miranda = days + 1
    $ olivia_path = 2

    jump pgn_comp_site_cityshop_realty


label pgn_newolivhome_03:
    scene bg pgn_olivhome_new_tour_01
    $ renpy.pause(3, 0)
    scene bg pgn_olivhome_new_tour_02
    v emo-170 "Привет, [pname_max[0]]! Не хочешь заказать чего-нибудь?"
    menu:
        "Кофе":
            $ ivent24.append("newolivhome_tour_cofe")
            play sound "content/audio/long_expected.mp3" noloop
            $ renpy.notify(str(task_notifi[11])+" $"+"10")
            $ currency -= 10
        "Ничего":
            m emo-0 "Спасибо. Я ничего не буду."
            pass
    v emo-161 "А чего сегодня один и без сестры?"
    m emo-0 "Я кое-кого жду."
    if vicky_path >= 10:
        v emo-169 "Девушку?"
        m emo-5 "А... эм... нет. Я жду агента по недвижимости."
        v emo-170 "Подыскиваешь себе квартиру, решил стать взрослым и жить отдельно? Если хочешь, можешь пожить со мной."
        m emo-3 "Спасибо, но нет. Меня друг попросил помочь ему с поисками нового жилья."
        v emo-164 "А, ясно."
    v emo-172 "Если понадобится ещё кофе, зови."
    m emo-3 "Хорошо."
    scene bg pgn_olivhome_new_tour_01
    if ("newolivhome_tour_cofe") in ivent24:
        scene bg pgn_olivhome_new_tour_01b
    $ renpy.pause(3, hard=True)
    scene bg pgn_olivhome_new_tour_03
    if ("newolivhome_tour_cofe") in ivent24:
        scene bg pgn_olivhome_new_tour_03b
    mi emo-281 "Здравствуйте. Я полагаю, вы [pname_max[0]]?"
    m emo-3 "Да, это я."
    scene bg pgn_olivhome_new_tour_04
    if ("newolivhome_tour_cofe") in ivent24:
        scene bg pgn_olivhome_new_tour_04b
    m emo-0 "Будете кофе, вам заказать?"
    mi emo-281 "О нет, спасибо."
    mi emo-282 "Хм..."
    m emo-8 "Что такое, что не так с моим лицом?"
    mi emo-282 "Вы мне кажитесь знакомым и вроде где-то видела, но не могу вспомнить..."
    m emo-13 "Может вам показалось!?"
    mi emo-283 "Ох, вспомнила! Вы то самый, [pname_max[0]]. с большим и здоровенным... Ой! Забыла, что мы в общественном месте."
    m emo-13 "Видимо да, это я."
    mi emo-281 "Вы готовы, можем идти?"
    m emo-1 "А далеко идти?"
    mi emo-280 "Близко, можем пройтись пешком."
    m emo-0 "Хорошо."
    scene bg pgn_olivhome_new_tour_05
    mi emo-281 "Вот мы и пришли."
    scene bg pgn_olivhome_new_tour_06
    $ renpy.pause (3, 0)
    scene bg pgn_olivhome_new_tour_07
    mi emo-281 "Проходите, я покажу вам весь дом."
    m emo-6 "{i}Дом!? Да я вроде говорил про квартиру. Наверное очень дорого будет стоить.{/i}"
    m emo-13 "{i}Эта дамочка, Миранда. Видно, внешне, что увлекается фитнесом, да и не только, вся такая накаченная... А если она не Миранда, вовсе... страшновато заходить в такой дом. Но я здесь ради Оливии.{/i}"
    scene bg pgn_olivhome_new_tour_08
    mi emo-280 "В конце этого коридора дверь, ведущая на цокольный этаж или же подвал. Через цокольный этаж можно попасть на задний двор."
    mi emo-280 "Давайте сначала покажу тут вам всё, а уже потом в конце можно выйти на задний двор."
    scene bg pgn_olivhome_new_tour_09
    mi emo-280 "Здесь можно расположить столовую, кухню. Хозяин квартиры сам не готовит, поэтому здесь нет ни какой мебели, даже кухонной гарнитуры."
    m emo-0 "А мебель хоть какая-то есть в доме?"
    mi emo-280 "Да, в некоторых помещениях она имеется. Теперь поднимемся на второй этаж."
    scene bg pgn_olivhome_new_tour_10
    mi emo-280 "Будьте осторожны и держитесь за поручень."
    m emo-13 "{i}Я бы подержался за её большую попку. Но ни как не могу выкинуть мысль из головы, что вдруг она не женщина вовсе и врезать может очень сильно.{/i}"
    scene bg pgn_olivhome_new_tour_11
    mi emo-280 "Это спальня. Как видите из мебели имеется: кровать, тумбочки, с каждой стороны и справа гардеробный шкаф."
    m emo-0 "{i}Кажется это женская комната. Только она говорила, что здесь живёт или жил хозяин, а не хозяйка. Может это её дом?{/i}"
    scene bg pgn_olivhome_new_tour_12
    mi emo-280 "Просторная гостиная..."
    m emo-6 "Без телевизора."
    mi emo-280 "Эм... да, без телевизора. Хозяин дома редко что-то смотрит, у него очень мало времени, очень занятой человек."
    mi emo-280 "Так же имеется барная стойка. Выпивка бесплатна, в арендную плату не входит."
    mi emo-280 "Хорошо. Посмотрим, что тут у нас на последнем этаже."
    scene bg pgn_olivhome_new_tour_13
    m emo-6 "{i}Хм... две душевые стойки? И место очень много, есть где развернуться.{/i}"
    scene bg pgn_olivhome_new_tour_14
    m emo-0 "А тут была детская?"
    mi emo-281 "Ну, да, можно эту комнату переделать в детскую... У вас есть дети?"
    m emo-5 "А... нет, нет. Просто ассоциация с двуярусной кроватью. И комната очень большая, только какая-то пустая."
    mi emo-283 "Они двуспальные, так что тут могут уместиться 4 человека или может даже больше."
    mi emo-280 "Теперь посмотрим задний двор?"
    m emo-0 "Да, конечно."
    scene bg pgn_olivhome_new_tour_15
    m emo-6 "{i}Хм... а бассейна нет.{/i}"
    scene bg pgn_olivhome_new_tour_16
    mi emo-281 "И так, вы ищите себе апартаменты для проживания или для вечеринок? Такому актёру, как вы, могу предложить вариант получше."
    m emo-0 "{i}Вариант получше!? Наверное будет стоить ещё дороже.{/i}"
    m emo-0 "Нет. Я просто хочу помочь знакомой."
    mi emo-283 "А, своей тайной девушке или любовнице?"
    m emo-2 "Эм..."
    mi emo-281 "Хорошо, не буду давить. Перейдём к цене. Арендная плата в месяц составляет $5000."
    m emo-9 "{i}Ого! Как много. Мы за свой дом платим $4000, но у нас территория больше и бассейн. Хотя у нас свой дом, а не чужой.{/i}"
    m emo-3 "А скидку можно?"
    mi emo-282 "Хм... думаю смогу уговорить владельца на скидку, может даже большую. Но конечно не за просто так."
    m emo-4 "Я готов на всё что угодно, хоть прям сейчас."
    mi emo-281 "Нет, нет, стоп. Я конечно не против когда-нибудь посмотреть на ваш инструмент по ближе, но меня интересует другая особа."
    mi emo-283 "Ходят слухи, что вы очень хорошо знакомы и даже больше, с режиссером и сценаристом этих фильмов, в которых вы снимаетесь."
    m emo-13 "Ах, да, я её знаю.\n{i}Откуда эти слухи пошли, ну было один раз, минет она мне сделала в одном фильме.{/i}"
    mi emo-281 "Очень хотела бы с ней встретиться, лично. Можете устроить?"
    m emo-0 "Попробую с ней поговорить."
    mi emo-281 "Договорились. Но знайте, предложение ограничено, максимум 2 недели могу подождать, а после ни о какой скидке идти речи и не может быть."
    m emo-0 "Понял. Спасибо."
    $ days_miranda = days + 15
    $ olivia_path = 3
label pgn_newolivhome_03b:
    scene bg pgn_olivhome_new_tour_06
    $ location = []
    $ location.append("loc_olivhomenew")
    call screen loc_olivhomenew


label pgn_newolivhome_04a:
    k emo-102 "Ой, кто тут у нас, [pname_max[0]]! Снова что-то от любимой тёти нужно."
    m emo-13 "Да, так и есть."
    k emo-102 "Для любимого племянника, что угодно."
    m emo-0 "В общем, у моей знакомой проблемы с жильём и я предложил свою помощь."
    k emo-100 "Не думаю, что мама позволит кого-то приютить."
    m emo-0 "Нет, я не об этом."
    m emo-0 "Так вот, я нашёл подходящее жильё, близко находится к школе и т.д., но оно слишком дорого стоит."
    k emo-100 "Эм... в долг дать деньги не с могу, я как только получаю, сразу трачу."
    m emo-0 "..."
    k emo-104 "Снова мимо? Хорошо, продолжай."
    m emo-0 "Агент по недвижимости готов предоставить скидку, но попросили встречи с тобой. Что-то вроде свидания."
    k emo-108 "А он красивый, этот агент?"
    m emo-0 "Это женщина и да, красивая, вроде. И о на узнала меня, по нашим... фильмам."
    k emo-104 "Хм, раз узнала, странно что не пригласила тебя."
    m emo-0 "Ты пойдёшь, с ней?"
    if pornfilm_g < 15:
        k emo-100 "Даже и не знаю, я её даже не видела в лицо, но даже если ты говоришь, что она красивая, то поверю на слово. Но, что мне с этого будет?"
        m emo-0 "Всё что захочешь, я сделаю."
        k emo-104 "Я соглашусь, если ты выучишь отлично все сценарии фильмов и снимешься без единой ошибки. Тогда помогу. А пока нет."
        m emo-13 "Но у меня не так много времени есть, потом ни какой скидки не будет."
        k emo-105 "Я сказала, нет. Или съёмки в фильмах или ни как."
        $ olivia_path = 3.1
    if pornfilm_g >= 15:
        k emo-100 "Хорошо, я с ней встречусь."
        m emo-0 "Вот её контакт. Спасибо тебе огромное."
        $ olivia_path = 4
        $ days_kira = days + 1
    jump jump_dialogue

label pgn_newolivhome_04b:
    m emo-0 "Я выполнил твоё условие?"
    k emo-104 "Какое условие?"
    m emo-0 "Ну, чтобы ты сходила на свидание с Мирандой."
    k emo-102 "Ах да, точно, уже и забыла. Хорошо, я с ней встречусь."
    m emo-0 "Вот её контакт. Заранее, спасибо тебе огромное."
    $ olivia_path = 4
    $ days_kira = days + 1
    jump jump_dialogue

label pgn_newolivhome_04c:
    hide screen sms_kira_menu

    "{#l=Снова что-то от любимой тёти нужно.}"
    "{#r=Да, так и есть.}"
    "{#l=Для любимого племянника, что угодно.}"
    "{#r=В общем, у моей знакомой проблемы с жильём и...}"
    "{#l=Хочешь попросить маму разрешения пожить здесь?}"
    "{#r=Нет, я не об этом.}"
    "{#r=Так вот, я нашёл подходящее жильё, но оно дорого стоит.}"
    "{#l=Денег у меня нет.}"
    "{#r=...}"
    "{#l=Хорошо, продолжай.}"
    "{#r=Агент по недвижимости готов предоставить скидку, но попросили встречи с тобой. Что-то вроде свидания.}"
    "{#l=А он красивый, этот агент?}"
    "{#r=Это женщина и да, красивая, вроде.}"
    "{#r=Ты пойдёшь, с ней?}"
    if pornfilm_g < 15:
        "{#l=Даже и не знаю. Но, что мне с этого будет?}"
        "{#r=Всё что захочешь, я сделаю.}"
        "{#l=Я соглашусь, если ты снимаешься несколько раз в фильмах.}"
        "{#r=Легко}"
        "{#l=Легко!? Хорошо, только не забудь текст выучить наизусть.}"
        "{#r=Но у меня не так много времени есть.}"
        "{#l=Выполнишь моё условия, тогда поговорим.}"
        $ olivia_path = 3.1
    if pornfilm_g >= 15:
        "{#l=Хорошо, я с ней встречусь.}"
        "{#r=Контакт отправлен}"
        "{#r=Вот её контакт. Спасибо тебе огромное.}"
        $ olivia_path = 4
        $ days_kira = days + 1

    jump phone_max

label pgn_newolivhome_04d:
    hide screen sms_kira_menu
    "{#r=Я выполнил твоё условие?}"
    "{#l=Какое условие?}"
    "{#r=Ну, чтобы ты сходила на свидание с Мирандой.}"
    "{#l=Ах да, точно, уже и забыла. Хорошо, я с ней встречусь.}"
    "{#r=Вот её контакт. Заранее, спасибо тебе огромное.}"
    "{#r=Контакт отправлен}"
    $ olivia_path = 4
    $ days_kira = days + 1
    jump phone_max


label pgn_newolivhome_datevideo01:
    hide screen sms_miranda_menu
    $ sms_miranda.sms_missed_text = []
    $ sms_miranda.sms_missed = 0
    $ ivent24.append("pgn_newolivhome_datevideo01")
    if renpy.variant("pc"):
        scene animated pgn_olivhome_video1_pc
        $ renpy.pause()
    if renpy.variant("small") or renpy.variant("touch"):
        scene animated pgn_olivhome_video1_a
        call screen pgn_newolivhome_datevideo_a
    jump phone_max

label pgn_newolivhome_datevideo02:
    hide screen sms_miranda_menu
    $ sms_miranda.sms_missed_text = []
    $ sms_miranda.sms_missed = 0
    $ ivent24.append("pgn_newolivhome_datevideo02")
    if renpy.variant("pc"):
        scene animated pgn_olivhome_video2_pc
        $ renpy.pause()
    if renpy.variant("small") or renpy.variant("touch"):
        scene animated pgn_olivhome_video2_a
        call screen pgn_newolivhome_datevideo_a
    jump phone_max

label pgn_newolivhome_datevideo03:
    hide screen sms_miranda_menu
    $ sms_miranda.sms_missed_text = []
    $ sms_miranda.sms_missed = 0
    $ ivent24.append("pgn_newolivhome_datevideo03")
    if renpy.variant("pc"):
        scene animated pgn_olivhome_video3_pc
        $ renpy.pause()
    if renpy.variant("small") or renpy.variant("touch"):
        scene animated pgn_olivhome_video3_a
        call screen pgn_newolivhome_datevideo_a
    jump phone_max

screen pgn_newolivhome_datevideo_a:
    imagebutton idle "nav_phone_h_close_a" hover "nav_phone_h_close_b" action Jump ("phone_max") xalign 1.0


label pgn_newolivhome_05a:
    scene bg pgn_olivhome_afterdate_01
    m emo-3 "{i}О! Тётя [pname_kira[0]] пришла с свидания. Пойду узнаю у неё.{/i}"
    scene bg pgn_olivhome_afterdate_02
    m emo-3 "Привет. А чего в дом не заходишь?"
    k emo-107 "Я так устала, что еле дошла от такси и до сюда."
    m emo-5 "Могу помочь дойти или может даже донести."
    k emo-108 "Ручки не отвалятся? Спасибо, племянник, но я тут ещё немного полежу и сама дойду, не переживай."
    m emo-3 "Как прошло свидание?"
    k emo-109 "Мы с ней так долго разговаривали, и оказывается у нас так много общих интересов. Так наговорилась, что челюсть побаливает."
    if ("pgn_newolivhome_datevideo01") in ivent24:
        m emo-4 "{i}Я знаю, как она много ртом работала. Но думаю, что лучше не говорить ей пока об этом, что у меня есть видео.{/i}"
    m emo-0 "Она, что-нибудь сказала?"
    k emo-107 "Да. Пригласила меня ещё на свидание."
    m emo-3 "Потом мне расскажешь как прошло?"
    k emo-107 "Да, да. Дай тёте ешё немного отдохнуть, а сам иди спать."
    m emo-3 "Хорошо, тогда оставлю тебя. Спокойной ночи."
    $ accessiv.append("kira_afterdate_1")
    $ serialpgngame("loc_my_room_sleep")

label pgn_newolivhome_05b:
    m emo-3 "Как прошло свидание?"
    k emo-109 "Мы с ней так долго разговаривали, и оказывается у нас так много общих интересов. Так наговорилась, что челюсть побаливает."
    if ("pgn_newolivhome_datevideo01") in ivent24:
        m emo-4 "{i}Я знаю, как она много ртом работала. Но думаю, что лучше не говорить ей пока об этом, что у меня есть видео.{/i}"
    m emo-0 "Она, что-нибудь сказала?"
    k emo-101 "Да. Пригласила меня ещё на свидание."
    m emo-3 "Потом мне расскажешь как прошло?"
    k emo-101 "Если тебе так интересно, то расскажу."
    m emo-3 "Хорошо, тогда оставлю тебя."
    $ accessiv.append("kira_afterdate_1")
    jump jump_dialogue


label pgn_newolivhome_06a:
    scene bg pgn_olivhome_afterdate_03
    k emo-109 "Не спится?"
    m emo-0 "Решил тебя проведать, узнать как дела."
    k emo-107 "Хорошо, сейчас... очень хорошо. Тёплая вода... расслабляет."
    if ("pgn_newolivhome_datevideo02") in ivent24:
        m emo-4 "{i}Наверное пока она тут лежала, её горячая киска подогрела холодную ванну.{/i}"
    k emo-107 "Что-то ещё? Если хочешь секса, то извини, не могу... очень устала и нет сил. Завтра у нас будет ещё одно свидание."
    m emo-0 "Понял. Оставлю тебя. Спокойно ночи."
    $ accessiv.append("kira_afterdate_2")
    $ serialpgngame("loc_my_room_sleep")

label pgn_newolivhome_06b:
    m emo-3 "Как прошло свидание?"
    k emo-113 "Ой, знаешь, хорошо. С удовольствием пойду с ней ещё на одно. Миранда предложила сходить в одно место."
    m emo-3 "Ясно."
    if ("pgn_newolivhome_datevideo02") in ivent24:
        m emo-4 "{i}Оральный секс был, вагинальный тоже, остался третий.{/i}"
    $ accessiv.append("kira_afterdate_2")
    jump jump_dialogue


label pgn_newolivhome_07a:
    scene bg pgn_olivhome_afterdate_04
    if ("pgn_newolivhome_datevideo03") in ivent24:
        m emo-4 "{i}Ого! Тётя лежит попкой к верху, сесть не может. Бедная и сексуальная попка тёти.{/i}"
    k emo-107 "Кто там сзади так незаметно подкрался?"
    m emo-0 "Это я."
    k emo-107 "Что стоишь, присаживайся."
    scene bg pgn_olivhome_afterdate_05
    m emo-1 "..."
    k emo-100 "..."
    m emo-0 "Ну, как?"
    k emo-100 "Как, что?"
    m emo-0 "Как прошло ваше свидание?"
    k emo-100 "Сходили вместе в ресторан, поужинали. Потом прогулялись по пляжу."
    m emo-0 "..."
    m emo-0 "Тебе удобно, так лежать?"
    k emo-111 "Сесть не могу, попа болит."
    m emo-0 "А что случилось?"
    k emo-111 "Поскользнулась и упала, вот и болит."
    m emo-3 "Я маме после съёмок массаж делаю, ей помогает. Если хочешь, могу тебе массаж попы сделать."
    k emo-100 "Нет, спасибо. Извини, но мне сейчас не до этого. Может пойдёшь спать?"
    m emo-2 "Мне кажется, что я не смогу уснуть."
    scene bg pgn_olivhome_afterdate_06
    k emo-112 "Ох! [pname_max[0]]!"
    m emo-2 "Я понимаю, что ты у стала, но может поможешь?"
    k emo-103 "Хм... Всё что могу предложить, это подрочить на меня."
    $ menu_hbox = False
    menu:
        "Синдром":
            m emo-2 "Но у меня же туннельный синдром?"
            k emo-104 "Маме будешь об этом напоминать. А ты сам знаешь, что мы эту болезнь вместе придумали."
            k emo-104 "Или дрочишь или сам ищи способ, как снять напряжение."
        "Продолжить":
            pass
    $ anim_speed = 0.3
    scene animated pgn_olivhome_afterdate_liv
    $ renpy.pause()
    k emo-102 "[pname_max[0]], ускоряйся. Мне ещё душ нужно принять."
    m emo-3 "Хорошо. Сейчас."
    $ anim_speed = 0.1
    scene animated pgn_olivhome_afterdate_liv
    $ renpy.pause()
    m emo-7 "Почти..."
    scene bg pgn_olivhome_afterdate_07_7
    m emo-12 "Аррггхх... Мммм..."
    scene bg pgn_olivhome_afterdate_07_8
    k emo-104 "Ай! В глаз попал."
    m emo-2 "Прости. Я целился в рот..."
    k emo-113 "Чуть не забыла. Миранда просила передать, что попробует договорится о скидке и после обеда сообщит о результатах."
    m emo-3 "Спасибо. Ты самая лучшая тётя в мире!"
    k emo-114 "Спасибо. Давай, надевай шорты и бегом спать."
    $ accessiv.append("kira_afterdate_3")
    $ serialpgngame("loc_my_room_sleep")

label pgn_newolivhome_07b:
    m emo-3 "Расскажешь, как прошло?"
    k emo-109 "Ммм... нет."
    m emo-0 "Почему?"
    if ("pgn_newolivhome_datevideo03") in ivent24:
        m emo-6 "{i}Можешь не рассказывать и так знаю.{/i}"
    k emo-102 "Миранда просила передать, что после обеда сообщит по поводу скидки."
    m emo-4 "Спасибо. Я у тебя в долгу."
    k emo-108 "Ты знаешь, как отплатить."
    $ menu_hbox = False
    menu:
        "Сексом?":
            m emo-6 "Секс?"
            k emo-113 "Секс, это только для развлечения или снятия напряжения. Для меня лучше и на пользу карьере, когда знаешь все правильные реплики."
            m emo-0 "Ааа... точно."
        "Промолчать":
            pass
    $ accessiv.append("kira_afterdate_3")
    jump jump_dialogue


label pgn_newolivhome_08a:
    hide screen sms_olivia_menu
    "{#r=Привет.}"
    "{#r=Я смог найти вам жильё по приемлемой цене.}"
    "{#r=В центре города. Недалеко от школы.}"
    "{#r=$2000 в месяц.}"
    "{#r=Что мне передать агенту по недвижимости?}"
    "{#l=Ох! [pname_max[0]]!}"
    "{#l=Как? Как тебе удалось?}"
    "{#l=Через недвижимость дороже получается. А у тебя наоборот.}"
    "{#l=Мы с мамой никак не могли найти}"
    "{#l=Конечно. Мы согласны. Спасибо.}"
    "{#r=Хорошо. Я сообщу агенту, как с вами связаться.}"
    $ olivia_path = 4.5
    jump phone_max


label pgn_newolivhome_08b:
    hide screen sms_miranda_menu
    "{#r=Здравствуйте.}"
    "{#r=Моя знакомая рада, что цена не такая высокая.}"
    "{#r=Она согласна.}"
    "{#l=Хорошо. Тогда можете дать мне её контактный номер.}"
    "{#r=Да. Вот.}"
    "{#r=Номер отправлен}"
    "{#l=Спасибо. С вами приятно иметь дело.}"
    "{#l=Надеюсь, ещё увидимся.}"
    $ olivia_path = 5
    jump phone_max


label pgn_newolivhome_09:
    if qtime == 14 or qtime == 15:
        scene bg pgn_olivhome_relocation_01
        m emo-0 "{i}Вовремя, переезд проходит полным ходом. Пойду, узнаю как дела, может ещё какая-то помощь требуется.{/i}"
        scene bg pgn_olivhome_relocation_02
        m emo-0 "Эй! Привет!"
    if qtime >= 16 and qtime <= 20:
        scene bg pgn_olivhome_relocation_03a
        m emo-0 "{i}Наверное поздно пришёл, уже всё привезли им помощь уже не понадобится. Но, всё же я приехал.{/i}"
        m emo-6 "Никто не открывает. Может..."
        scene bg pgn_olivhome_relocation_03b
        m emo-0 "Открыто."
    if qtime == 14 or qtime == 15:
        scene bg pgn_olivhome_relocation_04a
    if qtime >= 16 and qtime <= 20:
        scene bg pgn_olivhome_relocation_04b
    d emo-57 "[pname_max[0]]! Спасибо, что пришёл..."
    m emo-3 "Здравствуйте. Диана."
    if qtime == 14 or qtime == 15:
        scene bg pgn_olivhome_relocation_05a
        d emo-51 "Ничего, что я в халате?"
        m emo-1 "Эм.. Ну... Ведь..."
        d emo-51 "Да, ты прав, не могу же я голой ходить и мешать людям работать."
    if qtime >= 16 and qtime <= 20:
        scene bg pgn_olivhome_relocation_05b
    d emo-53 "Мне Оливия передала, что ты помог нам с поиском нового жилья. Спасибо тебе большое."
    d emo-58 "Извини, что тогда запретила к нам приходить. Не знаю даже, почему так поступила."
    m emo-13 "{i}Всё она хорошо помнит и знает.{/i}"
    m emo-3 "Да нечего, всё хорошо. Я рад помочь своей девушке и её маме."
    d emo-53 "Ой, ты мой хороший какой. Спасибо. И если хочешь, можешь снова приходить и помогать Оливке с учебой."
    m emo-4 "Спасибо, с удовольствием."
    d emo-52 "Но только уроки и ни чего лишнего."
    m emo-3 "Да, конечно. А где Оливия?"
    d emo-55 "Она в своей комнате, наверху. 3-й этаж, дверь справа."
    m emo-3 "Спасибо."
    scene bg pgn_olivhome_relocation_06
    m emo-4 "{i}Ммм... Оливия без трусиков и чем-то увлеченно занимается, попробую подойти незаметно.{/i}"
    scene bg pgn_olivhome_relocation_07
    ol emo-144 "Ахх!!"
    m emo-3 "Привет!"
    ol emo-141 "[pname_max[0]]! Ты меня напугал!"
    scene bg pgn_olivhome_relocation_08
    m emo-6 "У тебя тут много места, и телевизор есть?"
    ol emo-142 "Да, мама взяла кредит в банке и купила мебель и технику. Остальное привезут и установят завтра."
    m emo-9 "Кредит? А выплатить сможете?"
    ol emo-142 "Мама сказала, раз такая низкая арендная плата, то можно улучшить условия проживания. И ты сам видел, что мебели не так много было."
    ol emo-143 "[pname_max[0]]. Спасибо тебе большое, ты очень хороший парень, я рада что ты мой... Т.е. наш с [pname_liza[4]] парень."
    m emo-0 "Всегда пожалуйста."
    m emo-4 "{i}Только благодарить нужно мою тётю, а она очень хорошо постаралась. Выложилась по полной.{/i}"
    ol emo-144 "Мама тебе сказала, что ты можешь ко мне приходить... помогать с уроками?"
    m emo-0 "Да. Так же, только по вторникам и пятницам?"
    ol emo-142 "Если хочешь, можешь в любой день, только кроме выходных, мы с [pname_liza[4]] гуляем."
    ol emo-142 "Лучше после школы, в 15 или в 16."
    m emo-3 "Хорошо. Вам нужна ещё какая-нибудь помощь?"
    ol emo-144 "Точно не знаю, это нужно у мамы спросить. И... Ты останешься на ужин? Мама приготовит, что-нибудь вкусное."
    m emo-3 "Я не против."
    scene bg pgn_olivhome_relocation_09
    ol emo-143 "А как тебе удалось найти такой дешевый дом, мы смотрели, ничего подобного не находили?"
    m emo-3 "Есть у меня знакомые, которые мне немного помогли."
    d emo-53 "О! Как-нибудь познакомишь, со своими знакомыми, поблагодарю и их."
    m emo-3 "Может быть, когда-нибудь."
    d emo-55 "А девушка это или мужчина?"
    ol emo-148 "Мам... Хватит давить на [pname_max[3]]. Как будет возможность, может и познакомит. Главное, что теперь у нас всё хорошо."
    d emo-51 "Да, Оливия, прости и ты [pname_max[0]]."
    m emo-3 "Всё нормально. Спасибо за ужин, очень вкусно."
    d emo-55 "[pname_max[0]], если хочешь, можешь к нам приходить в любое время, для тебя двери всегда будут открыты."
    $ olivia_path = 7
    $ qtime = 20
    jump loc_olivhomenew_kitchen


label pgn_newolivhome_tutoring:
    scene bg pgn_olivhome_tutor_01
    if ("olivhome_diana_spy") not in ivent24:
        ol emo-141 "Где будем заниматься?"
    if ("olivhome_diana_spy") in ivent24:
        ol emo-146 "Рада, что ты пришёл. Хм... ты уже возбуждён? Это у тебя такой фетиш на уроки или просто маму мою голую встретил?"
        m emo-13 "Ну..."
        ol emo-141 "Понятно. Где будем заниматься?"
    $ menu_hbox = True
    menu:
        "Диван":
            scene bg pgn_olivhome_tutor_02
            m emo-0 "А если вот так сделаем?"
            ol emo-140 "Поняла."
            m emo-0 "Да, всё верно. Что там далее?"
            $ menu_hbox = True
            menu:
                "Дотронуться до неё":
                    scene bg pgn_olivhome_tutor_03
                    ol emo-140 "[pname_max[0]]! Может поможешь мне до конца с уроками?"
                    m emo-0 "Обязательно помогу. Но может заодно другим концом займёшься?"
                    if ("olivhome_diana_spy") in ivent24:
                        ol emo-146 "Хорошо, доставай его."
                        jump pgn_newolivhome_tutoring_bj
                    else:
                        $ label_random = renpy.random.randint ( 1, 4)
                        if label_random != 2:
                            ol emo-146 "Хорошо, доставай его."
                            jump pgn_newolivhome_tutoring_bj
                        if label_random == 2:
                            ol emo-140 "Нет, мама может в любой момент зайти."
                "Не делать этого":
                    pass
            scene bg pgn_olivhome_tutor_02
            $ renpy.pause(3, hard=True)
            $ qtime += 1
            $ ivent24.append("olivia_tutoring")
            jump loc_olivhomenew_oroom
        "Кровать":
            scene bg pgn_olivhome_tutor_07
            ol emo-140 "[pname_max[0]], а что это означает?"
            m emo-0 "Что, именно? Ага, это..."
            ol emo-140 "Теперь ясно."
            scene bg pgn_olivhome_tutor_08
            $ menu_hbox = True
            menu:
                "Дотронуться до неё":
                    scene bg pgn_olivhome_tutor_09
                    if ("olivhome_diana_spy") in ivent24:
                        jump pgn_newolivhome_tutoring_vag
                    ol emo-143 "[pname_max[0]]! Ты меня отвлекаешь, пытаюсь выучить, а ты..."
                    m emo-3 "А я стимулирую тебя, чтобы запоминалось лучше."
                "Продолжить":
                    pass
            scene bg pgn_olivhome_tutor_10
            ol emo-144 "Ну, [pname_max[0]], прекрати! Я так кончу."
            m emo-3 "Может вместе кончим?"
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random != 2:
                ol emo-141 "Хорошо. Вытаскивай его."
                jump pgn_newolivhome_tutoring_vag
            if label_random == 2:
                pass
            scene bg pgn_olivhome_tutor_07
            $ renpy.pause(3, hard=True)
            $ qtime += 1
            $ ivent24.append("olivia_tutoring")
            jump loc_olivhomenew_oroom

label pgn_newolivhome_tutoring_bj:
    scene animated pgn_olivhome_tutor_bj
    $ renpy.pause()
    m emo-7 "{i}Класс! Оливия хорошо старается.{/i}"
    m emo-4 "{i}Был бы её учителем, то поставил... 4... А нет... 5{/i}"
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random != 2:
        pass
    if label_random == 2:
        jump pgn_newolivhome_tutoring_bj_diana
    scene animated pgn_olivhome_tutor_bj
    $ renpy.pause()
    $ label_random = renpy.random.randint ( 1, 5)
    if label_random != 3:
        pass
    if label_random == 3:
        jump pgn_newolivhome_tutoring_bj_diana
    m emo-7 "Оливка... Сейчас кончу."
    scene animated pgn_olivhome_tutor_bj_end
    m emo-12 "Аааррргх... Спасибо."
    scene bg pgn_olivhome_tutor_06
    ol emo-141 "Ну всё. Теперь уроки."
    m emo-4 "Да, продолжим."
    scene bg pgn_olivhome_tutor_02
    $ renpy.pause(3, hard=True)
    $ qtime += 1
    $ ivent24.append("olivia_tutoring")
    $ PGN_Addstatsex(stat_olivia, 0, 0, 1, 0, 0)
    jump loc_olivhomenew_oroom

label pgn_newolivhome_tutoring_bj_diana:
    scene bg pgn_olivhome_tutor_05
    d emo-52 "Дети, вам принести что-нибудь? Не хотите кофе или чай с печеньем попить?"
    ol emo-144 "А... Мам, нет спасибо. Мы уже почти закончили."
    scene bg pgn_olivhome_tutor_04
    if label_random == 3:
        m emo-0 "{i}Это я почти кончил.{/i}"
    if label_random == 2:
        m emo-9 "{i}Чёрт! В самом разгаре прервали.{/i}"
    scene bg pgn_olivhome_tutor_05
    d emo-56 "Оливка, ты что там делаешь?"
    ol emo-144 "Я ручку уронила, пытаюсь достать."
    m emo-0 "Попросила, я бы сам поднял, даже не дала времени среагировать."
    d emo-57 "Ну ладно, занимайтесь."
    scene bg pgn_olivhome_tutor_06
    m emo-0 "Ну, что, продолжим?"
    if label_random == 3:
        m emo-0 "Я уже почти кончил, все равно мама твоя ушла..."
        ol emo-140 "Ладно."
        scene animated pgn_olivhome_tutor_bj
        $ renpy.pause()
        scene animated pgn_olivhome_tutor_bj_end
        m emo-12 "Аааррргх... Да... Спасибо."
        $ PGN_Addstatsex(stat_olivia, 0, 0, 1, 0, 0)
        scene bg pgn_olivhome_tutor_06
        ol emo-141 "Ну всё. Теперь мне поможешь... с уроками."
        m emo-4 "Конечно."
    if label_random == 2:
        ol emo-145 "Нет. Вдруг вернётся, но уже с чаем или с чем-то ещё. Не думаю, что успеешь спрятать."
        $ menu_hbox = True
        menu:
            "Согласиться":
                pass
            "Зачем прятать?":
                m emo-4 "А зачем прятать? Может быть тоже присоединилась."
                ol emo-148 "[pname_max[0]]! Вообще то я твоя девушка, а не она."
                m emo-8 "Ладно, ладно. Извини. Сказал глупость."
    scene bg pgn_olivhome_tutor_02
    $ renpy.pause(3, hard=True)
    $ qtime += 1
    $ ivent24.append("olivia_tutoring")
    jump loc_olivhomenew_oroom

label pgn_newolivhome_tutoring_vag:
    scene bg pgn_olivhome_tutor_13_1
    ol emo-140 "[pname_max[0]], я сделаю всё сама. Мне так будет удобнее."
    m emo-3 "Ладно."
    $ anim_speed = 0.4
    scene animated pgn_olivhome_tutor_vag
    $ renpy.pause()
    m emo-10 "{i}В этой позе, в её киске очень узко.{/i}"
    m emo-4 "{i}Очень способная ученица.{/i}"
    scene animated pgn_olivhome_tutor_vag
    $ renpy.pause()
    $ label_random = renpy.random.randint ( 1, 4)
    if label_random != 4:
        pass
    if label_random == 4 or pgn_ach_repeat == 109:
        scene bg pgn_olivhome_tutor_11
        d emo-53 "Дети. Вам что-нибудь принести? Немного отдохнёте от уроков."
        ol emo-142 "Нет, спасибо мам. Нам немного осталось."
        d emo-55 "Хорошо. Продолжайте."
        scene bg pgn_olivhome_tutor_13_1
        m emo-0 "Ну что, продолжим? Как твоя мама сказал."
        ol emo-140 "Да, давай побыстрее, пока она не вернулась."
        $ anim_speed = 0.2
        scene animated pgn_olivhome_tutor_vag
        $ renpy.pause()
    m emo-13 "Можно... Прямо... В киску?"
    ol emo-146 "Да... кончай..."
    scene animated pgn_olivhome_tutor_vag_end
    if pgnach_109.aopen == False:
        $ PGN_Achadd(pgnach_109, 109)
    m emo-12 "Ааааххх... Мммм... ААаааххх..."
    if pgn_ach_repeat == 109:
        jump table_pgn_achievement
    scene bg pgn_olivhome_tutor_07
    $ renpy.pause(3, hard=True)
    $ qtime += 1
    $ ivent24.append("olivia_tutoring")
    $ PGN_Addstatsex(stat_olivia, 0, 0, 0, 1, 0)
    jump loc_olivhomenew_oroom


label pgn_olivhome_droom_dianespy:
    if ("olivhome_diana_spy_et") not in ivent24:
        scene bg pgn_olivhome_droomdspy_01
        m emo-6 "{i}Хм... Дверь в комнату Дианы открыта.{/i}"
    scene bg pgn_olivhome_droomdspy_02
    m emo-3 "{i}Ух! Мама Оливии, голая... ей нравится быть обнажённой.{/i}"
    scene bg pgn_olivhome_droomdspy_03
    d emo-57 "{i}Ооо! Какой негодник. Предпочитаешь более зрелое тело?{/i}"
    $ menu_hbox = True
    menu:
        "Прекратить" if pgn_ach_repeat == 0:
            pass
        "Продолжить подглядывать":
            scene bg pgn_olivhome_droomdspy_04
            d emo-54 "{i}Хм... не у ходит. Тогда устрою ему небольшое шоу.{/i}"
            $ label_random = renpy.random.randint ( 1, 3)
            if label_random == 1 or diana_path <= 1 or pgn_ach_repeat == 112:
                scene bg pgn_olivhome_droomdspy_05
                m emo-4 "{i}Классная попка. Если только мы были одни и если она страстно желала секса со мной, то я бы её трахнул.{/i}"
                m emo-0 "{i}[pname_max[0]]! Успокойся! А то сейчас от своего воображения кончу в штаны.{/i}"
                d emo-58 "Какие мне трусики надеть сегодня, даже и не знаю..."
                scene animated pgn_olivhome_droomdspy_ass
                if pgnach_112.aopen == False:
                    $ PGN_Achadd(pgnach_112, 112)
                m emo-0 "{i}Туда... сюда... Влево... Вправо...{/i}"
                m emo-0 "{i}Такое ощущение, что её попка приглашает меня.{/i}"
                d emo-51 "Где же они, где... Где мои любимые трусики... Ах... Вот они, только нужно достать."
                scene bg pgn_olivhome_droomdspy_06
                m emo-0 "{i}Ого! Еле сдерживаю себя и стояк у меня каменный. Пойду я лучше.{/i}"
            elif (label_random != 1 and diana_path > 1) or pgn_ach_repeat == 113:
                scene bg pgn_olivhome_droomdspy_06
                d emo-56 "Где же он у меня. Хм... А вот, нашла."
                scene bg pgn_olivhome_droomdspy_07
                m emo-4 "{i}Она из комода достала дилдо, сейчас будет очень интересно.{/i}"
                scene bg pgn_olivhome_droomdspy_04
                d emo-51 "{i}Надеюсь когда-нибудь это будет твой большой и настоящий. Смотри внимательно.{/i}"
                $ anim_speed = 0.3
                scene animated pgn_olivhome_droomdspy_dv_1
                m emo-0 " {i}Вот это да! С такой лёгкостью засунула в киску.{/i}"
                m emo-0 "{i}Мама Оливии очень горячая и... голодная. Так и хочется присоединиться. Но лучше не стоит задерживаться или всё же остаться до конца?{/i}"
                $ menu_hbox = True
                menu:
                    "Остаться":
                        $ anim_speed = 0.1
                        scene animated pgn_olivhome_droomdspy_dv_1
                        m emo-5 "{i}О! Она ускорилась!{/i}"
                        scene animated pgn_olivhome_droomdspy_dv_1
                        $ renpy.pause(10, hard=True)
                        scene animated pgn_olivhome_droomdspy_dv_2
                        d emo-56 "Аххх... Глубже... Давай глубже..."
                        m emo-9 "{i}Интересно, кого она себе представляет?{/i}"
                        $ anim_speed = 0.07
                        scene animated pgn_olivhome_droomdspy_dv_2
                        $ renpy.pause(7, hard=True)
                        scene bg pgn_olivhome_droomdspy_08
                        if pgnach_113.aopen == False:
                            $ PGN_Achadd(pgnach_113, 113)
                        d emo-54 "Ааааааххх..."
                        scene bg pgn_olivhome_droomdspy_09
                        m emo-4 "{i}Вау! Это было мощно. Класс!!!{/i}"
                        m emo-13 "{i}Но мне пора, а то сейчас своим членом проделаю дыру в стене.{/i}"
                    "Уйти" if pgn_ach_repeat == 0:
                        pass
            if pgn_ach_repeat == 112 or pgn_ach_repeat == 113:
                jump table_pgn_achievement
            $ qtime += 1
    $ ivent24.append("olivhome_diana_spy")
    jump loc_olivhomenew_et2


label pgn_newolivhome_10:
    scene bg pgn_newolivhome_10_hottub_01
    ol emo-143 "Привет, [pname_max[0]]! Заходи! Плавки взял?"
    m emo-6 "Плавки? Ты мне не о чём таком не говорила."
    ol emo-141 "Хм... А трусы на тебе хотя бы есть?"
    m emo-0 "Да."
    ol emo-143 "Хорошо. Тогда заходи, раздевайся до трусов и идём за мной."
    scene bg pgn_newolivhome_10_hottub_02
    ol emo-142 "Мы с Мамой совсем не ожидали такого подарка. Ты и так помог нам, да ещё это."
    m emo-0 "Я вспомнил, что ты хотела бассейн, а он есть только у нас и тебе приходится к нам приходить."
    ol emo-142 "Так я не только из-за бассейна, но и с [pname_liza[4]] повидаться."
    ol emo-143 "В общем мы с мамой ждали тебя, когда ты придёшь, чтобы вместе опробовать. Только мама уже..."
    scene bg pgn_newolivhome_10_hottub_03
    ol emo-148 "Мам, ты обещала, что не будешь залазить в бассейн, пока [pname_max[0]] не придёт."
    d emo-58 "Оливка, извини, мне очень жарко и не удержалась."
    ol emo-148 "И мам! Где твой купальник?"
    d emo-58 "Не знаю, я правда искала, но ни как не могла найти, может где-то ещё в коробках валяется."
    ol emo-147 "Все коробки давно разобрали и выбросили."
    m emo-3 "В этом нет ничего страшного, я тоже не взял."
    ol emo-146 "На тебе хотя бы трусы... Ладно. Пойдём."
    scene bg pgn_newolivhome_10_hottub_04
    d emo-53 "[pname_max[0]], ты такой душка. Этот навес и джакузи..."
    m emo-3 "Вы наверное соскучились, после развода, решил сделать приятное и заказал вам."
    scene bg pgn_newolivhome_10_hottub_06
    ol emo-142 "Он у меня такой молодец. Поэтому он мой парень."
    scene bg pgn_newolivhome_10_hottub_04
    d emo-55 "[pname_max[0]], а где и кем ты работаешь?"
    scene bg pgn_newolivhome_10_hottub_06
    m emo-13 "Эм... у меня нет постоянной работы, подрабатываю, где получится."
    m emo-2 "{i}Блин! Оливия! Сидим напротив её матери, а она не стесняясь просунула свою ручку... Оххх!{/i}"
    scene animated pgn_newolivhome_10_hottub_oliv_hj
    m emo-5 "{i}Мне нельзя кончить, только не здесь. Как же мне будет неудобно, если сейчас кончу в воду, всё же сплывёт.{/i}"
    scene bg pgn_newolivhome_10_hottub_05
    m emo-2 "{i}Чёрт! Это очень сложно, особенно когда Диана сидит совсем голая и... {/i}"
    scene bg pgn_newolivhome_10_hottub_07
    m emo-0 "{i}И у неё соски набухли. Кажется догадалась, что творит её дочь.{/i}"
    scene bg pgn_newolivhome_10_hottub_04
    d emo-55 "{i}Моя малышка думает, что я не понимаю, что она там правой рукой своей делает.{/i}"
    d emo-52 "{i}Нет уж, девочка моя, с таким большим ты не справишься, лучше пусть мама отблагодарит этого красавца. Я уж точно знаю как.{/i}"
    d emo-53 "Оливка, у [pname_max[1]] наверное в горле всё пересохло от такой жары, и у меня тоже. Может принесешь нам попить, сока или просто воды."
    scene bg pgn_newolivhome_10_hottub_06
    ol emo-140 "Ммм..."
    m emo-0 "Я не против... Если конечно не затруднит."
    scene bg pgn_newolivhome_10_hottub_08
    ol emo-140 "Хорошо. Я схожу, но не уверена, что у нас есть сок."
label pgn_newolivhome_10_arch:
    scene bg pgn_newolivhome_10_hottub_09
    m emo-0 "{i}И вот мы остались наедине. Надеюсь меня не выгонит, как в прошлый раз, когда по её же просьбе показал член.{/i}"
    scene bg pgn_newolivhome_10_hottub_10
    $ renpy.pause(3, 0)
    scene bg pgn_newolivhome_10_hottub_11
    d emo-55 "Вставай, вредно так долго сидеть в воде."
    m emo-0 "Эм... Ну..."
    d emo-53 "То что у тебя эрекция, в этом нет ничего постыдного, ты ещё молодой, это нормально, можешь не прикрываться."
    scene bg pgn_newolivhome_10_hottub_12
    d emo-51 "Снимай трусы и ложись."
    m emo-13 "{i}Блин! Как тогда, показал и тут же выгнала, а сейчас что, жизни будет учить!?{/i}"
    scene bg pgn_newolivhome_10_hottub_13
    d emo-57 "{i}И всё же у него очень большой. Сложно представить, как такое может поместиться в моей дочери. Я не могу настоять, чтобы они расстались, это будет неправильно с моей стороны, но можно иначе...{/i}"
    scene bg pgn_newolivhome_10_hottub_14
    if pgnach_111.aopen == False:
        $ PGN_Achadd(pgnach_111, 111)
    m emo-9 "Ох! Мама, мама Оливии! Оливия... может... вот-вот прийти..."
    d emo-51 "[pname_max[0]], давай договоримся. Если поблизости нет моей Оливки, то будешь ко мне обращаться просто по имени. Хорошо?"
    m emo-13 "Да. Но она моя девушка, это неправильно..."
    scene bg pgn_newolivhome_10_hottub_d_bj_1
    d emo-54 "Тс-с-с. Расслабься и получай удовольствие... Позволь мне отблагодарить тебя за все эти подарки."
    scene animated pgn_newolivhome_10_hottub_d_bj
    m emo-3 "{i}Ого! Не могу поверить. Оливия мне дрочила на виду у её мамы, теперь Диана делает минет, это у них что-то типа соревнований? Пока мне это нравится.{/i}"
    d emo-58 "[pname_max[0]], я давно не делала минет. Так что если что не так..."
    m emo-10 "Нет, всё хорошо... отлично... Мама Ол... Т.е Диана, продолжай, у тебя всё хорошо получается..."
    m emo-4 "{i}Диана стройная, как её дочь и... голая... Блин!{/i}"
    m emo-10 "Я уже скоро!"
    d emo-52 "Кончай мне... в рот."
    scene animated pgn_newolivhome_10_hottub_d_bj_end
    m emo-12 "Аргх!!!"
    scene bg pgn_newolivhome_10_hottub_15
    d emo-57 "[pname_max[0]], если захочешь ещё, ты знаешь где меня найти."
    m emo-4 "Хорошо."
    if pgn_ach_repeat == 111:
        jump table_pgn_achievement
    ol emo-148 " {i}Вот так, да Мама! Снова за своё, значит война.{/i}"
    $ qtime += 1
    $ diana_path = 2
    $ PGN_Addstatsex(stat_diana, 0, 0, 1, 0, 0)
    jump loc_olivhomenew_backyard

label pgn_newolivhome_hottub_olivdiane:
    scene bg pgn_newolivhome_10_hottub_04
    d emo-52 "[pname_max[0]]. Как тебе джакузи, понравилось в тот раз?"
    m emo-13 "Да. Неплохо."
    scene bg pgn_newolivhome_10_hottub_06
    m emo-10 "{i}Оливия снова за своё, точнее схватилась за мой член.{/i}"
    scene animated pgn_newolivhome_10_hottub_oliv_hj
    $ renpy.pause()
    scene bg pgn_newolivhome_10_hottub_05
    d emo-57 "Мы всегда будет рады такому гостю. Так что приходи по чаще."
    scene bg pgn_newolivhome_10_hottub_07
    m emo-3 "{i}Сиськи у Дианы шикарны.{/i}"
    scene animated pgn_newolivhome_10_hottub_oliv_hj
    $ renpy.pause()
    m emo-2 "{i}Чёрт! Да я так скоро кончу от этого, когда меня окружают такие красавицы.{/i}"
    scene bg pgn_newolivhome_10_hottub_06
    d emo-53 "Оливка, принесешь [pname_max[2]] попить? А то на нём и лица не видно."
    $ menu_hbox = True
    menu:
        "Если можно...":
            scene bg pgn_newolivhome_10_hottub_08
            ol emo-142 "Хорошо. Я сейчас быстренько сбегаю."
            d emo-55 "Оливка. А приготовь мне пожалуйста коктейль. Ты знаешь, тот что я люблю."
            ol emo-147 "Ох, ладно."
            jump pgn_newolivhome_hottub_diane
        "Пить не хочется":
            m emo-3 "Спасибо. Но мне пить не хочется."
    d emo-51 "Хорошо, тогда ещё немного побудем здесь."
label pgn_newolivhome_hottub_olivdiane_arch:
    scene animated pgn_newolivhome_10_hottub_oliv_hj
    $ renpy.pause()
    m emo-13 "{i}Блин! Оливия! Может хватит? Я так долго не продержусь.{/i}"
    scene bg pgn_newolivhome_10_hottub_07
    m emo-10 "{i}Ох уж эти сиськи её мамы и...{/i}"
    scene bg pgn_newolivhome_10_hottub_16
    m emo-10 "{i}И её...{/i}"
    m emo-13 "{i}Блин! Ещё чуть-чуть и я. Что же делать?{/i}"
    scene bg pgn_newolivhome_10_hottub_04
    d emo-51 "Дети, я тут уже дольше вас, так что мне пора выходить."
    d emo-52 "Только вы то же долго тут не сидите, очень вредно, и солнечный удар можно получить."
    scene bg pgn_newolivhome_10_hottub_06
    ol emo-142 "Хорошо, мам."
    scene bg pgn_newolivhome_10_hottub_16
    ol emo-146 "Наконец-то она ушла, больше не могу ждать. Трахни меня."
    scene bg pgn_newolivhome_10_hottub_oliv_vag_1
    ol emo-147 "[pname_max[0]], не тяни. Вставь его в меня."
    $ anim_speed = 0.3
    scene animated pgn_newolivhome_10_hottub_oliv_vag
    m emo-3 "{i}Я был уже на грани, но сейчас... Могу продолжать.{/i}"
    scene animated pgn_newolivhome_10_hottub_oliv_vag
    $ renpy.pause()
    ol emo-146 "[pname_max[0]], ускорься. Мама не должна нас увидеть."
    m emo-4 "Ага, хорошо."
    $ anim_speed = 0.1
    scene animated pgn_newolivhome_10_hottub_oliv_vag
    $ renpy.pause()
    m emo-10 "Я почти..."
    scene bg pgn_newolivhome_10_hottub_17
    m emo-12 "Арррггхх!!! Аааахххх!!!"
    scene bg pgn_newolivhome_10_hottub_18
    if pgnach_110.aopen == False:
        $ PGN_Achadd(pgnach_110, 110)
    m emo-4 "Ух! Спасибо! Было круто!"
    ol emo-143 "И тебе спасибо. Пойдём, а то мама может что-то заподозрить."
    m emo-4 "{i}Мне кажется она и так поняла, что мы будем делать.{/i}"
    if pgn_ach_repeat == 110:
        jump table_pgn_achievement
    if diana_path == 2:
        $ diana_path = 3
        scene bg pgn_newolivhome_10_hottub_19
        d emo-51 "{i}Ох... Оливка. Я не думала, что ты настолько далеко зашла. Ну что ж, посмотрим.{/i}"
    $ qtime += 1
    $ PGN_Addstatsex(stat_olivia, 0, 0, 0, 1, 0)
    jump loc_olivhomenew_backyard

label pgn_newolivhome_hottub_diane:
    scene bg pgn_newolivhome_10_hottub_09
    d emo-55 "Ты же сюда не ради этого пришёл, у вас дома большой бассейн. Так может сразу к делу?"
    m emo-3 "Эм... а... Да..."
    scene bg pgn_newolivhome_10_hottub_10
    $ renpy.pause(3, 0)
    scene bg pgn_newolivhome_10_hottub_11
    d emo-55 "Пойдём, большой мальчик."
    scene bg pgn_newolivhome_10_hottub_14
    d emo-54 "С нашего прошлого раза, очень соскучилась по этому размеру во рту."
    m emo-10 "Ох..."
    scene animated pgn_newolivhome_10_hottub_d_bj
    $ renpy.pause()
    m emo-4 "{i}Очень приятно проходят мои выходные. Лежу, загораю и мне делают минет.{/i}"
    m emo-10 "{i}Диана неплохо сосёт. Ну она же взрослая, опыт всё же есть.{/i}"
    scene animated pgn_newolivhome_10_hottub_d_bj
    $ renpy.pause()
    m emo-7 "Диана... Я"
    scene animated pgn_newolivhome_10_hottub_d_bj_end
    m emo-12 "Аргх!!!"
    scene bg pgn_newolivhome_10_hottub_14
    d emo-57 "Спасибо. Подкрепилась немного витаминами."
    m emo-4 "Это вам спасибо."
    d emo-55 "С нетерпением буду ждать следующего раза."
    $ qtime += 1
    $ PGN_Addstatsex(stat_diana, 0, 0, 1, 0, 0)
    jump loc_olivhomenew_backyard
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
