from gsearchadvance import googlesearch


question = 'Scientists recently established that a river in South America surprisingly does what?'
option1 = "Flows uphill"
option2 = "Glows"
option3 = "Simmers"
#option4 = "Phascolarctos cinereus"
options=[option1,option2,option3]
response = googlesearch(question,options).results()
print(response)
