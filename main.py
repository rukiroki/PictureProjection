import uuid
import json
from PIL import Image
import shutil
import os
import tkinter
from tkinter import filedialog
def muuid():
    fn="resource/manifest.json"
    mfile=open(fn,"r+")
    manifest=json.loads(mfile.read())
    mfile.close()
    manifest["header"]["uuid"]=str(uuid.uuid4())
    manifest["modules"][0]["uuid"]=str(uuid.uuid4())
    print(uuid.uuid4())
    print(json.dumps(manifest))
    mfile=open(fn,"w+")
    mfile.write(json.dumps(manifest))
    mfile.close()
def is128(img_path):
    image=Image.open(img_path)
    width,height=image.size
    print(f"宽：{width}，高{height}")
    if width <= 2048 and height<=2048:
        return True
    else:
        return False
def importTexture(img_path):
    image=Image.open(img_path)
    image = image.convert("RGBA")

    alpha = int(255 * 0.8) 
    data = image.getdata()

    new_data = []
    for item in data:
        new_data.append((item[0], item[1], item[2], alpha))

    image.putdata(new_data)

    image.save("resource/textures/entity/picture.png")
def pack_icon(img_path):
    image=Image.open(img_path)
    width,height=image.size
    compressed_image = image.resize((int(width/16), int(height/16)))
    compressed_image.save('resource/pack_icon.png')
def uvmap(img_path):
    image=Image.open(img_path)
    width,height=image.size
    texture_width=width
    texture_height=height
    size1=[1024 if width>1024 else width,1,1024 if height>1024 else height]
    size2=[width-1024 if width>1024 else 0,1,1024 if height>1024 else height]
    size3=[1024 if width>1024 else width,1,height-1024 if height>1024 else 0]
    size4=[width-1024 if width>1024 else 0,1,height-1024 if height>1024 else 0]
    uv1=[1024 if width>1024 else width,1024 if height>1024 else height]
    uv2=[width if width>1024 else 1024,1024 if height>1024 else height]
    uv3=[1024 if width>1024 else width,height if height>1024 else 1024]
    uv4=[width if width>1024 else 1024,height if height>1024 else 1024]
    uv_size1=[-1024 if width>1024 else -width,-1024 if height>1024 else -height]
    uv_size2=[1024-width if width>1024 else 0,-1024 if height>1024 else -height]
    uv_size3=[-1024 if width>1024 else -width,1024-height if height>1024 else 0]
    uv_size4=[1024-width if width>1024 else 0,1024-height if height>1024 else 0]
    origin=[512-width-8+1024 if width>1024 else 512,0,-520]
    
    p01="resource/models/entity/armor_stand.ghost_blocks_p01.geo.json"
    p02="resource/models/entity/armor_stand.ghost_blocks_p02.geo.json"
    p03="resource/models/entity/armor_stand.ghost_blocks_p03.geo.json"
    p04="resource/models/entity/armor_stand.ghost_blocks_p04.geo.json"
    fp01=open(p01,"r")
    fp02=open(p02,"r")
    fp03=open(p03,"r")
    fp04=open(p04,"r")
    jp01=json.loads(fp01.read())
    jp02=json.loads(fp02.read())
    jp03=json.loads(fp03.read())
    jp04=json.loads(fp04.read())
    fp01.close()
    fp02.close()
    fp03.close()
    fp04.close()
    rtw=jp01["minecraft:geometry"][0]["description"]["texture_height"]
    jp01["minecraft:geometry"][0]["description"]["texture_height"]=texture_height
    jp02["minecraft:geometry"][0]["description"]["texture_height"]=texture_height
    jp03["minecraft:geometry"][0]["description"]["texture_height"]=texture_height
    jp04["minecraft:geometry"][0]["description"]["texture_height"]=texture_height
    jp01["minecraft:geometry"][0]["description"]["texture_width"]=texture_width
    jp02["minecraft:geometry"][0]["description"]["texture_width"]=texture_width
    jp03["minecraft:geometry"][0]["description"]["texture_width"]=texture_width
    jp04["minecraft:geometry"][0]["description"]["texture_width"]=texture_width
    jp01["minecraft:geometry"][0]["bones"][0]["cubes"][0]["size"]=size1
    jp02["minecraft:geometry"][0]["bones"][0]["cubes"][0]["size"]=size2
    jp03["minecraft:geometry"][0]["bones"][0]["cubes"][0]["size"]=size3
    jp04["minecraft:geometry"][0]["bones"][0]["cubes"][0]["size"]=size4
    jp01["minecraft:geometry"][0]["bones"][0]["cubes"][0]["uv"]["up"]["uv"]=uv1
    jp02["minecraft:geometry"][0]["bones"][0]["cubes"][0]["uv"]["up"]["uv"]=uv2
    jp03["minecraft:geometry"][0]["bones"][0]["cubes"][0]["uv"]["up"]["uv"]=uv3
    jp04["minecraft:geometry"][0]["bones"][0]["cubes"][0]["uv"]["up"]["uv"]=uv4
    jp01["minecraft:geometry"][0]["bones"][0]["cubes"][0]["uv"]["up"]["uv_size"]=uv_size1
    jp02["minecraft:geometry"][0]["bones"][0]["cubes"][0]["uv"]["up"]["uv_size"]=uv_size2
    jp03["minecraft:geometry"][0]["bones"][0]["cubes"][0]["uv"]["up"]["uv_size"]=uv_size3
    jp04["minecraft:geometry"][0]["bones"][0]["cubes"][0]["uv"]["up"]["uv_size"]=uv_size4
    jp02["minecraft:geometry"][0]["bones"][0]["cubes"][0]["origin"]=origin
    jp04["minecraft:geometry"][0]["bones"][0]["cubes"][0]["origin"]=origin
    fp01=open(p01,"w+")
    fp02=open(p02,"w+")
    fp03=open(p03,"w+")
    fp04=open(p04,"w+")
    fp01.write(json.dumps(jp01))
    fp02.write(json.dumps(jp02))
    fp03.write(json.dumps(jp03))
    fp04.write(json.dumps(jp04))
    fp01.close()
    fp02.close()
    fp03.close()
    fp04.close()
def compress():
    shutil.make_archive('archive', 'zip', 'resource')
    pack_name = 'Picture projection.mcpack'
    if os.path.exists(pack_name):
        os.remove(pack_name)
    os.rename("archive.zip",pack_name)
def main():
    print("请打开此网址生成一个最大宽高为128*128块的图片，然后下载，继续操作。https://autosaved.org/Spritecraft")
    print("请选择生成好的图片。")
    root = tkinter.Tk()
    root.withdraw()
    f_path = filedialog.askopenfilename()
    if is128(f_path):
        muuid()
        pack_icon(f_path)
        importTexture(f_path)
        uvmap(f_path)
        compress()
        print("生成完毕。")
    else:
        print("您生成的图片太大，请重新生成最大宽高为128*128块的图片。")
main()