import matrices
def canicas():
    vertices = input("Digite el número de vertices: ")
    vec_estado = matrices.llenar(vec_estado)
    matrix = matrices.generar_matriz(vertices) 
    click= int(input("Ingrese los clicks, ingrese un valor negativo para terminar: "))
    while click >= 0:
        print("Vector estado ", click) 
        print(matrices.clicks(matrix, vec_estado, click))
        click = int(input("Ingrese los clicks, ingrese un valor negativo para terminar: "))




