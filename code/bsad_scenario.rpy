label insomnia_day1:
    stop music fadeout 3
    $ save_name = ("День первый.")
    $ renpy.block_rollback()
    $ insomnia_onload("lock")
    $ renpy.pause(4, hard = True)
    $ persistent.sprite_time = "day"
    $ persistent.timeofday = "winter_night"
    $ renpy.movie_cutscene(insomnia_gui_path + "days_transitions/insomnia_day1.ogv")
    scene bg black
    $ renpy.pause(3.5, hard = True)
    $ insomnia_set_mode_nvl() 
    scene bg insomnia_prolog_blue with Dissolve(3)
    $ renpy.pause(1, hard = True)
    $ insomnia_onload("unlock")
    $ insomnia_set_timeofday_cursor_var = True
    play music insomnia_domitori_taranofu_slow_pulse fadein 3
    insomnia_narrator "{i}В этом мире есть множество вещей, которые нельзя объяснить. {w}Их невозможно понять, невозможно увидеть и доказать, но тем не менее они существуют.{/i}"
    insomnia_narrator "{i}Сон - одна из этих вещей.{/i}"
    insomnia_narrator "{i}Ещё наши предки считали, что во время сна душа может покидать физическое тело и, пересекая тонкую, невидимую человеческому глазу грань, путешествовать в другие миры.{/i}" 
    insomnia_narrator "{i}Поэтому, никто не может гарантировать Тебе, что вся Твоя жизнь - это не сон. {w}Сон, в котором пленённое тело переживает подобные друг другу дни снова и снова. Бесчисленное число раз...{/i}" 
    $ renpy.pause(1, hard = True)
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
    insomnia_narrator "От громкого звона будильника создаётся впечатление, что мне в голову вбивают гвозди. Этот противный звон эхом распространяется по всей комнате, заставляя меня сделать хоть что-то."
    hide blink 
    scene bg insomnia_int_house_of_mt_day_blurred behind blink 
    show unblink 
    $ renpy.pause(2, hard = True)
    stop sound_loop fadeout 2 
    insomnia_narrator "Брошенная наотмашь подушка заставила замолкнуть эту адскую машину." 
    insomnia_narrator "Чувствую себя потерянным, словно старая безделушка, которая ранее, по идее, приносила удачу, а сейчас пылится где-то под диваном, ожидая, когда кто-то случайно её найдёт." 
    play sound_loop insomnia_knock fadein 2
    scene bg int_house_of_mt_day with Dissolve(1.5)
    $ renpy.pause(2, hard = True)
    insomnia_narrator "Резкий стук в дверь возвращает меня в реальность. Раз, другой, третий."
    show blink
    $ renpy.pause(2, hard = True)
    insomnia_narrator "Я накрываюсь одеялом с головой в надежде, что этот незваный гость просто уйдёт." 
    stop sound_loop fadeout 2 
    insomnia_narrator "Через какое-то время стук прекращается. Похоже, мой экзекутор смирился со своим поражением." 
    insomnia_narrator "Но как ни крути, думать, что я скоро снова засну, было очень наивно с моей стороны. {w}Я ворочаюсь с бока на бок, но сон так и не приходит."
    hide blink
    show unblink
    $ renpy.pause(2, hard = True)
    insomnia_narrator "Посмотрев на часы, я замечаю, что давно проспал завтрак, и мне придётся ходить голодным до самого обеда."
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
    insomnia_narrator "Я более или менее привёл себя в порядок и не нашёл занятия лучше, чем посиделки на площади вместе с товарищем Гендой, который всё таким же каменным и тотально безучастным взглядом смотрел в пустоту."  
    insomnia_narrator "Устроившись на самой дальней скамейке, я попытался понять, что за чертовщина стала мне сниться. Кошмары? Может быть. Ничего не могу вспомнить."  
    insomnia_narrator "Вроде бы уже почти ухватился за что-то важное, значимое, как это что-то упорхает от меня, взмахнув крыльями, подобно Жар-птице." 
    insomnia_narrator "Вдруг краем глаза я заметил, что рядом со мной кто-то стоит."  
    insomnia_narrator "Я непроизвольно вздрогнул, что вызвало ехидный смешок у заставшей меня врасплох пионерки." 
    $ insomnia_set_mode_adv() 
    show insomnia_us normal with dissolve
    play music insomnia_afternoon fadein 4
    insomnia_narrator "Ульяна. Девочка-апокалипсис." 
    insomnia_narrator "Из-за её детской непосредственности мы не раз встревали в разного рода авантюры, и почти всегда нам приходилось отдуваться." 
    insomnia_narrator "Но всё же, несмотря на все ее проделки, на неё решительно невозможно злиться. И я покривлю душой, если скажу, что мне с ней не весело."
    insomnia_protagonist "И давно ты здесь стоишь, Ульяна?" 
    insomnia_us "Ты вообще когда-нибудь улыбаешься?" 
    insomnia_protagonist "Да. {w}Наверное." 
    insomnia_us "Как так вообще можно жить? Почему ты уже второй день ходишь с кислой миной? Сторонишься всех, а вчера вообще прошёл мимо и даже не поздоровался!" 
    insomnia_narrator "Ульяна интересуется моим состоянием. Один этот факт уже вызывает массу подозрений, но что-то в её взгляде ясно даёт понять - ей и вправду это интересно." 
    insomnia_protagonist "Извини, Уль. Просто чертовски скверное настроение в последнее время." 
    insomnia_narrator "Но я же не соврал. Просто сказал не всю правду."
    insomnia_us "Э-эй! Вообще-то человек настроение сам себе делает. Никто, кроме тебя, его тебе не сделает. Как ты сам для себя решил, так и будет!"
    insomnia_us "Вот если ты сам для себя решил: «Всё. Мне весело!», - то тебе весело, а если ты решил, что тебе грустно, так и будет."
    insomnia_narrator "Голубые глаза девушки горят энтузиазмом, словно она Уоллес, говорящий воодушевляющую речь перед сынами Шотландии. Причём в несвойственной для себя простодушной манере."
    insomnia_narrator "Поэтому, я с неподдельным интересом и заинтересованностью слушаю её наставляющий монолог." 
    insomnia_us "Вроде и старше меня, но до сих пор не понял этого..."
    insomnia_us "Улыбнись, дурак!" 
    insomnia_narrator "Как ни странно, но от слов этой рыжеволосой энергичной девчонки на сердце стало... {w}Теплее что ли. Эти слова колыхнули фибры души, напоминая о каком-то совсем позабытом чувстве."
    show insomnia_us dontlike with dspr
    insomnia_narrator "Я искренне улыбнулся Ульяне, получив такую же, но более озорную улыбку в ответ, которая почему-то сменилась лёгким румянцем на щеках и убегающим куда-то взглядом."
    insomnia_narrator "А может мне просто показалось."
    play sound sfx_dinner_horn_processed fadein 2
    $ renpy.pause(3, hard = True)
    insomnia_narrator "Неловкую паузу прервал горн. Пора на обед."
    show insomnia_us normal with dspr
    insomnia_us "Пошли на обед, дурак. Завтрак, как я понимаю, ты проспал."
    hide insomnia_us with dissolve
    insomnia_narrator "Хихикнула она и быстро зашагала в сторону столовой. Мне пришлось поторопиться, чтобы не отставать."
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
    insomnia_narrator "Неожиданно перед глазами всё пошло кувырком..." 
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
    insomnia_narrator "Что это, чёрт побери, было? Я упал и..." 
    insomnia_narrator "Не помню. Наверное, просто показалось."
    stop sound_loop fadeout 2
    scene bg insomnia_ext_square_winter_day
    show insomnia_us sad
    with Dissolve(1.5)
    insomnia_us "А-у-у! Ты там живой? Может мне вожатую позвать?" 
    insomnia_protagonist "Всё в порядке. Я просто поскользнулся и упал." 
    insomnia_us "Припадочный ты какой-то. Хватит валяться!"
    show insomnia_us normal with dspr
    insomnia_narrator "Ульяна улыбалась, но по беспокойному взгляду и едва заметным ноткам волнения в голосе можно понять, что она переживает за меня. Это... мило."
    scene bg insomnia_ext_dining_hall_away_winter_day with dissolve 
    insomnia_narrator "По мере приближения к столовой вокруг появляется всё больше и больше пионеров, совершающих своё голодное паломничество. Ульяна не стала меня ждать и поспешно ретировалась." 
    scene bg insomnia_ext_dining_hall_near_winter_day with dissolve 
    insomnia_narrator "Зазевавшись, я едва не сталкиваюсь с Алисой Двачевской, которую за глаза все называют ДваЧе." 
    show insomnia_dv normal with dissolve
    play music insomnia_ease fadein 2
    insomnia_dv "Эй! Смотри куда прёшь!" 
    insomnia_narrator "Алиса была не в настроении, но мастерски скрывала это за надменным выражением лица. Ещё чуть-чуть и она буквально испепелит меня взглядом."
    insomnia_protagonist "Что-то случилось?" 
    show insomnia_dv normal2 with dspr 
    insomnia_narrator "Она на мгновение удивлённо вскинула бровь."
    insomnia_narrator "Хоть постороннему человеку это будет не заметно, но за время проведённое здесь, тени злости и обиды на лице этой пионерки ясны мне как гримасы боли." 
    insomnia_narrator "По началу она казалась мне типичной хулиганкой из-за любви к всякого рода подколкам и нежеланию следовать правилам лагеря, но сейчас я понимаю, что она на самом деле добрая и наивная девушка, хоть и прячется под личиной хулиганки." 
    insomnia_narrator "Причины её напускного образа мне, к сожалению, не ясны." 
    show insomnia_dv normal with dspr
    insomnia_dv "Ольга случилась! Приехала из райцентра сама не своя. Наорала на меня из-за..."
    insomnia_dv "Уф. Забудь. {w}Испортила мне всё настроение, чтоб её!" 
    insomnia_protagonist "Да будет тебе! Она же постоянно всех гоняет. Не стоит зацикливаться на этом и портить себе настроение." 
    insomnia_narrator "Я тепло улыбнулся Алисе. Не стоит ожидать, что я получу от неё улыбку в ответ, но всё же на её лице не осталось и следа обиды." 
    insomnia_dv "Кто бы говорил. Сам то несколько дней уже ходишь с таким лицом, что у Лены цветы на подоконнике от твоего взгляда завяли." 
    insomnia_th "Похоже, что не одна Ульяна заметила изменения в моём поведении из-за этих ночных кошмаров. Вспомнить бы, что мне снится, раз это так влияет на моё состояние." 
    insomnia_protagonist "Как видишь, теперь я в полном порядке." 
    insomnia_narrator "Сказал я, улыбнувшись ещё шире и пожав плечами." 
    insomnia_protagonist "А цветы могли и из-за холода завянуть. Зачем она их вообще с собой привезла?" 
    insomnia_dv "Сам её и спроси, если интересно." 
    insomnia_narrator "Сквозь зубы сказала она."
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
    insomnia_narrator "Из-за нашей задержки столовая заметно опустела. Почти все пионеры, отобедав, убежали по своим делам. Взяв еду, мы с Алисой разделились." 
    insomnia_narrator "Что-то буркнув себе под нос, она села за столик с Ульяной, по взгляду которой можно было понять, что скоро в лагере случится что-то очень нехорошее." 
    insomnia_narrator "Получив порцию, я сел за ближайший свободный столик."  
    insomnia_narrator "Несмотря на то, что я не ел с самого утра, аппетита практически не было. Самозабвенно ковыряясь вилкой в тарелке, решил вернуться к этим странным снам." 
    insomnia_narrator "Уже третий день я не высыпаюсь по ночам, а наутро чувствую себя просто отвратительно. Было ли такое раньше? Странно. Ничего не могу вспомнить."
    insomnia_narrator "Я приехал в лагерь примерно две недели назад..."
    show insomnia_sl normal with dissolve
    insomnia_sl "Ты не против, если я присяду?" 
    insomnia_protagonist "Ч-что?" 
    insomnia_sl "Я присяду?" 
    insomnia_protagonist "А, конечно-конечно."
    scene bg insomnia_sl_normal with dissolve
    play music insomnia_stride fadein 4
    insomnia_sl "Ты последние дни слишком рассеянный. Завтрак сегодня пропустил и дверь не открыл, когда я стучалась. Проблемы со сном?"
    insomnia_narrator "Славяна опустила брови и посмотрела на меня негодующим взглядом." 
    insomnia_narrator "Она добрая, активная и ответственная девушка, которая всегда готова помочь. Как раз является помощницей Ольги, что вполне ожидаемо. {w}Правда, некоторые случайно обронённые слова или действия ставят под сомнения искренность её действий." 
    insomnia_narrator "Я устало вздыхаю и опускаю подбородок на ладони, вспоминая, как плохо сегодня спал." 
    insomnia_protagonist "Да. В последнее время мне снятся кошмары."
    scene bg insomnia_sl_tired with dissolve
    insomnia_narrator "Славяна немного дёргает головой, словно хочет что-то сказать, но не решается. Она выглядит... {w}уставшей."
    insomnia_protagonist "Ты не знаешь, зачем Ольга Дмитриевна ездила в райцентр?" 
    insomnia_sl "Она поехала забрать почту, но, кажется, у неё там ещё какое-то {i}личное дело.{/i} Правда, по приезде она сама не своя." 
    insomnia_protagonist "В смысле?" 
    insomnia_sl "Ну-у. Раздражительная какая-то стала. На Алису накричала." 
    insomnia_narrator "В этот момент мимо нашего стола прошли Ульяна с Алисой, и, услышав своё имя, ДваЧе очень недобро глянула на Славю." 
    insomnia_narrator "Похоже, у рыжей конфликт не только с Леной; наверное, здесь причина неприязни скрывается в чрезмерной правильности моей собеседницы." 
    insomnia_protagonist "Ты тоже неважно выглядишь..." 
    insomnia_narrator "Чёрт! Какую же глупость я только что сморозил. Такое нельзя говорить девушке!" 
    insomnia_sl "Да-а, наверное, так и есть." 
    insomnia_sl "Замоталась в последнее время. Нужно отдохнуть. Я всё же в лагере или где?" 
    insomnia_narrator "Мне показалось, что в её глазах промелькнул блеск, который до этого я видел только у Ульяны, когда она хочет влезть в какую-то авантюру." 
    insomnia_protagonist "Это славно." 
    insomnia_narrator "Я участливо улыбнулся и кивнул головой." 
    insomnia_sl "Ладно. Тогда я пойду. Увидимся!"
    scene bg insomnia_int_dining_hall_winter with dissolve
    insomnia_protagonist "Да, давай." 
    insomnia_narrator "Наверное, мне тоже стоит идти, иначе просижу в столовой до ужина..."
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
    insomnia_narrator "Ничего не понимаю. Что со мной происходит? Уже второй раз перед глазами всплывают образы, которые пропадают так же быстро, как и появляются." 
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
    insomnia_narrator "Довольно резко прозвучавший рядом голос Ольги Дмитриевны выбил меня из колеи, спутав ход мыслей."
    insomnia_mt "Я знаю, что ты сегодня не пришёл на завтрак и, по всей видимости, поздно проснулся! Я надеюсь, ты понимаешь, что такое поведение не подобает настоящему пионеру?"
    insomnia_narrator "Ольга сегодня и вправду какая-то взвинченная. Я редко слышал, чтобы она повышала голос, как сейчас."
    insomnia_narrator "Да, конечно, она пытается быть строгой с пионерами. {w}Но ключевое слово - пытается."
    insomnia_narrator "Например, она позволяла мне некоторые вольности, относясь с снисхождением к моим пропускам утреннего построения и далёкого от расписания подъёму."
    insomnia_protagonist "Да, извините, больше не повторится."
    insomnia_mt "Отлично! Осознание проблемы - половина её решения!"
    insomnia_protagonist "Да, конечно."
    show insomnia_mt angry behind insomnia_normal_snow_day with dspr
    insomnia_mt "Раз ты сейчас ничем не занят, то..."
    insomnia_narrator "В раздумьях она играет локоном своих волос, пытаясь придумать мне поручение."
    insomnia_protagonist "Пионер понял, что ему нужно найти социально полезное занятие!"
    insomnia_narrator "Прервал я её размышления, пока она не придумала мне что-то тяжёлое и энергозатратное."
    stop ambience fadeout 2
    scene bg black with Dissolve(1)
    $ renpy.block_rollback()
    $ renpy.pause(1, hard = True)
    $ persistent.timeofday = "winter_night"
    scene bg int_house_of_mt_night with Dissolve(1)
    play ambience ambience_medstation_inside_night fadein 2
    play music insomnia_domitori_taranofu_trouble fadein 2
    insomnia_narrator "Я уставился в потолок, словно пытаясь найти там хоть каплю мотивации. Из-за всей этой мыслительной деятельности я чувствую себя как выжатый лимон."
    insomnia_narrator "Может быть, выйти на прогулку и, просто ни о чём не думая, подышать свежим воздухом? Хотя, с другой стороны, я обещал Ольге заняться чем-то полезным."

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
    insomnia_narrator "Так! Я обещал, что сделаю, значит сделаю!"
    insomnia_narrator "Бегать по лагерю и искать себе занятие я не хочу, поэтому просто уберусь в домике."
    scene bg black with Dissolve(1)
    $ renpy.pause(0.5, hard = True)
    scene bg int_house_of_mt_night with Dissolve(1)
    insomnia_narrator "Спустя тридцать минут, я смог привести свою обитель в более или менее презентабельный вид."
    insomnia_narrator "Я уже заканчивал, как мне попался на глаза листок, валяющийся под кроватью Ольги. Любопытство взяло верх, и я решил прочесть его содержимое."
    $ insomnia_set_mode_nvl()
    insomnia_narrator "{i}Оля! Мне бесконечно жаль, что приходится писать тебе об этом. Жаль, что наши отношения больше не те, какими они были раньше - ласковыми, теплыми, нежными.{/i}"
    insomnia_narrator "{i}Да ты и сама всё прекрасно видишь... Видишь, как мы отдалились друг от друга, как наши чувства угасают с каждым днём. Об этом говорит и редкость наших встреч, и холод в наших голосах...{/i}"
    insomnia_narrator "{i}Да чёрт, даже этот лагерь, в который я так настойчиво просил тебя не ехать, хватаясь за каждую соломинку, чтобы сохранить наши отношения! Но, видимо, ты в этом не слишком заинтересована.{/i}"
    insomnia_narrator "{i}Я больше не могу так.{/i}"
    insomnia_narrator "{i}Холод с твоей стороны постепенно сделал бесчувственным по отношению к тебе и меня самого.{/i}"
    insomnia_narrator "{i}Я больше не хочу называть тебя своей, не хочу вдыхать запах твоих волос, который раньше казался приятнее любого изысканного парфюма, не хочу слышать твой голос.{/i}"
    insomnia_narrator "{i}Да, Оля, наверное, ты уже и сама всё поняла...{w} Я последний трус, раз не смог сказать тебе это вживую, но у меня есть другая девушка.{/i}"
    insomnia_narrator "{i}Желаю тебе тоже обрести свое счастье, несмотря на то, что ты могла просто его не терять. {w}Прощай.{/i}"
    $ insomnia_set_mode_adv()
    insomnia_narrator "Во дела-а-а. Так вот в чём дело!"
    insomnia_narrator "Если честно, то я даже не знаю, что думать."
    insomnia_narrator "Это письмо явно стало ударом для Ольги Дмитриевны и теперь понятно, почему она ходила такая злая."
    insomnia_narrator "Я быстро положил письмо обратно и лег на кровать."
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
    insomnia_narrator "Грустно улыбнулась она." 
    insomnia_protagonist "Немного. Вы, главное, не расстраивайтесь сильно, если случилось что-то плохое. Ведь плохое всегда рано или поздно заканчивается." 
    insomnia_narrator "Я тепло ей улыбнулся. Ольга удивлённо вскинула бровь, наклонила голову вбок и о чём-то задумалась." 
    insomnia_mt "Возможно ты прав. Ладно. Думаю, что тебе стоит лечь спать пораньше. Негоже пропускать завтрак." 
    insomnia_protagonist "Да, конечно."
    show blink
    $ renpy.pause(2, hard = True)
    scene bg black
    hide blink
    insomnia_narrator "На меня и вправду накатила сильная усталость и, как только голова коснулась подушки, я моментально заснул." 
    stop ambience fadeout 2
    $ renpy.pause(3, hard = True) 
    jump insomnia_day2 

