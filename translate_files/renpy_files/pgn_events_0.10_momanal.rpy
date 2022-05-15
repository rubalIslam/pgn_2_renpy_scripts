






label pgn_events_momanal_01:
    $ mom_path = 11.1
    k emo-114 "[pname_max[0]], [pname_max[0]], постой. У меня для тебя хорошие новости."
    m emo-13 "Точно хорошие?"
    k emo-113 "Я написала новый сценарий для нового фильма."
    m emo-0 "Ммм... Ясно"
    k emo-104 "Ясно... И всё? Я думала, что ты будешь рад лишний раз заняться сексом и получить за это деньги."
    k emo-112 "Хны... Племяннику надоели мои фильмы... Хны..."
    m emo-0 "Хорошо, я снимусь."
    k emo-113 "Хороший мальчик."
    k emo-100 "Мне нужно писать сценарии, чтобы больше зарабатывать, и без меня у тебя не будет нормальной высокооплачиваемой работы."
    m emo-0 "Да, да, я понял"
    m emo-0 "Когда начнём?"
    k emo-103 "Не спеши. Мне твоей младшей сестре нужно ещё сообщить. Честно говоря, она меня упрашивала о нечто подобном."
    menu:
        "Значит сегодня?":
            if daysn == 1 or daysn == 4:
                k emo-104 "А ты ничего не забыл?"
                m emo-0 "Что я забыл?"
                k emo-104 "Сегодня же день, когда твоя Мама будет на съёмках."
                m emo-0 "Точно"
            else:
                k emo-104 "Если хочешь, можно сегодня. Только не забудь, что после ужина."
        "Значит вечером?":
            if daysn == 1 or daysn == 4:
                k emo-104 "А ты ничего не забыл?"
                m emo-0 "Что я забыл?"
                k emo-104 "Сегодня же день, когда твоя Мама будет на съёмках."
                m emo-0 "Точно"
            else:
                k emo-100 "Да, вечером, после ужина."
        "Завтра?" if daysn == 1 or daysn == 4:
            k emo-104 "Не сегодня уж точно. Только не забудь, что после ужина."
    jump jump_dialogue


label pgn_events_momanal_02:
    scene pgn_film_9_scene_01_vadx
    m emo-0 "Фух! Как же устал я с этой тренировки. Поскорей душ принять."
    scene pgn_film_9_scene_02_vadx
    menu:
        "Снова музыку включила на полную":
            pass
        "Опять кто-то забыл кран закрыть":
            pass
        "Что за шум!?":
            pass
    m emo-1 "Что это за шум!?"
    scene pgn_film_9_scene_03_vadx
    m emo-3 "Ого! Сестренка смотрит порно. Вот же проказница, пока мамы дома нет, смотрит на полную громкость и без наушников."
    scene animated familyporn_film9_01
    m emo-4 "Вау! Моя малышка двигает попкой в ритм секса..."
    m emo-4 "Держите меня семеро, я хочу эту попку.."
    scene pgn_film_9_scene_05_vadx
    l emo-48 "Хм... мой братик ни как не может отвести глаза... Я очень от этого возбудилась."
    l emo-41 "Братик! Может подойдешь уже ко мне... ближе... составишь мне компанию."
    menu:
        "С радостью, только душ приму":
            pass
        "Извини, я в душ":
            pass
        "А тебе на рано порно смотреть?":
            pass
    m emo-9 "А! Ой, прости... Эм.. Я.. Это... Пойду в душ, как раз туда и собирался."
    scene pgn_film_9_scene_06_vadx
    l emo-46 "Чёрт! Я перевозбудилась, мне нужен секс, мне нужен большой член."
    scene pgn_film_9_scene_07_vadx
    l emo-49 "А единственный, кто сейчас может меня удовлетворить, это мой братик."
    l emo-48 "Как только он выйдет из душа, от моего предложения отказаться точно не сможет."
    scene pgn_film_9_scene_08_vadx
    l emo-49 "Братик! Зайди ко мне на минуточку."
    scene pgn_film_9_scene_09_vadx
    m emo-9 "Сестренка..."
    l emo-43 "Сделай так же, как в прошлый раз, трахни меня в попку. Пожалуйста."
    menu:
        "Может подождём Маму?":
            pass
        "Презервативы есть?":
            pass
        "Мама скоро придёт":
            pass
    m emo-8 "Но мама может вот скоро уже прийти"
    scene pgn_film_9_scene_10_vadx
    l emo-49 "Т.е. ты меня не хочешь? Посмотри на эту попку, она так и просится на твой член."
    l emo-43 "Я вижу, что тебе самому очень этого хочется, так что оттрахай меня"
    m emo-3 "Хорошо. Ты сама напросилась."
    scene animated familyporn_film9_03
    $ renpy.pause()
    scene pgn_film_9_scene_12_vadx
    mom emo-69 "Наконец-то удалось уйти пораньше. Смогу за долгие месяцы отдохнуть нормально."
    scene pgn_film_9_scene_13_vadx
    mom emo-60 "Приму душ и буду заниматься любимыми делами. Стоп... Что за шум?"
    mom emo-68 "Она снова включила порно. Я же просила её, если смотреть, то в наушниках."
    scene pgn_film_9_scene_14_vadx
    mom emo-63 "Хм... Сумка сына здесь, неужели они вместе смотрят. Ну я им сейчас задам."
    scene pgn_film_9_scene_15_vadx
    mom emo-66 "О Боже! Дети! Как так!?"
    scene pgn_film_9_scene_16_vadx
    mom emo-66 "Вы... Вы... Вы..."
    l emo-50 "М..."
    scene pgn_film_9_scene_17_vadx
    m emo-9 "Мама!?"
    m emo-9 "{i}Что она тут делает? Тётя не о чём таком не говорила. Вот же блин, что делать то.{/i}"
    mom emo-68 "{i}Боюсь только представить, чтобы было, если на месте этой малышки была моя [pname_liza[0]]. Страшно представить.{/i}"
    mom emo-64 "Сынок, а ну живо вытащил из неё свой... свой... Вытащи!"
    scene pgn_film_9_scene_18_vadx
    mom emo-64 "Я не понимаю, чем ты вообще думал!? Она же твоя сестра!"
    m emo-8 "Я..."
    mom emo-63 "А ты, позволила ему трахнуть себя. Как ты могла?"
    menu:
        "Попросить выйти":
            pass
        "Не мешай, мне нужно здесь закончить":
            pass
        "Ты мне поможешь кончить?":
            pass
    scene pgn_film_9_scene_19_vadx
    m emo-2 "Мам, можешь выйти не надолго, я ещё не кончил."
    mom emo-64 "Что? Не кончил, ты что такое говоришь?"
    scene pgn_film_9_scene_20_vadx
    mom emo-68 "Ах! Малышка, ты меня напугала. Ты чего..."
    scene pgn_film_9_scene_21_vadx
    mom emo-74 "Ай! Как ты смеешь так обращаться со своей мамой. Вот сейчас встану и получите оба..."
    scene pgn_film_9_scene_22_vadx
    mom emo-68 "Солнышко. Ты что это задумала."
    m emo-3 "Видимо, тебе придётся помочь мне кончить."
    scene pgn_film_9_scene_23_vadx
    mom emo-69 "Сынок! Не надо! Я же твоя мама!"

    m emo-4 "{i}Не думал, что первый анал с мамой будет на съёмках. [pname_kira[0]], спасибо тебе за такой приятный сюрприз{/i}"
    scene pgn_film_9_scene_24_1_vadx
    m emo-3 "{i}Вау! Какой тугой анал!{/i}"
    scene pgn_film9_momanal_01_vadx
    mom emo-66 "Ааа!!! Больно!! Остановись!!!"
    menu:
        "Прекратить":
            pass
        "Продолжить":
            scene animated familyporn_film9_02
            $ accessiv.append("pf9_nonstop")
            mom emo-66 "Хватит!!!"
            mom emo-69 "Пожалуйста!!!"
            scene pgn_film9_momanal_02_vadx
            mom emo-68 "[pname_max[0]]!!!"
            m emo-9 "Прости, я...."
    scene pgn_film9_momanal_03_vadx
    $ renpy.pause(2)
    scene pgn_film9_momanal_11_vadx
    m emo-2 "[pname_kira[0]], что произошло? Почему, она убежала, я что-то не так сделал?"
    k emo-100 "Тут не твоей вины..."
    if ("pf9_nonstop") in accessiv:
        k emo-103 " Ну почти нет..."
    k emo-104 "Должна была участвовать другая актриса. Так что я сама в шоке, когда появилась [pname_mom[7]]."
    l emo-46 "И что нам делать?"
    k emo-100 "Так, малышка, иди в гримерную, мы скоро подойдём. А ты, [pname_max[0]], иди за мной."
    scene pgn_film9_momanal_05_vadx
    k emo-104 "Чего стоишь, снимай халат и в душ."
    scene pgn_film9_momanal_06_vadx
    m emo-15 "{i}Мама наверное сильно расстроена. Но от куда мне было знать, что она была не готова к этому сексу.{/i}"
    m emo-15 "{i}Блин!{/i}"
    scene pgn_film9_momanal_07_vadx
    m emo-9 "Ааа!!"
    k emo-101 "Расслабься, это я. Не могла же я отправить тебя домой таким возбужденным."
    scene animated familyporn_film9_event_08
    m emo-1 "[pname_kira[0]], а где мама?"
    k emo-107 "Как только она вся в слезах выбежала со съёмочной площадки, я пыталась остановить её и поговорить, но она сразу села в машину и уехала."
    k emo-111 "Я действительно не знала, что вместо той актрисы будет [pname_mom[0]]. Если бы знала, то отменила съёмки."
    m emo-8 "И... И... Ооххх! И что дальше будем делать?"
    k emo-100 "Вот сейчас закончим и вместе поедем домой."
    scene pgn_film9_momanal_09_vadx
    m emo-10 "Аааахх!!!"
    scene pgn_film9_momanal_10_vadx
    m emo-13 "Спасибо."
    k emo-101 "Беги переодевайся, и тебя с [pname_liza[4]] жду на парковке."
    m emo-0 "Хорошо."
    $ qtime += 1
    $ mom_path = 11.2
    jump loc_pool



