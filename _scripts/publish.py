import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--articletitle")
parser.add_argument("--genres")
parser.add_argument("--folder")
parser.add_argument("--articletype")
parser.add_argument("--author")
parser.add_argument("--publishdate")
parser.add_argument("--releasedate")
parser.add_argument("--gametitle")
parser.add_argument("--developer")
parser.add_argument("--publisher")
parser.add_argument("--tagline")
parser.add_argument("--tags")
parser.add_argument("--videoid")
args = parser.parse_args()

print('General Post Information')

article_title = args.articletitle
folder = args.folder
article_type = args.articletype
article_type_hyphen = '-'.join(article_type.split(' '))
article_type_comma = ', '.join(article_type.split(' '))
author = args.author or 'Brenda Zhang'
author_url = author.split(' ')[0].lower() or 'brenda'
date = args.publishdate
release_date = args.releasedate
game_title = args.gametitle
developer = args.developer
publisher = args.publisher
game_title_parts = game_title.split('-')
game_title_nospace = ''.join(game_title_parts)
game_title_nospace_caps = ''.join([w.capitalize() for w in game_title_parts])
game_title_space = ' '.join(game_title_parts)
game_title_space_caps = ' '.join([w.capitalize() for w in game_title_parts])
genres = args.genres
tagline = args.tagline
tags = args.tags
video_id = args.videoid

new_post = open('/Users/brendazhang/Desktop/projects/colludia/_posts/{folder}/{date}-{game_title}-{article_type_hyphen}.markdown'.format(
	article_type_hyphen = article_type_hyphen, date = date, folder = folder, game_title = game_title
), 'w+')
new_post.write('\
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
'.format(
	article_title = article_title,
	article_type = article_type,
	article_type_comma = article_type_comma,
	article_type_hyphen = article_type_hyphen,
	author = author,
	author_url = author_url,
	date = date,
	developer = developer,
	game_title = game_title,
	game_title_nospace = game_title_nospace,
	game_title_nospace_caps = game_title_nospace_caps,
	game_title_space = game_title_space,
	game_title_space_caps = game_title_space_caps,
	genres = genres,
	publisher = publisher,
	release_date = release_date,
	tagline = tagline,
	tags = tags,
	video_id = video_id
))
new_post.close()

if 'review' in article_type:
	print('Extra Quick Summary Information')

	main_character = input('Main character: ')
	platforms = input('Platforms: ') or 'PC'
	quote = input('Quote: ')
	recommended = input('Recommended: ') or 'Yes'
	thumbnail = input('Thumbnail: ')
	time_spent = input('Time spent: ')
	completion = input('Completion (%): ') or '100%'
	winning_traits = input('Winning traits: ')

	quick_summary = open('_data/post-quick-summary.yml', 'a+')
	quick_summary.write('\n\
	{game_title_nospace}:\n\
		quote: {quote}\n\
		image: post/{game_title_nospace}/{thumbnail}.png\n\
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
				answer:   {release_date}\n\
			- question: Time Spent\n\
				answer:   {time_spent}\n\
			- question: Completion\n\
				answer:   {completion}\n\
			- question: Winning Traits\n\
				answer:   {winning_traits}\n\
			- question: Recommended?\n\
				answer:   {recommended}\n\
	'.format(
		completion = completion,
		developer = developer,
		game_title_nospace = game_title_nospace,
		genres = genres,
		main_character = main_character,
		platforms = platforms,
		publisher = publisher,
		quote = quote,
		recommended = recommended,
		release_date = release_date,
		thumbnail = thumbnail,
		time_spent = time_spent,
		winning_traits = winning_traits,
	))
	quick_summary.close()
