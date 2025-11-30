label school_start:
    scene school
    with fade

    play music "audio/music/schoolstartt.ogg" fadeout 1.0 fadein 1.0

    mc """
    苦了这么多年，终于上大学了啊，这安徽建筑大学的徽宏门还真是漂亮呢，报志愿的时候就被这个门给忽悠过来了

    大学生活就要开始了，真的是好期待啊
    """

    show all_schoolstart
    with dissolve
    mc "好漂亮的女孩啊，但是她好像在找什么东西"

    scene school
    mc "地上有个录取通知书，难道是她掉的？"

    "你走过去把录取通知书捡起来，准备还给她"

    show tzs
    mc "同学，你好，请问你是在找这个嘛"

    scene school
    show all_happy
    with dissolve
    voice "audio/voice/all_1.mp3"
    "???" "啊，真的是谢谢你了同学，帮大忙了"

    "你听着女孩声音久久没有反应"
    mc """
    (这个女孩子真可爱啊，和我暑假关注的up主长的好像啊)

    (等等，她好像也是这个学校的，不会是同一个人吧)

    同学，你......
    """

    voice "audio/voice/all_2.mp3"
    "???" "同学，谢谢你，但是我现在比较忙，下次有机会再好好感谢你"
    
    scene school
    show all_run:
        xpos 900
    with dissolve

    mc """
    估计她比较忙

    那个女孩子真温柔呢，运气真不错啊，开学第一天就看见这么漂亮的同学
    """

    scene kaixue
    "如此想着，你也走进学校，来到了土木工程专业的报道处，进行了报道"
    mc "果然学土木的人还是男生多啊"
    "此时，在后面的排队的人向你问道:"

    show classmate
    with dissolve
    cm "同学你好，我叫陈忽晚，你叫什么名字啊？"

    mc "我叫[povname]，很高兴认识你"

    cm "听说今天上午报道之后，下午就是领军训服了，到明天就要军训了，听学长说我们今年军训要21天呢"

    scene kaixue
    """
    两人左一句右一句的说来说去

    很快你也完成报道流程了，你向宿舍走去
    """

    mc "同学，我先去宿舍了，待会聊"

    show classmate
    with dissolve
    cm "好好，你先去吧，我待会就上去，我们应该也是室友"

    scene dorm

    mc "这就是四改六嘛，我18岁之前还没住过宿舍呢"

    """
    你选择了靠近阳台的床位

    很快宿舍六个人也到齐了，每个人选择了自己的床位，并收拾了下也就出宿舍了。

    直到下午领军训服才见面，几个人也是开始互相交流了解，约在晚上一起吃晚饭。

    第一天晚上，每个人都尽量克制自己刚上大学兴奋心情，因为第二天就要开始军训了。

    为期两周的军训也开始了，宿舍六人的关系也变得熟络起来。
    """

    scene junxun
    "三周后"

    show classmate_normal0:
        xpos 1000
        ypos 500
    with dissolve
    cm "喂，[povname]，晒了两个星期的大太阳也是要结束了，据说下午的时候社团会招新，你有没有想去参加的社团啊。"
    
    scene junxun
    mc """
    嗯....不出意外的话我应该就是去参加学校的动漫社了

    我还挺想了解下大学的动漫社是什么样子的，是不是和动漫里面的社团一样，还是有点期待的，哈哈

    你呢，你有什么想参加的社团嘛
    """

    show classmate_normal0:
        xpos 1000
        ypos 500
    with dissolve
    cm """
    我嘛？我现在也在考虑，不知道参加什么社团好啊

    大学的社团好多啊，不去参加是不是也可以啊
    
    我好累啊，好不容易才从高中毕业，来到大学我想歇一歇，不去参加这些活动
    """

    scene junxun
    mc "哈哈，这也挺好的"

    "两个人继续在操场讨论"

    "校长" "同学们，我们学校的军训闭幕式暨开学典礼到这里就结束了，你们的大学生活即将开始，恭喜你们，最后不要忘记下午的时候社团会招新。"


    jump league_start