label pgn_events_momanal_03_breakfast:
    scene pgn_veranda_breakfest_without_mom
    if mom_path == 11.2:
        $ mom_path = 11.3
        l emo-40 "А где Мама?"
        k emo-100 "[pname_liza[0]], она сказала, что некоторое время не будет выходить из комнаты."
        a emo-20 "Что такого случилось вчера? Она была вся в слезах. Я пыталась спросить, но она захлопнула дверь."
        a emo-28 "[pname_max[0]], что ты снова натворил?"
        k emo-107 "[pname_max[0]]... Не совсем в этом виноват."
        if ("pf9_nonstop") in accessiv:
            m emo-8 "Я не знал, я думал так задумано, по сценарию."
            a emo-29 "Ага, прям так и поверила."
        k emo-111 "Видишь ли, [pname_alice[0]], в съёмках должна была участвовать другая актриса. А о изменениях мне не сообщили."
        a emo-32 "Ясно. Но ты всё равно в этом виноват. И должен найти способ, как помочь маме."
        m emo-14 "Хорошо."
        a emo-29 "Так, [pname_liza[0]], ты почему голая? А ну встала и пошла, и оделась."
        l emo-44 "Ты мне не Мама, что хочу, то и делаю."
        a emo-28 "Я твоя старшая сестра, а старших нужно слушать. Или захотелось, чтобы [pname_max[0]] прям тут на тебя накинулся?"
        m emo-1 "Я не..."
        a emo-33 "Ну да, ну да..."
        l emo-48 "..."
        a emo-20 "Ладно, как хочешь. Всем приятного аппетита."
    else:
        m emo-0 "Снова это?"
        a emo-20 "Если что-то не нравится, готовь сам."
        m emo-0 "Приятного аппетита."
    jump veranda_breakfast_next


label pgn_events_momanal_03_dinner:
    $ scenevar("kira_veranda_dinner_without_mom")
    m emo-0 "Всем приятного аппетита."
    m emo-0 "Мне отнести ей еду?"
    a emo-20 "Не нужно, я сама. Она хотя бы не на меня обижена."
    $ qtime = 20
    jump loc_veranda


