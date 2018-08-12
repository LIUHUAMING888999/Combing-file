import os

def file_name(file_dir,saveTxt):
    f = open(saveTxt, 'a',encoding='utf-8')
    num =0
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for name in files:
            print(name)
            num=num+1
            headlinestr = ['--------------------------------------------------------------------------\n']
            f.writelines(headlinestr)
            headstr = ['第',str(num),'个文件：' ,name,'\n']
            f.writelines(headstr)
            with open(os.path.join(root,name), 'r',encoding='utf-8') as file_to_read:
                lines = file_to_read.readlines()  # 整行读取数据
                # print(lines)
                f.writelines(lines)
                f.write("\n")
    f.close()





if __name__ == '__main__':

    file_name("src",'readResult.txt')