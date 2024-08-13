label bsar_insomnia_day1:
    stop music fadeout 3
    $ save_name = ("День первый.")
    $ renpy.block_rollback()
    $ bsar_onload("lock")
    $ renpy.pause(4, hard=True)
    $ persistent.sprite_time = "day"
    $ persistent.timeofday = "winter_night"
    $ renpy.movie_cutscene(bsar_gui_path + "days_transitions/bsar_insomnia_day1.ogv")
    scene bg black
    $ renpy.pause(3.5, hard=True)
    $ bsar_set_mode_nvl() 
    scene bg insomnia_prolog_blue with Dissolve(3)
    $ renpy.pause(1, hard=True)
    $ bsar_onload("unlock")
    $ bsar_set_dynamic_cursor('timeofday')
    play music bsar_insomnia_domitori_taranofu_slow_pulse fadein 3
    bsar_narrator "{i}В этом мире есть множество вещей, которые нельзя объяснить. {w}Их невозможно понять, невозможно увидеть и доказать, но тем не менее они существуют.{/i}"
    bsar_narrator "{i}Сон - одна из этих вещей.{/i}"
    bsar_narrator "{i}Ещё наши предки считали, что во время сна душа может покидать физическое тело и, пересекая тонкую, невидимую человеческому глазу грань, путешествовать в другие миры.{/i}" 
    bsar_narrator "{i}Поэтому, никто не может гарантировать Тебе, что вся Твоя жизнь - это не сон. {w}Сон, в котором пленённое тело переживает подобные друг другу дни снова и снова. Бесчисленное число раз...{/i}" 
    $ renpy.pause(1, hard=True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw"
    scene bg insomnia_prolog_bw
    show insomnia_she
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience insomnia_hum fadein 2
    nvl clear
    insomnia_she "Ты..."
    insomnia_she "Ты должен..."
    insomnia_she "Если ты вспомнишь, что я тогда сказала..."
    insomnia_she "Ты должен вспомнить!"
    insomnia_he "Кто ты? Что я должен вспомнить?"
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with insomnia_flash
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day"
    nvl clear
    play ambience ambience_int_cabin_day fadein 2
    play sound_loop insomnia_alarm_clock fadein 2 
    bsar_narrator "От громкого звона будильника создаётся впечатление, что мне в голову вбивают гвозди. Этот противный звон эхом распространяется по всей комнате, заставляя меня сделать хоть что-то."
    hide blink 
    scene bg insomnia_int_house_of_mt_day_blurred behind blink 
    show unblink 
    $ renpy.pause(2, hard = True)
    stop sound_loop fadeout 2 
    bsar_narrator "Брошенная наотмашь подушка заставила замолкнуть эту адскую машину." 
    bsar_narrator "Чувствую себя потерянным, словно старая безделушка, которая ранее, по идее, приносила удачу, а сейчас пылится где-то под диваном, ожидая, когда кто-то случайно её найдёт." 
    play sound_loop insomnia_knock fadein 2
    scene bg int_house_of_mt_day with Dissolve(1.5)
    $ renpy.pause(2, hard = True)
    bsar_narrator "Резкий стук в дверь возвращает меня в реальность. Раз, другой, третий."
    show blink
    $ renpy.pause(2, hard = True)
    bsar_narrator "Я накрываюсь одеялом с головой в надежде, что этот незваный гость просто уйдёт." 
    stop sound_loop fadeout 2 
    bsar_narrator "Через какое-то время стук прекращается. Похоже, мой экзекутор смирился со своим поражением." 
    bsar_narrator "Но как ни крути, думать, что я скоро снова засну, было очень наивно с моей стороны. {w}Я ворочаюсь с бока на бок, но сон так и не приходит."
    hide blink
    show unblink
    $ renpy.pause(2, hard = True)
    bsar_narrator "Посмотрев на часы, я замечаю, что давно проспал завтрак, и мне придётся ходить голодным до самого обеда."
    insomnia_th "Человек, который первым сказал, что утро добрым не бывает, был абсолютно прав."
    nvl clear
    play sound sfx_open_door_1
    $ renpy.pause(2, hard = True)
    stop ambience fadeout 2
    scene bg insomnia_ext_houst_of_mt_winter_day with dissolve
    play ambience insomnia_winter_wind fadein 2
    $ renpy.pause(1.5, hard = True)
    scene bg insomnia_ext_houses_winter_day with dissolve
    $ renpy.pause(1.5, hard = True)
    scene bg insomnia_ext_square_winter_day with dissolve
    $ renpy.pause(1.5, hard = True)
    bsar_narrator "Я более или менее привёл себя в порядок и не нашёл занятия лучше, чем посиделки на площади вместе с товарищем Гендой, который всё таким же каменным и тотально безучастным взглядом смотрел в пустоту."  
    bsar_narrator "Устроившись на самой дальней скамейке, я попытался понять, что за чертовщина стала мне сниться. Кошмары? Может быть. Ничего не могу вспомнить."  
    bsar_narrator "Вроде бы уже почти ухватился за что-то важное, значимое, как это что-то упорхает от меня, взмахнув крыльями, подобно Жар-птице." 
    bsar_narrator "Вдруг краем глаза я заметил, что рядом со мной кто-то стоит."  
    bsar_narrator "Я непроизвольно вздрогнул, что вызвало ехидный смешок у заставшей меня врасплох пионерки." 
    $ bsar_set_mode_adv() 
    show insomnia_us normal with dissolve
    play music insomnia_afternoon fadein 4
    bsar_narrator "Ульяна. Девочка-апокалипсис." 
    bsar_narrator "Из-за её детской непосредственности мы не раз встревали в разного рода авантюры, и почти всегда нам приходилось отдуваться." 
    bsar_narrator "Но всё же, несмотря на все ее проделки, на неё решительно невозможно злиться. И я покривлю душой, если скажу, что мне с ней не весело."
    insomnia_protagonist "И давно ты здесь стоишь, Ульяна?" 
    insomnia_us "Ты вообще когда-нибудь улыбаешься?" 
    insomnia_protagonist "Да. {w}Наверное." 
    insomnia_us "Как так вообще можно жить? Почему ты уже второй день ходишь с кислой миной? Сторонишься всех, а вчера вообще прошёл мимо и даже не поздоровался!" 
    bsar_narrator "Ульяна интересуется моим состоянием. Один этот факт уже вызывает массу подозрений, но что-то в её взгляде ясно даёт понять - ей и вправду это интересно." 
    insomnia_protagonist "Извини, Уль. Просто чертовски скверное настроение в последнее время." 
    bsar_narrator "Но я же не соврал. Просто сказал не всю правду."
    insomnia_us "Э-эй! Вообще-то человек настроение сам себе делает. Никто, кроме тебя, его тебе не сделает. Как ты сам для себя решил, так и будет!"
    insomnia_us "Вот если ты сам для себя решил: «Всё. Мне весело!», - то тебе весело, а если ты решил, что тебе грустно, так и будет."
    bsar_narrator "Голубые глаза девушки горят энтузиазмом, словно она Уоллес, говорящий воодушевляющую речь перед сынами Шотландии. Причём в несвойственной для себя простодушной манере."
    bsar_narrator "Поэтому, я с неподдельным интересом и заинтересованностью слушаю её наставляющий монолог." 
    insomnia_us "Вроде и старше меня, но до сих пор не понял этого..."
    insomnia_us "Улыбнись, дурак!" 
    bsar_narrator "Как ни странно, но от слов этой рыжеволосой энергичной девчонки на сердце стало... {w}Теплее что ли. Эти слова колыхнули фибры души, напоминая о каком-то совсем позабытом чувстве."
    show insomnia_us dontlike with dspr
    bsar_narrator "Я искренне улыбнулся Ульяне, получив такую же, но более озорную улыбку в ответ, которая почему-то сменилась лёгким румянцем на щеках и убегающим куда-то взглядом."
    bsar_narrator "А может мне просто показалось."
    play sound sfx_dinner_horn_processed fadein 2
    $ renpy.pause(3, hard = True)
    bsar_narrator "Неловкую паузу прервал горн. Пора на обед."
    show insomnia_us normal with dspr
    insomnia_us "Пошли на обед, дурак. Завтрак, как я понимаю, ты проспал."
    hide insomnia_us with dissolve
    bsar_narrator "Хихикнула она и быстро зашагала в сторону столовой. Мне пришлось поторопиться, чтобы не отставать."
    stop music
    play sound_loop insomnia_heart
    scene bg insomnia_ext_square_winter_day:
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

    $ insomnia_heartbeat_animation("bg insomnia_ext_square_winter_day", 1.05, 1.0)
    bsar_narrator "Неожиданно перед глазами всё пошло кувырком..." 
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw"
    scene bg insomnia_ext_winter_park
    show insomnia_snow_layer3_anim
    show insomnia_snow_layer2_anim
    show insomnia_she
    show insomnia_snow_layer1_anim
    show insomnia_snow_layer0_anim
    show insomnia_static_noise_anim
    with insomnia_flash
    play sound_loop insomnia_hum fadein 2
    play ambience insomnia_winter_wind fadein 2
    play music insomnia_lucas_king_hurt fadein 2
    insomnia_he "Холодно же! Хватит! Выкинь! Выкинь снежок, кому говорю?" 
    insomnia_she "Ладно, ладно." 
    insomnia_he "Ты когда-нибудь станешь менее инфантильной?" 
    insomnia_she "Не стану. К тому же, разве это что-то плохое?"  
    insomnia_he "Ну вот. Опять эта ехидная улыбка! На тебя просто невозможно злиться."  
    insomnia_she "А на меня и не нужно злиться, дурак."
    insomnia_she "Ты, кстати, уже решил, что подаришь сестре на день рождения?" 
    insomnia_he "Всё ещё думаю." 
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day" 
    $ persistent.sprite_time = "day"
    scene bg insomnia_ext_square_winter_day
    show insomnia_us sad at center
    with insomnia_flash
    play ambience insomnia_winter_wind fadein 2
    play sound_loop insomnia_heart
    $ insomnia_heartbeat_animation("bg insomnia_ext_square_winter_day", 1.02, 1.0)
    $ insomnia_heartbeat_animation("insomnia_us sad", 1.02, 1.0)
    play ambience insomnia_winter_wind fadein 2
    insomnia_us "Эй, как можно было на ровном месте упасть?" 
    bsar_narrator "Что это, чёрт побери, было? Я упал и..." 
    bsar_narrator "Не помню. Наверное, просто показалось."
    stop sound_loop fadeout 2
    scene bg insomnia_ext_square_winter_day
    show insomnia_us sad
    with Dissolve(1.5)
    insomnia_us "А-у-у! Ты там живой? Может мне вожатую позвать?" 
    insomnia_protagonist "Всё в порядке. Я просто поскользнулся и упал." 
    insomnia_us "Припадочный ты какой-то. Хватит валяться!"
    show insomnia_us normal with dspr
    bsar_narrator "Ульяна улыбалась, но по беспокойному взгляду и едва заметным ноткам волнения в голосе можно понять, что она переживает за меня. Это... мило."
    scene bg insomnia_ext_dining_hall_away_winter_day with dissolve 
    bsar_narrator "По мере приближения к столовой вокруг появляется всё больше и больше пионеров, совершающих своё голодное паломничество. Ульяна не стала меня ждать и поспешно ретировалась." 
    scene bg insomnia_ext_dining_hall_near_winter_day with dissolve 
    bsar_narrator "Зазевавшись, я едва не сталкиваюсь с Алисой Двачевской, которую за глаза все называют ДваЧе." 
    show insomnia_dv normal with dissolve
    play music insomnia_ease fadein 2
    insomnia_dv "Эй! Смотри куда прёшь!" 
    bsar_narrator "Алиса была не в настроении, но мастерски скрывала это за надменным выражением лица. Ещё чуть-чуть и она буквально испепелит меня взглядом."
    insomnia_protagonist "Что-то случилось?" 
    show insomnia_dv normal2 with dspr 
    bsar_narrator "Она на мгновение удивлённо вскинула бровь."
    bsar_narrator "Хоть постороннему человеку это будет не заметно, но за время проведённое здесь, тени злости и обиды на лице этой пионерки ясны мне как гримасы боли." 
    bsar_narrator "По началу она казалась мне типичной хулиганкой из-за любви к всякого рода подколкам и нежеланию следовать правилам лагеря, но сейчас я понимаю, что она на самом деле добрая и наивная девушка, хоть и прячется под личиной хулиганки." 
    bsar_narrator "Причины её напускного образа мне, к сожалению, не ясны." 
    show insomnia_dv normal with dspr
    insomnia_dv "Ольга случилась! Приехала из райцентра сама не своя. Наорала на меня из-за..."
    insomnia_dv "Уф. Забудь. {w}Испортила мне всё настроение, чтоб её!" 
    insomnia_protagonist "Да будет тебе! Она же постоянно всех гоняет. Не стоит зацикливаться на этом и портить себе настроение." 
    bsar_narrator "Я тепло улыбнулся Алисе. Не стоит ожидать, что я получу от неё улыбку в ответ, но всё же на её лице не осталось и следа обиды." 
    insomnia_dv "Кто бы говорил. Сам то несколько дней уже ходишь с таким лицом, что у Лены цветы на подоконнике от твоего взгляда завяли." 
    insomnia_th "Похоже, что не одна Ульяна заметила изменения в моём поведении из-за этих ночных кошмаров. Вспомнить бы, что мне снится, раз это так влияет на моё состояние." 
    insomnia_protagonist "Как видишь, теперь я в полном порядке." 
    bsar_narrator "Сказал я, улыбнувшись ещё шире и пожав плечами." 
    insomnia_protagonist "А цветы могли и из-за холода завянуть. Зачем она их вообще с собой привезла?" 
    insomnia_dv "Сам её и спроси, если интересно." 
    bsar_narrator "Сквозь зубы сказала она."
    insomnia_th "Точно! Алиса же постоянно надоедает Ольге Дмитриевне из-за того, что их поселили вместе с Леной. Возможно, именно из-за очередной просьбы о расселении и сорвалась вожатая." 
    insomnia_th "Не понимаю, почему она так упёрлась и не хочет их расселить, ведь даже Ульянка пару проказ устроила, как раз из-за того, что её поселили со Славей, а не Алисой." 
    insomnia_th "Кстати, а зачем Ольга вообще ездила в Райцентр?" 
    insomnia_dv "Приём! Ты куда уставился то? Опять ворон считаешь?"
    insomnia_dv "Холодно тут. Пошли в столовую. Не хочу ещё и обед пропустить." 
    insomnia_protagonist "А? Да, конечно. Пошли." 
    stop ambience fadeout 2 
    stop music fadeout 2 
    scene bg insomnia_int_dining_hall_winter with dissolve 
    play ambience ambience_dining_hall_empty fadein 2 
    bsar_narrator "Из-за нашей задержки столовая заметно опустела. Почти все пионеры, отобедав, убежали по своим делам. Взяв еду, мы с Алисой разделились." 
    bsar_narrator "Что-то буркнув себе под нос, она села за столик с Ульяной, по взгляду которой можно было понять, что скоро в лагере случится что-то очень нехорошее." 
    bsar_narrator "Получив порцию, я сел за ближайший свободный столик."  
    bsar_narrator "Несмотря на то, что я не ел с самого утра, аппетита практически не было. Самозабвенно ковыряясь вилкой в тарелке, решил вернуться к этим странным снам." 
    bsar_narrator "Уже третий день я не высыпаюсь по ночам, а наутро чувствую себя просто отвратительно. Было ли такое раньше? Странно. Ничего не могу вспомнить."
    bsar_narrator "Я приехал в лагерь примерно две недели назад..."
    show insomnia_sl normal with dissolve
    insomnia_sl "Ты не против, если я присяду?" 
    insomnia_protagonist "Ч-что?" 
    insomnia_sl "Я присяду?" 
    insomnia_protagonist "А, конечно-конечно."
    scene bg insomnia_sl_normal with dissolve
    play music insomnia_stride fadein 4
    insomnia_sl "Ты последние дни слишком рассеянный. Завтрак сегодня пропустил и дверь не открыл, когда я стучалась. Проблемы со сном?"
    bsar_narrator "Славяна опустила брови и посмотрела на меня негодующим взглядом." 
    bsar_narrator "Она добрая, активная и ответственная девушка, которая всегда готова помочь. Как раз является помощницей Ольги, что вполне ожидаемо. {w}Правда, некоторые случайно обронённые слова или действия ставят под сомнения искренность её действий." 
    bsar_narrator "Я устало вздыхаю и опускаю подбородок на ладони, вспоминая, как плохо сегодня спал." 
    insomnia_protagonist "Да. В последнее время мне снятся кошмары."
    scene bg insomnia_sl_tired with dissolve
    bsar_narrator "Славяна немного дёргает головой, словно хочет что-то сказать, но не решается. Она выглядит... {w}уставшей."
    insomnia_protagonist "Ты не знаешь, зачем Ольга Дмитриевна ездила в райцентр?" 
    insomnia_sl "Она поехала забрать почту, но, кажется, у неё там ещё какое-то {i}личное дело.{/i} Правда, по приезде она сама не своя." 
    insomnia_protagonist "В смысле?" 
    insomnia_sl "Ну-у. Раздражительная какая-то стала. На Алису накричала." 
    bsar_narrator "В этот момент мимо нашего стола прошли Ульяна с Алисой, и, услышав своё имя, ДваЧе очень недобро глянула на Славю." 
    bsar_narrator "Похоже, у рыжей конфликт не только с Леной; наверное, здесь причина неприязни скрывается в чрезмерной правильности моей собеседницы." 
    insomnia_protagonist "Ты тоже неважно выглядишь..." 
    bsar_narrator "Чёрт! Какую же глупость я только что сморозил. Такое нельзя говорить девушке!" 
    insomnia_sl "Да-а, наверное, так и есть." 
    insomnia_sl "Замоталась в последнее время. Нужно отдохнуть. Я всё же в лагере или где?" 
    bsar_narrator "Мне показалось, что в её глазах промелькнул блеск, который до этого я видел только у Ульяны, когда она хочет влезть в какую-то авантюру." 
    insomnia_protagonist "Это славно." 
    bsar_narrator "Я участливо улыбнулся и кивнул головой." 
    insomnia_sl "Ладно. Тогда я пойду. Увидимся!"
    scene bg insomnia_int_dining_hall_winter with dissolve
    insomnia_protagonist "Да, давай." 
    bsar_narrator "Наверное, мне тоже стоит идти, иначе просижу в столовой до ужина..."
    stop music fadeout 1
    stop ambience fadeout 1
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw"
    scene bg insomnia_ext_winter_street
    show insomnia_snow_layer3_anim
    show insomnia_snow_layer2_anim
    show insomnia_sister
    show insomnia_snow_layer1_anim
    show insomnia_snow_layer0_anim
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience insomnia_winter_wind fadein 2
    play sound_loop insomnia_hum fadein 2
    play music insomnia_lucas_king_isolation fadein 2
    insomnia_he "Будешь праздновать день рождения в этом году?"  
    insomnia_sister "Да. Возьму отпуск и поеду к родителям, отдохну и маму с папой увижу. Что-то я замоталась с этой работой."  
    insomnia_he "Там же ещё лес рядом. Опять будешь в нём пропадать?" 
    insomnia_sister "Да-а. Как в детстве, когда за грибами в конце лета ходили. Помнишь?"  
    insomnia_he "Помню. Только я никогда это не любил."
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day"
    scene bg insomnia_int_dining_hall_winter with insomnia_flash
    play ambience ambience_dining_hall_empty fadein 2
    bsar_narrator "Ничего не понимаю. Что со мной происходит? Уже второй раз перед глазами всплывают образы, которые пропадают так же быстро, как и появляются." 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1)
    $ renpy.pause(1, hard = True)
    scene bg insomnia_ext_houses_winter_day
    show insomnia_heavy_snow_day
    show insomnia_normal_snow_day
    with Dissolve(1)
    play ambience insomnia_winter_wind fadein 2
    insomnia_mt "Пионер!"
    show insomnia_mt rage behind insomnia_normal_snow_day with dissolve
    insomnia_protagonist "Да? Что? Где?"
    bsar_narrator "Довольно резко прозвучавший рядом голос Ольги Дмитриевны выбил меня из колеи, спутав ход мыслей."
    insomnia_mt "Я знаю, что ты сегодня не пришёл на завтрак и, по всей видимости, поздно проснулся! Я надеюсь, ты понимаешь, что такое поведение не подобает настоящему пионеру?"
    bsar_narrator "Ольга сегодня и вправду какая-то взвинченная. Я редко слышал, чтобы она повышала голос, как сейчас."
    bsar_narrator "Да, конечно, она пытается быть строгой с пионерами. {w}Но ключевое слово - пытается."
    bsar_narrator "Например, она позволяла мне некоторые вольности, относясь с снисхождением к моим пропускам утреннего построения и далёкого от расписания подъёму."
    insomnia_protagonist "Да, извините, больше не повторится."
    insomnia_mt "Отлично! Осознание проблемы - половина её решения!"
    insomnia_protagonist "Да, конечно."
    show insomnia_mt angry behind insomnia_normal_snow_day with dspr
    insomnia_mt "Раз ты сейчас ничем не занят, то..."
    bsar_narrator "В раздумьях она играет локоном своих волос, пытаясь придумать мне поручение."
    insomnia_protagonist "Пионер понял, что ему нужно найти социально полезное занятие!"
    bsar_narrator "Прервал я её размышления, пока она не придумала мне что-то тяжёлое и энергозатратное."
    stop ambience fadeout 2
    scene bg black with Dissolve(1)
    $ renpy.block_rollback()
    $ renpy.pause(1, hard = True)
    $ persistent.timeofday = "winter_night"
    scene bg int_house_of_mt_night with Dissolve(1)
    play ambience ambience_medstation_inside_night fadein 2
    play music insomnia_domitori_taranofu_trouble fadein 2
    bsar_narrator "Я уставился в потолок, словно пытаясь найти там хоть каплю мотивации. Из-за всей этой мыслительной деятельности я чувствую себя как выжатый лимон."
    bsar_narrator "Может быть, выйти на прогулку и, просто ни о чём не думая, подышать свежим воздухом? Хотя, с другой стороны, я обещал Ольге заняться чем-то полезным."

    menu: 
        "Пойти на прогулку": 
            $ insomnia_day1_stroll = True 
            jump insomnia_day1_stroll 

        "Убраться в домике": 
            $ insomnia_paradise_ending_v += 1 
            jump insomnia_day1_cleaning 

