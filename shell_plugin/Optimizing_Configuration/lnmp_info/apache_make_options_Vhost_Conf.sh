#!/bin/bash

##############################
#判断MAKE安装apache的vhost虚拟主机的配置文件,即包含有效的"</VirtualHost>"关键字的文件路径
##############################
updatedb

ENV_PATH="../env_config"

#注意主配置文件所在的路径不包含关键字："/etc/httpd/conf/httpd.conf" |"share"|"doc"|"ln*mp*"等

locate   "httpd.conf"  |  grep  -i  "\/conf\/httpd\.conf$" |  grep  -v  "\/etc\/httpd\/conf\/httpd.conf" |  grep  -vi "\/doc"  |  grep  -vi  "\/share\/"  |  grep -vi  "ln*mp*"  

#判断是否存在编译安装生成的httpd.conf文件，没有的话退出当前脚本
[  `echo  $?`  ==  0 ]   ||  exit  1

#定位主配置文件的路径
CONF=`locate   "httpd.conf"  |  grep  -i  "\/conf\/httpd\.conf$" |  grep  -v  "\/etc\/httpd\/conf\/httpd.conf" |  grep  -vi "\/doc"  |  grep  -vi  "\/share\/"  |  grep -vi  "ln*mp*"`
#定位安装目录
ServerRoot=`grep   -iw  "serverroot"   $CONF |  grep  -v  "^#"  |  awk  '{print $2}'  |  awk  -F  '"'  '{print  $2}'`

#判断httpd.conf中是否包含 "</VirtualHost>" 虚拟主机配置
grep -v  "^#"  $CONF  | grep  -i  "</VirtualHost>"
[ `echo  $?` == 0 ]  &&  echo  "$CONF"   >>   ./cache.tmp

#之后判断Include包含的文件中是否有"</VirtualHost>"虚拟主机配置
#将http.conf中Include包含的目录列表放到当前目录的include.tmp文件中
grep  -v  "^#"   $CONF  |  grep  -iw "^include"  | awk  '{print  $2}' >>  ./include.tmp

COUNT=`wc -l  include.tmp | awk  '{print $1}'`
	
#依次将include中的相对路径转换成绝对路径

for  ((i=1;i<=COUNT;i++))
do
	DIR=`sed  -n  ''$i',1p'   ./include.tmp  | grep  "^/"`
#根据返回值判断是绝对路径还是相对路径。返回值为0为绝对路径
	if [  `echo  $?` != 0 ]  
	then
			echo  $ServerRoot/$DIR   >>   include.tmp
	fi
done


#判断并删除cache.tmp中包含"*"号的行

COUNT=`wc -l  include.tmp | awk  '{print $1}'`

for  ((i=1;i<=COUNT;i++))
do
	sed  ''$i',1p'  include.tmp  |  grep  '*'
	if  [ `echo  $?` == 0 ]
	then
		ll  `sed  -n  ''$i',1p'  include.tmp`  |  awk  '{print  $9}'  >>  include.tmp
	fi
done

#删除include.tmp中的相对路径和包含"*"号的行
sed  -i  '/*/d'  include.tmp 

#删除include.tmp中的相对路径
sed  -i  '/^\//!d'   include.tmp 

#将包含关键字"</VirtualHost>"的文件路径存放到cache.tmp文件中

COUNT=`wc -l  include.tmp | awk  '{print $1}'`

for  ((i=1;i<=COUNT;i++))
do
	sed  ''$i',1p'  include.tmp  |  grep  -i  '</VirtualHost>'  |  grep  -v  "^#"
	if  [ `echo  $?` == 0 ]
	then
		sed  ''$i',1p'  include.tmp   >>  cache.tmp
	fi
done

#判断cache.tmp文件是否有内容，为空时退出当前脚本
[ `wc -l  cache.tmp | awk  '{print $1}'` > 0 ] ||  exit  1

#为cache.tmp中的每行路径加''单引号
sed  -i  "s/$/'/g"  cache.tmp 
sed  -i  "s/^/'/g"  cache.tmp 

#将回车换行符替换成","逗号
sed   -i    ':t;N;s/\n/,/;b t'  cache.tmp 

#添加"[]"
sed  -i  "s/$/]/g"  cache.tmp 
sed  -i  "s/^/[/g"  cache.tmp 

#查看"Make_Vhost_Conf"所在的行号
LINE_NUM=`grep  -n  "Make_Vhost_Conf"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Make_Vhost_Conf"行之后添加一行
sed  -ie  "/Make_Vhost_Conf/a \'Make_Vhost_Conf\':`cat  cache.tmp`" $ENV_PATH

#删除原来的"Make_Vhost_Conf"行
sed -i  ''$LINE_NUM'd'   $ENV_PATH
			
rm  -rf    ./cache.tmp
rm  -rf    ./include.tmp



			
