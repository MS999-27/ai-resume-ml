from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import cm
import os


def build_pdf(resume_text: str, name: str, output_path: str = "resume_output.pdf"):
    """
    Converts plain resume text into a professionally formatted PDF
    using ReportLab library.
    """
    print("📄 Building PDF with ReportLab...")
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Color scheme
    DARK = HexColor("#1a1a2e")
    PURPLE = HexColor("#7c3aed")
    GRAY = HexColor("#64748b")
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Title'],
        fontSize=24,
        textColor=DARK,
        fontName='Helvetica-Bold',
        spaceAfter=4
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=PURPLE,
        fontName='Helvetica-Bold',
        spaceBefore=12,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=DARK,
        leading=16,
        spaceAfter=4
    )
    
    story = []
    
    # Name header
    story.append(Paragraph(name, name_style))
    story.append(HRFlowable(width="100%", thickness=2, color=PURPLE))
    story.append(Spacer(1, 0.3*cm))
    
    # Parse and format resume sections
    lines = resume_text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            story.append(Spacer(1, 0.2*cm))
            continue
        
        # Section headers (lines with === or ALL CAPS)
        if "===" in line or (line.isupper() and len(line) > 3):
            clean = line.replace("=", "").strip()
            story.append(Paragraph(clean, section_style))
            story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
        elif line.startswith("•") or line.startswith("-"):
            story.append(Paragraph(f"&nbsp;&nbsp;{line}", body_style))
        else:
            story.append(Paragraph(line, body_style))
    
    doc.build(story)
    print(f"✅ PDF saved: {output_path}")
    return output_path