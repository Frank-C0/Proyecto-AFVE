

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
    for s2 in (
        "<inactivo>",
        "<pocoActivo>",
        "<moderadamenteActivo>",
        "<muyActivo>",
    ):
        for s3 in (
            "<Leve>",
            "<Moderado>",
            "<Brusco>",
        ):
            print(f"{s1} - {s2} - {s3}")