# 从 Vote 迁移到 Obsidian, 图片引用的处理

主要处理在 vote 中使用的对图片大小的控制,例如一下内容,在 Obsidian 中并不支持,需要移除掉

```
![](vx_images/20200314164218.png =500x)
```

修改为:

```
![](vx_images/20200314164218.png)
```

使用 Python 开发, 遍历指定文件夹下所有文件, 逐行扫描并修改.