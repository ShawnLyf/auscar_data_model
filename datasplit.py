import os
import shutil
from random import shuffle

data_dir = "auscar"
train_dir = os.path.join(data_dir, "train")
test_dir = os.path.join(data_dir, "test")

# Create train and test directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# List all directories within data directory
class_dirs = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d)) and d not in ["train", "test"]]

for class_dir in class_dirs:
    class_path = os.path.join(data_dir, class_dir)
    image_files = [f for f in os.listdir(class_path) if f.endswith(('.png', '.jpg', '.jpeg'))]  # add more extensions if needed
    
    # Shuffle the images
    shuffle(image_files)
    
    # Splitting index
    split_idx = int(0.7 * len(image_files))
    
    # Create train and test class directories
    train_class_dir = os.path.join(train_dir, class_dir)
    test_class_dir = os.path.join(test_dir, class_dir)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)
    
    # Move the images to respective directories
    for i, image_file in enumerate(image_files):
        source = os.path.join(class_path, image_file)
        if i < split_idx:
            dest = os.path.join(train_class_dir, image_file)
        else:
            dest = os.path.join(test_class_dir, image_file)
        shutil.move(source, dest)
