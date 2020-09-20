#!/usr/bin/python3
# Project Name: Insights
# Author: Andrew Eng
# Original Creation Date: 2020-09-20
# Summary: This is the Myers Briggs Personality Test.  This initial code base is taken from the MBTI Self Scorable Form by Katharine C. Briggs and Isabel Briggs Myers.  

# Version Control

e = 0
s = 0
t = 0
j = 0
i = 0
n = 0
f = 0
p = 0
response = ""
questions = ""
preference = []

# Evaluate J and P
def eval(evaluation, response, question):
	# Questions Part 1: 1, 10, 20, 9
	# Questions Part 2: 28, 36, 43, 49
	# Questions Part 3: 59, 70, 58
	global e, s, t, j, i, n, f, p

	def invalid():
		print("##########################################")
		print("\n>>>> Invalid Response, try again: <<<<\n")
		print("##########################################")
		response = input(question)
		eval(evaluation, response.lower(), question)

	if evaluation == "jp":
		if response == "a":
			j = j+1
			return j
		if response == "b":
			p = p+1
			return p
		else:
			invalid()

	if evaluation == "pj":
		if response == "a":
			p = p+1
			return p
		if response == "b":
			j = j+1
			return j
		else:
			invalid()

	if evaluation == "ie":
		if response == "a":
			i = i+1
			return i
		if response == "b":
			e = e+1
			return e
		else:
			invalid()

	if evaluation == "ei":
		if response == "a":
			e = e+1
			return e
		if response == "b":
			i = i+1
			return i
		else:
			invalid()

	if evaluation == "sn":
		if response == "a":
			s = s+1
			return s
		if response == "b":
			n = n+1
			return n
		else:
			invalid()

	if evaluation == "ns":
		if response == "a":
			n = n+1
			return n
		if response == "b":
			s = s+1
			return s
		else:
			invalid()

	if evaluation == "ft":
		if response == "a":
			f = f+1
			return f
		if response == "b":
			t = t+1
			return t
		else:
			invalid()

	if evaluation == "tf":
		if response == "a":
			t = t+1
			return t
		if response == "b":
			f = f+1
			return f
		else:
			invalid()

def part1():
	print("\n###############################################################################")
	print("#### Which answer comes closest to describing how you usually feel or act? ####")
	print("###############################################################################")

def part2():
	print("\n###################################################################################################################################")
	print("#### Which word in each pair appeals to you more?  Think about what the words mean, not about how they look or how they sound. ####")
	print("###################################################################################################################################")

def part3():
	print("\n###############################################################################")
	print("#### Which answer comes closest to describing how you usually feel or act? ####")
	print("###############################################################################")

def part4(): 
	print("\n###################################################################################################################################")
	print("#### Which word in each pair appeals to you more?  Think about what the words mean, not about how they look or how they sound. ####")
	print("###################################################################################################################################")

def execute(que_no, question, answer_a, answer_b, mb):
	request = f"\n{que_no}. {question} {answer_a}\n {answer_b}\n Input: "
	response = input(request)
	eval(mb, response.lower(), request)

