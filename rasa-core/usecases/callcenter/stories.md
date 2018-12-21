
## Change from Virtual Assistant to a real Doctor
* handover
    - utter_handover

## greetings
* greet
    - utter_greet_action

## Evaluate user identification number 
* evaluate_identification_number
    - ask_name
    - slot{"requested_slot" : "identification_number"}

## Evaluate user name
* evaluate_name
    - ask_date_of_birth
    - slot{"requested_slot" : "user_name"}

## Evaluate user date of birth
* evaluate_date_of_birth
    - ask_site
    - slot{"requested_slot" : "date"}

## Evaluate pain site
* evaluate_site
    - ask_character

## Evaluate pain character
* evaluate_character
    - ask_location
>follow0

## Deny that it is a localized pain
>follow0
* deny
    - ask_radiation
>follow1

## Confirm that it is a localized pain
>follow0
* confirm
    - ask_associated_symptoms
> follow2

## Evaluate where the pain radiates
>follow1
* evaluate_radiation
    - ask_associated_symptoms
> follow2

## Evaluate the associated symptoms
> follow2
* evaluate_associated_symptoms
    - ask_night_pain
>follow3 

# Deny that there are associated symptoms
> follow2
* evaluate_associated_symptoms_no 
    - ask_night_pain
>follow3

## Confirm that the pain interrups the sleep
>follow3   
* confirm
    - ask_exacerbating_relieving_factor
>follow4

## Deny that the pain interrups the sleep
>follow3    
* deny
    - ask_exacerbating_relieving_factor
>follow4

## Evaluate the exacerbating or relieving factors
>follow4
* evaluate_exacerbating_relieving_factor
    - ask_severity

## Deny the existence of the exacerbating or relieving factors
>follow4
* evaluate_exacerbating_relieving_factor_no
    - ask_severity

## Evaluate the severity of the pain
* evaluate_severity
    - ask_allergy
    - slot{"user_name" : "user_name"}
>follow5

## Evaluate the allergies
>follow5
* evaluate_allergy
    - ask_medication

## Deny the existence of allergies   
>follow5
* evaluate_allergy_no
    - ask_medication
>follow6

## Evaluate the medication the user takes
>follow6
* evaluate_medication
    - ask_cardio
>follow7

## Deny that the user takes any the medication
>follow6
* evaluate_medication_no
    - ask_cardio
>follow7

## Evaluate cardio illness
>follow7
* evaluate_cardio
    - ask_neoplasm
>follow8 

## Deny the existence of any cardio illness  
>follow7
* evaluate_cardio_no
    - ask_neoplasm
>follow8 

## Evaluate neoplasm illness
>follow8
* evaluate_neoplasm
    - ask_illness
> follow9

## Deny the existence of any neoplasm illness  
>follow8
* evaluate_neoplasm_no
    - ask_illness
>follow9

## Evaluate the illness  
>follow9
* evaluate_illness
    - ask_toxic_habits
>follow10

## Deny the existence of any kind diseases
>follow9
* evaluate_illness_no
    - ask_toxic_habits
>follow10

## Evaluate toxic habits
>follow10    
* evaluate_toxic_habits
    - goodbye

## Deny toxic habits
>follow10
* evaluate_toxic_habits_no
    - goodbye


