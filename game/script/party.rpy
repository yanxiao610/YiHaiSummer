label party_start:
    scene classroom
    with fade
    play music "audio/music/party.ogg" fadeout 1.0 fadein 1.0
    """
    大学的生活已经正式开始了，

    一天接着一天的早八和课程

    但是肯定比高三好多了
    """

    play sound "audio/voice/qq.mp3"
    "一段背景提示音"

    mc """
    是会长在社团群发的消息啊

    说是要在这周六举行第一次线下联谊
    """

    play sound "audio/voice/qq.mp3"
    "又是一段提示音"
    show all_party1
    with dissolve
    mc "是李药妍发的啊"

    scene classroom
    show all_party2
    with dissolve
    
    play sound "audio/voice/qq.mp3"
    mc "她还挺激动的嘛"

    scene classroom 
    show all_party3
    with dissolve

    mc "看来她很期待这次联谊呢"

    scene party_people
    with fade
    mc "好多人啊,都不知道坐哪了"

    "你正想着,突然发现李药妍向你招手"
    show all_hello
    with dissolve

    voice "audio/voice/all_15.mp3"
    al "我旁边还有空位,你坐我旁边吧"

    mc "哦哦,好,多谢了"

    scene party_people
    with fade
    show master_say:
        xpos 1000
        ypos 200
    with dissolve   

    voice "audio/voice/master_6.mp3"
    master """
    欢迎各位新成员来到我们的动漫社～！

    今天我们要彼此了解，分享最爱的作品

    当然，最后还有个问答活动哦！
    
    希望大家玩得开心！
    """
    scene party_people
    with fade
    show master_happy

    scene party_people
    show all_curious
    al "(小声)问答活动……真的假的"

    scene party_people
    show master_happy
    with dissolve
    mc "你看会长那个表情，就知道跑不掉了"

    scene party_people
    with fade
    "会长突然向你走来"
    show master_curious
    with dissolve

    voice "audio/voice/master_7.mp3"
    master "你在小声吐槽我嘛,[povname]同学"

    scene party_people
    show master_xe
    with dissolve
    mc "新成员可是要积极表现的哟～[povname]同学"

    scene party_people
    mc "我只是……还没准备好"

    scene party_people
    show master_xe
    with dissolve

    voice "audio/voice/master_8.mp3"
    master "没关系，我会~带着你一起的～"

    scene party_people
    with fade
    show all_curious
    pause 2.0


    scene party_people
    with fade
    "社员A" "我推《Love Live！》,我推妮可！"
    "社员B" "我喜欢《命运石之门》,助手是最棒的！"
    show master_normal
    with dissolve
    master "[povname]同学,那你喜欢什么作品呢?"
    
    scene party_people  
    mc """
    我喜欢《你的名字》
    或许是因为那种错过与重逢的感觉……很美好吧
    """

    show all_happy
    with dissolve
    al """
    我也是！
    那种就算忘记了名字,也不会忘记彼此的感觉……好浪漫啊
    """

    scene party_people
    "社员们" "哦～～你们不对劲"

    show all_shy
    with dissolve
   
    al "(小声) 不是....那样..."

    "你也不好意思的笑"

    scene party_people
    show master_normal
    with dissolve

    voice "audio/voice/master_9.mp3"
    master "好了好了,大家别闹了,下面开始二次元知识竞赛"
    master "答错要表演一段自己印象深刻的台词哦~"

    scene party_people    
    "经过一段时间比赛,会长也抽到你了"

    show master_normal
    with dissolve
    "请问《命运石之门》中,发往过去的邮件叫什么名字?"
    
    scene party_people
    "你思索了下"
    mc """
    命运石之门是我好久之前看的了,具体细节我记不太清楚了

    嗯~我记得是不是叫"B-mail"?

    """
    show master_normal
    with dissolve


    voice "audio/voice/master_10.mp3"
    master """
    回答错误了哦,[povname]同学
    
    正确答案是D-mail哦
    
    不过没关系,来表演一段台词吧

    那请[povname]来一句《进巨》中你印象最深的台词吧

    """

    scene party_people

    "你深吸一口气,站起来"

    mc "我……?那就……"
    mc "(低声)世界是残酷的"

    show all_happy:
        xpos 1080-100
        ypos 200
    with dissolve
    show master_shy:
        xpos 100
        ypos 300
    with dissolve

    "大家爆笑出声"
    master "(捂脸笑) 好厉害的表现力啊～"
    al "太棒了！"
    "社员" "[povname]你也太中二了吧"

    scene party_people
    "过了一会儿,联谊活动也结束了"
    "大家纷纷都走了，你看会长留在这里收拾东西，你也留了下来"
    "李药妍也留在这里帮忙"

    scene party_classroom
    with fade
    show all_normal
    with dissolve

    voice "audio/voice/al_16.mp3"
    al "会长，你总是笑得好温柔啊"

    scene party_classroom
    show master_happy
    with dissolve
    master """
            那是因为要让大家喜欢社团嘛～

            (停顿)

            不过啊……偶尔也希望，有人能让我放松地笑一次
    """

    scene party_classroom
    mc """
        我觉得，会长其实……已经做得很好了
        
        大家都很喜欢你
    """

    show all_happy
    with dissolve
    al "是啊是啊，会长你真的很棒！"

    scene party_classroom
    show master_happy
    with dissolve
    master """
        谢谢你们的鼓励

        那[povname]呢?
    """

    voice "audio/voice/master_11.mp3"
    master "——你也喜欢我这样的人吗？"
    
    scene party_classroom
    mc "……我——"

    show master_xe
    with dissolve
    master "哈哈,开玩笑的啦,别那么紧张"

    scene party_classroom

    "联谊活动室收拾的差不多了,你们也离开了,只是会长说她还有点事情要处理"
    "于是就只剩你和李药妍了"

    scene eatroad
    with fade
    
    "你和李药妍一起走在小吃街的路上"

    show all_surprise
    with dissolve

    voice "audio/voice/all_17.mp3"
    al "会长……好像和你挺合拍的呢"

    scene eatroad
    
    mc " 她只是善于照顾别人吧"

    show all_sad1
    with dissolve
    al """
        那我呢？
    """

    voice "audio/voice/all_18.mp3"
    al " ——我是不是太笨拙了点？"
    
    scene eatroad
    mc """
        不,你很真实
        而且——
        (微笑)
        你笑起来的样子，比任何动画里的角色都更治愈
    """

    show all_shy
    with dissolve
    al "嗯"


jump cospicture_start
