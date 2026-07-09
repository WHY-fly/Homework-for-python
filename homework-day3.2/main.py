import argparse
from course_organizer.core import organize_files
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="自动整理课程资料的小工具")
    parser.add_argument("path", help="需要整理的文件夹路径")
    args = parser.parse_args()
    organize_files(args.path)