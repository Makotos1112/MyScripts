import tkinter as tk

import pyperclip

"""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
■使い方と注意点■
このファイルの使い方は下記のページで解説しています。

[Python] Wordpressのタグ打ちを楽にしてくれるツール [Wordpress]
: https://www.makotosblog.com/howto_addingtags/

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""


#表示させるボタンを管理する関数
def assort_categories():
    #配列と、配列の要素を増やすことでボタンを増設できます。

    #カテゴリA
    category_A = {'カテゴリA' :
        [
        "AAA-01",
        "AAA-02",
        "AAA-03",
        "AAA-04",
        "AAA-05",
        "AAA-06",
        "AAA-07",
        "AAA-08",
        "AAA-09",
        "AAA-10",
        ]
    }

    #カテゴリB
    category_B = {'カテゴリB' :
        [
        "BBB-01",
        "BBB-02",
        "BBB-03",
        "BBB-04",
        "BBB-05",
        "BBB-06",
        "BBB-07",
        "BBB-08",
        "BBB-09",
        "BBB-10",
        ]
    }

    #カテゴリC
    category_C = {'カテゴリC' :
        [
        "CCC-01",
        "CCC-02",
        "CCC-03",
        "CCC-04",
        "CCC-05",
        "CCC-06",
        "CCC-07",
        "CCC-08",
        "CCC-09",
        "CCC-10",
        ]
    }

    #ボタンを１つの配列に統合
    dict_categories = [ category_A, category_B, category_C]

    #各ボタンのカテゴリ名を配列で取得
    keys_categories = []
    for dict in dict_categories:
        for key in dict.keys():
            keys_categories.append(key)

    #カテゴリの数を取得
    length_categories = len(dict_categories)

    return dict_categories, keys_categories, length_categories


def adding_tags(array_categories, keys_categories, length_categories):
    root = tk.Tk()
    root.geometry("400x400+0+90") #GUIサイズ （横x縦+開始横座標+開始縦座標)
    root.title('タグ追加ツール') #タイトルバー

    #出力用の空配列
    array_output = []


    #クリックしたワード単体をクリップボードにコピーする
    def copy_single_word(event):
        event.widget.config(bg="pink")
        array_output.append(event.widget.cget("text")) #出力用配列に格納
        pyperclip.copy(event.widget.cget("text")) #クリップボードにコピー


    #クリックした複数のワードをクリップボードにコピーする
    def copy_multi_words(event):
        joined_result = ', '.join(array_output) #配列をカンマで区切って連結
        pyperclip.copy(joined_result) #クリップボードにコピー

        #実行後にGUIをリセットする
        array_output.clear() #配列を空にする
        for btn in array_button:
            btn.config(bg='lightblue')

    #クローズボタン
    def close():
        root.destroy()


    #copy_multi_wordsを実行するためのボタン配置
    btn_get = tk.Button(root, text = "実行", bg = "green", width = 5, font = ("", 10) )
    btn_get.grid(row = 0, column = 0, sticky = "ns")
    btn_get.bind("<ButtonPress>", copy_multi_words)



    # --- Frameの作成 ------------------------------------------------------
    dict_frame = {}
    #カテゴリーの数だけフレームを作成する
    for num in range(length_categories):
        dict_frame[num] = tk.LabelFrame(root,text=keys_categories[num],foreground="green")
        dict_frame[num].grid(row = 0, column = num+1, sticky = "n", padx=4)


    #ボタンを各フレームに配置する
    array_button = []
    for num in range(length_categories) :
        r = 0 #行 →
        c = 0 #列 ↓
        array_words = array_categories[num][keys_categories[num]]

        for word in array_words :
            # ボタンのインスタンス作成
            btn = tk.Button(dict_frame[num], text = word, anchor="w", bg = 'lightblue', width = 11, font = ("", 9, "bold"))
            array_button.append(btn)

            # ボタンを配置
            btn.grid(row = r, column = c, pady=2, padx=2)

            #ボタンが多い場合の改行設定
            T = 10 #改行変数
            r += 1
            if r % T == 0 :
                c += 1
                r = 0

            # ボタンクリック時のイベント設定
            btn.bind("<ButtonPress>", copy_single_word)


    #クローズボタン(GUIと画像を閉じる)
    btn_close = tk.Button(root, text='Exit',width = 5, height = 3, bg = 'magenta', command=lambda:close())
    btn_close.grid(row = 0, column = 0, sticky=tk.N)

    root.mainloop()



#### main関数でのファイル実行 #################################################
def main():
    array_categories, keys_categories, length_categories = assort_categories()
    adding_tags(array_categories, keys_categories, length_categories)

if __name__ == "__main__":
    main()
    print(f'※※※このスクリプトは{__name__}で実行されました。※※※')