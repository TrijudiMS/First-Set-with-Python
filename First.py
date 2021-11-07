import pandas as pd

df_production = None
new_result_production = result = ""
first = {}

# function to check production have one or more result production
def check_production(result_production):
    global new_result_production,result, first
    # if the production has two result production
    if "|" in result_production:
        # split result production by "|"
        temp_result_production = result_production.split("|")
        # combine result production and add ", " between them
        for i in range(len(temp_result_production)):
            # if element first or last element
            if i == 0 or i == len(temp_result_production):
                # use rules_first for get first value from first character on each element
                result = rules_first(temp_result_production[i][0])
                # add first value on new_result_production
                new_result_production += result
            # if not first or last element
            else:
                # use rules_first for get first value from first character on each element
                result = rules_first(temp_result_production[i][0])
                # add comma and first value on new_result_production
                new_result_production += ", " + result
        # return new result_production to put in first dict 
        return new_result_production
    # if the production has one result production
    else:
        # return split result_production 
        return result_production.split()
    
# function for get first value based on first function
def rules_first(firstword):
    """
        rules 1:    if firstword is lowercase, first value  = firstword
        rules 2:    if firstword is epsilon, first value  = firstword
        rules 3:    if firstword is uppercase, first value = first[firstword]
    """
    
    global first
    # implement rule 2 and rule 1
    if firstword == "_" or firstword.isupper() != True:
        first_value = firstword
    # implement rule 3
    elif firstword.isupper() == True:
        # first value of first word same as first[firstword]
        first_value = first[firstword]

    return first_value

# function for get set of first value on each name production
def first_production(production):
    global df_production, result, new_result_production, first
    # get rows & columns of production
    rows, columns = production.shape
    # decrement looping
    for row in range(rows-1, -1, -1):
        # get result production on each row
        hasil_produksi = production["Hasil_Produksi"][row]
        # get name production
        columns = df_production.columns[0]
        result = new_result_production = ""
        # check result production whether one result or more result
        hasil_produksi = check_production(hasil_produksi)
        # if result production is one result
        if len(hasil_produksi) == 1:
            # get first value by firstword
            first_value = rules_first(hasil_produksi[0][0])
            # insert first value as value on first dict with key name production
            first[production[columns][row]] = first_value
        # if result production is two or more result
        else:     
            # remote duplicate first
            new_hasil_produksi = ""
            # remove duplicate first value 
            hasil_produksi = hasil_produksi.split(", ")
            for nomor_hasil_produksi in range(len(hasil_produksi)):
                # if first value not in new_hasil_produksi, add first value
                if hasil_produksi[nomor_hasil_produksi] not in new_hasil_produksi:
                    if nomor_hasil_produksi == 0 or nomor_hasil_produksi == len(hasil_produksi):
                        new_hasil_produksi += hasil_produksi[nomor_hasil_produksi]
                    else:
                        new_hasil_produksi += ", " + hasil_produksi[nomor_hasil_produksi]
                # if first value already in new_hasil_produksi, ignore
                else:
                    pass
            # insert new_hasil_produksi as value on first dict with key name production
            first[production[columns][row]] = new_hasil_produksi
    # return an dict first containing a set of first value on each name production 
    return first
        
# function to create initial production and display first of production
def main():
    global df_production, first

    # Example Case 1
    first = {}
    # set production
    production = {
        "Produksi":["K", "K'", "L", "L'", "M"], 
        "Hasil_Produksi": ["LK'", "/LK|_", "ML", "-ML|_", "+M|(K)|x|y"]
    }
    df_production = pd.DataFrame(production)
    first_result = first_production(df_production)
    # print production and first of production
    print("Production: ")
    print(df_production.head(5))
    print("\nFirst of Production: ")
    for index, value in enumerate(first_result):
        print(f"first({value})\t: {first_result[value]}")

    print("\n\n\n")

    # Example Case 2
    first = {}
    # set production
    production = {
        "Produksi":['E', "E'","T", "T'","F"], 
        "Hasil_Produksi": ["TE'", "+TE'|_", "FT'", "*FT'|_", "(E)|id"]
    }
    df_production = pd.DataFrame(production)
    first_result = first_production(df_production)
    # print production and first of production
    print("Production: ")
    print(df_production.head(5))
    print("\nFirst of Production: ")
    for index, value in enumerate(first_result):
        print(f"first({value})\t: {first_result[value]}")

    print("\n\n\n")

    # Example Case 3
    first = {}
    # set production
    production = {
        "Produksi":["S", "A", "B", "B'", "C"], 
        "Hasil_Produksi": ["AB|_", "Ca|_", "cB'", "aACB'|_", "b|_"]
    }
    df_production = pd.DataFrame(production)
    first_result = first_production(df_production)
    # print production and first of production
    print("Production: ")
    print(df_production.head(5))
    print("\nFirst of Production: ")
    for index, value in enumerate(first_result):
        print(f"first({value})\t: {first_result[value]}")
    
    print("\n\n\n")

if __name__ == "__main__":
    main()