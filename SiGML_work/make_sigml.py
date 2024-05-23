import os

input_file = 'C:/Users/asus/OneDrive/Desktop/VS/PYTHON/MINOR/input_01.txt'
output_file = "C:/Users/asus/AppData/Local/Programs/SiGML-Player/resources/static/sigml/your_input.sigml"
folder_path = "C:/Users/asus/OneDrive/Desktop/VS/PYTHON/MINOR/SiGML_work/text_to_isl-main/static/SignFiles"


with open(input_file, 'r') as input_txt, open(output_file, 'w') as output_txt:
    output_txt.write('<sigml>\n')
    for word_index, word in enumerate(input_txt.read().split()):
        sigml_file_path = os.path.join(folder_path, f"{word}.sigml")
        if os.path.exists(sigml_file_path):
            with open(sigml_file_path, 'r') as sigml_file:
                content = sigml_file.read()
                content = content.replace('<sigml>', '').replace('</sigml>', '')
                output_txt.write(content + '\n')
        else:
            output_txt.write("\n")
    output_txt.write('</sigml>\n')


print("SiGML file generated successfully")
