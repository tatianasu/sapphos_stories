# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Lira = Character('Эйлин', color="#312940")
define King = Character('Король', color="#312940")
define Sigrid = Character('Сигрид', color="#312940")
define Bard = Character('Бардесса', color="#312940")
define Agness = Character('Агнесса', color="#312940")
define Veila = Character('Вейла', color="#312940")
default GG_name = Character('[main_charecter_name]', color="#312940")
define narrator = nvl_narrator

define audio.bard_music = "audio/вступительная.ogg"
define audio.castle_music = "audio/дворец1.ogg"
define audio.sigrid_thim = "audio/тема_наставницы.ogg"
define audio.team_music = "audio/сбор_команды.ogg"
default duty = 0
default honor = 0

default shield = 0
default sword = 0

default timerz = 5
init -1:
    $ off_on = False

#Баллы отношений 
default sigrid_fav = 0
default vaila_fav = 0
default agness_fav = 0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    play music bard_music
    jump scene_1
    return

label scene_1:

    scene bg_castle_hands
    show char_bard_neutral

    Bard "Рано или поздно любая принцесса понимает, что ей суждено стать лидером и вести за собой свою страну."
    Bard "Но что послужит знаком того, что принцесса созрела для власти?"
    Bard "Обряд, переживший века, станет её личным испытанием."
    Bard "За каждой красивой сказкой скрывается трагедия."

    scene bg_walls_hands
    Bard "Укусив отравленное яблоко, Белоснежка измениась навсегда.Тень подозрений не покидала её на протяжении всей жизни." 

    show bg_disney_forest1
    window hide
    pause
    show bg_disney_forest2
    window hide
    pause

    scene bg_walls_hands
    Bard "Аврора. В её замке, ставшем крепостью, не находилось места ни для одной души."
    
    show wip_bg_disney_aurora1
    window hide
    pause
    show wip_bg_disney_aurora2
    window hide
    pause

    scene bg_walls_hands
    Bard "Чего им не хватило? Решительности, смелости или хитрости?"
    Bard "Никто не знает, но след на их жизни это оставило навсегда."
    Bard "Обряд заставил их увидеть мир в его истинном свете."
    Bard "Успешно пройденные испытания означали, что принцесса готова к восхождению на трон."
    Bard "Однако нельзя править страной в одиночку, так же как и пройти этот путь."
    Bard "Сопровождающие принцессу в обряде - героини, будующие главнокомандующие"
    Bard "Обряд существует вне времени. Он всегда был, есть и будет."
    Bard "Преподнесенный самим богами, духами либо другими высшими силами."
    Bard "Не важно. Он направлял человечество рукой избранной королевы."
    Bard "И первый выбор, которая сделает будущая королева..."
    Bard "Это выбор человека, которому она доверит жизнь."


    python:
        main_charecter_name = renpy.input(("Введите ваше имя"))

    Bard "[main_charecter_name]. Она пройдет этот путь вместе с принцессой и докажет свою преданность либо Короне, либо Чести Рыцаря."

    scene bg_castle_throne_room
    
    "Так наша история начинает"
    stop music fadeout 3.0
    
    play sound "audio/скрип_дверей.ogg"
    nvl clear
    "Дубовые двери тронного зала распахнулись, открывая путь ей. В безмолвии ее шаги гремели от стен. Солнце еще не озарило горизонта, и мягкий полумрак затенял лицо короля, сидящего на троне."
    nvl clear

    play music castle_music

    show char_lyra_neutral_eu
    GG_name "{i}Какая неприятная тишина. И Король сидит молча, перебирает в руках печатку. Как же обратить на себя внимание?{/i}"

    
    menu:
        "Потревожить короля":
            GG_name "Ваше Высочество, мне передали, что Вы меня ждете."
            jump scene_1_add1

        "Молча опуститься на колено и ждать.":
            jump scene_2

return

label scene_1_add1:
    scene bg_castle_throne_room
    show char_king_neutral

    King "Доброе утро, леди [main_charecter_name]"

    jump scene_2

return


