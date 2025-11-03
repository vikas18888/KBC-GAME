# KBC.py
import sys

# Ensure UTF-8 output in VS Code
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')



print("🎉 WELCOME TO KBC 🎉")
print("----------------------------")


print("ROUND 1")
print("Q1: WHICH IS THE CAPITAL OF INDIA?")
q1 = ["A. MUMBAI", "B. DELHI", "C. KOLKATA", "D. RAJASTHAN"]
for option in q1:
    print(option)
user = input("ENTER YOUR ANSWER (A/B/C/D or CITY NAME): ").strip().lower()

if user in ("b", "delhi"):
    print("✅ CONGRATULATIONS! YOU CLEARED ROUND 1 🎉\n")
else:
    print("❌ SORRY, THIS IS THE WRONG ANSWER. YOU ARE ELIMINATED.\n")
    sys.exit()
users=input("WANT TO PLAY MORE?").strip().lower()
if users=="yes":
    print("LETS BEGIN ROUND 2")
    
else:
    print("YOU ARE NO LONGER PART OF GAME")
    sys.exit()


print("ROUND 2")
print("Q2: WHO IS THE MOST FAMOUS CRICKET PLAYER IN THE WORLD?")
q2 = ["A. VIRAT", "B. ROHIT", "C. DHONI", "D. RAHUL"]
for option in q2:
    print(option)
user = input("ENTER YOUR ANSWER: ").strip().lower()

if user in ("a", "virat"):
    print("✅ CONGRATULATIONS! YOU CLEARED ROUND 2 🎉\n")
else:
    print("❌ SORRY, THIS IS THE WRONG ANSWER. YOU ARE ELIMINATED.\n")
    sys.exit()
users=input("WANT TO PLAY MORE?").strip().lower()
if users=="yes":
    print("LETS BEGIN ROUND 2")
    
else:
    print("YOU ARE NO LONGER PART OF GAME")
    sys.exit()

print("🎯 FINAL ROUND 🎯")
print("Q3: WHICH DEVICE IS USED TO MEASURE TEMPERATURE?")
q3 = ["A. BAROMETER", "B. THERMOMETER", "C. SPEEDOMETER", "D. AMMETER"]
for option in q3:
    print(option)
user = input("ENTER YOUR ANSWER: ").strip().lower()

if user in ("b", "thermometer"):
    print("🏆 CONGRATULATIONS! YOU CLEARED THE FINAL ROUND! 🏆")
    print("💰 YOU WON ₹7 CRORE 💰")
else:
    print("❌ SORRY, WRONG ANSWER. YOU ARE ELIMINATED.\n")
