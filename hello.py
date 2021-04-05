print("hi")
import pandas as pd
df = pd.read_csv("/valohai/inputsNeighborhood_zhvi_uc_sfr_sm_sa_mon.csv")
df.head().to_csv("/valohai/outputs/writecsv.csv")