label pgn_events_momanal_04:
    $ mom_path = 11.4
    m emo-0 "Можешь подсказать, как поднять настроение маме. У меня совсем нет идей."
    k emo-104 "Секс точно не поможет."
    m emo-0 "Она меня даже и близко не подпустит к себе."
    k emo-101 "И меня наверное тоже. Допустим можно сводить её куда-нибудь, развеяться."
    m emo-0 "А куда?"
    k emo-104 "Тут помочь ни с чем не смогу, сама мало где была. Точнее в приличных местах я не была."
    k emo-100 "Вроде в отеле есть ресторан."
    k emo-100 "В общем идеею тебе подала, думай дальше сам."
    m emo-0 "Ладно."
    jump jump_dialogue


label pgn_events_momanal_05_blackcard:
    m emo-0 "Тёть, а у тебя есть \"Чёрная Карта\"?"
    k emo-104 "Тебе кофе захотелось попить?"
    m emo-0 "Нет, вроде что-то типа карточки, наверное размером с кредитной карты."
    k emo-100 "Нет, никогда о таком не слышала. Спроси в отеле, может они знают."
    m emo-0 "Хорошо."
    jump jump_dialogue


label pgn_events_momanal_06:
    $ mom_path, qtime = 11.6, qtime+1
    scene pgn_mall_maverick_maxoffice_01
    other emo-984 "Здравствуйте. Что-то интересует?"
    m emo-13 "Да. Эм... У вас есть в продаже смокинг, просто я тут его ни где не вижу."
    other emo-984 "Есть. Если хотите сейчас примерить, то можете пройти в примерочную."
    scene bg pgn_maxnewclothing_04
    $ renpy.pause (3)
    scene bg pgn_maxnewclothing_05
    other emo-984 "Пожалуйста. Если что, позовите."
    m emo-3 "Ок"
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_07
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene pgn_mall_maverick_maxoffice_02
    m emo-6 "Хм... Я похож на какого-то старика. И эти полоски... "
    m emo-0 "Можно что-нибудь другое, необязательно смокинг."
    other emo-985 "Да, конечно. Вы ищите повседневную одежду или для работы?"
    m emo-0 "Хочу в ресторан сходить, но в том, что я хожу не подходит."
    other emo-985 "Поняла, сейчас принесу."
    scene bg pgn_maxnewclothing_04
    $ renpy.pause (3)
    scene bg pgn_maxnewclothing_05
    m emo-3 "Спасибо."
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_07
    $ renpy.pause(2)
    scene bg pgn_maxnewclothing_06
    $ renpy.pause(2)
    scene pgn_mall_maverick_maxoffice_03
    m emo-0 "Хм... Неплохо. Мне нравится."
    scene pgn_mall_maverick_maxoffice_04
    other emo-984 "С вас $320"
    play sound "content/audio/long_expected.mp3" noloop
    $ renpy.notify(str(task_notifi[11])+" $"+"320")
    $ currency -= 320
    other emo-984 "Спасибо за покупку."
    jump jump_dialogue


label pgn_events_momanal_07:
    "Тук-тук"
    mom emo-60 "Кто там?"
    m emo-1 "Мама, это я. Я хотел бы..."
    mom emo-60 "Уходи, не хочу ни с тобой и ни с кем разговаривать. Мне нужно ещё некоторое время побыть одной."
    m emo-8 "Мам..."
    mom emo-63 "[pname_max[0]], уйди, я не в настроении."
    m emo-13 "Может сходим куда-нибудь вместе?"
    mom emo-69 "И куда хочешь меня пригласить?"
    menu menu_pgn_events_momanal_07:
        "В кинотеатр":
            m emo-0 "Можем сходить в кинотеатр и посмотреть любой фильм, который захочешь."
            mom emo-72 "Сейчас нет в прокате ничего, что мне нравится. Там только одни твои боевики и фантастика."
            jump menu_pgn_events_momanal_07
        "В ресторан":
            m emo-0 "Я заказал столик в ресторане. Можем туда сходить."
            mom emo-66 "Ты уже заказал? Во сколько?"
            if ((("restgn_19") in ivent24 or ("restgn_vip_19") in ivent24) and qtime == 19) or ((("restgn_20") in ivent24 or ("restgn_vip_20") in ivent24) and qtime == 20) or ((("restgn_21") in ivent24 or ("restgn_vip_21") in ivent24) and qtime == 21) or ((("restgn_22") in ivent24 or ("restgn_vip_22") in ivent24) and qtime == 22) or ((("restgn_23") in ivent24 or ("restgn_vip_23") in ivent24) and qtime == 23):
                m emo-13 "Сейчас"
                mom emo-68 "Нет, я спросила не когда ты сделал заказ, а на какое время."
                m emo-0 "Прямо... сейчас..."
                mom emo-66 "Ох, Боже! [pname_max[0]]!"
                mom emo-73 "Какой же ты у меня дурак. Ты понимаешь, что это очень и очень мало времени, чтобы женщине собраться."
                m emo-4 "Так надень, что-нибудь по-быстрому и поедем."
                mom emo-63 "Нет [pname_max[0]], так не пойдёт. В другой раз. Только не забудь об этом мне как можно пораньше сообщить."
                mom emo-69 "Я признательна за старание, но так нельзя."
                m emo-13 "Извини. Может тебе массаж сделаю?"
                m emo-1 "Мам?"
                $ qtime += 1
            if ((("restgn_19") in ivent24 or ("restgn_vip_19") in ivent24) and qtime < 19) or ((("restgn_20") in ivent24 or ("restgn_vip_20") in ivent24) and qtime < 20) or ((("restgn_21") in ivent24 or ("restgn_vip_21") in ivent24) and qtime < 21) or ((("restgn_22") in ivent24 or ("restgn_vip_22") in ivent24) and qtime < 22) or ((("restgn_23") in ivent24 or ("restgn_vip_23") in ivent24) and qtime < 23):
                m emo-0 "Время ещё есть."
                mom emo-68 "А у тебя есть что из одежды? Я не помню, чтобы покупала тебе что-то подобное. А из того что было, уже вырос."
                m emo-3 "Да, я приготовился."
                mom emo-67 "Хорошо. Как буду готова, поедем."
                $ ivent24.append("restgn_mom_true")
            jump jump_dialogue


