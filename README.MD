# 从 Vote 迁移到 Obsidian, 图片引用的处理

## 背景

主要处理在 vote 中使用的对图片大小的控制,例如以下内容, 500 的大小设置在 Obsidian 中并不支持,需要移除掉

```
![](vx_images/20200314164218.png =500x)
```

修改为:

```
![](vx_images/20200314164218.png)
```

使用 Python 开发, 遍历指定文件夹下所有文件, 逐行扫描并修改.


## 如何使用

终端输入

```python
python3 replace.py
```
将需要处理的文件夹拖入即可.

或者,直接指定文件夹路径:

```python
python3 replace.py xx/xx/xx
```