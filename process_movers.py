import json

with open('.tmp-cg-markets.json') as f:
    markets = json.load(f)

STABLE_IDS = {
    'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
    'ethena-usde','sky-dollar','usds','ondo-us-dollar-yield','frax','usual-usd',
    'blackrock-usd-institutional-digital-liquidity-fund'
}
WRAPPED = {
    'wrapped-bitcoin','wrapped-eeth','wrapped-steth','staked-ether','weeth',
    'wrapped-beacon-eth','lido-staked-sol','jupiter-staked-sol','solv-protocol-solvbtc',
    'jito-staked-sol','rocket-pool-eth','renzo-restaked-eth','mantle-staked-ether',
    'marinade-staked-sol','wbeth','susds','coinbase-wrapped-btc','coinbase-wrapped-staked-eth',
    'binance-staked-sol','wrapped-bnb','binance-bridged-usdc-bnb-smart-chain',
    'bridged-usdc-polygon-pos-bridge'
}

def is_stable(c):
    if c['id'] in STABLE_IDS:
        return True
    sym = (c.get('symbol') or '').upper()
    name = (c.get('name') or '').lower()
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'):
        return True
    if 'stablecoin' in name:
        return True
    return False

filtered = [
    c for c in markets
    if c.get('total_volume') and c['total_volume'] >= 1_000_000
    and not is_stable(c)
    and c['id'] not in WRAPPED
    and c.get('price_change_percentage_24h') is not None
]

top100 = filtered[:100]
green = sum(1 for c in top100 if c['price_change_percentage_24h'] > 0)
sorted_pct = sorted([c['price_change_percentage_24h'] for c in filtered[:50]])
median50 = sorted_pct[len(sorted_pct)//2] if sorted_pct else 0
print(f"PULSE: green={green}/100, median50={median50:.2f}%")

winners = sorted(filtered, key=lambda c: c['price_change_percentage_24h'], reverse=True)[:10]
losers = sorted(filtered, key=lambda c: c['price_change_percentage_24h'])[:10]

def hum(n):
    if n is None:
        return "?"
    if n >= 1e9:
        return f"${n/1e9:.1f}B"
    if n >= 1e6:
        return f"${n/1e6:.0f}M"
    if n >= 1e3:
        return f"${n/1e3:.0f}k"
    return f"${n:.0f}"

def fmt(coins, label):
    print(f"\n{label}")
    for i, c in enumerate(coins, 1):
        sym = c['symbol'].upper()
        name = c['name']
        price = c['current_price']
        p24 = c['price_change_percentage_24h']
        p7d = c.get('price_change_percentage_7d_in_currency') or 0
        p1h = c.get('price_change_percentage_1h_in_currency') or 0
        vol = c['total_volume']
        mcap = c['market_cap']
        rank = c['market_cap_rank']
        tags = []
        if rank and rank <= 20:
            tags.append('MAJOR')
        if mcap and mcap < 50_000_000:
            tags.append('MICROCAP')
        if rank and rank > 150 and p24 > 30:
            tags.append('PUMP-RISK')
        if p24 > 15 and p7d > 25:
            tags.append('BREAKOUT')
        if p24 > 20 and p7d < 0:
            tags.append('FADE')
        if p24 < -10 and mcap and vol/mcap > 0.25:
            tags.append('CAPITULATION')
        tags = tags[:2]
        if price is None:
            pstr = "?"
        elif price < 0.01:
            pstr = f"${price:.6f}"
        elif price < 1:
            pstr = f"${price:.4f}"
        elif price < 100:
            pstr = f"${price:.2f}"
        else:
            pstr = f"${price:,.0f}"
        tag_str = ' [' + ','.join(tags) + ']' if tags else ''
        print(f"{i}. {sym} ({name}) {pstr} {p24:+.1f}% / 7d {p7d:+.1f}% / 1h {p1h:+.1f}% | {hum(vol)} / #{rank}{tag_str}")

fmt(winners, "WINNERS")
fmt(losers, "LOSERS")

with open('.tmp-cg-trending.json') as f:
    trending = json.load(f)
print("\nTRENDING")
for i, item in enumerate(trending.get('coins', [])[:7], 1):
    c = item['item']
    name = c['name']
    sym = c['symbol']
    rank = c.get('market_cap_rank') or '?'
    data = c.get('data', {})
    pcd = data.get('price_change_percentage_24h', {})
    p24 = pcd.get('usd', 0) if isinstance(pcd, dict) else 0
    price = data.get('price', 0)
    if isinstance(price, str):
        try:
            price = float(price.replace('$','').replace(',',''))
        except:
            price = 0
    print(f"{i}. {name} ({sym}) #{rank} ${price:.6f} {p24:+.1f}%")
