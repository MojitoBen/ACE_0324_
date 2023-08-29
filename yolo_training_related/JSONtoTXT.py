import json
import os
 
def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    x1 = box[0]
    y1 = box[1]
    x2 = box[2]
    y2 = box[3]
    return (x1, y1, x2, y2)
 
 
def decode_json(json_floder_path, json_name):
    txt_name = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel_txt/' + json_name[0:-5] + '.txt' 
    txt_file = open(txt_name, 'w')
 
    json_path = os.path.join(json_floder_path, json_name)
    with open(json_path, 'rb') as f:
        json_data = f.read().decode('utf-8', errors='ignore')
    data = json.loads(json_data)
    
 
    img_w = data['imageWidth']
    img_h = data['imageHeight']
 
    for i in data['shapes']:
 
        if i['label'] == 'steel':
            x1 = float((i['points'][0][0]))/img_w
            y1 = float((i['points'][0][1]))/img_h
            x2 = float((i['points'][1][0]))/img_w
            y2 = float((i['points'][1][1]))/img_h
 
            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write( 'steel' + " " + " ".join([str(a) for a in bbox]) + '\n')
        if i['label'] == 'sid':
            xx1 = float((i['points'][0][0]))/img_w
            yy1 = float((i['points'][0][1]))/img_h
            xx2 = float((i['points'][1][0]))/img_w
            yy2 = float((i['points'][1][1]))/img_h
 
            cc = (xx1, yy1, xx2, yy2)
            ccox = convert((img_w, img_h), cc)
            txt_file.write( 'sid' + " " + " ".join([str(a) for a in ccox]) + '\n')
 
 
if __name__ == "__main__":
 
    json_floder_path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel_json/'
    json_names = os.listdir(json_floder_path)
    for json_name in json_names:
        decode_json(json_floder_path, json_name)
