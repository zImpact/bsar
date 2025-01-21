label bsar_insomnia_day1:
    $ bsar_set_time("night")
    stop music fadeout 3
    scene bg black with Dissolve(3)
    $ bsar_new_chapter("Бессонница.", "День первый.")
    $ bsar_set_mode_nvl()
    scene bg bsar_prolog_blue with Dissolve(3)
    $ renpy.pause(1, hard=True)
    play music bsar_domitori_taranofu_slow_pulse fadein 3
    bsar_narrator "{i}В этом мире есть множество вещей, которые нельзя объяснить. {w}Их невозможно понять, невозможно увидеть и доказать, тем не менее они существуют.{/i}"
    bsar_narrator "{i}Сон — одна из этих вещей.{/i}"
    bsar_narrator "{i}Ещё наши предки считали, что во время сна душа может покидать физическое тело и, пересекая тонкую, невидимую человеческому глазу грань, путешествовать в другие миры.{/i}" 
    bsar_narrator "{i}Поэтому, никто не может гарантировать Тебе, что вся Твоя жизнь — это не сон. {w}Сон, в котором пленённое тело переживает подобные друг другу дни снова и снова. Бесчисленное число раз...{/i}" 
    $ renpy.pause(1, hard=True)
    $ bsar_set_time("bw", "day")
    scene bg bsar_prolog_bw
    show bsar_she normal
    show bsar_static_noise_anim
    with bsar_flash
    play ambience bsar_hum fadein 2
    nvl clear
    bsar_she "Ты..."
    bsar_she "Ты должен..."
    bsar_she "Если ты вспомнишь, что я тогда сказала..."
    bsar_she "Ты должен вспомнить!"
    bsar_he "Кто ты? Что я должен вспомнить?"
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with bsar_flash
    $ bsar_set_time("day")
    nvl clear
    play ambience ambience_int_cabin_day fadein 2
    play sound_loop bsar_alarm_clock fadein 2 
    bsar_narrator "От громкого звона будильника создаётся впечатление, что мне в голову вбивают гвозди. Этот противный звон эхом распространяется по всей комнате, заставляя меня сделать хоть что-то."
    hide blink 
    scene bg bsar_int_house_of_mt_day_blurred behind blink 
    show unblink 
    $ renpy.pause(2, hard=True)
    stop sound_loop fadeout 2 
    bsar_narrator "Брошенная наотмашь подушка заставила замолкнуть эту адскую машину." 
    bsar_narrator "Чувствую себя потерянным, словно старая безделушка, которая ранее, по идее, приносила удачу, а сейчас пылится где-то под диваном, ожидая, когда кто-то случайно её найдёт." 
    play sound_loop bsar_knock fadein 2
    scene bg int_house_of_mt_day with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    bsar_narrator "Резкий стук в дверь возвращает меня в реальность. Раз, другой, третий."
    show blink
    $ renpy.pause(2, hard=True)
    bsar_narrator "Я накрываюсь одеялом с головой в надежде, что этот незваный гость просто уйдёт." 
    stop sound_loop fadeout 2 
    bsar_narrator "Через какое-то время стук прекращается. Похоже, мой экзекутор смирился со своим поражением." 
    bsar_narrator "Но как ни крути, думать, что я скоро снова засну, было очень наивно с моей стороны. {w}Я ворочаюсь с бока на бок, но сон так и не приходит."
    hide blink
    show unblink
    $ renpy.pause(2, hard=True)
    bsar_narrator "Посмотрев на часы, я замечаю, что давно проспал завтрак, и мне придётся ходить голодным до самого обеда."
    bsar_th "Человек, который первым сказал, что утро добрым не бывает, был абсолютно прав."
    nvl clear
    play sound sfx_open_door_1
    $ renpy.pause(2, hard=True)
    stop ambience fadeout 2
    scene bg bsar_ext_houst_of_mt_winter_day with dissolve
    play ambience bsar_winter_wind fadein 2
    $ renpy.pause(1.5, hard=True)
    scene bg bsar_ext_houses_winter_day with dissolve
    $ renpy.pause(1.5, hard=True)
    scene bg bsar_ext_square_winter_day with dissolve
    $ renpy.pause(1.5, hard=True)
    bsar_narrator "Я более или менее привёл себя в порядок и не нашёл занятия лучше, чем посиделки на площади вместе с товарищем Гендой, который всё таким же каменным и тотально безучастным взглядом смотрел в пустоту."  
    bsar_narrator "Устроившись на самой дальней скамейке, я попытался понять, что за чертовщина стала мне сниться. Кошмары? Может быть. Ничего не могу вспомнить."  
    bsar_narrator "Вроде бы уже почти ухватился за что-то важное, значимое, как это что-то упорхнёт от меня, взмахнув крыльями, подобно Жар-птице." 
    bsar_narrator "Вдруг краем глаза я заметил, что рядом со мной кто-то стоит."  
    bsar_narrator "Я непроизвольно вздрогнул, что вызвало ехидный смешок у заставшей меня врасплох пионерки." 
    $ bsar_set_mode_adv() 
    show bsar_us normal with dissolve
    play music bsar_afternoon fadein 4
    bsar_narrator "Ульяна. Девочка-апокалипсис." 
    bsar_narrator "Из-за её детской непосредственности мы не раз встревали в разного рода авантюры, и почти всегда нам приходилось отдуваться." 
    bsar_narrator "Но всё же, несмотря на все ее проделки, на неё решительно невозможно злиться. И я покривлю душой, если скажу, что мне с ней не весело."
    bsar_protagonist "И давно ты здесь стоишь, Ульяна?" 
    bsar_us "Ты вообще когда-нибудь улыбаешься?" 
    bsar_protagonist "Да. {w}Наверное." 
    bsar_us "Как так вообще можно жить? Почему ты уже второй день ходишь с кислой миной? Сторонишься всех, а вчера вообще прошёл мимо и даже не поздоровался!" 
    bsar_narrator "Ульяна интересуется моим состоянием. Один этот факт уже вызывает массу подозрений, но что-то в её взгляде ясно даёт понять — ей и вправду это интересно." 
    bsar_protagonist "Извини, Уль. Просто чертовски скверное настроение в последнее время." 
    bsar_narrator "Но я же не соврал. Просто сказал не всю правду."
    bsar_us "Э-эй! Вообще-то человек настроение сам себе делает. Никто, кроме тебя, его тебе не сделает. Как ты сам для себя решил, так и будет!"
    bsar_us "Вот если ты сам для себя решил: «Всё. Мне весело!», — то тебе весело, а если ты решил, что тебе грустно, так и будет."
    bsar_narrator "Голубые глаза девушки горят энтузиазмом, словно она Уоллес, говорящий воодушевляющую речь перед сынами Шотландии. Причём в несвойственной для себя простодушной манере."
    bsar_narrator "Поэтому, я с неподдельным интересом и заинтересованностью слушаю её наставляющий монолог." 
    bsar_us "Вроде и старше меня, но до сих пор не понял этого..."
    bsar_us "Улыбнись, дурак!" 
    bsar_narrator "Как ни странно, но от слов этой рыжеволосой энергичной девчонки на сердце стало... {w}Теплее что ли. Эти слова колыхнули фибры души, напоминая о каком-то совсем позабытом чувстве."
    show bsar_us dontlike with dspr
    bsar_narrator "Я искренне улыбнулся Ульяне, получив такую же, но более озорную улыбку в ответ, которая почему-то сменилась лёгким румянцем на щеках и убегающим куда-то взглядом."
    bsar_narrator "А может мне просто показалось."
    play sound sfx_dinner_horn_processed fadein 2
    $ renpy.pause(3, hard=True)
    bsar_narrator "Неловкую паузу прервал горн. Пора на обед."
    show bsar_us normal with dspr
    bsar_us "Пошли на обед, дурак. Завтрак, как я понимаю, ты проспал."
    hide bsar_us with dissolve
    bsar_narrator "Хихикнула она и быстро зашагала в сторону столовой. Мне пришлось поторопиться, чтобы не отставать."
    stop music
    play sound_loop bsar_heart
    scene bg bsar_ext_square_winter_day:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1 zoom 1.05

        parallel:
            ease 1 xalign 0.48
            ease 1 xalign 0.52
            repeat

        parallel:
            ease 1.5 rotate 1.5 zoom 1.05
            ease 1.5 rotate -1.05 zoom 1.035
            repeat

    $ bsar_heartbeat_animation("bg bsar_ext_square_winter_day", 1.05, 1.0)
    bsar_narrator "Неожиданно перед глазами всё пошло кувырком..." 
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    stop music fadeout 2
    $ bsar_set_time("bw", "day")
    scene bg bsar_ext_winter_park
    show bsar_snow_layer3_anim
    show bsar_snow_layer2_anim
    show bsar_she normal
    show bsar_snow_layer1_anim
    show bsar_snow_layer0_anim
    show bsar_static_noise_anim
    with bsar_flash
    play sound_loop bsar_hum fadein 2
    play ambience bsar_winter_wind fadein 2
    play music bsar_lucas_king_hurt fadein 2
    bsar_he "Холодно же! Хватит! Выкинь! Выкинь снежок, кому говорю?" 
    bsar_she "Ладно, ладно." 
    bsar_he "Ты когда-нибудь станешь менее инфантильной?" 
    bsar_she "Не стану. К тому же, разве это что-то плохое?"  
    bsar_he "Ну вот. Опять эта ехидная улыбка! На тебя просто невозможно злиться."  
    bsar_she "А на меня и не нужно злиться, дурак."
    bsar_she "Ты, кстати, уже решил, что подаришь сестре на день рождения?" 
    bsar_he "Всё ещё думаю." 
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    stop music fadeout 2
    $ bsar_set_time("day")
    scene bg bsar_ext_square_winter_day
    show bsar_us sad at center
    with bsar_flash
    play ambience bsar_winter_wind fadein 2
    play sound_loop bsar_heart
    $ bsar_heartbeat_animation("bg bsar_ext_square_winter_day", 1.02, 1.0)
    $ bsar_heartbeat_animation("bsar_us sad", 1.02, 1.0)
    play ambience bsar_winter_wind fadein 2
    bsar_us "Эй, как можно было на ровном месте упасть?" 
    bsar_narrator "Что это, чёрт побери, было? Я упал и..." 
    bsar_narrator "Не помню. Наверное, просто показалось."
    stop sound_loop fadeout 2
    scene bg bsar_ext_square_winter_day
    show bsar_us sad
    with Dissolve(1.5)
    bsar_us "А-у-у! Ты там живой? Может мне вожатую позвать?" 
    bsar_protagonist "Всё в порядке. Я просто поскользнулся и упал." 
    bsar_us "Припадочный ты какой-то. Хватит валяться!"
    show bsar_us normal with dspr
    bsar_narrator "Ульяна улыбалась, но по беспокойному взгляду и едва заметным ноткам волнения в голосе можно понять, что она переживает за меня. Это... мило."
    scene bg bsar_ext_dining_hall_away_winter_day with dissolve 
    bsar_narrator "По мере приближения к столовой вокруг появляется всё больше и больше пионеров, совершающих своё голодное паломничество. Ульяна не стала меня ждать и поспешно ретировалась." 
    scene bg bsar_ext_dining_hall_near_winter_day with dissolve 
    bsar_narrator "Зазевавшись, я едва не сталкиваюсь с Алисой Двачевской, которую за глаза все называют ДваЧе." 
    show bsar_dv normal with dissolve
    play music bsar_ease fadein 2
    bsar_dv "Эй! Смотри куда прёшь!" 
    bsar_narrator "Алиса была не в настроении, но мастерски скрывала это за надменным выражением лица. Ещё чуть-чуть и она буквально испепелит меня взглядом."
    bsar_protagonist "Что-то случилось?" 
    show bsar_dv normal2 with dspr 
    bsar_narrator "Она на мгновение удивлённо вскинула бровь."
    bsar_narrator "Хоть постороннему человеку это будет незаметно, но за время проведённое здесь, тени злости и обиды на лице этой пионерки ясны мне как гримасы боли." 
    bsar_narrator "По началу она казалась мне типичной хулиганкой из-за любви к всякого рода подколкам и нежеланию следовать правилам лагеря." 
    bsar_narrator "Сейчас я понимаю, что она на самом деле добрая и наивная девушка, хоть и прячется под личиной хулиганки." 
    bsar_narrator "Причины её напускного образа мне, к сожалению, не ясны." 
    show bsar_dv normal with dspr
    bsar_dv "Ольга случилась! Приехала из райцентра сама не своя. Наорала на меня из-за..."
    bsar_dv "Уф. Забудь. {w}Испортила мне всё настроение, чтоб её!" 
    bsar_protagonist "Да будет тебе! Она же постоянно всех гоняет. Не стоит зацикливаться на этом и портить себе настроение." 
    bsar_narrator "Я тепло улыбнулся Алисе. Не стоит ожидать, что я получу от неё улыбку в ответ, но всё же на её лице не осталось и следа обиды." 
    bsar_dv "Кто бы говорил. Сам то несколько дней уже ходишь с таким лицом, что у Лены цветы на подоконнике от твоего взгляда завяли." 
    bsar_th "Похоже, что не одна Ульяна заметила изменения в моём поведении из-за этих ночных кошмаров. Вспомнить бы, что мне снится, раз это так влияет на моё состояние." 
    bsar_protagonist "Как видишь, теперь я в полном порядке." 
    bsar_narrator "Сказал я, улыбнувшись ещё шире и пожав плечами." 
    bsar_protagonist "А цветы могли и из-за холода завянуть. Зачем она их вообще с собой привезла?" 
    bsar_dv "Сам её и спроси, если интересно." 
    bsar_narrator "Сквозь зубы сказала она."
    bsar_th "Точно! Алиса же постоянно надоедает Ольге Дмитриевне из-за того, что их поселили вместе с Леной. Возможно, именно из-за очередной просьбы о расселении и сорвалась вожатая." 
    bsar_th "Не понимаю, почему она так упёрлась и не хочет их расселить, ведь даже Ульянка пару проказ устроила, как раз из-за того, что её поселили со Славей, а не Алисой." 
    bsar_th "Кстати, а зачем Ольга вообще ездила в Райцентр?" 
    bsar_dv "Приём! Ты куда уставился то? Опять ворон считаешь?"
    bsar_dv "Холодно тут. Пошли в столовую. Не хочу ещё и обед пропустить." 
    bsar_protagonist "А? Да, конечно. Пошли." 
    stop ambience fadeout 2 
    stop music fadeout 2 
    scene bg bsar_int_dining_hall_winter with dissolve 
    play ambience ambience_dining_hall_empty fadein 2 
    bsar_narrator "Из-за нашей задержки столовая заметно опустела. Почти все пионеры, отобедав, убежали по своим делам. Взяв еду, мы с Алисой разделились." 
    bsar_narrator "Что-то буркнув себе под нос, она села за столик с Ульяной, по взгляду которой можно было понять, что скоро в лагере случится что-то очень нехорошее." 
    bsar_narrator "Получив порцию, я сел за ближайший свободный столик."  
    bsar_narrator "Несмотря на то, что я не ел с самого утра, аппетита практически не было. Самозабвенно ковыряясь вилкой в тарелке, решил вернуться к этим странным снам." 
    bsar_narrator "Уже третий день я не высыпаюсь по ночам, а наутро чувствую себя просто отвратительно. Было ли такое раньше? Странно. Ничего не могу вспомнить."
    bsar_narrator "Я приехал в лагерь примерно две недели назад..."
    show bsar_sl normal with dissolve
    bsar_sl "Ты не против, если я присяду?" 
    bsar_protagonist "Ч-что?" 
    bsar_sl "Я присяду?" 
    bsar_protagonist "А, конечно-конечно."
    scene bg bsar_sl_normal with dissolve
    play music bsar_stride fadein 4
    bsar_sl "Ты последние дни слишком рассеянный. Завтрак сегодня пропустил и дверь не открыл, когда я стучалась. Проблемы со сном?"
    bsar_narrator "Славяна опустила брови и посмотрела на меня негодующим взглядом." 
    bsar_narrator "Она добрая, активная и ответственная девушка, которая всегда готова помочь. Как раз является помощницей Ольги, что вполне ожидаемо. {w}Правда, некоторые случайно обронённые слова или действия ставят под сомнение искренность её действий." 
    bsar_narrator "Я устало вздыхаю и опускаю подбородок на ладони, вспоминая, как плохо сегодня спал." 
    bsar_protagonist "Да. В последнее время мне снятся кошмары."
    scene bg bsar_sl_tired with dissolve
    bsar_narrator "Славяна немного дёргает головой, словно хочет что-то сказать, но не решается. Она выглядит... {w}уставшей."
    bsar_protagonist "Ты не знаешь, зачем Ольга Дмитриевна ездила в райцентр?" 
    bsar_sl "Она поехала забрать почту, но, кажется, у неё там ещё какое-то {i}личное дело.{/i} Правда, по приезде она сама не своя." 
    bsar_protagonist "В смысле?" 
    bsar_sl "Ну-у. Раздражительная какая-то стала. На Алису накричала." 
    bsar_narrator "В этот момент мимо нашего стола прошли Ульяна с Алисой, и, услышав своё имя, ДваЧе очень недобро глянула на Славю." 
    bsar_narrator "Похоже, у рыжей конфликт не только с Леной; наверное, здесь причина неприязни скрывается в чрезмерной правильности моей собеседницы." 
    bsar_protagonist "Ты тоже неважно выглядишь..." 
    bsar_narrator "Чёрт! Какую же глупость я только что сморозил. Такое нельзя говорить девушке!" 
    bsar_sl "Да-а, наверное, так и есть." 
    bsar_sl "Замоталась в последнее время. Нужно отдохнуть. Я всё же в лагере или где?" 
    bsar_narrator "Мне показалось, что в её глазах промелькнул блеск, который до этого я видел только у Ульяны, когда она хочет влезть в какую-то авантюру." 
    bsar_protagonist "Это славно." 
    bsar_narrator "Я участливо улыбнулся и кивнул." 
    bsar_sl "Ладно. Тогда я пойду. Увидимся!"
    scene bg bsar_int_dining_hall_winter with dissolve
    bsar_protagonist "Да, давай." 
    bsar_narrator "Наверное, мне тоже стоит идти, иначе просижу в столовой до ужина..."
    stop music fadeout 1
    stop ambience fadeout 1
    $ bsar_set_time("bw", "day")
    scene bg bsar_ext_winter_street
    show bsar_snow_layer3_anim
    show bsar_snow_layer2_anim
    show bsar_sister normal
    show bsar_snow_layer1_anim
    show bsar_snow_layer0_anim
    show bsar_static_noise_anim
    with bsar_flash
    play ambience bsar_winter_wind fadein 2
    play sound_loop bsar_hum fadein 2
    play music bsar_lucas_king_isolation fadein 2
    bsar_he "Будешь праздновать день рождения в этом году?"  
    bsar_sister "Да. Возьму отпуск и поеду к родителям, отдохну и маму с папой увижу. Что-то я замоталась с этой работой."  
    bsar_he "Там же ещё лес рядом. Опять будешь в нём пропадать?" 
    bsar_sister "Да-а. Как в детстве, когда за грибами в конце лета ходили. Помнишь?"  
    bsar_he "Помню. Только я никогда это не любил."
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    stop music fadeout 2
    $ bsar_set_time("day")
    scene bg bsar_int_dining_hall_winter with bsar_flash
    play ambience ambience_dining_hall_empty fadein 2
    bsar_narrator "Ничего не понимаю. Что со мной происходит? Уже второй раз перед глазами всплывают образы, которые пропадают также быстро, как и появляются." 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1)
    $ renpy.pause(1, hard=True)
    scene bg bsar_ext_houses_winter_day
    show bsar_heavy_snow_day
    show bsar_normal_snow_day
    with Dissolve(1)
    play ambience bsar_winter_wind fadein 2
    bsar_mt "Пионер!"
    show bsar_mt rage behind bsar_normal_snow_day with dissolve
    bsar_protagonist "Да? Что? Где?"
    bsar_narrator "Довольно резко прозвучавший рядом голос Ольги Дмитриевны выбил меня из колеи, спутав ход мыслей."
    bsar_mt "Я знаю, что ты сегодня не пришёл на завтрак и, по всей видимости, поздно проснулся! Я надеюсь, ты понимаешь, что такое поведение не подобает настоящему пионеру?"
    bsar_narrator "Ольга сегодня и вправду какая-то взвинченная. Я редко слышал, чтобы она повышала голос, как сейчас."
    bsar_narrator "Да, конечно, она пытается быть строгой с пионерами. {w}Но ключевое слово — пытается."
    bsar_narrator "Например, она позволяла мне некоторые вольности, относясь со снисхождением к моим пропускам утреннего построения и далёкого от расписания подъёму."
    bsar_protagonist "Да, извините, больше не повторится."
    bsar_mt "Отлично! Осознание проблемы — половина её решения!"
    bsar_protagonist "Да, конечно."
    show bsar_mt angry behind bsar_normal_snow_day with dspr
    bsar_mt "Раз ты сейчас ничем не занят, то..."
    bsar_narrator "В раздумьях она играет локоном своих волос, пытаясь придумать мне поручение."
    bsar_protagonist "Пионер понял, что ему нужно найти социально полезное занятие!"
    bsar_narrator "Прервал я её размышления, пока она не придумала мне что-то тяжёлое и энергозатратное."
    stop ambience fadeout 2
    scene bg black with Dissolve(1)
    $ bsar_set_time("night")
    scene bg int_house_of_mt_night with Dissolve(1)
    play ambience ambience_medstation_inside_night fadein 2
    play music bsar_domitori_taranofu_trouble fadein 2
    bsar_narrator "Я уставился в потолок, словно пытаясь найти там хоть каплю мотивации. Из-за всей этой мыслительной деятельности я чувствую себя как выжатый лимон."
    bsar_narrator "Может быть, выйти на прогулку и, просто ни о чём не думая, подышать свежим воздухом? Хотя, с другой стороны, я обещал Ольге заняться чем-то полезным."

    menu: 
        "Пойти на прогулку": 
            $ bsar_insomnia_day1_stroll = True 
            jump bsar_insomnia_day1_stroll

        "Убраться в домике": 
            $ bsar_insomnia_paradise_ending_v += 1 
            jump bsar_insomnia_day1_cleaning

