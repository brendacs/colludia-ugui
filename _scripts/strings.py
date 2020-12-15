FRONT_MATTER = '\
---\n\
pageType: post\n\
game: {game_title_nospace}\n\
slug: /{game_title}-{article_type_hyphen}/\n\
title: "{article_title} <em class=\'game-title\'>{game_title_space_caps}</em>"\n\
postType: [{article_type_comma}]\n\
tagline: "{tagline}"\n\
date: {date}\n\
release-date: {release_date}\n\
image: {game_title_nospace_caps}.png\n\
video: https://www.youtube.com/embed/{video_id}\n\
author: {author}\n\
categories: [{genres}, {article_type_comma}, story]\n\
tags: ["{game_title_space_caps}", "{developer}", "{publisher}", {tags}]\n\
---\
'

QUICK_SUMMARY = '\n\
{game_title_nospace}:\n\
	quote: {quote}\n\
	image: post/{game_title_nospace}/{thumbnail}\n\
	points:\n\
		- question: Genre\n\
			answer:   {genres}\n\
		- question: Developer\n\
			answer:   {developer}\n\
		- question: Publisher\n\
			answer:   {publisher}\n\
		- question: Main Character\n\
			answer:   {main_character}\n\
		- question: Platforms\n\
			answer:   {platforms}\n\
		- question: Release Date\n\
			answer:   {release_date_verbose}\n\
		- question: Time Spent\n\
			answer:   {time_spent}\n\
		- question: Completion\n\
			answer:   {completion}\n\
		- question: Winning Traits\n\
			answer:   {winning_traits}\n\
		- question: Recommended?\n\
			answer:   {recommended}\n\
'

POST_IMAGES = '\n\
[image0]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}0.png\n\
[image1]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}1.png\n\
[image2]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}2.png\n\
[image3]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}3.png\n\
[image4]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}4.png\n\
[image5]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}5.png\n\
[image6]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}6.png\n\
[image7]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}7.png\n\
[image8]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}8.png\n\
[image9]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}9.png\n\
[image10]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}10.png\n\
[image11]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}11.png\n\
[image12]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}12.png\n\
[image13]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}13.png\n\
[image14]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}14.png\n\
[image15]: ../../../images/post/{game_title_nospace}/{game_title_nospace_caps}15.png\n\
'