label pgn_events_momanal_08:
    $ mom_path = 12
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
    mom emo-71 "Вау! Давно не была в подобных заведениях."
    m emo-0 "А я никогда не был."
    mom emo-69 "Он наверное очень дорогой и столик непросто было забронировать."
    if blackcard.have == False:
        m emo-0 "Мне просто повезло. И не волнуйся, я оплачу."
    if blackcard.have == True:
        m emo-3 "Это было не сложно."
    scene pgn_hotel_gn_mom_04_petruha
    other emo-999 "Здравствуйте. Для вашего стола уже готовятся блюда, минут через 10-15 вам принесу. Пока вы ждёте ваш заказ, не желаете чего-нибудь выпить?"
    m emo-0 "Нам два бокала вина..."
    mom emo-62 "Один, бокал. Ему нельзя, он плохо переносит спиртное."
    other emo-999 "Хорошо. Сейчас принесу."
    scene black
    $ renpy.pause(1)
    scene pgn_hotel_gn_mom_05_petruha with dissolve
    if ("restgn_vip_19") not in ivent24 and ("restgn_vip_20") not in ivent24 and ("restgn_vip_21") not in ivent24 and ("restgn_vip_22") not in ivent24 and ("restgn_vip_23") not in ivent24:
        $ restgn_wine += 1
    $ renpy.pause(1)
    mom emo-62 "Спасибо"
    scene pgn_hotel_gn_mom_03_petruha
    show pgn_hotel_gn_mom_03_wine
    m emo-6 "Мам!?"
    mom emo-64 "Тебе ещё рано. И я не позволю тебе пить спиртное. Если не согласен, то сейчас же отсюда уйдём."
    m emo-2 "Ладно, как скажешь."
    mom emo-62 "Вот и хорошо."
    scene pgn_hotel_gn_mom_06_petruha
    $ renpy.pause(2)
    scene pgn_hotel_gn_mom_07_petruha with dissolve
    m emo-13 "Хочу извиниться за тот случай. Прости меня. Я не знал, что ты не в курсе что там будет."
    if ("pf9_nonstop") in accessiv:
        mom emo-73 "Ты мог остановиться, когда я тебя об этом умоляла."
        m emo-8 "Мне действительно очень жаль."
    mom emo-62 "Извинения приняты."
    m emo-1 "Значит мы сможем продолжить съёмки?"
    scene pgn_hotel_gn_mom_07_petruha
    show pgn_hotel_gn_mom_07_wine
    mom emo-69 "Нет, продолжать эти съёмки не будем. Всё же для меня это было очень болезнено, мне не понравилось."
    m emo-0 "Ясно\n{i}Жаль. Попробую вместе с Тётей придумать, как решить проблему.{/i}"
    menu:
        "Предложить ещё вина":
            m emo-0 "Ещё вино будешь?"
            mom emo-62 "[pname_max[0]], спасибо. Но на сегодня мне хватит, сильно напиваться не хочу."
        "Счёт":
            pass
    scene pgn_hotel_gn_mom_08_petruha
    mom emo-75 "[pname_max[0]], пока ты ждёшь счёт, мне нужно отойти в дамскую комнату."
    m emo-3 "Как оплачу, встречу тебя."
    scene pgn_hotel_gn_mom_09
    m emo-6 "{i}Блин! Никак не могу не насмотреться на эту попку. В этом платье я ещё больше её хочу.{/i}"
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
    $ renpy.pause(2)
    scene pgn_hotel_gn_mom_12_petruha
    mom emo-62 "О! [pname_max[0]]. Уже оплатил?"
    m emo-3 "Да, мы можем идти."
    mom emo-62 "Хорошо. А то уже поздно."
    $ qtime += 2
    if qtime >= 24:
        $ qtime = qtime - 24
        $ daysnchange()
    jump loc_pool


label pgn_events_momanal_09:
    $ mom_path = 12.1
    m emo-1 "Кажется поход в ресторан помог поднять настроение маме. Попробуем снова снять фильм?"
    k emo-104 "[pname_max[0]], как ты себе это представляешь?"
    m emo-6 "А что?"
    k emo-100 "Забыл, что в прошлый раз было, хочешь повторения?"
    m emo-13 "Может всё обойдётся?"
    k emo-100 "[pname_max[0]]! Чтобы продолжить съёмки, нужно подготовить твою маму к этому виду секса."
    menu:
        "Попросить [pname_liza[3]]?":
            m emo-3 "Мама проводит уроки, так может [pname_liza[0]] её научит."
            k emo-104 "Да!? А когда спросит у неё от куда такой большой опыт. Кого в армию отправят?"
            m emo-0 "Да, точно."
        "Мне её подготовить?":
            k emo-104 "И как ты себе это представляешь? Есть идеи и продуманный план?"
            m emo-0 "Нет"
            k emo-101 "Вот, так что основную часть оставь на меня. Т.к. частично я тоже виновата перед ней. И у меня опыта побольше."
        "Так же как с [pname_liza[4]]?":
            k emo-101 "Примерно, да. Но только без твоего участия."
            m emo-8 "Почему без меня?"
            k emo-103 "Не будем пугать её твоими размерами. Мне нужно, чтобы она была расслабленной и не о чем не тревожилась. А так, она будет вспоминать только тот случай."
    m emo-0 "Ладно"
    k emo-100 "Сегодня ночью к ней загляну, посмотрим, согласится ли."
    m emo-0 "А если нет?"
    k emo-101 "Тогда проведу с неё столько ночей, сколько понадобится."
    m emo-1 "Хорошо. Скажешь, когда она, ну это, будет готова."
    k emo-101 "Конечно."
    m emo-0 "Спасибо."
    jump loc_pool