label insomnia_day1_stroll: 
    $ renpy.block_rollback()
    insomnia_narrator "Ай! Да и чёрт с ним. Не думаю, что она вообще вспомнит об этом. Мне явно стоит проветриться."
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
    insomnia_narrator "Ворота."
    insomnia_narrator "Как бы я не пытался не думать об этих странных видениях, они, подобно мерзким осьминогам, тянутся своими отвратительными склизкими щупальцами к моему сознанию, чтобы..."
    insomnia_narrator "Э-эм."
    insomnia_narrator "О чём это я? Ах, точно, об осьминогах! Ненавижу осьминогов! Или я не об этом?"
    insomnia_narrator "Что-то у меня плохое предчувствие."
    stop music fadeout 1
    insomnia_narrator "Вдруг краем глаза я замечаю, как ко мне стремительно приближается..."
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
    insomnia_narrator "Снег попадает мне прямо в глаза..."
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
    insomnia_narrator "Я машинально делаю пару шагов назад, как вдруг всё встаёт с ног на голову."
    insomnia_narrator "Я падаю, теряя равновесие..."
    play sound sfx_bones_breaking
    show blink
    $ renpy.pause(2, hard = True)
    insomnia_narrator "Необычайно громко по всей округе эхом раздаётся ужасный хруст... или мне это кажется?" 
    insomnia_narrator "{i}Кажется что?..{/i}"
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
    insomnia_narrator "Крик? Кто-то кричит? Почему?" 
    insomnia_she "Э-это ч... ровь?!" 
    insomnia_she "Ч-чёр... Зов... жатую!"
    play sound insomnia_electro
    $ renpy.pause(1, hard = True)
    insomnia_voice "Иван Степанович, теряем! ЭЭГ показывает смерть мозга!"
    insomnia_narrator "Кажется, мне куда-то нужно? {w}Но куда? {w}Ладно... Неважно."

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
    insomnia_narrator "Я резко отскакиваю в сторону, и запущенный в меня снежок пролетает мимо." 
    insomnia_dv "Блин! Я надеялась, что попаду." 
    show insomnia_dv normal2 behind insomnia_normal_snow_night with dissolve 
    insomnia_narrator "С нескрываемой досадой в голосе выдала Алиса, выходя из-за статуи пионера." 
    insomnia_protagonist "Добрая ты девочка, Алиса. Что ты тут вообще забыла?" 
    insomnia_dv "А это уже не твоё дело, {i}дорогуша.{/i}" 
    insomnia_narrator "Что-то подозрительное промелькнуло в нотках её голоса..."
    insomnia_narrator "До того, как я успеваю среагировать, Ульяна молниеносно засыпает мне за воротник снег и также быстро отскакивает к Алисе."
    show insomnia_dv smile behind insomnia_normal_snow_night:
        linear 1.0 xalign 0.25
    $ renpy.pause(1.0, hard = True)
    show insomnia_us smile at right behind insomnia_normal_snow_night with dissolve
    insomnia_narrator "Наблюдая за моей агонией, рыжие в унисон заливаются звонким смехом."
    insomnia_protagonist "УЛЬЯНА! Чтоб тебя!" 
    insomnia_us "Как будто что-то плохое!" 
    insomnia_protagonist "Я ж тебя..." 
    show insomnia_us sad behind insomnia_normal_snow_night:
        linear 1.0 xalign 0.4
    $ renpy.pause(1.0, hard = True)
    show insomnia_dv sad behind insomnia_normal_snow_night 
    show insomnia_mt rage behind insomnia_normal_snow_night at right 
    with dspr
    insomnia_narrator "Но неожиданное появление Ольги Дмитриевны застаёт меня врасплох, и я замираю."
    insomnia_narrator "Сказать, что она злая, значит не сказать ничего. Кажется, вот-вот у неё вздуется вена на лбу." 
    insomnia_mt "Значит, вот оно - твоё социально полезное занятие?!" 
    insomnia_protagonist "Это.... Это не..." 
    insomnia_mt "Быстро в домик!" 
    insomnia_protagonist "Но ведь..." 
    insomnia_mt "Я сказала БЫСТРО!"
    insomnia_narrator "Блин! Всё очень и очень плохо. Бросив напоследок ошарашенный взгляд на притихших девчонок и обречённо качнув головой вожатой, я поспешил в домик."
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1.5, hard = True)
    scene bg int_house_of_mt_night with Dissolve(2)
    play ambience ambience_medstation_inside_night fadein 2
    insomnia_narrator "Надо же было так влипнуть! Наверное, Алисе с Ульяной тоже досталось. Нет. Точно досталось!" 
    insomnia_narrator "Мне совершенно не хотелось выслушивать нравоучения непонятно из-за чего разъяренной Ольги." 
    insomnia_narrator "К тому же накатила непонятно откуда взявшаяся усталость, и как только голова коснулась подушки я моментально заснул." 
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
    $ insomnia_onload("lock")
    $ persistent.timeofday = "winter_day"
    $ persistent.sprite_time = "day" 
    $ renpy.movie_cutscene(insomnia_gui_path + "days_transitions/insomnia_day2.ogv")
    $ renpy.pause(2, hard = True) 
    scene bg black
    show blink
    $ insomnia_set_timeofday_cursor_var = True
    $ insomnia_onload("unlock")
    insomnia_narrator "Нос заложен. Горло дерёт, словно связки сорваны от бессмысленного и громкого крика в пустоту. Глаза слезятся. Я плакал во сне. Почему? Не помню." 
    insomnia_narrator "Нахлынувшие после пробуждения мысли, подобно волнам во время прилива, смыли остатки сна из моей памяти, оставив только две мокрые дорожки на щеках." 
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
    insomnia_narrator "Пионерка фыркнула, уставившись на меня отрешённым взглядом."
    insomnia_narrator "Женя - живое воплощение лени со стервозным характером. И голосом настолько дребезжащим и скрипучим, что на ум невольно приходят ассоциации с несмазанной калиткой."
    insomnia_narrator "Мне кажется, что она еврейка, но я таки не уверен." 
    insomnia_mz "Я сказала, что мне нужна помощь в библиотеке. Поэтому, жду тебя после завтрака!" 
    insomnia_protagonist "Поговорим сначала о моей награде." 
    insomnia_narrator "Её глаза, смотрящие поверх очков, несколько мгновений излучали то любопытство, то полное безразличие к ситуации в целом и моей персоне в частности." 
    insomnia_th "Что же, всё равно делать мне сегодня нечего. Почему бы и не сходить?" 
    insomnia_protagonist "Ладно-ладно. Я приду." 
    insomnia_narrator "Прервал я Женю, которая, по всей видимости, уже намеревалась сказать какую-то остроту. Она довольно хмыкнула и встала из-за стола." 
    show insomnia_mz normal2 with dspr 
    insomnia_mz "Вот и славно. Не задерживайся!" 
    insomnia_protagonist "Конечно..." 
    hide insomnia_mz with dissolve
    insomnia_narrator "Господи, сколько раз нужно повторять самому себе, что надо сначала думать, а потом говорить." 
    insomnia_narrator "Я же только что сдуру подписал себе смертный приговор." 
    insomnia_narrator "Другими словами - больше часа в одном помещении с Женей."
    stop music fadeout 2 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard = True)
    scene bg insomnia_ext_library_winter_day
    show insomnia_heavy_snow_day
    show insomnia_normal_snow_day
    with Dissolve(1)
    play ambience insomnia_winter_wind fadein 2
    insomnia_narrator "И вот я стою в смятении перед библиотекой." 
    insomnia_narrator "Какую на этот раз чепуху она придумала, чтобы изобразить бурную деятельность?"
    insomnia_narrator "Может, пока не поздно, лучше пойти в домик?"
    insomnia_narrator "А ей потом скажу, что в столовой переел и стало плохо."
    insomnia_narrator "Мысль была замечательной."
    play sound sfx_open_door_1
    insomnia_narrator "Но только я развернулся спиной к двери, как она распахнулась."
    insomnia_mz "Ну? Чего ты тут стоишь, не заходишь?" 
    insomnia_narrator "Она что, у окна дежурит? Как она вообще узнала, что я тут?"
    insomnia_narrator "Несколько секунд я еще стоял неподвижно, осторожно подбирая слова."
    show insomnia_mz normal2 behind insomnia_normal_snow_day with dissolve
    insomnia_narrator "А потом с милой улыбкой повернулся к молодой любительнице книг."
    insomnia_protagonist "Женя! А я как раз к тебе шел!"
    show insomnia_mz angry behind insomnia_normal_snow_day with dspr
    insomnia_mz "Ага, спиной вперед?"
    insomnia_protagonist "А я это... {w}Повернулся посмотреть на... {w}То есть, мне послышалось... {w}Да! Послышалось, что Славя меня звала!" 
    insomnia_mz "Славя уже давно у меня в библиотеке сидит, умник. Если хочешь помогать, то заходи, а нет, то иди лесом."
    hide insomnia_mz with dissolve
    insomnia_narrator "И исчезла, скрывшись в дверном проеме." 
    insomnia_th "А она чертовски проницательная!"  
    insomnia_narrator "Не удивлюсь, если сквозь свои очки она видит не только душу человека, но и его будущее."
    play sound sfx_open_door_1
    $ renpy.pause(2, hard = True)
    stop ambience fadeout 2
    scene bg insomnia_int_library_winter_day with dissolve
    play ambience ambience_library_day fadein 2
    play music insomnia_over_the_time_sandy_winter fadein 2
    insomnia_narrator "Внутри библиотеки было немногим теплее, чем на улице. Пахло книжной пылью и коммунизмом." 
    insomnia_narrator "Атрибутика и портреты с лозунгами смотрели на меня буквально отовсюду, из-за чего по телу невольно пробежали мурашки." 
    insomnia_th "Нечасто же я заходил в библиотеку." 
    insomnia_narrator "Славя действительно была здесь и рылась в каких-то бумагах, перебирая их и перекладывая с места на место." 
    insomnia_narrator "Увидев меня, блондинка улыбнулась и слабо кивнула в знак приветствия, не отрываясь от работы." 
    insomnia_narrator "А Женя уселась прямо на полу среди башенок из книжек." 
    insomnia_narrator "Одни были открыты, другие лежали подальше, видимо, отложенные на потом." 
    insomnia_narrator "Тут были стопки самой различной литературы в самых разных переплётах." 
    insomnia_narrator "От старинных тряпичных до новеньких твердых." 
    show insomnia_mz smile with dissolve 
    insomnia_mz "Спасибо, что пришёл. На самом деле, я думала, что ты будешь отлынивать." 
    insomnia_protagonist "То, что я стою перед тобой, ни о чём не говорит?" 
    show insomnia_mz normal2 with dspr 
    insomnia_narrator "Женя смерила меня долгим строгим взглядом и глубоко вздохнула." 
    insomnia_protagonist "Так. Чем я буду заниматься? На полу сидеть?" 
    insomnia_mz "Нет. Впрочем, как хочешь. С прошлой смены в библиотеку не вернулось с десяток книг. И поэтому я решила их проштамповать." 
    insomnia_protagonist "Чего-чего делать?" 
    insomnia_mz "Проштамповать. Проставить метки нашего лагеря на форзац страницы с помощью штампа. Ты ведь знаешь, что такое форзац?" 
    insomnia_protagonist "Э-э-э... Коне-ечно." 
    show insomnia_mz angry with dspr 
    insomnia_narrator "Женя закатывает глаза и громко цокает языком." 
    insomnia_mz "Форзац — это лист бумаги, соединяющий корку книги и первую страницу. Это, по сути, первая страница и есть." 
    insomnia_narrator "Я живо кивал, наблюдая, как Женя опускает штампик на губку, смоченную чернилами, и проставляет клеймо на тот самый форзац." 
    insomnia_mz "Справишься?" 
    insomnia_narrator "Она указала на длинные ряды стеллажей за её спиной." 
    insomnia_th "М-да..." 
    insomnia_th "Намечается длинная и рутинная работа, но делать нечего." 
    insomnia_th "Я уже согласился помочь, и назад пути нет." 
    hide insomnia_mz with dissolve 
    insomnia_narrator "Я сел на пол рядом с Женей и принял от неё второй штампик и губку с чернилами, сразу же измазавшись в них." 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard = True) 
    scene bg insomnia_int_library_winter_day with Dissolve(1) 
    insomnia_narrator "Сорок или пятьдесят книг спустя я довёл процесс до автоматизма, позволяющий мне брать книгу, ставить печать и брать новую, практически не глядя на них." 
    insomnia_th "Наверное, так и чувствуют себя принтеры." 
    insomnia_narrator "В процессе работы мы переговаривались ни о чем и обо всем одновременно." 
    insomnia_narrator "Делились впечатлениями от лагеря, сплетничали о его обитателях, говорили о погоде, о жизни до лагеря и прочем." 
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
    insomnia_narrator "Она мило засмеялась, но мне пришлось вернуть её с небес на землю." 
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
    insomnia_narrator "Мысли путаются, наскакивают друг на друга, переплетаются. {w}Я не могу выудить из этой вакханалии хотя бы частичку воспоминаний."
    insomnia_protagonist "Не стоит беспокоиться. Я в норме, просто давайте поговорим о чем-нибудь другом." 
    insomnia_sl "Ну хорошо, понимаю, как скажешь." 
    insomnia_protagonist "Славь, я все хотел спросить тебя..." 
    insomnia_sl "Да?" 
    insomnia_protagonist "Тогда, в столовой... Что ты имела в виду, сказав «отдохнуть»?"  
    insomnia_sl "Тьфу! Так начал, я уже думала, будто что-то серьезное спросить собираешься." 
    insomnia_sl "И вообще, я тут совсем заболталась, мне уже нужно бежать, я Ольге Дмитриевной обещала помочь." 
    insomnia_sl "Ты не против, если я попрошу тебя доделать тут работу с бумагами? Пожа-алуйста?" 
    insomnia_narrator "Я осмотрел свои измазанные в чернилах руки." 
    insomnia_narrator "Определенно, смена деятельности мне не помешает. Нужно подумать." 
    insomnia_narrator "Женя кивнула мне, давая понять, что справится с остатками одна." 
    insomnia_narrator "Чёрт, как же гудит голова! Что же со мной происходит последние дни?" 
    insomnia_protagonist "Конечно, Славя! Для тебя - все, что угодно!" 
    insomnia_narrator "Сказал я, разминая свои затекшие от длительного сидения ноги." 
    hide insomnia_sl with dissolve 
    stop music fadeout 2 
    insomnia_narrator "Славя смежила губы в лучезарной улыбке и поспешно покинула библиотеку." 
    scene bg insomnia_logbook with dissolve 
    insomnia_narrator "Я сажусь за стол, оценивая оставшийся фронт работ." 
    insomnia_narrator "Тут осталось перенести несколько записей в формуляры. {w}Плёвое дело."
    scene bg black with Dissolve(1)
    $ renpy.pause(1, hard = True)
    scene bg insomnia_logbook with Dissolve(1)
    insomnia_narrator "И так сойдёт!" 
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
    insomnia_narrator "Не успел я толком отойти от библиотеки, как столкнулся с Алисой, которая, по всей видимости, спешила попасть внутрь и совершенно не смотрела по сторонам."  
    insomnia_narrator "Из-за удара она выронила книгу, которая упала на снег обложкой кверху. «Унесённые ветром»."
    insomnia_narrator "Заметив, что моё внимание приковано к книге, ДваЧе быстро её подняла, спрятав за спину." 
    insomnia_protagonist "Должок идёшь возвращать, Алиса?" 
    insomnia_dv "А тебе какое дело?" 
    insomnia_narrator "Губы плотно сжаты, свободная рука превращается в кулак." 
    insomnia_narrator "Не требуется обладать какими-то знаниями в области психологии, чтобы понять этот жест и пронизывающий меня крайне недовольный взгляд." 
    insomnia_narrator "Я смиренно киваю головой и улыбаюсь, пытаясь разрядить обстановку. {w}Получается немного фальшиво, но Алиса этого не замечает, или делает вид, что не замечает."  
    insomnia_narrator "Пионерка делает шаг назад и возвращается к своему надменно-безразличному состоянию." 
    insomnia_dv "Давай-давай, проходи, не задерживайся! И забудь то, что видел!" 
    insomnia_protagonist "Да, конечно. {w}Вот-вот уже. {w}Почти. {w}{i}Ещё чуть-чуть...{/i}." 
    insomnia_dv "Болван!" 
    hide insomnia_dv with dissolve 
    insomnia_narrator "ДваЧе прошла мимо меня, намеренно задев плечом."
    insomnia_narrator "Больше всего я удивляюсь тому факту, что позволяю себе пасовать перед этой девчонкой. {w}Боже, эта Алиса..." 
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
    insomnia_narrator "Чёрт! У меня очень стойкое чувство дежавю, словно события из ведений, которые я толком не могу вспомнить, уже и в правду происходили."  
    insomnia_narrator "Нет. Это не могут быть мои воспоминания! {w}Похоже, что мне светит путёвка в жёлтый дом." 
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
    insomnia_narrator "Ульяна тепло улыбнулась и подмигнула мне, а затем побежала в библиотеку. Странно видеть эту шестнадцатилетнюю егозу такой милой."  
    insomnia_narrator "Раньше она постоянно пыталась меня подколоть, а сейчас тишь да гладь." 

    if insomnia_day1_stroll == True: 
        insomnia_narrator "Не считая снежков, конечно." 

    play sound sfx_dinner_horn_processed fadein 2 
    $ renpy.pause(3, hard = True) 
    insomnia_narrator "Горн. Пора на обед."
    stop ambience fadeout 2 
    scene bg black with Dissolve(1)
    $ renpy.pause(1.5, hard = True)
    scene bg int_house_of_mt_day with Dissolve(1) 
    $ renpy.block_rollback()
    play ambience ambience_medstation_inside_night fadein 2
    play music insomnia_maconda_die_begin fadein 4
    insomnia_narrator "После обеда меня разморило."
    insomnia_narrator "Голова начала гудеть, а мысли кровавыми сгустками выскальзывать из черепа."
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
    insomnia_narrator "Нет же! Папа работает учителем, а мама бухгалтер."  
    insomnia_narrator "Я с отличием закончил десятый класс в Московской гимназии номер четырнадцать и за это был отправлен в этот лагерь, {i}потому что давно хотел сюда попасть.{/i}"  
    insomnia_narrator "{i}Ведь так?{/i}"
    stop ambience fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day" 
    scene bg int_house_of_mt_day with insomnia_flash 
    play ambience ambience_medstation_inside_night fadein 2 
    insomnia_protagonist "И что мне делать?" 
    insomnia_narrator "Задал я вопрос пустой комнате, которая ответила мне абсолютно ничем."
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
    insomnia_narrator "Я чувствую невероятную лёгкость и безволие, в какой-то мере, расконцентрированность." 
    insomnia_narrator "Пространство вокруг меня наполнилось звуками. {w}Тиканье часов, какой-то писк, шаги, едва различимые голоса вдали." 
    insomnia_voice "Я своими глазами это видел, Иван Степанович!" 
    insomnia_voice "Это просто чудо какое-то! Возможно, есть шансы, что он всё же..."
    scene bg black with insomnia_flash
    insomnia_narrator "А ведь понимаю, что сон. Поэтому пытался хитрить, ускользать, изворачиваться, чтобы не проснуться." 
    insomnia_narrator "Пытался оглохнуть, ослепнуть, дематериализоваться, чтоб реальность не могла меня изловить и затащить обратно."  
    insomnia_narrator "Хотелось ещё послушать, что говорят эти странные голоса."
    insomnia_narrator "Но вот звуки становятся тихими и невнятными, возвращается тяжесть тела..."
    insomnia_narrator "Кончилось."
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
    insomnia_narrator "Я закашлял. В горле першило, руки и ноги онемели. Чувствую себя отвратно." 
    show insomnia_mt angry with dspr 
    insomnia_mt "Ты здоров? Уже который день выглядишь... {w}неважно." 
    insomnia_protagonist "Всё в порядке. Просто плохо чувствую себя после дневного сна. Я прогуляюсь." 
    insomnia_mt "Подожди! На, возьми. Перекусишь хотя бы." 
    insomnia_narrator "Вожатая протянула мне целлофановый свёрток. Бутерброды." 
    insomnia_protagonist "Спасибо большое, Ольга Дмитриевна. Я пошёл, по дороге перекушу." 
    insomnia_narrator "Накинув пальто, я вышел из домика."
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
    insomnia_narrator "Давненько я не видел Мику. Хочу повидаться с этой весёлой и словоохотливой японкой. Скорее всего, она у себя в кружке."  
    insomnia_narrator "Может быть, спросить у неё про эти странные сны и видения? Она единственная, кто не будет искать скрытый смысл в моих словах и уж точно не станет крутить пальцем у виска." 
    play sound sfx_open_door_1
    $ renpy.pause(2, hard = True)
    stop ambience fadeout 2
    scene bg insomnia_int_musclub_night_2 with dissolve 
    play ambience ambience_medstation_inside_night fadein 2
    insomnia_narrator "Открыв дверь и зайдя внутрь, я стал свидетелем ссоры, которую точно не ожидал увидеть." 
    insomnia_narrator "Алиса с Леной? Ожидаемо."
    insomnia_narrator "Алиса со Славяной? Тоже."
    insomnia_narrator "Алиса, ругающаяся с Ульяной? Удивительно, но происходит."
    insomnia_narrator "Голоса доносятся из подсобки."
    scene bg insomnia_us_dv_confrontation with dissolve
    play music insomnia_painful_history fadein 2
    insomnia_us "Алиса, может быть, ты уже успокоишься?" 
    insomnia_dv "А может ты не будешь меня затыкать?!" 
    insomnia_us "Я не трогала его! Мы же вообще живём в разных доми..." 
    insomnia_dv "НЕ ВРИ! Я уверена, что его взяла ты! Верни сейчас же или хуже будет!" 
    insomnia_narrator "Кажется, дело может принять плохой оборот. {w}Стоит ли вмешиваться? С другой стороны, я точно не знаю, что здесь происходит."     
    $ persistent.sprite_time = "night"      

    menu: 
        "Вмешаться": 
            $ insomnia_day2_intervene = True 
            insomnia_narrator "И чего я встал как истукан? Нужно вмешаться, пока Ульяне не досталось. Я быстро перескакиваю порог и встречаюсь взглядом с Алисой."
            scene bg int_clubs_male2_night_nolight
            show insomnia_dv sad at left 
            show insomnia_us sad at right 
            with dissolve 
            insomnia_dv "ТЫ подслушивал?!" 
            insomnia_narrator "Я замер, не ожидав такой реакции." 
            insomnia_protagonist "Почему вы ругаетесь? Вас за километр слышно." 
            insomnia_dv "Ага-ага. Заливай больше. Сто процентов стоял под дверью и слушал, болван!" 
            insomnia_us "Алиса!" 
            insomnia_dv "А с тобой я позже разберусь!" 
            hide insomnia_dv with dissolve 
            stop music fadeout 4
            insomnia_narrator "ДваЧе толкнула меня и быстро скрылась в дверном проёме, оставив дверь нараспашку."
            insomnia_narrator "Я перевёл взгляд на ошарашенную Ульяну, но она лишь грустно помотала головой." 
            insomnia_us "Извини, что тебе пришлось это услышать. Она почти весь день такая злая. Я её попробую догнать и успокоить."
            hide insomnia_us with dissolve
            insomnia_narrator "Последнее предложение Ульяна пробормотала себе под нос и выскочила за дверь, громко зовя Алису."
            insomnia_th "Чёрт! Помог, называется."
            insomnia_narrator "Алиса точно на меня обидится, и Ульяна тоже была не особо рада моему появлению."  
            insomnia_narrator "Умею же я портить то, что, как казалось изначально, ещё больше испортить нельзя." 

        "Не вмешиваться": 
            $ insomnia_paradise_ending_v +=1 
            insomnia_narrator "Я почему-то ошеломленно замираю, не в силах сделать даже шаг, а девушки продолжают свой разговор на повышенных тонах."
            insomnia_us "Алиса, чтоб тебя! Перестань истерить! Я понимаю, насколько важен тебе этот дневник."
            insomnia_us "Мы подруги, и я бы никогда не навредила тебе!"
            insomnia_narrator "Ничего себе! Такого я точно не ожидал."
            insomnia_narrator "На мгновение в помещении музыкального кружка повисла полная тишина. Настолько тяжёлая и абсолютная, что кажется, словно воздух уплотнился и стал вязким." 
            insomnia_dv "Уль... Ульяна. Извини. {w}Не знаю, что на меня нашло. Я правда не хотела." 
            insomnia_narrator "Никогда не слышал, чтобы голос Алисы так дрожал." 
            insomnia_us "Всё в порядке. Давай завтра вместе поищем твой дневник?" 
            stop music fadeout 4
            insomnia_narrator "Я решаю постучать, чтобы выдать своё присутствие до того, как девочки увидят меня и обвинят в подслушивании." 
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
            insomnia_narrator "Девушки ненаигранно улыбались. Всё же хорошо, что я решил не лезть." 
            insomnia_protagonist "А что, собственно, с Мику?" 
            insomnia_dv "У неё какие-то проблемы с горлом. Заболела, бедняжка." 
            insomnia_us "Ага, жалко её." 
            insomnia_us "Ладно. Может, пойдём прогуляемся?" 
            insomnia_narrator "Ульяна потёрла руки и хитро подмигнула Алисе." 
            insomnia_dv "Я за! А ты, хлюпик?" 
            insomnia_protagonist "Опять какую-то авантюру надумали? Ну хорошо, я с вами."
            show insomnia_us smile with dspr
            insomnia_narrator "Ульяна подпрыгнула и хлопнула в ладошки." 
            insomnia_us "Вперёд к приключениям!"

    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(4, hard = True)      
    $ renpy.block_rollback() 

