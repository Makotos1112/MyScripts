import glob
import os
from pathlib import Path
import shutil
from tkinter import filedialog

import ffmpeg
import tqdm


"""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
■使い方と注意点■
このファイルの使い方は下記のページで解説しています。

[Python] 複数の動画をまとめて短く切り取る方法 [Twitter]
https://www.makotosblog.com/howto_shortmovie/

30行目：実行対象の拡張子を.mp4に設定していますが、変更でその他にも対応可能です。
75行目：引数を変更することで切り取るタイミング(開始からの秒数)を変更できます。

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""

#参照フォルダの選択(動画単体ではなくフォルダ指定して実行)
def select_dir_movies() :
    def_dir_source = r"C:\\"
    dir_source = filedialog.askdirectory(initialdir = def_dir_source)
    source_movies = fr'{dir_source}\*.mp4'

    #取得した動画を配列に格納
    movies = []
    for movie in glob.glob(source_movies):
        movies.append([movie, Path(movie).stem])
    return movies


#出力先フォルダの選択
def select_dir_output() :
    def_dir_destination = r"C:\\"
    dir_destination = filedialog.askdirectory(initialdir = def_dir_destination)
    return dir_destination


#取得した動画からショートムービーを作成 引数で秒数を設定。
def create_short_movie(movies, dir_destination, time):
    total_target_num = len(movies)
    comment = ""
    success_count = 0
    skip_count = 0
    copy_count = 0
    failure_count = 0

    #tqdmモジュールで進捗バーを表示
    for target in tqdm.tqdm(movies):
        probe = ffmpeg.probe(target[0])
        video_len_sec = float(probe['format']['duration'])

        if not os.path.isfile(fr'{dir_destination}\{target[1]}_short_{time}sec.mp4'): #ショートがまだ作成済みでない場合
            if video_len_sec < 120: #動画時間がtime秒以下なら加工せずにリネームコピーする
                shutil.copyfile(target[0], fr'{dir_destination}\{target[1]}_short_{time}sec.mp4')
                comment += f"\n COPY : 「{target[1]}」冒頭{time}秒 のリネームを作成しました。"
                copy_count += 1
            else: #未作成かつ動画時間がtime秒より長ければ
                try: #ショート動画を作成実行
                    video = ffmpeg.input(target[0], ss=0, t=time).output(fr'{dir_destination}\{target[1]}_short_{time}sec.mp4')
                    ffmpeg.run(video, quiet=True)
                    comment += f"\n SUCCESS : 「{target[1]}」冒頭{time}秒 のショートコピーを作成しました。"
                    success_count += 1
                except Exception:
                    comment += f"\n FAILURE : 「{target[1]}」冒頭{time}秒 のショートコピー作成に失敗しました。"
                    failure_count += 1
        else:
            comment += f"\n SKIP : 「{target[1]}_short_{time}sec.mp4」 は作成済みによりスキップしました。"
            skip_count += 1
            continue

    comment += f"""

    ■作業完了■ {total_target_num}件中
    切り取り完了 :  {success_count}
    コピー({time}秒以下) :  {copy_count}
    スキップ(スキップ) :  {skip_count}
    切り取り失敗 :  {failure_count}
    """
    return comment

#作業結果をテキストファイル出力
def output_text(dir_destination, comment):
    txt = open(f'{dir_destination}/result.txt', 'w')
    txt.write(f'{comment}')
    txt.close()



#### main関数でのファイル実行 #################################################
def main():
    movies = select_dir_movies()
    dir_destination = select_dir_output()
    comment = create_short_movie(movies, dir_destination, 120)
    output_text(dir_destination, comment)

if __name__ == "__main__":
    main()
    print(f'※※※このスクリプトは{__name__}で実行されました。※※※')