label pgn_events_momanal_10:
    if mom_path > 12.1:
        scene n-malone
        m emo-3 "{i}У мамы шикарное тело, прям создано для меня.{/i}"
        "Тукт-тук"
        mom emo-60 "Кто там?"
        scene f95_papersand_momfunwithkira_01
        m emo-1 "{i}А вот и тётя пришла.{/i}"
        k emo-109 "Соскучилась? Не против моей компании?"
        mom emo-67 "Заходи быстрее, не стой на пороге."
    scene f95_papersand_momfunwithkira_02
    if mom_path == 12.1:
        m emo-3 "{i}Фух! Вроде успел.{/i}"
        k emo-112 "Сложно устоять перед этим ротиком, так и хочется тебя поцеловать."
    scene f95_papersand_momfunwithkira_03
    mom emo-68 "Аххх... Ммм... Аххх... "
    scene f95_papersand_momfunwithkira_04
    k emo-108 "Оооо... Ммм... Какая мокрая и горячая киска. Мне разбудить [pname_max[1]]?"
    if mom_path > 12.1:
        m emo-4 "{i}Да, да, да...{/i}"
    mom emo-69 "Давай не будем его будить, пускай спит, отдыхает."
    if mom_path > 12.1:
        m emo-8 "{i}Блин.{/i}"
    k emo-113 "Завтра хорошенько поработает с твоими дырочками... "
    mom emo-71 "Ага... Моя очередь. "
    scene f95_papersand_momfunwithkira_05
    k emo-108 "Аххх... Как приятно... Можешь прикусить один из сосков... Ох!"
    k emo-114 "Боже!!! Ммм... Да... Твои пальчики чудо..."
    scene f95_papersand_momfunwithkira_06
    if mom_path > 12.1:
        m emo-4 "{i}Я бы сейчас пристроился сзади.{/i}"
        k emo-109 "Мммм... Ты так же и [pname_max[1]] целуешь, нежно и страстно?"
        mom emo-73 "Мы с ним не часто целуемся."
        k emo-112 "При встрече так и хочется, чтобы поскорее уже куда-нибудь пристроил своего монстра."
        mom emo-73 "Ты меня прекрасно понимаешь."
    if mom_path == 12.1:
        k emo-104 "Сестрёнка, ты в обиде на меня?"
        mom emo-62 "За что?"
        k emo-100 "Я честно не знала, что тебя поставили на эти съёмки. Прости..."
        mom emo-62 "Не переживай, ты моя любимая сестра, ты бы по своей воле мне такую боль не причинила."
    if mom_path > 12.1:
        scene f95_papersand_momfunwithkira_07
        m emo-2 "{i}Чёрт! Как же сложно удержаться, хочу туда, хочу к ним.{/i}"
        m emo-4 "{i}Нельзя, так нельзя, помастурбирую на них здесь. От таких горячих красавиц и в мороз будет жарко.{/i}"
    scene f95_papersand_momfunwithkira_08
    if pgnach_116.aopen == False:
        $ PGN_Achadd(pgnach_116, 116)
    if mom_path == 12.1:
        k emo-100 "По поводу фильма."
        mom emo-60 "Да, что?"
        k emo-104 "Ты не против, если я помогу тебе с подготовкой к анальному сексу?"
    if mom_path > 12.1:
        k emo-104 "Ты подумала насчёт моих уроков?"
    scene f95_papersand_momfunwithkira_09
    if mom_path > 12.1:
        mom emo-60 "По анальному сексу?"
        k emo-101 "Да. Так что?"
    if mom_path == 12.1:
        mom emo-69 "[pname_kira[6]], может не надо? Мне было очень больно. И у тебя идей и опыта достаточно для написания других сценариев."
        k emo-102 "Это да. Но рано или поздно, обычный секс тебе наскучит и захочется чего-то нового. И [pname_max[0]] не исключение."
        mom emo-71 "То, что когда-нибудь [pname_max[0]] захочет, я не спорю. Но у него же такой большой. Мне сложно осмыслить как он помещается в худенькой попке [pname_alice[1]]."
        k emo-101 "Ладно. В следующий раз поговорим."
        mom emo-60 "Хорошо."
        k emo-108 "Тогда давай вот что сделаем."
    if mom_path > 12.1 and pgn_ach_repeat != 116:
        mom emo-73 "Даже и не знаю..."
        k emo-114 "Как ты сама сказала, у меня большой опыт. Тебе понравится, я обещаю."
        $ label_random = renpy.random.randint ( 1, 5)
        if label_random == 2 or label_random == 4 or "walkthrough_light" in accessiv:
            $ mom_path = 12.3
            mom emo-69 "Ну ладно. Только я сейчас не готова."
            k emo-109 "А я и не говорила, что сейчас. Сейчас нам обеим нужен хорошенький оргазм перед сном."
        else:
            mom emo-69 "Пока не готова к этому."
            k emo-101 "Хорошо. Не буду настаивать, а пока продолжим."
    scene f95_papersand_momfunwithkira_10
    mom emo-69 "Мммм... Аахх..."
    k emo-113 "Твоя киска супер, сестра. Я прям так и чувствую, как она у тебя горит."
    mom emo-71 "Помолчи. Лучше активнее двигай тазом... Мммххмм... Охх..."
    k emo-112 "Мммм..."
    scene f95_papersand_momfunwithkira_11
    mom emo-68 "Аааа... Аааааххх... Да!"
    k emo-114 "Ааааааххх..."
    if mom_path > 12.1:
        scene f95_papersand_momfunwithkira_12
        m emo-4 "{i}О да! Я тоже кончил.{/i}"
    mom emo-75 "Спасибо, что пришла. Может останешься?"
    k emo-101 "Я не против, моя малышка..."
    if mom_path > 12.1:
        m emo-3 "{i}Ага, спасибо тётя, за такое классное шоу. Мне тоже пора уже спать.{/i}"
    if pgn_ach_repeat == 116:
        jump table_pgn_achievement
    if mom_path == 12.1:
        $ mom_path = 12.2
    $ serialpgngame("loc_my_room_sleep")


label pgn_events_momanal_11:
    m emo-3 "Когда начнёшь уроки с Мамой?"
    k emo-104 "Может быть завтра, или после завтра... или..."
    m emo-2 "..."
    k emo-101 "Сегодня ночью и начну."
    m emo-0 "Почему ночью, может быть вечером? И я могу помочь."
    k emo-105 "Я тебе уже говорила, что твоё присутствие может только всё испортить."
    k emo-112 "И у меня есть работа, так что только ночью."
    m emo-0 "Ладно"
    k emo-104 "И [pname_max[0]]. Если придёшь посмотреть, не шуми. Твоя мама должна думать, что мы только одни, вдвоём. Понял?"
    m emo-0 "Да."
    $ mom_path = 12.4
    jump jump_dialogue



