#!/usr/bin/env python3
"""
Generate final website pages with YOUR affiliate links.

Usage:
1. Copy affiliate_catalog_TEMPLATE.json to affiliate_catalog.json
2. Replace "YOUR_AFFILIATE_LINK_HERE" with your actual affiliate links
3. Run: python3 generate_with_affiliate_links.py
4. Pages will be created in output/ folder
"""

import json
from pathlib import Path
from datetime import datetime

def generate_page(slug, data):
    """Generate beautiful product page with affiliate links."""
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Best {data['title']} Singapore 2026 | Compare & Save</title>
    <meta name="description" content="{data['tagline']}">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #0071e3;
            --primary-dark: #0051a2;
            --text: #1d1d1f;
            --text-secondary: #86868b;
            --bg: #f5f5f7;
            --card: #ffffff;
            --success: #34c759;
        }}
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
        }}
        
        /* Navigation */
        nav {{
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }}
        nav .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        nav .logo {{
            font-size: 20px;
            font-weight: 700;
            color: var(--text);
            text-decoration: none;
        }}
        nav .back {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
        }}
        nav .back:hover {{ text-decoration: underline; }}
        
        /* Hero */
        .hero {{
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: white;
            padding: 80px 20px 60px;
            text-align: center;
        }}
        .hero h1 {{
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 20px;
            line-height: 1.1;
        }}
        .hero .tagline {{
            font-size: 20px;
            opacity: 0.9;
            margin-bottom: 30px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        /* Why Section */
        .why-section {{
            background: white;
            padding: 60px 20px;
        }}
        .why-section .container {{
            max-width: 800px;
            margin: 0 auto;
        }}
        .why-section h2 {{
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 20px;
            text-align: center;
        }}
        .why-section p {{
            font-size: 17px;
            line-height: 1.8;
            color: var(--text-secondary);
        }}
        
        /* Products */
        .products {{
            padding: 60px 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .products h2 {{
            font-size: 32px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 15px;
        }}
        .products .subtitle {{
            text-align: center;
            color: var(--text-secondary);
            margin-bottom: 40px;
        }}
        
        /* Product Cards */
        .product-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
        }}
        .product-card {{
            background: white;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        .product-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        }}
        .product-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            position: relative;
        }}
        .product-card.featured .product-header {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }}
        .product-header .badge {{
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(255,255,255,0.2);
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }}
        .product-header h3 {{
            font-size: 22px;
            font-weight: 600;
            margin-bottom: 8px;
            padding-right: 80px;
        }}
        .product-header .price-range {{
            font-size: 28px;
            font-weight: 700;
        }}
        .product-header .rating {{
            font-size: 14px;
            opacity: 0.9;
            margin-top: 5px;
        }}
        
        .product-body {{
            padding: 25px;
        }}
        .product-body .best-for {{
            background: #f0f7ff;
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 14px;
            color: var(--primary);
            margin-bottom: 15px;
            font-weight: 500;
        }}
        .product-body h4 {{
            font-size: 14px;
            font-weight: 600;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
        }}
        .product-body ul {{
            list-style: none;
            margin-bottom: 20px;
        }}
        .product-body li {{
            padding: 6px 0;
            padding-left: 20px;
            position: relative;
            font-size: 14px;
        }}
        .product-body li::before {{
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--success);
            font-weight: 700;
        }}
        
        .btn {{
            display: block;
            background: var(--primary);
            color: white;
            text-align: center;
            padding: 14px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
            transition: background 0.3s;
        }}
        .btn:hover {{ background: var(--primary-dark); }}
        
        /* Disclaimer */
        .disclaimer {{
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 20px;
            margin: 40px 20px;
            border-radius: 10px;
            max-width: 1160px;
            margin-left: auto;
            margin-right: auto;
        }}
        .disclaimer h4 {{
            color: #856404;
            margin-bottom: 10px;
        }}
        .disclaimer p {{
            color: #856404;
            font-size: 14px;
            line-height: 1.6;
        }}
        
        /* Footer */
        footer {{
            background: #1a1a2e;
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}
        footer p {{
            opacity: 0.7;
            font-size: 14px;
            margin: 5px 0;
        }}
        footer .affiliate-note {{
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
            font-size: 12px;
            opacity: 0.5;
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 32px; }}
            .product-grid {{ grid-template-columns: 1fr; }}
            .why-section h2, .products h2 {{ font-size: 24px; }}
        }}
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="../index.html" class="logo">PriceScout</a>
            <a href="../index.html" class="back">← Back</a>
        </div>
    </nav>
    
    <section class="hero">
        <h1>Best {data['title']} Singapore</h1>
        <p class="tagline">{data['tagline']}</p>
    </section>
    
    <section class="why-section">
        <div class="container">
            <h2>Why You Need a {data['title'].rstrip('s')}</h2>
            <p>{data['why_need']}</p>
        </div>
    </section>
    
    <div class="disclaimer">
        <h4>⚠️ Important Notice</h4>
        <p>Prices and availability change frequently. We earn a small commission if you purchase through our links (at no extra cost to you). This helps us maintain the site and continue providing comparisons. Always check the current price on the retailer's site before purchasing.</p>
    </div>
    
    <section class="products">
        <h2>Top 5 {data['title']} Compared</h2>
        <p class="subtitle">Click "View on [Store]" to check today's best price</p>
        
        <div class="product-grid">
