

for s3 in (
    "<Leve>",
    "<Moderado>",
    "<Brusco>",
):
    for s2 in (
        "<inactivo>",
        "<pocoActivo>",
        "<moderadamenteActivo>",
        "<muyActivo>",
    ):
        for s1 in (
            "<noterremoto>",
            "<microTerremotos>", 
            "<pequenosTerremotos>", 
            "<terremotosModerados>", 
            "<terremotosFuertes>", 
            "<terremotosMayores>", 
            "<grandesTerremotos>", 
            "<terremotosMuyGrandes>", 
        ):
            print(f"{s3} - {s2} - {s1}")
            