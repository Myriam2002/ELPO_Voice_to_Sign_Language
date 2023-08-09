import Speech_to_list_functions as sl
import Text_to_image as ti


list_text = sl.speech('output.wav')
print(list_text)

textImage = ti.imgDisplay(list_text)
