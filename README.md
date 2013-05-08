关于 goo
======

goo 是一个终端下基于 SSH 的用来登录服务器的工具。
可记住主机的登录信息，也可给主机增加别名。后续登录可直接使用别名，方便管理。


LICENSE
-------

MIT


安装
-----

将 `goo` 文件放置到 `/usr/local/bin` 路径下 (或任何 `$PATH` 中的目录) 即可。


使用
----

#### 1. 登录

* 首先用完整信息登录一次主机:

        $ goo [host] [user] [password]

    需要指明 key 的:

        $ goo -k your_key_path [host] [user]

    登录过一次之后，goo 便会记录下该主机登录信息，后续登录可直接使用主机名:

        $ goo [host]


* 当然，还可以更简单一些：使用**别名**登录。

    给曾登录过的主机增加别名:

        $ goo [host] -a [alias]

    之后便可以直接使用别名了:

        $ goo [alias]

#### 2. 查看主机

    $ goo -l

#### 3. 删除

* 删除别名:

    $ goo -d [alias]

* 删除主机 (同时会删除别名):

    $ goo -d [host]