label bsar_insomnia_day1_cleaning: 
    $ renpy.block_rollback()
    $ persistent.sprite_time = "day"
    bsar_narrator "Так! Я обещал, что сделаю, значит сделаю!"
    bsar_narrator "Бегать по лагерю и искать себе занятие я не хочу, поэтому просто уберусь в домике."
    scene bg black with Dissolve(1)
    $ renpy.pause(0.5, hard=True)
    scene bg int_house_of_mt_night with Dissolve(1)
    bsar_narrator "Спустя тридцать минут, я смог привести свою обитель в более или менее презентабельный вид."
    bsar_narrator "Я уже заканчивал, как мне попался на глаза листок, валяющийся под кроватью Ольги. Любопытство взяло верх, и я решил прочесть его содержимое."
    $ bsar_set_mode_nvl()
    bsar_narrator "{i}Оля! Мне бесконечно жаль, что приходится писать тебе об этом. Жаль, что наши отношения больше не те, какими они были раньше — ласковыми, теплыми, нежными.{/i}"
    bsar_narrator "{i}Да ты и сама всё прекрасно видишь... Видишь, как мы отдалились друг от друга, как наши чувства угасают с каждым днём. Об этом говорит и редкость наших встреч, и холод в наших голосах...{/i}"
    bsar_narrator "{i}Да чёрт, даже этот лагерь, в который я так настойчиво просил тебя не ехать, хватаясь за каждую соломинку, чтобы сохранить наши отношения! Но, видимо, ты в этом не слишком заинтересована.{/i}"
    bsar_narrator "{i}Я больше не могу так.{/i}"
    bsar_narrator "{i}Холод с твоей стороны постепенно сделал бесчувственным по отношению к тебе и меня самого.{/i}"
    bsar_narrator "{i}Я больше не хочу называть тебя своей, не хочу вдыхать запах твоих волос, который раньше казался приятнее любого изысканного парфюма, не хочу слышать твой голос.{/i}"
    bsar_narrator "{i}Да, Оля, наверное, ты уже и сама всё поняла...{w} Я последний трус, раз не смог сказать тебе это вживую, но у меня есть другая девушка.{/i}"
    bsar_narrator "{i}Желаю тебе тоже обрести свое счастье, несмотря на то, что ты могла просто его не терять. {w}Прощай.{/i}"
    $ bsar_set_mode_adv() 
    bsar_narrator "Во дела-а-а. Так вот в чём дело!"
    bsar_narrator "Если честно, то я даже не знаю, что думать."
    bsar_narrator "Это письмо явно стало ударом для Ольги Дмитриевны и теперь понятно, почему она ходила такая злая."
    bsar_narrator "Я быстро положил письмо обратно и лег на кровать."
    bsar_th "Думаю, что впредь, нужно относиться к вожатой более терпимо что ли. Ей сейчас точно не легко."
    show blink
    $ renpy.pause(2, hard=True)
    scene bg black
    hide blink
    $ bsar_set_time("bw", "day")
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg bsar_ext_roof behind blink
    show bsar_snow_layer3_anim_quick
    show bsar_snow_layer2_anim_quick
    show bsar_she normal
    show bsar_snow_layer1_anim_quick
    show bsar_snow_layer0_anim_quick
    show bsar_static_noise_anim
    with bsar_flash
    play ambience bsar_winter_wind fadein 2
    play sound_loop bsar_hum fadein 2
    play music bsar_flashback_music1 fadein 2
    bsar_she "Так и знала, что найду тебя здесь!"
    bsar_he "Неужели я настолько предсказуем?"
    bsar_she "Нет. Конечно нет. Просто ты мне сам как-то рассказывал, что тебе здесь нравится из-за...{w=1.0}{nw}"
    bsar_he "Из-за того, что тут очень спокойно."
    bsar_she "И очень холодно."
    bsar_she "Значит, завтра ты всё-таки уезжаешь?"
    bsar_he "Да..."
    bsar_he "Завтра я уезжаю."
    bsar_she "Я буду ждать. Только не забывай о..."
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    $ bsar_set_time("night")
    scene bg int_house_of_mt_night
    show bsar_mt grin at center
    with bsar_flash
    play ambience ambience_medstation_inside_night fadein 2
    bsar_mt "О, вижу, ты прибрался!"
    bsar_mt "Молодец!"
    bsar_protagonist "А-а..." 
    bsar_protagonist "Да, прибрался. Я же обещал заняться делом." 
    bsar_th "Я заснул... {w}Или это был не сон?" 
    bsar_th "Уф. Откровенно говоря, меня уже воротит от всех этих странных видений."
    bsar_th "Может не стоит лезть во всё это? Как говорил знакомый мой покойничек: Я много знал..." 
    bsar_protagonist "Ольга, а..." 
    bsar_protagonist "Ой! То есть Ольга Дмитриевна, что-то сегодня случилось?"
    show bsar_mt sad with dspr
    bsar_mt "Это так заметно?" 
    bsar_narrator "Грустно улыбнулась она." 
    bsar_protagonist "Немного. Вы, главное, не расстраивайтесь сильно, если случилось что-то плохое. Ведь плохое всегда рано или поздно заканчивается." 
    bsar_narrator "Я тепло ей улыбнулся. Ольга удивлённо вскинула брови, наклонила голову вбок и о чём-то задумалась." 
    bsar_mt "Возможно ты прав. Ладно. Думаю, что тебе стоит лечь спать пораньше. Негоже пропускать завтрак." 
    bsar_protagonist "Да, конечно."
    show blink
    $ renpy.pause(2, hard=True)
    scene bg black
    hide blink
    bsar_narrator "На меня и вправду накатила сильная усталость и, как только голова коснулась подушки, я моментально заснул." 
    stop ambience fadeout 2
    $ renpy.pause(3, hard=True) 
    jump bsar_insomnia_day2

