label cospicture_start:

    scene classroom
    with fade   
    play music "audio/music/cos2.ogg" fadeout 1.0 fadein 1.0
    "又是一个普通的上课时间"
    "你正坐在教室里发呆,这时手机震动了一下"

    play sound "audio/voice/qq.mp3"
    show all_invite1
    with dissolve
    "是一条来自李药妍消息"


    scene classroom
    show all_invite2
    with dissolve
    "你很好奇为什么突然叫你网名了"
    "(作者ps: 实际上是因为内置一个聊天软件的代码太复杂了,之后才能读取姓名,我做不出来)"
    
    scene classroom
    play sound "audio/voice/qq.mp3"
    show all_invite3
    with dissolve
    " "

    scene classroom
    show all_invite4
    with dissolve
    "你好奇的问她是什么事"

    play sound "audio/voice/qq.mp3"
    scene classroom
    show all_invite5
    with dissolve
    "你有点惊讶"

    scene classroom
    show all_invite6
    with dissolve
    "她想叫你给她拍cos照片"

    scene classroom
    "你有点意外,想了想决定"
    menu:
        "反正也没什么事,就答应她吧":
            pass
        "不想去,想躺在宿舍床上玩游戏":
            jump all_invite_reject


    scene classroom
    show all_invite_ok1
    with dissolve
    "你看着她的文字心想"
    "应该不是开玩笑,于是同意了她的请求,答应和她一起拍照片,并约好了地点"

    scene classroom
    show all_invite_ok2
    with dissolve
    "阿莲莲向你回复了一个开心的表情"

    scene jiuyuebridge
    with fade
    "到了周六下午,你来到了约定的地点——九月桥"
    show all_cos_normal
    with dissolve

    "你一来就看见了李药妍,她正穿着cos服在九月桥旁边等你"
    "你不禁感叹,几乎是脱口而出"

    scene jiuyuebridge
    mc "……和小樱一模一样啊"

    show all_cos_normal
    with dissolve

    voice "audio/voice/all_19.mp3"
    al "不会奇怪吗？我还是第一次在公共场合穿"

    scene jiuyuebridge
    mc """
        一点也不奇怪，反而……很合适
       
        颜色和你平时的气质挺搭的"
    """

    show all_cos_shy
    with dissolve
    al "真的吗？谢谢你"

    scene jiuyuebridge
    mc "抱歉,等很久了嘛？"

    show all_cos_normal
    with dissolve

    voice "audio/voice/all_20.mp3"
    al """
        没有啦,我刚到不久
        场景我也找好了,就在旁边的的花丛那里
    """

    scene cao2
    with fade
    "你向李药妍手指的方向望去,确实是一个拍照的好地方啊"
    "你们边说边走过去拍照"

    mc "cos服是你亲手做的吗？"


    show all_cos_normal
    with dissolve
    voice "audio/voice/all_21.mp3"
    al "嗯,是我自己做的,花了我好久时间呢"

    scene cao2
    mc """
        真厉害啊,那我可要拍好点,不然对不起你的血汗

    """

    show all_cos_normal
    with dissolve
    voice "audio/voice/all_22.mp3"
    al "哈哈,加油大摄影师"

    scene cao1
    with fade
    "你们来到花丛旁边,开始拍照"

    show all_cos2:
        xpos 500
        ypos 100
    with dissolve

    "你拿起相机开始给李药妍指导动作"

    mc """
        好，那我们从轻松一点的姿势开始
        
        往右看一点，对，微笑……眼神跟着光 
        
        ——很好

        (咔嚓)
    """

    scene cao1
    show all_cos3:
        xpos 500
        ypos 100
    with dissolve

    mc """
        再抬头一点。风来了，别动——

        (咔嚓)

        很好看

    """

    scene cao1
    show all_cos_shy
    with dissolve

    voice "audio/voice/all_23.mp3"
    al "别突然讲这种话啊"

    scene cao1
    mc "哈哈,不好意思"

    "你们又拍了几组照片,这时你提议换个地方拍照"

    mc "我们去大活那边拍吧,换个背景"

    show all_cos_normal
    with dissolve
    al "好啊"

    play music "audio/music/cos1.ogg" fadeout 1.0 fadein 1.0
    scene aju
    with fade
    "你们拍了几组照片后,坐到旁边的石阶上休息"
    
    show all_cos_normal
    with dissolve
    al """
        其实我原本不太敢在校园这种地方穿上cos服

        总觉得会被别人笑"中二"什么的
    """ 

    scene aju

    mc """
        但是你做到了啊
        
        能坚持'喜欢'一件事，比看热闹的人强太多
    """

    show all_cos_shy
    with dissolve


    al """
        ……谢谢你

        我也想留下'喜欢'的证据，不然会忘记自己是什么样的人

        [povname]，你拍照的时候，总是很认真

        感觉在看镜头的人，也被认真地对待
    """

    scene aju
    mc """
        也许吧。
        我觉得拍照不是记录别人，而是……留下当下的空气
    """

    show all_cos_normal
    with dissolve


    voice "audio/voice/all_24.mp3"
    al "那今天的空气，是什么味道的呢？"

    scene aju

    mc "嗯……甜的"

    show all_cos_normal
    with dissolve

    al "甜……吗?"

    scene aju

    mc "糖果摊的味道"

    "两人都笑了起来"

    "坐着歇了会"

    mc "最后再拍一张吧,就用小樱最经典的姿势"
    show all_cos_final
    with dissolve
    al "好啊"
    
    "(ps 作者提示词水平真有限了,太难还原了,望见谅^_^)"
    "咔嚓"
    "你按下快门"

    scene aju
    mc "完美"
    mc "今天就这样吧"

    "你们收拾好东西离开"

    show all_cos_shy
    with dissolve

    voice "audio/voice/all_25.mp3"
    al "今天拍了好多……谢谢你啊"

    scene aju
    mc "我才该谢谢你,拍出这么棒的片子，完全不需要后期了"

    show all_cos_normal

    al """
        呐,[povname]

        下次能再拜托你吗？
        
        我还想试别的角色。也许……不是魔法少女那种
    """

    scene aju
    mc "当然可以啊,只要你不嫌我拍的多"

    show all_cos_normal
    with dissolve
    voice "audio/voice/all_26.mp3"
    al "那就约好了,下次约你拍照的时候你可不许拒绝我哦"

    "李药妍伸出小指，你也伸出小指与她勾在一起来定下这个约定"

jump office_start

label all_invite_reject:

    scene classroom
    show all_invite_refuse1
    with dissolve
    "你拒绝了她的邀请"

    scene classroom
    show all_invite_refuse2
    with dissolve
    "她与你约定下次一起拍照"
jump office_start    