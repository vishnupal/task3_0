import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras.optimizers import RMSprop
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Input
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.models import Model
count =0
from keras.models import load_model
def run(ep):
    
    m = load_model('my.h5')
    for  layer in m.layers:
        layer.trainable = False
    top_model = m.input
    print(count)
    top_model1=m.output
    
    conv1 = Conv2D(63, kernel_size=4, activation='relu',name="dense_"+str(count+1))(top_model)
    pool1 = MaxPooling2D(pool_size=(2, 2),name="dense_"+str(count+2))(conv1)
    conv2 = Conv2D(7, kernel_size=4, activation='relu',name="dense"+str(count+3))(pool1)
    pool2 = MaxPooling2D(pool_size=(2, 2),name="dense"+str(count+4))(conv2)
    flat = Flatten()(pool2)
    hidden1 = Dense(3, activation='relu',name="dense"+str(count+5))(top_model1)
    output= Dense(1, activation='sigmoid',name="dense"+str(count+6))(hidden1)
    m = Model(inputs=top_model, outputs=output)
    
    m.compile(optimizer = "adam", loss='binary_crossentropy', metrics=['accuracy'])
    from keras_preprocessing.image import ImageDataGenerator
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)
    training_set = train_datagen.flow_from_directory(
            '/home/cnn_dataset/training_set/',
            target_size=(64, 64),
            batch_size=32,
            class_mode='binary')
    test_set = test_datagen.flow_from_directory(
            '/home/cnn_dataset/test_set/',
            target_size=(64, 64),
            batch_size=32,
            class_mode='binary')
    acc=m.fit(
            training_set,
            steps_per_epoch=12000,
            epochs=ep,
            validation_data=test_set,
            validation_steps=800)
    m.save('my.h5')
    return float(acc.history['val_accuracy'][-1])*100
ep=2



try:
    fi=open("/home/count.txt","r")
    count=fi.read()
    count=float(count)
    
    fi.close()
except:
    count =0
try:
    file=open("/home/accuracy.txt","r")
    aa=file.read()
    aa=float(aa)
except:
    aa = 0

print(count)
print(aa)
while aa<=50:
    aa=run(ep)
    file=open("/home/accuracy.txt","w")
    file.write("%f"%(aa))
    file.close()
    print(aa)
    ep+=2
    count+=7
    fi=open("/home/count.txt","w")
    fi.write("%f"%(count))
    fi.close()
    
    
    
    
else:
    file=open("/home/accuracy.txt","w")
    file.write("%f"%(aa))
    count+=7
    fi=open("/home/count.txt","w")
    fi.write("%f"%(count))
    fi.close()
    

    os.system("curl -I POST -u admin:redhat http://192.168.43.151:8080/job/job5/build?token=redhat")

