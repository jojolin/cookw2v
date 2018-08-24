# cook word2vec
- 开了个挖土机挖了接近70万+的菜谱，利用gensim训练了词向量
- 以下是一些稍微有点意思的同类词
- 可以到[这里](https://pan.baidu.com/s/13YELtCBZocbH3VQGPp-cfg)下载部分中间模型，最终模型暂时不予公开
- !! 你可以开挖土机(自备)去挖数据，然后接着训练模型

```
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "七夕"
remain len(unchecked): 210
cycle: ['七夕', '情人节', '情侣', '春意', '儿童节', 'Brunch', '悠然', '高逼格', '温情', '特饮', '圣诞节', '圣诞', '感恩节', '屋', '浪漫', '礼物', '主题', '伴手', '饕餮', '约会', '礼', '家庭主妇', '款待', '家居', '美食家', '春光', '微风', '禅意', '秋意', '掠过']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "礼物"
remain len(unchecked): 192
cycle: ['礼物', '公主', '情人节', '圣诞节', '七夕', '生日礼物', '宝贝儿', '玩具', '儿童节', '怀着', '萌', '欢乐', '怀旧', '狐狸', '厨娘', '圣诞', '感恩节', '屋', '浪漫', '主题', '中秋', '六一', '庆祝', '节日', '情侣', '春意', 'Brunch', '悠然', '高逼格', '温情']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "玫瑰花"
remain len(unchecked): 201
cycle: ['玫瑰花', '玫瑰', '花瓣', '菊花', '茉莉花', '花朵', '提子', '蓝莓', '山楂', '洛神', '桂花', '桑葚', '树莓', '黑加仑', '金桔', '花蕊', '花心', '树叶', '小花', '蝴蝶结', '帽子', '线条', '干花', '桑叶', '枸杞茶', '金银花', '形裱', '苞', '菊花茶', '茉莉']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "中秋"
remain len(unchecked): 181
cycle: ['中秋', '中秋节', '一年一度', '圣诞节', '临近', '今年', '国庆', '端午', '新年', '庆祝', '端午节', '元宵节', '中秋佳节', '清明节', '暑假', '除夕', '前夕', '转眼', '迎来', '元旦', '出门在外', '某日', '情人节', '感恩节', '儿童节', '主题', '圣诞', '六一', '节日', '每逢']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "月饼"
remain len(unchecked): 174
cycle: ['月饼', '冰皮', '蛋挞', '绿豆糕', '青团', '南瓜饼', '塔皮', '莲蓉', '菠萝包', '酥皮', '五仁', '枣泥', '麻薯', '皮料', '豆馅', '布丁', '挞', '苹果派', '蛋挞水', '蛋挞皮', '双皮奶', '牛轧糖', '豌豆黄', '桃酥', '冰糖葫芦', '奶黄包', '沙琪玛', '菠萝派', '小笼包', '叉烧包']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "青瓜"
remain len(unchecked): 165
cycle: ['青瓜', '黄瓜', '莴苣', '小黄瓜', '生菜', '苦菊', '莴笋', '卷心菜', '水萝卜', '苦苣', '海蜇', '火腿肠', '青笋', '西芹', '水芹', '芹菜', '茼蒿', '圆白菜', '高丽菜', '酸黄瓜', '洋菇', '胡瓜', '花枝', '青菜', '黄瓜片', '穿心莲', '豆苗', '豌豆苗', '茭白', '荷兰豆']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "起锅"
remain len(unchecked): 135
cycle: ['起锅', '出锅', '盛出', '乘出', '关火', '盛盘', '盛起', '装起', '出勺', '起油锅', '上桌', '上菜', '装盘', '出盘', '铲出', '后盛出', '成出', '铲起', '后盛起', '装出', '熄火', '停火', '开盖', '关火后', '离火', '揭盖', '装碟', '成盘', '装盆', '入盘']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "煎炸"
remain len(unchecked): 136
cycle: ['煎炸', '炸制', '炸', '煎炒', '煎制', '中火炸', '煎', '油炸', '翻炸', '炸熟', '炸至', '炸透', '炸成', '复炸', '先炸', '煸炒', '爆炒', '煸', '略炸', '炒制', '油煎', '烙制', '烙至', '烧制', '煎脆', '烙', '中炸', '油中炸', '锅中炸', '炕']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "搅拌"
remain len(unchecked): 143
cycle: ['搅拌', '搅打', '搅和', '翻拌', '搅', '打搅', '混合', '混拌', '搅匀', '调拌', '打', '打发', '抽打', '切拌', '搅合', '翻搅', '摇', '轻拌', '翻版', '压拌', '拌合', '搅动', '搅到', '搅伴', '刮拌', '抓拌', '混匀', '拌和', '调和', '混']
(nlp) jzlin@ubuntu1604:~/projects/cookw2v$ python cycle.py model/w2v.model_1808241042 30 0.5 "熄火"
remain len(unchecked): 175
cycle: ['熄火', '关火', '离火', '停火', '揭盖', '开盖', '关火后', '用余温', '盛起', '待凉', '出锅', '起锅', '盛出', '离火后', '起小泡', '降温', '关火放凉', '消失', '闭火', '放气', '再虚蒸', '虚蒸', '断电', '闷上', '掀盖', '闷', '泄压', '余温', '关火用', '余热']
```

## code usage

### train
  - require: gensim

  - init
    - `python w2v.py train data/t_data.json true model/w2v.model`

  - continue train
    - `python w2v.py train data/t_data.json false model/w2v.model_1808161311`

### evaluate
- `python evaluate.py simi model/w2v.model_1808161539 "七夕"`

### cycle
- `python cycle.py model/w2v.model_1808161539 20 0.5 "七夕"`