label insomnia_day1_cleaning: 
    $ renpy.block_rollback()
    $ persistent.sprite_time = "day"
    bsar_narrator "Так! Я обещал, что сделаю, значит сделаю!"
    bsar_narrator "Бегать по лагерю и искать себе занятие я не хочу, поэтому просто уберусь в домике."
    scene bg black with Dissolve(1)
    $ renpy.pause(0.5, hard = True)
    scene bg int_house_of_mt_night with Dissolve(1)
    bsar_narrator "Спустя тридцать минут, я смог привести свою обитель в более или менее презентабельный вид."
    bsar_narrator "Я уже заканчивал, как мне попался на глаза листок, валяющийся под кроватью Ольги. Любопытство взяло верх, и я решил прочесть его содержимое."
    $ bsar_set_mode_nvl()
    bsar_narrator "{i}Оля! Мне бесконечно жаль, что приходится писать тебе об этом. Жаль, что наши отношения больше не те, какими они были раньше - ласковыми, теплыми, нежными.{/i}"
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
    insomnia_th "Думаю, что впредь, нужно относиться к вожатой более терпимо что ли. Ей сейчас точно не легко."
    show blink
    $ renpy.pause(2, hard = True)
    scene bg black
    hide blink
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw"
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg insomnia_roof behind blink
    show insomnia_snow_layer3_anim_quick
    show insomnia_snow_layer2_anim_quick
    show insomnia_she
    show insomnia_snow_layer1_anim_quick
    show insomnia_snow_layer0_anim_quick
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience insomnia_winter_wind fadein 2
    play sound_loop insomnia_hum fadein 2
    play music insomnia_flashback_music1 fadein 2
    insomnia_she "Так и знала, что найду тебя здесь!"
    insomnia_he "Неужели я настолько предсказуем?"
    insomnia_she "Нет. Конечно нет. Просто ты мне сам как-то рассказывал, что тебе здесь нравится из-за...{w=1.0}{nw}"
    insomnia_he "Из-за того, что тут очень спокойно."
    insomnia_she "И очень холодно."
    insomnia_she "Значит, завтра ты всё-таки уезжаешь?"
    insomnia_he "Да..."
    insomnia_he "Завтра я уезжаю."
    insomnia_she "Я буду ждать. Только не забывай о..."
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_night"
    scene bg int_house_of_mt_night
    show insomnia_mt grin at center
    with insomnia_flash
    play ambience ambience_medstation_inside_night fadein 2
    insomnia_mt "О, вижу, ты прибрался!"
    insomnia_mt "Молодец!"
    insomnia_protagonist "А-а..." 
    insomnia_protagonist "Да, прибрался. Я же обещал заняться делом." 
    insomnia_th "Я заснул... {w}Или это был не сон?" 
    insomnia_th "Уф. Откровенно говоря, меня уже воротит от всех этих странных видений."
    insomnia_th "Может не стоит лезть во всё это? Как говорил знакомый мой покойничек: Я много знал..." 
    insomnia_protagonist "Ольга, а..." 
    insomnia_protagonist "Ой! То есть Ольга Дмитриевна, что-то сегодня случилось?"
    show insomnia_mt sad with dspr
    insomnia_mt "Это так заметно?" 
    bsar_narrator "Грустно улыбнулась она." 
    insomnia_protagonist "Немного. Вы, главное, не расстраивайтесь сильно, если случилось что-то плохое. Ведь плохое всегда рано или поздно заканчивается." 
    bsar_narrator "Я тепло ей улыбнулся. Ольга удивлённо вскинула бровь, наклонила голову вбок и о чём-то задумалась." 
    insomnia_mt "Возможно ты прав. Ладно. Думаю, что тебе стоит лечь спать пораньше. Негоже пропускать завтрак." 
    insomnia_protagonist "Да, конечно."
    show blink
    $ renpy.pause(2, hard = True)
    scene bg black
    hide blink
    bsar_narrator "На меня и вправду накатила сильная усталость и, как только голова коснулась подушки, я моментально заснул." 
    stop ambience fadeout 2
    $ renpy.pause(3, hard = True) 
    jump insomnia_day2 

