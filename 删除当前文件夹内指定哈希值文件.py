import os
import hashlib
import logging

def setup_logger():
    """设置日志记录器"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # 创建文件处理器并设置格式
    file_handler = logging.FileHandler('delete_files.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    
    return logger

def calculate_hash(file_path, hash_algorithm="md5", buffer_size=65536):
    """计算文件的哈希值"""
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            hash_func.update(data)
    return hash_func.hexdigest()

def delete_files_with_hash(target_hash, logger):
    """删除具有指定哈希值的文件"""
    current_directory = os.getcwd()
    for root, _, files in os.walk(current_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path).lower()
            if file_hash == target_hash.lower():
                os.remove(file_path)
                logger.info(f"Deleted file: {file_path}")

if __name__ == "__main__":
    # 设置日志记录器
    logger = setup_logger()
    
    # 手动输入要删除的目标哈希值
    target_hash_to_delete = input("Enter the target hash value to delete files: ").lower()

    # 删除具有指定哈希值的文件
    delete_files_with_hash(target_hash_to_delete, logger)

    print("Deletion completed.")
