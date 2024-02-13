from PIL import Image

# Загрузка изображений

path = r'H:/python/pygame/tutorrials/Pygame-Tutorials/Game/'
images = [Image.open(path + f'R{i}.png') for i in range(1, 10)]

# Создание нового изображения для объединения
combined_image = Image.new('RGBA', (64 * 9, 64))

# Объединение изображений
x_offset = 0
for image in images:
    combined_image.paste(image, (x_offset, 0))
    x_offset += 64

# Сохранение объединенного изображения с сохранением альфа-канала
combined_image.save(path + 'R.png')