label bsar_insomnia_day1_stroll: 
    $ renpy.block_rollback()
    bsar_narrator "Ай! Да и чёрт с ним. Не думаю, что она вообще вспомнит об этом. Мне явно стоит проветриться."
    play sound sfx_open_door_1
    $ renpy.pause(2, hard=True)
    stop ambience fadeout 2
    scene bg bsar_ext_house_of_mt_winter_night2
    show bsar_heavy_snow_night
    show bsar_normal_snow_night
    with dissolve
    play ambience bsar_winter_wind fadein 2
    $ renpy.pause(1.5, hard=True)
    show bg bsar_ext_houses_winter_night behind bsar_heavy_snow_night with dissolve
    $ renpy.pause(1.5, hard=True)
    show bg bsar_ext_square_winter_night behind bsar_heavy_snow_night with dissolve
    $ renpy.pause(1.5, hard=True)
    show bg bsar_ext_clubs_winter_night behind bsar_heavy_snow_night with dissolve
    $ renpy.pause(1.5, hard=True)
    show bg bsar_ext_camp_entrance_winter_night behind bsar_heavy_snow_night with dissolve
    $ renpy.pause(1.5, hard=True)
    bsar_narrator "Ворота."
    bsar_narrator "Как бы я не пытался не думать об этих странных видениях, они, подобно мерзким осьминогам, тянутся своими отвратительными склизкими щупальцами к моему сознанию, чтобы..."
    bsar_narrator "Э-эм."
    bsar_narrator "О чём это я? Ах, точно, об осьминогах! Ненавижу осьминогов! Или я не об этом?"
    bsar_narrator "Что-то у меня плохое предчувствие."
    stop music fadeout 1
    bsar_narrator "Вдруг краем глаза я замечаю, как ко мне стремительно приближается..."
    play music music_list["awakening_power"] fadein 2
    call screen bsar_qte(["↓"], 2, 3)
    call screen bsar_qte(["→"], 2, 3)
    call screen bsar_qte(["↑"], 2, 3)
    jump bsar_insomnia_day1_stroll_completed

label bsar_insomnia_day1_stroll_failed: 
    $ renpy.block_rollback()
    hide bsar_heavy_snow_night
    hide bsar_normal_snow_night
    with dissolve
    stop music fadeout 2
    scene bg bsar_ext_camp_entrance_winter_night_blurred with flash
    bsar_narrator "Снег попадает мне прямо в глаза..."
    play sound_loop bsar_heart
    scene bg bsar_ext_camp_entrance_winter_night_blurred:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1 zoom 1.05

        parallel:
            ease 1 xalign 0.48
            ease 1 xalign 0.52
            repeat

        parallel:
            ease 1.5 rotate 1.5 zoom 1.05
            ease 1.5 rotate -1.05 zoom 1.035
            repeat

    $ bsar_heartbeat_animation("bg bsar_ext_camp_entrance_winter_night_blurred", 1.05, 1.0)
    bsar_narrator "Я машинально делаю пару шагов назад, как вдруг всё встаёт с ног на голову."
    bsar_narrator "Я падаю, теряя равновесие..."
    play sound sfx_bones_breaking
    show blink
    $ renpy.pause(2, hard=True)
    bsar_narrator "Необычайно громко по всей округе эхом раздаётся ужасный хруст... или мне это кажется?" 
    bsar_narrator "{i}Кажется что?..{/i}"
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    $ bsar_set_time("bw", "day")
    scene bg bsar_ext_roof
    show bsar_snow_layer3_anim_quick
    show bsar_snow_layer2_anim_quick
    show bsar_she
    show bsar_snow_layer1_anim_quick
    show bsar_snow_layer0_anim_quick
    show bsar_static_noise_anim
    with bsar_flash
    play ambience bsar_winter_wind fadein 2
    play sound_loop bsar_hum fadein 2
    bsar_she "Так и знала, что найду тебя здесь!" 
    bsar_he "Неужели я настолько предсказуем? Зачем ты пришла?" 
    bsar_she "Нам пора."
    stop ambience fadeout 2
    scene bg bsar_prolog_bw
    show bsar_static_noise_anim
    with bsar_flash
    $ bsar_heartbeat_animation("bg bsar_prolog_bw", 1.05, 1.0)
    $ bsar_heartbeat_animation("bsar_static_noise_anim", 1.05, 1.0)
    play sound_loop bsar_heart
    bsar_narrator "Крик? Кто-то кричит? Почему?" 
    bsar_she "Э-это ч... ровь?!" 
    bsar_she "Ч-чёр... Зов... жатую!"
    play sound bsar_electro
    $ renpy.pause(1, hard=True)
    bsar_voice "Иван Степанович, теряем! ЭЭГ показывает смерть мозга!"
    bsar_narrator "Кажется, мне куда-то нужно? {w}Но куда? {w}Ладно... Неважно."

    if not persistent.insomnia_achievements["insomnia_murderous_snowball"]:
        $ persistent.insomnia_achievements["insomnia_murderous_snowball"] = True
        $ insomnia_show_achievement("insomnia_murderous_snowball")

    $ renpy.pause(1, hard=True)
    scene bg black with dissolve
    stop sound_loop fadeout 2
    $ renpy.pause(1, hard=True)
    #$ insomnia_set_main_menu_cursor()
    #return     

label bsar_insomnia_day1_stroll_completed: 
    $ renpy.block_rollback() 
    $ persistent.sprite_time = "night" 
    bsar_narrator "Я резко отскакиваю в сторону, и запущенный в меня снежок пролетает мимо." 
    bsar_dv "Блин! Я надеялась, что попаду." 
    show bsar_dv normal2 behind bsar_normal_snow_night with dissolve 
    bsar_narrator "С нескрываемой досадой в голосе выдала Алиса, выходя из-за статуи пионера." 
    bsar_protagonist "Добрая ты девочка, Алиса. Что ты тут вообще забыла?" 
    bsar_dv "А это уже не твоё дело, {i}дорогуша.{/i}" 
    bsar_narrator "Что-то подозрительное промелькнуло в нотках её голоса..."
    bsar_narrator "До того как я успеваю среагировать, Ульяна молниеносно засыпает мне за воротник снег и также быстро отскакивает к Алисе."
    show bsar_dv smile behind bsar_normal_snow_night:
        linear 1.0 xalign 0.25
    $ renpy.pause(1.0, hard=True)
    show bsar_us smile at right behind bsar_normal_snow_night with dissolve
    bsar_narrator "Наблюдая за моей агонией, рыжие в унисон заливаются звонким смехом."
    bsar_protagonist "УЛЬЯНА! Чтоб тебя!" 
    bsar_us "Как будто что-то плохое!" 
    bsar_protagonist "Я ж тебя..." 
    show bsar_us sad behind bsar_normal_snow_night:
        linear 1.0 xalign 0.4
    $ renpy.pause(1.0, hard=True)
    show bsar_dv sad behind bsar_normal_snow_night 
    show bsar_mt rage behind bsar_normal_snow_night at right 
    with dspr
    bsar_narrator "Но неожиданное появление Ольги Дмитриевны застаёт меня врасплох, и я замираю."
    bsar_narrator "Сказать, что она злая, значит не сказать ничего. Кажется, вот-вот у неё вздуется вена на лбу." 
    bsar_mt "Значит, вот оно — твоё социально полезное занятие?!" 
    bsar_protagonist "Это.... Это не..." 
    bsar_mt "Быстро в домик!" 
    bsar_protagonist "Но ведь..." 
    bsar_mt "Я сказала БЫСТРО!"
    bsar_narrator "Блин! Всё очень и очень плохо. Бросив напоследок ошарашенный взгляд на притихших девчонок и обречённо качнув головой вожатой, я поспешил в домик."
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1.5, hard=True)
    scene bg int_house_of_mt_night with Dissolve(2)
    play ambience ambience_medstation_inside_night fadein 2
    bsar_narrator "Надо же было так влипнуть! Наверное, Алисе с Ульяной тоже досталось. Нет. Точно досталось!" 
    bsar_narrator "Мне совершенно не хотелось выслушивать нравоучения непонятно из-за чего разъяренной Ольги." 
    bsar_narrator "К тому же накатила непонятно откуда взявшаяся усталость, и как только голова коснулась подушки я моментально заснул." 
    stop ambience fadeout 2 
    $ bsar_set_time("bw", "day")
    scene bg bsar_int_kitchen_bw
    show bsar_she normal
    show bsar_static_noise_anim
    with bsar_flash
    play music bsar_lucius_OST_piano fadein 2
    play ambience ambience_medstation_inside_night fadein 2
    bsar_she "Эй, ты опять ходишь с таким лицом, что аж смотреть противно!" 
    bsar_he "Очередной завал на работе. Эти ночные смены меня доконают." 
    bsar_she "Эй, перестань! Ну же, давай улыбнись! Улыбнись, дурак!" 
    bsar_he "Нельзя же человека за то, что он устал, называть дураком!" 
    bsar_she "{b}МНЕ{/b} можно! Люблю тебя, дурак." 
    bsar_he "Господи, ты неисправима. {w}За это я тебя и люблю." 
    bsar_she "Неужели только за это?"
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with bsar_flash
    $ renpy.pause(3, hard=True) 
    jump bsar_insomnia_day2    