label insomnia_day3:
    $ save_name = ("День третий.")
    $ renpy.block_rollback()
    $ insomnia_set_null_cursor()
    $ insomnia_onload("lock")
    $ renpy.movie_cutscene(insomnia_gui_path + "days_transitions/insomnia_day3.ogv")
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
    $ insomnia_onload("unlock")
    insomnia_narrator "Тёмные переулки, руки в карманах, ладонь поглаживает холодную рукоять ПМа. Первый лёд хрустит под ногами. Луна за тучами спряталась, не показывается." 
    insomnia_protagonist "Лис, наш выход только после того, как клиент клюнет. Не раньше."
    insomnia_fox_orange "Да поняла я. Не учи учёного."
    insomnia_fox_orange "Чего ты вообще подписался на эту встречу?"
    insomnia_protagonist "ОД приписал. Сказал, что буду отрабатывать упущенный товар."
    insomnia_fox_orange "Ну ты даёшь."
    insomnia_fox_orange "Какого ты вообще попёрся туда? Это же не наш уровень, а ФСКН."
    insomnia_protagonist "Так получилось."
    insomnia_narrator "Я остановился у поворота и жестом показал своей напарнице замереть." 
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
    insomnia_narrator "Спросил. {w}И проснулся."
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_night"
    scene bg int_house_of_mt_night2 with insomnia_flash
    play ambience ambience_medstation_inside_night fadein 2
    play music insomnia_domitori_taranofu_planet_of_colds fadein 2
    play sound_loop insomnia_medical_devices fadein 2
    insomnia_narrator "В комнате было темно. Похоже, проснулся до рассвета."
    insomnia_narrator "Я открыл рот в беззвучном крике."
    insomnia_narrator "Нет, физической боли не было. {w}Было ощущение, что само моё естество разрывают, кромсают, сжигают изнутри."
    insomnia_narrator "Ещё чуть-чуть и я просто... {w}просто исчезну. Испарюсь, словно меня никогда и не было."
    insomnia_narrator "Лоб покрылся холодным липким потом, а по спине пробежали мурашки."
    $ insomnia_show_centered_text("Почему мне так тревожно и одиноко?")
    $ insomnia_show_centered_text("Почему возникло чувство вины?")
    $ insomnia_hide_centered_text(dspr)
    insomnia_narrator "В окно робко заглянула луна, освещая домик и даруя предметам более смазанные и кривые очертания."
    $ insomnia_show_centered_text("Я всё ещё сплю или уже нет?")
    $ insomnia_hide_centered_text(dspr)
    insomnia_narrator "В голову лез всякий вздор."
    insomnia_narrator "Попытался встать, но не смог. {w}Тело не слушалось. {w}Попытался снова. {w}Получилось. Собственные движения немного успокоили." 
    insomnia_narrator "Сознание прояснилось, и я смог сконцентрироваться. Всего лишь дурной сон. {w}Который раз."
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
    insomnia_narrator "Подошёл к окну. Оно показывало смазанные ели, причудливый танец падающих снежинок, спрятавшееся за рваными облаками небо."
    insomnia_narrator "Куда не глянь, везде простиралась хвойная стена. {w}Бескрайняя и до боли одинаковая."
    insomnia_narrator "Стало душно."
    insomnia_narrator "Горло свело судорогой, в груди возникло тянущее чувство. {w}Хочется курить."
    insomnia_narrator "Не знаю, почему я решил, что мне нужно именно этого, ибо я раньше никогда даже не пробовал табачить."
    insomnia_narrator "Захотелось выйти на улицу и бежать. Бежать пока не кончатся силы. Подальше от этих лесных стен и кошмаров."
    $ renpy.pause(2, hard = True)
    scene bg int_house_of_mt_night2 with fade
    insomnia_narrator "Я постоял ещё немного и вернулся в кровать, но спать уже не хотелось." 
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
    insomnia_narrator "Бледное, мелкое солнце светило на лагерь из последних сил. Светило, но ни капельки не грело." 
    insomnia_narrator "{i}Воспоминания на всю жизнь?{/i}" 
    insomnia_narrator "А какая меня дальше ждёт жизнь? Бренное существование в окружении мягких стен жёлтого дома и бормочущих всякую чушь чудаков?" 
    insomnia_narrator "Или дурдом выглядит иначе?" 
    insomnia_narrator "Хотя, почём мне знать, я там никогда не был!"
    insomnia_narrator "Ну вот. Опять потерял самообладание. Почему бы мне просто не рассказать кому-нибудь об этом?" 
    insomnia_narrator "Просто излить душу, может поплакать даже. {w}Смешно." 
    insomnia_narrator "Пару дней каких-то кошмаров, а уже раскис, как маленькая девочка, потерявшая плюшевого мишку." 
    insomnia_narrator "Линейка уже кончилась. Странно, что Слави сегодня на утреннем построении не было. Может, у неё какие-то проблемы?"
    insomnia_narrator "Наверное, всё же это не моё дело." 
    show insomnia_us smile behind insomnia_normal_snow_day with dissolve
    insomnia_us "А-у-у. Есть кто дома? Чего встал, как столб посреди площади? Линейка давным-давно закончилась." 
    insomnia_protagonist "Ах да. Извини." 
    insomnia_us "За что?" 
    insomnia_protagonist "В смысле?" 
    insomnia_us "За что извиняешься, говорю. Хватит тормозить!" 
    insomnia_protagonist "А, неважно. Как там Алиса?" 
    insomnia_us "В полном порядке." 
    insomnia_narrator "Пионерка улыбнулась и показала большой палец." 
    insomnia_narrator "А почему, собственно, не Ульяна?" 
    insomnia_narrator "Думаю, с ней вполне можно поговорить про кошмары. Но аккуратно и без лишних подробностей. Только при этом всегда остаётся шанс быть высмеянным." 
    insomnia_narrator "Начну издалека." 
    insomnia_protagonist "Как спалось?" 
    insomnia_us "Отлично, а почему спрашиваешь?" 
    insomnia_protagonist "Просто интересно." 
    insomnia_us "Что, бессонница мучает?" 
    insomnia_protagonist "Так заметно?" 
    insomnia_us "Очень заметно! Мешки под глазами уже больше, чем сами глаза. Ходишь как живой мертвец из того фильма..." 
    insomnia_narrator "Её правда. Мой внешний вид оставляет желать лучшего. Я похож на узника концлагеря, а не на счастливого пионера." 
    insomnia_us "Слу-у-ушай, а хочешь я тебе ловец снов дам? У меня сестра увлекается этой, как её..."
    show insomnia_us dontlike behind insomnia_normal_snow_day with dspr
    insomnia_narrator "Девушка замирает, сводит брови и начинает бегать глазами по площади, словно ища подсказку."
    show insomnia_us normal behind insomnia_normal_snow_day with dspr
    insomnia_us "Вспомнила! Мистикой она увлекается!" 
    insomnia_us "Короче, она мне сделала ловец снов. Амулет какой-то индейский. Говорит, что помогает с кошмарами." 
    insomnia_protagonist "А ты уверена, что он поможет?" 
    insomnia_us "Не нравится мне твой скепти-чтоб-его-цизм."
    insomnia_protagonist "Извини. Я с радостью возьму этот ловец снов."
    show insomnia_us smile behind insomnia_normal_snow_day with dspr
    insomnia_us "Отличненько! Увидимся на завтраке, там я тебе его и отдам." 
    hide insomnia_us with dissolve 
    insomnia_narrator "Ульянка на прощание махнула мне рукой и быстро убежала в сторону домиков. Ловец снов значит? Почему бы, собственно, и нет."
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
    insomnia_narrator "Усталость после практически бессонной ночи накрывала, подобно шерстяному одеялу." 
    insomnia_narrator "Полусладкий чай совсем не помогал. Насыпал ещё несколько ложек, размешал."  
    insomnia_narrator "Сахар помог чуть-чуть растопить окостеневший ум." 
    insomnia_narrator "Дико это всё. Сны снами, но слишком уж они реальными кажутся." 
    insomnia_narrator "И эти пробелы в памяти... {w}С ними что?" 
    insomnia_narrator "Я посмотрел на стену, словно пытаясь найти там ответ." 
    insomnia_narrator "Цементные швы между кафелем, да и сам кафель, были где-то тёмными от пыли, а где-то совершенно чистыми, если даже не блестящими." 
    insomnia_narrator "Как будто недомыли и бросили." 
    insomnia_narrator "Интересно, сколько ещё моё сознание будет таким же немытым? {w}Сколько я ещё буду осознавать, что это всего лишь сны, а не реальность?" 
    insomnia_narrator "Или, может быть, то и есть реальность, а это - всего лишь дурацкий сон?" 
    insomnia_narrator "Бред бьющегося в предсмертных конвульсиях Морфея... {w}Я запнулся." 
    insomnia_narrator "Дверь столовой распахнулась, и зашла Ульяна. Её-то я и дожидался. Боялся, что разминулись."
    stop music fadeout 2
    insomnia_narrator "Румяная с улицы, глаза блестят, на плечах снег тает. Сразу меня замечает, берёт поднос и садится напротив."
    show insomnia_us normal with dissolve 
    insomnia_us "Вот, принесла, как и обещала." 
    insomnia_narrator "Она протянула мне амулет." 
    show insomnia_dream_catcher with dissolve
    insomnia_narrator "Красивый."
    insomnia_narrator "Не помню, где я это слышал, но всё же. По древним преданиям плохие сны запутываются в паутине из ниток, а хорошие проскальзывают сквозь отверстие посередине." 
    insomnia_protagonist "Спасибо большое, Уль. Это многое для меня значит."
    hide insomnia_dream_catcher with dissolve
    insomnia_us "Ну что ты. Слушай, а возьми, пожалуйста, ещё это..." 
    insomnia_narrator "Девушка протягивает мне сложенный вчетверо тетрадный листок." 
    insomnia_narrator "Я уже собирался его развернуть, как Ульяна меня остановила." 
    insomnia_us "Подожди. Не читай его сейчас, пожалуйста. Потом. Вечером, когда будешь ложиться спать." 
    insomnia_narrator "Она густо краснеет, переводит взгляд вниз, изредка поглядывая на меня смущённым взглядом. К еде она так и не притронулась." 
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
    insomnia_narrator "И вправду, зачем? {w}Почему я до сих пор переживаю за Славю, хоть и решил, что это меня не касается?"
    insomnia_narrator "Не знаю. Но почему-то изнутри гложет чувство, словно я ей что-то должен. А что должен - поди разбери." 
    insomnia_narrator "Завтра поход. Она наверняка будет там." 
    show insomnia_mz out_normal:
        linear 1.0 xalign 0.72
    $ renpy.pause(1.0, hard = True)
    show insomnia_dv normal at left with dissolve
    insomnia_dv "Какие люди!"
    insomnia_mz "Двачевская."
    insomnia_dv "Привет, мышка-Женя."
    insomnia_mz "Ты неисправима! Мне пора в библиотеку."
    insomnia_protagonist "Удачи."
    insomnia_narrator "Женя выпрямилась, слегка откинула голову и свела брови. Со стороны казалось, что она смотрит на ДваЧе сверху вниз, хоть и ниже неё на полголовы."
    hide insomnia_mz with dissolve
    insomnia_narrator "Затем она резко повернулась к нам спиной и быстро засеменила в сторону библиотеки."
    show insomnia_dv normal:
        linear 1.0 xalign 0.5
    $ renpy.pause(1.0, hard = True)
    insomnia_protagonist "Злая ты, Алиса. Ты вообще хоть кого-то любишь?"
    insomnia_dv "Животных люблю. Кто-то там кошек любит, кто-то собак, а я всех люблю без разбора."
    insomnia_dv "Людей только не люблю. Надоели. Постоянно носятся туда-сюда."
    insomnia_dv "Агрессивные какие-то."
    insomnia_protagonist "Агрессивные?"
    insomnia_narrator "Я усмехнулся. Алиса нахмурилась."
    insomnia_dv "Что смешного?"
    insomnia_protagonist "Ничего. Как ты?"

    if insomnia_day2_intervene: 
        insomnia_narrator "Алиса едва заметно сморщила нос и сжала губы, сделав небольшой шаг в сторону." 
        insomnia_dv "Не твоё дело, подслушиватель!" 
        insomnia_protagonist "Это случайно получилось!" 
        insomnia_dv "Да-да. Ври больше! Случайно у него получилось." 
        insomnia_narrator "Я глубоко вздохнул и закатил глаза. Спокойно. {w}Раз. {w}Два. {w}Три." 
        insomnia_protagonist "Думай, что хочешь." 
        hide insomnia_dv with dissolve 
        insomnia_narrator "Махнув рукой, я развернулся и пошёл прочь с площади. Алиса крикнула мне вслед то ли «дурак», то ли «дубина». Не имеет значения." 
        jump insomnia_day3_after_dv  

    else:
        insomnia_narrator "Пионерка улыбнулась, немного опустив брови." 
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
        insomnia_narrator "Алиса дёрнула головой, чтобы убрать локон волос, полезший в глаза, и скрестила руки на груди. Повисло молчание."  
        insomnia_narrator "Мне кажется или воздух стал горячее?" 
        insomnia_narrator "По площади туда-сюда носились пионеры из младших отрядов. Играли в снежки, лепили снеговиков, строили снежные крепости. Весело быть детьми."  
        insomnia_narrator "Проблемы, которые сейчас давят, подобно каменной глыбе, неожиданно упавшей на голову, для детей всего лишь мелочь." 
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
    insomnia_narrator "А что, если Алиса права?" 
    insomnia_narrator "Ладно. Спешить некуда. Вечером узнаю." 
    scene bg black with Dissolve(1)
    $ renpy.pause(2, hard = True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_night"
    $ persistent.sprite_time = "night"
    scene bg insomnia_ext_square_winter_night_tree with Dissolve(1) 
    play music insomnia_domitori_taranofu_winter_night fadein 2 
    insomnia_narrator "Новый год подбирался всё ближе и ближе, скрываясь за предпоследним листом календаря. " 
    insomnia_narrator "Вся площадь была обряжена в яркие украшения. От гирлянд и разноцветной мишуры до игрушек и вырезанных из бумаги снежинок, создавая неповторимую атмосферу скорого торжества."  
    insomnia_narrator "Этот день сулил множество праздничных хлопот для всех обитателей лагеря. Ну, почти для всех... " 
    insomnia_narrator "Лампочки мигали и переливались, как бы крича о том, что тут самое праздничное место в округе. На лавочке недалеко от ёлки сидела Лена и читала книгу." 
    show insomnia_un normal with dissolve 
    insomnia_protagonist "Привет, Лен!" 
    insomnia_un "Привет." 
    insomnia_protagonist "Красивая ёлка." 
    insomnia_un "Да, красивая." 
    insomnia_narrator "Девушка неопределённо пожимает плечами и снова углубляется в чтение." 
    insomnia_narrator "Лена. Асоциальная и крайне застенчивая девушка."
    insomnia_narrator "За прошедшие две недели мы практически не общались."
    insomnia_narrator "Она любит до позднего вечера засиживаться на площади в обнимку с книжкой."  
    insomnia_narrator "Никогда не видел её в шумных компаниях. Это всё, что я могу сказать про неё. Такая вот зеленоглазая девочка-тихоня." 
    insomnia_protagonist "Помнишь, как встречала новый год в детстве?" 
    insomnia_narrator "Лена почему-то оживилась. Закрыла книгу и положила себе на колени." 
    insomnia_un "Да, помню, как отец наряжался в костюм Деда Мороза и выходил в подъезд, чтобы за десять минут до нового года позвонить в звонок, а затем подарить подарки. Я, конечно, всё понимала, и..." 
    insomnia_narrator "Лена запнулась, видимо поняв, что слишком разговорилась. Спустя пару мгновений, говоря уже более тихим голосом, она закончила рассказ." 
    insomnia_un "...всегда подыгрывала ему." 
    insomnia_narrator "А у меня также было? Вроде бы да. Также." 
    insomnia_protagonist "Да-а... Раньше было очень здорово." 
    insomnia_un "А сейчас разве нет?" 
    insomnia_protagonist "Ну не сказать, что уж слишком. {w}Кстати, я слышал, что Мику заболела. Не знаешь, что с ней?" 
    insomnia_narrator "Лена печально вздохнула и перевела взгляд своих студёных зелёных глаз на меня." 
    insomnia_un "Ангина. Жалко её." 
    insomnia_protagonist "Всё будет хорошо." 
    insomnia_un "Ты плохо спишь, да?" 
    insomnia_narrator "Со вздохом я покачал головой из стороны в сторону." 
    insomnia_protagonist "Снятся кошмары." 
    insomnia_narrator "Она снова посмотрела на меня и улыбнулась, а по лицу - тени. Девушка собиралась что-то сказать, но передумала." 
    insomnia_un "Прости, что спросила. Знаешь, мне уже пора бежать. Пока." 
    insomnia_narrator "Тихий голос девушки слился с ветром и унёс сказанные ею слова куда-то в сторону. Но, по всей видимости, она попрощалась." 
    insomnia_protagonist "Прощай, Лена." 
    hide insomnia_un with dissolve 
    insomnia_narrator "Я вздохнул и засунул руки в карманы. {w}Новый год, значит?" 
    stop music fadeout 2 
    stop ambience fadeout 2 
    scene bg black with Dissolve(1) 
    $ renpy.pause(1, hard = True)
    scene bg int_house_of_mt_night2 with Dissolve(1) 
    play ambience ambience_medstation_inside_night fadein 2
    play sound_loop insomnia_couch fadein 2
    insomnia_narrator "В домик я вернулся пустым и уставшим."
    insomnia_narrator "Этот день казался противоестественно длинным, как будто в сутках появился ещё один, а может и все два лишних часа." 
    insomnia_narrator "Несмотря на минусовую температуру за окном, мне было невероятно жарко, словно моя комнатушка превратилась в «ЗИЛовскую» микроволновку."  
    insomnia_narrator "Записка. {w}Ульяна же просила меня прочитать её вечером. Как я мог забыть?"
    insomnia_narrator "Кое-как повесив амулет над изголовьем кровати, я лёг на одеяло в одежде."  
    insomnia_narrator "Потом. {w}Всё потом. Времени до отбоя у меня ещё много. Даже Ольга ещё не пришла."
    show insomnia_us_note with dissolve
    insomnia_narrator "В послании было всего два предложения."
    insomnia_narrator "По телу пробежали мурашки, а жар почему-то прошёл."
    insomnia_narrator "Кратко и лаконично. Буквы на листке бумаги не будут заикаться, краснеть и отводить взгляд. {w}Так проще."
    hide insomnia_us_note with dissolve
    insomnia_narrator "И всё-таки Алиса была права. А ведь и вправду, на моей памяти она не разу не ошибалась."
    insomnia_narrator "Если я скажу, что у меня нет чувств к Ульяне, я буду полным лжецом."  
    insomnia_narrator "Мне захотелось поговорить с ней до назначенного времени, но усталость напомнила о себе." 
    insomnia_narrator "Я зевнул так, что чуть не свело челюсть, а глаза начали слипаться. Ладно. {w}Потом. {w}Всё потом. Времени у меня ещё много..."
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
    insomnia_narrator "Снова {i}та{/i} лёгкость и безмятежность. Чувствую себя... живым." 
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
    insomnia_narrator "Ужасный кашель обжигает и раздирает горло. Я падаю на землю, пытаясь откашляться." 
    $ renpy.pause(1, hard = True) 
    insomnia_narrator "Спустя какое-то время мне становится лучше."
    $ insomnia_show_centered_text("Где я?")
    $ insomnia_hide_centered_text(dspr)
    insomnia_narrator "Кругом мертвенная тишина, которую нарушает только гулкий стук моего сердца." 
    insomnia_narrator "Всё застилала густая молочная мгла. Не могу толком ничего разглядеть дальше одного ярда." 
    insomnia_she_red "Ты слышишь меня? Ты должен слышать! Иди ко мне." 
    insomnia_protagonist "Но куда я должен идти?" 
    insomnia_narrator "Мой голос сорвался на более низкую ноту, а окончание вопроса поглотил этот всеобъятный туман." 
    insomnia_she_red "Ты знаешь, куда тебе нужно. Просто иди." 
    insomnia_narrator "И я пошёл." 
    scene bg insomnia_ext_square_fog with dissolve 
    insomnia_narrator "Кажется, я вышел на площадь, когда споткнулся и ударился о что-то металлическое."

    if persistent.font_size == "large":
        insomnia_narrator "{isc}{=insomnia_scared_text_style_large}Дыхание участилось, а руки пробил тремор.{/=insomnia_scared_text_style_large}{/isc}"

    elif persistent.font_size == "small":
        insomnia_narrator "{isc}{=insomnia_scared_text_style_small}Дыхание участилось, а руки пробил тремор.{/=insomnia_scared_text_style_small}{/isc}"

    insomnia_narrator "Лавочка. {w}Просто лавочка. {w}Нужно идти дальше." 
    scene bg insomnia_ext_path2_fog with dissolve 
    insomnia_narrator "Что происходит?" 
    insomnia_narrator "Я уже сошёл с ума? Куда я вообще иду? Не знаю!"
    $ insomnia_show_centered_text("Я НЕ ЗНАЮ, ЧЁРТ ПОБЕРИ!")
    $ insomnia_hide_centered_text(dspr)
    insomnia_narrator "Нет, нет, нет. {w}Нельзя терять самообладание. {w}Нужно идти."
    insomnia_narrator "Идти..."
    scene bg insomnia_ext_old_building_fog with dissolve
    insomnia_narrator "Неожиданно туман начал рассеиваться, и я смог разглядеть обветшалое уродливое здание." 
    insomnia_narrator "Щербатая улыбка крыши, зияющая пробоинами, и пустые глазницы окон, смотрящие в пустоту." 
    insomnia_narrator "Кажется, Ольга рассказывала мне про это место. Старый корпус. Мне сюда. Точно сюда."
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
    insomnia_narrator "Ну вот я и приехал в пионерлагерь «Совёнок»."
    scene bg insomnia_ext_camp_entrance_winter_day with dissolve
    insomnia_narrator "Из-за небольших проволочек с документами я задержался и приехал на день позже, но ничего страшного в этом нет, ведь впереди меня ждут целых три недели отдыха!" 
    show insomnia_us smile with dissolve
    insomnia_narrator "Из-за ворот вдруг выглянула девочка, она подошла поближе и улыбнулась."  
    insomnia_narrator "Очень симпатичная, кстати. Огненные, как цветок мака волосы, и голубые глаза, в которых, казалось, можно утонуть. Она невысокого роста, на вид ей лет шестнадцать. " 
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

label sotp_three_deaths:
    stop music fadeout 3
    scene bg black with Dissolve(3)
    $ save_name = ("Три смерти.\nПролог.")
    $ renpy.block_rollback()
    $ sotp_onload("lock")
    $ persistent.timeofday = "bw"
    $ renpy.pause(3.5, hard = True)
    $ sotp_set_mode_nvl()
    scene bg sotp_prolog_bw
    show sotp_static_noise_anim
    with Dissolve(3)
    $ renpy.pause(1, hard = True)
    $ sotp_onload("unlock")
    $ sotp_set_timeofday_cursor_var = True
    play music sotp_bensound_sadday fadein 3
    sotp_narrator "У всех в жизни бывает день, который переворачивает всё с ног на голову. "
    sotp_narrator "Для кого-то это день встречи своей будущей любви, для кого-то день смерти самого близкого человека, а для меня это день получения первой взятки."
    sotp_narrator "Всё произошло на удивление буднично и спокойно. Просто в один момент в ящике моего рабочего стола оказался беременный купюрами конверт."
    sotp_narrator "Даже не могу вспомнить, за что именно я тогда получил эту мелочёвку."
    sotp_narrator "То ли благодарность за то, что быстро и тихо закрыл дело какого-то приблатнённого сынка, то ли это была озлобленная подачка какого-то барыги."
    sotp_narrator "Совесть? А что с ней? Она быстро покрылась коррозией цинизма, когда я вытаскивал из подъездов и магазинов буйных алкашей, будучи ещё работником патрульно-постовой службы."
    sotp_narrator "Совесть уже тогда перестала быть монолитной, но всё ещё стояла, правда её срок годности подходил к концу."
    nvl clear
    sotp_narrator "Кувалдой, совершившей последний удар по ставшей уже столь хрупкой совести, стала полностью умалишённая мать-наркоманка, отдававшая свою малолетнюю дочь на растерзание за очередную дозу."
    sotp_narrator "Это только обывателям кажется, что нам вместе с формой вместо живого сердца камень в грудину помещают, но нет."
    sotp_narrator "Всё куда более обыденно и прозаично."
    sotp_narrator "Мы просто начинаем видеть то, что вы не можете или стараетесь не замечать."
    sotp_narrator "Такую чернуху, что видим мы, не смогут вообразить даже самые изощрённые и воспаленные мозги любого из почивших и ныне живущих творцов."
    nvl clear
    sotp_narrator "Вы когда-нибудь видели, как у передознувшегося, бьющегося в агонии наркомана начинается обратная перистальтика?"
    sotp_narrator "О, это незабываемое зрелище. Это когда перед смертью у человека содержимое органов пищеварения начинает двигаться в обратном направлении."
    sotp_narrator "Если вы действительно верите, что бывает абсолютно безболезненная, а уж тем более чистая смерть, то, к сожалению, ваша вера совсем неоправдана."
    sotp_narrator "Наркомания, грабежи, убийства, изнасилования, самоубийства. Это только заглавие того списка мерзости, с которой я работаю."
    sotp_narrator "Совесть тут только мешает, поэтому лучше всего выкинуть её раньше, чем она заставит тебя сломаться."
    sotp_narrator "Ладно. Речь не об том."
    stop music fadeout 3
    scene bg black with Dissolve(3)
    $ save_name = ("Три смерти.\nАКТ 1. Как я жил.")
    $ renpy.pause(2, hard = True)
    $ sotp_show_centered_text("Три смерти. АКТ 1. Как я жил.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ sotp_set_mode_adv()
    scene bg sotp_ext_winter_park
    show sotp_snow_layer3_anim
    show sotp_snow_layer2_anim
    show sotp_yana
    show sotp_snow_layer1_anim
    show sotp_snow_layer0_anim
    show sotp_static_noise_anim
    with sotp_flash
    play ambience sotp_winter_wind fadein 2
    play music sotp_lucas_king_hurt fadein 2
    sotp_narrator "Вечерний зимний парк, острые снежинки царапают лицо."
    sotp_narrator "От вездесущего белого цвета уже рябит в глазах, ужасно хочется увидеть хоть какие-нибудь яркие цвета."
    sotp_narrator "Картинка мира превратилась в монотонную монохромную киноленту."
    sotp_th "Настроение паршивое."
    sotp_narrator "Неожиданно в затылок прилетает нечто холодное и мокрое."
    sotp_narrator "С характерным чавканьем снежок разбивается об мою голову и крупинки снега проваливаются за ворот, заставляя вздрогнуть всем телом."
    sotp_narrator "Я поворачиваюсь на шесть часов, лицом туда, откуда прилетел снежок, и вижу, что к отправке готовится новый снаряд."
    sotp_protagonist "Холодно же! Хватит! Выкинь! Выкинь снежок, кому говорю!"
    sotp_narrator "Она обиженно надувает щёки, потирая мокрой перчаткой красный от мороза нос."
    sotp_yana "Ладно, ладно."
    sotp_protagonist "Ты когда-нибудь станешь менее инфантильной?"
    sotp_yana "Не стану! К тому же, разве это что-то плохое?"
    sotp_narrator "К ней мгновенно возвращается былой задор. Она улыбается."
    sotp_protagonist "Ну вот. Опять эта ехидная улыбка! На тебя просто невозможно злиться."
    sotp_yana "А на меня и не нужно злиться, дурак."
    sotp_narrator "Я познакомился с этим чудным ребёнком в теле красивейшей девушки в институтские годы."
    sotp_narrator "Тогда я, молодой и неопытный, вчерашний школьник, который не хотел идти по стопам отца, повстречал свою первую любовь."
    sotp_narrator "Это была не та наивная юношеская влюблённость с потными ладошками и неловкими поцелуями возле подъезда."
    sotp_narrator "Нет, конечно, всё это было, но всё же чем-то наши отношения отличались от отношений сверстников."
    sotp_narrator "Наверное, потому что уже во вторую нашу встречу я сказал, что хочу увидеть её рядом с собой в свадебном платье."
    sotp_narrator "А я, стоит заметить, никогда не слыл вертопрахом, а уж тем более пустословом."
    sotp_yana "Ты, кстати, уже решил, что подаришь сестре на день рождения?"
    sotp_protagonist "Всё ещё думаю."
    sotp_narrator "Она остановилась и нахмурилась. Вперев руки в бока она, надув губы, сказала:"
    sotp_yana "Бу-бу-бу. Я мрачный и загадочный. Бу-бу-бу. Буду ходить по парку с лицом потенциального самоубийцы. Бу-бу-бу."
    sotp_protagonist "Вообще на меня не похоже!"
    sotp_narrator "Она всегда умеет заставить меня улыбаться, но вот пародии у неё не выходят от слова совсем."
    sotp_yana "Ещё как похоже! Чего ты после работы ходишь чернее тучи?"
    sotp_protagonist "Сложный период начался. Дел невпроворот. Старое разгрести не успеваешь, как новое появляется. Повышение ещё на носу."
    sotp_protagonist "Да и ты же помнишь. С начала декабря у меня начинается бессонница."
    sotp_yana "Ух!"
    sotp_narrator "Она «устрашающе» потрясла своим миниатюрным кулачком в воздухе."
    sotp_yana "Так! Слушать мою команду! Сейчас мы пойдём выбирать твоей сестре подарок, а завтра ты записываешься к врачу по поводу твоих проблем со сном. Всё ясно?!"
    sotp_narrator "Я резко встал по стойке смирно и отдал воинское приветствие."
    sotp_protagonist "Так точно, мой командир! Позвольте отнести вас до назначенной точки!"
    sotp_narrator "Я резво подскочил к ней и подхватил на руки. Лёгкая, как пёрышко. Яна же от неожиданности вскрикнула."
    stop music fadeout 3
    stop ambience fadeout 3
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_int_kitchen_bw 
    show sotp_sister
    show sotp_static_noise_anim
    play ambience ambience_medstation_inside_night fadein 2
    with Dissolve(2)
    sotp_narrator "Крохотная, но уютная кухонька сестры. На плите закипает чайник."
    sotp_narrator "Я сто раз предлагал ей заменить это старьё на электрический, но сестра постоянно отказывалась."
    sotp_narrator "Вот любит она чтобы как раньше, как в детстве. {w}Разница в возрасте у нас, конечно, заметная, но росли мы в ту эпоху, когда время застыло, словно смола."
    sotp_narrator "Она до сих пор сидит в куртке. Ох уж эта её дурная привычка не снимать верхнюю одежду дома."
    sotp_narrator "Мать постоянно её за это отчитывала, но уж если моя сестрёнка к чему-то привыкла, то никакими нравоучениями ты её не отвадишь."
    sotp_narrator "Не могу только понять как она не спарилась."
    sotp_protagonist "Будешь праздновать день рождения в этом году?"
    sotp_sister "Да. Возьму отгул и поеду к родителям, отдохну и маму с папой увижу. Что-то я замоталась с этой работой."
    sotp_narrator "Маму с папой... Она всегда говорит так, словно отец всё ещё жив, словно они с мамой сейчас так же, как мы, сидят на кухне, пьют чай."
    sotp_narrator "Мама смотрит какой-то очередной сериал, а отец буравит взглядом свежий выпуск газеты."
    sotp_narrator "Когда сестрёнка говорит, что повидалась с отцом, значит, она ездила на кладбище."
    sotp_narrator "Я не навещал папу уже много лет. Как раз после моего поступления на службу в полицию. Не знаю, почему так получилось. Просто не могу."
    sotp_narrator "Наверное, стыдно смотреть в его глаза на фотографии, выгравированной на мраморе."
    sotp_protagonist "Там же ещё лес рядом. Опять будешь в нём пропадать?"
    sotp_sister "Да-а. Как в детстве, когда за грибами в конце лета ходили. Помнишь?"
    sotp_protagonist "Помню. {w}Только я никогда этого не любил."
    sotp_narrator "Она помрачнела."
    sotp_sister "Как же эта работа тебя изменила... {w}Права была мама. {w}Зря ты пошёл по стопам отца."
    sotp_sister "Это работа не для тебя. Мясорубка, а не работа. Ты вообще доволен своей жизнью?"
    sotp_narrator "Мне повезло с сестрой. Несмотря на статус старшей, она никогда не позволяла себе обижать или подкалывать меня."
    sotp_narrator "Мы всегда общались на равных. С ней можно обсудить всё что угодно."
    sotp_protagonist "Да будет тебе. Всё в порядке. У меня есть ты, любимая девушка и хорошая подруга. Пока всё на месте, я счастлив."
    sotp_protagonist "Профессия накладывает свой след, но я держусь. Ты, вон, вообще лесником вроде когда-то хотела стать!"
    sotp_sister "Нашёл что вспомнить!"
    sotp_narrator "Она задорно хохочет."
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_int_float
    show sotp_yana
    show sotp_static_noise_anim
    with Dissolve(2)
    play ambience ambience_medstation_inside_night fadein 2
    sotp_yana "Я собралась. Идём?"
    sotp_narrator "Я загибаю край страницы книги, которую читал, и откладываю её в сторону."
    sotp_protagonist "Да, пошли."
    sotp_yana "До сих пор не могу понять, зачем ты постоянно читаешь. {w}Нет, это, конечно, здорово, но почему так много? Думаешь найти на страницах смысл жизни?"
    sotp_protagonist "Я уже нашёл этот смысл, когда встретил бойкую первокурсницу в институте."
    sotp_narrator "Она захихикала, но даже нисколечко не покраснела."
    sotp_yana "Ну расскажи в чём секрет то?"
    sotp_protagonist "Привычку много читать мне привил отец. «Читай, сынок», - говорил он, «В классике можно всегда найти правду, если хорошо искать»."
    sotp_protagonist "Меня, правда, тогда больше тянуло к фантастике, к далёким звёздам и бескрайнему космосу."
    sotp_protagonist "В итоге я вырос, понял, что отец всё же ошибался. {w}Правда оказалась не печатной, а привычка читать всё равно осталась. Вот и весь секрет."
    sotp_yana "Эх, а я то надеялась, что ты всё же разгадываешь тайну философского камня."
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    $ save_name = ("Три смерти.\nАКТ 2. Как я работал.")
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("Три смерти. АКТ 2. Как я работал.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    scene bg sotp_prosecutor_office
    show sotp_snow_layer3_anim
    show sotp_snow_layer2_anim
    show sotp_lis
    show sotp_snow_layer1_anim
    show sotp_snow_layer0_anim
    show sotp_static_noise_anim
    with Dissolve(2)
    play ambience sotp_winter_wind fadein 2
    play music sotp_master_of_spirits_own_shadow fadein 2
    sotp_narrator "Как только мы вышли на улицу, дышать стало легче. Внеочередное звание далось нелегко."
    sotp_narrator "«Ночная работа» сильно выматывает, но и плоды ты получаешь сочные."
    sotp_fox "Ну что, дорогуша, поздравляю с повышением! Обмоем звёздочку?"
    sotp_protagonist "Заметь, не я это предложил. Только недолго и немного."
    sotp_narrator "Лис. Моя добрая подруга и напарница. Мы пережили достаточно многое, чтобы доверять друг другу."
    sotp_narrator "Каждый из нас отлично знает про делишки другого, которые тянут на несколько статей уголовного кодекса, что, естественно, ещё больше скрепляет пайку нашего товарищества."
    sotp_narrator "Мы познакомились сразу после моего поступления на службу. Никогда бы не подумал, что такая надменная и ловкая на остроты девушка работает в полиции."
    sotp_narrator "Лис была бы отличной манекенщицей, с её то замашками. Смотреть на весь мир сверху вниз с обложки глянцевого журнала. Ей это к лицу."
    sotp_fox "Петля не жмёт?"
    sotp_narrator "Она лукаво улыбнулась."
    sotp_protagonist "Какая петля?"
    sotp_fox "Семейной жизни! Когда уже детишки? Крёстной возьмешь?"
    sotp_narrator "Спустя много лет нашей совместной работы, я наконец-то разгадал формулу, что заткнёт за пояс даже секрет создания золота из железа."
    sotp_narrator "Пара прямых и точных фраз про работу позволяют сбить её спесь."
    sotp_protagonist "Не паясничай. Ты, кстати, помнишь про следующую сделку, которую мы крышуем?"
    sotp_narrator "Она в мгновение ока становится серьёзной и даже немного встревоженной."
    sotp_fox "Ты то так не ори. Хочешь обратно в старлеи? Помню я, помню."
    sotp_protagonist "Вот и отлично. Поэтому я и не хочу сегодня напиваться."
    sotp_fox "Дело аж через неделю. Мог бы придумать отмазку получше. Просто пей больше воды между шотами. Нельзя нарушать традиции!"
    sotp_protagonist "Пошли уже. Пока про эти традиции не вспомнило пол-отдела и мне не пришлось раскошеливаться на целый банкет для дармоедов."
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_int_od_cabinet
    show sotp_od
    show sotp_static_noise_anim
    with Dissolve(2)
    play music sotp_maconda_die_begin fadein 2
    sotp_od "Закрой дверь и садись."
    sotp_narrator "После вчерашнего голова немного гудела. Мы с Лис явно перебрали, но благодаря её совету с постоянным запиванием алкоголя водой, катастрофы не произошло."
    sotp_narrator "Правда, видок у меня довольно потрёпанный. {w}Не самый лучший момент, чтобы приходить на ковёр к начальству, но уже никуда не денешься."
    sotp_protagonist "По какому поводу обязан, Олег Дмитриевич?"
    sotp_narrator "Он выжидающе молчал, словно давая мне возможность додуматься самому и озвучить догадку."
    sotp_narrator "Олег Дмитриевич больше походит на кремень, нежели на человека." 
    sotp_narrator "Постоянно тыкает тебя мордой во все твои промахи, постоянно наблюдая за любыми твоими действиями."
    sotp_narrator "Оно, конечно, не мудрено. Круговая порука никуда не пропадала."
    sotp_narrator "Хотя, его монолитный казалось бы образ немного надломился в моих глазах."
    sotp_narrator "Как-то давно он позвонил мне в час ночи, позвал, нет, приказал ехать в бар, что находится неподалёку от центра города."
    sotp_narrator "От него ушла жена, не выдержавшая всей этой нервотрепки и он решил найти утешение на дне стакана, но по всей видимости в одиночку это было сделать не так просто."
    sotp_od "Хочу напомнить, насколько важна для тебя следующая сделка."
    sotp_od "После того провала с крупной партией тобой остались очень недовольны достаточно влиятельные люди. Мне потребовалось приложить много усилий, чтобы сгладить все углы."
    sotp_od "Стоило бы передумать о твоём повышении, но мы знакомы уже давно, да и я знаю, что ты отличный работник. Но более промахи неприемлемы."
    sotp_od "Если снова что-то пойдёт не так, пеняй на себя. Ты меня понял?"
    sotp_narrator "Говорил он медленно и спокойно. Только за этим мнимым спокойствием затаилась реальная угроза."
    sotp_narrator "Да. Если ты уже запрыгнул на эту карусель, то слезть с неё вряд ли удастся."
    sotp_protagonist "Так точно!"
    sotp_od "Вот и славно. Напоминаю: будь готов в четверг ехать в область. Скорее всего придётся остаться там на пару суток. Эта оторва, чтоб её, едет с тобой. Всё ясно?"
    sotp_narrator "ОД и Лис друг друга недолюбливают, но работа есть работа."
    sotp_protagonist "Так точно!"
    sotp_od "Свободен."
    sotp_narrator "ОД курирует мою с Лис «ночную работу». {w}Вернее сказать, он просто в один момент подловил меня на крючок, когда ему стало известно о получении мной взятки."
    sotp_narrator "Мы стараемся делать вид, что тут нет никакого принуждения. Пока получается неплохо, помимо подобных случаев с провалами или оплошностями. Тогда то он и дёргает крючок, намертво засевший в моей десне."
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_prosecutor_office
    show sotp_snow_layer3_anim
    show sotp_snow_layer2_anim
    show sotp_phone
    show sotp_snow_layer1_anim
    show sotp_snow_layer0_anim
    show sotp_static_noise_anim
    with Dissolve(2)
    play ambience sotp_winter_wind fadein 2
    sotp_narrator "Стоило мне только выйти из отделения, как назойливой мухой зазвонил телефон."
    sotp_sister "Алло?"
    sotp_protagonist "Привет, сестрёнка!"
    sotp_sister "Привет. Смотри, сегодня вечером я уезжаю. Не будет меня где-то несколько дней."
    sotp_sister "Пожалуйста, не забывай иногда заглядывать ко мне, а то цветы завянут. Ключи у тебя есть."
    sotp_narrator "По всей квартире у неё навалом комнатных растений, которые она любит чуть меньше, чем меня, и за которыми нужен постоянный уход."
    sotp_protagonist "Без проблем. Может, мне заехать и помочь с вещами?"
    sotp_sister "Не утруждайся. Я вполне смогу спуститься на лифте с парой сумок и донести их до машины. Но за заботу спасибо."
    sotp_protagonist "Хорошо. Тогда на связи. Приятной поездки в отчий дом."
    sotp_sister "Спасибо. Передавай Яне привет!"
    sotp_protagonist "Обязательно. Пока."
    sotp_sister "Пока!"
    hide sotp_phone with dissolve
    sotp_narrator "Я сбросил звонок и побрёл уже было домой."
    sotp_fox "Эй, дорогуша!"
    show sotp_lis behind sotp_snow_layer1_anim with dissolve
    sotp_narrator "Ну конечно. Я обернулся и помахал ей рукой."
    sotp_fox "Ты как после вчерашнего?"
    sotp_protagonist "Сносно. Меня сегодня ОД вызывал."
    sotp_narrator "Лис удивлённо вскинула брови."
    sotp_fox "Вызвал? По поводу?"
    sotp_protagonist "Напомнил про следующее дело. Недвусмысленно намекнув, что в случае провала всё будет очень плохо."
    sotp_fox "Заса-ада. Если он счёл нужным напомнить, то у нас и впрямь всё серьёзно."
    sotp_narrator "Она на мгновение о чём-то задумалась."
    sotp_fox "Хотя, хрен с ним. Не стоит сейчас над этим запариваться."
    sotp_fox "Пошли лучше поедим где-нибудь, сходим в какой-нибудь ресторан. Давно я с Янкой не виделась. Прячешь её от меня?"
    sotp_protagonist "Хорошая мысль. Сейчас позвоню ей. Только в этот раз без спиртного."
    sotp_fox "Обижаешь!"
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_int_abandoned_workshop
    show sotp_int_hanged_man
    show sotp_lis
    show sotp_static_noise_anim
    with Dissolve(2)
    play music sotp_death fadein 2
    sotp_narrator "Неожиданный вызов. Пришлось ехать сюда прямо из ресторана."
    sotp_narrator "Яна всё понимает, но оставлять её там одну всё же было очень неприятно."
    sotp_narrator "Заброшенный цех в промзоне. {w}Труп. {w}Висельник. {w}Обстоятельства необычные."
    sotp_fox "Висящее тело обнаружили местные бездомные."
    sotp_fox "Предположительно смерть наступила от удушья около восьми часов назад."
    sotp_fox "Срочник. Ушёл в самоволку. По месту службы характеризуется как нежелающий служить, совершал немало дисциплинарных нарушений."
    sotp_narrator "Монотонным, как снежный пейзаж голосом вводила она меня в курс дела."
    sotp_protagonist "Почему этим занимается не военная прокуратура?"
    sotp_fox "Уже занимается, но из-за того, что это случилось за пределами воинской части, припаяли и нас."
    sotp_protagonist "Что-нибудь интересное уже узнали?"
    sotp_fox "Первичный телесный осмотр показал наличие у него множества гематом, несколько следов от прижигания кожи сигаретой, свежие ссадины на коленях."
    sotp_protagonist "Ого! Я думал, что такие зверства в казармах остались в девяностых."
    sotp_narrator "Лис поджала губы и неопределённо повела плечами."
    sotp_fox "Воинская часть, в которой он проходил службу, имеет довольно плохую репутацию."
    sotp_protagonist "А что нам тогда сейчас делать?"
    sotp_fox "Ну, подождём пока подъедут из военной прокуратуры. А дальше они уже заберут это дело себе с концами."
    sotp_protagonist "Понятно."
    sotp_fox "Как думаешь, спишут на простое самоубийство или всё же начнут разбираться в истинных причинах такого действия?"
    sotp_protagonist "Если дело попадёт к Самойленко, знакомый тип, учились на одном потоке, то спишут на суицид из-за неразделённой любви или какую-нибудь другую дребедень."
    sotp_protagonist "Найдут записку, мол так и так, ухожу сам, никого не вините. {w}Почерковедческую экспертизу никто проводить не станет."
    sotp_protagonist "Самойленко такие дела щёлкает как орешки."
    sotp_fox "Ну, это уже не наша забота."
    sotp_narrator "Возможно, раньше при виде подобной картины у меня бы защемило в груди."
    sotp_narrator "Молодой парень не вынес постоянных истязаний и избиений от одуревших от безнаказанности «дедов», которым всё это скорее всего сойдёт с рук, ибо шумиха не нужна никому."
    sotp_narrator "Какие чувства это должно вызвать? Злобу от собственного бессилия и несправедливости нашего мира?"
    sotp_narrator "Право, я повидал за свой короткий срок службы уже столько невинно загубленных жизней, что очерствел абсолютно."
    sotp_narrator "Единственные чувства, что это дело у меня вызывает - обида за то, что нам пришлось сорваться из ресторана."
    sotp_protagonist "Когда они уже приедут?"
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_int_float
    show sotp_yana
    show sotp_static_noise_anim
    with Dissolve(2)
    play ambience ambience_medstation_inside_night fadein 2
    sotp_yana "Да ладно тебе! Всё в порядке! Всё равно здорово посидели! Была рада увидеться с Лис!"
    sotp_yana "Я даже не знала, что у вас столько интересных историй с работы припасено. Почему ты мне раньше всё это не рассказывал?"
    sotp_narrator "Яна всё же дождалась меня и мы вместе вернулись домой."
    sotp_protagonist "Просто у Лис язык без костей. Не люблю я особо трепаться про работу, ты же знаешь."
    sotp_narrator "Яна встрепенулась и подскочила ко мне."
    sotp_yana "Эй, ты опять ходишь с таким лицом, что аж смотреть противно!"
    sotp_protagonist "Очередной завал на работе. Эти ночные смены меня доконают."
    sotp_yana "Эй, перестань! Ну же, давай улыбнись! Улыбнись, дурак!"
    sotp_narrator "Я уже говорил, что она в любой ситуации может заставить меня улыбнуться?"
    sotp_protagonist "Нельзя же человека за то, что он устал, называть дураком!"
    sotp_yana "{b}МНЕ{/b} можно! Люблю тебя, дурак."
    sotp_narrator "Она подошла ещё ближе. Наши лица совсем рядом."
    sotp_protagonist "Господи, ты неисправима. {w}За это я тебя и люблю."
    sotp_yana "Неужели только за это?"
    sotp_narrator "Она подмигнула и в то же мгновение поцеловала меня."
    sotp_narrator "Раздалась звучная мелодия."
    sotp_narrator "Как же не вовремя!"
    sotp_narrator "Как бы я не пытался игнорировать телефон, он назойливо, словно пьяный сосед, продолжает трезвонить."
    show sotp_phone behind sotp_static_noise_anim with dissolve
    sotp_narrator "Я отстраняюсь от Яны и отвечаю на звонок, мельком глянув на экран. {w}Незнакомый номер."
    play music sotp_socialism fadein 2
    sotp_protagonist "Алло?"
    sotp_narrator "Тяжёлый вздох и натужный мужской голос:"
    sotp_phone "Вы приходитесь родственником..."
    sotp_yana "Что-то случилось?"
    sotp_narrator "Наверное, она сразу же заметила изменения на моём лице, но я не отвечаю ей, продолжая слушать голос из телефона."
    sotp_protagonist "Да, я её брат. Кто вы?"
    sotp_phone "Ваша сестра попала в аварию. Состояние крайне тяжёлое. Ее увезли в больницу номер двадцать три. Вы сможете приехать?"
    sotp_protagonist "Да. Сейчас приеду."
    hide sotp_phone with dissolve
    sotp_narrator "С окончанием разговора, внутри всё оборвалось. Сейчас же в машину и гнать в больницу. Хоть бы она выкарабкалась."
    sotp_yana "Посмотри на меня! Ты весь красный! Что случилось?"
    sotp_protagonist "Сестра в больнице. Говорят, состояние тяжёлое. {w}Нужно ехать. {w}Прямо сейчас."
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ save_name = ("Три смерти.\nАКТ 3. Так я и умер.")
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("Три смерти. АКТ 3. Так я и умер.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    scene bg sotp_ext_winter_street
    show sotp_snow_layer3_anim
    show sotp_snow_layer2_anim
    show sotp_yana
    show sotp_snow_layer1_anim
    show sotp_snow_layer0_anim
    show sotp_static_noise_anim
    with Dissolve(2)
    play music sotp_bensound_november fadein 2
    play ambience sotp_winter_wind fadein 2
    sotp_yana "Ты же говорил, что бросишь."
    sotp_narrator "Я делаю долгую затяжку и медленно выпускаю сигаретный дым прежде чем ответить." 
    sotp_narrator "Кофе и сигареты помогают держаться на ногах. Бессонница одолевает меня всё больше."
    sotp_protagonist "Я бросал. Но после той аварии снова начал."
    sotp_narrator "Яна выглядит очень расстроенной. После той ночи она стала реже улыбаться."
    sotp_yana "Извини. Мне очень жаль твою сестру. Не хотела об этом напоминать."
    sotp_protagonist "Эй! Ничего страшного. Не стоит сильно расстраиваться."
    sotp_narrator "Пытаюсь её подбодрить. Нельзя, чтобы мой последний лучик света становился таким же тусклым и бесцветным, как я."
    sotp_protagonist "Я понимаю, что такое... {w}такое порой случается. И с этим просто нужно смириться."
    sotp_narrator "Отец преподал мне хороший последний урок. {w}Покойникам плевать на твои слёзы."
    sotp_narrator "Ты же на самом деле жалеешь не умершего, а себя, потому что в твоей жизни больше нет этого человека. {w}Излишний эгоизм."
    sotp_narrator "На похоронах мы встретились с мамой. Мы не проронили ни слова. Она постарела."
    sotp_narrator "Но меня не отпускает только одна мысль. Что сестра оставила после себя?" 
    sotp_narrator "Жилплощадь?"
    sotp_narrator "Горечь в нашей памяти?" 
    sotp_narrator "Всё это эфемерно и бессмысленно. Время быстро сотрёт память о ней со страниц этой жизни." 
    sotp_narrator "Наверное, это и будет настоящая смерть. {b}Забвение.{/b}"
    sotp_narrator "{i}А что будет после меня?{/i}"
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_form
    show sotp_static_noise_anim
    with Dissolve(2)
    play music sotp_defeated_clown fadein 2
    sotp_narrator "Спустя пару дней у меня всё же дошли руки разобрать вещи сестры."
    sotp_yana "Это пионерская форма твоей сестры?"
    sotp_narrator "Внимание Яны привлекла коробка, в которой сестра хранила атрибуты своего советского детства."
    sotp_protagonist "Да. Она часто мне рассказывала о том пионерлагере. «Совёнок». {w}Я то сам в детских лагерях никогда и не бывал, а пионером уж подавно не был."
    sotp_yana "И много она тебе рассказала?"
    sotp_protagonist "Да-а. Я себе этот лагерь по её рассказам столько раз представлял. Во всех подробностях."
    sotp_narrator "В моих фантазиях этот лагерь был лучшим местом на земле, где все к тебе добры и заботливы, где чувство общности наполняет тебя дополна."
    sotp_protagonist "Мечтал когда-нибудь попасть в него. {w}Эх, детские грёзы. {w}Не хочу, чтобы после её смерти эти вещи пылились в каком-то чулане."
    sotp_yana "А меня бы с собой взял?"
    sotp_protagonist "Куда?"
    sotp_narrator "Я не сразу понял вопрос."
    sotp_yana "В «Совёнок»!"
    sotp_narrator "Она всплеснула руками, полная энтузиазма. Яна всегда была любительницей помечтать."
    sotp_protagonist "Взял бы конечно! Это были бы прекрасные воспоминания! {i}Воспоминания на всю жизнь!{/i}"
    sotp_narrator "Я вдруг снова по-детски наивно представил себе эту картину в мельчайших деталях."
    sotp_narrator "Яна, Я, Сестра, да и Лис тоже в придачу." 
    sotp_narrator "Мы навсегда молоды и полны жизни, а окружает нас оживший наяву чудесный пионерлагерь из моих детский фантазий."
    sotp_narrator "Наверное, так и выглядел бы мой рай."
    sotp_yana "Вот и здорово! Надеюсь, у тебя когда-нибудь получится отыскать свой «Совёнок»! А я... Я всегда смогу найти к тебе дорогу!"
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_roof
    show sotp_snow_layer3_anim
    show sotp_snow_layer2_anim
    show sotp_snow_layer1_anim
    show sotp_snow_layer0_anim
    show sotp_static_noise_anim
    with Dissolve(2)
    play ambience sotp_winter_wind fadein 2
    play music sotp_bensound_tomorrow fadein 2
    sotp_narrator "Этой ночью мне всё же удалось заснуть, но я быстро проснулся из-за какого-то кошмарного сна. Не могу ничего вспомнить."
    sotp_narrator "Я поднялся на крышу. {w}Прекрасное место, чтобы побыть наедине с городом."
    sotp_narrator "Морозная ночь, тишина и покой. Только ветер тихо и невнятно бормочет."
    sotp_narrator "Я закурил."
    show sotp_phone behind sotp_snow_layer1_anim with dissolve
    sotp_narrator "Спустя какое-то время зазвонил телефон. Лис."
    sotp_protagonist "Привет."
    sotp_fox "Привет, извини, что не позвонила раньше. У тебя снова зимняя бессонница, да?.."
    sotp_fox "После того, как ты уехал на несколько дней, ОД завалил меня работой за двоих."
    sotp_fox "Я слышала, что случилось с твоей сестрой. Мне жаль. Как ты там, дорогуша?"
    sotp_protagonist "Всё в норме. Не переживай. Ты готова к завтрашнему отъезду?"
    sotp_narrator "Лис медлила с ответом."
    sotp_fox "Ты уверен, что хочешь поехать?"
    sotp_protagonist "У меня нет выбора. Как и у тебя."
    sotp_fox "Да, ты прав. Ладно. Тогда увидимся завтра."
    sotp_protagonist "Пока."
    hide sotp_phone with dissolve
    sotp_narrator "Я докурил третью сигарету и щелчком пальцев отправил тлеющий бычок за пределы крыши."
    sotp_narrator "Сзади послышались шаги, поднимающиеся по скрипучей деревянной лестнице."
    show sotp_yana behind sotp_snow_layer1_anim with dissolve
    sotp_yana "Так и знала, что найду тебя здесь!"
    sotp_protagonist "Неужели я настолько предсказуем?"
    sotp_yana "Нет. Конечно нет. Просто ты мне сам как-то рассказывал, что тебе здесь нравится из-за..."
    sotp_protagonist "Из-за того, что тут очень спокойно."
    sotp_yana "И очень холодно."
    sotp_narrator "Она хихикнула и поёжилась."
    sotp_yana "Значит, завтра ты всё-таки уезжаешь?"
    sotp_protagonist "Да..."
    sotp_protagonist "Завтра я уезжаю."
    sotp_yana "Я буду ждать. Только не забывай о том, что я тебе говорила."
    sotp_protagonist "Я всегда найду к тебе дорогу?"
    sotp_narrator "Быстро вспомнил я её фразу, когда речь зашла о «Совёнке»."
    sotp_yana "Именно! Ты у меня такой внимательный к мелочам!"
    sotp_protagonist "Издержки профессии."
    sotp_narrator "Пожал я плечами."
    sotp_yana "Ладно. Пошли спать, а то ещё заболеешь!"
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_int_float_dream_catcher
    show sotp_static_noise_anim
    with Dissolve(2)
    play ambience ambience_medstation_inside_night fadein 2
    sotp_protagonist "Ты серьёзно думаешь, что эта безделушка мне поможет?"
    sotp_narrator "Я держал в руке подаренный Яной перед отъездом ловец снов. Она сказала, что эта вещица может избавить меня от кошмаров."
    sotp_yana "Ох, как же я не люблю, когда в твоём голосе слышны нотки скепти-чтоб-его-цизма."
    sotp_narrator "Она скривилась, словно только что проглотила лимон."
    sotp_protagonist "Извини, я попробую. Весь на нервах из-за этой поездки и кошмаров. Так хочется всё отменить, из..."
    sotp_narrator "Она остановила меня, приложив палец к губам."
    sotp_yana "Твои глаза извиняются лучше. {w}Но на самом деле, мне и правда не нравится эта твоя работа. {w}Странная она какая-то."
    sotp_narrator "На её лице отразились тени сомнений."
    sotp_yana "С тобой точно всё будет в порядке?"
    sotp_narrator "Лис в нетерпении начала жать на гудок автомобиля, недвусмысленно намекая, что мне пора заканчивать прощанье."
    sotp_narrator "Ладно. Всё равно мы расстаёмся всего на пару дней."
    sotp_protagonist "Да, точно. Спасибо за ловец снов. Люблю тебя!"
    sotp_yana "И я люблю тебя, дурак."
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_lane
    show sotp_lis
    show sotp_static_noise_anim
    with Dissolve(2)
    play ambience ambience_cold_wind_loop fadein 2
    play music sotp_hoyts_office fadein 2
    sotp_narrator "Сегодня последний день."
    sotp_narrator "Уже завтра я поеду к Яне, но какое-то у меня плохое предчувствие. {w}Она весь день не берёт трубку."
    sotp_narrator "Тёмные переулки, руки в карманах, ладонь поглаживает холодную рукоять ПМа. Первый лёд хрустит под ногами. Луна за тучами спряталась, не показывается."
    sotp_protagonist "Лис, наш выход только после того, как клиент клюнет. Не раньше."
    sotp_narrator "Наша задача: проследить за «прикормышем» и обеспечить прикрытие в случае форс-мажора."
    sotp_narrator "Прикормыш - жертвоприношение от крупной сети производителей синтетики."
    sotp_narrator "Они сливают нам новые рецептуры, конкурентов и своих мелких, ненужных лакеев, а мы их не трогаем. Такая вот договорённость."
    sotp_narrator "В этот раз мы загребаем одного из партнёров. Чем-то он видать провинился."
    sotp_fox "Да поняла я. Не учи учёного."
    sotp_fox "Чего ты вообще подписался на эту встречу?"
    sotp_protagonist "ОД приписал. Сказал, что буду отрабатывать упущенный товар."
    sotp_fox "Ну ты даёшь."
    sotp_fox "Какого ты вообще попёрся туда? Это же не наш уровень, а ФСКН."
    sotp_protagonist "Так получилось."
    sotp_narrator "Я остановился у поворота и жестом показал своей напарнице замереть."
    sotp_fox "Как тебя твоя отпустила? Не прознала ещё про твои тёмные делишки?"
    sotp_protagonist "Нет, не прознала. А у тебя как дела с..."
    sotp_fox "А это уже не твоё дело, дорогуша. Следи лучше за точкой."
    sotp_narrator "Она не любит говорить о своей личной жизни. Правда, она у неё настолько бурная, что и не уследишь."
    sotp_protagonist "Вот бы быстрее всё это закончить."
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    $ sotp_set_mode_nvl()
    scene bg sotp_prolog_bw
    show sotp_static_noise_anim
    with Dissolve(2)
    sotp_narrator "Дальше пустота. Всё как в тумане. Яна не брала трубку не просто так."
    sotp_doctor "Примите мои соболезнования. Мы сделали всё, что смогли, но она скончалась, не выйдя из комы.\n"
    sotp_narrator "Не придумали тех слов, что могут описать это щемящее чувство в груди. Словно само сердце стало полым."
    sotp_protagonist "Когда я смогу забрать тело?\n"
    sotp_doctor "Но... Вам не нужно время, чтобы....\n"
    sotp_protagonist "Она умерла. С этим просто нужно смириться. Когда я смогу забрать тело?\n"
    sotp_narrator "Очередная авария. Они происходят постоянно. Пьяный водитель, плохая погода, ошибка, случайность."
    sotp_narrator "Но почему?"
    sotp_narrator "Почему они?"
    $ sotp_show_centered_text("К чёрту всё.")
    $ sotp_show_centered_text("К чёрту.")
    $ sotp_show_centered_text("Мне нужно выпить.")
    $ sotp_hide_centered_text(dspr)
    stop music fadeout 3
    scene bg black with Dissolve(3)
    $ renpy.pause(3, hard = True)
    $ sotp_set_mode_adv()
    scene bg sotp_int_protagonist_room_zoomed:
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

    $ sotp_heartbeat_animation("bg sotp_int_protagonist_room_zoomed", 1.05, 1.0)
    show sotp_static_noise_anim
    with Dissolve(1)
    play music sotp_death_friend_1st_december fadein 2
    sotp_protagonist "Привет, пап, давно мы с тобой не общались."
    sotp_narrator "Я изрядно пьян. Способность здраво мыслить маячит где-то на периферии."
    sotp_narrator "Телефон опять разрывается. ОД, Лис, ОД, Лис. Я его выключаю."
    sotp_protagonist "Молчишь? Ты всегда молчал, когда я приезжал к вам после поступления на службу."
    sotp_protagonist "Ты же не хотел, чтобы я шёл в ментовку."
    sotp_protagonist "Я ведь сразу и не пошёл."
    sotp_protagonist "А потом оно само как-то, понимаешь?"
    sotp_narrator "Я делаю очередной глоток. {w}Горло дерёт. {w}В глазах плывёт."
    sotp_protagonist "Я ведь с самого детства тобой восхищался. Мой отец - милиционер! Прям как дядя Стёпа!"
    sotp_protagonist "Я ведь не знал тогда, что это за мясорубка. {w}Не знал, что тебе приходилось видеть."
    sotp_protagonist "В моих глазах ты всегда был сделан из бетона, из стали."
    sotp_protagonist "Честный, неподкупный, справедливый. Да ты таким и был ведь. Правдарубом."
    sotp_protagonist "Тебя никто на работе не любил. Везде ты как в бочке затычка."
    sotp_protagonist "Я и поверил, что так же можно, что я тоже из стали. А я слабее оказался."
    sotp_protagonist "Хребет не уберёг и что теперь? {w}Пока меня за ниточки то туда, то сюда, мои близкие умирали. {w}Зато при бабле."
    sotp_protagonist "Знаешь, сколько мне ОД в конверте сунул? Дохера!"
    sotp_protagonist "Но разве стоит этот кулёк жизни Яны? {w}Я же мог остаться с ней и ничего бы не случилось!"
    sotp_narrator "Я сам не заметил, как сжал в руке ловец снов подаренный Яной."
    sotp_narrator "Ещё один глоток. Горько."
    sotp_protagonist "Прости, пап."
    sotp_protagonist "Перед матерью извиниться не смог. Просто не было сил взять телефон и позвонить."
    sotp_protagonist "Я не справился. {w}Нечего мне тут больше оставаться."
    sotp_protagonist "Пора к вам. К тебе, к Яне, к сестре."
    sotp_narrator "Дуло служебного Макарова смотрело в мою сторону. Холодом веяло из этой трубки. Загробным холодом."
    sotp_narrator "Я в последний раз взглянул на ловец снов. Хочу заплакать, но не могу."
    $ sotp_show_centered_text("Чёрт с ним.")
    play sound sotp_handgun
    scene bg black
    stop music
    $ renpy.pause(5, hard = True)
    play sound sotp_heart_monitor
    $ renpy.pause(5, hard = True)
    sotp_fox "Какие у него шансы выйти из комы, Иван Степанович?"
    sotp_doctor "Огнестрельное в голову - это не шутки. Удивительно, что он вообще смог выжить."
    sotp_fox "Зачем ты так?"
    sotp_doctor "Ладно, милочка, вашему другу нужен покой. Пойдемте."
    $ renpy.pause(3, hard = True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "winter_day"
    scene bg sotp_ext_road_winter_day with sotp_flash
    play ambience sotp_winter_wind fadein 2
    play music sotp_nightwish_nemo_piano_cover fadein 2
    sotp_narrator "Ну вот я и приехал в пионерлагерь «Совёнок»."
    scene bg sotp_ext_camp_entrance_winter_day with dissolve
    sotp_narrator "Из-за небольших проволочек с документами я задержался и приехал на день позже, но ничего страшного в этом нет, ведь впереди меня ждут целых три недели отдыха!"
    show sotp_us smile with dissolve
    sotp_narrator "Из-за ворот вдруг выглянула девочка, она подошла поближе и улыбнулась."
    sotp_narrator "Очень симпатичная, кстати. Огненные, как цветок мака волосы, и голубые глаза, в которых, казалось, можно утонуть. Она невысокого роста, на вид ей лет шестнадцать. "
    sotp_usp "Привет, ты, наверное, только что приехал?"
    sotp_protagonist "Да. Только что."
    $ sotp_set_main_menu_cursor()
    return

label sotp_shadows:
    stop music fadeout 3
    scene bg black with Dissolve(3)
    $ save_name = ("Тени.\nАКТ 1. Авторитет.")
    $ renpy.block_rollback()
    $ sotp_onload("lock")
    $ persistent.timeofday = "bw"
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("Тени. АКТ 1. Авторитет.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("18 декабря 1999 года.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("Допрос обвиняемого по статье 105.1 УК РФ.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    scene bg sotp_int_tish_interrogation
    show sotp_static_noise_anim
    with Dissolve(2)
    $ sotp_onload("unlock")
    $ sotp_set_timeofday_cursor_var = True
    play music sotp_master_of_spirits_it_was_me fadein 2
    sotp_narrator "Следователь, Сказаев Павел Иванович, коренастый мужчина тридцати трёх лет, красный, как рак, смиренно опустив голову, сидел на косом табурете подле двери."
    sotp_narrator "Следователь был невысок, но внешне довольно привлекателен. О таких говорят: косая сажень в плечах."
    sotp_narrator "Глаза его были глубоко посажены, а взгляд выражал раздражение и усталость."
    sotp_narrator "Третий раз всё повторяется, словно по нотам. Ему хотелось послать всё к чёрту и бросить дело, но Рубикон уже перейдён."
    sotp_narrator "Глубоко вздохнув, Сказаев вынул из пальто портсигар и закурил."
    sotp_skaz "Антон Степанович, успокойтесь. {w}Поймите, правдивые показания не ухудшат ваше положение. Сотрудничество со следствием только смягчит вашу уголовную ответственность."
    sotp_skaz "Можете рассказать, как всё было на самом деле?"
    sotp_narrator "По комнате распространился запах табака, испускаемый крепко зажатой между пальцами сигаретой. Глаза следователя слипались от усталости. Сегодняшний день полностью его измотал."
    sotp_tish "Просто я удивлён, что меня задержали. Никак не возьму в толк, что я мог такого натворить. Можно сигаретку, товарищ следователь?"
    sotp_narrator "Спросил Тишкевич Антон Степанович. Сгорбленный, полноватый мужичок среднего возраста в сложившейся ситуации был бледен, рассеян и уныл."
    sotp_narrator "Павел Иванович молча передал через стол портсигар. Дрожащими руками Тишкевич попытался прикурить с помощью зажигалки, найденной рядом с сигаретами."
    sotp_narrator "Получилось только на третий раз. Хоть он и пытался не подавать виду, но нервы уже были на пределе."
    sotp_tish "Хорошие у вас сигареты, хорошие. Импортные?"
    sotp_skaz "Они самые, не люблю наши. Горчат."
    sotp_tish "Понимаю, понимаю. Дорогие небось, но цену свою явно с лихвой отбивают, а я вот только наши и курю, а что ещё делать?"
    sotp_tish "Денег-то нынче на другие не хватает, ой как не хватает, товарищ Сказаев. Мне жена уже всю плешь проела. Всё, мол, брось, да брось. Черт бы эту бабу побрал! Я с пятнадцати лет курю, а с ней всего двадцать живу!"
    sotp_narrator "Тишкевич шмыгнул длинным носом, отбросил бычок от быстро скуренной сигареты в сторону и сплюнул на бетонный пол."
    sotp_narrator "Подобное проявление моветона подействовало на Сказаева ободряюще. Выпрямившись, он уверенно, можно сказать, по-хозяйски посмотрел на допрашиваемого, показывая, кто здесь главный."
    sotp_skaz "Можете сказать, почему вы здесь?"
    sotp_tish "Скрутили посреди улицы ни с того, ни с сего и приволокли сюда, ироды! Скоро уже отпустите? Мне к Зинке бы, а то она ж..."
    sotp_narrator "Антон попытался приплести жену, хотя эта самая Зинка, наоборот, была бы только рада его дальнейшему отсутствию."
    sotp_narrator "Он бы продолжил, но споткнулся о взгляд следователя и сразу затих, сгорбившись ещё сильнее, из-за чего в полумраке стал напоминать горбуна из романа Гюго."
    sotp_skaz "Понятно. Вы часто выпиваете?"
    sotp_tish "Ну, а что? Бывает. Бывает, выпиваю... Иногда."
    sotp_narrator "Допрашиваемый потер вспотевшие ладони о штанины. Милиционер же уныло покачал тяжелой головой."
    sotp_skaz "У вас ранее были проблемы с памятью вследствие алкогольного опьянения?"
    sotp_tish "Ну что вы? Конечно же..."
    sotp_skaz "Вы выпивали в ночь на одиннадцатое декабря?"
    sotp_narrator "Следователь словно не обращал внимание на те показания, что давал ему обвиняемый, а спрашивал лишь для того, чтобы спросить."
    sotp_narrator "Выбитый из колеи таким грубым вмешательством, Тишкевич смотрел на своего мучителя тёмными глазами, полными недоумения и недовольства."
    sotp_narrator "Он очень не любил, когда его перебивают."
    sotp_narrator "Тусклая лампочка на мгновение погасла, погрузив крошечную серую комнатушку во мрак. Сказаев неразборчиво выругался себе под нос."
    sotp_skaz "Ну, так? Вы пили одиннадцатого декабря?"
    sotp_tish "Это же вчера было? Вчера-то, если память не изменяет, дома сидел, телевизор глядел, суббота же... А-а, ещё в магазин ходил, за хлебом, ну и чекушку прихватил." 
    sotp_tish "Для аппетита, так сказать. Грех же под борщец домашний не хряпнуть, сто грамм всего-то, прости господи!"
    sotp_narrator "Следователь поскрёб ногтями левую, поросшую трёхдневной щетиной, щеку. В свете единственной лампы ранние морщины на его лице вырисовывались четче."
    sotp_narrator "Рука потянулась ко внутреннему карману пальто. Но портсигара там не было. Он жестом попросил вернуть сигареты, но сразу же убрал их, вспомнив, что решил бросить."
    sotp_narrator "Раскрыв потрепанную синюю папку и достав оттуда бумаги, Павел Иванович сказал мужчине напротив:"
    sotp_skaz "Взгляните, пожалуйста, на эти фотографии."
    sotp_tish "Ужас какой! Кто ж её так? А я тут причём? Никого не видел, ничего не слышал, Богом клянусь! Вчера только в магазин и сразу назад, в хату!"
    sotp_narrator "Антон Степанович поспешил отодвинуть бумаги в сторону. Ему было тошно."
    sotp_narrator "Снова хотелось курить, но попросить прямо сейчас было неловко. Следователь сжал кулаки и начал глубоко дышать. {w}Вот-вот он сорвется."
    sotp_skaz "На фотографиях Зинаида Николаевна,{w} твоя жена..."
    sotp_skaz "Тишкевич, чтоб тебя, это уже третий допрос! Прекрати валять дурака. {w}Ты хоть понимаешь, что если продолжишь нести бред - точно отправишься на нары по сто пятой?"
    sotp_skaz "Выкладывай, что было неделю назад, одиннадцатого декабря!"
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ save_name = ("Тени.\nАКТ 2. Чудо.")
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("Тени. АКТ 2. Чудо.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("{font=[sotp_laptev]}И снова я записываю дело в блокнот. Ничего не могу с собой поделать.\nКоллеги уже за глаза Сказочником называют, как будто это что-то плохое.{/font}")
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("29 декабря 1999 года.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("Сказаев Павел Иванович.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_set_mode_nvl()
    scene bg sotp_int_alcotable
    show sotp_static_noise_anim
    with Dissolve(2)
    play music sotp_master_of_spirits_awareness fadein 2
    sotp_narrator "Гражданина Тишкевича можно причислить к тем, кто в силу своей несознательности кубарем скатывался по социальной лестнице."
    sotp_narrator "Выросший в глубоко верующей семье, молодой парень с отличием закончил институт и, покинув любящих родителей, постепенно начал забывать закон Божий, всё больше и больше окунаясь в омут работы."
    sotp_narrator "Где-то вдали маячила туманная перспектива, заманивая всё дальше в свободное плавание, словно сирена."
    sotp_narrator "После разъединения пролетариев всех стран настали тяжёлые времена для государства в целом и для Антона Степановича в частности."
    sotp_narrator "Мужчина пристрастился к дешёвому алкоголю, время от времени мог отвесить жене за своенравие, а порой даже и просто так. Жаловался на жизнь своим собутыльникам, таким же неудачникам, как он."
    nvl clear
    sotp_narrator "И вот, на дворе уже девяносто третий год: колоссальная безработица, практически поголовное пьянство и резкий скачок преступности."
    sotp_narrator "Тридцатипятилетнему Антону «вежливо» предлагают уйти с должности главного инженера цеха и занять пост обычного рабочего, с которого тот начинал одиннадцать лет назад."
    sotp_narrator "Зарплата там и в лучшие времена, мягко говоря, была не самой высокой, а сейчас и подавно: этих грошей едва хватало на хлеб, сигареты и сомнительного вида алкоголь, к которому Тишкевич начал питать особую слабость."
    sotp_narrator "Так некогда перспективный инженер и любящий муж стал частью серой рабочей массы без амбиций, одним из тех, кто заливает своё горе огненной водой."
    sotp_narrator "Его бывшее рабочее место занял племянник нового главы завода, и теперь Антон чуть ли не мыл полы в некогда своем кабинете."
    nvl clear
    sotp_narrator "Его даже посещали мысли подстроить несчастный случай, чтобы получить инвалидность, но не смог, струсил и так не вовремя вспомнил про Божьи законы." 
    sotp_narrator "Григорию, его бывшему коллеге по цеху, в каком-то смысле повезло больше: однажды он полез проверять списанный станок и лишился ведущей руки почти по самый локоть."
    sotp_narrator "Дали вторую группу инвалидности. {w}Антон потом ещё пару раз видел его, идущего вразвалочку явно нетрезвой походкой с блаженной улыбкой на лице и бутылкой в целой руке."
    sotp_narrator "Работать не нужно: пенсию по инвалидности платят. А что руки нет, так это не страшно, вторая-то осталась при нём." 
    sotp_narrator "Правда, по итогу на одной из пьянок тот Гриша получил заточку под ребро из-за какого-то «крокодила»."
    nvl clear
    sotp_narrator "И вот, спустя года, после очередной попойки и настиг Антона Степановича алкогольный делирий, в народе прозванный белой горячкой или белочкой, тут уж кому как удобнее."
    sotp_narrator "Проявляется это неприятное состояние бредом. Да таким, что начинаешь видеть и слышать то, чего никогда не было и быть не может." 
    sotp_narrator "А самое забавное в том, что хрен разберешь, где заканчивается явь и начинаются «мультики»."
    sotp_narrator "Каждый свое видит. К одному черти приходят, к другой инопланетные медузы-насильники (я не шучу. Были уже подобные прецеденты)."
    sotp_narrator "К нашему же пациенту тени пришли. Что за тени? Поди разбери. {w}Более внятно описать свои галлюцинации он не смог. Пытался, конечно, но бранные выражения приводить не буду."
    nvl clear
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_thermal_power_plant
    show sotp_static_noise_anim
    with Dissolve(2)
    play music sotp_master_of_spirits_the_last_word fadein 2
    sotp_narrator "В тот вечер Антон Тишкевич находился на кухне, выпивал. По его словам, всё произошло в одно мгновение."
    sotp_narrator "За окном залаяли собаки, он обернулся посмотреть, а когда перевел взгляд обратно в комнату, его уже окружили."
    sotp_narrator "Со всех сторон подступали чёрные, словно сама бездна, тени. Были ли это тени его почивших родственников или же черти, выглядящие совершенно не так, как описывала ему в детстве бабка, пришли по его душу, он понять не смог, хотя в конечном итоге склонился ко второму варианту."
    sotp_narrator "Где-то в глубинах подсознания просыпалось давно позабытое из-за беззаботной жизни алкоголика чувство первобытного страха. В комнате стало невыносимо жарко."
    sotp_narrator "Как потом выяснили, просто повысилась температура тела. Симптом, обычный для делирия, но не для Тишкевича в те мгновения."
    sotp_narrator "Для него это был жар адских котлов, готовых для приёма очередного грешника."
    nvl clear
    sotp_narrator "Тени тем временем бесновались по полной: гремели посудой, копались в помойном ведре и - самое ужасное - тащили еду из холодильника!"
    sotp_narrator "На виновника сего бала сатаны они внимания не обращали. Да и не нужно было, он вот-вот бы и сам дубу дал."
    sotp_narrator "А что? Вполне вероятный исход. {w}Мужик хоть и не старый, но алкогольный стаж более шести лет."
    sotp_narrator "В таком положении очень часто случается выброс гормонов, нарушается сердечный ритм и..."
    sotp_narrator "Всё, мотор встал. {w}Но наш оказался не так прост."
    sotp_narrator "Взяв себя в руки, он начал рассуждать (как ошибочно полагал) здраво. Раз его не заметили, значит, слепые эти тварюги."
    nvl clear
    sotp_narrator "Пока он приходил в себя, больше половины уже разошлись по дому и устраивают кавардак в других комнатах. Нужно бежать. Путь из кухни был свободен. Всего-то пару рывков и он выскочит в коридор."
    sotp_narrator "Там дверь на задвижке, единственная преграда на его пути к свободе из этого кромешного ада. Взяв большой кухонный нож в жирных разводах от консервов, которые использовались как закуска, мужчина аккуратно отодвинул табурет и вышел из-за стола."
    sotp_narrator "Помедлив секунду, чтобы посмотреть на реакцию теней, Тишкевич с облегчением выдохнул." 
    sotp_narrator "Ни одна из тварюг и носом не повела на его действия, если у них, конечно, вообще был нос."
    sotp_narrator "Тихой поступью мужчина начал двигаться к коридору, как вдруг со стороны спальни послышались тяжёлые шаркающие шаги, словно к нему направлялся великан."
    nvl clear
    sotp_narrator "Сердцебиение участилось, а руки обмякли. {w}Всё, конец? {w}Сейчас Антона схватят и утащат в преисподнюю? О, он совершенно не сомневался, что именно туда."
    sotp_narrator "Он отлично знал и помнил все свои грехи. Алчность, гнев, лень, зависть - а ведь это только смертные грехи."
    sotp_narrator "Именно сейчас, за много лет он решил покаяться, взмолить к господу короткой, сбивчивой и наполовину забытой молитвой перед своей кончиной, пока за стеной всё ближе и ближе раздавались протяжные шаги экзекутора."
    sotp_narrator "Неожиданно для себя Тишкевич ощутил прилив сил, тягу к жизни. Руки снова начали его слушаться. Покрепче сжав нож, он понял, что не умрёт сегодня."
    sotp_narrator "Словно отделяясь от темноты, на свет лампы выплыло нечто огромное, едва напоминающее своими очертаниями что-то человеческое. Остальные тени при его приближении будто в страхе пригибались и пятились назад."
    nvl clear
    sotp_narrator "Неужто сам Сатана пришёл по душу Антона Степановича?"
    sotp_narrator "Нет, фига им, а не его душа! {w}Крича «Отче наш», мужчина набросился на главного беса, с легкостью повалил на пол и начал бить его ножом, пока тот не обмяк."
    sotp_narrator "Тварь пыталась что-то хрипеть своим жутким, заунывным голосом и даже отмахиваться, но сила вместе с удачей была сегодня не на его стороне. {w}Неужели он, какой-то работяга-пьяница, смог победить самого Люцифера?"
    sotp_narrator "В этот момент к нему пришло озарение. Антон понял, что ещё не всё потеряно, Бог его не оставил! Больше никакого алкоголя. Он снова начнёт ходить в церковь каждое воскресенье и будет молиться!"
    sotp_narrator "А сейчас пора бежать. Отбросив своё божие орудие правосудия (то есть нож), Тишкевич рывком добрался до двери и покинул квартиру, трясясь от страха, но ликуя от победы над злом."
    sotp_narrator "Звучит как полнейшая чепуха и театр абсурда, но именно так и во всех подробностях Тишкевич описывал этот вечер на допросах. {w}Забавно."
    nvl clear
    sotp_narrator "Неужели Тишкевич и правда вообразил, что он эдакий Давид своего времени, поразивший ужасного врага во имя Божье, или он просто придумал это на ходу?"
    sotp_narrator "Спустя пару дней убийца бесов был обнаружен в пригородном посёлке, без документов, ничего не помнящий. Так бы, возможно, и закончилась эта странная, но всё же относительно безобидная история."
    sotp_narrator "Антона Степановича ждало бы просто длительное лечение от алкоголизма. Если бы не одно «но». {w}И этим «но» была Тишкевич Зинаида Петровна, гражданка тридцати восьми лет, жена Тишкевича Антона Степановича."
    nvl clear
    sotp_narrator "Зинаида Петровна проснулась поздно ночью из-за слишком громких звуков и возгласов мужа, доносившихся с кухни. Голова женщины гудела, глаза слипались. Не хватало ещё из-за Антона проспать утренний будильник."
    sotp_narrator "Сон у Зинаиды был крепкий и проспать будильник ей было проще простого, а пропускать завтра никак нельзя. Только вот на прошлой неделе брала отгул из-за очередной Антоновой пьянки и его отсыпания в отрезвителе."
    sotp_narrator "Бросила бы она этого алкаша. С превеликой радостью бы бросила! Да какая-то наследственная у неё связь с пьющими, если так можно выразиться."
    nvl clear
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    scene bg sotp_cammunal
    show sotp_static_noise_anim 
    with Dissolve(2)
    play music sotp_master_of_spirits_patience fadein 2
    sotp_narrator "Детство у девочки выдалось далеко не самым лёгким: дальнюю комнату в коммуналке ей приходилось делить с алкоголиком-отцом, таким же пропойцей дедом и забитой матерью."
    sotp_narrator "На тот момент Зинаида ничего не имела против матери — та обещала ей и дачку, и тачку, и собачку, — а вот мужчин в доме побаивалась."
    sotp_narrator "Дед с отцом имели обыкновение напиваться до беспамятства и «строить» родню за любое нелестное слово."
    sotp_narrator "Воспоминания о детстве были эфемерными и отдавали чем-то холодным, пустым, давящим: перед глазами всплывали ряды пустых бутылок с красными этикетками; опухшее, покрытое синяками лицо матери и сочувствующие глаза соседской девочки, протягивающей купленную ей на день рождения «гематогенку»."
    sotp_narrator "Но уже с колокольни юношеского максимализма всё это ей казалось незначительным, ведь прошлым живут только «лузеры»."
    nvl clear
    sotp_narrator "Едва прозвенел последний в её жизни школьный звонок, она с полупустым чемоданом отправилась в северную столицу необъятной."
    sotp_narrator "К тому моменту мать потеряла в её глазах всякий авторитет из-за малодушия и мягкотелости. Поэтому с переездом Зинаида вычеркнула бывшую семью из своей жизни полностью и навсегда."
    sotp_narrator "Грустное прошлое растворялось в море новых эмоций, лиц и мест, словно пар от работающей теплоэлектростанции в чистом небе."
    sotp_narrator "Только вот со временем столичные красавцы и красавицы стали обходить её стороной, с насмешкой называя синим чулком, ибо, несмотря на внешнюю красоту, по натуре своей Зинаида оставалась неисправимой провинциалкой."
    sotp_narrator "И вот уже ее настиг первый нервный срыв на фоне кажущегося всеобщим презрения."
    sotp_narrator "Затворничество, ночная зубрежка матчасти, одна за другой закрытые сессии, красный диплом — и предложение по программе «молодой специалист»."
    nvl clear
    sotp_narrator "Забыв про несбывшиеся Питерские мечты, девушка с огнём в глазах отправилась в небольшой, но быстро растущий городок, где следующие три года должна будет работать преподавателем начальных классов."
    sotp_narrator "По приезде на новое место она и встретила своё будущее: ещё зелёного, но уже достаточно перспективного, чтобы начать строить планы на будущую семейную жизнь, инженера Антона."
    sotp_narrator "Молодой, поджарый, притягивающий не только фигурой, но и умом — он казался ей удивительно родственной душой. Правда, итог этой истории мы уже знаем. {w}Не бывает у нас, как в сказке. {w}Ну не бывает..."
    nvl clear
    sotp_narrator "Не успела Зинаида Петровна зайти на кухню, как на неё набросился, повалив на пол, её же собственный муж."
    sotp_narrator "Больно ударившись головой о деревянное покрытие пола, женщина попыталась закричать и отмахнуться от обезумевшего Антона, но тот, крепко её придавив, смотрел сквозь неё пустым взглядом и не переставая что-то беззвучно бормотал."
    sotp_narrator "Лезвие недавно заточенного колбасного ножа легко вошло в плоть. Сначала оно казалось холодным, но, в конце концов, запылало."
    sotp_narrator "Все силы испарялись, когда кровь начала покидать тело. Весь окружающий мир завибрировал, сделался каким-то мутным и невнятным."
    sotp_narrator "Последующие удары практически не чувствовались, а затем глаза и вовсе окутала тёмная пелена."
    nvl clear
    sotp_narrator "Женщину нашла соседка-полуночница, которая буквально через пару минут после побега Антона Степановича, из-за громкого шума заглянув в открытую дверь, обнаружила практически мёртвое бессознательное тело."
    sotp_narrator "«Скорая» приехала быстро. Возвращалась с вызова буквально в паре кварталов от очередной сердобольной старушки, постоянно беспокоящей по поводу и без."
    sotp_narrator "К моменту приезда Зинаида уже побелела, дыхание стало слабым и прерывистым. Оперативно проверили всё, что нужно было проверить и повезли, зловеще сверкая мигалкой, в реанимацию."
    sotp_narrator "Не довезли. Скончалась по дороге. Так как дело было криминальное, тело покойной передали на судмедэкспертизу."
    nvl clear
    sotp_narrator "Секцию проводила Яночка, молоденькая и вполне привлекательная девушка, только-только прошедшая переквалификацию из патанатомии. {w}Несмотря на неопытность, причину смерти выявила быстро и верно."
    sotp_narrator "Один из ножевых ударов пробил грудную клетку, повредив перикард и ранив сердце. Отверстие в сердечной сумке было слишком большое и кровь обильно стекла в торакальную полость* (грудную полость)."
    sotp_narrator "Итог: смерть от кровопотери. Главный подозреваемый - пропавший муж."
    sotp_narrator "Тут уже началась наша, милицейская работа. Дело оказалось несложным, но довольно любопытным. Для порядка опросили соседей, провели обыск, сняли «пальчики» с ножа для опознания."
    sotp_narrator "Долго не хотели поднимать архив. Понять можно, всего лишь очередная жертва домашних распрей. Но все же по моему настоянию достали тонкую папку на мужа."
    nvl clear
    sotp_narrator "Ага. Тишкевич Антон Степанович, тысяча девятьсот пятьдесят восьмого года рождения. Числится в базе данных за мелкое воровство и хулиганство - административные нарушения."
    sotp_narrator "Судимостей нет. Ну вот. Пора начинать искать. Только вот не пришлось. Сам нашелся. Не поверите, но через пару дней пришёл в милицейский участок, ибо не мог понять, где находится."
    sotp_narrator "Там же его и повязали бдительные сотрудники, опознав по ориентировке."
    sotp_narrator "Всё отрицал, божился, что ничего не помнит. Путал события недельной давности, думая, что это было вчера. Потом вообще забывал, где находится и почему. Сложно с ним пришлось по итогу."
    nvl clear
    sotp_narrator "Ну, что можно сказать в заключение? Беда у нас нынче с алкоголизмом. Бутылку какой-то палёнки можно раздобыть практически на каждом углу, да и стоит она дешевле, чем та же книжка."
    sotp_narrator "Не знаю, станет ли лучше в следующем тысячелетии, но сильно на это надеюсь."
    sotp_narrator "Но всё же интересно, сколько ещё пройдет через мои руки уголовных дел из-за алкоголя?"
    stop music fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(3, hard = True)
    $ save_name = ("Тени.\nАКТ 3. Тайна.")
    $ sotp_set_mode_adv()
    $ renpy.pause(0.5, hard = True)
    $ sotp_show_centered_text("Тени. АКТ 3. Тайна.", transition = dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    scene bg sotp_prosecutor_office
    show sotp_snow_layer3_anim
    show sotp_snow_layer2_anim
    show sotp_static_noise_anim
    with Dissolve(2)
    play ambience sotp_winter_wind fadein 2
    play music sotp_master_of_spirits_alien_shadow fadein 2
    sotp_narrator "Зимний вечер сшибал своей прохладой и свежестью. Сказаев медленно, словно в нерешительности, перешагнул порог прокуратуры и попал на тускло освещенное крыльцо."
    sotp_narrator "С момента его последнего выхода улицы уже успели покрыться белёсым покрывалом с редкими грязными лужами в дорожных ямах - но и те постепенно затягивались тонкой коркой льда." 
    sotp_narrator "После сумрака допросной комнаты тут света было слишком. Он резал глаза и заставлял щуриться."
    sotp_narrator "Вытащив из внутреннего кармана пальто портсигар, следователь закурил предпоследнюю сигарету. Едкий дым царапнул горло, но взамен немного расслабил."
    sotp_narrator "Быстро докурив, Павел Иванович неторопливо спустился по косым бетонным ступеням и направился в сторону дома, но спустя мгновение остановился и подумал зайти в аптеку напротив, за обезболивающим." 
    sotp_narrator "Видок у него, кстати, был тот ещё."
    show bg sotp_skazaev_prosecutor_office behind sotp_snow_layer3_anim with dissolve
    sotp_narrator "Помятая одежда, красные, лопнувшие капилляры глаз, огромные мешки под этими самыми глазами, которые, впрочем, больше смахивали на настоящие синяки."
    sotp_narrator "Квартал, окружающий здание прокуратуры, являлся промышленным, и запах был соответствующим. Пахло какой-то гарью вперемешку с солидолом и ещё чёрт пойми чем."
    sotp_narrator "За столько лет работы в этом месте следователь никак не мог привыкнуть к естественной в этих местах вони, поэтому, проходя мимо заводских помещений, уже привычно и незаметно для самого себя скривил нос от мерзкого запаха." 
    sotp_narrator "Для местных запах был обыденностью и неприязни не вызывал, да и люд здесь был простым и работящим. {w}Цеховым, можно сказать." 
    sotp_narrator "В потёмках следователь вполне мог сойти за типичного такого работягу, тащущего свой горб после тяжёлой смены."
    sotp_narrator "Выдавало его разве что выражение лица и слишком чистое, дорогое пальто. Возможно, что Тишкевич работал именно на этом заводе, который в таком случае лишился сотрудника."
    sotp_narrator "«Готов поспорить, что ненадолго», - подумал Сказаев."
    show bg sotp_ext_living_buildings behind sotp_snow_layer3_anim with dissolve
    sotp_narrator "Вдали уже виднелись провинциальные потекшие хрущёвки."
    sotp_narrator "В большинстве окон горел свет, и можно было разглядеть какую-нибудь семейную драму, которые в большинстве своём похожи одна на другую, как трафарет."
    sotp_narrator "Только вот сейчас эти фоторамки окон были украшены гирляндами и бумажными снежинками, что делало проблемы за ними более... незначительными, что ли. {w}Уже совсем скоро новый год, который Павел Иванович, как всегда, встретит на работе."
    sotp_narrator "Эта работа... Сколько жизней он смог спасти?"
    sotp_narrator "А сколько смертей увидел? Это только кажется, что ко всему можно привыкнуть, но раз за разом всё собирается и скатывается в снежный ком, которому только дай волю обрушиться на голову."
    sotp_narrator "Неожиданно из чертогов памяти вырвалось нечеткое вспоминание, его личная анафема, которая преследовала Павла Ивановича с самого начала карьеры и утихла только спустя шесть лет."
    sotp_narrator "Отец того мальчика. Он ведь тогда точно так же напился до беспамятства. {w}Бредил, невнятно бормотал и смеялся сам себе."
    sotp_narrator "А потом что-то случилось тогда, когда мать задержалась на работе." 
    sotp_narrator "Следователь уже не помнил, что именно случилось в тот злополучный октябрьский вечер. {w}Много воды утекло."
    show bg sotp_ext_living_buildings_fence behind sotp_snow_layer3_anim with dissolve
    sotp_narrator "В память тогда ещё зелёного милиционера впился, словно пиявка, только стоп-кадр с телом девятилетнего мальчишки." 
    sotp_narrator "Подстриженные «под горшок» волосы, покрытые коркой тёмной спёкшейся крови, вытекшей из проломленной молотком головы."
    sotp_narrator "Кадр этот больше смахивал на момент из какого-то второсортного зарубежного ужастика в гнусавой озвучке неизвестного переводчика, который когда-то давно крутили в местном киноклубе."
    sotp_narrator "Именно из-за настолько похожих событий того рокового случая он неосознанно с неподдельным интересом разрабатывал дело Тишкевичей? Или было что-то другое? «К чёрту всё это», - решил следователь." 
    $ sotp_show_centered_text("«К чёрту. Прошлое остается прошлым».", transition = dissolve)
    $ renpy.pause(1, hard = True)
    $ sotp_hide_centered_text(dissolve)
    sotp_narrator "После невеселых воспоминаний на мужчину накатила хандра."
    sotp_narrator "Он шёл по серым улочкам городка, словно по сумеречному лесу, а мерзкий запах окружающей его территории вперемешку с головной болью встал комом поперёк горла." 
    sotp_narrator "Ужасно захотелось выпить чего-нибудь горячительного, и следователь не стал отказывать себе в этом желании."
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    $ sotp_show_centered_text("Тишкевич Антон Степанович в соответствии с частью первой, статьей 105 УК РФ, а также со статьей 23 УК РФ совершил убийство в состоянии алкогольного опьянения, что было рассмотрено как отягчающее обстоятельство. Мужчина был приговорен к восьми годам исправительной колонии общего режима. Смягчающим обстоятельством стало признание, которое в конечном итоге всё же удалось получить на одном из допросов.", transition = dissolve)
    $ renpy.pause()
    $ sotp_hide_centered_text(dissolve)
    $ renpy.pause(0.5, hard = True)
    $ sotp_set_main_menu_cursor()
    return