from fpdf import FPDF
import pandas as pd 

def generate_report(df, p1, p2):

    #Initial conditions page
    pdf=FPDF("L", "mm", "A4")

    #Page 1
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.text(10, 10, f"Automatic Report: {p1} - {p2} Confirmed Cases")
    pdf.image('./output/graph_confirmed'+p1+p2+'.png', x = 30, y = 15, w =0, h =0)
    
    #Page 2
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.text(10, 10, f"Automatic Report: {p1} - {p2} Deaths")
    pdf.image('./output/graph_deaths'+p1+p2+'.png', x = 30, y = 15, w =0, h =0)
    
    #Page 3
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.text(10, 10, f"Automatic Report: {p1} - {p2}")
    pdf.image('./output/graph_measures'+p1+p2+'.png', x = 30, y = 15, w =0, h =0)

    #Extra comment Page 3
    df_2=df[df['ISO_ALP_2']==p1]
    pop_p1=str(int(df_2["POPULATION"].unique()))
    df_3=df[df['ISO_ALP_2']==p2]
    pop_p2=str(int(df_3["POPULATION"].unique()))    
    pdf.text(140, 10, f"Population {p1}: {pop_p1} - Popupulation {p2}: {pop_p2}")

    #Page 4
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.image('./output/table'+p1+'.png', x = 30, y = 0, w =0, h =0)
    pdf.image('./output/table'+p2+'.png', x = 30, y = 100, w =0, h =0)
    pdf.text(10, 10, f"Automatic Report: {p1} - {p2}")
    pdf.text(140, 10, f"Population {p1}: {pop_p1} - Popupulation {p2}: {pop_p2}")

    #Save Report 
    pdf.output("./output/report.pdf", "F")