label bsar_insomnia_day2:
    $ bsar_set_time("day")
    $ bsar_new_chapter("Бессонница.", "День второй.")
    scene bg black
    show blink
    bsar_narrator "Нос заложен. Горло дерёт, словно связки сорваны от бессмысленного и громкого крика в пустоту. Глаза слезятся. Я плакал во сне. Почему? Не помню." 
    bsar_narrator "Нахлынувшие после пробуждения мысли, подобно волнам во время прилива, смыли остатки сна из моей памяти, оставив только две мокрые дорожки на щеках." 
    scene bg bsar_int_dining_hall_winter behind blink
    show bsar_mz normal2 behind blink
    hide blink
    show unblink
    $ renpy.pause(2, hard=True)
    play ambience ambience_dining_hall_empty fadein 2
    play music bsar_everyday_fantasy fadein 2
    bsar_mz "...в библиотеке!" 
    bsar_protagonist "А-а-ага. Стой! В смысле?" 
    show bsar_mz angry with dspr 
    bsar_narrator "Пионерка фыркнула, уставившись на меня отрешённым взглядом."
    bsar_narrator "Женя — живое воплощение лени со стервозным характером. И голосом настолько дребезжащим и скрипучим, что на ум невольно приходят ассоциации с несмазанной калиткой."
    bsar_narrator "Мне кажется, что она еврейка, но я таки не уверен." 
    bsar_mz "Я сказала, что мне нужна помощь в библиотеке. Поэтому, жду тебя после завтрака!" 
    bsar_protagonist "Поговорим сначала о моей награде." 
    bsar_narrator "Её глаза, смотрящие поверх очков, несколько мгновений излучали то любопытство, то полное безразличие к ситуации в целом и моей персоне в частности." 
    bsar_th "Что же, всё равно делать мне сегодня нечего. Почему бы и не сходить?" 
    bsar_protagonist "Ладно-ладно. Я приду." 
    bsar_narrator "Прервал я Женю, которая, по всей видимости, уже намеревалась сказать какую-то остроту. Она довольно хмыкнула и встала из-за стола." 
    show bsar_mz normal2 with dspr 
    bsar_mz "Вот и славно. Не задерживайся!" 
    bsar_protagonist "Конечно..." 
    hide bsar_mz with dissolve
    bsar_narrator "Господи, сколько раз нужно повторять самому себе, что надо сначала думать, а потом говорить." 
    bsar_narrator "Я же только что сдуру подписал себе смертный приговор." 
    bsar_narrator "Другими словами — больше часа в одном помещении с Женей."
    stop music fadeout 2 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard=True)
    scene bg bsar_ext_library_winter_day
    show bsar_heavy_snow_day
    show bsar_normal_snow_day
    with Dissolve(1)
    play ambience bsar_winter_wind fadein 2
    bsar_narrator "И вот я стою в смятении перед библиотекой." 
    bsar_narrator "Какую на этот раз чепуху она придумала, чтобы изобразить бурную деятельность?"
    bsar_narrator "Может, пока не поздно, лучше пойти в домик?"
    bsar_narrator "А ей потом скажу, что в столовой переел и стало плохо."
    bsar_narrator "Мысль была замечательной."
    play sound sfx_open_door_1
    bsar_narrator "Но только я развернулся спиной к двери, как она распахнулась."
    bsar_mz "Ну? Чего ты тут стоишь, не заходишь?" 
    bsar_narrator "Она что, у окна дежурит? Как она вообще узнала, что я тут?"
    bsar_narrator "Несколько секунд я еще стоял неподвижно, осторожно подбирая слова."
    show bsar_mz normal2 behind bsar_normal_snow_day with dissolve
    bsar_narrator "А потом с милой улыбкой повернулся к молодой любительнице книг."
    bsar_protagonist "Женя! А я как раз к тебе шел!"
    show bsar_mz angry behind bsar_normal_snow_day with dspr
    bsar_mz "Ага, спиной вперед?"
    bsar_protagonist "А я это... {w}Повернулся посмотреть на... {w}То есть, мне послышалось... {w}Да! Послышалось, что Славя меня звала!" 
    bsar_mz "Славя уже давно у меня в библиотеке сидит, умник. Если хочешь помогать, то заходи, а нет, то иди лесом."
    hide bsar_mz with dissolve
    bsar_narrator "И исчезла, скрывшись в дверном проеме." 
    bsar_th "А она чертовски проницательная!"  
    bsar_narrator "Не удивлюсь, если сквозь свои очки она видит не только душу человека, но и его будущее."
    play sound sfx_open_door_1
    $ renpy.pause(2, hard=True)
    stop ambience fadeout 2
    scene bg bsar_int_library_winter_day with dissolve
    play ambience ambience_library_day fadein 2
    play music bsar_over_the_time_sandy_winter fadein 2
    bsar_narrator "Внутри библиотеки было немногим теплее, чем на улице. Пахло книжной пылью и коммунизмом." 
    bsar_narrator "Атрибутика и портреты с лозунгами смотрели на меня буквально отовсюду, из-за чего по телу невольно пробежали мурашки." 
    bsar_th "Нечасто же я заходил в библиотеку." 
    bsar_narrator "Славя действительно была здесь и рылась в каких-то бумагах, перебирая их и перекладывая с места на место." 
    bsar_narrator "Увидев меня, блондинка улыбнулась и слабо кивнула в знак приветствия, не отрываясь от работы." 
    bsar_narrator "А Женя уселась прямо на полу среди башенок из книжек." 
    bsar_narrator "Одни были открыты, другие лежали подальше, видимо, отложенные на потом." 
    bsar_narrator "Тут были стопки самой различной литературы в самых разных переплётах." 
    bsar_narrator "От старинных тряпичных до новеньких твердых." 
    show bsar_mz smile with dissolve 
    bsar_mz "Спасибо, что пришёл. На самом деле, я думала, что ты будешь отлынивать." 
    bsar_protagonist "То, что я стою перед тобой, ни о чём не говорит?" 
    show bsar_mz normal2 with dspr 
    bsar_narrator "Женя смерила меня долгим строгим взглядом и глубоко вздохнула." 
    bsar_protagonist "Так. Чем я буду заниматься? На полу сидеть?" 
    bsar_mz "Нет. Впрочем, как хочешь. С прошлой смены в библиотеку не вернулось с десяток книг. И поэтому я решила их проштамповать." 
    bsar_protagonist "Чего-чего делать?" 
    bsar_mz "Проштамповать. Проставить метки нашего лагеря на форзац страницы с помощью штампа. Ты ведь знаешь, что такое форзац?" 
    bsar_protagonist "Э-э-э... Конечно." 
    show bsar_mz angry with dspr 
    bsar_narrator "Женя закатывает глаза и громко цокает языком." 
    bsar_mz "Форзац — это лист бумаги, соединяющий корку книги и первую страницу. Это, по сути, первая страница и есть." 
    bsar_narrator "Я живо кивал, наблюдая, как Женя опускает штампик на губку, смоченную чернилами, и проставляет клеймо на тот самый форзац." 
    bsar_mz "Справишься?" 
    bsar_narrator "Она указала на длинные ряды стеллажей за её спиной." 
    bsar_th "М-да..." 
    bsar_th "Намечается длинная и рутинная работа, но делать нечего." 
    bsar_th "Я уже согласился помочь, и назад пути нет." 
    hide bsar_mz with dissolve 
    bsar_narrator "Я сел на пол рядом с Женей и принял от неё второй штампик и губку с чернилами, сразу же измазавшись в них." 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard=True) 
    scene bg bsar_int_library_winter_day with Dissolve(1) 
    bsar_narrator "Сорок или пятьдесят книг спустя я довёл процесс до автоматизма, позволяющий мне брать книгу, ставить печать и брать новую, практически не глядя на них." 
    bsar_th "Наверное, так и чувствуют себя принтеры." 
    bsar_narrator "В процессе работы мы переговаривались ни о чем и обо всем одновременно." 
    bsar_narrator "Делились впечатлениями от лагеря, сплетничали о его обитателях, говорили о погоде, о жизни до лагеря и прочем." 
    show bsar_mz normal2 at left 
    show bsar_sl normal at right 
    with dissolve 
    bsar_mz "...вот я и стала с книгами тут работать. Книги — они ведь не обманут, не сорвутся на тебя. Общаться с ними порой легче, чем с людьми." 
    bsar_protagonist "Ты главное не увлекайся сильно с книгами разговаривать. Ничего хорошего из этого не выйдет." 
    bsar_mz "Вот об этом я и говорю." 
    bsar_sl "А я думаю, что это здорово, когда человек так увлекается чем-то в жизни. У тебя, наверное, и дома целая библиотека стоит?" 
    bsar_mz "Не совсем у меня, а скорее у отца библиотека." 
    bsar_sl "Давай, расскажи, как ты живешь вне лагеря!" 
    bsar_mz "Я даже и не знаю, что рассказать. У меня папа ученый, поэтому книг у меня всегда было в избытке. А маму я не видела никогда."  
    bsar_mz "Гулять меня особо не отпускают. Отец говорит, что на улице я ничему хорошему от ребят не научусь, вот я и читаю книги."
    bsar_mz "Очень люблю эти волшебные миры и истории про рыцарей, правда, книги про этих самых рыцарей достать было трудновато." 
    bsar_sl "Ого! Как же так? Ты совсем никуда не выходишь?" 
    bsar_mz "Ну как же! Я хожу в школу, общаюсь там с одноклассниками. А гулять меня как-то не зовет никто, да и не тянет." 
    bsar_sl "А я люблю гулять! Особенно на природе! Мы с родителями в конце лета каждые выходные едем в лес за грибами! Так здорово бродить среди деревьев и слушать пение птиц. Хотела бы я и тебя с собой взять!" 
    bsar_mz "В лес? Ну не знаю." 
    bsar_sl "Да, в лес. Хотела бы я когда-нибудь работать на природе! Может, лесником? Бывают женщины-лесники?" 
    bsar_narrator "Она мило засмеялась, но мне пришлось вернуть её с небес на землю." 
    bsar_protagonist "Лесники должны загонять животных для охотников — это их основная работа." 
    bsar_sl "Правда? Нет! Я люблю животных! Не хочу, чтобы их убивали, особенно из-за меня." 
    bsar_protagonist "А я как-то не особо леса люблю. Какая-то непонятная у меня к ним неприязнь."
    bsar_mz "Слушай, а расскажи, как ты живешь вне лагеря?"
    bsar_protagonist "Ну, я живу в Москве с роди..."
    stop ambience fadeout 2 
    stop music fadeout 2
    $ bsar_set_time("bw", "day")
    scene bg bsar_ext_winter_street
    show bsar_snow_layer3_anim
    show bsar_snow_layer2_anim
    show bsar_she normal
    show bsar_snow_layer1_anim
    show bsar_snow_layer0_anim
    show bsar_static_noise_anim
    with bsar_flash
    play ambience bsar_winter_wind fadein 2
    play sound_loop bsar_hum fadein 2
    play music bsar_socialism fadein 2
    bsar_she "Ты же говорил, что бросишь." 
    bsar_he "Я бросал. Но после той аварии снова начал." 
    bsar_she "Извини. Мне очень жаль твою сестру. Не хотела об этом напоминать." 
    bsar_he "Эй! Ничего страшного. Не стоит сильно расстраиваться."
    bsar_he "Я понимаю, что такое... {w}такое порой случается. И с этим просто нужно смириться."
    $ bsar_set_time("day")
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene bg bsar_int_library_winter_day
    show bsar_sl normal at center
    with bsar_flash
    play ambience ambience_medstation_inside_night fadein 2
    bsar_sl "Эй! С тобой все в порядке?" 
    bsar_narrator "Мысли путаются, наскакивают друг на друга, переплетаются. {w}Я не могу выудить из этой вакханалии хотя бы частичку воспоминаний."
    bsar_protagonist "Не стоит беспокоиться. Я в норме, просто давайте поговорим о чем-нибудь другом." 
    bsar_sl "Ну хорошо, понимаю, как скажешь." 
    bsar_protagonist "Славь, я все хотел спросить тебя..." 
    bsar_sl "Да?" 
    bsar_protagonist "Тогда, в столовой... Что ты имела в виду, сказав «отдохнуть»?"  
    bsar_sl "Тьфу! Так начал, я уже думала, будто что-то серьезное спросить собираешься." 
    bsar_sl "И вообще, я тут совсем заболталась, мне уже нужно бежать, я Ольге Дмитриевной обещала помочь." 
    bsar_sl "Ты не против, если я попрошу тебя доделать тут работу с бумагами? Пожа-алуйста?" 
    bsar_narrator "Я осмотрел свои измазанные в чернилах руки." 
    bsar_narrator "Определенно, смена деятельности мне не помешает. Нужно подумать." 
    bsar_narrator "Женя кивнула мне, давая понять, что справится с остатками одна." 
    bsar_narrator "Чёрт, как же гудит голова! Что же со мной происходит последние дни?" 
    bsar_protagonist "Конечно, Славя! Для тебя — все что угодно!" 
    bsar_narrator "Сказал я, разминая свои затекшие от длительного сидения ноги." 
    hide bsar_sl with dissolve 
    stop music fadeout 2 
    bsar_narrator "Славя смежила губы в лучезарной улыбке и поспешно покинула библиотеку." 
    scene bg bsar_logbook with dissolve 
    bsar_narrator "Я сажусь за стол, оценивая оставшийся фронт работ." 
    bsar_narrator "Тут осталось перенести несколько записей в формуляры. {w}Плёвое дело."
    scene bg black with Dissolve(1)
    $ renpy.pause(1, hard=True)
    scene bg bsar_logbook with Dissolve(1)
    bsar_narrator "И так сойдёт!" 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1)
    $ renpy.pause(1, hard=True)
    scene bg bsar_ext_square_winter_day
    show bsar_heavy_snow_day
    show bsar_dv normal at center
    show bsar_normal_snow_day
    with Dissolve(1)
    play ambience bsar_winter_wind fadein 2
    play music bsar_standing_tall fadein 2
    bsar_narrator "Не успел я толком отойти от библиотеки, как столкнулся с Алисой, которая, по всей видимости, спешила попасть внутрь и совершенно не смотрела по сторонам."  
    bsar_narrator "Из-за удара она выронила книгу, которая упала на снег обложкой кверху. «Унесённые ветром»."
    bsar_narrator "Заметив, что моё внимание приковано к книге, ДваЧе быстро её подняла, спрятав за спину." 
    bsar_protagonist "Должок идёшь возвращать, Алиса?" 
    bsar_dv "А тебе какое дело?" 
    bsar_narrator "Губы плотно сжаты, свободная рука превращается в кулак." 
    bsar_narrator "Не требуется обладать какими-то знаниями в области психологии, чтобы понять этот жест и пронизывающий меня крайне недовольный взгляд." 
    bsar_narrator "Я смиренно киваю головой и улыбаюсь, пытаясь разрядить обстановку. {w}Получается немного фальшиво, но Алиса этого не замечает, или делает вид, что не замечает."  
    bsar_narrator "Пионерка делает шаг назад и возвращается к своему надменно-безразличному состоянию." 
    bsar_dv "Давай-давай, проходи, не задерживайся! И забудь то, что видел!" 
    bsar_protagonist "Да, конечно. {w}Вот-вот уже. {w}Почти. {w}{i}Ещё чуть-чуть...{/i}." 
    bsar_dv "Болван!" 
    hide bsar_dv with dissolve 
    bsar_narrator "ДваЧе прошла мимо меня, намеренно задев плечом."
    bsar_narrator "Больше всего я удивляюсь тому факту, что позволяю себе пасовать перед этой девчонкой. {w}Боже, эта Алиса..." 
    stop ambience fadeout 2
    stop music fadeout 2
    $ bsar_set_time("bw", "day")
    scene bg bsar_ext_prosecutor_office
    show bsar_snow_layer3_anim
    show bsar_snow_layer2_anim
    show bsar_lis normal
    show bsar_snow_layer1_anim
    show bsar_snow_layer0_anim
    show bsar_static_noise_anim
    with bsar_flash 
    play ambience bsar_winter_wind fadein 2
    play sound_loop bsar_hum fadein 2
    play music bsar_cyprinid_floating fadein 2
    bsar_fox "Ну что, дорогуша, поздравляю с повышением! Обмоем звёздочку?"
    bsar_he "Заметь, не я это предложил. Только не долго и не много."
    bsar_fox "Петля не жмёт?"
    bsar_he "Какая петля?"
    bsar_fox "Семейной жизни! Когда уже детишки? Крёстной возьмешь?"
    bsar_he "Не паясничай. Ты, кстати, помнишь про следующую сделку, которую мы крышуем?"
    bsar_fox "Ты то так не ори. Хочешь обратно в старлеи? Помню я, помню."
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    stop music fadeout 2
    $ bsar_set_time("day")
    scene bg bsar_ext_square_winter_day
    show bsar_heavy_snow_day
    show bsar_normal_snow_day
    with bsar_flash
    play ambience bsar_winter_wind fadein 2 
    bsar_narrator "Чёрт! У меня очень стойкое чувство дежавю, словно события из видений, которые я толком не могу вспомнить, уже и в правду происходили."  
    bsar_narrator "Нет. Это не могут быть мои воспоминания! {w}Похоже, что мне светит путёвка в жёлтый дом." 
    bsar_protagonist "Карету мне, карету! Сюда я больше не ездок..."
    show bsar_us normal behind bsar_normal_snow_day with dissolve
    bsar_us "Физкульт-привет!" 
    bsar_protagonist "Привет, Ульяна." 
    bsar_us "Чего это ты тут стоишь? Да ещё и бледный какой-то. Может, Виолетту позвать? Укольчик сделает!" 
    bsar_protagonist "Нет, нет. Спасибо."    

    if bsar_insomnia_day1_stroll: 
        bsar_protagonist "Вам вчера сильно от Ольги досталось?" 
        bsar_us "Да. Она всё-таки узнала про те конфеты!" 
        bsar_protagonist "Про какие конфеты?" 
        bsar_us "Ну... Которые я одолжила в столовой." 
        bsar_protagonist "Серьёзно? Ульяна, ты неисправима!"  

    bsar_us "Ладно. Не суть важно. Ты Алису не видел?" 
    bsar_protagonist "Алису? Алису видел, она в библиотеку пошла." 
    bsar_us "Спасибо! Не болей!" 
    hide bsar_us with dissolve
    bsar_narrator "Ульяна тепло улыбнулась и подмигнула мне, а затем побежала в библиотеку. Странно видеть эту шестнадцатилетнюю егозу такой милой."  
    bsar_narrator "Раньше она постоянно пыталась меня подколоть, а сейчас тишь да гладь." 

    if bsar_insomnia_day1_stroll: 
        bsar_narrator "Не считая снежков, конечно." 

    play sound sfx_dinner_horn_processed fadein 2 
    $ renpy.pause(3, hard=True) 
    bsar_narrator "Горн. Пора на обед."
    stop ambience fadeout 2 
    scene bg black with Dissolve(1)
    $ renpy.pause(1.5, hard=True)
    scene bg int_house_of_mt_day with Dissolve(1) 
    $ renpy.block_rollback()
    play ambience ambience_medstation_inside_night fadein 2
    play music bsar_maconda_die_begin fadein 4
    bsar_narrator "После обеда меня разморило."
    bsar_narrator "Голова начала гудеть, а мысли кровавыми сгустками выскальзывать из черепа."
    scene bg bsar_int_house_of_mt_day_vingete_blurred with Dissolve(1.1)
    $ renpy.pause(1.1, hard=True)
    $ bsar_show_random_words(bsar_insomnia_day2_amnesia_scene, k=70)
    $ renpy.pause(1, hard=True)
    $ bsar_show_centered_text("У МЕНЯ АМНЕЗИЯ?", style=style.bsar_insomnia_centered_text_style)
    stop ambience fadeout 2 
    $ bsar_set_time("bw", "day")
    scene bg bsar_prolog_bw
    show bsar_static_noise_anim
    with bsar_flash
    play ambience bsar_hum fadein 2 
    bsar_narrator "Нет же! Папа работает учителем, а мама бухгалтер."  
    bsar_narrator "Я с отличием закончил десятый класс в Московской гимназии номер четырнадцать и за это был отправлен в этот лагерь, {i}потому что давно хотел сюда попасть.{/i}"  
    bsar_narrator "{i}Ведь так?{/i}"
    stop ambience fadeout 2
    $ bsar_set_time("day")
    scene bg int_house_of_mt_day with bsar_flash 
    play ambience ambience_medstation_inside_night fadein 2 
    bsar_protagonist "И что мне делать?" 
    bsar_narrator "Задал я вопрос пустой комнате, которая ответила мне абсолютно ничем."
    show blink
    $ renpy.pause(2, hard=True)
    $ bsar_set_time("bw", "day")
    stop ambience fadeout 2 
    scene bg bsar_prolog_bw
    show bsar_static_noise_anim
    with bsar_flash 
    play ambience bsar_heart_monitor fadein 2
    play sound_loop bsar_voices fadein 2
    bsar_narrator "Я чувствую невероятную лёгкость и безволие, в какой-то мере, расконцентрированность." 
    bsar_narrator "Пространство вокруг меня наполнилось звуками. {w}Тиканье часов, какой-то писк, шаги, едва различимые голоса вдали." 
    bsar_voice "Я своими глазами это видел, Иван Степанович!" 
    bsar_voice "Это просто чудо какое-то! Возможно, есть шансы, что он всё же..."
    scene bg black with bsar_flash
    bsar_narrator "А ведь понимаю, что сон. Поэтому пытался хитрить, ускользать, изворачиваться, чтобы не проснуться." 
    bsar_narrator "Пытался оглохнуть, ослепнуть, дематериализоваться, чтоб реальность не могла меня изловить и затащить обратно."  
    bsar_narrator "Хотелось ещё послушать, что говорят эти странные голоса."
    bsar_narrator "Но вот звуки становятся тихими и невнятными, возвращается тяжесть тела..."
    bsar_narrator "Кончилось."
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    stop music fadeout 2
    $ bsar_set_time("night")
    scene bg int_house_of_mt_night behind blink 
    show unblink 
    $ renpy.pause(2, hard=True)
    play ambience ambience_medstation_inside_night fadein 2 
    show bsar_mt rage with dissolve 
    bsar_mt "Вставай! Вставай, кому говорю?!" 
    bsar_protagonist "Да встаю я! Что случилось то? На десять минут задремал." 
    bsar_mt "Какие десять минут? Уже вот-вот и вечер на дворе! Ты ужин проспал!" 
    bsar_protagonist "Прошу прощения. Не рассчитал." 
    bsar_narrator "Я закашлял. В горле першило, руки и ноги онемели. Чувствую себя отвратно." 
    show bsar_mt angry with dspr 
    bsar_mt "Ты здоров? Уже который день выглядишь... {w}неважно." 
    bsar_protagonist "Всё в порядке. Просто плохо чувствую себя после дневного сна. Я прогуляюсь." 
    bsar_mt "Подожди! На, возьми. Перекусишь хотя бы." 
    bsar_narrator "Вожатая протянула мне целлофановый свёрток. Бутерброды." 
    bsar_protagonist "Спасибо большое, Ольга Дмитриевна. Я пошёл, по дороге перекушу." 
    bsar_narrator "Накинув пальто, я вышел из домика."
    play sound sfx_open_door_1
    $ renpy.pause(2, hard=True)
    stop ambience fadeout 2
    scene bg bsar_ext_house_of_mt_winter_night2 with dissolve
    play ambience bsar_winter_wind fadein 2
    $ renpy.pause(1.5, hard=True)
    scene bg bsar_ext_houses_winter_night with dissolve
    $ renpy.pause(1.5, hard=True)
    scene bg bsar_ext_square_winter_night with dissolve
    $ renpy.pause(1.5, hard=True)
    scene bg bsar_ext_musclub_winter_night with dissolve
    $ renpy.pause(1.5, hard=True)
    bsar_narrator "Давненько я не видел Мику. Хочу повидаться с этой весёлой и словоохотливой японкой. Скорее всего, она у себя в кружке."  
    bsar_narrator "Может быть, спросить у неё про эти странные сны и видения? Она единственная, кто не будет искать скрытый смысл в моих словах и уж точно не станет крутить пальцем у виска." 
    play sound sfx_open_door_1
    $ renpy.pause(2, hard=True)
    stop ambience fadeout 2
    scene bg bsar_int_musclub_night_2 with dissolve 
    play ambience ambience_medstation_inside_night fadein 2
    bsar_narrator "Открыв дверь и зайдя внутрь, я стал свидетелем ссоры, которую точно не ожидал увидеть." 
    bsar_narrator "Алиса с Леной? Ожидаемо."
    bsar_narrator "Алиса со Славяной? Тоже."
    bsar_narrator "Алиса, ругающаяся с Ульяной? Удивительно, но происходит."
    bsar_narrator "Голоса доносятся из подсобки."
    scene bg bsar_us_dv_confrontation with dissolve
    play music bsar_painful_history fadein 2
    bsar_us "Алиса, может быть, ты уже успокоишься?" 
    bsar_dv "А может ты не будешь меня затыкать?!" 
    bsar_us "Я не трогала его! Мы же вообще живём в разных доми..." 
    bsar_dv "НЕ ВРИ! Я уверена, что его взяла ты! Верни сейчас же или хуже будет!" 
    bsar_narrator "Кажется, дело может принять плохой оборот. {w}Стоит ли вмешиваться? С другой стороны, я точно не знаю, что здесь происходит."     
    $ persistent.sprite_time = "night"      

    menu: 
        "Вмешаться": 
            $ bsar_insomnia_day2_intervene = True 
            bsar_narrator "И чего я встал как истукан? Нужно вмешаться, пока Ульяне не досталось. Я быстро перескакиваю порог и встречаюсь взглядом с Алисой."
            scene bg int_clubs_male2_night_nolight
            show bsar_dv sad at left 
            show bsar_us sad at right 
            with dissolve 
            bsar_dv "ТЫ подслушивал?!" 
            bsar_narrator "Я замер, не ожидав такой реакции." 
            bsar_protagonist "Почему вы ругаетесь? Вас за километр слышно." 
            bsar_dv "Ага-ага. Заливай больше. Сто процентов стоял под дверью и слушал, болван!" 
            bsar_us "Алиса!" 
            bsar_dv "А с тобой я позже разберусь!" 
            hide bsar_dv with dissolve 
            stop music fadeout 4
            bsar_narrator "ДваЧе толкнула меня и быстро скрылась в дверном проёме, оставив дверь нараспашку."
            bsar_narrator "Я перевёл взгляд на ошарашенную Ульяну, но она лишь грустно помотала головой." 
            bsar_us "Извини, что тебе пришлось это услышать. Она почти весь день такая злая. Я её попробую догнать и успокоить."
            hide bsar_us with dissolve
            bsar_narrator "Последнее предложение Ульяна пробормотала себе под нос и выскочила за дверь, громко зовя Алису."
            bsar_th "Чёрт! Помог, называется."
            bsar_narrator "Алиса точно на меня обидится, и Ульяна тоже была не особо рада моему появлению."  
            bsar_narrator "Умею же я портить то, что, как казалось изначально, ещё больше испортить нельзя." 

        "Не вмешиваться": 
            $ bsar_insomnia_paradise_ending_v +=1 
            bsar_narrator "Я почему-то ошеломленно замираю, не в силах сделать даже шаг, а девушки продолжают свой разговор на повышенных тонах."
            bsar_us "Алиса, чтоб тебя! Перестань истерить! Я понимаю, насколько важен тебе этот дневник."
            bsar_us "Мы подруги, и я бы никогда не навредила тебе!"
            bsar_narrator "Ничего себе! Такого я точно не ожидал."
            bsar_narrator "На мгновение в помещении музыкального кружка повисла полная тишина. Настолько тяжёлая и абсолютная, что кажется, словно воздух уплотнился и стал вязким." 
            bsar_dv "Уль... Ульяна. Извини. {w}Не знаю, что на меня нашло. Я правда не хотела." 
            bsar_narrator "Никогда не слышал, чтобы голос Алисы так дрожал." 
            bsar_us "Всё в порядке. Давай завтра вместе поищем твой дневник?" 
            stop music fadeout 4
            bsar_narrator "Я решаю постучать, чтобы выдать своё присутствие до того, как девочки увидят меня и обвинят в подслушивании." 
            bsar_protagonist "Мику здесь?"
            scene bg int_clubs_male2_night_nolight
            show bsar_dv smile at left 
            show bsar_us normal at right 
            with dissolve 
            $ renpy.pause(5, hard=True) 
            bsar_dv "Она уехала четыре дня назад, дурень." 
            bsar_protagonist "Почему дурень-то? Обидно же." 
            bsar_dv "А я по-дружески. Обидно ему. {w}Напоминаешь мне одного знакомого хлюпика, как его там звали?" 
            bsar_us "Не помню, на «С», кажется. Хотя, не так это и важно." 
            bsar_narrator "Девушки не наигранно улыбались. Всё же хорошо, что я решил не лезть." 
            bsar_protagonist "А что, собственно, с Мику?" 
            bsar_dv "У неё какие-то проблемы с горлом. Заболела, бедняжка." 
            bsar_us "Ага, жалко её." 
            bsar_us "Ладно. Может, пойдём прогуляемся?" 
            bsar_narrator "Ульяна потёрла руки и хитро подмигнула Алисе." 
            bsar_dv "Я за! А ты, хлюпик?" 
            bsar_protagonist "Опять какую-то авантюру надумали? Ну хорошо, я с вами."
            show bsar_us smile with dspr
            bsar_narrator "Ульяна подпрыгнула и хлопнула в ладошки." 
            bsar_us "Вперёд к приключениям!"

    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(4, hard=True)      
    $ renpy.block_rollback() 