label pgn_events_momanal_12:
    scene pgn_momanal_lesson_01_petruha
    m emo-0 "{i}Так, мама здесь, хорошо. Осталось дождаться тётю.{/i}"
    scene pgn_momanal_lesson_03_petruha
    m emo-3 "{i}А вот и учитель.{/i}"
    scene pgn_momanal_lesson_02_petruha
    k emo-104 "Эй, малышка! Ты не спишь? Надеюсь не забыла про наш сегодняшний урок?"
    scene pgn_momanal_lesson_04_petruha
    mom emo-60 "Привет. Не сплю, просто прилегла, конечно помню. Вот приготовилась."
    k emo-103 "А свою узкую анальную дырочку?"
    mom emo-73 "Ну..."
    k emo-101 "Пойдём в ванную, объясню и покажу, как эффективнее всего. Вставай."
    scene pgn_momanal_lesson_18
    $ renpy.pause(3)
    scene pgn_momanal_lesson_05_petruha
    m emo-6 "{i}Так, пока только тётя пришла. Что она там делает, переодевается?{/i}"
    scene pgn_momanal_lesson_06_petruha
    m emo-4 "{i}Ммм... Как тогда с уроками для [pname_liza[1]], тоже так сексуально была одета.{/i}"
    scene pgn_momanal_lesson_07_petruha
    m emo-6 "{i}Она к столу идёт или...{/i}"
    scene pgn_momanal_lesson_08_petruha
    k emo-101 "Привет, сладенький."
    m emo-2 "Я... Это... Тут.. Ну.."
    k emo-104 "Помнишь о чём договаривались? Не издавать ни звука. Хорошо?"
    m emo-3 "Да."
    scene pgn_momanal_lesson_09_petruha
    k emo-101 "[pname_mom[6]], ну что ж ты так долго, я заждалась."
    mom emo-60 "Я ещё несколько раз промыла. Не хотела подставлять грязную попу."
    k emo-109 "[pname_mom[6]], того раза было достаточно для сегодняшнего урока, а так тщательно будешь подготавливать для своего сына."
    mom emo-69 "Ну я подумала..."
    k emo-101 "Давай, садись на кровать."
    scene pgn_momanal_lesson_10_petruha
    k emo-100 "Ещё раз проясним. Ты точно готова и хочешь этого?"
    mom emo-71 "Да, я хочу. И... Раз [pname_max[0]] тоже этого захочет, то я должна быть готова."
    m emo-16 "{i}О да, я очень хочу.{/i}"
    k emo-100 "Хорошо."
    scene pgn_momanal_lesson_11
    k emo-102 "Посмотри внимательно на мою попку. Что там?"
    mom emo-66 "Ох! [pname_kira[0]], у тебя.. там..."
    k emo-101 "Да, в моей попке анальная пробка. Вытащи её, неспеша."
    scene animated pgn_momanal_lesson_01
    k emo-102 "Смелее"
    scene animated pgn_momanal_lesson_01b
    $ renpy.pause()
    scene pgn_momanal_lesson_12_6
    k emo-113 "Оу!"
    mom emo-66 "Ого! Какой он большой."
    k emo-114 "[pname_mom[6]]! Это большой!? Внутри побывали игрушки и побольше и ни чего, всё хорошо. А теперь засунь его обратно и высунь..."
    k emo-101 "Поиграй немного с моей попкой."
    scene animated pgn_momanal_lesson_01с
    $ renpy.pause()
    k emo-101 "Без особых усилий, да?"
    mom emo-60 "Ага."
    scene pgn_momanal_lesson_10_petruha
    if pgnach_117.aopen == False:
        $ PGN_Achadd(pgnach_117, 117)
    k emo-101 "К концу всех наших уроков, [pname_max[0]] сможет без проблем входить в твою дырочку. Больно, не будет, будет только приятно."
    mom emo-73 "Надеюсь."
    k emo-101 "Хорошо. Теперь ложись."
    scene pgn_momanal_lesson_13
    k emo-113 "Немного лубриканта. Если нет лубриканта, то сгодится и слюна. Но если есть смазка, то лучше с ней, вход будет гладким и ощущения иные."
    scene pgn_momanal_lesson_14
    k emo-101 "Пока всего один пальчик. Расслабься."
    scene pgn_momanal_lesson_15
    mom emo-69 "Аххх!! Ммм..."
    k emo-104 "Как ощущения?"
    mom emo-68 "Приятные. Ммм..."
    k emo-108 "Хорошо. Ещё немного, дырочка очень тугая. Туда-сюда..."
    mom emo-73 "Поскорее бы его..."
    k emo-105 "Так, притормози. Забыла, что ли, что было на съёмках!? И это всего один палец. Такая же забывчивая, как и твой сынок."
    scene pgn_momanal_lesson_16_1
    k emo-101 "Ладно, теперь два."
    scene pgn_momanal_lesson_17
    mom emo-75 "Ох! [pname_kira[0]]. Это... так приятно...."
    scene animated pgn_momanal_lesson_02
    $ renpy.pause()
    mom emo-68 "Ахх... Ммм.... Аххх..."
    mom emo-71 "[pname_kira[0]]... Ммм.. Сестра... Я..."
    scene pgn_momanal_lesson_15
    mom emo-66 "Аххххх.... О да...."
    k emo-114 "Ого! Кончила от анальной стимуляции. Вот это неожиданность, сестренка!"
    scene pgn_momanal_lesson_10_petruha
    mom emo-75 "Спасибо тебе, [pname_kira[0]]. Мне очень понравилась."
    k emo-114 "Я рада слышать. Думаю, если бы здесь был [pname_max[0]], он тоже был бы рад."
    k emo-104 "Следующий урок проведем через день, и до этого тебе нужно поработать со своей попкой пальчиками. Хорошо?"
    mom emo-62 "Да."
    k emo-101 "Сейчас выключу свет и повеселимся немного перед сном."
    if pgn_ach_repeat == 117:
        jump table_pgn_achievement
    $ days_mom = days+2
    $ mom_path = 12.5
    $ serialpgngame("loc_my_room_sleep")