label scene_2:
    scene bg_castle_throne_room
    show char_king_neutral

    King "Леди [main_charecter_name],ты же понимаешь, что делаешь тут в такое время?"
    hide char_king_neutral

    show char_lyra_neutral_eu
    GG_name "Обряд?... Обряд для принцессы."
    hide char_lyra_neutral_eu

    "Король усмехнулся - сухо, без радости. Поднял на нее уставшие, выцвевшие глаза. Глаза старика."
    nvl clear

    show char_king_neutral
    King "Я не считаю, что ты годишься для этого, но принцееса внезапно выбрала {i}тебя{/i}"
    hide char_king_neutral

    show char_lyra_neutral_eu
    GG_name "{i}Кажется, я ему не нравлюсь{/i}"
    hide char_lyra_neutral_eu

    "В истории есть два пути героини - Долг и Честь. По пути Долга героиня будет верна короне и традициям Обряда во что бы то ни стало. По пути Чести героиня руководствуется своим сердцем. Старайтесь придерживаться одного Пути, но помните, что у каждого выбора будут свои последствия."
    nvl clear

    show char_lyra_neutral_eu
    menu:   
        "Согласиться":
            GG_name  "Я постораюсь не разочаровать Вас (+ Долг)"
            $ duty += 1
            jump scene2_dute

        "Возразить":
            GG_name "Принцесса выбрала меня, она верит, что я справлюсь.(+ Честь)"
            $ honor += 1
            jump scene2_honor

        "Молчать":
            jump scene2_silence

    return


label scene2_dute:

    scene bg_castle_throne_room
    show char_king_neutral

    King "Могу поспорить, что твоя мать говорила тоже самое, леди [main_charecter_name]"
    King "Прежде, чем предать мою жену."

    jump scene_3

    return

label scene2_honor:

    scene bg_castle_throne_room
    show char_king_neutral

    King "Покойная королева тоже верила в твою мать, леди [main_charecter_name]"
    King "И жестоко за это поплатилась."

    jump scene_3

    return

label scene2_silence:

    scene bg_castle_throne_room
    show char_king_neutral

    King "Нечего сказать, леди [main_charecter_name]?"
    hide char_king_neutral

    show char_lyra_neutral_eu
    GG_name "..."
    hide char_lyra_neutral_eu

    show char_king_neutral
    King "Наверное, стыд полностью овладел тобой из-за предательство твоей матери"
    King "Покойная королева так верила в нее."
    
    jump scene_3

    return

label scene_3:

    scene bg_castle_throne_room
    show char_king_neutral

    King "Только благодаря Сигрид предыдущий обряд  успешно завершился."
    King "Она воспитала тебя леди [main_charecter_name], поэтому я даю тебе шанс"
    hide char_king_neutral

    show char_lyra_sadness_eu
    GG_name "{i}Успешно завешился? моя мать погибла во время того обряда.{/i}"
    hide char_lyra_sadness_eu

    show char_king_neutral
    King "Воспользуйся шансом стереть позор с имени своей семьи."
    hide char_king_neutral

    show char_lyra_anger_eu
    menu:
        "Возразить (+ Честь)":
            GG_name "Ваше Высочество, моя мать пожартвовала жизнью во время того обряда!"
            jump scene_3_add1

        "Молчать.":
            jump scene_3_add2

    return

label scene_3_add1:

    scene bg_castle_throne_room
    show char_king_neutral

    King "Это была ее плата за предательство!"
    hide char_king_neutral

    show char_lyra_sadness_eu
    GG_name "..."
    hide char_lyra_sadness_eu
    
    show char_king_neutral
    King "Похоже Сигрид не научила тебя манерам."

    jump scene_4

label scene_3_add2: 

    scene bg_castle_throne_room
    show char_lyra_anger_eu
    GG_name "..."

    jump scene_4

label scene_4:

    scene bg_castle_throne_room
    show char_king_neutral

    King "Десятки лет тренеровок пошли на смарку из-за прихоти принцессы"
    
    King "Это не твоя судьба, она была уготовлена другой..."

    "В порыве злости король ударил кулаком по подлокотнику"
    nvl clear
    
    King "Ты не прошла подготовку! Глупая девчонка не достойна занять место главы королевской гвардии, советницы королевы!"

    "Обессиленный, король закрыл глаза"
    nvl clear

    King "Мне будет не хватать Сигрид на ее посту, если ты заменишь ее."

    hide char_king_neutral
    show char_lyra_anger_eu
    menu:
        "Отказаться от возможности (+ Честь)":
            GG_name "Я не притендую на место Сигрид (+Честь)"
            $ honor += 1
            jump scene4_honor

        "Следовать правилам (+ Долг)":
            GG_name "После обряда рыцарь обязан принять на себя бремя руководства всей королевской армией. (+Долг)"
            $ duty += 1
            jump scene4_duty

