import os
import re
import sys

# 处理 MD 文件
def process_md_file(file_path):
    # 打开文件并读取每一行
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        # 去掉两端的空白字符
        # line = line.strip()
        pattern = r"(\!\[\]\(vx_images/([0-9]*).(png|jpg)) =([0-9]*x\))"
        result = re.match(pattern, line)
        if result:
            # print("0:", result.group(0)) # 使用 group 方法获取第一个分组
            # print("1:", result.group(1)) # 使用 group 方法获取第一个分组
            # print("2:", result.group(2)) # 使用 group 方法获取第二个分组
            line = result.group(1) + ")\n"
            # print(f"匹配成功: {line}")

        new_lines.append(line)

    # 写入新文件
    with open(file_path, "w", encoding="utf-8") as f:
        for line in new_lines:
            # f.write(line + "\n")    
            f.write(line) 


def main():
    dir_path = ""
    if len(sys.argv) < 2:
        # print(f"请指定相关目录, 例如: python3 replace.py /xxx/xxx/xx/")
        # return None
        dir_path = input("请指定要处理的相关目录:")
        if (len(dir_path) <= 0):
            print("未指定目录, 程序退出!")
            return
    else:
        # 接收指定的目录
        dir_path = sys.argv[1]    

    # 移除掉前后的 '
    dir_path = dir_path.strip("'")
    print(f"指定的路径是: {dir_path}")
    # 遍历目录下的所有子目录和文件
    for root, dirs, files in os.walk(str(dir_path)):
        for file in files:
            if file.endswith(".md"):
                # # 获取完整的文件路径
                file_path = os.path.join(root, file)
                # print(f"file_path: {file_path}")
                # 递归调用 process_md_file 函数，并将结果添加到原始列表中
                lines = process_md_file(file_path)
                print(f"Processing {file_path}...")
                # print(lines)

if __name__ == "__main__":
    main()
