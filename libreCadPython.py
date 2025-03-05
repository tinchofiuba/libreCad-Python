import ezdxf

def create_dxf():
    # Crear un nuevo documento DXF
    doc = ezdxf.new(dxfversion='R2010')
    msp = doc.modelspace()

    # Añadir un semicírculo con forma de "C"
    center = (0, 0)  # Centro del semicírculo
    radius = 50      # Radio del semicírculo
    start_angle = 90 # Ángulo de inicio en grados
    end_angle = 270  # Ángulo final en grados
    msp.add_arc(center, radius, start_angle, end_angle)

    # Calcular el punto superior del arco
    top_point = (center[0], center[1] + radius)

    # Añadir una línea horizontal desde el punto superior del arco
    line_length = 100  # Longitud de la línea horizontal
    msp.add_line(top_point, (top_point[0] + line_length, top_point[1]))

    # Guardar el documento en un archivo
    doc.saveas("output.dxf")
    print("Documento guardado como output.dxf")

if __name__ == "__main__":
    create_dxf()