label scene4_honor:

    scene bg_castle_throne_room
    show char_king_neutral

    King "От твоего желания ничего тут не зависит"

    King "После обряда рыцарь обязан принять на себя бремя руководства всей королевской армией."
    
    King  "Хотя я и уверен, что ты слишком юна для этого"

    jump scene_5

label scene4_duty:
    scene bg_castle_throne_room
    show char_king_neutral
    
    "Король грустно усмехнулся"
    nvl clear 

    King  "Радует, что ты хотя бы законы знаешь"
    King "Не забывай, что предательство карается смертью по закону"

    jump scene_5
    
label scene_5:

    scene bg_castle_throne_room
    show char_king_neutral
    
    King "Надеюсь, ты не пойдешь по стопам матери. А теперь иди."

    King "Обряд ждет верных."

    if duty > honor:
        jump scene5_duty
    else:
        jump scene5_honor

label scene5_duty:
    scene bg_castle_throne_room
    show char_lyra_anger_eu
    GG_name "{i}Я не подведу корону{/i}"
    jump scene_6

label scene5_honor:
    scene bg_castle_throne_room
    show char_lyra_anger_eu
    GG_name "{i}Я не подведу принцессу{/i}"
    jump scene_6



label scene_6:
    stop music fadeout 2
    play sound "audio/скрип_дверей.ogg"
    play music sigrid_thim
    "В смешанных чувствах [main_charecter_name], покинула тронный зал" 
    nvl clear
    #Звук - скрип двери
    "Выйдя во внутренний двор она остановилась, чтобы перевести дух. И тут же встретилася взглядом с наставницей"
    nvl clear
    scene bg_castle_courtyard

    show char_sigrid_smile
    Sigrid "Ну что, цыпленок, готова к их играм?"
    hide char_sigrid_smile

    show char_lyra_anger_eu
    GG_name "Разве у меня есть выбор?"
    hide char_lyra_anger_eu

    show char_sigrid_smile
    Sigrid "Выбор есть всегда, но правильный только один."
    hide char_sigrid_smile

    show char_lyra_sadness_eu
    GG_name "Король говорил о моей матери, снова называл ее предательницей"
    GG_name "Сигрид, почему ты всегда юлишь, когда я спрашиваю о ней"
    hide char_lyra_sadness_eu

    show char_sigrid_neutral
    Sigrid "Ты уже знаешь, все, что должна, а перемывать кости павшим воинам ниже моего достоинства"
    hide char_sigrid_neutral

    show char_lyra_anger_eu
    GG_name "Ты всегда говорила мне, что она была доблестной воительницей! Я не верю, что она могла предать корону!"
    hide char_lyra_anger_eu

    show char_sigrid_smile
    Sigrid "Сосредоточься на настоящем, а не на прошлом. Кстати, держи."


    $ timerz = 2
    $ off_on = True
    $ time_range = 2
    $ marker = "faile_scene"

    menu:
        "Поймать":
            jump scene_7

label scene_7:
    $ off_on = False
    scene amulet_cutscene_line
    window hide
    pause

    "Треснувший синий камень на шнурке"
    nvl clear
    jump scene_8
    
    

label faile_scene:
    scene bg_castle_courtyard
    "[main_charecter_name] не успела. Глухой стук послышался у ее ног."
    nvl clear

    "Сигрид немного расстроилась из-за этой оплошности."
    nvl clear

    show char_sigrid_thoughtful
    Sigrid "Реакция снижена. Надеюсь, это просто от нервов?"
    
    scene amulet_cutscene_line
    window hide
    pause

    "[main_charecter_name] наклонилась и ахнула."
    nvl clear

    "Треснувший синий камень на шнурке"
    nvl clear

    scene bg_castle_courtyard
    show char_lyra_sadness_eu
    GG_name "Это из-за меня?"
    hide char_lyra_sadness_eu

    show char_sigrid_thoughtful
    Sigrid "Если ты про трещину, то нет."
    jump scene_8

