import cv2
import numpy as np
import os
import random
import shutil

def augment_dataset(num_images=100):
    base_img_path = "dataset/images/train/drone-debris.jpg"
    base_lbl_path = "dataset/labels/train/drone-debris.txt"
    
    img = cv2.imread(base_img_path)
    with open(base_lbl_path, "r") as f:
        labels = [line.strip().split() for line in f.readlines()]
    
    print(f"Generating {num_images} augmented images...")
    
    for i in range(1, num_images + 1):
        aug_img = img.copy()
        new_labels = []
        
        # 1. Random Brightness and Contrast
        alpha = random.uniform(0.7, 1.3) # Contrast
        beta = random.randint(-40, 40)   # Brightness
        aug_img = cv2.convertScaleAbs(aug_img, alpha=alpha, beta=beta)
        
        # 2. Random Blur
        if random.random() > 0.5:
            k = random.choice([3, 5])
            aug_img = cv2.GaussianBlur(aug_img, (k, k), 0)
            
        # 3. Random Horizontal Flip
        flipped = False
        if random.random() > 0.5:
            aug_img = cv2.flip(aug_img, 1)
            flipped = True
            
        # Adjust labels
        for label in labels:
            cls_id, x_c, y_c, w, h = label
            x_c, y_c, w, h = float(x_c), float(y_c), float(w), float(h)
            
            if flipped:
                x_c = 1.0 - x_c
                
            new_labels.append(f"{cls_id} {x_c:.4f} {y_c:.4f} {w:.4f} {h:.4f}")
            
        # Save new image and label
        img_name = f"aug_{i:03d}.jpg"
        cv2.imwrite(f"dataset/images/train/{img_name}", aug_img)
        
        with open(f"dataset/labels/train/aug_{i:03d}.txt", "w") as f:
            f.write("\n".join(new_labels))
            
    print(f"Successfully generated {num_images} augmented training samples!")

if __name__ == "__main__":
    augment_dataset(100)
