from PIL import Image
import os

# Pasta de entrada com as imagens originais
input_folder = "./"

# Pasta de saída para as imagens redimensionadas e com qualidade reduzida
output_folder = "./"

# Tamanho desejado
new_size = (150, 150)

# Verifique se a pasta de saída existe, se não, crie-a
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Liste todos os arquivos na pasta de entrada
files = os.listdir(input_folder)

# Itere sobre os arquivos na pasta de entrada
for filename in files:
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Abra a imagem
        img = Image.open(os.path.join(input_folder, filename))
        
        # Redimensione a imagem
        img = img.resize(new_size)
        
        # Reduza a qualidade da imagem em 50%
        img.save(os.path.join(output_folder, "001_" + filename), quality=50)

print("Redimensionamento e redução de qualidade concluídos.")