part1()
que_no = 1
answer_a = " [a] plan what you do and when"
answer_b = " [b] just go?"
question = "When you go somewhere for the day, would you rather\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 2
answer_a = " [a] more of a spontaneous person"
answer_b = " [b] more of an organized person?"
question = "Do you consider yourself to be\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 3
answer_a = " [a] fact Courses"
answer_b = " [b] courses involving theory?"
question = "If you were a teacher, would you rather teach\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 4
answer_a = " [a] a good mixer"
answer_b = " [b] rather quiet and reserved?"
question = "Are you usually\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 5
answer_a = " [a] imaginative people"
answer_b = " [b] realistic people"
question = "Do you usually get along better with\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 6
answer_a = " [a] your heart rules your head"
answer_b = " [b] your head rules your heart"
question = "Do you more often let\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 7
answer_a = " [a] on the spur of the moment"
answer_b = " [b] according to your plans"
question = "Do you prefer to do many things\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 8
answer_a = " [a] easy to get to know"
answer_b = " [b] hard to get to know"
question = "Are you\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 9
answer_a = " [a] appeal to you"
answer_b = " [b] cramp you?"
question = "Does following a schedule\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 10
answer_a = " [a] organize it carefully before you start"
answer_b = " [b] find out what is necessary as you go along"
question = "When you have a special job to do, do you like to\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 11
answer_a = " [a] go with the flow"
answer_b = " [b] follow a schedule?"
question = "In most instances, do you prefer to\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 12
answer_a = " [a] private person"
answer_b = " [b] a very open person?"
question = "Would most people say you are\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 13
answer_a = " [a] a practical person"
answer_b = " [b] an ingenious person?"
question = "Would you rather be considered\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 14
answer_a = " [a] introduce others"
answer_b = " [b] get introduced?"
question = "In a large group do you more often\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 15
answer_a = " [a] is always coming up with new ideas"
answer_b = " [b] has both feet on the ground?"
question = "Would you rather have as a friend someone who\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 16
answer_a = " [a] value sentiment more than logic"
answer_b = " [b] value logic more than sentiment?"
question = "Are you inclined to\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 17
answer_a = " [a] wait and see what happens and then make plans"
answer_b = " [b] plan things far in advance?"
question = "Do you prefer to\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 18
answer_a = " [a] by yourself"
answer_b = " [b] with others?"
question = "Do you tend to spend a lot of time\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 19
answer_a = " [a] gives you more energy"
answer_b = " [b] is often draining?"
question = "Do you find being around a lot of people\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 20
answer_a = " [a] arrange dates, parties, etc, well in advance"
answer_b = " [b] be free to do whatver looks like fun when the time comes?"
question = "Do you prefer to\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 21
answer_a = " [a] most of the time do whatever you feel like that day"
answer_b = " [b] know ahead of time what you'll be doing most days?"
question = "In planning a trip would you prefer to\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 22
answer_a = " [a] sometimes get bored"
answer_b = " [b] always have fun?"
question = "At parties, do you\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 23
answer_a = " [a] mingle well with others"
answer_b = " [b] tend to keep more to yourself?"
question = "Do you usually\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 24
answer_a = " [a] a person with a quicksand brilliant mind"
answer_b = " [b] a practical person with a lot of common sense?"
question = "Are you more attracted to\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 25
answer_a = " [a] rather enjoy an emergency that makes you work against time"
answer_b = " [b] usually plan your work so you won't need to work under pressure?"
question = "In your daily work, do you\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

part1()
que_no = 26
answer_a = " [a] a lot of time to get to know you"
answer_b = " [b] a little time to get to know you"
question = "Would you say it generally takes others\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

part2()
que_no = 27
answer_a = " [a] Private"
answer_b = " [b] Open"
question = "Evaluate:\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

# I started flipping que_no and the parts(), found it easier this way... c
# Clean up the above code

