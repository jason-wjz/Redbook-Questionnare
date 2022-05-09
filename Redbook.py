import streamlit as st      # import 完了之后直接填网页内容
import pandas as pd
import numpy as np
# streamlit 一次只能用一个

# -------小红书 APP调查问卷
st.set_page_config(page_title='小红书APP调查问卷', page_icon=':heart:')    # 网页名称设置，默认为本地脚本的名称（ local:host)

st.title(':rainbow:小红书APP对大学生及上班族旅游消费行为的影响调查问卷')  # 标题
st.write('使用小红书app的用户大家好！小红书作为一款当红app大家可以在在小红书社区通过文字、图片、视频笔记的分享，'
         '来记录这个时代年轻人的正能量和美好生活，而旅游作为一种享受生活的方式在小红书上的占比也是日益增加，下面我'
         '将对小红书app对大家的旅游前后的行为以及消费影响进行调查，希望大家能抽出宝贵的几分钟完成下面的问卷，谢谢大家！')  # 说明

with st.form('report'):         # 将整个页面做为一个 report
    sex = st.radio('1.性别', ['男', '女'])                                # 点击框 + 单选
    age = st.radio('2.你的年龄',['18~24岁', '25~31岁', '32~38岁'])
    salary = st.radio('3.你每个月生活费（工资）是多少？ （单位为元）',['2000以下', '2000-3000（不包括3000）',
                                         '3000-4000（不包括4000）', '4000-5000（不包括5000）',
                                         '5000及以上'])


    travel_cost = st.radio('4. 你每次的旅游花费是多少？（单位为元）',['1000以下', '1000-2000（不包括2000）',
                                      '2000-3000（不包括3000）', '3000-4000（不包括4000）', '4000及以上'])
    before_use_referrence = st.radio('5. 你在出游前会不会使用小红书攻略参考？',['一定使用（只要有出游想法就一定会用小红书）', '经常使用（大多数出游前都会参考小红书）',
                                      '偶尔使用（只有极小部分出游前参考）', '从不使用'])
    consideration = st.radio('6. 参考小红书来进行旅游，你更看重的是？',['查看小红书上的攻略后更省钱,省时', '能发现一些小众宝藏地',
                                      '自己没什么想法，需要依赖出行路线规划', '想打卡小红书上的博主去过的地方', '其他'])
    res_1, res_2, res_3, res_4, res_5 =[], [], [], [], []
    choices_1 = ['网红马路、打卡拍照（外滩、武康路等）', '美食探店', '物馆、艺术馆、展览', '公园等自然风光',
                 '主题乐园（迪士尼等）', '古镇、特色小镇', '体验馆（蜡像馆、星空馆等）', '其他文化场所（名人故居、历史建筑遗迹等）']

    st.write('7.你会根据小红书的推荐与分享去哪里玩？')
    for i in choices_1:
        if st.checkbox(i) == 1:
            res_1.append(i)                  # 点击框 + 多选
    if len(res_1) == 0:         # 检查是否填写
        error1 = 1
    else:
        error1 = 0
    rec_1 = '/'.join(res_1)

    eventual_as_referrence = st.slider('8.你最终的旅游行为有多大程度参考了小红书APP上的旅游信息？（参考程度从高到低）', min_value=1, max_value=5)        # 滑动条

    st.write('9. 小红书上旅游相关的笔记有哪些闪光点吸引你呢？')
    choices_2 = ['景点图片精美', '推荐人是好看的小哥哥小姐姐', '文字信息务实有用', '笔记是标题党设有悬念',
                 '图文排版设计感强', '短视频形式更加直观、吸引力强', '其他']
    for j in choices_2:
        if st.checkbox(j) == 1:
            res_2.append(j)
    if len(res_2) == 0:
        error2 = 1
    else:
        error2 = 0
    rec_2 = '/'.join(res_2)

    willing_cost = st.radio('10. 你会不会去小红书中推荐的网红店消费？',['从不消费', '偶尔消费', '经常消费'])
    feeling_cost = st.slider('11.你觉得小红书推荐的网红店消费体验感如何（信息真实度、性价比等等）', min_value=1, max_value=5)
    feeling_cost_after_use = st.radio('12. 在使用小红书后，你是否觉得自己的旅游消费增加了？',['使不使用小红书，旅游消费支出都差不多',
                                             '使用小红书后的旅游消费支出增多了', '使用小红书红的旅游消费支出减少了'])
    correspondence = st.slider('13. 目的地及相关消费的实际情况与小红书描述的符合程度如何？（有没有被照骗）', min_value=1, max_value=5)
    useful = st.slider('14. 小红书旅游相关笔记对你出游的有用程度是多少呢？（即你收到了多少干货）', min_value=1, max_value=5)
    travel_cost_feeling_after_use = st.slider('15. 你使用小红书进行旅游消费的满意度是多少分？', min_value=1, max_value=5)
    update = st.radio('16. 游玩后你是否会上传分享笔记或防雷吐槽至小红书呢？',['会', '不会'])

    choices_3 = ['编辑较为麻烦', '防止泄露个人隐私', '对某一景点体验一般、感触不深', '广告与用户推荐鱼龙混杂，不愿参与',
                 '不愿发表个人意见，以免产生分歧', '其他 ']
    st.write('17. 你不会上传分享推荐笔记或防雷吐槽的原因是？')
    for choice in choices_3:
        if st.checkbox(choice) == 1:
            res_3.append(choice)
    if len(res_3) == 0:
        error3 = 1
    else:
        error3 = 0
    rec_3 = '/'.join(res_3)

    choices_4 = ['p图过度，网红滤镜照骗', '广告泛滥', '信息复杂有用程度低', '不喜欢页面设计等',
                 '其他  ']
    st.write('18. 你最想吐槽小红书在旅游推荐上的什么雷点？')
    for x in choices_4:
        if st.checkbox(x) == 1:
            res_4.append(x)
    if len(res_4) == 0:
        error4 = 1
    else:
        error4 = 0
    rec_4 = '/'.join(res_4)

    choices_5 = ['景点图片美化过于严重，p图过度', '广告泛滥，多数与旅游内容无关', '信息价值不大（发布内容已经知道）', '网红博主存在虚假宣传，打广告等嫌疑',
                 '对小红书不了解，对其他APP信任度更高', '其他    ']
    st.write('19. 你抛弃小红书APP的原因是什么呢？')
    for y in choices_5:
        if st.checkbox(y) == 1:
            res_5.append(y)
    if len(res_5) == 0:
        error5 = 1
    else:
        error5 = 0
    rec_5 = '/'.join(res_5)

    advice = st.text_input('20.你对于小红书还有什么想要提出的建议或踩雷经历分享？')                            # 文本输入
    other_APP = st.text_input('21. 相较于小红书，请列举一下你所使用的其他同类旅游社区APP及其优势功能')          # 文本输入

    date = st.date_input('填写日期')       # 日期选择

    if st.form_submit_button('提交问卷'):   # 与开头的 st.form(key = 'report')对应，点了才提交表单
        if sum([error1, error2, error3, error4, error5]) == 0:      # 检查是否有未填写指标
            st.write('感谢您的参与！')
            data = pd.DataFrame([[sex, age, salary, travel_cost, before_use_referrence, consideration, rec_1,
                              eventual_as_referrence, rec_2, willing_cost,feeling_cost, feeling_cost_after_use,
                              correspondence, useful, travel_cost_feeling_after_use,
                              update, rec_3, rec_4, rec_5, advice, other_APP, date]],
                                columns=['sex','age','salary','travel_cost','before_use_referrence',
                                        'consideration','share','eventual_as_referrence','lighting point','willing_cost',
                                        'feeling_cost','feeling_cost_after_use','correspondence','useful','travel_cost_feeling_after_use',
                                        'update', 'update reason','dislike','dislike_reason','advice','other_APP','date'])
            st.balloons()
            data.astype(str).to_csv('./report_result.csv', encoding='utf-8-sig', mode='a')      # 文件名称， 编码（中文不用utf8会乱码）， 'a'追加（不然会覆写）
            with st.expander('是否查看数据'):     # 点击后展开的内容
                st.write('您的输入结果：')
                st.dataframe(data)
        else:
            st.write('您还有未填写的指标！')

# st.download_button('点此保存', data.to_csv().encode('utf-8'), file_name='report_result.csv', )
# st.download_button('点此下载数据', data)        # 下载数据

