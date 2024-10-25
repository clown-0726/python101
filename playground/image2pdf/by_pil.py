from PIL import Image

images = Image.open("example.png").convert('RGB')
images.save("example.pdf")