label scene_8:
    $ off_on = False
    
    scene bg_castle_courtyard
    show char_lyra_sadness_eu
    GG_name "Что это?"
    hide char_lyra_sadness_eu


    show char_sigrid_neutral
    Sigrid "Амулет для связи со мной. Просто сожми в руке и представь мое лицо"
    hide char_sigrid_neutral


    show char_lyra_neutral_eu
    GG_name "Откуда он у тебя? Магия же запрещена."
    hide char_lyra_neutral_eu

    show char_sigrid_neutral
    Sigrid "Времена меняются, но лучше бы тебе хранить медальон в секрете"
    hide char_sigrid_neutral

    'В истории есть два стата, влияющих на действия и характер героини - Клинок и Щит. По статам Клинка героиня будет остра на язык и скоропалительна в своих решениях. По статам Щита героиня будет более вдумчива и последовательна в своих решениях. Старайтесь придерживаться одного стата, но помните, что у каждого выбора будут свои последствия.'
    nvl clear

    show char_lyra_neutral_eu
    menu:
        "Съязвить (+ 1 балл Клинок)":
            GG_name "Думаешь мне тебя на тренеровках не хватило?"
            $ sword += 1
            jump scene8_sword

        "Поблагодарить (+ 1 балл Щит)":
            GG_name  "Спасибо, мне нужна любая помощь."
            $ shield += 1
            jump scene8_shield

label scene8_sword:
    scene bg_castle_courtyard

    "Вам палец в рот не клади." #табличка
    nvl clear

    show char_lyra_smile_eu
    GG_name "Ты делаешь мне одолжение под видом помощи? Боишься, что я не справлюсь?"
    hide char_lyra_smile_eu

    show char_sigrid_thoughtful
    Sigrid "..."
    

    "Сигрид закатила глаза."
    nvl clear
    hide char_sigrid_thoughtful

    show char_lyra_smile_eu
    GG_name "Или что я сбегу?"
    hide char_lyra_smile_eu

    show char_sigrid_neutral
    Sigrid "Хватит!"

    Sigrid "Пойдем на улицу. Тебе уже приготовили коня."
    
    jump scene_9

label scene8_shield:
    scene bg_castle_courtyard
    
    "Вы сдержаны и обходительны." #табличка 
    nvl clear
    
    show char_sigrid_neutral
    Sigrid "Пойдем на улицу. Тебе уже приготовили коня."

    jump scene_9

label scene_9:
    scene bg_castle_courtyard

    show char_sigrid_neutral

    Sigrid "..."
    Sigrid "*протягивает еще что-то*"

    hide char_sigrid_neutral

    show char_lyra_thougtful_eu
    GG_name "Карта?"
    hide  char_lyra_thougtful_eu

    show char_sigrid_neutral
    Sigrid "А ты как хотела, вслепую искать?"
    hide char_sigrid_neutral

    show char_lyra_anger_eu
    GG_name "*нахмурилась и потупила голову*"
    hide  char_lyra_anger_eu

    show char_sigrid_thoughtful
    "Сигрид неспокойно." #табличка
    nvl clear

    Sigrid "Да что с тобой такое."

    Sigrid "*вздохнула*"

    Sigrid "Ты это из-за короля?"
    hide char_sigrid_thoughtful

    show char_lyra_sadness_eu
    GG_name "Да"
    GG_name "{i}За столько лет так и не приблизилась к разгадке смерти моей матери, Сигрид не хочет ни подтвердить, ни опровергнуть предательство.{/i}"
    hide char_lyra_sadness_eu

    show char_sigrid_thoughtful 
    Sigrid "Если ты пройдешь Обряд, прошлое уже не будет иметь значение."
    hide char_sigrid_thoughtful

    show char_lyra_smile_eu
    GG_name "Возможно ты права"
    hide char_lyra_smile_eu

    show char_sigrid_smile 
    Sigrid "Я верю в тебя. Совсем недавно ты была достойной ученицей, пришло время превзайти учителя."
    hide char_sigrid_smile 

    show char_lyra_neutral_eu
    GG_name '{i}Видимо, уже пора уходить?{/i}'

    menu:
        "Коснуться руки (+ 1 балл отношения с Сигрид)": #платный выбор
            $ sigrid_fav += 1
            jump scene9_sigrid_fav

        "Кивнуть":
            jump scene9_no_sigrid
    
