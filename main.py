import os
import subprocess
import time


def execute_python_files_in_folder(folder_path):
    # 遍历指定文件夹内的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):  # 仅处理Python文件
                file_path = os.path.join(root, file)
                print(f"Executing {file_path}...")

                # 使用subprocess运行Python文件
                try:
                    subprocess.run(["python", file_path], check=True)
                    time.sleep(10)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing {file_path}: {e}")
                    time.sleep(10)

# 指定要执行的文件夹路径
folder_to_execute = "./100problems"

# 执行文件夹内的Python代码
execute_python_files_in_folder(folder_to_execute)
