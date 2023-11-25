'''from PIL import Image
import os

input_folder = "Trab_classificador_imagem/data"

output_folder = "Trab_classificador_imagem/data_resize"

new_size = (150,150)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
files = os.listdir(input_folder)

for filename in files:
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        
        img = Image.open(os.path.join(input_folder, filename))
        
        img = img.resize(new_size)
        
        output_path = os.path.join(output_folder, "001_" + filename)
        img.save(output_path)

        print(f"Imagem redimensionada e salva em: {output_path}")
'''

from PIL import Image
import os

# Pasta de entrada com as imagens originais
input_folder_classe = "Trab_classificador_imagem/data/classe1"

# Pasta de saída para as imagens redimensionadas e com qualidade reduzida
output_folder_classe = "Trab_classificador_imagem/data_resize/class1"

# Tamanho desejado
new_size = (150, 150)

# Verifique se a pasta de saída existe, se não, crie-a
if not os.path.exists(output_folder_classe):
    os.makedirs(output_folder_classe)

# Liste todos os arquivos na pasta de entrada
files = os.listdir(output_folder_classe)

# Itere sobre os arquivos na pasta de entrada
for filename in files:
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Abra a imagem
        img = Image.open(os.path.join(input_folder_classe, filename))
        
        # Redimensione a imagem
        img = img.resize(new_size)
        
        # Reduza a qualidade da imagem em 50%
        img.save(os.path.join(output_folder_classe, "001_" + filename), quality=50)

print("Redimensionamento e redução de qualidade concluídos.")