label scene9_sigrid_fav:

    scene bg_castle_courtyard
    show char_lyra_neutral_eu

    "[main_charecter_name] потянулась к руке наставницы"
    nvl clear

    GG_name "{i}Могу ли я попросить ее обнять меня?{/i}"
    hide char_lyra_neutral_eu

    show char_sigrid_thoughtful
    "Сигрид нахмурилась, однако руку не убрала"
    hide char_sigrid_thoughtful

    show char_lyra_sadness_eu
    GG_name "Сигрид?"
    hide char_lyra_sadness_eu

    show char_sigrid_thoughtful
    Sigrid "Да?"
    hide char_sigrid_thoughtful

    show char_lyra_sadness_eu
    GG_name "Когда моей матери было сложно, ее поддержали?"
    hide char_lyra_sadness_eu

    show char_sigrid_thoughtful
    Sigrid "*Задумалась.*"
    Sigrid "Ингрид… Пожалуй, она не знала, что такое поддержка."
    hide char_sigrid_thoughtful

    show char_lyra_sadness_eu
    GG_name "Может, поэтому она сделала что-то не так? Мать просто не поддержали, и она сама тоже не умела?"
    
    nvl clear
    '[main_charecter_name] сжала ее сухую горячую ладонь'
    nvl clear

    show char_lyra_sadness_eu
    GG_name "Тебе было страшно во время обряда?"
    hide char_lyra_sadness_eu

    show char_sigrid_thoughtful
    Sigrid "Мне было страшно, [main_charecter_name], но я была лишь оруженосицей, все главные решения принимала твоя мать"
    hide char_sigrid_thoughtful

    show char_lyra_sadness_eu
    GG_name "{i}В тот день не только я потеряла близкого человека.{/i}"
    GG_name "Мне так жаль, что тебе пришлось это пережить"
    hide char_lyra_sadness_eu

    "Сигрид притянула к себе воспитанницу за руку. [main_charecter_name] прильнула к наставнице и заключила в объятия. Иногда для успокоения души, нужно немного человеческого тепла."
    nvl clear

    "[main_charecter_name] жадно впитывала это тепло кожей. Прежде, чем объятия стали неприлично долгими, [main_charecter_name] разжала руки и посмотрела в глаза Сигрид. В памяти отпечатался запах сена и расскаленного железа - запах волос Сигрид."
    nvl clear
    
    show char_lyra_smile_eu
    GG_name "Этот запах. Так успокаивает."

    "Кажется, Сигрид может быть мягкой." #табличка
    nvl clear

    jump scene_10

label scene9_no_sigrid:
    scene bg_castle_courtyard

    "Сигрид потрепала [main_charecter_name] по голове." 
    nvl clear

    jump scene_10

label scene_10:
    scene bg_castle_courtyard

    "{i}[main_charecter_name] прикрыла глаза, медленно вдыхая и выдыхая. Предстоит что-то тяжелое, что-то, что выходит за рамки теории.{/i}"
    nvl clear 

    show char_sigrid_smile
    Sigrid "Впрочем, ладно. Пора в путь."
    stop music fadeout 2.0
    play sound "audio/скрип_дверей.ogg"
    "[main_charecter_name] обернулась на скрип ворот. В проеме показались две женские фигуры. Первым делом в глаза бросилась…"
    nvl clear
    play music team_music
    menu:
        "Та, что в доспехах":
            jump scene10_armor

        "Та, что в плаще":
            jump scene10_hood

label scene10_armor: 
    scene bg_castle_courtyard

    "[main_charecter_name] увидела знакомую экипировку учебного легиона Поющих клинков. Вьющиеся короткие волосы непослушно обрамляли лицо"
    nvl clear 

    show char_lyra_anger_eu
    GG_name "Ты выбрала оруженосицу за меня?"
    hide char_lyra_anger_eu

    show char_sigrid_smile
    Sigrid "Да, ты бы не выбрала никого лучше."
    hide char_sigrid_smile

    show char_lyra_anger_eu
    GG_name "Но моя мать выбирала оруженосицу сама! Тогда она и выбрала тебя."
    hide char_lyra_anger_eu

    show char_sigrid_smile
    Sigrid "Назначение твоей матери не было таким внезапным, как твое."
    hide char_sigrid_smile
    
    show char_lyra_thougtful_eu
    "[main_charecter_name] посмотрела на вторую спутницу. Потрепанный плащ, надменный взгляд и черные, как смоль волосы."
    nvl clear
    GG_name "Это кто?"
    hide char_lyra_thougtful_eu

    show char_sigrid_neutral
    Sigrid "Вейла. Одна из сильнейших ведьм Десятого королевства."
    hide char_sigrid_neutral

    show char_lyra_thougtful_eu
    GG_name "Сколько я себя помню, в Тринадцатом королевсте магия и ведьмы под запретом" 
    hide char_lyra_thougtful_eu
    
    show char_sigrid_smile
    Sigrid "Я же говорила, что времена меняются"

    jump scene_11

