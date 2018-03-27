import os
result=[]
def get_file(path):
    get_all=os.listdir(path)
    for i in get_all:
        
        judge=os.path.join(path,i)
        print(judge)
        if os.path.isdir(judge):
            get_file(judge)
        else:
            result.append(os.path.basename(judge))


if __name__ == "__main__":
        get_file("D:\\Github")
        print(len(result))
