# -*- coding: utf-8 -*-
"""Story config.
"""


################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) CHARAS <- duplicated
# 2) STAGES
#       舞台基本設定
# 3) DAYS
#       年月日設定
# 4) TIMES
#       時間帯基本設定
# 5) ITEMS
#       小道具設定
# 6) WORDS
#       辞書設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("chisa", "千紗", "西村,千紗", 17,(1,1), "female", "高校二年", "me:私"),
        ("eisuke", "英輔", "中山,英輔", 17,(1,1), "male", "高校二年", "me:俺"),
        ("miyo", "美代", "田中,美代", 17,(1,1), "female", "高校二年"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("riverbed", "河川敷"),
        ("crossroad", "交差点"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("first", "付き合い始めの日", 5,31, 2019),
        ("enjoy1", "楽しい日々１", 7,10, 2019),
        ("disquiet1", "不穏1", 10,11, 2019),
        ("disquiet2", "不穏2", 10,25, 2019),
        ("depart", "別れの日", 11,25, 2019),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        ("line", "ＬＩＮＥ"),
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Except / Type
        )

LAYERS = (
        # Key / Title / Words
        )

