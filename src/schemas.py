from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field

Binaire = Annotated[int, Field(ge=0, le=1, description="1 = oui, 0 = non")]
Log1p = Annotated[
    float,
    Field(ge=0, le=4.5, description="Valeur déjà transformée en log1p"),
]


class PredictionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    genre: Binaire
    poste: float = Field(ge=0, le=0.3, description="Poste encodé en décimal (valeurs observées : 0.035 à 0.222)")
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