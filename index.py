import cv2;
import os;

path = os.getcwd()
list_dir =  os.listdir(path);
print(list_dir)
# list_dir = ['Mel']
for folder in list_dir:
    currentFolderPath = os.path.join(path,folder);
    if(os.path.isdir(currentFolderPath)):
        for file in os.listdir(currentFolderPath):
            file_path =os.path.join(currentFolderPath,file);
            # C:\Users\91638\OneDrive\Desktop\IMG_CLASSES\Atopic Dermatitis
            os.chdir(r"c:/Users/91638/OneDrive/Desktop/IMG_CLASSES/"+folder);
            if(os.path.isfile(file_path)):
                img = cv2.imread(file_path); 
                imageName = file.split('.')[0];
                flippedImage = cv2.flip(img,0);
                flipped_1 = cv2.flip(img,1);
                flipped_neg_1 = cv2.flip(img,-1);
                cv2.imwrite(imageName +'_flipped.jpg', flippedImage);
                cv2.imwrite(imageName +'_flipped_1.jpg', flipped_1);
                cv2.imwrite(imageName +'_flipped_neg_1.jpg', flipped_neg_1);
                