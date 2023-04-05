### Hi there 👋

## Group 4 Project 4
 * Stephanie Tran
 * Cristian Jung
 * Ana Gonzalez
 * Rob James
 * Kelly Stave 
 
# project-4-health-analysis

## Project 4 group members
Ana Gonzalez, Robert James, Cristian M. Jung, Kelly Stave, and Stephanie Tran

## INTRODUCTION

For Project 4, our group will be exploring diabetes in adults 18 and older within the US.
* Machine Learning Modeling:
	* Initial Testing for all models:
		* We first decided to break up the dataset into 4 major categories:
			* Consumption: Veggies, Heavy Alcohol Consumption, Smoker, Fruits
			* Demographic: Age, Income, Education, Sex
			* General health: BMI, Physical Activity
			* Pre-existing conditions: HighBP, Heart Disease History or Attack, HighChol, Stroke
	* KMEANS:
		* StandardScaler, PCA, LogisticRegression Model, Desicion Tree Model, Deep Learning ML Model
		* RESULTS of each major categories:
			
			* Consumption:
				* StandardScaler, PCA, Desicion Tree Model
					* Accuracy Score 56.9%
				* StandardScaler, PCA, Deep Learning ML Model
					* Accuracy Score 56.3%
			
			* Demographic:
				* LogisticRegression Model
					* Accuracy Score 64.2%
			
			* General health:
				* StandardScaler, LogisticRegression Model
					* Accuracy Score 64.5%
			
			* Pre-existing conditions:
				* LogisticRegression Model
					* Accuracy Score 69.3%
	
	
	* XGBOOST:
		* XGBOOST XGBClassifier Modeling	
		* RESULTS of each major categories:
			
			
			* Consumption:
				* Accuracy Score 58.3%
				* Veggies F-Score: 101
				* HvyAlcoholConsumption F-Score: 83
				* Smoker F-Score: 81
				* Fruits F-Score: 66
			
			* Demographic:
				* Accuracy Score 70.8%
				* Age F-Score: 361
				* Income F-Score: 259
				* Education F-Score: 173
				* Sex F-Score: 110
			
			* General health:
				* Accuracy Score 69.8%
				* BMI F-Score: 717
				* PhysActivity: F-Score 47
			
			* Pre-existing conditions:
				* Accuracy Score 74.8%
				* HighBP F-Score: 53
				* HeartDiseaseorAttack F-Score: 45
				* HighChol F-Score: 41
				* Stroke F-Score: 30
			
			* We combined the top feature from each of the four categories:
				* Accuracy Score 78.1%
				* BMI F-Score: 415
				* Age F-Score: 372
				* HighBP F-Score: 110
				* Veggies F-Score: 57
		
		* FINAL RESULT (with all features minus subjective columns):
			* Accuracy Score 81.1%
			* Feature Importance:

## RESULTS
* XGBOOST Modeling, with all features minus subjective columns, gave an Accuracy score of entire Binary Dataset: 81.1%

* Webpage:
	* We created a webpage with Dashboard including Diabetes Risk Predictor.
		* Pages:
			* Home: Introduction with Categorized Features Result and Overall.
			* Data: 
			* Predict: Model Function
			* GitHub: Link to our builds and images
	* Visitor takes a quick survey, then we output if one is at risk or not.