label bsar_insomnia_day3:
    $ bsar_set_time("bw", "day")
    $ bsar_new_chapter("Бессонница.", "День третий.")
    scene bg bsar_ext_lane
    show bsar_lis normal
    show bsar_static_noise_anim
    with bsar_flash
    play ambience ambience_cold_wind_loop fadein 2
    play sound_loop bsar_hum fadein 2
    play music bsar_hoyts_office fadein 2
    bsar_narrator "Тёмные переулки, руки в карманах, ладонь поглаживает холодную рукоять ПМа. Первый лёд хрустит под ногами. Луна за тучами спряталась, не показывается." 
    bsar_protagonist "Лис, наш выход только после того, как клиент клюнет. Не раньше."
    bsar_fox_orange "Да поняла я. Не учи учёного."
    bsar_fox_orange "Чего ты вообще подписался на эту встречу?"
    bsar_protagonist "ОД приписал. Сказал, что буду отрабатывать упущенный товар."
    bsar_fox_orange "Ну ты даёшь."
    bsar_fox_orange "Какого ты вообще попёрся туда? Это же не наш уровень, а ФСКН."
    bsar_protagonist "Так получилось."
    bsar_narrator "Я остановился у поворота и жестом показал своей напарнице замереть." 
    bsar_fox_orange "Как тебя твоя отпустила? Не прознала ещё про твои тёмные делишки?"
    bsar_protagonist "Нет, не прознала. А у тебя как дела с..."
    bsar_fox_orange "А это уже не твоё дело, дорогуша. Следи лучше за точкой."
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    scene bg bsar_prolog_bw
    show bsar_static_noise_anim
    with bsar_flash
    bsar_she_red "Нет! Пожалуйста, не поддавайся! Ты должен проснуться."
    bsar_protagonist "А разве я сплю?"
    bsar_narrator "Спросил. {w}И проснулся."
    stop music fadeout 2
    $ bsar_set_time("night")
    scene bg int_house_of_mt_night2 with bsar_flash
    play ambience ambience_medstation_inside_night fadein 2
    play music bsar_domitori_taranofu_planet_of_colds fadein 2
    play sound_loop bsar_medical_devices fadein 2
    bsar_narrator "В комнате было темно. Похоже, проснулся до рассвета."
    bsar_narrator "Я открыл рот в беззвучном крике."
    bsar_narrator "Нет, физической боли не было. {w}Было ощущение, что само моё естество разрывают, кромсают, сжигают изнутри."
    bsar_narrator "Ещё чуть-чуть и я просто... {w}просто исчезну. Испарюсь, словно меня никогда и не было."
    bsar_narrator "Лоб покрылся холодным липким потом, а по спине пробежали мурашки."
    $ bsar_show_centered_text("Почему мне так тревожно и одиноко?", style=style.bsar_insomnia_centered_text_style)
    $ bsar_show_centered_text("Почему возникло чувство вины?", style=style.bsar_insomnia_centered_text_style)
    $ bsar_hide_centered_text(dspr)
    bsar_narrator "В окно робко заглянула луна, освещая домик и даруя предметам более смазанные и кривые очертания."
    $ bsar_show_centered_text("Я всё ещё сплю или уже нет?", style=style.bsar_insomnia_centered_text_style)
    $ bsar_hide_centered_text(dspr)
    bsar_narrator "В голову лез всякий вздор."
    bsar_narrator "Попытался встать, но не смог. {w}Тело не слушалось. {w}Попытался снова. {w}Получилось. Собственные движения немного успокоили." 
    bsar_narrator "Сознание прояснилось, и я смог сконцентрироваться. Всего лишь дурной сон. {w}Который раз."
    scene bg int_house_of_mt_night2:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 5 zoom 2.1 xalign 0.7 yalign 0.4
    $ renpy.pause(5, hard=True)
    scene bg bsar_ext_winter_forest
    show bsar_snow_layer3_anim
    show bsar_snow_layer2_anim
    show bsar_snow_layer1_anim
    show bsar_snow_layer0_anim
    with fade
    bsar_narrator "Подошёл к окну. Оно показывало смазанные ели, причудливый танец падающих снежинок, спрятавшееся за рваными облаками небо."
    bsar_narrator "Куда не глянь, везде простиралась хвойная стена. {w}Бескрайняя и до боли одинаковая."
    bsar_narrator "Стало душно."
    bsar_narrator "Горло свело судорогой, в груди возникло тянущее чувство. {w}Хочется курить."
    bsar_narrator "Не знаю, почему я решил, что мне нужно именно этого, ибо я раньше никогда даже не пробовал табачить."
    bsar_narrator "Захотелось выйти на улицу и бежать. Бежать пока не кончатся силы. Подальше от этих лесных стен и кошмаров."
    $ renpy.pause(2, hard=True)
    scene bg int_house_of_mt_night2 with fade
    bsar_narrator "Я постоял ещё немного и вернулся в кровать, но спать уже не хотелось." 
    stop ambience fadeout 2 
    stop music fadeout 2
    stop sound_loop fadeout 2
    $ bsar_set_time("day")
    scene bg black with Dissolve(1)
    $ renpy.pause(2, hard=True)
    scene bg bsar_ext_square_winter_day
    show bsar_heavy_snow_day
    show bsar_mt grin
    show bsar_normal_snow_day
    with Dissolve(1)
    play ambience bsar_winter_wind fadein 2 
    bsar_mt "К сожалению, осталась всего неделя до окончания смены, но впереди нас ждут предпраздничные хлопоты и масса хорошего настроения!" 
    bsar_mt "Не забудьте, что на завтра запланирован поход в лес."
    bsar_mt "Надеюсь, по окончанию смены у вас останутся только хорошие воспоминания о нашем «Совёнке»." 
    bsar_mt "{i}Воспоминания на всю жизнь!{/i}" 
    bsar_mt "Все свободны." 
    hide bsar_mt with dissolve 
    bsar_narrator "Бледное, мелкое солнце светило на лагерь из последних сил. Светило, но ни капельки не грело." 
    bsar_narrator "{i}Воспоминания на всю жизнь?{/i}" 
    bsar_narrator "А какая меня дальше ждёт жизнь? Бренное существование в окружении мягких стен жёлтого дома и бормочущих всякую чушь чудаков?" 
    bsar_narrator "Или дурдом выглядит иначе?" 
    bsar_narrator "Хотя, почём мне знать, я там никогда не был!"
    bsar_narrator "Ну вот. Опять потерял самообладание. Почему бы мне просто не рассказать кому-нибудь об этом?" 
    bsar_narrator "Просто излить душу, может поплакать даже. {w}Смешно." 
    bsar_narrator "Пару дней каких-то кошмаров, а уже раскис, как маленькая девочка, потерявшая плюшевого мишку." 
    bsar_narrator "Линейка уже кончилась. Странно, что Слави сегодня на утреннем построении не было. Может, у неё какие-то проблемы?"
    bsar_narrator "Наверное, всё же это не моё дело." 
    show bsar_us smile behind bsar_normal_snow_day with dissolve
    bsar_us "А-у-у. Есть кто дома? Чего встал, как столб посреди площади? Линейка давным-давно закончилась." 
    bsar_protagonist "Ах да. Извини." 
    bsar_us "За что?" 
    bsar_protagonist "В смысле?" 
    bsar_us "За что извиняешься, говорю. Хватит тормозить!" 
    bsar_protagonist "А, неважно. Как там Алиса?" 
    bsar_us "В полном порядке." 
    bsar_narrator "Пионерка улыбнулась и показала большой палец." 
    bsar_narrator "А почему, собственно, не Ульяна?" 
    bsar_narrator "Думаю, с ней вполне можно поговорить про кошмары. Но аккуратно и без лишних подробностей. Только при этом всегда остаётся шанс быть высмеянным." 
    bsar_narrator "Начну издалека." 
    bsar_protagonist "Как спалось?" 
    bsar_us "Отлично, а почему спрашиваешь?" 
    bsar_protagonist "Просто интересно." 
    bsar_us "Что, бессонница мучает?" 
    bsar_protagonist "Так заметно?" 
    bsar_us "Очень заметно! Мешки под глазами уже больше, чем сами глаза. Ходишь как живой мертвец из того фильма..." 
    bsar_narrator "Её правда. Мой внешний вид оставляет желать лучшего. Я похож на узника концлагеря, а не на счастливого пионера." 
    bsar_us "Слушай, а хочешь я тебе ловец снов дам? У меня сестра увлекается этой, как её..."
    show bsar_us dontlike behind bsar_normal_snow_day with dspr
    bsar_narrator "Девушка замирает, сводит брови и начинает бегать глазами по площади, словно ища подсказку."
    show bsar_us normal behind bsar_normal_snow_day with dspr
    bsar_us "Вспомнила! Мистикой она увлекается!" 
    bsar_us "Короче, она мне сделала ловец снов. Амулет какой-то индейский. Говорит, что помогает с кошмарами." 
    bsar_protagonist "А ты уверена, что он поможет?" 
    bsar_us "Не нравится мне твой скепти-чтоб-его-цизм."
    bsar_protagonist "Извини. Я с радостью возьму этот ловец снов."
    show bsar_us smile behind bsar_normal_snow_day with dspr
    bsar_us "Отличненько! Увидимся на завтраке, там я тебе его и отдам." 
    hide bsar_us with dissolve 
    bsar_narrator "Ульянка на прощание махнула мне рукой и быстро убежала в сторону домиков. Ловец снов значит? Почему бы, собственно, и нет."
    $ bsar_set_time("bw", "day")
    scene bg bsar_int_kitchen_bw
    show bsar_she normal
    show bsar_static_noise_anim
    with bsar_flash
    play ambience ambience_medstation_inside_night fadein 2
    play sound_loop bsar_hum fadein 2
    play music bsar_master_of_spirits_the_last_word fadein 2
    bsar_he "Ты серьёзно думаешь, что эта безделушка мне поможет?" 
    bsar_she "Ох, как же я не люблю, когда в твоём голосе слышны нотки скепти-чтоб-его-цизма." 
    bsar_he "Извини, я попробую. Весь на нервах из-за этой поездки и кошмаров. Так хочется всё отменить, из..." 
    bsar_she "Твои глаза извиняются лучше. {w}Но на самом деле, мне и правда не нравится эта твоя работа. {w}Странная она какая-то."
    bsar_she "С тобой точно всё будет в порядке?" 
    bsar_he "Да, точно. Спасибо за ловец снов. Люблю тебя!" 
    bsar_she "И я лю..." 
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    stop music fadeout 2
    $ bsar_set_time("day")
    scene bg black with bsar_flash
    $ renpy.pause(0.5, hard=True)
    scene bg bsar_int_dining_hall_winter with Dissolve(1)
    play ambience ambience_dining_hall_empty fadein 2
    play sound_loop bsar_voices fadein 2
    play music bsar_master_of_spirits_own_shadow fadein 2
    bsar_narrator "Усталость после практически бессонной ночи накрывала, подобно шерстяному одеялу." 
    bsar_narrator "Полусладкий чай совсем не помогал. Насыпал ещё несколько ложек, размешал."  
    bsar_narrator "Сахар помог чуть-чуть растопить окостеневший ум." 
    bsar_narrator "Дико это всё. Сны снами, но слишком уж они реальными кажутся." 
    bsar_narrator "И эти пробелы в памяти... {w}С ними что?" 
    bsar_narrator "Я посмотрел на стену, словно пытаясь найти там ответ." 
    bsar_narrator "Цементные швы между кафелем, да и сам кафель, были где-то тёмными от пыли, а где-то совершенно чистыми, если даже не блестящими." 
    bsar_narrator "Как будто недомыли и бросили." 
    bsar_narrator "Интересно, сколько ещё моё сознание будет таким же немытым? {w}Сколько я ещё буду осознавать, что это всего лишь сны, а не реальность?" 
    bsar_narrator "Или, может быть, то и есть реальность, а это - всего лишь дурацкий сон?" 
    bsar_narrator "Бред бьющегося в предсмертных конвульсиях Морфея... {w}Я запнулся." 
    bsar_narrator "Дверь столовой распахнулась, и зашла Ульяна. Её-то я и дожидался. Боялся, что разминулись."
    stop music fadeout 2
    bsar_narrator "Румяная с улицы, глаза блестят, на плечах снег тает. Сразу меня замечает, берёт поднос и садится напротив."
    show bsar_us normal with dissolve 
    bsar_us "Вот, принесла, как и обещала." 
    bsar_narrator "Она протянула мне амулет." 
    show bsar_dream_catcher at bsar_dream_catcher_anim:
        xcenter 0.69 ycenter 2.10 zoom 0.1 rotate -90  
        ease 2 ypos 0.50 zoom 0.7 rotate 3
        ease 1 zoom 0.6 xcenter 0.50 rotate 0
    $ renpy.pause(3, hard=True)
    bsar_narrator "Красивый."
    bsar_narrator "Не помню, где я это слышал, но всё же."
    bsar_narrator "По древним преданиям плохие сны запутываются в паутине из ниток, а хорошие проскальзывают сквозь отверстие посередине." 
    bsar_protagonist "Спасибо большое, Уль. Это многое для меня значит."
    show bsar_dream_catcher at bsar_dream_catcher_anim:
        ease 1 xcenter 0.6 zoom 0.6 rotate 3
        ease 2 xcenter 0.73 ycenter 2.10 zoom 0.5 rotate -90
    $ renpy.pause(3, hard=True)
    bsar_us "Ну что ты. Слушай, а возьми, пожалуйста, ещё это..." 
    bsar_narrator "Девушка протягивает мне сложенный вчетверо тетрадный листок." 
    bsar_narrator "Я уже собирался его развернуть, как Ульяна меня остановила." 
    bsar_us "Подожди. Не читай его сейчас, пожалуйста. Потом. Вечером, когда будешь ложиться спать." 
    bsar_narrator "Она густо краснеет, переводит взгляд вниз, изредка поглядывая на меня смущённым взглядом. К еде она так и не притронулась." 
    bsar_protagonist "Да, конечно. Без проблем." 
    bsar_us "Спасибо. Я пойду." 
    bsar_protagonist "А как же завтрак?" 
    bsar_us "Я не особо голодна. Возьму с собой. Пока." 
    bsar_protagonist "Ага. Увидимся." 
    hide bsar_us with dissolve
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(1) 
    scene bg bsar_ext_square_winter_day
    show bsar_mz out_normal at center
    with Dissolve(1)
    play music bsar_fripperies fadein 2
    play ambience bsar_winter_wind fadein 2
    bsar_mz "...поэтому мне и нравится творчество Лермонтова." 
    bsar_protagonist "Думаю, что ты права. Особенно мне понравился твой взгляд на «Героя нашего времени»." 
    bsar_mz "Да-а. Часть людей слишком поверхностно знакомится с этим произведением и не понимает вложенного в роман смысла." 
    bsar_protagonist "Кстати, хотел спросить, ты не видела Славяну?" 
    bsar_mz "Видела. Вчера вечером куда-то собиралась, но куда — не сказала." 
    bsar_protagonist "А ты у вожатой спрашивала?" 
    bsar_mz "Не-а. Зачем?" 
    bsar_narrator "И вправду, зачем? {w}Почему я до сих пор переживаю за Славю, хоть и решил, что это меня не касается?"
    bsar_narrator "Не знаю. Но почему-то изнутри гложет чувство, словно я ей что-то должен. А что должен — поди разбери." 
    bsar_narrator "Завтра поход. Она наверняка будет там." 
    show bsar_mz out_normal:
        linear 1.0 xalign 0.72
    $ renpy.pause(1.0, hard=True)
    show bsar_dv normal at left with dissolve
    bsar_dv "Какие люди!"
    bsar_mz "Двачевская."
    bsar_dv "Привет, мышка-Женя."
    bsar_mz "Ты неисправима! Мне пора в библиотеку."
    bsar_protagonist "Удачи."
    bsar_narrator "Женя выпрямилась, слегка откинула голову и свела брови. Со стороны казалось, что она смотрит на ДваЧе сверху вниз, хоть и ниже неё на полголовы."
    hide bsar_mz with dissolve
    bsar_narrator "Затем она резко повернулась к нам спиной и быстро засеменила в сторону библиотеки."
    show bsar_dv normal:
        linear 1.0 xalign 0.5
    $ renpy.pause(1.0, hard=True)
    bsar_protagonist "Злая ты, Алиса. Ты вообще хоть кого-то любишь?"
    bsar_dv "Животных люблю. Кто-то там кошек любит, кто-то собак, а я всех люблю без разбора."
    bsar_dv "Людей только не люблю. Надоели. Постоянно носятся туда-сюда."
    bsar_dv "Агрессивные какие-то."
    bsar_protagonist "Агрессивные?"
    bsar_narrator "Я усмехнулся. Алиса нахмурилась."
    bsar_dv "Что смешного?"
    bsar_protagonist "Ничего. Как ты?"

    if bsar_insomnia_day2_intervene: 
        bsar_narrator "Алиса едва заметно сморщила нос и сжала губы, сделав небольшой шаг в сторону." 
        bsar_dv "Не твоё дело, подслушиватель!" 
        bsar_protagonist "Это случайно получилось!" 
        bsar_dv "Да-да. Ври больше! Случайно у него получилось." 
        bsar_narrator "Я глубоко вздохнул и закатил глаза. Спокойно. {w}Раз. {w}Два. {w}Три." 
        bsar_protagonist "Думай, что хочешь." 
        hide bsar_dv with dissolve 
        bsar_narrator "Махнув рукой, я развернулся и пошёл прочь с площади. Алиса крикнула мне вслед то ли «дурак», то ли «дубина». Не имеет значения." 
        jump bsar_insomnia_day3_after_dv  

    else:
        bsar_narrator "Пионерка улыбнулась, немного опустив брови." 
        bsar_dv "Вполне неплохо. Весело вчера было." 
        bsar_protagonist "Да, только я всё равно не одобряю это проникновение со взломом." 
        bsar_dv "Коне-е-ечно. Сам-то булочки за обе щеки уплетал." 
        bsar_protagonist "Хорошо-хорошо. Твоя правда." 
        bsar_dv "Кстати, ты не знаешь, что с Ульяной?" 
        bsar_protagonist "А что с ней не так?" 
        bsar_dv "Слишком активная стала, улыбается постоянно. Сегодня прибежала в домик, долго копалась в вещах, потом что-то писала, а что писала — ни под каким предлогом не сказала." 
        bsar_protagonist "Тебе лучше знать." 
        bsar_dv "Ясно." 
        bsar_protagonist "Подожди-ка. Вы же живёте в разных домиках?" 
        bsar_dv "А. Прикинь, Ольга сегодня утром пришла и сказала, что мы наконец-то можем съехаться, мол это её новогодний подарок. Вот теперь вещи перетаскиваем потихоньку." 
        bsar_narrator "Алиса дёрнула головой, чтобы убрать локон волос, полезший в глаза, и скрестила руки на груди. Повисло молчание."  
        bsar_narrator "Мне кажется или воздух стал горячее?" 
        bsar_narrator "По площади туда-сюда носились пионеры из младших отрядов. Играли в снежки, лепили снеговиков, строили снежные крепости. Весело быть детьми."  
        bsar_narrator "Проблемы, которые сейчас давят, подобно каменной глыбе, неожиданно упавшей на голову, для детей всего лишь мелочь." 
        bsar_protagonist "Кстати, та записка. Она её для меня написала, похоже." 
        bsar_dv "Ну, и чего ты молчал? Что там?" 
        bsar_protagonist "Ульяна попросила её вечером прочитать." 
        bsar_dv "Понятно. Девочка-то влюбилась!" 
        bsar_protagonist "Ты явно преувеличиваешь." 
        bsar_dv "Может быть, но смотри мне! Только попробуй её обидеть..." 
        bsar_protagonist "Не обижу. Можешь не продолжать." 
        bsar_dv "Ладно. Я пойду." 
        bsar_protagonist "Ага." 
        hide bsar_dv with dissolve 
        jump bsar_insomnia_day3_after_dv 

