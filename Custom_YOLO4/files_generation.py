import os

current_path = os.path.abspath(os.curdir)

COLAB_DARKNET_PATH = '/content/gdrive/MyDrive/Custom_YOLO4'

YOLO_FORMAT_PATH = current_path + '/custom'
COLAB_IMAGE_PATH = COLAB_DARKNET_PATH + '/dataset'

class_count = 0
test_percentage = 0.2
paths = []

if not os.path.exists('/content/custom'):
  os.makedirs('/content/custom')
  
# classes. names 파일 생성
with open(YOLO_FORMAT_PATH + '/' + 'classes.names', 'w') as names, \
     open(COLAB_DARKNET_PATH + '/dataset/' + 'classes.txt', 'r') as txt:
    for line in txt:
        names.write(line)  
        class_count += 1
    print ("[classes.names] is created")

# custom_data.data 파일 생성
with open(YOLO_FORMAT_PATH + '/' + 'custom_data.data', 'w') as data:
    data.write('classes = ' + str(class_count) + '\n')
    data.write('train = ' + COLAB_DARKNET_PATH + '/custom/' + 'train.txt' + '\n')
    data.write('valid = ' + COLAB_DARKNET_PATH + '/custom/' + 'test.txt' + '\n')
    data.write('names = ' + COLAB_DARKNET_PATH + '/custom/' + 'classes.names' + '\n')
    data.write('backup = backup')
    print ("[custom_data.data] is created")

os.chdir(COLAB_IMAGE_PATH)
for current_dir, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.jpg'):
            image_path = COLAB_DARKNET_PATH + '/dataset/' + f
            paths.append(image_path + '\n')

paths_test = paths[:int(len(paths) * test_percentage)]

paths = paths[int(len(paths) * test_percentage):]

# train.txt 파일 생성
with open(YOLO_FORMAT_PATH + '/' + 'train.txt', 'w') as train_txt:
    for path in paths:
        train_txt.write(path)
    print ("[train.txt] is created")

# test.txt 파일 생성
with open(YOLO_FORMAT_PATH + '/' + 'test.txt', 'w') as test_txt:
    for path in paths_test:
        test_txt.write(path)
    print ("[test.txt] is created")

