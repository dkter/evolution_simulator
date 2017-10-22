import random
import add_if_or_elif




curDna=''
def randomCreature():
    testDNA=''
    for i in range(0,11):
        testDNA += str(random.randint(0,9))
    for i in range (0,5):
      curDna+=add_if(curDna,len(curDna-1))
 
print(curDna)




# """  ##########################
#     #/\/\/\/\/\/\/\/\/\/\/\/\/\#
#    #/##########################\#
#   #/##/         /#\          \##\#
#  #/ ##  /##################\  ## \#
# #<  ##### I AM PYTHON MAN. #####  >#
#  #\ ##  \##################/  ## /#
#   #\##\         \#/          /##/#
#    #\##########################/#
#     #\/\/\/\/\/\/\/\/\/\/\/\/\/#
#      ##########################  """
#  