label bsar_insomnia_day3_after_dv:
    stop music fadeout 2
    $ renpy.block_rollback()
    bsar_narrator "А что, если Алиса права?" 
    bsar_narrator "Ладно. Спешить некуда. Вечером узнаю." 
    scene bg black with Dissolve(1)
    $ renpy.pause(2, hard=True)
    $ bsar_set_time("night", "day")
    scene bg bsar_ext_square_winter_night_tree with Dissolve(1) 
    play music bsar_domitori_taranofu_winter_night fadein 2 
    bsar_narrator "Новый год подбирался всё ближе и ближе, скрываясь за предпоследним листом календаря. " 
    bsar_narrator "Вся площадь была обряжена в яркие украшения. От гирлянд и разноцветной мишуры до игрушек и вырезанных из бумаги снежинок, создавая неповторимую атмосферу скорого торжества."  
    bsar_narrator "Этот день сулил множество праздничных хлопот для всех обитателей лагеря. Ну, почти для всех... " 
    bsar_narrator "Лампочки мигали и переливались, как бы крича о том, что тут самое праздничное место в округе. На лавочке недалеко от ёлки сидела Лена и читала книгу." 
    show bsar_un normal with dissolve 
    bsar_protagonist "Привет, Лен!" 
    bsar_un "Привет." 
    bsar_protagonist "Красивая ёлка." 
    bsar_un "Да, красивая." 
    bsar_narrator "Девушка неопределённо пожимает плечами и снова углубляется в чтение." 
    bsar_narrator "Лена. Ассоциальная и крайне застенчивая девушка."
    bsar_narrator "За прошедшие две недели мы практически не общались."
    bsar_narrator "Она любит до позднего вечера засиживаться на площади в обнимку с книжкой."  
    bsar_narrator "Никогда не видел её в шумных компаниях. Это всё, что я могу сказать про неё. Такая вот зеленоглазая девочка-тихоня." 
    bsar_protagonist "Помнишь, как встречала новый год в детстве?" 
    bsar_narrator "Лена почему-то оживилась. Закрыла книгу и положила себе на колени." 
    bsar_un "Да, помню, как отец наряжался в костюм Деда Мороза и выходил в подъезд, чтобы за десять минут до нового года позвонить в звонок, а затем вручить подарки. Я, конечно, всё понимала, и..." 
    bsar_narrator "Лена запнулась, видимо поняв, что слишком разговорилась. Спустя пару мгновений, говоря уже более тихим голосом, она закончила рассказ." 
    bsar_un "...всегда подыгрывала ему." 
    bsar_narrator "А у меня также было? Вроде бы да. Также." 
    bsar_protagonist "Да... Раньше было очень здорово." 
    bsar_un "А сейчас разве нет?" 
    bsar_protagonist "Ну не сказать, что уж слишком. {w}Кстати, я слышал, что Мику заболела. Не знаешь, что с ней?" 
    bsar_narrator "Лена печально вздохнула и перевела взгляд своих студёных зелёных глаз на меня." 
    bsar_un "Ангина. Жалко её." 
    bsar_protagonist "Всё будет хорошо." 
    bsar_un "Ты плохо спишь, да?" 
    bsar_narrator "Со вздохом я покачал головой из стороны в сторону." 
    bsar_protagonist "Снятся кошмары." 
    bsar_narrator "Она снова посмотрела на меня и улыбнулась, а по лицу — тени. Девушка собиралась что-то сказать, но передумала." 
    bsar_un "Прости, что спросила. Знаешь, мне уже пора бежать. Пока." 
    bsar_narrator "Тихий голос девушки слился с ветром и унёс сказанные ею слова куда-то в сторону. Но, по всей видимости, она попрощалась." 
    bsar_protagonist "Прощай, Лена." 
    hide bsar_un with dissolve 
    bsar_narrator "Я вздохнул и засунул руки в карманы. {w}Новый год, значит?" 
    stop music fadeout 2 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard=True)
    scene bg int_house_of_mt_night2 with Dissolve(1) 
    play ambience ambience_medstation_inside_night fadein 2
    play sound_loop bsar_couch fadein 2
    bsar_narrator "В домик я вернулся пустым и уставшим."
    bsar_narrator "Этот день казался противоестественно длинным, как будто в сутках появился ещё один, а может и все два лишних часа." 
    bsar_narrator "Несмотря на минусовую температуру за окном, мне было невероятно жарко, словно моя комнатушка превратилась в «ЗИЛовскую» микроволновку."  
    bsar_narrator "Записка. {w}Ульяна же просила меня прочитать её вечером. Как я мог забыть?"
    bsar_narrator "Кое-как повесив амулет над изголовьем кровати, я лёг на одеяло в одежде."  
    bsar_narrator "Потом. {w}Всё потом. Времени до отбоя у меня ещё много. Даже Ольга ещё не пришла."
    show bsar_us_note with dissolve
    bsar_narrator "В послании было всего два предложения."
    bsar_narrator "По телу пробежали мурашки, а жар почему-то прошёл."
    bsar_narrator "Кратко и лаконично. Буквы на листке бумаги не будут заикаться, краснеть и отводить взгляд. {w}Так проще."
    hide bsar_us_note with dissolve
    bsar_narrator "И всё-таки Алиса была права. А ведь и вправду, на моей памяти она не разу не ошибалась."
    bsar_narrator "Если я скажу, что у меня нет чувств к Ульяне, я буду полным лжецом."  
    bsar_narrator "Мне захотелось поговорить с ней до назначенного времени, но усталость напомнила о себе." 
    bsar_narrator "Я зевнул так, что чуть не свело челюсть, а глаза начали слипаться. Ладно. {w}Потом. {w}Всё потом. Времени у меня ещё много..."
    $ bsar_set_time("bw", "day")
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    scene bg bsar_prolog_bw
    show bsar_static_noise_anim
    with bsar_flash 
    play ambience bsar_hum fadein 2 
    bsar_she_red "Прости..." 
    bsar_protagonist "За что?"
    bsar_she_red "Я... я не смогла тебе помочь. Время вышло. Придётся смириться с неотвратимым."
    $ bsar_show_centered_text("Свобода.", style=style.bsar_insomnia_centered_text_style)
    $ bsar_show_centered_text("Свобода от оков.", style=style.bsar_insomnia_centered_text_style)
    $ bsar_hide_centered_text(dspr)
    bsar_narrator "Снова {i}та{/i} лёгкость и безмятежность. Чувствую себя... живым." 
    $ bsar_show_centered_text("Да, ЖИВЫМ!", style=style.bsar_insomnia_centered_text_style)
    $ bsar_hide_centered_text(dspr)
    bsar_she_red "Нам пора встретиться. Кажется..."
    $ renpy.pause(1, hard=True)

    if persistent.font_size == "large":
        bsar_she_red "{bsar_scare}{=bsar_scared_text_red_large}Кажется, я умираю.{/=bsar_scared_text_red_large}{/bsar_scare}"

    elif persistent.font_size == "small":
        bsar_she_red "{bsar_scare}{=bsar_scared_text_red_small}Кажется, я умираю.{/=bsar_scared_text_red_small}{/bsar_scare}"

    bsar_she_red "Но что-то дало мне силы на последний рывок." 
    bsar_protagonist "Как ты можешь умереть?" 
    bsar_she_red "С того момента, как я сюда попала, силы стремительно покидают меня. {w}Я не смогла. {w}Ты не вспомнил."
    bsar_she_red "Позволь дать тебе ответы перед..."
    $ bsar_set_time("fog", "day")
    scene bg bsar_ext_house_of_mt_fog with bsar_flash
    play music bsar_dark_shades fadein 5
    bsar_narrator "Ужасный кашель обжигает и раздирает горло. Я падаю на землю, пытаясь откашляться." 
    $ renpy.pause(1, hard=True) 
    bsar_narrator "Спустя какое-то время мне становится лучше."
    $ bsar_show_centered_text("Где я?", style=style.bsar_insomnia_centered_text_style)
    $ bsar_hide_centered_text(dspr)
    bsar_narrator "Кругом мертвенная тишина, которую нарушает только гулкий стук моего сердца." 
    bsar_narrator "Всё застилала густая молочная мгла. Не могу толком ничего разглядеть дальше одного ярда." 
    bsar_she_red "Ты слышишь меня? Ты должен слышать! Иди ко мне." 
    bsar_protagonist "Но куда я должен идти?" 
    bsar_narrator "Мой голос сорвался на более низкую ноту, а окончание вопроса поглотил этот необъятный туман." 
    bsar_she_red "Ты знаешь, куда тебе нужно. Просто иди." 
    bsar_narrator "И я пошёл." 
    scene bg bsar_ext_square_fog with dissolve 
    bsar_narrator "Кажется, я вышел на площадь, когда споткнулся и ударился о что-то металлическое."

    if persistent.font_size == "large":
        bsar_narrator "{bsar_scare}{=bsar_scared_text_style_large}Дыхание участилось, а руки пробил тремор.{/=bsar_scared_text_style_large}{/bsar_scare}"

    elif persistent.font_size == "small":
        bsar_narrator "{bsar_scare}{=bsar_scared_text_style_small}Дыхание участилось, а руки пробил тремор.{/=bsar_scared_text_style_small}{/bsar_scare}"

    bsar_narrator "Лавочка. {w}Просто лавочка. {w}Нужно идти дальше." 
    scene bg bsar_ext_path2_fog with dissolve 
    bsar_narrator "Что происходит?" 
    bsar_narrator "Я уже сошёл с ума? Куда я вообще иду? Не знаю!"
    $ bsar_show_centered_text("Я НЕ ЗНАЮ, ЧЁРТ ПОБЕРИ!", style=style.bsar_insomnia_centered_text_style)
    $ bsar_hide_centered_text(dspr)
    bsar_narrator "Нет, нет, нет. {w}Нельзя терять самообладание. {w}Нужно идти."
    bsar_narrator "Идти..."
    scene bg bsar_ext_old_building_fog with dissolve
    bsar_narrator "Неожиданно туман начал рассеиваться, и я смог разглядеть обветшалое уродливое здание." 
    bsar_narrator "Щербатая улыбка крыши, зияющая пробоинами, и пустые глазницы окон, смотрящие в пустоту." 
    bsar_narrator "Кажется, Ольга рассказывала мне про это место. Старый корпус. Мне сюда. Точно сюда."
    stop music fadeout 2
    scene bg bsar_int_old_building_night_edited with dissolve 
    bsar_protagonist "Что даль..." 
    stop ambience fadeout 2
    $ bsar_set_time("bw", "day")
    scene bg bsar_form 
    show bsar_static_noise_anim
    with bsar_flash
    play ambience ambience_medstation_inside_night fadein 2
    play music bsar_defeated_clown fadein 2
    bsar_she_red "Это пионерская форма твоей сестры?" 
    bsar_protagonist "Да. Она часто мне рассказывала о том пионерлагере." 
    bsar_protagonist "«Совёнок»! Я то сам в детских лагерях никогда и не бывал, а пионером уж подавно не был. Советы через год после моего рождения развалились." 
    bsar_she_red "И много она тебе рассказала?" 
    bsar_protagonist "Да-а. Я себе этот лагерь по её рассказам столько раз представлял." 
    bsar_protagonist "Во всех подробностях. Мечтал когда-нибудь попасть в него. {w}Эх, детские грёзы. Не хочу, чтобы после её смерти эти вещи пылились в каком-то чулане." 
    bsar_she_red "А меня бы с собой взял?" 
    bsar_protagonist "Куда?" 
    bsar_she_red "В «Совёнок»!" 
    bsar_protagonist "Взял бы, конечно! Это бы были прекрасные воспоминания!" 
    bsar_protagonist "{i}Воспоминания на всю жизнь!{/i}" 
    stop ambience fadeout 2
    $ bsar_set_time("fog", "day")
    scene bg bsar_int_old_building_night_edited 
    show bsar_she_night
    with bsar_flash
    play ambience bsar_hum fadein 2
    bsar_she_red "Дальше я дам тебе ответы, какие смогу, но времени у нас мало и то, что ты увидишь, может повлиять на исход всего." 

    menu:
        "Где я?":
            bsar_she_red "Как ты мог понять по пробившимся к тебе фрагментам памяти, случились две трагедии. Сначала в аварии скончалась твоя сестра. Затем погибла... {w}Я."
            $ bsar_set_time("bw", "day") 
            scene bg bsar_medical_room_celling 
            show bsar_static_noise_anim
            with bsar_flash
            play sound_loop bsar_hum fadein 2
            bsar_doctor "Примите мои соболезнования. Мы сделали всё, что смогли, но она скончалась, не выйдя из комы."  
            bsar_protagonist "Когда я смогу забрать тело?"  
            bsar_doctor "Но... Вам не нужно время, чтобы...."  
            bsar_protagonist "Она умерла. С этим просто нужно смириться. Когда я смогу забрать тело?"
            stop sound_loop fadeout 2
            $ bsar_set_time("fog", "day")
            scene bg bsar_int_old_building_night_edited
            show bsar_she_night
            with bsar_flash 
            bsar_she_red "Это было для тебя страшным ударом. {w}Ты просто не выдержал. Пара недель беспробудного пьянства, безрезультатные попытки сослуживцев достучаться до тебя." 
            bsar_she_red "В конце концов, ты сделал неправильный выбор."
            $ bsar_set_time("bw", "day")
            scene bg bsar_makarov_pistol
            show bsar_static_noise_anim
            with bsar_flash
            play sound_loop bsar_hum fadein 2
            $ renpy.pause(1.5, hard=True)
            scene bg white with bsar_flash
            play sound bsar_handgun
            $ renpy.pause(1, hard=True)
            show blink
            $ renpy.pause(2, hard=True)
            scene bg bsar_prolog_bw behind blink
            show bsar_static_noise_anim behind blink
            hide blink
            with bsar_flash
            bsar_fox_orange "Какие у него шансы выйти из комы, Иван Степанович?"
            bsar_doctor "Огнестрельное в голову — это не шутки. Удивительно, что он вообще смог выжить." 
            bsar_fox_orange "Зачем ты так?" 
            bsar_doctor "Ладно, милочка, вашему другу нужен покой. Пойдемте."
            stop sound_loop fadeout 2
            $ bsar_set_time("fog", "day")
            scene bg bsar_int_old_building_night_edited
            show bsar_she_night
            with bsar_flash
            bsar_she_red "И вот мы здесь." 
            $ bsar_show_centered_text("{bsar_scare}{=bsar_scared_text_centered}Время пришло.{/=bsar_scared_text_centered}{/bsar_scare}", style=style.bsar_insomnia_centered_text_style)
            $ bsar_show_centered_text("{bsar_scare}{=bsar_scared_text_centered}Прости.{/=bsar_scared_text_centered}{/bsar_scare}", style=style.bsar_insomnia_centered_text_style)

        "Кто ты?":
            $ bsar_insomnia_paradise_ending_v += 1 
            stop ambience fadeout 2
            $ bsar_set_time("bw", "day")
            scene bg bsar_ext_roof
            play ambience bsar_winter_wind fadein 2
            show bsar_snow_layer3_anim_quick
            show bsar_snow_layer2_anim_quick
            show bsar_she normal
            show bsar_snow_layer1_anim_quick
            show bsar_snow_layer0_anim_quick
            show bsar_static_noise_anim
            with bsar_flash
            bsar_she_red "Так и знала, что найду тебя здесь!" 
            bsar_protagonist "Неужели я настолько предсказуем?" 
            bsar_she_red "Нет. Конечно нет. Просто ты мне сам как-то рассказывал, что тебе здесь нравится из-за...{w=1.0}{nw}" 
            bsar_protagonist "Из-за того, что тут очень спокойно." 
            bsar_she_red "И очень холодно." 
            bsar_she_red "Значит завтра ты всё-таки уезжаешь?" 
            bsar_protagonist "Да. Завтра я уезжаю."  
            bsar_she_red "Я буду ждать. Только не забывай о том, что я говорила, хорошо?" 
            bsar_protagonist "{i}«Чтобы не случилось, я всегда найду к тебе дорогу?»{/i}"  
            bsar_she_red "Именно!"

    stop ambience fadeout 2
    $ bsar_set_time("bw", "day")
    $ renpy.pause(1, hard=True)
    scene bg bsar_heart_monitor 
    show bsar_heart_monitor_frame
    with bsar_flash
    play sound_loop bsar_hum
    $ renpy.pause(1, hard=True)
    $ bsar_show_heart_monitor_phrases("military_service")
    $ bsar_show_heart_monitor_phrases("composure")
    $ bsar_show_heart_monitor_phrases("institute")
    $ bsar_show_heart_monitor_phrases("meeting_with_her")
    $ bsar_show_heart_monitor_phrases("love")
    $ bsar_show_heart_monitor_phrases("police_work")
    $ bsar_show_heart_monitor_phrases("fox")
    $ bsar_show_heart_monitor_phrases("friendship")
    $ bsar_show_heart_monitor_phrases("rest")
    $ bsar_show_heart_monitor_phrases("easy_money")
    $ bsar_show_heart_monitor_phrases("protection")
    $ bsar_show_heart_monitor_phrases("drug_trafficking")
    $ bsar_show_heart_monitor_phrases("sisters_death")
    $ bsar_show_heart_monitor_phrases("nightmares")
    $ bsar_show_heart_monitor_phrases("doubts")
    $ bsar_show_heart_monitor_phrases("new_deal")
    $ bsar_show_heart_monitor_phrases("her_death")
    stop sound_loop fadeout 2
    stop music fadeout 2

    if bsar_insomnia_paradise_ending_v == 3:
        jump bsar_insomnia_paradise_ending

    else:
        jump bsar_insomnia_awakening_ending

