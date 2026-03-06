import os
from datetime import datetime

def generar_indice(ruta_carpeta):
    # Nombre del archivo de salida
    archivo_salida = "Indice_Documentacion.md"
    
    try:
        # Obtenemos la lista de archivos en la carpeta
        archivos = os.listdir(ruta_carpeta)
        
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(f"# Índice Automático de Documentación\n")
            f.write(f"Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Proyectos y archivos encontrados en: `{ruta_carpeta}`\n\n")
            f.write("| Nombre del Archivo | Tipo |\n")
            f.write("|--- |--- |\n")
            
            for archivo in archivos:
                # Ignoramos el propio script y archivos ocultos
                if not archivo.startswith('.') and archivo != "main.py":
                    tipo = "Carpeta" if os.path.isdir(os.path.join(ruta_carpeta, archivo)) else "Archivo"
                    f.write(f"| {archivo} | {tipo} |\n")
        
        print(f"✅ ¡Éxito! Se ha creado '{archivo_salida}' correctamente.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Ejecución
if __name__ == "__main__":
    # El punto '.' significa que leerá la carpeta donde esté guardado el script
    generar_indice('.')