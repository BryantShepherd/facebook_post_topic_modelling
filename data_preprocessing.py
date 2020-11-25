from os import sep
import pandas as pd
import re

# Import Vietnamese stop words
# with open("./vietnamese-stopwords.txt", "r") as reader:
#     content = reader.readlines()
#     stopwords = [ x.strip() for x in content ]

def formatString(inputStr):
    """ Format given string """
    resultStr = inputStr
    resultStr = resultStr.lower()
    resultStr = re.sub(u"[^a-zA-ZÀÁÂÃÈÉÊẾÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽếềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵýỷỹ]", " ", resultStr)
    return resultStr


df = pd.read_csv("./topic_detection_clean.csv", sep='\t', header=None, names=['label', 'text'], dtype={ 'label': str, 'text': str})

df['text'] = [ formatString(val) for val in df['text']]

df.to_csv("./tdc.csv", sep='\t')