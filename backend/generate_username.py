import unicodedata

def remove_accents(text: str) -> str:
    """Normaliza y elimina tildes, eñes y diéresis."""
    # Descompone los caracteres en su base + el acento
    nfkd_form = unicodedata.normalize('NFKD', text)
    # Filtra solo los caracteres que no sean marcas de acento (Non-Spacing Marks)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def generate_username(full_name, used_usernames):
    """
    Genera un nombre de usuario ignorando prefijos (Mr, Dr) y sufijos (Jr, V).
    Lógica: primera letra del nombre + apellido real.
    """

    # 1. Normalización: Quitar acentos y eñes antes de procesar
    name_clean = remove_accents(full_name.lower())

    prefixes = {"mr", "mrs", "ms", "dr", "prof", "sir", "madam"}
    suffixes = {"jr", "sr", "i", "ii", "iii", "iv", "v", "vi"}
    

    # Limpieza y tokenización
    clean_name = clean_name = name_clean.replace("-", " ").replace(".", "")
    parts = [p for p in clean_name.split() if p not in prefixes]
    
    if not parts:
        base = "u"
    elif len(parts) == 1:
        base = parts[0][0]
    else:
        # Si el último elemento es un sufijo (ej. 'v'), lo ignoramos para hallar el apellido
        if parts[-1] in suffixes and len(parts) > 2:
            last_name = parts[-2] 
        else:
            last_name = parts[-1]
            
        first_char = parts[0][0]
        base = f"{first_char}{last_name}"
    
    # Manejo de duplicidad correlativa 
    candidate = base
    counter = 1
    while candidate in used_usernames:
        candidate = f"{base}{counter}"
        counter += 1
    
    used_usernames.add(candidate)
    return candidate