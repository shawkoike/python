# ライブラリのインポート
import matplotlib as plt
from wordcloud import WordCloud
import MeCab as mecab

def create_word_list(filepath):
    # ファイルをオープンする
    data = open(filepath, "r")
    # mecab のインスタンス生成
    m = mecab.Tagger ("-Ochasen")
    # 返却用変数
    word_list = []
    # 一行ずつ読み込む
    for line in data:
        # ノードの作成
        node = m.parseToNode(line)
        # ノード分回す
        while(node):
            # ヘッダーとフッターは空文字のため扱わない
            if len(node.surface) > 0:
                # 品詞が「動詞、形容詞、名詞、副詞」だったら
                if node.feature.split(",")[0] in ["動詞", "形容詞","名詞"]:
                    word_list.append(node.surface)
            # 次のノードに進める
            node = node.next
            # ノードが None 型だったらループから抜ける
            if node is None:
                break
    # 返却
    return word_list

def create_wordcloud(text):
    # フォントのパス
    fpath = "./ipam.ttc"
    # 除外ワード
    stop_words = ["いい", "感じ", "あっ", "使っ", "あり", "やっ", "する", "いる", "なっ", "でき", "よう", "てる", \
    "思っ", "さん", "こと", "ところ", "ため", "ところ", "みよ"]
    # wordCloud のインスタンス生成
    word_cloud = WordCloud(background_color="white", font_path=fpath, stopwords=set(stop_words), width=900, height=500).generate(text)
    # png ファイルに出力
    word_cloud.to_file("./result.png")


word_list = create_word_list("./data.txt")
create_wordcloud(text = ' '.join(word_list))