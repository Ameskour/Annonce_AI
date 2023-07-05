from flask import Flask, render_template, request, jsonify
from fuzzywuzzy import process

import openai

# Set up your OpenAI API credentials
openai.api_key = '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'
app = Flask(__name__)

questions = {
    "offer_type": {
        "question": "Quelle est l'offre (vente, location, Location saisonnière, Vente de programme neuf en état futur d'achèvement (VEFA)) ?",
        "responses": ["vente", "location", "location saisonnière", "vente de programme neuf en état futur d'achèvement (vefa)"],
        "next": "property_type"
    },
    "property_type": {
        "question": "Quel est le type de bien (appartement, maison, terrain , parking) ?",
        "responses": ["appartement", "maison", "terrain" , "parking"],
        "next": "terrain_status"  # 'terrain_status' or 'city' based on user response, this is updated in the chat function
    },
    
        #---------------------------------------------------property_type : Maisson ou appartement-------------------------------------------

    "city": {
        "question": "Ville : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "neighborhood"
    },
    "neighborhood": {
        "question": "Quartier : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "living_area"
    },
    "living_area": {
        "question": "Surface habitable : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_area1"
    },
    "terrain_area1": {
        "question": "Surface terrain : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "construction_year"
    },
    "construction_year": {
        "question": "Année de construction : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "prestige_status"
    },
    "prestige_status": {
        "question": "Est-ce que c’est un bien de prestige ? (oui/non) : ",
        "responses": ["oui", "non"],  # Update this based on the choices
        "next": "property_status"
    },
    "property_status": {
        "question": "Statut du bien (lotissement ou copropriété) : ",
        "responses": ["lotissement", "copropriété"],
        "next": "number_of_lots_AppartementMaison"
    },
    
    
    "number_of_lots_AppartementMaison": {
        "question": "Nombre de lots et procédure en cours : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "property_style"
    },
    
    
    "property_style": {
        "question": "Style de bien (contemporain, traditionnel, ossature bois...) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "number_of_levels"
    },
    "number_of_levels": {
        "question": "Nombre de niveaux (1, 2, 3, 4) : ",
        "responses": ["1", "2", "3", "4"],
        "next": "number_of_floors"
    },
    "number_of_floors": {
        "question": "Nombre d'étages : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "number_of_rooms"
    },
    "number_of_rooms": {
        "question": "Nombre de pièces : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "number_of_bathrooms"
    },
    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    "number_of_bathrooms": {
        "question": "Nombre SDB: ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Nombre_SDB"
    },
    
    "Nombre_SDB": {
        "question": "Mitoyenneté (individuelle, 1 coté, 2 cotés, 3 cotés) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Mitoyennete"
    },
    
    "Mitoyennete": {
        "question": "Intérieur, Etat du bien (à rénover, petits travaux...) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Etat_du_bien"
    },
    
    "Etat_du_bien": {
        "question": "Intérieur, Luminosité (sombre, peu claire, standard, clair, très lumineux) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Luminosite"
    },
    "Luminosite": {
        "question": "Intérieur, Standing (inférieur, bon état, haute gamme...) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Standing"
    },
    "Standing": {
        "question": "Quels sont les agréments qui contient ce bien (type de cuisine, sous-sol, buanderie, chambre parentale, bureau ou dressing...)? : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "agrements"
    },
    "agrements": {
        "question": "Extérieur, Etat de la façade (Neuf, Bon état, À rafraîchir, À rénover, À restaurer) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "façade"
    },
    "façade": {
        "question": "Extérieur, Vue (vis-à-vis, dégagée, exceptionnelle) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Vue_AM"
    },
    "Vue_AM": {
        "question": "Extérieur, Orientation (Nord, sud, est, ouest) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Orientation"
    },
    "Orientation": {
        "question": "Quelles sont les caractéristiques extérieures (garage, piscine, parking, annexes ou jardin...)? : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "caracteristiques"
    },
    "caracteristiques": {
        "question": "DPE (A à G) :",
        "responses": [],  # This is left empty as this is a free text response
        "next": "DPE"
    },
    "DPE": {
        "question": "GES (A à G) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "GES"
    },
    "GES": {
        "question": "Nombre de pièces : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "number_of_bathrooms"
    },
    "GES": {
        "question": "Proximités (transports, école, brasseries et restaurants, centre-ville) :  ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Proximites"
    },
    "Proximites": {
        "question": "Points forts : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "forts"
    },
    
    # And so on until the last question for maison ou appartement
    "forts": {
        "question": "Points à améliorer : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": None  # This is the last question for maison ou appartement
    },
    
    #---------------------------------------------------terrain-------------------------------------------

    "terrain_status": {
        "question": "Statut du terrain (lotissement ou copropriété) : ",
        "responses": ["lotissement", "copropriété"],
        "next": "number_of_lots"  # Update based on user response
    },
    "number_of_lots": {
        "question": "Nombre de lots et procédure en cours : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_type"
    },
    "terrain_type": {
        "question": "Type de terrain (agricole, constructible, industriel, potentiel à bâtir, piscinable, arboré, arbres fruitiers, viabilisé, clôturé, divisible, raccordé (eau, téléphone, électricité, gaz), copropriété, accessible, fosse sceptique, raccordé au tout à l égoût) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_occupation"
    },
    "terrain_occupation": {
        "question": "Occupation du terrain (louée, fermage, vide...) : ",
        "responses": ["louée", "fermage", "vide"],  # Update this based on the choices
        "next": "terrain_area"
    },
    
    "terrain_area": {
        "question": "Surface (m2) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_view"
    },
    "terrain_view": {
        "question": "Vue : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_constraints"
    },
    "terrain_constraints": {
        "question": "Contraintes (pollution, eau, arbres...) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_environment"
    },
    
    "terrain_environment": {
        "question": "environnement : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_riqsues"
    },
    
    "terrain_riqsues": {
        "question": "risques : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_Proximites"
    },
    
    "terrain_Proximites": {
        "question": "Proximités : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_forts"
    },
    
    "terrain_forts": {
        "question": "Points forts : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_ameliorer"
    },
    "terrain_ameliorer": {
        "question": "Points à améliorer : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": None  # This is the last question for terrain
    },
    

       
        #---------------------------------------------------property type Autre-------------------------------------------

    
    # for property type Autre
     "Autre_Ville": {
        "question": "ville : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Quartier"
    },
    "Autre_Quartier": {
        "question": "Quartier : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Autre_Surface"
    },
    "Autre_Surface": {
        "question": "Surface : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Autre_Anne"
    },
    
    
    
    "Autre_Anne": {
        "question": "Année de construction : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Nombre_niveaux"
    },
    "Autre_Nombre_niveaux": {
        "question": "Nombre de niveaux : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Nombre_etage"
    },
    "Autre_Nombre_etage": {
        "question": "Nombres d'étage : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Mitoyennete"
    },
    "Autre_Mitoyennete": {
        "question": "Mitoyenneté(individuelle,1 coté , 2 cotés ,3 cotés ... ) : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_etat_bien"
    },
    "Autre_etat_bien": {
        "question": "intérieur , Etat du bien (à rénover, petit travaux...) : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Luminosite"
    },
    
    
    "Autre_Luminosite": {
        "question": "intérieur , Luminosité : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Standing"
    },
    "Autre_Standing": {
        "question": "intérieur , Standing(inférieur, bon état, haute gamme...) :",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_caracteristiques"
    },
    "Autre_caracteristiques": {
        "question": "caractéristiques(disponiblté , télésurveillance , PMR , type chauffage, climatisation) : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Proximites"
    },
    "Autre_Proximites": {
        "question": "Proximités : ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_DPE"
    },
    "Autre_DPE": {
        "question": "DPE(A à G): ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_GES"
    },
       
    "Autre_GES": {
        "question": "GES (A à G) : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Autre_forts"
    },

    "Autre_forts": {
        "question": "Points forts : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_ameliorer"
    },
    "terrain_ameliorer": {
        "question": "Points à améliorer : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": None  # This is the last question for terrain
    },
}


