import tkinter as tk
from generador import generar_numeros_aleatorios
from ordenamiento import *

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generador y Ordenador de Números Aleatorios")
        self.geometry("600x400")  # Ajusta el tamaño de la ventana

        # Crear widgets
        self.ordenamiento_var = tk.StringVar()
        self.ordenamiento_var.set("burbuja")  # Valor predeterminado
        self.ordenamiento_label = tk.Label(self, text="Seleccione un método de ordenamiento:")
        self.ordenamiento_menu = tk.OptionMenu(self, self.ordenamiento_var, "burbuja", "seleccion", "insercion", "heap", "merge")

        # Crear una barra desplegable para la cantidad de números
        self.cantidad_var = tk.StringVar()
        self.cantidad_var.set("100")  # Valor predeterminado
        self.cantidad_label = tk.Label(self, text="Seleccione la cantidad de números:")
        self.cantidad_menu = tk.OptionMenu(self, self.cantidad_var, "100", "1000", "10000")

        self.generate_button = tk.Button(self, text="Generar números", command=self.generar_numeros)
        self.sort_button = tk.Button(self, text="Ordenar números", command=self.ordenar_numeros)
        self.save_sorted_button = tk.Button(self, text="Guardar números ordenados", command=self.guardar_ordenados)

        self.result_text_unsorted = tk.Text(self, height=10, width=20)  # Área para números sin ordenar
        self.result_text_sorted = tk.Text(self, height=10, width=20)  # Área para números ordenados

        # Posicionar widgets
        self.ordenamiento_label.grid(row=0, column=0, padx=10, pady=5)
        self.ordenamiento_menu.grid(row=0, column=1, padx=10, pady=5)
        self.cantidad_label.grid(row=1, column=0, padx=10, pady=5)
        self.cantidad_menu.grid(row=1, column=1, padx=10, pady=5)
        self.generate_button.grid(row=2, columnspan=2, padx=10, pady=5)
        self.sort_button.grid(row=3, columnspan=2, padx=10, pady=5)
        self.save_sorted_button.grid(row=5, columnspan=2, padx=10, pady=5)
        self.result_text_unsorted.grid(row=6, column=0, padx=10, pady=5)
        self.result_text_sorted.grid(row=6, column=1, padx=10, pady=5)

        # Inicializar la lista de números generados
        self.numeros_generados = []

    def generar_numeros(self):
        cantidad_numeros = int(self.cantidad_var.get())
        rango_maximo = int(self.cantidad_var.get())
        self.numeros_generados = generar_numeros_aleatorios(cantidad_numeros, rango_maximo)
        self.result_text_unsorted.delete(1.0, tk.END)
        for numero in self.numeros_generados:
            self.result_text_unsorted.insert(tk.END, str(numero) + "\n")
        self.guardar_sin_ordenar()

    def ordenar_numeros(self):
        metodo_ordenamiento = self.ordenamiento_var.get()
        if metodo_ordenamiento == "burbuja":
            ord_burbuja(self.numeros_generados)
        elif metodo_ordenamiento == "seleccion":
            ord_seleccion(self.numeros_generados)
        elif metodo_ordenamiento == "insercion":
            ord_insercion(self.numeros_generados)
        elif metodo_ordenamiento == "heap":
            ord_heapsort(self.numeros_generados)
        elif metodo_ordenamiento == "merge":
            ord_mergesort(self.numeros_generados)            
        self.result_text_sorted.delete(1.0, tk.END)
        for numero in self.numeros_generados:    
            self.result_text_sorted.insert(tk.END, f"{numero}\n")

    def guardar_sin_ordenar(self):
        with open("numeros_sin_ordenar.txt", "w") as file:
            for numero in self.numeros_generados:
                file.write(f"{numero}\n")
        print("Números sin ordenar guardados en 'numeros_sin_ordenar.txt'")
    
    def guardar_ordenados(self):
        with open("guardar_ordenados.txt", "w") as file:
            for numero in self.numeros_generados:
                file.write(f"{numero}\n")
        print("Números ordenados  guardados en 'guardar_ordenados.txt'")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
