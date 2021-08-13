This project which depends on PhantomJS is used to download free comics from website
For reference and learning only, please do not use it for commercialization
===========================================================================
only on python 3.
===========================================================================
for easy to use so i made some encapsulation
===========================================================================

'update_src.bat' => download src only

'download_image.bat' => download image from update_src.bat

'mangabz_spider.conf' => to change which comic you want to download

===========================================================================
how to use=>
1. you need to write 'mangabz_spider.conf'

----------------------mangabz_spider.conf----------------------------------
name = 租借女友                               // <- comic_name
url = http://www.mangabz.com/279bz/         // <- comic_main_page(cut it until like this)
root_path = D:\\Comics\\                    // <- storage address(remember 2 '\' like '\\'
---------------------------------------------------------------------------
2. run update_src.bat when it run  a period of time time or it's done,then close it.
3. run download_image.bat
(two bat can't run at the same time, or there will be some bugs.Actually download_image.bat is faster )