label insomnia_day1_stroll: 
    $ renpy.block_rollback()
    bsar_narrator "Ай! Да и чёрт с ним. Не думаю, что она вообще вспомнит об этом. Мне явно стоит проветриться."
    play sound sfx_open_door_1
    $ renpy.pause(2, hard = True)
    stop ambience fadeout 2
    scene bg insomnia_ext_house_of_mt_winter_night2
    show insomnia_heavy_snow_night
    show insomnia_normal_snow_night
    with dissolve
    play ambience insomnia_winter_wind fadein 2
    $ renpy.pause(1.5, hard = True)
    show bg insomnia_ext_houses_winter_night behind insomnia_heavy_snow_night with dissolve
    $ renpy.pause(1.5, hard = True)
    show bg insomnia_ext_square_winter_night behind insomnia_heavy_snow_night with dissolve
    $ renpy.pause(1.5, hard = True)
    show bg insomnia_ext_clubs_winter_night behind insomnia_heavy_snow_night with dissolve
    $ renpy.pause(1.5, hard = True)
    show bg insomnia_ext_camp_entrance_winter_night behind insomnia_heavy_snow_night with dissolve
    $ renpy.pause(1.5, hard = True)
    bsar_narrator "Ворота."
    bsar_narrator "Как бы я не пытался не думать об этих странных видениях, они, подобно мерзким осьминогам, тянутся своими отвратительными склизкими щупальцами к моему сознанию, чтобы..."
    bsar_narrator "Э-эм."
    bsar_narrator "О чём это я? Ах, точно, об осьминогах! Ненавижу осьминогов! Или я не об этом?"
    bsar_narrator "Что-то у меня плохое предчувствие."
    stop music fadeout 1
    bsar_narrator "Вдруг краем глаза я замечаю, как ко мне стремительно приближается..."
    play music music_list["awakening_power"] fadein 2
    call screen insomnia_qte(["↓"], 2, 3)
    call screen insomnia_qte(["→"], 2, 3)
    call screen insomnia_qte(["↑"], 2, 3)
    jump insomnia_day1_stroll_completed

label insomnia_day1_stroll_failed: 
    $ renpy.block_rollback()
    hide insomnia_heavy_snow_night
    hide insomnia_normal_snow_night
    with dissolve
    stop music fadeout 2
    scene bg insomnia_ext_camp_entrance_winter_night_blurred with flash
    bsar_narrator "Снег попадает мне прямо в глаза..."
    play sound_loop insomnia_heart
    scene bg insomnia_ext_camp_entrance_winter_night_blurred:
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

    $ insomnia_heartbeat_animation("bg insomnia_ext_camp_entrance_winter_night_blurred", 1.05, 1.0)
    bsar_narrator "Я машинально делаю пару шагов назад, как вдруг всё встаёт с ног на голову."
    bsar_narrator "Я падаю, теряя равновесие..."
    play sound sfx_bones_breaking
    show blink
    $ renpy.pause(2, hard = True)
    bsar_narrator "Необычайно громко по всей округе эхом раздаётся ужасный хруст... или мне это кажется?" 
    bsar_narrator "{i}Кажется что?..{/i}"
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw" 
    scene bg insomnia_roof
    show insomnia_snow_layer3_anim_quick
    show insomnia_snow_layer2_anim_quick
    show insomnia_she
    show insomnia_snow_layer1_anim_quick
    show insomnia_snow_layer0_anim_quick
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience insomnia_winter_wind fadein 2
    play sound_loop insomnia_hum fadein 2
    insomnia_she "Так и знала, что найду тебя здесь!" 
    insomnia_he "Неужели я настолько предсказуем? Зачем ты пришла?" 
    insomnia_she "Нам пора."
    stop ambience fadeout 2
    scene bg insomnia_prolog_bw
    show insomnia_static_noise_anim
    with insomnia_flash
    $ insomnia_heartbeat_animation("bg insomnia_prolog_bw", 1.05, 1.0)
    $ insomnia_heartbeat_animation("insomnia_static_noise_anim", 1.05, 1.0)
    play sound_loop insomnia_heart
    bsar_narrator "Крик? Кто-то кричит? Почему?" 
    insomnia_she "Э-это ч... ровь?!" 
    insomnia_she "Ч-чёр... Зов... жатую!"
    play sound insomnia_electro
    $ renpy.pause(1, hard = True)
    insomnia_voice "Иван Степанович, теряем! ЭЭГ показывает смерть мозга!"
    bsar_narrator "Кажется, мне куда-то нужно? {w}Но куда? {w}Ладно... Неважно."

    if not persistent.insomnia_achievements["insomnia_murderous_snowball"]:
        $ persistent.insomnia_achievements["insomnia_murderous_snowball"] = True
        $ insomnia_show_achievement("insomnia_murderous_snowball")

    $ renpy.pause(1, hard = True)
    scene bg black with dissolve
    stop sound_loop fadeout 2
    $ renpy.pause(1, hard = True)
    $ insomnia_set_main_menu_cursor()
    return     

label insomnia_day1_stroll_completed: 
    $ renpy.block_rollback() 
    $ persistent.sprite_time = "night" 
    bsar_narrator "Я резко отскакиваю в сторону, и запущенный в меня снежок пролетает мимо." 
    insomnia_dv "Блин! Я надеялась, что попаду." 
    show insomnia_dv normal2 behind insomnia_normal_snow_night with dissolve 
    bsar_narrator "С нескрываемой досадой в голосе выдала Алиса, выходя из-за статуи пионера." 
    insomnia_protagonist "Добрая ты девочка, Алиса. Что ты тут вообще забыла?" 
    insomnia_dv "А это уже не твоё дело, {i}дорогуша.{/i}" 
    bsar_narrator "Что-то подозрительное промелькнуло в нотках её голоса..."
    bsar_narrator "До того, как я успеваю среагировать, Ульяна молниеносно засыпает мне за воротник снег и также быстро отскакивает к Алисе."
    show insomnia_dv smile behind insomnia_normal_snow_night:
        linear 1.0 xalign 0.25
    $ renpy.pause(1.0, hard = True)
    show insomnia_us smile at right behind insomnia_normal_snow_night with dissolve
    bsar_narrator "Наблюдая за моей агонией, рыжие в унисон заливаются звонким смехом."
    insomnia_protagonist "УЛЬЯНА! Чтоб тебя!" 
    insomnia_us "Как будто что-то плохое!" 
    insomnia_protagonist "Я ж тебя..." 
    show insomnia_us sad behind insomnia_normal_snow_night:
        linear 1.0 xalign 0.4
    $ renpy.pause(1.0, hard = True)
    show insomnia_dv sad behind insomnia_normal_snow_night 
    show insomnia_mt rage behind insomnia_normal_snow_night at right 
    with dspr
    bsar_narrator "Но неожиданное появление Ольги Дмитриевны застаёт меня врасплох, и я замираю."
    bsar_narrator "Сказать, что она злая, значит не сказать ничего. Кажется, вот-вот у неё вздуется вена на лбу." 
    insomnia_mt "Значит, вот оно - твоё социально полезное занятие?!" 
    insomnia_protagonist "Это.... Это не..." 
    insomnia_mt "Быстро в домик!" 
    insomnia_protagonist "Но ведь..." 
    insomnia_mt "Я сказала БЫСТРО!"
    bsar_narrator "Блин! Всё очень и очень плохо. Бросив напоследок ошарашенный взгляд на притихших девчонок и обречённо качнув головой вожатой, я поспешил в домик."
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1.5, hard = True)
    scene bg int_house_of_mt_night with Dissolve(2)
    play ambience ambience_medstation_inside_night fadein 2
    bsar_narrator "Надо же было так влипнуть! Наверное, Алисе с Ульяной тоже досталось. Нет. Точно досталось!" 
    bsar_narrator "Мне совершенно не хотелось выслушивать нравоучения непонятно из-за чего разъяренной Ольги." 
    bsar_narrator "К тому же накатила непонятно откуда взявшаяся усталость, и как только голова коснулась подушки я моментально заснул." 
    stop ambience fadeout 2 
    $ persistent.timeofday = "bw"
    $ persistent.sprite_time = "day"
    scene bg insomnia_int_kitchen_bw
    show insomnia_she
    show insomnia_static_noise_anim
    with insomnia_flash
    play music insomnia_lucius_OST_piano fadein 2
    play ambience ambience_medstation_inside_night fadein 2
    insomnia_she "Эй, ты опять ходишь с таким лицом, что аж смотреть противно!" 
    insomnia_he "Очередной завал на работе. Эти ночные смены меня доконают." 
    insomnia_she "Эй, перестань! Ну же, давай улыбнись! Улыбнись, дурак!" 
    insomnia_he "Нельзя же человека за то, что он устал, называть дураком!" 
    insomnia_she "{b}МНЕ{/b} можно! Люблю тебя, дурак." 
    insomnia_he "Господи, ты неисправима. {w}За это я тебя и люблю." 
    insomnia_she "Неужели только за это?"
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with insomnia_flash
    $ renpy.pause(3, hard = True) 
    jump insomnia_day2    

