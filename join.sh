#!/bin/bash
# 将安装文件封装到 .run 
# makeself命令的使用方法是: makeself  要压缩的目录  要做成的文件名  描述信息   第一个要执行的脚本
# 本脚本写好后，将要安装的文件或目录打包到 package.tgz ,然后执行： cat join.sh package.tgz > test.tgz , 如需加密可先对本脚本使用gzexe一遍
lines=8		#当前文件总行数+1
tail -n +$lines "$0" >test.tgz		#从脚本的第 $lines 行开始提取输出到 test.tgz
tar -xzvf test.tgz -C ./文档		#解压到目录
exit 0		# 这一行必须要，否则合并输出到新的 .run 文件时会继续执行压缩包出错

































