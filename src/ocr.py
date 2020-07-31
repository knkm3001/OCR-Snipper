
from PIL import Image,ImageOps,ImageEnhance
import pyocr
import pyocr.builders
from io import BytesIO
import pyperclip

def ocr(binary_data,debugmode):

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    #print("Using '%s'" % (tools[0].get_name()))

    img = Image.open(BytesIO(binary_data))
    new_img = img.convert('L') \
                 .resize((int(img.width*2), int(img.height*2))) \
                 .point(lambda x: 0 if x < 80 else x)
    
    
    new_img = ImageEnhance.Sharpness(new_img).enhance(1.5) # 画像をシャープに
                
                 
                 


    if debugmode:
        new_img.save('./debug.png', quality=95)



    # 画像から日本語文字を読み取る
    text = tools[0].image_to_string(
        new_img,
        lang="jpn",                                             # 日本語を設定
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)  # 結果をテキストとして受け取る
    )
    print(text+'\n')
    pyperclip.copy(text)