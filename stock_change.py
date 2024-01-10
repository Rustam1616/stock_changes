import pandas as pd
import yfinance as yf
import datetime
from IPython.display import display
import streamlit as st
firms = ['AAPL','MSFT','AMZN','NVDA','GOOGL','META','GOOG','BRK-B','TSLA','UNH','LLY','JPM','XOM','AVGO','V','JNJ','PG','MA',
         'HD','ADBE','MRK','CVX','COST','ABBV','PEP','KO','WMT','CRM','BAC','ACN','NFLX','MCD','LIN','AMD','CSCO','INTC',
         'ORCL','TMO','CMCSA','ABT','DIS','PFE','WFC','INTU','VZ','QCOM','PM','AMGN','TXN','IBM','COP','DHR','UNP','NOW',
         'SPGI','GE','NKE','CAT','HON','AMAT','SBUX','LOW','BA','NEE','RTX','T','BKNG','GS','ELV','ISRG','UPS','BMY','DE',
         'MS','TJX','PLD','BLK','LMT','MDT','MMC','SYK','MDLZ','AXP','ADP','GILD','LRCX','PGR','AMT','ADI','CB','ETN','VRTX',
         'CVS','C','REGN','MU','SCHW','CI','SNPS','ZTS','BSX','CME','TMUS','SO','PANW','FI','SLB','BX','KLAC','CDNS','EQIX',
         'MO','EOG','DUK','BDX','AON','NOC','ITW','SHW','ICE','CSX','WM','CL','PYPL','HUM','MCK','APD','TGT','CMG','FDX',
         'MPC','USB','ORLY','MCO','ROP','PH','PXD','GD','ABNB','ANET','APH','MSI','TDG','AJG','MMM','TT','PNC','PSX','NXPI',
         'FCX','MAR','EMR','HCA','LULU','WELL','NSC','AZO','PCAR','CTAS','ECL','ADSK','AIG','MCHP','SRE','CCI','CARR','AFL',
         'HLT','ROST','VLO','CPRT','WMB','TFC','NEM','CHTR','TEL','MSCI','COF','KMB','PSA','MNST','DLR','EW','DXCM','OXY',
         'F','HES','SPG','AEP','ADM','MET','TRV','CNC','CEG','D','NUE','DHI','EXC','OKE','GM','IDXX','STZ','GIS','PAYX',
         'IQV','O','PCG','BK','DOW','ODFL','AME','SYY','YUM','AMP','GWW','JCI','LHX','ALL','CTSH','OTIS','FAST','VRSK',
         'PRU','HAL','KVUE','BKR','CSGP','CTVA','A','FTNT','XEL','EA','BIIB','IT','KMI','URI','DD','COR','RSG','FIS','LEN',
         'CMI','KDP','PPG','PEG','ROK','ED','ACGL','ON','HSY','GPN','DVN','CDW','VICI','EL','GEHC','MLM','IR','VMC','FANG',
         'KR','EXR','KHC','DG','PWR','CAH','ANSS','FICO','WEC','MPWR','AWK','WTW','WST','SBAC','MRNA','EIX','EFX','RCL',
         'LYB','HPQ','TTWO','CBRE','XYL','FTV','DLTR','KEYS','WBD','AVB','HIG','ZBH','WY','DAL','APTV','MTD','CHD','STT',
         'TSCO','TROW','RMD','GLW','DFS','BR','DTE','EBAY','MTB','ETR','WAB','NVR','HPE','MOH','ES','ULTA','CTRA','HWM',
         'AEE','STE','RJF','INVH','PHM','DOV','GPC','TRGP','FE','PPL','EQR','IFF','VRSN','DRI','EXPE','LH','FITB','CBOE',
         'GRMN','TDY','PTC','IRM','NDAQ','BAX','VTR','HOLX','EXPD','CNP','FDS','STLD','CLX','BRO','FLT','AKAM','TYL','EG',
         'J','ATO','CMS','COO','MKC','FSLR','BALL','NTAP','ARE','PFG','HUBB','LVS','BG','HBAN','CINF','AXON','OMC','NTRS',
         'MRO','WAT','RF','TXT','AVY','WBA','DGX','SWKS','CF','ALB','WDC','IEX','CCL','ILMN','EPAM','STX','ALGN',
         'LUV','SNA','EQT','JBHT','LDOS','WRB','TER','SWK','MAA','PKG','TSN','K','AMCR','LW','POOL','ESS','MAS','CAG',
         'BBY','CFG','DPZ','UAL','CE','LYV','ENPH','NDSN','SYF','L','LNT','HST','LKQ','PODD','MOS','IPG','GEN','IP','EVRG',
         'KEY','KIM','APA','SJM','AES','VTRS','ZBRA','MGM','TAP','JKHY','ROL','NRG','RVTY','TRMB','CDAY','BF-B','NI','PNR',
         'GL','REG','KMX','INCY','UDR','TFX','EMN','CZR','FFIV','CRL','TECH','CHRW','WRK','AOS','ALLE','HII','HRL','CPT',
         'QRVO','MTCH','PEAK','HSIC','ETSY','JNPR','RHI','PAYC','AIZ','MKTX','UHS','WYNN','BWA','PNW','CPB','AAL','NWSA',
         'BXP','FOXA','CTLT','GNRC','TPR','BEN','FRT','FMC','BBWI','PARA','XRAY','IVZ','BIO','NCLH','WHR','CMA','HAS',
         'VFC','ZION','DVA','RL','SEE','ALK','SEDG','MHK','FOX','NWS']
gdf = pd.DataFrame(columns=['Date','Close','Company','roll','percent', '3 days ago'])
for firm in firms:
    ticker = yf.Ticker(firm)
    df = ticker.history(start = datetime.datetime.today()-datetime.timedelta(days=8), 
                        end = datetime.datetime.today())['Close']
    df = df.reset_index()
    df['Company'] = firm
    df['Close'] = round(df['Close'],ndigits=2)
    df['roll'] = df['Close'].diff(periods=3)
    df['percent'] = round(df['roll'] / df['Close'] * 100,ndigits = 2)
    df['3 days ago'] = df['Close'] - df['roll']
    df = df.tail(1)
    gdf = pd.concat([gdf, df])
    
st.dataframe(gdf.sort_values(by=['percent']).head(50))