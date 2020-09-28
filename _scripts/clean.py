import re

folder_name = input('Folder name: ') or 'review'
file_date = input('File date (YYYY-MM-DD): ')
game_name = input('Hyphenated game name (venice-2089): ')
file_type = input('Hyphenated article type (demo-review): ')
file = '_posts/{folder_name}/{file_date}-{game_name}-{file_type}.markdown'.format(
  file_date = file_date,
  game_name = game_name,
  folder_name = folder_name,
  file_type = file_type
)

with open(file, 'r' ) as f:
  content = f.read()
  content_new = re.sub('!\[.*\].*', r'![][image0]', content, flags = re.M)
  f_out = open(file, 'w+')
  f_out.write(content_new)
  f_out.close()

game_name_parts = game_name.split('-')
game_title_nospace = ''.join(game_name_parts)
game_title_nospace_caps = ''.join([w.capitalize() for w in game_name_parts])

post = open(file, "a+")
post.write('\n\
[image0]: /images/post/{game_title_nospace}/{game_title_nospace_caps}0.png\n\
[image1]: /images/post/{game_title_nospace}/{game_title_nospace_caps}1.png\n\
[image2]: /images/post/{game_title_nospace}/{game_title_nospace_caps}2.png\n\
[image3]: /images/post/{game_title_nospace}/{game_title_nospace_caps}3.png\n\
[image4]: /images/post/{game_title_nospace}/{game_title_nospace_caps}4.png\n\
[image5]: /images/post/{game_title_nospace}/{game_title_nospace_caps}5.png\n\
[image6]: /images/post/{game_title_nospace}/{game_title_nospace_caps}6.png\n\
[image7]: /images/post/{game_title_nospace}/{game_title_nospace_caps}7.png\n\
[image8]: /images/post/{game_title_nospace}/{game_title_nospace_caps}8.png\n\
[image9]: /images/post/{game_title_nospace}/{game_title_nospace_caps}9.png\n\
[image10]: /images/post/{game_title_nospace}/{game_title_nospace_caps}10.png\n\
[image11]: /images/post/{game_title_nospace}/{game_title_nospace_caps}11.png\n\
[image12]: /images/post/{game_title_nospace}/{game_title_nospace_caps}12.png\n\
[image13]: /images/post/{game_title_nospace}/{game_title_nospace_caps}13.png\n\
[image14]: /images/post/{game_title_nospace}/{game_title_nospace_caps}14.png\n\
[image15]: /images/post/{game_title_nospace}/{game_title_nospace_caps}15.png\n\
'.format(
  game_title_nospace = game_title_nospace,
	game_title_nospace_caps = game_title_nospace_caps
))
