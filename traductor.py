import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class TraductorSDH:
    def __init__(self, ruta_excel):
        self.df = pd.read_excel(ruta_excel)
        self.modelo = SentenceTransformer('all-MiniLM-L6-v2')

        self.terminos_ingles = self.df['English'].astype(str).tolist()
        self.terminos_espanol = self.df['Spanish'].astype(str).tolist()
        self.embeddings_diccionario = self.modelo.encode(self.terminos_ingles, convert_to_tensor=True)

    def cargar_corpus_desde_carpeta(self, carpeta):
        textos = []
        nombres_archivos = []
        for archivo in os.listdir(carpeta):
            if archivo.endswith(".txt"):
                ruta = os.path.join(carpeta, archivo)
                with open(ruta, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    textos.append(contenido)
                    nombres_archivos.append(archivo)
        return textos, nombres_archivos

    def analizar_corpus(self, lista_textos, nombres_archivos, umbral=0.5):
        resultados = []
        embeddings_corpus = self.modelo.encode(lista_textos, convert_to_tensor=True)
        similitudes = cosine_similarity(embeddings_corpus, self.embeddings_diccionario)

        for i, fila in enumerate(similitudes):
            for j, score in enumerate(fila):
                if score >= umbral:
                    resultados.append({
                        'archivo': nombres_archivos[i],
                        'frase_corpus': lista_textos[i],
                        'termino_diccionario': self.terminos_ingles[j],
                        'traduccion_espanol': self.terminos_espanol[j],
                        'similitud': round(float(score), 4)
                    })
        return resultados

    def exportar_csv(self, resultados, salida_csv='resultados_sdh.csv'):
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(salida_csv, index=False, encoding='utf-8')
