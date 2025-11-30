label office_start:
    scene classroom1
    with fade
    play music "audio/music/master.ogg" fadeout 1.0 fadein 1.0
    "现在是晚上9点半,9点钟就下晚自习了,你的同学都回宿舍了,你还留在教室里备考4级"
    mc "现在时间也差不多了吧,该回宿舍了"

    "你收拾好东西,准备离开教室"

    scene master_even
    with fade
    "走在走廊上,你随意往教室中一看,却发现一个熟悉的身影正坐在教室里"
    "是动漫社的社长,正是你的学姐周可儿"

    menu:
        "进去和学姐聊会吧":
            pass
        "算了,看书有点太累了,直接回宿舍吧":
            jump dance_start
            
    mc """
        ……会长？

        你怎么还在教室里面啊
    """    

    show master_scary
    with dissolve

    voice "audio/voice/master_12.mp3"
    master "啊...."

    "会长似乎被你的突然出现吓了一跳"

    scene master_even

    mc "抱歉抱歉,会长,我不是故意吓你的"
    mc "(看来会长十分投入啊,连旁边有人都没注意到)"

    show master_normal
    with dissolve

    "会长很快转换成平常的状态,微笑着看向你"


    master """
        没关系
    """

    voice "audio/voice/master_13.mp3"
    master """
        是我有点大惊小怪了

        我只是在写些课外作业罢了
    """

    scene master_even

    mc "作业?"

    show master_tired
    with dissolve
    master """
        嗯——

        (揉揉眼睛)

        白天被社团事务缠住,只有晚上才能有时间做些自己的事情

        ——算是补救时间吧
    """ 

    scene master_even
    mc """
        会长你真的很拼呢

        我要没看错的话,你桌子上的这些都是建筑专业的书吧
    """

    show master_normal
    with dissolve
    master "是啊,建筑专业的课业量本来就很大,平时社团活动又多,只能利用晚上时间补课了"
    
    voice "audio/voice/master_14.mp3"
    master "不过也还好啦,我还挺喜欢建筑的"

    scene master_even
    mc """
        哎,真的嘛学姐,我还以为你会更喜欢动漫什么的呢

        很难将像你这么漂亮的女生和建筑联系到一起呢
    """

    show master_happy2
    with dissolve
    master """
        确实有很多人都这么和我说过呢

        但是事实上我就是特别喜欢建筑啊

        古典中式园林,西方罗马建筑啊这些我都很喜欢

        尤其是当我想到这么一个庞然大物能从无到有地被设计出来,然后被建造出来
        
        心里就会觉得特别有成就感
    """

    scene master_even

    mc "说到建筑,学姐的话也变得多起来了呢"
    mc "那学姐你有特别喜欢的建筑或者建筑师吗?"

    show master_surprise
    with dissolve

    master """
        嗯....

        要说特别喜欢的话,我觉得就是贝聿铭

        我说过我喜欢中式园林,贝聿铭在老年的时候回苏州设计了苏州博物馆

        他的设计把现代建筑和传统中式园林结合得非常好
    """

    scene master_even
    show master_happy

    master """
        用无人机从高空俯拍,简直是太美了啊

        真的是太美了啊

        还有他设计的香港中银大厦,以竹子为灵感,用棱柱/三角这样的几何形式去实现

        真的非常令人震撼

        包括法国现在的卢浮宫玻璃金字塔也是他设计的

        他对几何还有光的应用真的是顶级了

        别聊我了,我都快说起兴致来了

        (停顿)
    """    

    voice "audio/voice/master_15.mp3"
    master """
        对了[povname],你是为什么选土木这个专业呢?

        你高考分数应该可以选其他的热门专业吧

        像电子计算机这些专业
    """

    scene master_even
    mc """
        我选土木的原因啊

        记得初一暑假的时候

        家里亲戚带我去工地上打灰，虽然累，但是想到建筑是因为自己而建造成功的时候，心里不免兴奋

        尤其是我记得当时的工地是一个大酒店，酒店的楼层非常高，当你从水泥混凝土的框架向下眺望的话，你会油然升起一股 “I am the king  of world 的感觉”

        别人都说土木不行了，我偏不信，我喜欢工地的样板间，喜欢和混凝土打交道，喜欢基建

        我决定放弃计算机，把我的天赋带入工地
    """

    show master_happy2
    with dissolve

    voice "audio/voice/master_16.mp3"
    master "你这个理由还挺有意思的，看来我们两个还是很像的" 
    master "对了,你想读研嘛"

    scene tongji
    with fade
    mc """
        我才大一，还没考虑好

        但是我一直听说"宇宙第一土木"的称号

        扎根大地不离土,培育栋梁参天木

        我对同济大学充满了好感，我也想去朝圣
    """   

    scene master_even
    with fade
    show master_surprise
    with dissolve
    master "我们两个还真的是很像呢,连想去的大学都一样"

    scene master_even
    show master_happy2
    with dissolve
    master """
        同济的建筑也是国内顶尖水平，我想去那里进修

        为了这个目标我努力了很多年

        在我21年高考的时候,建筑还和计算机一样是热门专业

        其实当年我超过了工大的录取分数线

        但是我没有办法选择建筑专业

        于是我便选择了省内第二的建筑专业院校

        就是我们学校

        只是可惜现在的建筑类分数线越来越低了
    """

    scene master_even
    mc "学姐,你还真是不容易呢"
    mc "你每天都这么辛苦嘛"


    show master_tired
    with dissolve

    voice "audio/voice/master_17.mp3"
    master """
        嗯,大概吧

        白天当社长,晚上画图
    """

    mc "学姐会感到累嘛?"

    scene master_even
    show master_normal
    with dissolve


    voice "audio/voice/master_18.mp3"
    master "有的时候也会有点累的"

    scene master_even

    mc "那现在呢"

    show master_xe

    master """
        不累
        因为今晚，有个人陪我一起了
    """

    scene master_even
    mc "……"

    show master_normal
    with dissolve

    voice "audio/voice/master_19.mp3"
    master "你不会嫌无聊吧?"


    scene master_even
    mc """
        不会
        
        我觉得——
        
        学姐平时总是一副从容不迫的样子

        今天能看到"学姐在认真努力的样子",挺难得的

    """

    show master_happy2
    with dissolve
    pause 2.0

    scene master_even
    mc "学姐偶尔也可以停下来休息会啊,没必要把自己搞得那么累的"

    show master_surprise
    with dissolve

    master "是嘛....."

    scene master_even

    "就这样,你也在会长旁边坐下继续开始备考4级"

    "时间很快就到了11点"

    show master_tired
    with dissolve
    master "终于搞定了,我也该下班了"

    scene master_even
    mc "辛苦了"

    show master_happy2
    with dissolve
    master "谢谢...."

    voice "audio/voice/master_20.mp3"
    master "--还有谢谢你今晚能留下来陪我"

    scene master_even
    show master_normal
    with dissolve
    master """
        有时候啊，
        我总觉得自己要同时撑两个世界——
        一个是现实的建筑图纸，
        一个是梦里的二次元。
        
        但今晚，我好像……
        终于平衡了一点点。
    """

    scene master_even
    "你没有说话,只是微笑着点了点头"

    show master_normal
    with dissolve
    master """
        走吧
    """

    voice "audio/voice/master_21.mp3"
    master "如果你回不去宿舍的话,我可是会内疚的哦"

    scene master_even0
    with fade
    "你们一同走出了教室"

jump dance_start     
