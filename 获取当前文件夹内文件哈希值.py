# -*- coding: utf-8 -*-
import os
import hashlib
import csv

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def list_files(start_path):
    file_list = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            sha256 = calculate_sha256(file_path)
            file_list.append((file, sha256, file_path))
    return file_list

def export_to_csv(file_list, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:  # 在 Python 3.x 中使用 'w'，并指定编码和换行
        csv_writer = csv.writer(f)
        csv_writer.writerow(['文件名称', 'SHA-256', '文件路径'])
        for row in file_list:
            csv_writer.writerow(row)

if __name__ == "__main__":
    start_path = '.'  # 当前文件夹
    csv_file = '1.csv'
    files = list_files(start_path)
    export_to_csv(files, csv_file)
    print("SHA-256 值已计算并导出至", csv_file)
