import requests
import pandas as pd
from datetime import datetime

api_key = "3UK7W7QTG5ZRV13D"
company_tickers = [
    "AFFLE.BO", "SEACOAST.BO", "ICICIPRUMF.BO", "SPANDANA.BO", "STERLINREN.BO",
    "ALPHALOGIC.BO", "NOVATEOR.BO", "360ONEWAM.BO", "IIFLSEC.BO", "MUFGREEN.BO",
    "MISQUITA.BO", "GALACTICO.BO", "VAXFAB.BO", "NIPPONINDIA.BO", "GUJFLUORO.BO",
    "IRCTC.BO", "GOBLIN.BO", "GENSOLENG.BO", "VISHWARAJ.BO", "GREENPANEL.BO",
    "SHAHLON.BO", "ABSLMF.BO", "MOUNT.BO", "ANUROOP.BO", "COLAB.BO", "CSBANK.BO",
    "UJJIVANSFB.BO", "HINDWARE.BO", "EASUNCAP.BO", "PRINCEPIPE.BO", "ASSAMEN.BO",
    "GIANLIFE.BO", "ARTEMISMED.BO", "SUMICHEM.BO", "MIRAEASSET.BO", "JANUSCORP.BO",
    "VARDHAN.BO", "UNIVERSUS.BO", "CBPH.BO", "OCTAVIUS.BO", "SUVENPHAR.BO",
    "SMAUTO.BO", "SBICARD.BO", "ROJEWEL.BO", "COSPOWER.BO", "HITACHIIND.BO",
    "DJMEDIAPR.BO", "NATURALB.BO", "REGISIND.BO", "BILLWININD.BO", "AARTISURF.BO",
    "BONLON.BO", "BOROSIL.BO", "ROSSARI.BO", "NDRAUTO.BO", "SURATW.BO", "MAXHEALTH.BO",
    "MAXINDIA.BO", "HAPPSTMNDS.BO", "ROUTE.BO", "SAMRATFOR.BO", "ADVITIN.BO", "ARCHIDPLY.BO",
    "CAMS.BO", "CHEMCON.BO", "SECMARK.BO", "ANGELONE.BO", "ATAMVALVES.BO", "MAZDOCK.BO",
    "UTIAMC.BO", "GMPOLY.BO", "LIKHITHA.BO", "VEERGLOBAL.BO", "HEMIPROP.BO", "EQUITASBN.BO",
    "SHINE.BO", "GLAND.BO", "RBL.BO", "TARC.BO", "RAVINDR.BO", "FAIRCHEM.BO", "BECTORFOOD.BO",
    "ANTONYWASTE.BO", "RITAFIN.BO", "IRFC.BO", "INDIGOPNTS.BO", "HOMEFIRST.BO", "STOVEKRAF.BO",
    "MRPAGRO.BO", "SMC.BO", "NURECA.BO", "RAILTEL.BO", "HERANBA.BO", "DAVSUG.BO", "DRCSYS.BO",
    "MTARTECH.BO", "JUBILANT.BO", "EASEMYTR.BO", "KNOWLEDGE.BO", "SUUMAYA.BO", "ANUPAM.BO",
    "CRAFTSMAN.BO", "LXCHEM.BO", "KALYANKJIL.BO", "SURYODAYS.BO", "NAZARA.BO", "SUVIDHAA.BO",
    "BBQ.BO", "EKI.BO", "RAJESHWARI.BO", "JETMALL.BO", "MACROTEC.BO", "DEEPIND.BO", "INOXWIND.BO",
    "VINEETLAB.BO", "SHYAMMET.BO", "SONACOMS.BO", "NAVODAY.BO", "DODLA.BO", "KIMS.BO", "ADESHWAR.BO",
    "TIMESGTY.BO", "INDIAPEST.BO", "FOCUSBS.BO", "GRINFRA.BO", "CLEAN.BO", "AAPLUS.BO", "ZOMATO.BO",
    "TATVA.BO", "GLENMARK.BO", "GRETEX.BO", "ROLEXR.BO", "EXXARO.BO", "KRSNAA.BO", "WINDLAS.BO",
    "DEVYANI.BO", "MEGH.BO", "EPIGRAL.BO", "CARTRADE.BO", "NUVOCO.BO", "APTUS.BO", "CHEMPLAST.BO",
    "SHARPLINE.BO", "AASHKA.BO", "AMIORG.BO", "VIJAYA.BO", "PLATONE.BO", "SANSERA.BO", "PREVEST.BO",
    "MARKOLINE.BO", "SBLIL.BO", "PARASDEF.BO", "GETALONG.BO", "SVRL.BO", "ABSLAMC.BO", "PROMAX.BO",
    "SAMOR.BO", "ADISHAKTI.BO", "FSN_ECOM.BO", "FINOPAY.BO", "SJS.BO", "SIGACHI.BO", "PBFINTECH.BO",
    "SUYOG.BO", "ONE97.BO", "SAPPHIRE.BO", "LATENT.BO", "TARSONS.BO", "OMNIPOTENT.BO", "GOFASH.BO",
    "DMR.BO", "HITECH.BO", "STARHL.BO", "TEGINDIA.BO", "ANANDRATH.BO", "ZODIAC.BO", "RATEGAIN.BO",
    "SHRIRAMP.BO", "JETFREIGHT.BO", "CEINFO.BO", "METROBR.BO", "MEDPLUS.BO", "DATAPAT.BO", "HPADHES.BO",
    "SUPRIYA.BO", "CLARAIND.BO", "BRANDTBK.BO", "CMSINFO.BO", "BRANDCON.BO", "FABINO.BO", "WONDER.BO",
    "AGSTTL.BO", "ALKOSIGN.BO", "ADANIWILMAR.BO", "QRO.BO", "SAFA.BO", "DEVIT.BO", "VEDANT.BO",
    "MARUTIINT.BO", "SOFTTECH.BO", "EKENNIS.BO", "EUREKA.BO", "GDL.BO", "GMRPOWER.BO", "BHATIACOL.BO",
    "MOTHERSUMI.BO", "ACHYUT.BO", "EVOQ.BO", "AVRO.BO", "UMAEXPO.BO", "VERANDA.BO", "SUNRISE.BO",
    "DHYAANI.BO", "HARIOM.BO", "EIGHTYJ.BO", "SHASHWAT.BO", "GLOBALLIF.BO", "FONE4.BO", "NANAVATI.BO",
    "CAMPUSAC.BO", "RAINBOW.BO", "SILVERTUC.BO", "LICINDIA.BO", "PRUDENTCOR.BO", "VENUSP.BO", "DELHIVERY.BO",
    "PARADEEP.BO", "TIERRA.BO", "ETHOS.BO", "EMUDHRA.BO", "AETHER.BO", "WEWIN.BO", "SILVERPEAR.BO",
    "SCARNOSE.BO", "GOEL.BO", "MODISN.BO", "PEARLGRN.BO", "SAILANI.BO", "KESAR.BO", "BRIGHT.BO", "JAYANT.BO",
    "VEERKRUP.BO"
]

function = "TIME_SERIES_DAILY"
outputsize = "full"

for symbol in company_tickers:
    print(f"Fetching data for {symbol}...")
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" in data:
        time_series = data["Time Series (Daily)"]

        stock_data = []
        for date, daily_data in time_series.items():
            stock_data.append({
                "Date": datetime.strptime(date, "%Y-%m-%d"),
                "Open": float(daily_data["1. open"]),
                "High": float(daily_data["2. high"]),
                "Low": float(daily_data["3. low"]),
                "Close": float(daily_data["4. close"]),
                "Volume": int(daily_data["5. volume"])
            })

        df = pd.DataFrame(stock_data)
        start_date = datetime(2015, 1, 1)
        end_date = datetime(2024, 6, 30)
        df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

        # Save to CSV
        csv_path = f'stock_market_data_{symbol.split(".")[0]}.csv'
        df.to_csv(csv_path, index=False)
        print(f"Stock market data for {symbol} saved to {csv_path}")
    else:
        print(f"The API response does not contain the expected data for {symbol}. Please check the symbol and try again.")
