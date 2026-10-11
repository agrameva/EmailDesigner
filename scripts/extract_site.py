import urllib.request
import re

url = 'https://simplyadmission.com'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    
    # 1. Logo
    logo = None
    img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    for src in img_tags:
        if 'logo' in src.lower():
            logo = src
            break
            
    # 2. Social Links
    socials = set()
    a_tags = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', html)
    for href in a_tags:
        if any(x in href for x in ['facebook.com', 'instagram.com', 'twitter.com', 'linkedin.com', 'youtube.com']):
            socials.add(href)
            
    # 3. Colors/Fonts
    fonts = set()
    link_tags = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', html)
    for href in link_tags:
        if 'fonts.googleapis.com' in href:
            fonts.add(href)
            
    hex_colors = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', html)
    
    print(f'LOGO: {logo}')
    print(f'SOCIALS: {list(socials)}')
    print(f'FONTS: {list(fonts)}')
    print(f'COLORS: {list(set(hex_colors))[:15]}')
except Exception as e:
    print(f'Error: {e}')