'''
    
    # Add product cards
    for i, product in enumerate(data['products'], 1):
        featured_class = ' featured' if i == 1 else ''
        badge = '<span class="badge">Best Value</span>' if i == 1 else ''
        
        features_html = '\n'.join([f'<li>{f}</li>' for f in product['features']])
        
        # Determine store name from URL
        url = product.get('affiliate_url', '')
        if 'shopee' in url.lower():
            store_name = 'Shopee'
        elif 'amazon' in url.lower():
            store_name = 'Amazon'
        elif 'lazada' in url.lower():
            store_name = 'Lazada'
        else:
            store_name = 'Store'
        
        html += f'''            <div class="product-card{featured_class}">
                <div class="product-header">
                    {badge}
                    <h3>#{i} {product['name']}</h3>
                    <div class="price-range">{product['price_range']}</div>
                    <div class="rating">{'★' * int(float(product['rating'].split('/')[0]))} {product['rating']}</div>
                </div>
                <div class="product-body">
                    <div class="best-for">💡 Best for: {product['best_for']}</div>
                    <h4>Key Features</h4>
                    <ul>
                        {features_html}
                    </ul>
                    <a href="{product.get('affiliate_url', '#')}" class="btn" target="_blank" rel="nofollow noopener">View on {store_name} →</a>
                </div>
            </div>
'''
    
    html += f'''        </div>
    </section>
    
    <footer>
        <p>© 2026 PriceScout.sg — Singapore Product Comparisons</p>
        <p>Prices verified from Amazon SG, Shopee, Lazada, Courts, Best Denki</p>
        <p class="affiliate-note">This site contains affiliate links. We earn commissions on qualifying purchases.</p>
    </footer>
</body>
</html>'''
    
    return html

def main():
    """Generate all pages from affiliate catalog."""
    
    # Load catalog
    catalog_path = Path('affiliate_catalog.json')
    if not catalog_path.exists():
        print("❌ Error: affiliate_catalog.json not found!")
        print("Please copy affiliate_catalog_TEMPLATE.json to affiliate_catalog.json")
        print("Then replace YOUR_AFFILIATE_LINK_HERE with your actual affiliate links.")
        return
    
    with open(catalog_path, 'r') as f:
        catalog = json.load(f)
    
    # Create output directory
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    
    # Generate pages
    for slug, data in catalog.items():
        if slug.startswith('_'):
            continue
        
        html = generate_page(slug, data)
        (output_dir / f'{slug}.html').write_text(html)
        print(f"✓ Generated: {slug}.html")
    
    print(f"\n✅ All pages created in: {output_dir.absolute()}")
    print("\nNext steps:")
    print("1. Copy these files to your web server")
    print("2. Test all affiliate links work")
    print("3. Update links if products go out of stock")

if __name__ == '__main__':
    main()
