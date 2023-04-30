from gsearch2 import googlesearch


question = 'Which of these are NOT married to Monica Bellucci?'
option1 = "Vincent Cassel"
option2 = "Claudio Carlos Basso"
option3 = "Nicolas Lefebvre"
#option4 = "Phascolarctos cinereus"
options=[option1,option2,option3]#,option4]
response = googlesearch(question,options).results()
print(response)
