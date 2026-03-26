import os
folder=r"C:\Users\ndfxt\Pictures\Camera Roll"
old_names=os.listdir(folder)
for i,old_name in enumerate(old_names,start=1):
    old_path=os.path.join(folder,old_name)
    num,houzhui=os.path.splitext(old_name)
    if os.path.isdir(old_path):
        continue
    new_name=f"{num}号照片.{houzhui}"
    new_path=os.path.join(folder,new_name)
    os.rename(old_path,new_path)

print("批量重命名完成！")