label scene10_hood:
    scene bg_castle_courtyard
    

    "[main_charecter_name] присмотрелась к истрепавшейся ткани плаща. А потом подняла глаза на саму девушку, жующую яблоко."
    nvl clear

    show char_lyra_thougtful_eu
    GG_name "Это кто?"
    hide char_lyra_thougtful_eu

    show char_sigrid_neutral
    Sigrid "Вейла. Одна из сильнейших ведьм Десятого королевства."
    hide char_sigrid_neutral

    show char_lyra_thougtful_eu
    GG_name "Сколько я себя помню, в Тринадцатом королевсте магия и ведьмы под запретом" 
    hide char_lyra_thougtful_eu

    show char_sigrid_neutral
    Sigrid "Я же говорила, что времена меняются"
    hide char_sigrid_neutral

    show char_lyra_thougtful_eu
    GG_name "А она?"
    "[main_charecter_name] указала на вторую спутницу в знакомой экипировке учебного легиона поющих клинков."
    nvl clear
    hide char_lyra_thougtful_eu

    show char_lyra_thougtful_eu
    GG_name "Ты выбрала оруженосицу за меня?"
    hide char_lyra_thougtful_eu

    show char_sigrid_neutral
    Sigrid "Да, ты бы не выбрала никого лучше."
    hide char_sigrid_neutral

    show char_lyra_anger_eu
    GG_name "Но моя мать выбирала! Она выбрала тебя."
    hide char_lyra_anger_eu

    show char_sigrid_neutral
    Sigrid "Назначение твоей матери не было таким внезапным, как твое."

    jump scene_11

label scene_11:
    scene bg_castle_courtyard

    show char_agnessa_neutral
    Agness "*Торопливо кланится*"
    Agness "Леди [main_charecter_name]! Я... я буду вашей оруженосицей, меня зовут Агнесс!"
    hide char_agnessa_neutral

    show char_lyra_anger_eu
    "[main_charecter_name] сощурилась." 
    nvl clear
    hide char_lyra_anger_eu
    
    show char_agnessa_neutral
    "{i}Агнесса покраснела, теребя в руках какую-то травинку.{/i}"
    nvl clear
    hide char_agnessa_neutral

    show char_veila_sarcasm
    Veila "Оружие хоть держать умеешь? Или только краснеть научилась?"
    hide char_veila_sarcasm

    show char_agnessa_neutral
    Agness "У-умею! Я была лучшей в легионе!"
    hide char_agnessa_neutral

    show char_veila_sarcasm
    "{i}Ведьма засмеялась.{/i}"
    nvl clear 
    hide char_agnessa_neutral
    
    show char_veila_sarcasm
    Veila "А это действительно будет весело."
    hide char_veila_sarcasm

    show char_lyra_anger_eu
    "{i}[main_charecter_name] резко выдохнула, пытаясь унять раздражение.{/i}"
    nvl clear


    jump scene11_shield


label scene11_shield:
    scene bg_castle_courtyard
    show char_lyra_thougtful_eu
    GG_name "А еще мне казалось, что в Обряде учавствуют только трое: принцесса, рыцарка и ее оруженосица."
    hide char_lyra_thougtful_eu

    show char_veila_anger
    Veila "*скрестила руки на груди.*"
    Veila "Я – Ваша гарантия на прохождение Обряда."
    hide char_veila_anger

    show  char_sigrid_neutral
    Sigrid "Иногда исключения оправданы. Ведьма должна быть здесь на этот раз."
    hide char_sigrid_neutral
    
    show char_lyra_thougtful_eu
    "[main_charecter_name] понимающе кивнула. Она еще расспросит обо всем у Вейлы."
    nvl clear
 
    GG_name "Меня зовут [main_charecter_name]"

    jump scene_12