label bsar_insomnia_awakening_ending:
    scene bg black with bsar_flash
    play sound bsar_heart_stopped
    $ renpy.pause(6, hard=True)
    scene bg white with bsar_flash
    $ renpy.pause(1, hard=True)
    
    if not persistent.insomnia_achievements["insomnia_awakening"]:
        $ persistent.insomnia_achievements["insomnia_awakening"] = True
        $ insomnia_show_achievement("insomnia_awakening")

    $ renpy.pause(1, hard=True)
    scene bg black with dissolve
    stop sound_loop fadeout 2
    $ renpy.pause(1, hard=True)
    $ insomnia_set_main_menu_cursor()
    return

label bsar_insomnia_paradise_ending:
    $ bsar_show_heart_monitor_phrases("sleep_that_knows_no_breaking")
    scene bg white with bsar_flash
    play sound bsar_heart_stopped
    $ renpy.pause(6, hard=True)
    $ bsar_set_time("day")
    $ renpy.pause(1, hard=True)
    scene bg bsar_ext_road_winter_day with bsar_flash
    play ambience bsar_winter_wind fadein 2
    play music bsar_nightwish_nemo_piano_cover fadein 2
    bsar_narrator "Ну вот я и приехал в пионерлагерь «Совёнок»."
    scene bg bsar_ext_camp_entrance_winter_day with dissolve
    bsar_narrator "Из-за небольших проволочек с документами я задержался и приехал на день позже, но ничего страшного в этом нет, ведь впереди меня ждут целых три недели отдыха!" 
    show bsar_us smile with dissolve
    bsar_narrator "Из-за ворот вдруг выглянула девочка, она подошла поближе и улыбнулась."  
    bsar_narrator "Очень симпатичная, кстати. Огненные, как цветок мака волосы, и голубые глаза, в которых, казалось, можно утонуть. Она невысокого роста, на вид ей лет шестнадцать. " 
    bsar_usp "Привет, ты, наверное, только что приехал?" 
    bsar_protagonist "Да. Только что."

    if not persistent.insomnia_achievements["insomnia_paradise"]:
        scene bg bsar_titles_bg with Dissolve(1.5)
        $ persistent.insomnia_achievements["insomnia_paradise"] = True

        show insomnia_titles_final insomnia_titles_text at insomnia_titles_anim
        $ renpy.pause(38, hard=True)

        $ insomnia_show_achievement("insomnia_paradise")

    $ renpy.pause(1, hard=True)
    scene bg black with dissolve
    stop music fadeout 2
    stop ambience fadeout 2
    $ renpy.pause(1, hard=True)
    #$ insomnia_set_main_menu_cursor()
    #return