#2023 remake by Daniel Segal in Python version, at copyright by Alex Segal's "3DS2RIB" in 1996-x on C
                        #3DS2RIB. Good old (dated 1996) program to convert .3DS scenes to .RIB files.
import sys
import numpy as np
from pymeshio import obj, opengl

def convert_3ds_to_rib(input_file, output_file):
    # Load .3DS file
    mesh = obj.load(input_file)

    # Extract vertices, faces, and normals
    vertices = np.array(mesh.vertices)
    faces = np.array(mesh.faces)
    normals = np.array(mesh.normals)

    # Open output RIB file
    with open(output_file, 'w') as rib_file:
        # Write RIB header
        rib_file.write('##RenderMan RIB-Structure 1.0\n')

        # Write RIB geometry commands
        rib_file.write('PointsPolygons [ ')
        for face in faces:
            rib_file.write(str(len(face)) + ' ')
            for vertex_idx in face:
                rib_file.write(str(vertex_idx) + ' ')
        rib_file.write('] [\n')

        # Write vertex positions
        rib_file.write('\t"P" [\n')
        for vertex in vertices:
            rib_file.write('\t\t' + ' '.join(map(str, vertex)) + '\n')
        rib_file.write('\t]\n')

        # Write vertex normals
        rib_file.write('\t"N" [\n')
        for normal in normals:
            rib_file.write('\t\t' + ' '.join(map(str, normal)) + '\n')
        rib_file.write('\t]\n')

        # Close RIB geometry commands
        rib_file.write(']\n')

    print(f'Successfully converted {input_file} to {output_file}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python 3ds_to_rib.py input_file.3ds output_file.rib')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_3ds_to_rib(input_file, output_file)

#To use this script, you would run it from the command line with two arguments: the input .3DS file and the output .RIB file. For example:
    # python 3ds_to_rib.py input_file.3ds output_file.rib
