import shutil
from pathlib import Path
from .rules import EXTENSION_RULES
def organize_files(target_dir):
    base_path = Path(target_dir)
    if not base_path.exists() or not base_path.is_dir():
        print("错误：目标目录不存在或不是文件夹！")
        return
    for item in base_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            folder_name = EXTENSION_RULES.get(ext, '未分类文件')
            target_folder = base_path / folder_name
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_folder / item.name))
    print("文件自动整理完成！")
