label dance_start:
    scene dance_space
    with fade
    play music "audio/music/dance.ogg" fadeout 1.0 fadein 1.0
    "此刻动漫社中的很多喜欢宅舞的同学正在这里练习跳舞"
    "是为了即将在科大举行的动漫之夜做准备"
    "大家选的曲目也是经典老二次元宅舞《极乐净土》"

    show master_happy2
    with dissolve
    master """
        药妍，那个动作再轻一点
        
        不然看起来太僵硬
    """

    scene dance_space
    show all_sad1
    with dissolve

    voice "audio/voice/all_27.mp3"
    al """
        呜——我已经尽力啦！
        会长都跳得像专业舞者一样。
    """

    scene dance_space
    show master_normal
    with dissolve
    master """
        那是因为我练了三年
        
        放心,多看多练就可以了
        
        这个也是经典宅舞了,很多人都会跳的
    """    

    scene dance_space
    "至于你还在这里的原因是有人喊你过来给这些同学拍照,顺便当当她们的后勤"

    scene dance_space
    "强劲的音乐停下了"

    play music "audio/music/dance1.ogg" fadeout 1.0 fadein 1.0    

    show master_say
    with dissolve


    voice "audio/voice/master_22.mp3"
    master """
        好，今天的动作部分差不多就这样吧
        
        明天重点练同步节奏

        今天就这样吧,大家早点回去休息,可以看看视频复习一下动作
    """

    scene dance_space1
    with fade
    "社员陆续离开，只剩你、李药妍、周可儿三人留下收尾"

    show all_surprise
    with dissolve

    voice "audio/voice/all_28.mp3"
    al """
        啊——累死了

        会长，你果然不是人
    """

    scene dance_space1
    show master_shy
    with dissolve

    master "谢谢夸奖"

    scene dance_space1
    show all_shy
    with dissolve

    voice "audio/voice/all_29.mp3"
    al "那、那个……[povname]，你觉得我刚才跳得怎么样？"

    scene dance_space1
    "你正要开口，会长顺势打断"

    show master_normal
    with dissolve

    voice "audio/voice/master_23.mp3"
    master "要不你帮我看一下动作录像？我想知道哪个角度更自然点"

    scene dance_space1
    show all_curious
    with dissolve

    voice "audio/voice/all_30.mp3"
    al "欸？我也要！我也要你看我的!"

    scene dance_space1
    show all_curious:
        xpos 1080-100
        ypos 200
    with dissolve
    show master_normal:
        xpos 100
        ypos 300
    with dissolve
    "气氛微妙,面对二人请求,你选择"

    menu:
        "先帮会长看":
            jump dance_master_watch
        "先帮李药妍看":
            jump dance_al_watch


label dance_master_watch:
    scene dance_space1
    "你选择了先帮会长看录像"

    mc "我这边调下光线。会长的动作太快，摄像有点模糊"

    show master_think
    with dissolve

    voice "audio/voice/master_24.mp3"
    master "你还挺专业的嘛"

    scene dance_space1
    mc """
        之前社团活动录过

        你刚才那个旋转动作挺漂亮的，不过手臂可以再放松一点
    """          

    show master_normal
    with dissolve
    master """
        看来我还得多仰仗你

        ——[povname]同学
        
        你觉得我现在跳舞的时候，笑得太假了吗？

    """

    scene dance_space1
    mc """
        不

        只是……像在扮演"完美的会长"
    """

    show master_surprise
    with dissolve
    pause 2.0

    scene dance_space1  
    mc """
        真正的你，其实可以不用那么完美
    """

    show master_shy
    with dissolve

    voice "audio/voice/master_25.mp3"
    master """
        ....你这家伙,我会记住的

        那我下次就放松一点
    """

    scene dance_space1
    show master_happy2
    with dissolve

    voice "audio/voice/master_26.mp3"
    master "只要有你在镜头后面，看着我就够了"

    mc "..."

    "之后你又去帮李药妍看了录像就收拾回宿舍了"

    jump endact_start

label dance_al_watch:
    scene dance_space1
    "你选择了先帮李药妍看录像"
    "你拿起平板，播放刚才从相机中导入的李药妍刚才的录像"

    mc "动作还不错，就是中间那一段，手臂稍微快了点"

    show all_surprise
    with dissolve

    voice "audio/voice/all_31.mp3"
    al "欸？真的吗？"

    "同时她向你靠过来"

    al "我来看看"

    "你们两人的身体不经意间触碰到一块"

    scene dance_space1
    show all_shy
    with dissolve
    al "啊……对不起！"

    scene dance_space1
    mc "抱歉"
    
    "你们二人都有些脸红"
    "为了结束这现在尴尬的气氛，你继续帮她分析动作"

    mc """
        这里手臂放松一点

        然后脚步再稳一点就更好了
    
        不过你笑的时候挺自然的，镜头里看着挺舒服
    """

    show all_happy
    with dissolve

    voice "audio/voice/all_32.mp3"
    al " 欸？你是在夸我吗？"

    scene dance_space1
    mc "算是吧"

    show all_happy
    with dissolve

    al """
        那我明天练舞的时候，要更努力笑一点
        
        ……这样你就能多看我几次了
    """

    scene dance_space1
    "李药妍说完这个话你还没有反应,她的脸就害羞红了起来"
    show all_shy
    "你看着李药妍的表情,心里有些微微一动"

    scene dance_space1
    mc "(她真的很可爱啊)"

    "之后你又去帮会长看了录像就收拾回宿舍了"

    jump endact_start