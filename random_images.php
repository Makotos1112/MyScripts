<?php

/*
///////////////////////////////////////////////////////////////////////////////

■使い方と注意点■
このファイルの使い方は下記のページで解説しています。

[WordPress] 画像をランダムに任意の数表示させる方法 [PHP]
https://www.makotosblog.com/howto_randomimages/

コード中の●●●という箇所を環境に合わせて書き換えてください。
使用している画像は "sample_images" というフォルダに入っています。


このコードの複製は流用は自由ですが、生じうるいかなる問題について制作者は責任を負いません。

///////////////////////////////////////////////////////////////////////////////
*/


///ランダム画像出力////////////////////////////////
function random_image( $atts ) {

    //何枚出力させるかを決める引数
   $num = $atts['num'];

   //用意した画像から配列を作成
   $images = array(
       '01_White' => 'https://●●●/sample_01.jpg',
       '02_Black' => 'https://●●●/sample_02.jpg',
       '03_Red' => 'https://●●●/sample_03.jpg',
       '04_Orange' => 'https://●●●/sample_04.jpg',
       '05_Yellow' => 'https://●●●/sample_05.jpg',
       '06_Green' => 'https://●●●/sample_06.jpg',
       '07_Light Blue' => 'https://●●●/sample_07.jpg',
       '08_Blue' => 'https://●●●/sample_08.jpg',
       '09_Purple' => 'https://●●●/sample_09.jpg',
       '10_Gray' => 'https://●●●/sample_10.jpg',
       );

   //numの引数が1の場合でも配列に格納させる
   if ( $num == 1) {
       $randkeys = [array_rand( $images, $num)];
   } else {
       $randkeys = array_rand( $images, $num);
   }


   //配列の並びをシャッフル
   shuffle($randkeys);
   
   //画像を横並びにするためにflexのdivタグを用意する
   //flexboxのスタイルとrow wrapで画像を回り込み表示にする
   $opening_tag = "<div style=\"display: flex; flex-flow: row wrap;\">";
   $closing_tag = "</div>";

   //foreachで各画像からimageタグを生成する
   foreach( $randkeys as $color ) {
       $image = $images[$color];
       $tag .= "<img class=\"aligncenter size-medium\" src=\"${image}\" alt=\"${color}\" width=\"200\" height=\"120\">";
   }

   //作成した画像をdivタグで囲んで完成
   $content = $opening_tag .= $tag .= $closing_tag;
   
   return $content;
}

//並べたい数で出力する
add_shortcode('random_image', 'random_image');


///ランダム画像出力_json//////////////////////////
function random_image_json( $atts ) {

    //何枚出力させるかを決める引数
   $num = $atts['num'];

   //出力サイズを決める変数
   $width = $atts['width'];
   $height = $width * 5 / 8 ; //高さは幅から自動計算

   //jsonファイルのパスを変数に代入
   $url = "https://●●●/sample_images.json";

   //ファイルの内容を文字列として読み込む
   //文字コードをUTF-8に変換
   //jsonをphpの連想配列に変換
   $json = file_get_contents($url);
   $json = mb_convert_encoding($json, 'UTF8', 'ASCII,JIS,UTF-8,EUC-JP,SJIS-WIN');
   $images = json_decode($json,true);


   //numの引数が1の場合でも配列に格納させる
   if ( $num == 1) {
       $randkeys = [array_rand( $images, $num)];
   } else {
       $randkeys = array_rand( $images, $num);
   }


   //配列の並びをシャッフル
   shuffle($randkeys);
   
   //画像を横並びにするためにflexのdivタグを用意する
   //flexboxのスタイルとrow wrapで画像を回り込み表示にする
   $opening_tag = "<div style=\"display: flex; flex-flow: row wrap;\">";
   $closing_tag = "</div>";

   //foreachで各画像からimageタグを生成する
   foreach( $randkeys as $color ) {
       $image = $images[$color];
       $tag .= "<img class=\"aligncenter size-medium\" src=\"${image}\" alt=\"${color}\" width=\"${width}\" height=\"$height\">";
   }

   //作成した画像をdivタグで囲んで完成
   $content = $opening_tag .= $tag .= $closing_tag;
   
   return $content;
}

//並べたい数で出力する
add_shortcode('random_image_json', 'random_image_json');



 ?>