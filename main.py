from argparse import ArgumentParser
import pandas as pd 
from fpdf import FPDF
from src.graphs import *
from src.pdf import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
import email.mime.application
from getpass import getpass

#python3 main.py --p1 ES --p2 NL --p3 "Social distancing"
#python3 main.py --p4 to@gmail.com

parser = ArgumentParser(description="Obtain a PDF report with the evolution of COVID in a given country.")
parser.add_argument("--p1",help="Choose 1 of these: AF, BT, AG, BO, BA, AR, AL, NP, DZ, BD, AO, CL, UY, PY, PE, AZ, BR, PT, EC, CO, AM, BH, VE, GY, SR, BE, PA, AU, CR, NI, HN, BZ, SV, BS, GT, BJ, MX, BN, BG, PG, SB, CM, TV, VU, FJ, TO, NR, KI, ID, SN, PH, TD, MY, BF, CN, CG, BB, CA, TH, NZ, GB, KM, MG, CY, DM, US, ML, GD, LC, VC, IT, WS, CF, ET, IN, SC, KE, MA, SA, UZ, TM, TG, TL, TJ, SG, SK, TZ, GR, SI, SS, PW, PS, PL, SZ, QA, TT, DO, GQ, SY, KP, SD, OM, DE, BY, MH, UA, YE, BI, AT, NL, LS, LV, HR, LT, EE, TR, CZ, FI, DK, SE, DJ, LA, NO, KG, MR, CV, ER, MZ, KH, FM, IS, MD, CH, LU, HU, LI, IE, RO, AE, GE, IR, KZ, VN, JM, ME, ZA, MN, MM, MT, UG, ZM, IL, GM, ZW, MK, MU, LK, JP, RU, TN, MV, NE, KW, GW, LR, NG, PK, MW, RS, SL, RW, HT, JO, GH, ES, LB, EG, IQ, LY, FR, SO, BW, CU, GA, GN, KN, SM, ST.", type=str, default='ES')
parser.add_argument("--p2",help="Choose other country in ISO ALPHA 2 code.", type=str, default='NL')
parser.add_argument("--p3",help="Choose 1 of these: Public health measures, Movement restrictions, Social distancing, Governance and socio-economic measures, Lockdown.", type=str, default='Social distancing')
parser.add_argument("--p4",help="Add your email.", type=str, default=None)
args = parser.parse_args()

#Read CSV
df = pd.read_csv('./output/mining.csv', encoding='latin-1')
df=df.drop('Unnamed: 0',axis=1)

#Make Graphs
make_graphs(df,args.p1,args.p2,args.p3)

#Make Report
generate_report(df,args.p1,args.p2,args.p3)

#Generate mail
msg = MIMEMultipart()
msg.attach(MIMEText('Here you have your automatic report\nEnjoy\n'))
fp=open("./output/report.pdf",'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
fp.close()
att.add_header('Report', 'Report', filename="./output/report.pdf")
msg.attach(att)

#Send mail 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
password = getpass("Email Password: ")
server.login('from@gmail.com', password)
server.sendmail('from@gmail.com', args.p4, msg.as_string())
server.quit()

