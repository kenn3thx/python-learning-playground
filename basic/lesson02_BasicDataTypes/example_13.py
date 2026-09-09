# Temperature Converter
def cToFConverter(degreeC):
    return round(float(degreeC) * 1.8 + 32, 1)
    

def main():

    while True:
        degreeC = input("Please enter C degree: ")

        if(degreeC):
            degreeF = cToFConverter(degreeC)
            print(f"{degreeC}C is converted to {degreeF}F")
            break
        else:
            print("C degree is None, please try again")


if __name__ == "__main__":
    main()