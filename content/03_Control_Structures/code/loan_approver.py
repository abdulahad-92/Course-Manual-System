# The Credit Score & Loan Approver

credit_score = 680
annual_revenue = 65000

print("--- LOAN APPLICATION STATUS ---")

if credit_score >= 700 and annual_revenue >= 50000:
    print("Decision: Loan Approved: Prime Rate")
elif 600 <= credit_score <= 699 and annual_revenue >= 50000:
    print("Decision: Loan Approved: Standard Rate")
elif annual_revenue < 50000:
    print("Decision: Loan Denied: Insufficient Revenue")
else:
    print("Decision: Loan Denied: Credit Risk")
