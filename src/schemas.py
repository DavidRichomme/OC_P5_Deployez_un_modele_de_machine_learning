from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field

EXEMPLE = {
  "genre": 0,
  "poste": 0.1986,
  "nombre_experiences_precedentes": 1.0986122886681098,
  "annee_experience_totale": 1.9459101490553132,
  "annees_dans_l_entreprise": 1.0986122886681098,
  "annees_dans_le_poste_actuel": 0,
  "distance_domicile_travail": 1,
  "niveau_education": 3,
  "frequence_deplacement": 2,
  "annees_depuis_la_derniere_promotion": 1.0986122886681098,
  "note_evaluation_precedente": 3,
  "note_evaluation_actuelle": 1.3862943611198906,
  "heure_supplementaires": 1,
  "augmentation_salaire_precedente": 16,
  "fe1_tranche_salariale": 1,
  "fe2_satisfaction_globale": 9,
  "fe3_tranche_age": 2,
  "statut_marital_divorce": 0,
  "statut_marital_marie": 1,
  "departement_consulting": 1,
  "departement_ressources_humaines": 0
}

Binaire = Annotated[int, Field(ge=0, le=1, description="1 = oui, 0 = non")]
Log1p = Annotated[
    float,
    Field(ge=0, le=4.5, description="Valeur déjà transformée : ln(1 + x). Exemple : 3 ans s'écrit 1.386"),
]


class PredictionInput(BaseModel):
    model_config = ConfigDict(json_schema_extra={"examples": [EXEMPLE]}, extra="forbid")

    genre: Binaire
    poste: float = Field(ge=0, le=0.3, description="Poste encodé en décimal (voir le README pour la correspondance)")
    nombre_experiences_precedentes: Log1p
    annee_experience_totale: Log1p
    annees_dans_l_entreprise: Log1p
    annees_dans_le_poste_actuel: int = Field(ge=0, le=40, description="Années dans le poste actuel")
    distance_domicile_travail: int = Field(ge=0, le=50, description="Distance domicile-travail en km")
    niveau_education: int = Field(ge=1, le=5, description="Niveau d'éducation (1 à 5)")
    frequence_deplacement: int = Field(ge=1, le=3, description="Fréquence de déplacement (1 à 3)")
    annees_depuis_la_derniere_promotion: Log1p
    note_evaluation_precedente: int = Field(ge=1, le=4, description="Note d'évaluation précédente (1 à 4)")
    note_evaluation_actuelle: float = Field(ge=0.69, le=1.61, description="Note d'évaluation actuelle, déjà transformée en log1p")
    heure_supplementaires: Binaire
    augmentation_salaire_precedente: int = Field(ge=0, le=50, description="Augmentation de salaire précédente (%)")
    fe1_tranche_salariale: int = Field(ge=1, le=4, description="Tranche salariale (1 à 4)")
    fe2_satisfaction_globale: int = Field(ge=0, le=20, description="Score de satisfaction globale")
    fe3_tranche_age: int = Field(ge=1, le=5, description="Tranche d'âge (1 à 5)")
    statut_marital_divorce: Binaire
    statut_marital_marie: Binaire
    departement_consulting: Binaire
    departement_ressources_humaines: Binaire


class PredictionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    probabilite: float
    classe_predite: int