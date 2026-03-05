import random
QA_Bank = [{
         'id': 1,
         'scenario': 'The refrigerator temperature reads 8°C. Should you:',
         'options': {
               'A': 'Continue using it - close enough',
               'B': 'Report it to management immediately',
               'C': 'Try to adjust temperature yourself',
               'D': 'Move all food to another fridge'
         },
         'correct_answer': 'B',
         'explanation': 'Temperature control issues must be reported immediately.',
         'is_challenge': False
      },
{
    "id": 2,
   "scenario": "You have have the following batches to cook: 1 bag of OR chicken, 2 bags of tenders, and 1 bag of zinger fillets.\n Which batch should you cook first?",
   "options": {
         "A": "Cook the OR chicken first",
         "B": "Cook the tenders first",
         "C": "Cook the zinger fillets first",
         "D": "Cook whichever batch you feel like first"
   },
   "correct_answer": "A",
   "explanation": "The OR chicken has takes the longest time to cook so it should be cooked first, unless your manger specifies otherwise.",
   "is_challenge": True
},
{
   'id': 3,
   'scenario': 'What colour chux do you need to use to clean the fryers after dropping a batch of chicken?',
   'options': {
      'A': "Green",
      'B': "Blue",
      'C': 'Red',
      'D': "Purple"
   },
   'correct_answer': 'C',
   'explanation': "You must always use the Red chux after to clean the fryers to prevent decomtamination.",
   'is_challenge': False
},
{
   'id': 4,
   'scenario':  "It is a busy night and we need to make sure the chicken texture is as good as possible. What strategy do we use to maintain the flour to prevent clumps? ",
   'options': {
      'A': "Sift and top the lugs up as you alternate between them, when they need to.",
      'B': "Save sifting for the end" ,
      'C': "Only do it when you need to",
      'D': "Do it after every bag", 
   },
   'correct_answer': "A",
   'explanation': "Sifting and topping up the flour as you go, ensures that the flour is top quality while allowing you to bread all the chicken quickly.",
   'is_challenge': True
},


]


