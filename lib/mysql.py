#函数名
#函数功能描述
#支持的操作系统
#函数实现方式描述
#函数参数定义
#函数的输出

###############查找类函数##############
#函数名:find_mysql
#函数功能描述:查找mysql的安装路径，确认mysql是否加到了/etc/init.d下面
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:mysqld_safe的位置


#函数名:find_my_cnf
#函数功能描述:查找mysql的配置文件my.cnf
#支持的操作系统:CentOS
#函数实现方式描述:在/etc目录下查找my.cnf文件
#函数参数定义:
#函数的输出:my.cnf的位置

#函数名:find_mysql_data_path
#函数功能描述:查找mysql的数据目录的位置
#支持的操作系统:CentOS
#函数实现方式描述:在my.cnf文件中查找数据目录的位置
#函数参数定义:
#函数的输出:mysql数据目录的位置


#########检测类函数####################
#函数名:detec_mysql_install
#函数功能描述:检测mysql是否安装了
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:是或否

#函数名:detec_mysql_install_way
#函数功能描述:检测mysql的安装方式
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:yum apt-get make


#函数名:detec_mysql_listen
#函数功能描述:检测mysql监听的端口
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:端口号


#函数名:detec_mysql_slow_query
#函数功能描述:检测mysql是否开启了慢查询
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:启用了或未启用

#函数名:detec_mysql_bad_table
#函数功能描述:检测mysql中是否存在怀表
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:是或否，表的名称


#############mysql安装类函数############

#函数名:install_yum_mysql
#函数功能描述:yum方式安装mysql
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置


#函数名:install_apt_mysql
#函数功能描述:apt-get方式安装mysql
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置


#函数名:install_make_mysql
#函数功能描述:make方式安装mysql
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置

