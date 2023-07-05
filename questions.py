questions = {
    "offer_type": {
        "question": "Quelle est l'offre (vente, location, Location saisonnière, Vente de programme neuf en état futur d'achèvement (VEFA)) ?",
        "responses": ["vente", "location", "location saisonnière", "vente de programme neuf en état futur d'achèvement","vefa", "VEFA"],
        "next": "property_type"
    },
    "property_type": {
        "question": "Quel est le type de bien (appartement, maison, terrain, local commercial, parking, bastide , château , masison de village ,villa , hôtel particulier , ferme , mas , rez de villa , chalet , studio , triplex , terrain  constructible , box de stockage , cabanon , cave , garage , viager , bureaux , immeuble commercial , entrepôt) ?",
        "responses": ["appartement", "maison", "terrain" , "parking", "local commercial", "fond de commerce", "bastide", "château", "maison de village", "villa", "hôtel particulier", "ferme", "mas", "propriété", "rez de villa", "chalet", "duplex", "immeuble résidentiel", "loft", "rez de jardin", "studio", "triplex", "terrain constructible", "box de stockage", "cabanon", "cave", "garage", "viager", "bureaux", "immeuble commercial", "entrepôt"],
        "next": "terrain_status"  # 'terrain_status' or 'city' based on user response, this is updated in the chat function
    },
    
        #---------------------------------------------------property_type : Maisson ou appartement-------------------------------------------

    "city": {
        "question": "Quelle est la ville où se situe le bien ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "quartier"
    },
    "quartier": {
        "question": "Quel est le quartier du bien ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "living_area"
    },
    "living_area": {
        "question": "Quelle est la surface habitable du bien (en m²) ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_area in m²"
    },
    "terrain_area in m²": {
        "question": "Quelle est la surface du terrain (en m²) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "construction_year"
    },
    "construction_year": {
        "question": "Quelle est l'année de construction du bien ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "prestige_status"
    },
    "prestige_status": {
        "question": "Est-ce que c’est un bien de prestige ? (oui/non) : ",
        "responses": ["oui", "non"],  # Update this based on the choices
        "next": "property_status"
    },
    "property_status": {
        "question": "Le bien est-il situé dans lotissement ou copropriété ?",
        "responses": ["lotissement", "copropriété"],
        "next": "property_style"
    },
    
    "number_of_lots_AppartementMaison": {
        "question": "Nombre de lots et procédure en cours : ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "property_style"
    },
      
    "property_style": {
        "question": "Quel est le style du bien (contemporain, traditionnel, ossature bois, etc.) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "nombre_de_niveaux"
    },
    "nombre_de_niveaux": {
        "question": "Combien de niveaux compte le bien (1, 2, 3, 4) ?",
        "responses": ["1", "2", "3", "4"],
        "next": "nombre_de_etages"
    },
    "nombre_de_etages": {
        "question": "Combien d'étages compte le bien ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Nombre_de_pieces"
    },
    "Nombre_de_pieces": {
        "question": "Combien de pièces compte le bien ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "nombre_de_chambre"
    },
    #------------------------------------------------ here
    "nombre_de_chambre": {
        "question": "combien de chambre compte le bien ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Nombre_SDB"
    },

    "Nombre_SDB": {
        "question": " Nombre SDB ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Mitoyennete_du_bien"
    },
    
    "Mitoyennete_du_bien": {
        "question": "Quelle est la mitoyenneté du bien (individuelle, 1 coté, 2 cotés, 3 cotés) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "etat_interieur_du_bien"
    },
    
    "etat_interieur_du_bien": {
        "question": "Quel est l'état intérieur du bien (à rénover, petits travaux, etc.) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "luminosit_interieure_du_bien"
    },
    
    "luminosit_interieure_du_bien": {
        "question": "Comment décririez-vous la luminosité intérieure du bien (sombre, peu claire, standard, clair, très lumineux) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "tanding_intérieur_du_bien"
    },
    "tanding_intérieur_du_bien": {
        "question": "Quel est le standing intérieur du bien (inférieur, bon état, haut de gamme, etc.) ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "agrements_du_bien"
    },
    "agrements_du_bien": {
        "question": "Quels sont les agréments du bien (type de cuisine, sous-sol, buanderie, chambre parentale, bureau ou dressing, etc.) ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "façade_du_bien"
    },
    "façade_du_bien": {
        "question": "Quel est l'état de la façade du bien (neuf, bon état, à rafraîchir, à rénover, à restaurer) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "vue_le_bien"
    },
    "vue_le_bien": {
        "question": "Comment est la vue depuis le bien (vis-à-vis, dégagée, exceptionnelle) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "orientation_du_bien"
    },
    "orientation_du_bien": {
        "question": "Quelle est l'orientation du bien (nord, sud, est, ouest) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "caracteristiques_exterieures_du_bien"
    },
    "caracteristiques_exterieures_du_bien": {
        "question": "Quelles sont les caractéristiques extérieures du bien (garage, piscine, parking, annexes, jardin, etc.) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "DPE"
    },
    "DPE": {
        "question": "Quelle est la classe énergétique du bien selon le DPE (de A à G) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "GES"
    },
    "GES": {
        "question": "Quelle est la classe d'émission de gaz à effet de serre du bien selon le GES (de A à G) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "proximite_du_bien"
    },
   
    "proximite_du_bien": {
        "question": "Quelles sont les commodités à proximité du bien (transports, écoles, restaurants, centre-ville, crèche, etc.) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "points_fort_du_bien"
    },
    "points_fort_du_bien": {
        "question": "Quels sont les points forts du bien ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "point_ameliorer"
    },
    
    # And so on until the last question for maison ou appartement
    "point_ameliorer": {
        "question": "Quels sont les points à améliorer concernant le bien ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": None  # This is the last question for maison ou appartement
    },

    #---------------------------------------------------terrain-------------------------------------------

    "terrain_status": {
        "question": "Quel est le statut du terrain (lotissement ou copropriété) ? ",
        "responses": ["lotissement", "copropriété"],
        "next": "terrain_type"  # Update based on user response
    },
    "number_of_lots": {
        "question": "Combien de lots y a-t-il et y a-t-il une procédure en cours ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_type"
    },
    "terrain_type": {
        "question": "Quel est le type de terrain (agricole, constructible, industriel, potentiel à bâtir, piscinable, arboré, arbres fruitiers, viabilisé, clôturé, divisible, raccordé (eau, téléphone, électricité, gaz), copropriété, accessible, fosse sceptique, raccordé au tout à l'égoût) ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_occupation"
    },
    "terrain_occupation": {
        "question": "Comment est occupé le terrain actuellement (loué, en fermage, vide, etc.) ?",
        "responses": ["louée", "fermage", "vide"],  # Update this based on the choices
        "next": "terrain_area"
    },
    
    "terrain_area": {
        "question": "Quelle est la surface du terrain (en m²) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_view"
    },
    "terrain_view": {
        "question": "Quelle est la vue depuis le terrain ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_constraints"
    },
    "terrain_constraints": {
        "question": "Quelles sont les contraintes du terrain (pollution, eau, arbres, etc.) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_environment"
    },
    
    "terrain_environment": {
        "question": "Comment décririez-vous l'environnement du terrain ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_riqsues"
    },
    
    "terrain_riqsues": {
        "question": "Quels sont les risques associés au terrain ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_Proximites"
    },
    
    "terrain_Proximites": {
        "question": "Quelles sont les commodités à proximité du terrain (transports, écoles, restaurants, centre-ville, crèche, etc.) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_forts"
    },
    
    "terrain_forts": {
        "question": "Quels sont les points forts du terrain ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_ameliorer"
    },
    "terrain_ameliorer": {
        "question": "Quels sont les points à améliorer concernant le terrain ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": None  # This is the last question for terrain
    },
    

       
        #---------------------------------------------------property type Autre-------------------------------------------

    
    # for property type Autre
     "Autre_Ville": {
        "question": "Quelle est la ville ? ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Quartier"
    },
    "Autre_Quartier": {
        "question": "Quel est le quartier ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Autre_Surface"
    },
    "Autre_Surface": {
        "question": "Quelle est la surface ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Autre_Anne"
    },
    
    
    
    "Autre_Anne": {
        "question": "Quelle est l'année de construction ? ",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Nombre_niveaux"
    },
    "Autre_Nombre_niveaux": {
        "question": "Combien de niveaux y a-t-il(1,2,3,4) ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Nombre_etage"
    },
    "Autre_Nombre_etage": {
        "question": "Combien d'étages y a-t-il ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Mitoyennete"
    },
    "Autre_Mitoyennete": {
        "question": "Quelle est la mitoyenneté (individuelle, 1 côté, 2 côtés, 3 côtés, etc.) ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_etat_bien"
    },
    "Autre_etat_bien": {
        "question": "Quel est l'état du bien (à rénover, petits travaux, etc.) ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Luminosite_interieure"
    },
    
    
    "Autre_Luminosite_interieure": {
        "question": "Quelle est la luminosité intérieure ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Standing_interieur"
    },
    "Autre_Standing_interieur": {
        "question": "Quel est le standing intérieur (inférieur, bon état, haute gamme, etc.) ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_caracteristiques"
    },
    "Autre_caracteristiques": {
        "question": "Quelles sont les caractéristiques du bien (disponibilité, télésurveillance, PMR, type de chauffage, climatisation, etc.) ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_Proximites"
    },
    "Autre_Proximites": {
        "question": "Quelles sont les proximités ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_DPE"
    },
    "Autre_DPE": {
        "question": "Quel est le DPE (A à G) ?",
        "responses": [], # This is left empty as this is a free text response 
        "next": "Autre_GES"
    },
       
    "Autre_GES": {
        "question": "Quel est le GES (A à G) ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "Autre_forts"
    },

    "Autre_forts": {
        "question": "Quels sont les points forts ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "terrain_ameliorer"
    },
    "terrain_ameliorer": {
        "question": "Quels sont les points à améliorer ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": None  # This is the last question for terrain
    },

    "sale_price": {
        "question": "Quel est le prix de vente ? ",
        "responses": [],  # This is left empty as this is a free text response
        "next": "charge"
    },
    "rent_price": {
        "question": "Quel est le prix de loyer ?",
        "responses": [],  # This is left empty as this is a free text response
        "next": "charge"
    },
    "charge": {
        "question": "Les honoraires sont à la charge du (vendeur ou acheteur) ?",
        "responses": ["vendeur", "acheteur"],  # This question has specific responses
        "next": "Tonalite_de_l_annonce"
    }, 

    "Tonalite_de_l_annonce": {
    "question": "Quelle est la tonalité de l'annonce (Story-telling, Enthousiaste, vendeur, formel, posé, lyrique, comique, oratoire, solennel) ?",
    "responses": [],  # This is left empty as this is a free text response
    "next": "Longueur_de_lannonce"
},

"Longueur_de_lannonce": {
    "question": "Quelle est la longueur de l'annonce (Normal, Courte et concise, Détailée, Très détaillée) ?",
    "responses": [],  # This is left empty as this is a free text response
    "next": None  # This is the last question for maison ou appartement
}

}

