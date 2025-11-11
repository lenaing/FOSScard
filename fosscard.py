#!/usr/bin/env python3
"""
FOSScard - Generate Magic-style cards for your open source contributions
Usage: python fosscard.py profile.yaml > output.html
       cat profile.yaml | python fosscard.py > output.html
"""

import sys
import yaml
from pathlib import Path

STYLES_DIR = 'styles'

def load_style(name):
    """Load Style for the FOSScard"""

    style_file = Path(f"{STYLES_DIR}").joinpath(f"{name}.yaml")

    if not style_file.exists():
        raise ValueError(f"No such style: '{name}'")

    with open(style_file, 'r') as f:
        data = yaml.safe_load(f)

    return data

def generate_html(data):
    """Generate HTML for the FOSScard"""

    name = data.get('name', 'Anonymous Developer')
    name_link = data.get('link', '')
    logo = data.get('logo', '')
    header_background = data.get('header_background', '')

    # If header_background is a URL (not already wrapped in url()), wrap it
    if header_background and (header_background.startswith('http://') or header_background.startswith('https://')):
        if not header_background.startswith('url('):
            header_background = f"url('{header_background}')"

    style_name = data.get('style', 'dark').lower()
    style = load_style(style_name)['style']

    # If footer_background is not present in the style, use section_background
    if 'footer_background' not in style:
        style['footer_background'] = style['section_background']

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
                    link = item_details.get('link', '')
                    desc = item_details.get('description', '')
                    complexity = item_details.get('complexity', 0)
                    # Choose color based on complexity level
                    if complexity < 3:
                        complexity_indicator = '🟩' * complexity
                    elif complexity < 5:
                        complexity_indicator = '🟨' * complexity
                    elif complexity > 4:
                        complexity_indicator = '🟥' * complexity
                    else:
                        complexity_indicator = ''
                    if link:
                        project_name_html = f'<a href="{link}" class="project-name" target="_blank">{item_name}</a>'
                    else:
                        project_name_html = f'<span class="project-name">{item_name}</span>'
                    if complexity_indicator:
                        project_name_html += f' <span class="complexity">{complexity_indicator}</span>'
                    projects_html += f'''
                    <div class="project">
                        {project_name_html}
                        <span class="project-desc">{desc}</span>
                    </div>
                    '''
                else:
                    # Language grouping with projects underneath
                    projects_html += f'<div class="language">{item_name}</div>'
                    for proj_name, proj_details in item_details.items():
                        if isinstance(proj_details, dict):
                            link = proj_details.get('link', '')
                            desc = proj_details.get('description', '')
                            complexity = proj_details.get('complexity', 0)
                            # Choose color based on complexity level
                            if complexity >= 5:
                                complexity_indicator = '🟥' * complexity
                            elif 3 <= complexity <= 4:
                                complexity_indicator = '🟨' * complexity
                            elif 1 <= complexity <= 2:
                                complexity_indicator = '🟩' * complexity
                            else:
                                complexity_indicator = ''
                            if link:
                                project_name_html = f'<a href="{link}" class="project-name" target="_blank">{proj_name}</a>'
                            else:
                                project_name_html = f'<span class="project-name">{proj_name}</span>'
                            if complexity_indicator:
                                project_name_html += f' <span class="complexity">{complexity_indicator}</span>'
                            projects_html += f'''
                            <div class="project">
                                {project_name_html}
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
            background: {style['background']};
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }}

        .card {{
            width: 480px;
            background: {style['card_background']};
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
            background: {header_background if header_background else style['section_background']};
            background-size: cover;
            background-position: center;
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
            background: {style['section_background']};
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
            background: {style['section_background']};
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
            background: {style['section_background']};
            border-left: 3px solid {style['accent']};
            border-radius: 4px;
        }}

        .category:first-child {{
            margin-top: 0;
        }}

        .language {{
            font-size: 15px;
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
            font-size: 14px;
            font-weight: 600;
            color: {style['text_color']};
            display: inline;
            margin-bottom: 2px;
        }}

        .complexity {{
            font-size: 10px;
            margin-left: 4px;
        }}

        .project-desc {{
            color: {style['text_color']};
            opacity: 0.8;
            display: block;
            font-size: 11px;
        }}

        .footer {{
            padding: 12px 20px;
            background: {style['footer_background']};
            border-top: 2px solid {style['border_color']};
            text-align: center;
            font-size: 10px;
            color: {style['text_color']};
            opacity: 0.6;
        }}

        .footer a {{
            color: {style['header_color']};
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
            <a href="https://github.com/iMilnb/FOSScard">FOSScard</a> • Open Source Contribution Card
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
