def main():
    print("Hello from data-project! from feur")
    print("Hello from anddtoknnrfoiroifolskvnskioejoiefjoiezjfozeifzjeifizoifozijefoizejfoizejfoizejfoziejfozeijfzoeeifjzeoifjzeoifjzeoifjzeoifjzeofjzefoizeofijzeofijzoiejfozeijfzoeifjzoiefjzeoifjzoiejfzoeijfzoeijfierfoine")
    import pandas as pd 
    import numpy as np 

    df = pd.read_csv("data/raw/dataset/global_air_quality_data_10000.csv")
    print(df.describe())
if __name__ == "__main__":
    main()
