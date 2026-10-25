"""Level 5 Lesson 5 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l5img import *
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('statement', 'statement', ['1f4c4', '1f4b5'], 'STATEMENT', None, 'a page and a dollar bill [sign: STATEMENT]'),
 ('charge', 'charge', ['1f4b8'], 'CHARGE', None, 'money with wings [sign: CHARGE]'),
 ('payment', 'payment', ['1f4b5'], 'PAID', 'check', 'a dollar bill with a green check [sign: PAID]'),
 ('balance', 'balance', ['1f4b0'], 'BALANCE', None, 'a money bag [sign: BALANCE]'),
 ('fee', 'fee', ['1f4b2'], 'FEE', None, 'a large dollar sign [sign: FEE]'),
 ('receipt', 'receipt', ['1f9fe'], 'RECEIPT', None, 'a receipt [sign: RECEIPT]'),
 ('refund', 'refund', ['1f4b5', '1f519'], 'REFUND', None, 'a dollar bill and a BACK arrow [sign: REFUND]'),
 ('budget', 'budget', ['1f4ca'], 'BUDGET', None, 'a bar chart [sign: BUDGET]'),
 ('deposit', 'deposit', ['1f3e6', '1f4b0'], 'DEPOSIT', None, 'a bank and a money bag [sign: DEPOSIT]'),
 ('due_date', 'due date', ['1f4c5'], 'DUE DATE', None, 'a calendar [sign: DUE DATE]'),
 ('account_number', 'account number', ['1f522'], 'ACCT', None, 'the numbers 1, 2, 3, and 4 [sign: ACCT]'),
 ('credit', 'credit', ['1f4c4', '1f4b5'], 'MONEY BACK', 'check', 'a page and a dollar bill with a green check [sign: MONEY BACK]. Money back on a statement, not a loan.'),
]
vocab_run(5, OUT, I)
