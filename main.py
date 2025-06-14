import numpy as np
import pandas as pd

def main():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    }

    df = pd.DataFrame(data)
    print("DataFrame created with Pandas:")
    print(df)

    print("Mean age:", np.mean(df['Age']))

if __name__ == "__main__":
    main()