label scene_12:
    scene bg_castle_courtyard
    
    show char_sigrid_neutral
    Sigrid "Теперь, когда все друг другу представились..."

    "Сигрид сделала паузу, окидывая всех взглядом."
    nvl clear

    show char_sigrid_neutral
    Sigrid "Расскажу про ваши задачи: дойти до башни, спасти принцессу и вернуться в течение недели."
    hide char_sigrid_neutral

    show char_agnessa_neutral
    Agness "И все?"
    hide char_agnessa_neutral

    show char_sigrid_smile
    Sigrid "А нужно что-то еще?"
    hide char_sigrid_smile

    show char_agnessa_neutral
    "Агнесса робко протянула руку, как на уроке."
    nvl clear 
    hide char_agnessa_neutral

    show char_agnessa_neutral
    Agness "Может, нам взять еще провизии? А не только ту, что лежит в сумках на лошадях."
    hide char_agnessa_neutral

    show char_veila_sarcasm
    Veila "Вдруг принцессе захочется пикника? Это не прогулка, девочка. Лошади тоже устают, им незачем лишний груз."
    hide char_veila_sarcasm

    show char_lyra_neutral_eu
    GG_name "Самое главное для нас сейчас…"

    menu:
        "не загнать лошадей (+ отношения с Вейлой)":
            $ vaila_fav += 1
            "Вейла ценит, что Вы к ней прислушиваетесь" #табличка
            nvl clear
            jump scene_13

        "не быть голодными(+ отношения с Агнессой)":
            $ agness_fav += 1
            "{i}«Агнесса ценит Вашу предусмотрительность»{/i}"#табличка
            nvl clear
            jump scene_13

        "быстрее добраться(+отношения с принцессой)":
            "{i}«Принцесса бы оценила Ваше умение расставлять приоритеты»{/i}"#табличка
            nvl clear
            jump scene_13
    
label scene_13:

    scene bg_castle_courtyard
    show char_sigrid_neutral
    Sigrid "Ну что. Готова? Башня ждет."
    hide char_sigrid_neutral

    show char_lyra_sadness_eu
    GG_name "А что если я провалю миссию?"
    hide char_lyra_sadness_eu

    show char_sigrid_thoughtful
    "Сигрид замолчала на минуту. Ветер пошевелил ее волосы. Наконец она разомкнула губы, и в ее голосе прозвучало что-то, похожее на страх."
    nvl clear 
    hide char_sigrid_thoughtful
    #ЗАМЕНИТЬ ЭМОЦИЮ

    show char_sigrid_thoughtful
    Sigrid "Тогда ты не достойна нести эту ношу."
    hide char_sigrid_thoughtful

    show char_lyra_sadness_eu
    "[main_charecter_name] закусила губу, но кивнула."
    nvl clear

    scene bg_castle_gate
    "За ними закрылись ворота. Впереди утоптанная тропа, ведущая в густой лес. Воздух наполнен запахом хвои и предчувствием опасности."
    nvl clear 

    show char_lyra_neutral_eu
    GG_name "Главное — не потеряться по дороге. Тебя это особенно касается"

    "Ее взгляд метнулся к…"
    nvl clear

    menu:
        "Агнессе":
            jump scene13_agness

        "Вейле":
            jump scene13_vaila

label scene13_agness:
    scene bg_castle_gate
    show char_agnessa_neutral
    Agness "Я буду следовать за вами, как тень!"
    hide char_agnessa_neutral 

    show char_veila_sarcasm
    Veila "Тень, которая спотыкается о собственный меч?"
    hide char_veila_sarcasm

    show char_lyra_neutral_eu
    "[main_charecter_name] повела плечами."
    nvl clear 

    jump scene_14

label scene13_vaila:
    scene bg_castle_gate
    show char_veila_smile
    Veila "Главное - успевайте за мной, леди [main_charecter_name]. Я вас ждать не буду."
    hide char_veila_smile
    
    show char_lyra_neutral_eu
    "[main_charecter_name] вздохнула, но почувствовала, как в ее груди разгорается искорка вызова."
    nvl clear 
    hide char_lyra_neutral_eu

    jump scene_14 

label scene_14:
    scene bg_castle_gate

    show char_lyra_neutral_eu
    GG_name "Давайте перепалки оставим хотя бы до первого привала."
    "[main_charecter_name] аккуратно развернула карту."
    nvl clear
    GG_name "По карте понятно, что ехать придется дня полтора."
    hide char_lyra_neutral_eu

    show char_lyra_smile_eu
    GG_name "Если, конечно, никто не устроит гонки на выживание."
    hide char_lyra_smile_eu
    "Вейла усмехнулась, а Агнесса потрепала коня по холке."
    nvl clear

    show char_veila_smile
    Veila "Ну что же, быстрее начнем - быстрее закончим. Ведите, леди [main_charecter_name]."

    stop music fadeout 0.5


#-------------ГЛАВА ВТОРАЯ------------------

