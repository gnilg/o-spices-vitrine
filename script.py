from PIL import Image
import os

# Répertoire source et destination
input_folder = "images_source"
output_folder = "images_redimensionnees"

# Dimensions cibles
new_width = 1024
new_height = 768

# Assurez-vous que le dossier de sortie existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Parcourir toutes les images du dossier source
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Redimensionner l'image
        img_resized = img.resize((new_width, new_height), Image.ANTIALIAS)

        # Enregistrer l'image redimensionnée
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)

        print(f"Image {filename} redimensionnée et sauvegardée dans {output_folder}")

print("✅ Toutes les images ont été redimensionnées avec succès !")
