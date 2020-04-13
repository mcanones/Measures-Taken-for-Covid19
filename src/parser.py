from argparse import ArgumentParser

class ParserKey():
    def __init__(self):
        parser = ArgumentParser(description="Obtain a PDF report with the evolution of COVID in a given country.")
        parser.add_argument("--p1", help="Choose 1 of these: AF, BT, AG, BO, BA, AR, AL, NP, DZ, BD, AO, CL, UY, PY, PE, AZ, BR, PT, EC, CO, AM, BH, VE, GY, SR, BE, PA, AU, CR, NI, HN, BZ, SV, BS, GT, BJ, MX, BN, BG, PG, SB, CM, TV, VU, FJ, TO, NR, KI, ID, SN, PH, TD, MY, BF, CN, CG, BB, CA, TH, NZ, GB, KM, MG, CY, DM, US, ML, GD, LC, VC, IT, WS, CF, ET, IN, SC, KE, MA, SA, UZ, TM, TG, TL, TJ, SG, SK, TZ, GR, SI, SS, PW, PS, PL, SZ, QA, TT, DO, GQ, SY, KP, SD, OM, DE, BY, MH, UA, YE, BI, AT, NL, LS, LV, HR, LT, EE, TR, CZ, FI, DK, SE, DJ, LA, NO, KG, MR, CV, ER, MZ, KH, FM, IS, MD, CH, LU, HU, LI, IE, RO, AE, GE, IR, KZ, VN, JM, ME, ZA, MN, MM, MT, UG, ZM, IL, GM, ZW, MK, MU, LK, JP, RU, TN, MV, NE, KW, GW, LR, NG, PK, MW, RS, SL, RW, HT, JO, GH, ES, LB, EG, IQ, LY, FR, SO, BW, CU, GA, GN, KN, SM, ST.", type=str, default='ES')
        parser.add_argument("--p2", help="Choose other country in ISO ALPHA 2 code.", type=str, default='NL')
        parser.add_argument("--p3", help="Add your email.", type=str, default=None)
        self.args = parser.parse_args()