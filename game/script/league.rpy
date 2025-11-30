label league_start:
    scene shetuanzhaoxin
    with fade
    play music "audio/music/league.ogg" fadeout 1.0 fadein 1.0

    mc "这个社团招新真的是好热闹啊，感觉什么社团都有啊，不过我早就决定参加动漫社了"
    mc "动漫社的展位好像在那边，我过去看看"

    scene zhaoxin
    with fade
    show master_normal
    with dissolve

    voice "audio/voice/master_1.mp3"
    "???" "你好呀，同学，你是对动漫社感兴趣吗？"


    mc "算是吧……主要是想了解下，社团都在做些什么"

    "???" """
    我们平时会组织观影会、绘画交流，还有在学园祭期间的原创展览
    """

    voice "audio/voice/master_2.mp3"
    "???" "如果你喜欢ACG文化，一定会觉得这里是天堂。"

    mc "听起来……挺不错的。请问你就是社长嘛？"

    voice "audio/voice/master_3.mp3"
    master """
    啊，对，我是大三的周可儿,现在担任社长,你是新生吧？
    
    名字可以告诉我吗？
    """
    mc "我叫[povname]，很高兴认识你"

    voice "audio/voice/master_4.mp3"
    master "[povname]同学，对吧。那——欢迎你加入我们的社团"

    scene zhaoxin
    show master_bm
    with dissolve
    "她递过来的报名表纸，夹带着一丝淡淡的花香。"

    scene zhaoxin
    with fade
    voice "audio/voice/all_3.mp3"
    "???" "请问这里是动漫社的摊位嘛?"

    mc "这个声音——有点耳熟。"

    show all_surprise:
        xpos 100
        ypos 200
    with dissolve
    mc "是你?"

    voice "audio/voice/all_4.mp3"
    "???" "咦？你是……！"

    "???" "没想到……我们又见面了。"


    mc "你也是来参加动漫社的嘛"

    scene zhaoxin
    show all_shy
    with dissolve

    "???" "嗯……对，我也是来参加动漫社的……谢谢你上次你帮了我"

    scene zhaoxin
    show  master_normal
    with dissolve

    voice "audio/voice/master_5.mp3"
    master "唉，你们两个认识嘛?"

    mc "只是见过一面，我到现在还不知道她的名字呢"

    scene zhaoxin
    show all_shy
    with dissolve
    voice "audio/voice/all_5.mp3"
    al "实在是万分抱歉，我叫李药妍，上次太匆忙了……开学那天没机会好好介绍自己。"

    mc "我是[povname]，很高兴认识你"

    scene zhaoxin
    show master_normal
    with dissolve

    master """
        看来缘分挺奇妙的嘛～那两位都要报名了嘛？
        
        说不定你们以后会在活动中搭档哦～

        动漫社欢迎你们的加入！

        那就把这个报名表填了吧

        这样就可以了，还有扫下这个二维码，加入我们社团群

        [povname]同学还有李药妍同学，那就下次见喽
    """

    scene zhaoxin
    show all_happy:
        xpos 1080-100
        ypos 200
    with dissolve
    show master_normal:
        xpos 100
        ypos 300
    with dissolve
    "[povname] 李药妍" "学姐再见"

    jump walk_start
