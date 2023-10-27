# ia-classificador-imagem

### Explicando a criação do Modelo:

**model = Sequential():** Aqui, você está criando um objeto Sequential que é um modelo sequencial em Keras. Esse modelo permite adicionar camadas sequencialmente, uma após a outra, sem que as camadas compartilhem conexões entre si.

**model.add(Conv2D(32, (3, 3), input_shape=(image_size[0], image_size[1], 3), activation='relu'):** Aqui, você está adicionando a primeira camada convolucional à rede. Os parâmetros são os seguintes:

_Conv2D(32, (3, 3):_ Esta camada possui 32 filtros de convolução, cada um com uma janela (kernel) de 3x3.<br>
_input_shape=(image_size[0], image_size[1], 3):_ Este é o formato de entrada da imagem. image_size é uma variável que deve conter as dimensões da imagem (altura, largura e canais de cor). Nesse caso, a imagem tem 3 canais de cor (provavelmente, RGB).<br>
_activation='relu':_ A função de ativação usada na camada é a função ReLU (Rectified Linear Unit), que é uma função não linear que ajuda a rede a aprender relações complexas nos dados.

**model.add(MaxPooling2D(pool_size=(2, 2)):** Esta linha adiciona uma camada de MaxPooling à rede. O MaxPooling é usado para reduzir o tamanho espacial das representações geradas pelas camadas convolucionais anteriores. Neste caso, uma janela de 2x2 é usada para realizar o pooling.

**model.add(Conv2D(64, (3, 3), activation='relu'):** Essa linha adiciona uma segunda camada convolucional com 64 filtros de convolução, também com uma janela de 3x3 e função de ativação ReLU.

**model.add(MaxPooling2D(pool_size=(2, 2)):** Aqui, outra camada de MaxPooling é adicionada para reduzir ainda mais o tamanho espacial das representações.

**model.add(Flatten()):** Esta linha adiciona uma camada de Flatten. Ela é usada para transformar os dados tridimensionais provenientes das camadas convolucionais em um vetor unidimensional, preparando os dados para as camadas totalmente conectadas.

**model.add(Dense(64, activation='relu'):** Adiciona uma camada totalmente conectada com 64 neurônios e função de ativação ReLU.

**model.add(Dropout(0.5)):** Aqui, é adicionada uma camada de dropout com uma taxa de 0,5. O dropout é uma técnica de regularização que ajuda a prevenir o overfitting, desligando aleatoriamente uma fração dos neurônios durante o treinamento.

**model.add(Dense(1, activation='sigmoid'):** A última camada é uma camada totalmente conectada com um único neurônio e uma função de ativação sigmoid. Essa camada é comumente usada em tarefas de classificação binária, onde a saída é uma probabilidade entre 0 e 1, indicando a probabilidade de pertencer à classe positiva.
