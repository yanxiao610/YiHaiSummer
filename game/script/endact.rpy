label endact_start:
    scene final_act
    with fade
    play music "audio/music/final.ogg" fadeout 1.0 fadein 1.0
    "终于到了动漫之夜的表演时间了"
    "看着她们在舞台上的表演,你不禁想到"
    mc "她们练习了这么久，演出效果还真是不错啊，没有辜负她们的汗水"
    mc "待会就去下馆子去庆祝一下"

    play sound "audio/voice/qq.mp3"
    "手机提示音"

    show all_final1
    with dissolve
    mc "是李药妍发来的消息"

    play sound "audio/voice/qq.mp3"
    "手机提示音"

    scene final_act
    show master_final1
    with dissolve
    mc "是周可儿发来的消息"

    scene final_act
    "她们两人都是约你今晚出去"
    "你选择晚上和谁一起呢？"

    menu:
        "和李药妍一起去":
            jump all_end_start
        "和周可儿一起去":
            jump master_end_start