label pgn_events_momanal_13:
    scene pgn_momanal_lesson2_01_vezdessushij
    m emo-0 "{i}[pname_kira[1]] пока не видно. Ох Мама, если бы я мог, зашёл сейчас и трахнул.{/i}"
    scene pgn_momanal_lesson2_02_vezdessushij
    k emo-109 "Готова к очередным занятиям?"
    mom emo-67 "Моя попка готова к твоим волшебным пальчикам."
    scene pgn_momanal_lesson2_03_vezdessushij
    k emo-104 "Я вижу. Ты тренировала свою попку, как я просила?"
    mom emo-73 "Да... Моя... Моя госпожа."
    k emo-104 "Госпожа!? Мне нравится. Только вот сегодня в ход пойдут не мои пальчики..."
    mom emo-68 "А что?"
    scene pgn_momanal_lesson2_04_vezdessushij
    k emo-109 "А вот этот красавец."
    mom emo-66 "[pname_kira[0]]! Он в меня не влезет."
    k emo-112 "Отказа не принимаю."
    mom emo-66 "Но..."
    k emo-113 "Ты только что назвала меня госпожой, значит ты моя игрушка и подчиняешься моим приказам."
    mom emo-67 "[pname_kira[0]]! Я пошутила."
    k emo-104 "Не хочешь меня слушаться, значит будешь наказана. Ложись ко мне на колени."
    scene pgn_momanal_lesson2_05_vezdessushij
    mom emo-73 "Может не надо, я буду послушной."
    scene pgn_momanal_lesson2_06_vezdessushij
    $ renpy.pause(1)
    scene pgn_momanal_lesson2_05_vezdessushij
    mom emo-68 "Ай! [pname_kira[0]]! Не надо так сильно."
    scene pgn_momanal_lesson2_06_vezdessushij
    $ renpy.pause(1)
    scene pgn_momanal_lesson2_07_vezdessushij
    mom emo-69 "Ай!"
    scene pgn_momanal_lesson2_06_vezdessushij
    $ renpy.pause(1)
    scene pgn_momanal_lesson2_07_vezdessushij
    mom emo-68 "Ай! Я... всё поняла. До... достаточно."
    scene pgn_momanal_lesson2_06_vezdessushij
    $ renpy.pause(1)
    scene pgn_momanal_lesson2_08_vezdessushij
    mom emo-71 "Аххх... "
    scene pgn_momanal_lesson2_06_vezdessushij
    $ renpy.pause(1)
    scene pgn_momanal_lesson2_08_vezdessushij
    mom emo-73 "Ммм... Ааахххх..."
    scene pgn_momanal_lesson2_09_vezdessushij
    if pgnach_118.aopen == False:
        $ PGN_Achadd(pgnach_118, 118)
    k emo-104 "{i}О! Из её киски сок ручьём течет. Сестрёнка, ты мне кое-кого напоминаешь.{/i}"
    k emo-113 "Отлично. Теперь твоя госпожа займётся этой сочной попкой."
    scene pgn_momanal_lesson2_10_vezdessushij
    k emo-102 "Перед тем, как я буду разрабатывать эту узкую дырочку, мне нужно её хорошенько увлажнить."
    mom emo-60 "У меня нет лубриканта..."
    scene animated pgn_momanal_lesson2_01
    mom emo-73 "Мммм..."
    scene pgn_momanal_lesson2_12_vezdessushij
    l emo-42 "{i}Да где же там опять [pname_max[0]]? Когда нужен, его нет.{/i}"
    scene pgn_momanal_lesson2_13_vezdessushij
    l emo-48 "{i}У мамы дверь приоткрыта. Наверное [pname_max[0]] там.{/i}"
    mom emo-71 "Аххх... Ммм..."
    l emo-44 "{i}Да, определенно там. Моей попки ему недостаточно, сразу к маме.{/i}"
    scene pgn_momanal_lesson2_14_vezdessushij
    l emo-50 "{i}Мама и Тётя [pname_kira[0]]!?{/i}"
    scene animated pgn_momanal_lesson2_01
    l emo-50 "{i}Тётя лижет маме анал!?{/i}"
    mom emo-68 "Ммм... Ммм..."
    l emo-49 "{i}Видимо маме это нравится. Вот бы [pname_max[0]] мне также сделал. Если его здесь нет, тогда где он? Хм...{/i}"
    scene pgn_momanal_lesson2_15_vezdessushij
    l emo-43 "{i}А... вот он где.{/i}"
    scene pgn_momanal_lesson2_16_vezdessushij
    l emo-41 "Помощь не нужна, бра-тик?"
    m emo-9 "А... [pname_liza[0]]! Ты что тут делаешь?"
    l emo-40 "Да вот, проснулась, а тебя нет. Стала тебя искать. А ты вот здесь всяким занимаешься."
    l emo-41 "Не против, если я помогу тебе немного?"
    m emo-3 "Нет, не против."
    scene pgn_momanal_lesson2_17_1_vezdessushij
    mom emo-73 "[pname_kira[0]], помедленней."
    k emo-108 "Тссс. Опять по попе хочешь получить, непослушная девчонка?"
    scene animated pgn_momanal_lesson2_02
    mom emo-68 "Ай! Ай... Ммм... Ахххх..."
    l emo-44 "Мне плохо видно."
    m emo-0 "А я что поделаю. "
    scene animated pgn_momanal_lesson2_03
    k emo-114 "Какая красота. Я сейчас, сбегаю за кое-чем."
    mom emo-66 "[pname_kira[0]], в меня ещё большего размера не влезет."
    scene pgn_momanal_lesson2_16_vezdessushij
    l emo-40 "Что там происходит?"
    m emo-0 "Тётя куда-то убежала, но вроде сказала, что ещё вернётся."
    l emo-40 "Давай встанем в другую позу, чтобы мне и тебе было видно."
    m emo-6 "Как?"
    scene pgn_momanal_lesson2_19_vezdessushij
    l emo-41 "Так вместе сможем смотреть и удовольствие получим оба."
    scene pgn_momanal_lesson2_20_vezdessushij
    k emo-114 "А вот и я, кое–что принесла."
    k emo-100 "О!"
    scene pgn_momanal_lesson2_21_vezdessushij
    mom emo-62 "Что такое?"
    k emo-109 "Всё хорошо, просто показалось. \n{i}Ну детишки, совсем не могут сдержаться, ох молодость.{/i}"
    k emo-101 "Устраивайся поудобнее, сейчас вместе насладимся этим длиннющим дилдо."
    scene pgn_momanal_lesson2_22_vezdessushij
    k emo-103 "Минуточку, сейчас... Теперь двигай попкой, сестренка."
    scene animated pgn_momanal_lesson2_04
    $ renpy.pause()
    menu menu_pgn_events_momanal_13_both:
        "[pname_liza[0]] и [pname_max[0]]":
            scene animated pgn_momanal_lesson2_05
            $ renpy.pause()
            jump menu_pgn_events_momanal_13_both
        "Тётя [pname_kira[0]] и Мама":
            scene animated pgn_momanal_lesson2_04
            $ renpy.pause()
            jump menu_pgn_events_momanal_13_both
        "далее":
            pass
    scene animated pgn_momanal_lesson2_05b
    $ renpy.pause (2)
    l emo-41 "Спасибо, братик."
    scene pgn_momanal_lesson2_24_7_vezdessushij
    mom emo-75 "Спасибо, это было потрясающе."
    k emo-101 "Всё что угодно для моей любимой сестрёнки. Если захочешь, я могу тебя обучить и на тренировать на любой секс, который захочешь или на который захочет [pname_max[0]]."
    k emo-109 "[pname_mom[7]], теперь твоя попка точно сможет принять член твоего сына."
    mom emo-73 "Я... я.. думаю что ещё пока не готова для анала с ним."
    k emo-114 "[pname_mom[7]].... Хорошо. Я оставлю тебе тот дилдо, потренируешься ещё сама."
    mom emo-75 "Спасибо."
    if pgn_ach_repeat == 118:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_liza, 1, 0, 0, 0, 0)
    $ mom_path = 12.6
    $ serialpgngame("loc_my_room_sleep")


