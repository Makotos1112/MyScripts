<?php

/* //////////////////////////////////////////////////////////

このファイルでは、Wordpressのテーマ「Cocoon」のカスタマイズアイデアを紹介しています。
各コードをfunction.phpの追記領域に貼り付けることで有効になります。

[Cocoon] Cocoonカスタマイズアイデア一覧 [Wordpress]
https://www.makotosblog.com/howto_cocoon_customize/

////////////////////////////////////////////////////////// */



//本文のタグを下部にも表示 //////////////////////////////////////////////////////////
//※「Cocoon設定」＞「投稿タブ」＞「カテゴリ・タグ表示設定」＞「カテゴリ・タグ表示位置」を「タイトル上」か「本文上」に設定しておく
function is_category_tag_display_position_content_bottom(){
  return true;
}


// タグクラウドの最大表示数を変更 //////////////////////////////////////////////////////////
//ウィジェット「タグクラウド」で一度に表示できるタグの数を変更する
function my_tag_cloud_number_filter($args) {
	$myargs = array(
		'number' => 30,
	);
	$args = wp_parse_args($args, $myargs);
	return $args;
}
add_filter('widget_tag_cloud_args', 'my_tag_cloud_number_filter');




//固定ページにカテゴリ導入 //////////////////////////////////////////////////////////
//投稿と同じカテゴリを固定ページでも設定できるようになります。
add_action( 'init', 'my_add_pages_categories' ) ; 
function my_add_pages_categories()
{
    register_taxonomy_for_object_type( 'category', 'page' ) ;
}
add_action( 'pre_get_posts', 'my_set_page_categories' ) ;
function my_set_page_categories( $query )
{
    if ( $query->is_category== true && $query->is_main_query()){
        $query->set( 'post_type', array( 'post', 'page', 'nav_menu_item' )) ;
    }
}

//ギャラリーのCSSを無効にする（CSSで自分で編集する設定) //////////////////////////////////////////////////////////
//ギャラリーのスタイルシート設定を無効化します。
 add_filter( 'use_default_gallery_style', '__return_false' );


//ユーザからは見えない非公開タグを作成する //////////////////////////////////////////////////////////
//管理者権限でログインしている時のみ表示されるタグを作成します。
//追加するときは || $tag->name=='名称'
function remove_admin_tags($tags,$tax=null,$args=null){
	if(!is_admin()){
		foreach($tags as $idx=>$tag){
			if($tag->name=='非公開タグA' || $tag->name=='非公開タグB' || $tag->name=='非公開タグC'){
				unset($tags[$idx]);
			}
		}
	}
	return($tags);
}
add_filter('get_terms','remove_admin_tags',10,3);
add_filter('get_the_terms','remove_admin_tags',10,3);



// contact form 7 の軽量化 ////////////////////////////////////////////////////////////////////
// contact form 7 のファイルを必要な場合だけ読み込むことで軽量化します。
function wpcf7_file_load() {
	add_filter( 'wpcf7_load_js', '__return_false' );
	add_filter( 'wpcf7_load_css', '__return_false' );
	if( is_page( 'foroverseas' ) || is_page( 'support' ) ){
		if ( function_exists( 'wpcf7_enqueue_scripts' ) ) {
			wpcf7_enqueue_scripts();
		}
		if ( function_exists( 'wpcf7_enqueue_styles' ) ) {
			wpcf7_enqueue_styles();
		}
	}
}
add_action( 'template_redirect', 'wpcf7_file_load' );


?>
