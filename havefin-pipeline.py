# %% [code]
import pandas as pd

def loan_payment(p, rate, years):
    r = rate / 12; n = years * 12
    return p * r / (1 - (1 + r) ** (-n))

bal, rows = 150000.0, []
pay = loan_payment(bal, 0.065, 15)
saved = 0.0
for m in range(1, 15 * 12 + 1):
    interest = bal * 0.065 / 12
    bal = max(bal - (pay - interest), 0)
    saved = saved * (1 + 0.04 / 12) + 500
    rows.append((m, pay, interest, bal, saved))
df = pd.DataFrame(rows, columns=["month", "payment", "interest", "balance", "saved_balance"])
df.to_csv("havefin_schedule.csv", index=False)
print(df.tail())
