import requests

headers = {'Content-Type': 'application/json'}
apiKey = 'apiKey=776299ee963f4bb9a025b9cd2ad3e910'

raw = input('What ingredients do you have?')
components = raw.split()
items = ',+'.join(components)
ingredient = 'ingredients=' + items

dietChoice = input("Do you have any dietary requirements?")

includeIngredients = "includeIngredients={}".format(raw)
addRecipeNutrition = "addRecipeNutrition=true"
dietRequirement = ""

if dietChoice == 'yes':
  dietRequirement = input("What is your dietary requirement?")
  diet = "diet={}".format(dietRequirement)
  dietUrl = 'https://api.spoonacular.com/recipes/complexSearch?{}&{}&{}&{}'.format(diet, includeIngredients, addRecipeNutrition, apiKey)
else:
   dietUrl = 'https://api.spoonacular.com/recipes/complexSearch?{}&{}&{}'.format(includeIngredients,addRecipeNutrition, apiKey)

response = requests.get(dietUrl)
dietaryRecipesRaw = response.json()
dietaryRecipes = dietaryRecipesRaw['results']
print('Here are your {} recipe options including {}: '.format(dietRequirement, items))
for d in range(0, len(dietaryRecipes)):
   print(dietaryRecipes[d]['title'])
   dietaryNutrition = (dietaryRecipes[d]['nutrition'])
   nutrients = (dietaryNutrition['nutrients'])
   print(nutrients[0]['amount'])
   print(nutrients[0]['unit'] + " per serving")

def DisplayRecipeInformation():
   global recipeChoice
   selectRecipe = input("Which recipe would you like to make?")
   for r in range(0, 10):
       if selectRecipe == (dietaryRecipes[r]['title']):
           recipeChoice = (dietaryRecipes[r])
           image = (recipeChoice['image'])
           recipeTime = (recipeChoice['readyInMinutes'])
           servings = (recipeChoice['servings'])
           nutrition = (recipeChoice['nutrition'])
           ingredients = (nutrition['ingredients'])

   print('For this recipe, you will need:')
   for i in range(0, len(ingredients)):
       print(ingredients[i]['amount'])
       print(ingredients[i]['unit'])
       print(ingredients[i]['name'])

   print(image)
   print('This recipe will take around ' + str(recipeTime) + ' minutes to make and serves ' + str(servings))

   confirmChoice = input('Would you like to continue to the recipe steps for {}? '.format(selectRecipe))
   if confirmChoice == "yes":
       stepDetails = (recipeChoice['analyzedInstructions'][0]['steps'])
       for s in range(0, len(stepDetails)):
           print(stepDetails[s]['number'])
           print(stepDetails[s]['step'])
   else:
       DisplayRecipeInformation()


DisplayRecipeInformation()