label pgn_events_momanal_14:
    $ mom_path = 12.7
    k emo-101 "Твоя Мама готова к анальному сексу, я сделала всё что могла. Дальше всё зависит от тебя."
    m emo-0 "Мне нужно что-то ещё делать?"
    k emo-114 "Думал, что я проведу уроки, а она после сразу накинется и позволит войти, твоему большому и огромному члену, в её попку?"
    m emo-13 "Ну да."
    k emo-109 "Твоя Мама всё ещё в сомнениях и неуверена, что всё продёт гладко. Т.е физически она готова, но не морально."
    m emo-0 "Мне снова сводить её в ресторан?"
    k emo-104 "Возможно."
    m emo-0 "Ладно, что-нибудь придумаю. Спасибо снова за помощь. Буду должен."
    jump jump_dialogue


label pgn_events_momanal_15:
    $ pornstudio_path = 8
    m emo-4 "Когда можем приступить к съёмкам?"
    k emo-107 "И ты тоже. [pname_liza[0]] мне уже все уши протрещала."
    k emo-104 "У тебя получилось, с мамой?"
    m emo-3 "Да. Поэтому и спрашиваю."
    k emo-104 "Тогда думаю можно, в те дни, когда у твоей мамы проходят съёмки."
    m emo-6 "Почему только в те дни?"
    k emo-100 "Во-первых, [pname_mom[0]] будет уверена, что её дочь дома."
    k emo-100 "Во-вторых, мы все будем в одном павильоне и я смогу её задержать, чтобы у вас, детки, было время на переодевание."
    m emo-6 "Вроде бы понял."
    k emo-101 "Надеюсь Увидимся на съёмочной площадке."
    jump jump_dialogue


label mod5_momyoga_analsex:
    scene f95_papersand_momanalyoga_01
    mom emo-60 "[pname_max[0]], смотри внимательно, что и как я делаю, тогда у тебя всё получится."
    m emo-4 "{i}Ага, я смотрю и очень внимательно.{/i}"
    scene f95_papersand_momanalyoga_02
    mom emo-62 "А теперь потянем мышцы спины"
    m emo-9 "Блин!!!"
    scene f95_papersand_momanalyoga_03
    mom emo-66 "[pname_max[0]]! Что случилось?"
    scene f95_papersand_momanalyoga_04
    m emo-2 "Судорога в ноге."
    mom emo-60 "Это потому что ты мало со мной занимаешься йогой. Вот если бы каждый день этот делал, то такого не произошло."
    scene f95_papersand_momanalyoga_05
    m emo-13 "Может я пойду?"
    mom emo-60 "Нет, вставай и попробуем другую позу."
    scene f95_papersand_momanalyoga_06
    mom emo-60 "Ноги расставь чуть более ширины плеч."
    m emo-4 "{i}Сиськи... Мамины сиськи...{/i}"
    scene f95_papersand_momanalyoga_07
    mom emo-60 "А теперь тянемся и растягиваем свои мышцы, растягиваем и растягиваем."
    m emo-3 "{i}Есть идея, какие ещё мышцы я могу растянуть.{/i}"
    scene f95_papersand_momanalyoga_08
    if pgnach_126.aopen == False:
        $ PGN_Achadd(pgnach_126, 126)
    mom emo-73 "[pname_max[0]], ты чего там делаешь? Ты ещё не закончил с зарядкой."
    m emo-4 "{i}А вот и мамина дырочка.{/i}"
    scene f95_papersand_momanalyoga_09
    mom emo-66 "Ох! [pname_max[0]]!"
    scene f95_papersand_momanalyoga_10
    mom emo-71 "Ммм... Хорошо. Такие упражнения нам обоим на пользу."
    scene f95_papersand_momanalyoga_11
    mom emo-68 "Аааххх... Ахх.. Да... [pname_max[0]], да, да... Глубже..."
    mom emo-71 "Да, малыш... Вот так, трахай мамочку..."
    m emo-2 "Ой! Сейчас кончу."
    mom emo-68 "Только не в попу!"
    scene f95_papersand_momanalyoga_12
    m emo-12 "Аргх... Аааа...."
    scene f95_papersand_momanalyoga_13
    mom emo-69 "Я же попросила не кончать внутрь."
    m emo-13 "Ну немного попало. Ничего страшного."
    scene f95_papersand_momanalyoga_14
    mom emo-72 "Теперь придётся потратить время в ванной, а мне ещё завтрак готовить."
    m emo-13 "Так тебе не понравилась моя зарядка?"
    mom emo-62 "Понравилось, понравилась. Беги в душ, а потом я."
    if pgn_ach_repeat == 126:
        jump table_pgn_achievement
    $ PGN_Addstatsex(stat_mom, 1, 0, 0, 0, 0)
    $ ivent24.append("momyogasex")
    $ qtime += 1
    jump loc_pool
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
