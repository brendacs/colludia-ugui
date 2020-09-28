FRONT_MATTER = '\
---\n\
layout:       post\n\
game:         {game_title_nospace}\n\
permalink:    /{game_title}-{article_type_hyphen}/\n\
tab-title:    "{article_title}"\n\
title:        "{article_title} <em class=\'game-title\'>{game_title_space_caps}</em>"\n\
type:         [{article_type_comma}]\n\
desc:         "{game_title_space_caps} {article_type}: {tagline}"\n\
tagline:      "\\\"{tagline}\\"\"\n\
date:         {date}\n\
release-date: {release_date}\n\
image:        {game_title_nospace_caps}.png\n\
video:        https://www.youtube.com/embed/{video_id}\n\
author:       {author}\n\
author-url:   {author_url}\n\
categories:   [{genres}, {article_type_comma}, story]\n\
tags:         ["{game_title_space_caps}", "{developer}", "{publisher}", {tags}]\n\
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
