from multiprocessing import Pool
def apply_filter(image_path):
    print(f"processing {image_path}")

image_list = ["image1.jpg", "image2.jpg", "image3.jpg"]
if __name__ == "__main__":
    with Pool() as pool:
        pool.map(apply_filter, image_list) 