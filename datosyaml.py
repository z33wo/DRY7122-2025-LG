import yaml
with open("eva1.yaml", "r") as archivo_yaml:
    parseoyaml = yaml.safe_load(archivo_yaml)

print("id_usuario:", parseoyaml.get("id_usuario"))
print("token_seguridad:", parseoyaml.get("token_seguridad"))
print("fecha_creacion:", parseoyaml.get("fecha_creacion"))
print("estado", parseoyaml.get("estado"))