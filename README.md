# Hello shiv

这是一个简单的 shiv 使用示例，可以将 python 代码打包成一个可以单独执行的文件。也就是会把依赖打包到一起，此时要注意二进制依赖。

掌握 shiv 打包，需要掌握以下 3 个要点

- import 机制
- setup.py 文件编写
- shiv 命令

相关知识可以查看 reference

## 体验

```sh
$ cd /path/to/hello-shiv
$ python setup.py bdist_wheel

# shiv 可以提前安装好 pip install shiv
$ shiv -p "/usr/bin/env python3.9 " -c helloshiv -o dist/helloshiv dist/hello-1.0-py3-none-any.whl

$ ./dist/helloshiv
# => hi, requests@[version]
```

有几个参数说明一下

- `-c` `entry_points` 配置，比如这个例子里面配置了一个 **helloshiv**
- `-p` 指名使用的解释器。也可以不知定，那么执行的时候需要带上解释器路径，比如 `python dist/helloshiv`

## reference

- https://shiv.readthedocs.io/en/latest/cli-reference.html#shiv
- https://github.com/creamidea/creamidea.github.com/issues/31
- [Python 库打包分发(setup.py 编写)简易指南](https://blog.konghy.cn/2018/04/29/setup-dot-py/)
- [花了两天，终于把 Python 的 setup.py 给整明白了](https://zhuanlan.zhihu.com/p/276461821)
- [Python 打包时添加非代码文件的坑](https://zhuanlan.zhihu.com/p/24312755)
