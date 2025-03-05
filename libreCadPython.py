import ezdxf

def create_dxf():
    # Crear un nuevo documento DXF
    doc = ezdxf.new(dxfversion='R2010')
    msp = doc.modelspace()

    # Añadir una línea desde el punto (0, 0) hasta el punto (100, 100)
    msp.add_line((0, 0), (100, 100))

    # Guardar el documento en un archivo
    doc.saveas("output.dxf")
    print("Documento guardado como output.dxf")

if __name__ == "__main__":
    create_dxf()
