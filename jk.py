import openai
import speech
import keyboard as key
import logging
from googletrans import Translator

translator = Translator()
openai.api_key = "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"
totalTrys = 3
logger = None

def main(NumberOfTrys = 0):
  logger = configurate_logger()
  #Recognize Input
  #speech.speak("Prompt")
  print("Prompt")
  prompt = speech.recognize()

  #Validate Input
  #speech.speak(f"Hast du \"{str(prompt)}\" gesagt? y/n")
  print(f"Hast du \"{str(prompt)}\" gesagt? y/n")
  if(NumberOfTrys > 0): print(f"Noch {totalTrys-NumberOfTrys} Versuche!")#speech.speak(f"Noch {totalTrys-NumberOfTrys} Versuche!")
  validate(NumberOfTrys)

  #Translate
  prompt = translator.translate(str(prompt), src='de', dest='en').text
  prompt += "\n AI:" # Making a new Line and Adding 'AI: ' to it to make it easier for the ai to understand where the request Ends

  #Request
  result = translator.translate(str(tiffany_gideon(prompt)), src='en', dest='de').text 
  #speech.speak(result)
  print(result)

def configurate_logger():
  logging.basicConfig(filename='myapp.log', level=logging.WARNING, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
  return logging.getLogger(__name__)

def tiffany_gideon(prompt):
  try:
    response = openai.Completion.create(
      engine="davinci",
      prompt=f"{prompt}: \n",
      temperature=0.4,
      max_tokens=100,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0,
      stop=["\n"]
    )
    return response.choices[0].text
  except Exception as e:
    logger.error(e)
    return ""

def validate(NumberOfTrys = 0):
  while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
      if key.is_pressed('y'):  # if key 'q' is pressed 
        break  # finishing the loop
      elif key.is_pressed('n'):
        if NumberOfTrys < (totalTrys-1):
          main(NumberOfTrys+1)
        else:
          break
    except Exception as e:
      logger.error(e)
      break 

if __name__ == "__main__":
    main()
  