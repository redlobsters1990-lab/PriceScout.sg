# Affiliate Link Setup Guide for PriceScout.sg

## Shopee Affiliate Program (Shopee Ambassador)

### How to Join
1. Go to: https://affiliate.shopee.sg/
2. Sign up with your Shopee account
3. Wait for approval (usually 1-3 business days)
4. Once approved, you get access to the affiliate dashboard

### How to Create Affiliate Links

#### Method 1: Direct Product Link
1. Find the product on Shopee you want to promote
2. Copy the product URL (e.g., https://shopee.sg/product-name-i.123456789.9876543210)
3. Go to Shopee Affiliate dashboard
4. Paste the URL in "Link Generator"
5. Add your tracking parameters
6. Get your affiliate link

#### Method 2: Search Result Link (Easier)
1. Go to Shopee Affiliate dashboard
2. Use "Search Link Generator"
3. Enter keyword (e.g., "xiaomi air purifier 4")
4. Select your tracking ID
5. Copy the generated link

### Example Affiliate URL Structure

**Before (Regular Link):**
```
https://shopee.sg/Xiaomi-Smart-Air-Purifier-4-Pro-i.178877065.17925278734
```

**After (Affiliate Link):**
```
https://shopee.sg/Xiaomi-Smart-Air-Purifier-4-Pro-i.178877065.17925278734?af_click_lookback=7d&af_reengagement_window=7d&af_siteid=your_account_id&af_sub_siteid=air-purifiers-page&af_viewthrough_lookback=1d&is_retargeting=true&smtt=9&utm_campaign=your_campaign&utm_content=air-purifiers&utm_medium=affiliates&utm_source=an_17105240000
```

## Amazon Associates (Amazon SG)

### How to Join
1. Go to: https://affiliate-program.amazon.sg/
2. Sign up for Amazon Associates
3. Add your website (pricescout.sg)
4. Wait for approval

### How to Create Affiliate Links

#### Method 1: SiteStripe (Easiest)
1. Log into Amazon Associates
2. Visit any Amazon product page
3. Use the SiteStripe toolbar at top
4. Click "Text" or "Image" link
5. Copy the HTML or URL

#### Method 2: Product Link Tool
1. Go to Amazon Associates dashboard
2. Click "Product Linking" → "Product Links"
3. Search for product
4. Click "Get Link"

### Example Affiliate URL Structure

**Before (Regular Link):**
```
https://www.amazon.sg/Xiaomi-Smart-Air-Purifier-EU/dp/B09NDVN6YR
```

**After (Affiliate Link):**
```
https://www.amazon.sg/Xiaomi-Smart-Air-Purifier-EU/dp/B09NDVN6YR?tag=pricescout0c-20
```

## Lazada Affiliate Program

### How to Join
1. Go to: https://affiliate.lazada.sg/
2. Sign up for Lazada Affiliate
3. Wait for approval

### How to Create Links
1. Log into Lazada Affiliate dashboard
2. Use "Link Generator" tool
3. Paste product URL or search term
4. Add tracking parameters
5. Generate link

## How to Update the Website

### Step 1: Find Real Products
Search for actual products that are IN STOCK:
- Go to Shopee/Amazon/Lazada
- Search for product
- Verify it's available
- Copy the exact URL

### Step 2: Create Affiliate Links
Use the methods above to convert regular links to affiliate links

### Step 3: Update the Catalog
Edit this file:
```
/Users/chozengone/.openclaw/workspace-daf-shared/daf/sites/resilience/enhanced_catalog.json
```

Replace `search_url` with your actual affiliate link:
```json
{
  "name": "Xiaomi Smart Air Purifier 4",
  "price_range": "S$150-200",
  "affiliate_url": "https://shopee.sg/...YOUR_AFFILIATE_LINK...",
  "features": [...],
  "best_for": "...",
  "rating": "4.5/5"
}
```

### Step 4: Rebuild Pages
Run the Python script to regenerate HTML with new links

## Commission Rates (Typical)

| Platform | Commission | Cookie Duration |
|----------|-----------|-----------------|
| Shopee | 2-10% | 7 days |
| Amazon SG | 1-10% | 24 hours |
| Lazada | 2-8% | 7 days |

## Best Practices

1. **Disclosure**: Always include disclaimer that you earn commissions
2. **Honest Reviews**: Only recommend products you'd actually use
3. **Update Regularly**: Check links monthly, remove out-of-stock products
4. **Track Performance**: Use different tracking IDs for each page
5. **Price Transparency**: Show price ranges, note prices change

## Quick Start Checklist

- [ ] Sign up for Shopee Affiliate
- [ ] Sign up for Amazon Associates
- [ ] Sign up for Lazada Affiliate
- [ ] Find 5 real products per category
- [ ] Create affiliate links for each
- [ ] Update enhanced_catalog.json
- [ ] Rebuild website
- [ ] Test all links
- [ ] Add disclosure to footer
