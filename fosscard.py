#!/usr/bin/env python3
"""
FOSScard - Generate Magic-style cards for your open source contributions
Usage: python fosscard.py profile.yaml > output.html
       cat profile.yaml | python fosscard.py > output.html
"""

import sys
import yaml
from pathlib import Path


STYLES = {
    'dark': {
        'bg_gradient': 'linear-gradient(135deg, #000000 0%, #0a0a0a 100%)',
        'card_bg': 'linear-gradient(to bottom, #0d0d0d 0%, #050505 100%)',
        'border_color': '#8b7355',
        'text_color': '#e8e8e8',
        'header_color': '#8b7355',
        'section_bg': 'rgba(139, 115, 85, 0.1)',
        'accent': '#9d8362'
    },
    'light': {
        'bg_gradient': 'linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)',
        'card_bg': 'linear-gradient(to bottom, #ffffff 0%, #f1f3f5 100%)',
        'border_color': '#495057',
        'text_color': '#212529',
        'header_color': '#495057',
        'section_bg': 'rgba(73, 80, 87, 0.05)',
        'accent': '#228be6'
    },
    'matrix': {
        'bg_gradient': 'linear-gradient(135deg, #0d0208 0%, #001b1c 100%)',
        'card_bg': 'linear-gradient(to bottom, #003b00 0%, #001b00 100%)',
        'border_color': '#00ff41',
        'text_color': '#00ff41',
        'header_color': '#00ff41',
        'section_bg': 'rgba(0, 255, 65, 0.1)',
        'accent': '#00cc33'
    },
    'molokai': {
        'bg_gradient': 'linear-gradient(135deg, #1B1D1E 0%, #232526 100%)',
        'card_bg': 'linear-gradient(to bottom, #272822 0%, #1e1f1c 100%)',
        'border_color': '#66D9EF',
        'text_color': '#F8F8F2',
        'header_color': '#F92672',
        'section_bg': 'rgba(102, 217, 239, 0.08)',
        'accent': '#A6E22E'
    }
}


def generate_html(data):
    """Generate HTML for the FOSScard"""
    
    name = data.get('name', 'Anonymous Developer')
    name_link = data.get('link', '')
    logo = data.get('logo', '')
    style_name = data.get('style', 'dark').lower()
    style = STYLES.get(style_name, STYLES['dark'])
    projects = data.get('projects', {})
    
    # Build project sections HTML
    projects_html = ''
    for category, content in projects.items():
        projects_html += f'<div class="category">{category}</div>'
        
        for item_name, item_details in content.items():
            if isinstance(item_details, dict):
                # Check if this is a direct project or a language grouping
                if 'link' in item_details or 'description' in item_details:
                    # Direct project under category
                    link = item_details.get('link', '#')
                    desc = item_details.get('description', '')
                    projects_html += f'''
                    <div class="project">
                        <a href="{link}" class="project-name" target="_blank">{item_name}</a>
                        <span class="project-desc">{desc}</span>
                    </div>
                    '''
                else:
                    # Language grouping with projects underneath
                    projects_html += f'<div class="language">{item_name}</div>'
                    for proj_name, proj_details in item_details.items():
                        if isinstance(proj_details, dict):
                            link = proj_details.get('link', '#')
                            desc = proj_details.get('description', '')
                            projects_html += f'''
                            <div class="project">
                                <a href="{link}" class="project-name" target="_blank">{proj_name}</a>
                                <span class="project-desc">{desc}</span>
                            </div>
                            '''
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - FOSScard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: {style['bg_gradient']};
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }}
        
        .card {{
            width: 480px;
            background: {style['card_bg']};
            border: 2px solid {style['border_color']};
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5),
                        0 0 20px {style['border_color']}40;
            overflow: hidden;
            position: relative;
        }}
        
        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, 
                {style['border_color']}, 
                {style['accent']}, 
                {style['border_color']});
        }}
        
        .header {{
            padding: 20px;
            background: {style['section_bg']};
            border-bottom: 2px solid {style['border_color']};
            position: relative;
        }}
        
        .logo {{
            width: 60px;
            height: 60px;
            border-radius: 50%;
            border: 2px solid {style['border_color']};
            margin: 0 auto 12px;
            display: block;
            object-fit: cover;
        }}
        
        .name {{
            font-size: 22px;
            font-weight: bold;
            color: {style['header_color']};
            text-align: center;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        }}
        
        .content {{
            padding: 20px;
            max-height: 640px;
            overflow-y: auto;
            color: {style['text_color']};
        }}
        
        .content::-webkit-scrollbar {{
            width: 4px;
        }}
        
        .content::-webkit-scrollbar-track {{
            background: {style['section_bg']};
            border-radius: 4px;
        }}
        
        .content::-webkit-scrollbar-thumb {{
            background: {style['border_color']};
            border-radius: 4px;
        }}
        
        .category {{
            font-size: 16px;
            font-weight: bold;
            color: {style['header_color']};
            margin: 16px 0 8px 0;
            padding: 6px 10px;
            background: {style['section_bg']};
            border-left: 3px solid {style['accent']};
            border-radius: 4px;
        }}
        
        .category:first-child {{
            margin-top: 0;
        }}
        
        .language {{
            font-size: 13px;
            font-weight: 600;
            color: {style['accent']};
            margin: 10px 0 6px 10px;
            opacity: 0.9;
        }}
        
        .project {{
            margin: 8px 0 8px 20px;
            font-size: 12px;
            line-height: 1.6;
        }}
        
        .project-name {{
            font-weight: 600;
            color: {style['text_color']};
            display: block;
            margin-bottom: 2px;
        }}
        
        .project-desc {{
            color: {style['text_color']};
            opacity: 0.8;
            display: block;
            font-size: 11px;
        }}
        
        .footer {{
            padding: 12px 20px;
            background: {style['section_bg']};
            border-top: 2px solid {style['border_color']};
            text-align: center;
            font-size: 10px;
            color: {style['text_color']};
            opacity: 0.6;
        }}
        
        @media print {{
            body {{
                background: white;
            }}
            .card {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            {f'<img src="{logo}" alt="Logo" class="logo">' if logo else ''}
            <div class="name">{f'<a href="{name_link}" class="name" target="_blank">{name}</a>' if name_link else name}</div>
        </div>
        

        <div class="content">
            {projects_html}
        </div>
        
        <div class="footer">
            FOSScard • Open Source Contribution Card
        </div>
    </div>
</body>
</html>'''
    
    return html


def main():
    """Main entry point"""
    
    # Check if input is from stdin or file argument
    if len(sys.argv) > 1:
        yaml_file = Path(sys.argv[1])
        if not yaml_file.exists():
            print(f"Error: File '{yaml_file}' not found", file=sys.stderr)
            sys.exit(1)
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
    else:
        # Read from stdin
        data = yaml.safe_load(sys.stdin)
    
    html = generate_html(data)
    print(html)


if __name__ == '__main__':
    main()