label insomnia_day2:
    $ save_name = ("День второй.")
    $ renpy.block_rollback()
    $ insomnia_set_null_cursor()
    $ bsar_onload("lock")
    $ persistent.timeofday = "winter_day"
    $ persistent.sprite_time = "day" 
    $ renpy.movie_cutscene(bsar_gui_path + "days_transitions/insomnia_day2.ogv")
    $ renpy.pause(2, hard = True) 
    scene bg black
    show blink
    $ insomnia_set_timeofday_cursor_var = True
    $ bsar_onload("unlock")
    bsar_narrator "Нос заложен. Горло дерёт, словно связки сорваны от бессмысленного и громкого крика в пустоту. Глаза слезятся. Я плакал во сне. Почему? Не помню." 
    bsar_narrator "Нахлынувшие после пробуждения мысли, подобно волнам во время прилива, смыли остатки сна из моей памяти, оставив только две мокрые дорожки на щеках." 
    scene bg insomnia_int_dining_hall_winter behind blink
    show insomnia_mz normal2 behind blink
    hide blink
    show unblink
    $ renpy.pause(2, hard = True)
    play ambience ambience_dining_hall_empty fadein 2
    play music insomnia_everyday_fantasy fadein 2
    insomnia_mz "...в библиотеке!" 
    insomnia_protagonist "А-а-ага. Стой! В смысле?" 
    show insomnia_mz angry with dspr 
    bsar_narrator "Пионерка фыркнула, уставившись на меня отрешённым взглядом."
    bsar_narrator "Женя - живое воплощение лени со стервозным характером. И голосом настолько дребезжащим и скрипучим, что на ум невольно приходят ассоциации с несмазанной калиткой."
    bsar_narrator "Мне кажется, что она еврейка, но я таки не уверен." 
    insomnia_mz "Я сказала, что мне нужна помощь в библиотеке. Поэтому, жду тебя после завтрака!" 
    insomnia_protagonist "Поговорим сначала о моей награде." 
    bsar_narrator "Её глаза, смотрящие поверх очков, несколько мгновений излучали то любопытство, то полное безразличие к ситуации в целом и моей персоне в частности." 
    insomnia_th "Что же, всё равно делать мне сегодня нечего. Почему бы и не сходить?" 
    insomnia_protagonist "Ладно-ладно. Я приду." 
    bsar_narrator "Прервал я Женю, которая, по всей видимости, уже намеревалась сказать какую-то остроту. Она довольно хмыкнула и встала из-за стола." 
    show insomnia_mz normal2 with dspr 
    insomnia_mz "Вот и славно. Не задерживайся!" 
    insomnia_protagonist "Конечно..." 
    hide insomnia_mz with dissolve
    bsar_narrator "Господи, сколько раз нужно повторять самому себе, что надо сначала думать, а потом говорить." 
    bsar_narrator "Я же только что сдуру подписал себе смертный приговор." 
    bsar_narrator "Другими словами - больше часа в одном помещении с Женей."
    stop music fadeout 2 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard = True)
    scene bg insomnia_ext_library_winter_day
    show insomnia_heavy_snow_day
    show insomnia_normal_snow_day
    with Dissolve(1)
    play ambience insomnia_winter_wind fadein 2
    bsar_narrator "И вот я стою в смятении перед библиотекой." 
    bsar_narrator "Какую на этот раз чепуху она придумала, чтобы изобразить бурную деятельность?"
    bsar_narrator "Может, пока не поздно, лучше пойти в домик?"
    bsar_narrator "А ей потом скажу, что в столовой переел и стало плохо."
    bsar_narrator "Мысль была замечательной."
    play sound sfx_open_door_1
    bsar_narrator "Но только я развернулся спиной к двери, как она распахнулась."
    insomnia_mz "Ну? Чего ты тут стоишь, не заходишь?" 
    bsar_narrator "Она что, у окна дежурит? Как она вообще узнала, что я тут?"
    bsar_narrator "Несколько секунд я еще стоял неподвижно, осторожно подбирая слова."
    show insomnia_mz normal2 behind insomnia_normal_snow_day with dissolve
    bsar_narrator "А потом с милой улыбкой повернулся к молодой любительнице книг."
    insomnia_protagonist "Женя! А я как раз к тебе шел!"
    show insomnia_mz angry behind insomnia_normal_snow_day with dspr
    insomnia_mz "Ага, спиной вперед?"
    insomnia_protagonist "А я это... {w}Повернулся посмотреть на... {w}То есть, мне послышалось... {w}Да! Послышалось, что Славя меня звала!" 
    insomnia_mz "Славя уже давно у меня в библиотеке сидит, умник. Если хочешь помогать, то заходи, а нет, то иди лесом."
    hide insomnia_mz with dissolve
    bsar_narrator "И исчезла, скрывшись в дверном проеме." 
    insomnia_th "А она чертовски проницательная!"  
    bsar_narrator "Не удивлюсь, если сквозь свои очки она видит не только душу человека, но и его будущее."
    play sound sfx_open_door_1
    $ renpy.pause(2, hard = True)
    stop ambience fadeout 2
    scene bg insomnia_int_library_winter_day with dissolve
    play ambience ambience_library_day fadein 2
    play music insomnia_over_the_time_sandy_winter fadein 2
    bsar_narrator "Внутри библиотеки было немногим теплее, чем на улице. Пахло книжной пылью и коммунизмом." 
    bsar_narrator "Атрибутика и портреты с лозунгами смотрели на меня буквально отовсюду, из-за чего по телу невольно пробежали мурашки." 
    insomnia_th "Нечасто же я заходил в библиотеку." 
    bsar_narrator "Славя действительно была здесь и рылась в каких-то бумагах, перебирая их и перекладывая с места на место." 
    bsar_narrator "Увидев меня, блондинка улыбнулась и слабо кивнула в знак приветствия, не отрываясь от работы." 
    bsar_narrator "А Женя уселась прямо на полу среди башенок из книжек." 
    bsar_narrator "Одни были открыты, другие лежали подальше, видимо, отложенные на потом." 
    bsar_narrator "Тут были стопки самой различной литературы в самых разных переплётах." 
    bsar_narrator "От старинных тряпичных до новеньких твердых." 
    show insomnia_mz smile with dissolve 
    insomnia_mz "Спасибо, что пришёл. На самом деле, я думала, что ты будешь отлынивать." 
    insomnia_protagonist "То, что я стою перед тобой, ни о чём не говорит?" 
    show insomnia_mz normal2 with dspr 
    bsar_narrator "Женя смерила меня долгим строгим взглядом и глубоко вздохнула." 
    insomnia_protagonist "Так. Чем я буду заниматься? На полу сидеть?" 
    insomnia_mz "Нет. Впрочем, как хочешь. С прошлой смены в библиотеку не вернулось с десяток книг. И поэтому я решила их проштамповать." 
    insomnia_protagonist "Чего-чего делать?" 
    insomnia_mz "Проштамповать. Проставить метки нашего лагеря на форзац страницы с помощью штампа. Ты ведь знаешь, что такое форзац?" 
    insomnia_protagonist "Э-э-э... Коне-ечно." 
    show insomnia_mz angry with dspr 
    bsar_narrator "Женя закатывает глаза и громко цокает языком." 
    insomnia_mz "Форзац — это лист бумаги, соединяющий корку книги и первую страницу. Это, по сути, первая страница и есть." 
    bsar_narrator "Я живо кивал, наблюдая, как Женя опускает штампик на губку, смоченную чернилами, и проставляет клеймо на тот самый форзац." 
    insomnia_mz "Справишься?" 
    bsar_narrator "Она указала на длинные ряды стеллажей за её спиной." 
    insomnia_th "М-да..." 
    insomnia_th "Намечается длинная и рутинная работа, но делать нечего." 
    insomnia_th "Я уже согласился помочь, и назад пути нет." 
    hide insomnia_mz with dissolve 
    bsar_narrator "Я сел на пол рядом с Женей и принял от неё второй штампик и губку с чернилами, сразу же измазавшись в них." 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard = True) 
    scene bg insomnia_int_library_winter_day with Dissolve(1) 
    bsar_narrator "Сорок или пятьдесят книг спустя я довёл процесс до автоматизма, позволяющий мне брать книгу, ставить печать и брать новую, практически не глядя на них." 
    insomnia_th "Наверное, так и чувствуют себя принтеры." 
    bsar_narrator "В процессе работы мы переговаривались ни о чем и обо всем одновременно." 
    bsar_narrator "Делились впечатлениями от лагеря, сплетничали о его обитателях, говорили о погоде, о жизни до лагеря и прочем." 
    show insomnia_mz normal2 at left 
    show insomnia_sl normal at right 
    with dissolve 
    insomnia_mz "...вот я и стала с книгами тут работать. Книги - они ведь не обманут, не сорвутся на тебя. Общаться с ними порой легче, чем с людьми." 
    insomnia_protagonist "Ты главное не увлекайся сильно с книгами разговаривать. Ничего хорошего из этого не выйдет." 
    insomnia_mz "Вот об этом я и говорю." 
    insomnia_sl "А я думаю, что это здорово, когда человек так увлекается чем-то в жизни. У тебя, наверное, и дома целая библиотека стоит?" 
    insomnia_mz "Не совсем у меня, а скорее у отца библиотека." 
    insomnia_sl "Давай, расскажи, как ты живешь вне лагеря!" 
    insomnia_mz "Я даже и не знаю, что рассказать. У меня папа ученый, поэтому книг у меня всегда было в избытке. А маму я не видела никогда."  
    insomnia_mz "Гулять меня особо не отпускают. Отец говорит, что на улице я ничему хорошему от ребят не научусь, вот я и читаю книги."
    insomnia_mz "Очень люблю эти волшебные миры и истории про рыцарей, правда, книги про этих самых рыцарей достать было трудновато." 
    insomnia_sl "Ого! Как же так? Ты совсем никуда не выходишь?" 
    insomnia_mz "Ну как же! Я хожу в школу, общаюсь там с одноклассниками. А гулять меня как-то не зовет никто, да и не тянет." 
    insomnia_sl "А я люблю гулять! Особенно на природе! Мы с родителями в конце лета каждые выходные едем в лес за грибами! Так здорово бродить среди деревьев и слушать пение птиц. Хотела бы я и тебя с собой взять!" 
    insomnia_mz "В лес? Ну не знаю." 
    insomnia_sl "Да, в лес. Хотела бы я когда-нибудь работать на природе! Может, лесником? Бывают женщины-лесники?" 
    bsar_narrator "Она мило засмеялась, но мне пришлось вернуть её с небес на землю." 
    insomnia_protagonist "Лесники должны загонять животных для охотников — это их основная работа." 
    insomnia_sl "Правда? Нет! Я люблю животных! Не хочу, чтобы их убивали, особенно из-за меня." 
    insomnia_protagonist "А я как-то не особо леса люблю. Какая-то непонятная у меня к ним неприязнь."
    insomnia_mz "Слушай, а расскажи, как ты живешь вне лагеря?"
    insomnia_protagonist "Ну, я живу в Москве с роди..."
    stop ambience fadeout 2 
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw"
    scene bg insomnia_ext_winter_street
    show insomnia_snow_layer3_anim
    show insomnia_snow_layer2_anim
    show insomnia_she
    show insomnia_snow_layer1_anim
    show insomnia_snow_layer0_anim
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience insomnia_winter_wind fadein 2
    play sound_loop insomnia_hum fadein 2
    play music insomnia_socialism fadein 2
    insomnia_she "Ты же говорил, что бросишь." 
    insomnia_he "Я бросал. Но после той аварии снова начал." 
    insomnia_she "Извини. Мне очень жаль твою сестру. Не хотела об этом напоминать." 
    insomnia_he "Эй! Ничего страшного. Не стоит сильно расстраиваться."
    insomnia_he "Я понимаю, что такое... {w}такое порой случается. И с этим просто нужно смириться."
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day"
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene bg insomnia_int_library_winter_day
    show insomnia_sl normal at center
    with insomnia_flash
    play ambience ambience_medstation_inside_night fadein 2
    insomnia_sl "Эй! С тобой все в порядке?" 
    bsar_narrator "Мысли путаются, наскакивают друг на друга, переплетаются. {w}Я не могу выудить из этой вакханалии хотя бы частичку воспоминаний."
    insomnia_protagonist "Не стоит беспокоиться. Я в норме, просто давайте поговорим о чем-нибудь другом." 
    insomnia_sl "Ну хорошо, понимаю, как скажешь." 
    insomnia_protagonist "Славь, я все хотел спросить тебя..." 
    insomnia_sl "Да?" 
    insomnia_protagonist "Тогда, в столовой... Что ты имела в виду, сказав «отдохнуть»?"  
    insomnia_sl "Тьфу! Так начал, я уже думала, будто что-то серьезное спросить собираешься." 
    insomnia_sl "И вообще, я тут совсем заболталась, мне уже нужно бежать, я Ольге Дмитриевной обещала помочь." 
    insomnia_sl "Ты не против, если я попрошу тебя доделать тут работу с бумагами? Пожа-алуйста?" 
    bsar_narrator "Я осмотрел свои измазанные в чернилах руки." 
    bsar_narrator "Определенно, смена деятельности мне не помешает. Нужно подумать." 
    bsar_narrator "Женя кивнула мне, давая понять, что справится с остатками одна." 
    bsar_narrator "Чёрт, как же гудит голова! Что же со мной происходит последние дни?" 
    insomnia_protagonist "Конечно, Славя! Для тебя - все, что угодно!" 
    bsar_narrator "Сказал я, разминая свои затекшие от длительного сидения ноги." 
    hide insomnia_sl with dissolve 
    stop music fadeout 2 
    bsar_narrator "Славя смежила губы в лучезарной улыбке и поспешно покинула библиотеку." 
    scene bg insomnia_logbook with dissolve 
    bsar_narrator "Я сажусь за стол, оценивая оставшийся фронт работ." 
    bsar_narrator "Тут осталось перенести несколько записей в формуляры. {w}Плёвое дело."
    scene bg black with Dissolve(1)
    $ renpy.pause(1, hard = True)
    scene bg insomnia_logbook with Dissolve(1)
    bsar_narrator "И так сойдёт!" 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1)
    $ renpy.pause(1, hard = True)
    scene bg insomnia_ext_square_winter_day
    show insomnia_heavy_snow_day
    show insomnia_dv normal at center
    show insomnia_normal_snow_day
    with Dissolve(1)
    play ambience insomnia_winter_wind fadein 2
    play music insomnia_standing_tall fadein 2
    bsar_narrator "Не успел я толком отойти от библиотеки, как столкнулся с Алисой, которая, по всей видимости, спешила попасть внутрь и совершенно не смотрела по сторонам."  
    bsar_narrator "Из-за удара она выронила книгу, которая упала на снег обложкой кверху. «Унесённые ветром»."
    bsar_narrator "Заметив, что моё внимание приковано к книге, ДваЧе быстро её подняла, спрятав за спину." 
    insomnia_protagonist "Должок идёшь возвращать, Алиса?" 
    insomnia_dv "А тебе какое дело?" 
    bsar_narrator "Губы плотно сжаты, свободная рука превращается в кулак." 
    bsar_narrator "Не требуется обладать какими-то знаниями в области психологии, чтобы понять этот жест и пронизывающий меня крайне недовольный взгляд." 
    bsar_narrator "Я смиренно киваю головой и улыбаюсь, пытаясь разрядить обстановку. {w}Получается немного фальшиво, но Алиса этого не замечает, или делает вид, что не замечает."  
    bsar_narrator "Пионерка делает шаг назад и возвращается к своему надменно-безразличному состоянию." 
    insomnia_dv "Давай-давай, проходи, не задерживайся! И забудь то, что видел!" 
    insomnia_protagonist "Да, конечно. {w}Вот-вот уже. {w}Почти. {w}{i}Ещё чуть-чуть...{/i}." 
    insomnia_dv "Болван!" 
    hide insomnia_dv with dissolve 
    bsar_narrator "ДваЧе прошла мимо меня, намеренно задев плечом."
    bsar_narrator "Больше всего я удивляюсь тому факту, что позволяю себе пасовать перед этой девчонкой. {w}Боже, эта Алиса..." 
    stop ambience fadeout 2
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw" 
    scene bg insomnia_prosecutor_office
    show insomnia_snow_layer3_anim
    show insomnia_snow_layer2_anim
    show insomnia_lis
    show insomnia_snow_layer1_anim
    show insomnia_snow_layer0_anim
    show insomnia_static_noise_anim
    with insomnia_flash 
    play ambience insomnia_winter_wind fadein 2
    play sound_loop insomnia_hum fadein 2
    play music insomnia_cyprinid_floating fadein 2
    insomnia_fox "Ну что, дорогуша, поздравляю с повышением! Обмоем звёздочку?"
    insomnia_he "Заметь, не я это предложил. Только не долго и не много."
    insomnia_fox "Петля не жмёт?"
    insomnia_he "Какая петля?"
    insomnia_fox "Семейной жизни! Когда уже детишки? Крёстной возьмешь?"
    insomnia_he "Не паясничай. Ты, кстати, помнишь про следующую сделку, которую мы крышуем?"
    insomnia_fox "Ты то так не ори. Хочешь обратно в старлеи? Помню я, помню."
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day"
    scene bg insomnia_ext_square_winter_day
    show insomnia_heavy_snow_day
    show insomnia_normal_snow_day
    with insomnia_flash
    play ambience insomnia_winter_wind fadein 2 
    bsar_narrator "Чёрт! У меня очень стойкое чувство дежавю, словно события из ведений, которые я толком не могу вспомнить, уже и в правду происходили."  
    bsar_narrator "Нет. Это не могут быть мои воспоминания! {w}Похоже, что мне светит путёвка в жёлтый дом." 
    insomnia_protagonist "Карету мне, карету! Сюда я больше не ездок..."
    show insomnia_us normal behind insomnia_normal_snow_day with dissolve
    insomnia_us "Физкульт-привет!" 
    insomnia_protagonist "Привет, Ульяна." 
    insomnia_us "Чего это ты тут стоишь? Да ещё и бледный какой-то. Может, Виолетту позвать? Укольчик сделает!" 
    insomnia_protagonist "Нет, нет. Спасибо."    

    if insomnia_day1_stroll == True: 
        insomnia_protagonist "Вам вчера сильно от Ольги досталось?" 
        insomnia_us "Да. Она всё-таки узнала про те конфеты!" 
        insomnia_protagonist "Про какие конфеты?" 
        insomnia_us "Ну... Которые я одолжила в столовой." 
        insomnia_protagonist "Серьёзно? Ульяна, ты неисправима!"  

    insomnia_us "Ладно. Не суть важно. Ты Алису не видел?" 
    insomnia_protagonist "Алису? Алису видел, она в библиотеку пошла." 
    insomnia_us "Спасибо! Не болей!" 
    hide insomnia_us with dissolve
    bsar_narrator "Ульяна тепло улыбнулась и подмигнула мне, а затем побежала в библиотеку. Странно видеть эту шестнадцатилетнюю егозу такой милой."  
    bsar_narrator "Раньше она постоянно пыталась меня подколоть, а сейчас тишь да гладь." 

    if insomnia_day1_stroll == True: 
        bsar_narrator "Не считая снежков, конечно." 

    play sound sfx_dinner_horn_processed fadein 2 
    $ renpy.pause(3, hard = True) 
    bsar_narrator "Горн. Пора на обед."
    stop ambience fadeout 2 
    scene bg black with Dissolve(1)
    $ renpy.pause(1.5, hard = True)
    scene bg int_house_of_mt_day with Dissolve(1) 
    $ renpy.block_rollback()
    play ambience ambience_medstation_inside_night fadein 2
    play music insomnia_maconda_die_begin fadein 4
    bsar_narrator "После обеда меня разморило."
    bsar_narrator "Голова начала гудеть, а мысли кровавыми сгустками выскальзывать из черепа."
    scene bg insomnia_int_house_of_mt_day_vingete_blurred with Dissolve(1.1)
    $ renpy.pause(1.1, hard = True)
    $ insomnia_show_random_words(insomnia_day2_amnesia_scene, k = 70)
    $ renpy.pause(1, hard = True)
    $ insomnia_show_centered_text("У МЕНЯ АМНЕЗИЯ?")
    stop ambience fadeout 2 
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw" 
    scene bg insomnia_prolog_bw
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience insomnia_hum fadein 2 
    bsar_narrator "Нет же! Папа работает учителем, а мама бухгалтер."  
    bsar_narrator "Я с отличием закончил десятый класс в Московской гимназии номер четырнадцать и за это был отправлен в этот лагерь, {i}потому что давно хотел сюда попасть.{/i}"  
    bsar_narrator "{i}Ведь так?{/i}"
    stop ambience fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day" 
    scene bg int_house_of_mt_day with insomnia_flash 
    play ambience ambience_medstation_inside_night fadein 2 
    insomnia_protagonist "И что мне делать?" 
    bsar_narrator "Задал я вопрос пустой комнате, которая ответила мне абсолютно ничем."
    show blink
    $ renpy.pause(2, hard = True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw" 
    stop ambience fadeout 2 
    scene bg insomnia_prolog_bw
    show insomnia_static_noise_anim
    with insomnia_flash 
    play ambience insomnia_heart_monitor fadein 2
    play sound_loop insomnia_voices fadein 2
    bsar_narrator "Я чувствую невероятную лёгкость и безволие, в какой-то мере, расконцентрированность." 
    bsar_narrator "Пространство вокруг меня наполнилось звуками. {w}Тиканье часов, какой-то писк, шаги, едва различимые голоса вдали." 
    insomnia_voice "Я своими глазами это видел, Иван Степанович!" 
    insomnia_voice "Это просто чудо какое-то! Возможно, есть шансы, что он всё же..."
    scene bg black with insomnia_flash
    bsar_narrator "А ведь понимаю, что сон. Поэтому пытался хитрить, ускользать, изворачиваться, чтобы не проснуться." 
    bsar_narrator "Пытался оглохнуть, ослепнуть, дематериализоваться, чтоб реальность не могла меня изловить и затащить обратно."  
    bsar_narrator "Хотелось ещё послушать, что говорят эти странные голоса."
    bsar_narrator "Но вот звуки становятся тихими и невнятными, возвращается тяжесть тела..."
    bsar_narrator "Кончилось."
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_night"
    scene bg int_house_of_mt_night behind blink 
    show unblink 
    $ renpy.pause(2, hard = True)
    play ambience ambience_medstation_inside_night fadein 2 
    show insomnia_mt rage with dissolve 
    insomnia_mt "Вставай! Вставай, кому говорю?!" 
    insomnia_protagonist "Да встаю я! Что случилось то? На десять минут задремал." 
    insomnia_mt "Какие десять минут? Уже вот-вот и вечер на дворе! Ты ужин проспал!" 
    insomnia_protagonist "Прошу прощения. Не рассчитал." 
    bsar_narrator "Я закашлял. В горле першило, руки и ноги онемели. Чувствую себя отвратно." 
    show insomnia_mt angry with dspr 
    insomnia_mt "Ты здоров? Уже который день выглядишь... {w}неважно." 
    insomnia_protagonist "Всё в порядке. Просто плохо чувствую себя после дневного сна. Я прогуляюсь." 
    insomnia_mt "Подожди! На, возьми. Перекусишь хотя бы." 
    bsar_narrator "Вожатая протянула мне целлофановый свёрток. Бутерброды." 
    insomnia_protagonist "Спасибо большое, Ольга Дмитриевна. Я пошёл, по дороге перекушу." 
    bsar_narrator "Накинув пальто, я вышел из домика."
    play sound sfx_open_door_1
    $ renpy.pause(2, hard = True)
    stop ambience fadeout 2
    scene bg insomnia_ext_house_of_mt_winter_night2 with dissolve
    play ambience insomnia_winter_wind fadein 2
    $ renpy.pause(1.5, hard = True)
    scene bg insomnia_ext_houses_winter_night with dissolve
    $ renpy.pause(1.5, hard = True)
    scene bg insomnia_ext_square_winter_night with dissolve
    $ renpy.pause(1.5, hard = True)
    scene bg insomnia_ext_musclub_winter_night with dissolve
    $ renpy.pause(1.5, hard = True)
    bsar_narrator "Давненько я не видел Мику. Хочу повидаться с этой весёлой и словоохотливой японкой. Скорее всего, она у себя в кружке."  
    bsar_narrator "Может быть, спросить у неё про эти странные сны и видения? Она единственная, кто не будет искать скрытый смысл в моих словах и уж точно не станет крутить пальцем у виска." 
    play sound sfx_open_door_1
    $ renpy.pause(2, hard = True)
    stop ambience fadeout 2
    scene bg insomnia_int_musclub_night_2 with dissolve 
    play ambience ambience_medstation_inside_night fadein 2
    bsar_narrator "Открыв дверь и зайдя внутрь, я стал свидетелем ссоры, которую точно не ожидал увидеть." 
    bsar_narrator "Алиса с Леной? Ожидаемо."
    bsar_narrator "Алиса со Славяной? Тоже."
    bsar_narrator "Алиса, ругающаяся с Ульяной? Удивительно, но происходит."
    bsar_narrator "Голоса доносятся из подсобки."
    scene bg insomnia_us_dv_confrontation with dissolve
    play music insomnia_painful_history fadein 2
    insomnia_us "Алиса, может быть, ты уже успокоишься?" 
    insomnia_dv "А может ты не будешь меня затыкать?!" 
    insomnia_us "Я не трогала его! Мы же вообще живём в разных доми..." 
    insomnia_dv "НЕ ВРИ! Я уверена, что его взяла ты! Верни сейчас же или хуже будет!" 
    bsar_narrator "Кажется, дело может принять плохой оборот. {w}Стоит ли вмешиваться? С другой стороны, я точно не знаю, что здесь происходит."     
    $ persistent.sprite_time = "night"      

    menu: 
        "Вмешаться": 
            $ insomnia_day2_intervene = True 
            bsar_narrator "И чего я встал как истукан? Нужно вмешаться, пока Ульяне не досталось. Я быстро перескакиваю порог и встречаюсь взглядом с Алисой."
            scene bg int_clubs_male2_night_nolight
            show insomnia_dv sad at left 
            show insomnia_us sad at right 
            with dissolve 
            insomnia_dv "ТЫ подслушивал?!" 
            bsar_narrator "Я замер, не ожидав такой реакции." 
            insomnia_protagonist "Почему вы ругаетесь? Вас за километр слышно." 
            insomnia_dv "Ага-ага. Заливай больше. Сто процентов стоял под дверью и слушал, болван!" 
            insomnia_us "Алиса!" 
            insomnia_dv "А с тобой я позже разберусь!" 
            hide insomnia_dv with dissolve 
            stop music fadeout 4
            bsar_narrator "ДваЧе толкнула меня и быстро скрылась в дверном проёме, оставив дверь нараспашку."
            bsar_narrator "Я перевёл взгляд на ошарашенную Ульяну, но она лишь грустно помотала головой." 
            insomnia_us "Извини, что тебе пришлось это услышать. Она почти весь день такая злая. Я её попробую догнать и успокоить."
            hide insomnia_us with dissolve
            bsar_narrator "Последнее предложение Ульяна пробормотала себе под нос и выскочила за дверь, громко зовя Алису."
            insomnia_th "Чёрт! Помог, называется."
            bsar_narrator "Алиса точно на меня обидится, и Ульяна тоже была не особо рада моему появлению."  
            bsar_narrator "Умею же я портить то, что, как казалось изначально, ещё больше испортить нельзя." 

        "Не вмешиваться": 
            $ insomnia_paradise_ending_v +=1 
            bsar_narrator "Я почему-то ошеломленно замираю, не в силах сделать даже шаг, а девушки продолжают свой разговор на повышенных тонах."
            insomnia_us "Алиса, чтоб тебя! Перестань истерить! Я понимаю, насколько важен тебе этот дневник."
            insomnia_us "Мы подруги, и я бы никогда не навредила тебе!"
            bsar_narrator "Ничего себе! Такого я точно не ожидал."
            bsar_narrator "На мгновение в помещении музыкального кружка повисла полная тишина. Настолько тяжёлая и абсолютная, что кажется, словно воздух уплотнился и стал вязким." 
            insomnia_dv "Уль... Ульяна. Извини. {w}Не знаю, что на меня нашло. Я правда не хотела." 
            bsar_narrator "Никогда не слышал, чтобы голос Алисы так дрожал." 
            insomnia_us "Всё в порядке. Давай завтра вместе поищем твой дневник?" 
            stop music fadeout 4
            bsar_narrator "Я решаю постучать, чтобы выдать своё присутствие до того, как девочки увидят меня и обвинят в подслушивании." 
            insomnia_protagonist "Мику здесь?"
            scene bg int_clubs_male2_night_nolight
            show insomnia_dv smile at left 
            show insomnia_us normal at right 
            with dissolve 
            $ renpy.pause(5, hard = True) 
            insomnia_dv "Она уехала четыре дня назад, дурень." 
            insomnia_protagonist "Почему дурень-то? Обидно же." 
            insomnia_dv "А я по-дружески. Обидно ему. {w}Напоминаешь мне одного знакомого хлюпика, как его там звали?" 
            insomnia_us "Не помню, на «С», кажется. Хотя, не так это и важно." 
            bsar_narrator "Девушки ненаигранно улыбались. Всё же хорошо, что я решил не лезть." 
            insomnia_protagonist "А что, собственно, с Мику?" 
            insomnia_dv "У неё какие-то проблемы с горлом. Заболела, бедняжка." 
            insomnia_us "Ага, жалко её." 
            insomnia_us "Ладно. Может, пойдём прогуляемся?" 
            bsar_narrator "Ульяна потёрла руки и хитро подмигнула Алисе." 
            insomnia_dv "Я за! А ты, хлюпик?" 
            insomnia_protagonist "Опять какую-то авантюру надумали? Ну хорошо, я с вами."
            show insomnia_us smile with dspr
            bsar_narrator "Ульяна подпрыгнула и хлопнула в ладошки." 
            insomnia_us "Вперёд к приключениям!"

    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(4, hard = True)      
    $ renpy.block_rollback() 

label insomnia_day3:
    $ save_name = ("День третий.")
    $ renpy.block_rollback()
    $ insomnia_set_null_cursor()
    $ bsar_onload("lock")
    $ renpy.movie_cutscene(bsar_gui_path + "days_transitions/insomnia_day3.ogv")
    $ persistent.sprite_time = "day" 
    $ persistent.timeofday = "bw"
    $ renpy.pause(2, hard = True)
    scene bg insomnia_lane
    show insomnia_lis
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience ambience_cold_wind_loop fadein 2
    play sound_loop insomnia_hum fadein 2
    play music insomnia_hoyts_office fadein 2
    $ insomnia_set_timeofday_cursor_var = True
    $ bsar_onload("unlock")
    bsar_narrator "Тёмные переулки, руки в карманах, ладонь поглаживает холодную рукоять ПМа. Первый лёд хрустит под ногами. Луна за тучами спряталась, не показывается." 
    insomnia_protagonist "Лис, наш выход только после того, как клиент клюнет. Не раньше."
    insomnia_fox_orange "Да поняла я. Не учи учёного."
    insomnia_fox_orange "Чего ты вообще подписался на эту встречу?"
    insomnia_protagonist "ОД приписал. Сказал, что буду отрабатывать упущенный товар."
    insomnia_fox_orange "Ну ты даёшь."
    insomnia_fox_orange "Какого ты вообще попёрся туда? Это же не наш уровень, а ФСКН."
    insomnia_protagonist "Так получилось."
    bsar_narrator "Я остановился у поворота и жестом показал своей напарнице замереть." 
    insomnia_fox_orange "Как тебя твоя отпустила? Не прознала ещё про твои тёмные делишки?"
    insomnia_protagonist "Нет, не прознала. А у тебя как дела с..."
    insomnia_fox_orange "А это уже не твоё дело, дорогуша. Следи лучше за точкой."
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    scene bg insomnia_prolog_bw
    show insomnia_static_noise_anim
    with insomnia_flash
    insomnia_she_red "Нет! Пожалуйста, не поддавайся! Ты должен проснуться."
    insomnia_protagonist "А разве я сплю?"
    bsar_narrator "Спросил. {w}И проснулся."
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_night"
    scene bg int_house_of_mt_night2 with insomnia_flash
    play ambience ambience_medstation_inside_night fadein 2
    play music insomnia_domitori_taranofu_planet_of_colds fadein 2
    play sound_loop insomnia_medical_devices fadein 2
    bsar_narrator "В комнате было темно. Похоже, проснулся до рассвета."
    bsar_narrator "Я открыл рот в беззвучном крике."
    bsar_narrator "Нет, физической боли не было. {w}Было ощущение, что само моё естество разрывают, кромсают, сжигают изнутри."
    bsar_narrator "Ещё чуть-чуть и я просто... {w}просто исчезну. Испарюсь, словно меня никогда и не было."
    bsar_narrator "Лоб покрылся холодным липким потом, а по спине пробежали мурашки."
    $ insomnia_show_centered_text("Почему мне так тревожно и одиноко?")
    $ insomnia_show_centered_text("Почему возникло чувство вины?")
    $ insomnia_hide_centered_text(dspr)
    bsar_narrator "В окно робко заглянула луна, освещая домик и даруя предметам более смазанные и кривые очертания."
    $ insomnia_show_centered_text("Я всё ещё сплю или уже нет?")
    $ insomnia_hide_centered_text(dspr)
    bsar_narrator "В голову лез всякий вздор."
    bsar_narrator "Попытался встать, но не смог. {w}Тело не слушалось. {w}Попытался снова. {w}Получилось. Собственные движения немного успокоили." 
    bsar_narrator "Сознание прояснилось, и я смог сконцентрироваться. Всего лишь дурной сон. {w}Который раз."
    scene bg int_house_of_mt_night2:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 5 zoom 2.1 xalign 0.7 yalign 0.4
    $ renpy.pause(5, hard = True)
    scene bg insomnia_ext_winter_forest
    show insomnia_snow_layer3_anim
    show insomnia_snow_layer2_anim
    show insomnia_snow_layer1_anim
    show insomnia_snow_layer0_anim
    with fade
    bsar_narrator "Подошёл к окну. Оно показывало смазанные ели, причудливый танец падающих снежинок, спрятавшееся за рваными облаками небо."
    bsar_narrator "Куда не глянь, везде простиралась хвойная стена. {w}Бескрайняя и до боли одинаковая."
    bsar_narrator "Стало душно."
    bsar_narrator "Горло свело судорогой, в груди возникло тянущее чувство. {w}Хочется курить."
    bsar_narrator "Не знаю, почему я решил, что мне нужно именно этого, ибо я раньше никогда даже не пробовал табачить."
    bsar_narrator "Захотелось выйти на улицу и бежать. Бежать пока не кончатся силы. Подальше от этих лесных стен и кошмаров."
    $ renpy.pause(2, hard = True)
    scene bg int_house_of_mt_night2 with fade
    bsar_narrator "Я постоял ещё немного и вернулся в кровать, но спать уже не хотелось." 
    stop ambience fadeout 2 
    stop music fadeout 2
    stop sound_loop fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day"
    scene bg black with Dissolve(1)
    $ renpy.pause(2, hard = True)
    scene bg insomnia_ext_square_winter_day
    show insomnia_heavy_snow_day
    show insomnia_mt grin
    show insomnia_normal_snow_day
    with Dissolve(1)
    play ambience insomnia_winter_wind fadein 2 
    insomnia_mt "К сожалению, осталась всего неделя до окончания смены, но впереди нас ждут предпраздничные хлопоты и масса хорошего настроения!" 
    insomnia_mt "Не забудьте, что на завтра запланирован поход в лес."
    insomnia_mt "Надеюсь, по окончанию смены у вас останутся только хорошие воспоминания о нашем  «Совёнке»." 
    insomnia_mt "{i}Воспоминания на всю жизнь!{/i}" 
    insomnia_mt  "Все свободны." 
    hide insomnia_mt with dissolve 
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
    show insomnia_us smile behind insomnia_normal_snow_day with dissolve
    insomnia_us "А-у-у. Есть кто дома? Чего встал, как столб посреди площади? Линейка давным-давно закончилась." 
    insomnia_protagonist "Ах да. Извини." 
    insomnia_us "За что?" 
    insomnia_protagonist "В смысле?" 
    insomnia_us "За что извиняешься, говорю. Хватит тормозить!" 
    insomnia_protagonist "А, неважно. Как там Алиса?" 
    insomnia_us "В полном порядке." 
    bsar_narrator "Пионерка улыбнулась и показала большой палец." 
    bsar_narrator "А почему, собственно, не Ульяна?" 
    bsar_narrator "Думаю, с ней вполне можно поговорить про кошмары. Но аккуратно и без лишних подробностей. Только при этом всегда остаётся шанс быть высмеянным." 
    bsar_narrator "Начну издалека." 
    insomnia_protagonist "Как спалось?" 
    insomnia_us "Отлично, а почему спрашиваешь?" 
    insomnia_protagonist "Просто интересно." 
    insomnia_us "Что, бессонница мучает?" 
    insomnia_protagonist "Так заметно?" 
    insomnia_us "Очень заметно! Мешки под глазами уже больше, чем сами глаза. Ходишь как живой мертвец из того фильма..." 
    bsar_narrator "Её правда. Мой внешний вид оставляет желать лучшего. Я похож на узника концлагеря, а не на счастливого пионера." 
    insomnia_us "Слу-у-ушай, а хочешь я тебе ловец снов дам? У меня сестра увлекается этой, как её..."
    show insomnia_us dontlike behind insomnia_normal_snow_day with dspr
    bsar_narrator "Девушка замирает, сводит брови и начинает бегать глазами по площади, словно ища подсказку."
    show insomnia_us normal behind insomnia_normal_snow_day with dspr
    insomnia_us "Вспомнила! Мистикой она увлекается!" 
    insomnia_us "Короче, она мне сделала ловец снов. Амулет какой-то индейский. Говорит, что помогает с кошмарами." 
    insomnia_protagonist "А ты уверена, что он поможет?" 
    insomnia_us "Не нравится мне твой скепти-чтоб-его-цизм."
    insomnia_protagonist "Извини. Я с радостью возьму этот ловец снов."
    show insomnia_us smile behind insomnia_normal_snow_day with dspr
    insomnia_us "Отличненько! Увидимся на завтраке, там я тебе его и отдам." 
    hide insomnia_us with dissolve 
    bsar_narrator "Ульянка на прощание махнула мне рукой и быстро убежала в сторону домиков. Ловец снов значит? Почему бы, собственно, и нет."
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw"
    scene bg insomnia_int_kitchen_bw
    show insomnia_she
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience ambience_medstation_inside_night fadein 2
    play sound_loop insomnia_hum fadein 2
    play music insomnia_master_of_spirits_the_last_word fadein 2
    insomnia_he "Ты серьёзно думаешь, что эта безделушка мне поможет?" 
    insomnia_she "Ох, как же я не люблю, когда в твоём голосе слышны нотки скепти-чтоб-его-цизма." 
    insomnia_he "Извини, я попробую. Весь на нервах из-за этой поездки и кошмаров. Так хочется всё отменить, из..." 
    insomnia_she "Твои глаза извиняются лучше. {w}Но на самом деле, мне и правда не нравится эта твоя работа. {w}Странная она какая-то."
    insomnia_she "С тобой точно всё будет в порядке?" 
    insomnia_he "Да, точно. Спасибо за ловец снов. Люблю тебя!" 
    insomnia_she "И я лю..." 
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day"
    scene bg black with insomnia_flash
    $ renpy.pause(0.5, hard = True)
    scene bg insomnia_int_dining_hall_winter with Dissolve(1)
    play ambience ambience_dining_hall_empty fadein 2
    play sound_loop insomnia_voices fadein 2
    play music insomnia_master_of_spirits_own_shadow fadein 2
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
    show insomnia_us normal with dissolve 
    insomnia_us "Вот, принесла, как и обещала." 
    bsar_narrator "Она протянула мне амулет." 
    show insomnia_dream_catcher with dissolve
    bsar_narrator "Красивый."
    bsar_narrator "Не помню, где я это слышал, но всё же. По древним преданиям плохие сны запутываются в паутине из ниток, а хорошие проскальзывают сквозь отверстие посередине." 
    insomnia_protagonist "Спасибо большое, Уль. Это многое для меня значит."
    hide insomnia_dream_catcher with dissolve
    insomnia_us "Ну что ты. Слушай, а возьми, пожалуйста, ещё это..." 
    bsar_narrator "Девушка протягивает мне сложенный вчетверо тетрадный листок." 
    bsar_narrator "Я уже собирался его развернуть, как Ульяна меня остановила." 
    insomnia_us "Подожди. Не читай его сейчас, пожалуйста. Потом. Вечером, когда будешь ложиться спать." 
    bsar_narrator "Она густо краснеет, переводит взгляд вниз, изредка поглядывая на меня смущённым взглядом. К еде она так и не притронулась." 
    insomnia_protagonist "Да, конечно. Без проблем." 
    insomnia_us "Спасибо. Я пойду." 
    insomnia_protagonist "А как же завтрак?" 
    insomnia_us "Я не особо голодна. Возьму с собой. Пока." 
    insomnia_protagonist "Ага-а. Увидимся." 
    hide insomnia_us with dissolve
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(1) 
    scene bg insomnia_ext_square_winter_day
    show insomnia_mz out_normal at center
    with Dissolve(1)
    play music insomnia_fripperies fadein 2
    play ambience insomnia_winter_wind fadein 2
    insomnia_mz "...поэтому мне и нравится творчество Лермонтова." 
    insomnia_protagonist "Думаю, что ты права. Особенно мне понравился твой взгляд на «Героя нашего времени»." 
    insomnia_mz "Да-а. Часть людей слишком поверхностно знакомится с этим произведением и не понимает вложенного в роман смысла." 
    insomnia_protagonist "Кстати, хотел спросить, ты не видела Славяну?" 
    insomnia_mz "Видела. Вчера вечером куда-то собиралась, но куда - не сказала." 
    insomnia_protagonist "А ты у вожатой спрашивала?" 
    insomnia_mz "Не-а. Зачем?" 
    bsar_narrator "И вправду, зачем? {w}Почему я до сих пор переживаю за Славю, хоть и решил, что это меня не касается?"
    bsar_narrator "Не знаю. Но почему-то изнутри гложет чувство, словно я ей что-то должен. А что должен - поди разбери." 
    bsar_narrator "Завтра поход. Она наверняка будет там." 
    show insomnia_mz out_normal:
        linear 1.0 xalign 0.72
    $ renpy.pause(1.0, hard = True)
    show insomnia_dv normal at left with dissolve
    insomnia_dv "Какие люди!"
    insomnia_mz "Двачевская."
    insomnia_dv "Привет, мышка-Женя."
    insomnia_mz "Ты неисправима! Мне пора в библиотеку."
    insomnia_protagonist "Удачи."
    bsar_narrator "Женя выпрямилась, слегка откинула голову и свела брови. Со стороны казалось, что она смотрит на ДваЧе сверху вниз, хоть и ниже неё на полголовы."
    hide insomnia_mz with dissolve
    bsar_narrator "Затем она резко повернулась к нам спиной и быстро засеменила в сторону библиотеки."
    show insomnia_dv normal:
        linear 1.0 xalign 0.5
    $ renpy.pause(1.0, hard = True)
    insomnia_protagonist "Злая ты, Алиса. Ты вообще хоть кого-то любишь?"
    insomnia_dv "Животных люблю. Кто-то там кошек любит, кто-то собак, а я всех люблю без разбора."
    insomnia_dv "Людей только не люблю. Надоели. Постоянно носятся туда-сюда."
    insomnia_dv "Агрессивные какие-то."
    insomnia_protagonist "Агрессивные?"
    bsar_narrator "Я усмехнулся. Алиса нахмурилась."
    insomnia_dv "Что смешного?"
    insomnia_protagonist "Ничего. Как ты?"

    if insomnia_day2_intervene: 
        bsar_narrator "Алиса едва заметно сморщила нос и сжала губы, сделав небольшой шаг в сторону." 
        insomnia_dv "Не твоё дело, подслушиватель!" 
        insomnia_protagonist "Это случайно получилось!" 
        insomnia_dv "Да-да. Ври больше! Случайно у него получилось." 
        bsar_narrator "Я глубоко вздохнул и закатил глаза. Спокойно. {w}Раз. {w}Два. {w}Три." 
        insomnia_protagonist "Думай, что хочешь." 
        hide insomnia_dv with dissolve 
        bsar_narrator "Махнув рукой, я развернулся и пошёл прочь с площади. Алиса крикнула мне вслед то ли «дурак», то ли «дубина». Не имеет значения." 
        jump insomnia_day3_after_dv  

    else:
        bsar_narrator "Пионерка улыбнулась, немного опустив брови." 
        insomnia_dv "Вполне неплохо. Весело вчера было." 
        insomnia_protagonist "Да, только я всё равно не одобряю это проникновение со взломом." 
        insomnia_dv "Коне-е-ечно. Сам-то булочки за обе щеки уплетал." 
        insomnia_protagonist "Хорошо-хорошо. Твоя правда." 
        insomnia_dv "Кстати, ты не знаешь, что с Ульяной?" 
        insomnia_protagonist "А что с ней не так?" 
        insomnia_dv "Слишком активная стала, улыбается постоянно. Сегодня прибежала в домик, долго копалась в вещах, потом что-то писала, а что писала - ни под каким предлогом не сказала." 
        insomnia_protagonist "Тебе лучше знать." 
        insomnia_dv "Ясно." 
        insomnia_protagonist "Подожди-ка. Вы же живёте в разных домиках?" 
        insomnia_dv "А. Прикинь, Ольга сегодня утром пришла и сказала, что мы наконец-то можем съехаться, мол это её новогодний подарок. Вот теперь вещи перетаскиваем потихоньку." 
        bsar_narrator "Алиса дёрнула головой, чтобы убрать локон волос, полезший в глаза, и скрестила руки на груди. Повисло молчание."  
        bsar_narrator "Мне кажется или воздух стал горячее?" 
        bsar_narrator "По площади туда-сюда носились пионеры из младших отрядов. Играли в снежки, лепили снеговиков, строили снежные крепости. Весело быть детьми."  
        bsar_narrator "Проблемы, которые сейчас давят, подобно каменной глыбе, неожиданно упавшей на голову, для детей всего лишь мелочь." 
        insomnia_protagonist "Кстати, та записка. Она её для меня написала, похоже." 
        insomnia_dv "Ну, и чего ты молчал? Что там?" 
        insomnia_protagonist "Ульяна попросила её вечером прочитать." 
        insomnia_dv "Поня-ятно. Девочка-то влюбилась!" 
        insomnia_protagonist "Ты явно преувеличиваешь." 
        insomnia_dv "Может быть, но смотри мне! Только попробуй её обидеть..." 
        insomnia_protagonist "Не обижу. Можешь не продолжать." 
        insomnia_dv "Ладно. Я пойду." 
        insomnia_protagonist "Ага." 
        hide insomnia_dv with dissolve 
        jump insomnia_day3_after_dv 

label insomnia_day3_after_dv:
    stop music fadeout 2
    $ renpy.block_rollback()
    bsar_narrator "А что, если Алиса права?" 
    bsar_narrator "Ладно. Спешить некуда. Вечером узнаю." 
    scene bg black with Dissolve(1)
    $ renpy.pause(2, hard = True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_night"
    $ persistent.sprite_time = "night"
    scene bg insomnia_ext_square_winter_night_tree with Dissolve(1) 
    play music insomnia_domitori_taranofu_winter_night fadein 2 
    bsar_narrator "Новый год подбирался всё ближе и ближе, скрываясь за предпоследним листом календаря. " 
    bsar_narrator "Вся площадь была обряжена в яркие украшения. От гирлянд и разноцветной мишуры до игрушек и вырезанных из бумаги снежинок, создавая неповторимую атмосферу скорого торжества."  
    bsar_narrator "Этот день сулил множество праздничных хлопот для всех обитателей лагеря. Ну, почти для всех... " 
    bsar_narrator "Лампочки мигали и переливались, как бы крича о том, что тут самое праздничное место в округе. На лавочке недалеко от ёлки сидела Лена и читала книгу." 
    show insomnia_un normal with dissolve 
    insomnia_protagonist "Привет, Лен!" 
    insomnia_un "Привет." 
    insomnia_protagonist "Красивая ёлка." 
    insomnia_un "Да, красивая." 
    bsar_narrator "Девушка неопределённо пожимает плечами и снова углубляется в чтение." 
    bsar_narrator "Лена. Асоциальная и крайне застенчивая девушка."
    bsar_narrator "За прошедшие две недели мы практически не общались."
    bsar_narrator "Она любит до позднего вечера засиживаться на площади в обнимку с книжкой."  
    bsar_narrator "Никогда не видел её в шумных компаниях. Это всё, что я могу сказать про неё. Такая вот зеленоглазая девочка-тихоня." 
    insomnia_protagonist "Помнишь, как встречала новый год в детстве?" 
    bsar_narrator "Лена почему-то оживилась. Закрыла книгу и положила себе на колени." 
    insomnia_un "Да, помню, как отец наряжался в костюм Деда Мороза и выходил в подъезд, чтобы за десять минут до нового года позвонить в звонок, а затем подарить подарки. Я, конечно, всё понимала, и..." 
    bsar_narrator "Лена запнулась, видимо поняв, что слишком разговорилась. Спустя пару мгновений, говоря уже более тихим голосом, она закончила рассказ." 
    insomnia_un "...всегда подыгрывала ему." 
    bsar_narrator "А у меня также было? Вроде бы да. Также." 
    insomnia_protagonist "Да-а... Раньше было очень здорово." 
    insomnia_un "А сейчас разве нет?" 
    insomnia_protagonist "Ну не сказать, что уж слишком. {w}Кстати, я слышал, что Мику заболела. Не знаешь, что с ней?" 
    bsar_narrator "Лена печально вздохнула и перевела взгляд своих студёных зелёных глаз на меня." 
    insomnia_un "Ангина. Жалко её." 
    insomnia_protagonist "Всё будет хорошо." 
    insomnia_un "Ты плохо спишь, да?" 
    bsar_narrator "Со вздохом я покачал головой из стороны в сторону." 
    insomnia_protagonist "Снятся кошмары." 
    bsar_narrator "Она снова посмотрела на меня и улыбнулась, а по лицу - тени. Девушка собиралась что-то сказать, но передумала." 
    insomnia_un "Прости, что спросила. Знаешь, мне уже пора бежать. Пока." 
    bsar_narrator "Тихий голос девушки слился с ветром и унёс сказанные ею слова куда-то в сторону. Но, по всей видимости, она попрощалась." 
    insomnia_protagonist "Прощай, Лена." 
    hide insomnia_un with dissolve 
    bsar_narrator "Я вздохнул и засунул руки в карманы. {w}Новый год, значит?" 
    stop music fadeout 2 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard = True)
    scene bg int_house_of_mt_night2 with Dissolve(1) 
    play ambience ambience_medstation_inside_night fadein 2
    play sound_loop insomnia_couch fadein 2
    bsar_narrator "В домик я вернулся пустым и уставшим."
    bsar_narrator "Этот день казался противоестественно длинным, как будто в сутках появился ещё один, а может и все два лишних часа." 
    bsar_narrator "Несмотря на минусовую температуру за окном, мне было невероятно жарко, словно моя комнатушка превратилась в «ЗИЛовскую» микроволновку."  
    bsar_narrator "Записка. {w}Ульяна же просила меня прочитать её вечером. Как я мог забыть?"
    bsar_narrator "Кое-как повесив амулет над изголовьем кровати, я лёг на одеяло в одежде."  
    bsar_narrator "Потом. {w}Всё потом. Времени до отбоя у меня ещё много. Даже Ольга ещё не пришла."
    show insomnia_us_note with dissolve
    bsar_narrator "В послании было всего два предложения."
    bsar_narrator "По телу пробежали мурашки, а жар почему-то прошёл."
    bsar_narrator "Кратко и лаконично. Буквы на листке бумаги не будут заикаться, краснеть и отводить взгляд. {w}Так проще."
    hide insomnia_us_note with dissolve
    bsar_narrator "И всё-таки Алиса была права. А ведь и вправду, на моей памяти она не разу не ошибалась."
    bsar_narrator "Если я скажу, что у меня нет чувств к Ульяне, я буду полным лжецом."  
    bsar_narrator "Мне захотелось поговорить с ней до назначенного времени, но усталость напомнила о себе." 
    bsar_narrator "Я зевнул так, что чуть не свело челюсть, а глаза начали слипаться. Ладно. {w}Потом. {w}Всё потом. Времени у меня ещё много..."
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw"
    stop sound_loop fadeout 2
    stop ambience fadeout 2
    scene bg insomnia_prolog_bw
    show insomnia_static_noise_anim
    with insomnia_flash 
    play ambience insomnia_hum fadein 2 
    insomnia_she_red "Прости..." 
    insomnia_protagonist "За что?"
    insomnia_she_red "Я... я не смогла тебе помочь. Время вышло. Придётся смириться с неотвратимым."
    $ insomnia_show_centered_text("Свобода.")
    $ insomnia_show_centered_text("Свобода от оков.")
    $ insomnia_hide_centered_text(dspr)
    bsar_narrator "Снова {i}та{/i} лёгкость и безмятежность. Чувствую себя... живым." 
    $ insomnia_show_centered_text("Да, ЖИВЫМ!")
    $ insomnia_hide_centered_text(dspr)
    insomnia_she_red "Нам пора встретиться. Кажется..."
    $ renpy.pause(1, hard = True)

    if persistent.font_size == "large":
        insomnia_she_red "{isc}{=insomnia_scared_text_red_large}Кажется, я умираю.{/=insomnia_scared_text_red_large}{/isc}"

    elif persistent.font_size == "small":
        insomnia_she_red "{isc}{=insomnia_scared_text_red_small}Кажется, я умираю.{/=insomnia_scared_text_red_small}{/isc}"

    insomnia_she_red "Но что-то дало мне силы на последний рывок." 
    insomnia_protagonist "Как ты можешь умереть?" 
    insomnia_she_red "С того момента, как я сюда попала, силы стремительно покидают меня. {w}Я не смогла. {w}Ты не вспомнил."
    insomnia_she_red "Позволь дать тебе ответы перед..."
    $ renpy.block_rollback()
    $ persistent.timeofday = "fog"
    $ persistent.sprite_time = "day" 
    scene bg insomnia_ext_house_of_mt_fog with insomnia_flash
    play music insomnia_dark_shades fadein 5
    bsar_narrator "Ужасный кашель обжигает и раздирает горло. Я падаю на землю, пытаясь откашляться." 
    $ renpy.pause(1, hard = True) 
    bsar_narrator "Спустя какое-то время мне становится лучше."
    $ insomnia_show_centered_text("Где я?")
    $ insomnia_hide_centered_text(dspr)
    bsar_narrator "Кругом мертвенная тишина, которую нарушает только гулкий стук моего сердца." 
    bsar_narrator "Всё застилала густая молочная мгла. Не могу толком ничего разглядеть дальше одного ярда." 
    insomnia_she_red "Ты слышишь меня? Ты должен слышать! Иди ко мне." 
    insomnia_protagonist "Но куда я должен идти?" 
    bsar_narrator "Мой голос сорвался на более низкую ноту, а окончание вопроса поглотил этот всеобъятный туман." 
    insomnia_she_red "Ты знаешь, куда тебе нужно. Просто иди." 
    bsar_narrator "И я пошёл." 
    scene bg insomnia_ext_square_fog with dissolve 
    bsar_narrator "Кажется, я вышел на площадь, когда споткнулся и ударился о что-то металлическое."

    if persistent.font_size == "large":
        bsar_narrator "{isc}{=insomnia_scared_text_style_large}Дыхание участилось, а руки пробил тремор.{/=insomnia_scared_text_style_large}{/isc}"

    elif persistent.font_size == "small":
        bsar_narrator "{isc}{=insomnia_scared_text_style_small}Дыхание участилось, а руки пробил тремор.{/=insomnia_scared_text_style_small}{/isc}"

    bsar_narrator "Лавочка. {w}Просто лавочка. {w}Нужно идти дальше." 
    scene bg insomnia_ext_path2_fog with dissolve 
    bsar_narrator "Что происходит?" 
    bsar_narrator "Я уже сошёл с ума? Куда я вообще иду? Не знаю!"
    $ insomnia_show_centered_text("Я НЕ ЗНАЮ, ЧЁРТ ПОБЕРИ!")
    $ insomnia_hide_centered_text(dspr)
    bsar_narrator "Нет, нет, нет. {w}Нельзя терять самообладание. {w}Нужно идти."
    bsar_narrator "Идти..."
    scene bg insomnia_ext_old_building_fog with dissolve
    bsar_narrator "Неожиданно туман начал рассеиваться, и я смог разглядеть обветшалое уродливое здание." 
    bsar_narrator "Щербатая улыбка крыши, зияющая пробоинами, и пустые глазницы окон, смотрящие в пустоту." 
    bsar_narrator "Кажется, Ольга рассказывала мне про это место. Старый корпус. Мне сюда. Точно сюда."
    stop music fadeout 2
    scene bg insomnia_int_old_building_night_edited with dissolve 
    insomnia_protagonist "Что даль..." 
    stop ambience fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw" 
    scene bg insomnia_form 
    show insomnia_static_noise_anim
    with insomnia_flash
    play ambience ambience_medstation_inside_night fadein 2
    play music insomnia_defeated_clown fadein 2
    insomnia_she_red "Это пионерская форма твоей сестры?" 
    insomnia_protagonist "Да. Она часто мне рассказывала о том пионерлагере." 
    insomnia_protagonist "«Совёнок»! Я то сам в детских лагерях никогда и не бывал, а пионером уж подавно не был. Советы через год после моего рождения развалились." 
    insomnia_she_red "И много она тебе рассказала?" 
    insomnia_protagonist "Да-а. Я себе этот лагерь по её рассказам столько раз представлял." 
    insomnia_protagonist "Во всех подробностях. Мечтал когда-нибудь попасть в него. {w}Эх, детские грёзы. Не хочу, чтобы после её смерти эти вещи пылились в каком-то чулане." 
    insomnia_she_red "А меня бы с собой взял?" 
    insomnia_protagonist "Куда?" 
    insomnia_she_red "В «Совёнок»!" 
    insomnia_protagonist "Взял бы, конечно! Это бы были прекрасные воспоминания!" 
    insomnia_protagonist "{i}Воспоминания на всю жизнь!{/i}" 
    stop ambience fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "fog"
    scene bg insomnia_int_old_building_night_edited 
    show insomnia_she_night
    with insomnia_flash
    play ambience insomnia_hum fadein 2
    insomnia_she_red "Дальше я дам тебе ответы, какие смогу, но времени у нас мало и то, что ты увидишь, может повлиять на исход всего." 
    $ renpy.start_predict("insomnia/images/gui/misc/heart_monitor*.*")

    menu:
        "Где я?":
            insomnia_she_red "Как ты мог понять по пробившимся к тебе фрагментам памяти, случились две трагедии. Сначала в аварии скончалась твоя сестра. Затем погибла... {w}Я."
            $ renpy.block_rollback()
            $ persistent.timeofday = "bw"  
            scene bg insomnia_medical_room_celling 
            show insomnia_static_noise_anim
            with insomnia_flash
            play sound_loop insomnia_hum fadein 2
            insomnia_doctor "Примите мои соболезнования. Мы сделали всё, что смогли, но она скончалась, не выйдя из комы."  
            insomnia_protagonist "Когда я смогу забрать тело?"  
            insomnia_doctor "Но... Вам не нужно время, чтобы...."  
            insomnia_protagonist "Она умерла. С этим просто нужно смириться. Когда я смогу забрать тело?"
            stop sound_loop fadeout 2
            $ renpy.block_rollback()
            $ persistent.timeofday = "fog" 
            scene bg insomnia_int_old_building_night_edited
            show insomnia_she_night
            with insomnia_flash 
            insomnia_she_red "Это было для тебя страшным ударом. {w}Ты просто не выдержал. Пара недель беспробудного пьянства, безрезультатные попытки сослуживцев достучаться до тебя." 
            insomnia_she_red "В конце концов, ты сделал неправильный выбор."
            $ renpy.block_rollback()
            $ persistent.timeofday = "bw" 
            scene bg insomnia_makarov_pistol
            show insomnia_static_noise_anim
            with insomnia_flash
            play sound_loop insomnia_hum fadein 2
            $ renpy.pause(1.5, hard = True)
            scene bg white with insomnia_flash
            play sound insomnia_handgun
            $ renpy.pause(1, hard = True)
            show blink
            $ renpy.pause(2, hard = True)
            scene bg insomnia_prolog_bw behind blink
            show insomnia_static_noise_anim behind blink
            hide blink
            with insomnia_flash
            insomnia_fox_orange "Какие у него шансы выйти из комы, Иван Степанович?"
            insomnia_doctor "Огнестрельное в голову - это не шутки. Удивительно, что он вообще смог выжить." 
            insomnia_fox_orange "Зачем ты так?" 
            insomnia_doctor "Ладно, милочка, вашему другу нужен покой. Пойдемте."
            stop sound_loop fadeout 2
            $ renpy.block_rollback()
            $ persistent.timeofday = "fog" 
            scene bg insomnia_int_old_building_night_edited
            show insomnia_she_night
            with insomnia_flash
            insomnia_she_red "И вот мы здесь." 
            $ insomnia_show_centered_text("{isc}{=insomnia_scared_text_centered}Время пришло.{/=insomnia_scared_text_centered}{/isc}")
            $ insomnia_show_centered_text("{isc}{=insomnia_scared_text_centered}Прости.{/=insomnia_scared_text_centered}{/isc}")

        "Кто ты?":
            $ insomnia_paradise_ending_v += 1 
            stop ambience fadeout 2
            $ renpy.block_rollback()
            $ persistent.timeofday = "bw"
            scene bg insomnia_roof
            play ambience insomnia_winter_wind fadein 2
            show insomnia_snow_layer3_anim_quick
            show insomnia_snow_layer2_anim_quick
            show insomnia_she
            show insomnia_snow_layer1_anim_quick
            show insomnia_snow_layer0_anim_quick
            show insomnia_static_noise_anim
            with insomnia_flash
            insomnia_she_red "Так и знала, что найду тебя здесь!" 
            insomnia_protagonist "Неужели я настолько предсказуем?" 
            insomnia_she_red "Нет. Конечно нет. Просто ты мне сам как-то рассказывал, что тебе здесь нравится из-за...{w=1.0}{nw}" 
            insomnia_protagonist "Из-за того, что тут очень спокойно." 
            insomnia_she_red "И очень холодно." 
            insomnia_she_red "Значит завтра ты всё-таки уезжаешь?" 
            insomnia_protagonist "Да. Завтра я уезжаю."  
            insomnia_she_red "Я буду ждать. Только не забывай о том, что я говорила, хорошо?" 
            insomnia_protagonist "{i}«Чтобы не случилось, я всегда найду к тебе дорогу?»{/i}"  
            insomnia_she_red "Именно!"

    stop ambience fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "bw"
    $ renpy.pause(1, hard = True)
    scene bg insomnia_heart_monitor 
    show insomnia_heart_monitor_frame
    with insomnia_flash
    play sound_loop insomnia_hum
    $ renpy.pause(1, hard = True)
    $ insomnia_heart_monitor_phrases_f("insomnia_military_service")
    $ insomnia_heart_monitor_phrases_f("insomnia_composure")
    $ insomnia_heart_monitor_phrases_f("insomnia_institute")
    $ insomnia_heart_monitor_phrases_f("insomnia_meeting_with_her")
    $ insomnia_heart_monitor_phrases_f("insomnia_love")
    $ insomnia_heart_monitor_phrases_f("insomnia_police_work")
    $ insomnia_heart_monitor_phrases_f("insomnia_fox")
    $ insomnia_heart_monitor_phrases_f("insomnia_friendship")
    $ insomnia_heart_monitor_phrases_f("insomnia_rest")
    $ insomnia_heart_monitor_phrases_f("insomnia_easy_money")
    $ insomnia_heart_monitor_phrases_f("insomnia_protection")
    $ insomnia_heart_monitor_phrases_f("insomnia_drug_trafficking")
    $ insomnia_heart_monitor_phrases_f("insomnia_sisters_death")
    $ insomnia_heart_monitor_phrases_f("insomnia_nightmares")
    $ insomnia_heart_monitor_phrases_f("insomnia_doubts")
    $ insomnia_heart_monitor_phrases_f("insomnia_new_deal")
    $ insomnia_heart_monitor_phrases_f("insomnia_her_death")
    stop sound_loop fadeout 2
    stop music fadeout 2

    if insomnia_paradise_ending_v == 3:
        jump insomnia_paradise_ending

    else:
        jump insomnia_awakening_ending

label insomnia_awakening_ending:
    scene bg black with insomnia_flash
    play sound insomnia_heart_stopped
    $ renpy.pause(6, hard = True)
    scene bg white with insomnia_flash
    $ renpy.pause(1, hard = True)
    
    if not persistent.insomnia_achievements["insomnia_awakening"]:
        $ persistent.insomnia_achievements["insomnia_awakening"] = True
        $ insomnia_show_achievement("insomnia_awakening")

    $ renpy.pause(1, hard = True)
    scene bg black with dissolve
    stop sound_loop fadeout 2
    $ renpy.pause(1, hard = True)
    $ insomnia_set_main_menu_cursor()
    return

label insomnia_paradise_ending:
    $ insomnia_heart_monitor_phrases_f("insomnia_sleep_that_knows_no_breaking")
    scene bg white with insomnia_flash
    play sound insomnia_heart_stopped
    $ renpy.pause(6, hard = True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day"
    $ renpy.pause(1, hard = True)
    scene bg insomnia_ext_road_winter_day with insomnia_flash
    play ambience insomnia_winter_wind fadein 2
    play music insomnia_nightwish_nemo_piano_cover fadein 2
    bsar_narrator "Ну вот я и приехал в пионерлагерь «Совёнок»."
    scene bg insomnia_ext_camp_entrance_winter_day with dissolve
    bsar_narrator "Из-за небольших проволочек с документами я задержался и приехал на день позже, но ничего страшного в этом нет, ведь впереди меня ждут целых три недели отдыха!" 
    show insomnia_us smile with dissolve
    bsar_narrator "Из-за ворот вдруг выглянула девочка, она подошла поближе и улыбнулась."  
    bsar_narrator "Очень симпатичная, кстати. Огненные, как цветок мака волосы, и голубые глаза, в которых, казалось, можно утонуть. Она невысокого роста, на вид ей лет шестнадцать. " 
    insomnia_usp "Привет, ты, наверное, только что приехал?" 
    insomnia_protagonist "Да. Только что."

    if not persistent.insomnia_achievements["insomnia_paradise"]:
        scene bg insomnia_titles_bg with Dissolve(1.5)
        $ persistent.insomnia_achievements["insomnia_paradise"] = True

        show insomnia_titles_final insomnia_titles_text at insomnia_titles_anim
        $ renpy.pause(38, hard = True)

        $ insomnia_show_achievement("insomnia_paradise")

    $ renpy.pause(1, hard = True)
    scene bg black with dissolve
    stop music fadeout 2
    stop ambience fadeout 2
    $ renpy.pause(1, hard = True)
    $ insomnia_set_main_menu_cursor()
    return