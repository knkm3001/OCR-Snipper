
from PIL import Image,ImageOps,ImageEnhance
import pyocr
import pyocr.builders
from io import BytesIO
import pyperclip

import requests
import json
import base64

import env

Google_API_Kye = env.Google_API_Kye


def ocr(img_bin,debugmode,ocr_eng='tesseract'):
    """ ocr """

    new_img = imgPross(img_bin,debugmode)

    print('ocr_eng',ocr_eng)

    if ocr_eng == 'gcv':
        text = ocr_by_gcv(new_img)
    else:
        text = ocr_by_tesseract(new_img)
    
    print('===================================================\n')
    print(text+'\n')
    pyperclip.copy(text)


def imgPross(img_bin,debugmode):
    """ 画像加工 """
    
    img = Image.open(BytesIO(img_bin))
    # グレスケ、4倍、2値化
    new_img = img.convert('L') \
                 .resize((int(img.width*2), int(img.height*2))) \
                 .point(lambda x: 0 if x < 80 else x)
    new_img = ImageEnhance.Sharpness(new_img).enhance(1.5) # 画像をシャープに
    if debugmode:
        new_img.save('./debug.png', quality=95)

    return new_img


def ocr_by_tesseract(new_img):
    """ tesseractによるOCR """

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    text = tools[0].image_to_string(
        new_img,
        lang="jpn",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )

    return text

def ocr_by_gcv(new_img):
    """ Google Cloud Vision によるOCR """

    output = BytesIO()
    new_img.save(output, format='PNG')
    new_img_bin = output.getvalue()
    image_base64 = base64.b64encode(new_img_bin).decode('utf-8')

    #print(image_base64)

    api_url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(Google_API_Kye)
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_base64
            },
            'features': [{
                'type': 'TEXT_DETECTION'
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    res_json = res.json()
    
    text = res_json["responses"][0]["textAnnotations"][0]["description"]

    return text

