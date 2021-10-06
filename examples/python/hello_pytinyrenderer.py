import pytinyrenderer
import math

#only used for showing the image
import numpy as np
has_numpngw = False

try:
  from numpngw import write_apng
  has_numpngw = True
except:
 pass

scene = pytinyrenderer.TinySceneRenderer()

class TextureRGB888:
  def __init__(self):
    self.pixels = [
            255,0,0,#red, green, blue
            0,255,0,
            0,0,255,
            255,255,255]
    self.width = 2
    self.height= 2


texture = TextureRGB888()

capx_model = scene.create_capsule(0.1,0.4,0, texture.pixels, texture.width, texture.height)
capy_model = scene.create_capsule(0.1,0.4,1, texture.pixels, texture.width, texture.height)
capz_model = scene.create_capsule(0.1,0.4,2, texture.pixels, texture.width, texture.height)

cube_model = scene.create_cube([0.5,0.5,0.03], texture.pixels, texture.width, texture.height, 16.)
cube_instance = scene.create_object_instance(cube_model)
scene.set_object_position(cube_instance, [0,0,-0.5])


width = 640
height = 480
eye = [2., 4., 1.]
target = [0., 0., 0.]
light = pytinyrenderer.TinyRenderLight()
camera = pytinyrenderer.TinyRenderCamera(viewWidth=width, viewHeight=height,
                                          position=eye, target=target)

capsulex_instance = scene.create_object_instance(capx_model)
capsuley_instance = scene.create_object_instance(capy_model)
capsulez_instance = scene.create_object_instance(capz_model)

images=[]

img = scene.get_camera_image([capsulex_instance], light, camera)
rgb_array = np.reshape(np.array(img.rgb,dtype=np.uint8), (img.height, img.width, -1))
images.append(rgb_array)

img = scene.get_camera_image([capsuley_instance], light, camera)
rgb_array = np.reshape(np.array(img.rgb,dtype=np.uint8), (img.height, img.width, -1))
images.append(rgb_array)

img = scene.get_camera_image([capsulez_instance], light, camera)
rgb_array = np.reshape(np.array(img.rgb,dtype=np.uint8), (img.height, img.width, -1))
images.append(rgb_array)

img = scene.get_camera_image([capsulex_instance,capsuley_instance,capsulez_instance,cube_instance], light, camera)
rgb_array = np.reshape(np.array(img.rgb,dtype=np.uint8), (img.height, img.width, -1))
images.append(rgb_array)

if has_numpngw:
  write_apng('tinyanim10_tds.png', images, delay=500)
