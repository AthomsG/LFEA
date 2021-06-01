from PIL import Image, ImageOps

def img_to_matrix(img):
    width, height = img.size
    pixels = img.load() #returns dictionary where each entry has rgb values

    matrix = list()
    row  = list()
    for y in range(height):
        row = []
        for x in range(width):
            row += [pixels[x, y]]
        matrix.append(row)
    return matrix

def soma_linhas(pixels, orientation='x'):
    height = len(pixels)
    width  = len(pixels[0])
    
    if orientation=='x':
        soma = list()
        for i in range(width):
            soma += [0]
        for i in range(height):
            for j in range(width):
                soma[j] += pixels[i][j]
        return soma
    else:
        soma = list()
        for i in range(height):
            soma += [0]
        for i in range(width):
            for j in range(height):
                soma[j] += pixels[j][i]
        return soma

def normalize(linha):
    res = list()
    peak = max(linha)
    for ponto in linha:
        res.append(ponto/peak)
    return res

def matrix_to_img(matrix):
    height = len(matrix)
    width  = len(matrix[0])

    new_img = Image.new('L',(width, height))

    putdata = list()
    for i in range(height):
        for j in range(width):
            putdata += [matrix[i][j]]

    new_img.putdata(putdata)
    return new_img