que_no = 28
part2()
answer_a = " [a] Scheduled"
answer_b = " [b] Unplanned"
question = "Evaluate:\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 29
part2()
answer_a = " [a] Abstract"
answer_b = " [b] Solid"
question = "Evaluate:\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 30
part2()
answer_a = " [a] Gentle"
answer_b = " [b] Firm"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 31
part2()
answer_a = " [a] Thinking"
answer_b = " [b] Feeling"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 32
part2()
answer_a = " [a] Facts"
answer_b = " [b] Ideas"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 33
part2()
answer_a = " [a] Impulse"
answer_b = " [b] Decision"
question = "Evaluate:\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 34
part2()
answer_a = " [a] Hearty"
answer_b = " [b] Quiet"
question = "Evaluate:\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 35
part2()
answer_a = " [a] Quiet"
answer_b = " [b] Outgoing"
question = "Evaluate:\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 36
part2()
answer_a = " [a] Systematic"
answer_b = " [b] Casual"
question = "Evaluate:\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 37
part2()
answer_a = " [a] Theory"
answer_b = " [b] Certainty"
question = "Evaluate:\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 38
part2()
answer_a = " [a] Sensitive"
answer_b = " [b] Just"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 39
part2()
answer_a = " [a] Convincing"
answer_b = " [b] Touching"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 40
part2()
answer_a = " [a] Statement"
answer_b = " [b] Concept"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 41
part2()
answer_a = " [a] Unconstrained"
answer_b = " [b] Scheduled"
question = "Evaluate:\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 42
part2()
answer_a = " [a] Reserved"
answer_b = " [b] Talkative"
question = "Evaluate:\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 43
part2()
answer_a = " [a] Orderly"
answer_b = " [b] Easygoing"
question = "Evaluate:\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 44
part2()
answer_a = " [a] Idea"
answer_b = " [b] Actuality"
question = "Evaluate:\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 45
part2()
answer_a = " [a] Compassion"
answer_b = " [b] Foresight"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 46
part2()
answer_a = " [a] Benefits"
answer_b = " [b] Blessings"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 47
part2()
answer_a = " [a] No-nonsense"
answer_b = " [b] Theoretical"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 48
part2()
answer_a = " [a] Few Friends"
answer_b = " [b] Lots of Friends"
question = "Evaluate:\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 49
part2()
answer_a = " [a] Systematic"
answer_b = " [b] Spontaneous"
question = "Evaluate:\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 50
part2()
answer_a = " [a] Imaginative"
answer_b = " [b] Matter-of-fact"
question = "Evaluate:\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 51
part2()
answer_a = " [a] Warm"
answer_b = " [b] Objective"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 52
part2()
answer_a = " [a] Objective"
answer_b = " [b] Passionate"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 53
part2()
answer_a = " [a] Build"
answer_b = " [b] Invent"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 54
part2()
answer_a = " [a] Quiet"
answer_b = " [b] Gregarious"
question = "Evaluate:\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 55
part2()
answer_a = " [a] Theory"
answer_b = " [b] Fact"
question = "Evaluate:\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 56
part2()
answer_a = " [a] Compassionate"
answer_b = " [b] Logical"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 57
part2()
answer_a = " [a] Analytical"
answer_b = " [b] Sentimental"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 58
part2()
answer_a = " [a] Sensible"
answer_b = " [b] Facinating"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 59
part3()
answer_a = " [a] Take time to list the separate things to be done and the order of doing them"
answer_b = " [b] Plunge right in?"
question = "When you start a big project that is due in a week, do you\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 60
part3()
answer_a = " [a] Difficult to start and maintain a conversation with some people"
answer_b = " [b] Easy to talk to most people for long periods of time?"
question = "In social situations do you generally find it\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 61
part3()
answer_a = " [a] Do it in the accepted way"
answer_b = " [b] Invent a way of your own?"
question = "In doing something that many other people do, does it appeal to you more to\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 62
part3()
answer_a = " [a] Right away"
answer_b = " [b] Only after they really get to know you?"
question = "Can the new people you meet tell what you are interested in\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 63
part3()
answer_a = " [a] A person of real feeling"
answer_b = " [b] A consistently reasonable person"
question = "Do you generally prefer courses that teach\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 64
part3()
answer_a = " [a] A person of real feeling"
answer_b = " [b] A consistently reasonable person?"
question = "Is it a higher compliment to be called\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 65
part3()
answer_a = " [a] Necessary at times but generally unfavorable"
answer_b = " [b] Helpful and favorable most of the time?"
question = "Do you find going by a schedule\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 66
part3()
answer_a = " [a] Talk individually with people you know well"
answer_b = " [b] Join in the talk of the group?"
question = "When you are with a group of people, would you usually rather \n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 67
part3()
answer_a = " [a] Do much of the talking"
answer_b = " [b] Let others do most of the talking?"
question = "At parties do you\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 68
part3()
answer_a = " [a] Appeal to you"
answer_b = " [b] Leave you cold?"
question = "Does the idea of making a list of what you should get done over a weekend\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 69
part3()
answer_a = " [a] Competent"
answer_b = " [b] Compassionate?"
question = "Which is a higher compliment, to be called\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 70
part3()
answer_a = " [a] Make your social engagements some distance ahead"
answer_b = " [b] Be free to do things on the spur of the moment"
question = "Do you generally prefer to\n"
mb = "jp"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 71
part3()
answer_a = " [a] Figure out what needs to be done as you go along"
answer_b = " [b] Begin by breaking it down into steps?"
question = "Overall, when working on a big assignment, do you tend to\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 72
part3()
answer_a = " [a] Only with people who share some interest of yours"
answer_b = " [b] With almost anyone?"
question = "Can you keep a conversation going indefinitely\n"
mb = "ie"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 73
part3()
answer_a = " [a] Support the established methods of doing good"
answer_b = " [b] Analyze what is still wrong and attack unsolved problems?"
question = "Would you rather\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 74
part3()
answer_a = " [a] Enjoy odd or original ways of saying things"
answer_b = " [b] Like writers to say exactly what they mean?"
question = "In reading for pleasure, do you\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 75
part3()
answer_a = " [a] Good-natured but often inconsistent"
answer_b = " [b] Sharp-tongued but always logical?"
question = "Would you rather work under a boss (or teacher) who is\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 76
part3()
answer_a = " [a] However you feel that particular day"
answer_b = " [b] A set schedule?"
question = "Would you prefer to do most things according to\n"
mb = "pj"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 77
part3()
answer_a = " [a] Talk easily to almost anyone for as long as you have to"
answer_b = " [b] Find a lot to say only to certain people or under certain conditions?"
question = "Can you\n"
mb = "ei"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 78
part3()
answer_a = " [a] Weigh the facts"
answer_b = " [b] Consider people's feelings and opinions?"
question = "When making a decision, is it more important to you to \n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 79
part4()
answer_a = " [a] Imaginative"
answer_b = " [b] Realistic"
question = "Evaluate:\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 80
part4()
answer_a = " [a] Bighearted"
answer_b = " [b] Firm-minded"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 81
part4()
answer_a = " [a] Fair-minded"
answer_b = " [b] Caring"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 82
part4()
answer_a = " [a] Production"
answer_b = " [b] Design"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 83
part4()
answer_a = " [a] Possibilities"
answer_b = " [b] Certainties"
question = "Evaluate:\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 84
part4()
answer_a = " [a] Tenderness"
answer_b = " [b] Strength"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 85
part4()
answer_a = " [a] Practical"
answer_b = " [b] Sentimental"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 86
part4()
answer_a = " [a] Make"
answer_b = " [b] Create"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 87
part4()
answer_a = " [a] Novel"
answer_b = " [b] Already Known"
question = "Evaluate:\n"
mb = "ns"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 88
part4()
answer_a = " [a] Sympathize"
answer_b = " [b] Analyze"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 89
part4()
answer_a = " [a] Strong-willed"
answer_b = " [b] Tenderhearted"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 90
part4()
answer_a = " [a] Concrete"
answer_b = " [b] Abstract"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 91
part4()
answer_a = " [a] Devoted"
answer_b = " [b] Determined"
question = "Evaluate:\n"
mb = "ft"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 92
part4()
answer_a = " [a] Competent"
answer_b = " [b] Kindhearted"
question = "Evaluate:\n"
mb = "tf"
execute(que_no, question, answer_a, answer_b, mb)

