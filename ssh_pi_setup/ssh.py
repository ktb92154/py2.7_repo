#!/usr/bin/python
import sys

def prompt():
    response = sys.stdin.readline().strip()
    return response

fields = [ "Please tell me your name: ", "what school do you go to?: ", "What year are you in?: " ]

answers = []
for field in fields:
    print field,
    v = prompt()
    answers += [v]

print """Hello %s!
You go to %s
and you are in year %s""" % ( answers[0], answers[1], answers[2] )

year = int(answers[2])

if year == 9:
    print "Hope your GCSE\'s are going well."
elif year == 8:
    print "I hope you are studing for your exams!"
else:
   print "Thanks for playing"