from fpdf import FPDF
import pandas as pd 

def generate_report(df, p1, p2, p3):
    pdf=FPDF("L", "mm", "A4")
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.text(10, 10, f"Automatic Report: {p1} Confirmed Cases")
    pdf.image('output/graph_confirmed'+p1+'.png', x = 30, y = 15, w =0, h =0)

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.text(10, 10, f"Automatic Report: {p1} Deaths")
    pdf.image('output/graph_deaths'+p1+'.png', x = 30, y = 15, w =0, h =0)

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.text(10, 10, f"Automatic Report: {p3}")
    pdf.image('output/graph_confirmed'+p3+p1+p2+'.png', x = 30, y = 15, w =0, h =0)

    df_2=df[df['ISO_ALP_2']==p1]
    pop_p1=str(int(df_2["POPULATION"].unique()))
    df_3=df[df['ISO_ALP_2']==p2]
    pop_p2=str(int(df_3["POPULATION"].unique()))    
    pdf.text(140, 10, f"Population {p1}: {pop_p1} - Popupulation {p2}: {pop_p2}")
    
    pdf.output("./output/report.pdf", "F")
