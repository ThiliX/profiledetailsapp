import sys
import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def add_hyperlink(paragraph, url, text, color="004B91", underline=True):
    """Adds a clickable hyperlink to a docx paragraph."""
    part = paragraph.part
    r_id = part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)

    hyperlink = parse_xml(f'<w:hyperlink {nsdecls("w")} xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:id="{r_id}"/>')
    new_run = parse_xml(f'<w:r {nsdecls("w")}><w:rPr><w:color w:val="{color}"/><w:u w:val="single"/></w:rPr><w:t>{text}</w:t></w:r>')
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)

def create_document(index_no="YOUR_STUDENT_INDEX", repo_url="https://github.com/YOUR_USERNAME/profiledetailsapp", student_name="Thilina Wickramanayake"):
    doc = Document()

    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Title
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(8)
    title_p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = title_p.add_run("Mobile Application Development")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(26, 26, 26)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(20)
    sub_p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run("Practical Submission - Profile Details App (React Native)")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(13)
    run_sub.font.color.rgb = RGBColor(100, 100, 100)

    # Horizontal divider rule
    divider_p = doc.add_paragraph()
    divider_p.paragraph_format.space_after = Pt(16)
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="1" w:color="CCCCCC"/></w:pBdr>')
    divider_p._p.get_or_add_pPr().append(pBdr)

    # Submission Information Table
    h_info = doc.add_paragraph()
    h_info.paragraph_format.space_after = Pt(8)
    r_h = h_info.add_run("Student & Submission Details")
    r_h.font.name = "Arial"
    r_h.font.size = Pt(14)
    r_h.font.bold = True
    r_h.font.color.rgb = RGBColor(30, 30, 30)

    table = doc.add_table(rows=4, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    data = [
        ("Student Index Number", index_no),
        ("Student Name", student_name),
        ("Technology Stack", "React Native (Expo SDK 57), JavaScript"),
        ("Public Git Repository", repo_url)
    ]

    for i, (label, val) in enumerate(data):
        row = table.rows[i]
        
        # Label cell
        c0 = row.cells[0]
        c0.width = Inches(2.2)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(6)
        p0.paragraph_format.space_after = Pt(6)
        r0 = p0.add_run(label)
        r0.font.name = "Arial"
        r0.font.size = Pt(10.5)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(50, 50, 50)
        
        # Value cell
        c1 = row.cells[1]
        c1.width = Inches(4.3)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(6)
        p1.paragraph_format.space_after = Pt(6)
        
        if label == "Public Git Repository":
            add_hyperlink(p1, val, val)
        else:
            r1 = p1.add_run(val)
            r1.font.name = "Arial"
            r1.font.size = Pt(10.5)
            r1.font.color.rgb = RGBColor(20, 20, 20)
            if label == "Student Index Number":
                r1.font.bold = True

        # Subtle cell borders & shading
        shading0 = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F4F6F8"/>')
        c0._tc.get_or_add_tcPr().append(shading0)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Git Repository Details Section
    h_repo = doc.add_paragraph()
    h_repo.paragraph_format.space_before = Pt(12)
    h_repo.paragraph_format.space_after = Pt(6)
    r_repo = h_repo.add_run("Public Git Repository URL")
    r_repo.font.name = "Arial"
    r_repo.font.size = Pt(14)
    r_repo.font.bold = True
    r_repo.font.color.rgb = RGBColor(30, 30, 30)

    p_repo_box = doc.add_paragraph()
    p_repo_box.paragraph_format.space_after = Pt(16)
    run_url_label = p_repo_box.add_run("Repository Link: ")
    run_url_label.font.name = "Arial"
    run_url_label.font.bold = True
    run_url_label.font.size = Pt(11)
    add_hyperlink(p_repo_box, repo_url, repo_url)

    # Overview of Solution Implementation
    h_sol = doc.add_paragraph()
    h_sol.paragraph_format.space_before = Pt(10)
    h_sol.paragraph_format.space_after = Pt(6)
    r_sol = h_sol.add_run("Solution Implementation Summary")
    r_sol.font.name = "Arial"
    r_sol.font.size = Pt(14)
    r_sol.font.bold = True
    r_sol.font.color.rgb = RGBColor(30, 30, 30)

    features = [
        "Header Navigation: Styled top AppBar displaying 'My Profile' in bold centered text.",
        "Profile Avatar: Circular avatar component featuring user illustration and verified checkmark badge.",
        "User Information: Displays user Name ('Diluka') and Institutional Email ('diluka.w@nsbm.ac.lk') with vector mail icon.",
        "Interactive Points Counter: Dynamic Points state initialized to 0 with a star vector icon.",
        "Floating Action Button (FAB): Positioned at the bottom-right, allowing the user to interactively increment points count upon click/tap.",
        "Cross-Platform Compatibility: Engineered with Expo and React Native, fully operational across Android, iOS, and Web."
    ]

    for f in features:
        p_f = doc.add_paragraph(style='List Bullet')
        p_f.paragraph_format.space_before = Pt(2)
        p_f.paragraph_format.space_after = Pt(3)
        r_f = p_f.add_run(f)
        r_f.font.name = "Arial"
        r_f.font.size = Pt(10.5)

    # Reference Image
    if os.path.exists("sample.png"):
        doc.add_paragraph().paragraph_format.space_after = Pt(8)
        h_img = doc.add_paragraph()
        h_img.paragraph_format.space_after = Pt(6)
        r_img = h_img.add_run("Design Reference (sample.png)")
        r_img.font.name = "Arial"
        r_img.font.size = Pt(13)
        r_img.font.bold = True

        p_img = doc.add_paragraph()
        p_img.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(16)
        doc.add_picture("sample.png", width=Inches(2.5))
        
        caption = doc.add_paragraph()
        caption.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.paragraph_format.space_after = Pt(12)
        r_cap = caption.add_run("Figure 1: UI Reference Specification")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(9.5)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(120, 120, 120)

    filename = f"{index_no}.docx" if index_no != "YOUR_STUDENT_INDEX" else "Submission_Document.docx"
    doc.save(filename)
    print(f"Document created successfully: {filename}")
    return filename

if __name__ == "__main__":
    idx = sys.argv[1] if len(sys.argv) > 1 else "YOUR_STUDENT_INDEX"
    url = sys.argv[2] if len(sys.argv) > 2 else "https://github.com/YOUR_USERNAME/profiledetailsapp"
    name = sys.argv[3] if len(sys.argv) > 3 else "Thilina Wickramanayake"
    create_document(idx, url, name)
