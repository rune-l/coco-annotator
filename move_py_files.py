import os
import subprocess
test_set_path = '/Users/runelangergaard/Documents/SmartAnnotation/data/test_set'
test_imgs = os.listdir(test_set_path)
test_imgs

cwd_path = '/Users/runelangergaard'
os.chdir(cwd_path)

for img in test_imgs:
    full_path = os.path.join(test_set_path, img)
    subprocess.run([
        "scp", 
        "-i",
        "coco-anno.pem",
        full_path,
        "ec2-user@ec2-34-211-193-133.us-west-2.compute.amazonaws.com:/datasets/tmp"
    ])

