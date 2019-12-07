# -*- coding: utf-8 -*-
"""Episode: enjoy
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_handdistance(w: World):
    chi, ei = W(w.chisa), W(w.eisuke)
    return w.scene("手の届く距離で", "まだ二人は手の届く距離を歩いていた",
            chi.move(doing="歩いている"),
            chi.look("隣を歩く彼を"),
            chi.think("こんな風に帰れるなんてと"),
            ei.talk("ちょっと聞きたいんだが"),
            chi.look("彼は立ち止まりながら振り返り$meを"),
            ei.talk("好きな食べ物ってあるか"),
            chi.talk("好きは特別ないけど嫌いなら結構ある"),
            ei.talk("$meはグリンピースが駄目でさ、カレーとかピラフとかオムライスとかさ"),
            chi.talk("うんうん。わかる"),
            chi.think("同じポイントを見つけて嬉しいと"),
            ei.move(doing="歩き出す"),
            chi.move(doing="慌ててついていく"),
            chi.attention(),
            chi.look("彼の背中が近づいたり離れたりを繰り返すのを"),
            chi.think(doing="胸のどきどきを感じる"),
            # NOTE:
            #   手を繋げないまま、歩くが、互いに目を合わせたり、彼の話に適当に頷くのすら楽しい日々
            #   好きな食べ物の話なんかでも楽しい
            #   けれど尽く「合わない」
            camera=w.chisa,
            stage=w.stage.riverbed,
            day=w.day.enjoy1, time=w.time.afternoon,
            )

## episode
def ep_enjoytime(w: World):
    return w.episode("楽しかった頃", "まだあの頃は一緒に帰る道が楽しいばかりだった",
            sc_handdistance(w),
            )