# Add the new questions to the dictionary
questions["sale_price"] = {
    "question": "Prix de vente : ",
    "responses": [],  # This is left empty as this is a free text response
    "next": "charge"
}

questions["charge"] = {
    "question": "Honoraires à la charge du (vendeur ou acheteur) : ",
    "responses": ["vendeur", "acheteur"],  # This question has specific responses
    "next": None
}

questions["rent_price"] = {
    "question": "Prix de loyer : ",
    "responses": [],  # This is left empty as this is a free text response
    "next": "charge"
}


current_state = "offer_type"
previous_answers = {}

@app.route('/')
def index():
    return render_template('index.html')

def get_matching_score(user_input, choices):
    result = process.extractOne(user_input, choices)
    return result

def determine_next_state(current_state, user_input, offer_type):
    if current_state == "property_type": 
        if user_input == "maison" or user_input == "appartement":
            return "city"
        elif user_input == "terrain":
            return "terrain_status"
        elif user_input == "parking":
            return "Autre_Ville"
    elif current_state == "terrain_status":
        if user_input == "lotissement":
            return "terrain_type"            
        else:  # If user_input is "copropriété"
            return "number_of_lots"
    elif current_state == "property_status":
        if user_input == "lotissement":
            return "property_style"            
        else:  # If user_input is "copropriété"
            return "number_of_lots_AppartementMaison"    
    else:
        next_state = questions[current_state]['next']
        if next_state is None:
            if offer_type in ["vente", "vente de programme neuf en état futur d'achèvement (vefa)"] and "sale_price" not in previous_answers:
                return "sale_price"
            elif offer_type in ["location", "location saisonnière"] and "rent_price" not in previous_answers:
                return "rent_price"
            elif current_state == "charge" and "sale_price" in previous_answers and "charge" in previous_answers:
                return None  # End the conversation flow
            else:
                return next_state
        else:
            return next_state

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input', '')
    previous_answers = request.json.get('previous_answers', {})
    current_state = request.json.get('current_state', 'offer_type')

    previous_answers[current_state] = user_input  # Save user's response

    if current_state in ["offer_type", "property_type"]:
        match = get_matching_score(user_input, questions[current_state]['responses'])
        if match and match[1] < 70:  # match[1] is the score
            return jsonify({'question': "Sorry, I didn't understand that. Could you try again?", 
                            'previous_answers': previous_answers, 
                            'next_state': current_state})

    offer_type = previous_answers.get("offer_type", "").lower()
    current_state = determine_next_state(current_state, user_input, offer_type)

    if current_state is None:
        if "sale_price" not in previous_answers:
            return jsonify({'question': questions["sale_price"]['question'], 
                            'previous_answers': previous_answers, 
                            'next_state': "sale_price"})
        elif "charge" not in previous_answers:
            return jsonify({'question': questions["charge"]['question'], 
                            'previous_answers': previous_answers, 
                            'next_state': "charge"})
        elif previous_answers.get("sale_price") and previous_answers.get("charge"):
            ad_prompt = ' '.join([f'{key}: {value}' for key, value in previous_answers.items() if key not in ['sale_price', 'charge']])
            ad = create_advertisement(ad_prompt)
            return jsonify({'question': "Voici votre annonce :\n" + ad, 'previous_answers': previous_answers})

    return jsonify({'question': questions[current_state]['question'], 
                    'previous_answers': previous_answers, 
                    'next_state': current_state})


def create_advertisement(ad_prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a real estate agent creating an advertisement for a property. Generate the ad in French. Write a compelling description using only the characteristics in the prompt."},
                {"role": "user", "content": ad_prompt}
            ]
        )
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Please wait before making more requests.")
        return "Rate limit exceeded. Please wait before making more requests."

    message = response.choices[0].message['content'].strip()
    return message


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)