que_no = 93
part4()
answer_a = " [a] Practical"
answer_b = " [b] Innovative"
question = "Evaluate:\n"
mb = "sn"
execute(que_no, question, answer_a, answer_b, mb)

def raw_points():
	global e, s, t, j, i, n, f, p
	global preference
	print(f"\n###### My Raw Points ###### \
		\nExtraversion: {e} \
                \nIntroversion: {i} \
                \n----------------- \
		\nSensing: {s} \
                \nIntuition {n} \
                \n----------------- \
		\nThinking: {t} \
                \nFeeling: {f} \
                \n----------------- \
		\nJudging: {j} \
		\nPerceiving: {p} \
		\n#######################")

print("\n########## In the event of a category TIE, use the following to break it: ##########")
print("\nTie Breakers: \
	\nif E or I has the same value, I wins \
	\nif S or N has the same value, N wins \
	\nif T or F has the same value, F wins \
	\nif J or P has the same value, P wins")

print("\n########## Clarity gives you insight on how far right or left you are within each category ##########")
print ("\nClarity of Categories: \
	\nE or I, 11 - 13: Slight | 14 - 16: Moderate | 17 - 19: Clear | 20 - 21: Very Clear \
	\nS or N, 13 - 15: Slight | 16 - 20: Moderate | 21 - 24: Clear | 25 - 26: Very Clear \
	\nT or F, 12 - 14: Slight | 15 - 18: Moderate | 19 - 22: Clear | 23 - 24: Very Clear \
	\nJ or P, 11 - 13: Slight | 14 - 16: Moderate | 17 - 20: Clear | 21 - 22: Very Clear ")
print("\n##################################### My info below ##########################################")

preference = []

# Evaluate E and I
if e > i:
	preference.append("E")
if e < i:
	preference.append("I")
if e == i:
	preference.append("I")

# Evalute S and N
if s > n:
	preference.append("S")
if s < n:
	preference.append("N")
if s == n:
	preference.append("N")

# Evalute T and F
if t > f:
	preference.append("T")
if t < f:
	preference.append("F")
if t == f:
	preference.append("F")

# Evalute J and P
if j > p:
	preference.append("J")
if j < p:
	preference.append("P")
if j == p:
	preference.append("P")

raw_points()

print(f"\nMy preference is: {preference}")
