from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.db.database import Base

class Dataset(Base):
    __tablename__ = "dataset"

    id = Column(Integer, primary_key=True)
    genre = Column(Integer, nullable=False)
    poste = Column(Float, nullable=False)
    nombre_experiences_precedentes = Column(Float, nullable=False)
    annee_experience_totale = Column(Float, nullable=False)
    annees_dans_l_entreprise = Column(Float, nullable=False)
    annees_dans_le_poste_actuel = Column(Integer, nullable=False)
    a_quitte_l_entreprise = Column(Integer, nullable=False)
    distance_domicile_travail = Column(Integer, nullable=False)
    niveau_education = Column(Integer, nullable=False)
    frequence_deplacement = Column(Integer, nullable=False)
    annees_depuis_la_derniere_promotion = Column(Float, nullable=False)
    note_evaluation_precedente = Column(Integer, nullable=False)
    note_evaluation_actuelle = Column(Float, nullable=False)
    heure_supplementaires = Column(Integer, nullable=False)
    augmentation_salaire_precedente = Column(Integer, nullable=False)
    fe1_tranche_salariale = Column(Integer, nullable=False)
    fe2_satisfaction_globale = Column(Integer, nullable=False)
    fe3_tranche_age = Column(Integer, nullable=False)
    statut_marital_divorce = Column(Integer, nullable=False)
    statut_marital_marie = Column(Integer, nullable=False)
    departement_consulting = Column(Integer, nullable=False)
    departement_ressources_humaines = Column(Integer, nullable=False)


class Input(Base):
    __tablename__ = "inputs"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    genre = Column(Integer, nullable=False)
    poste = Column(Float, nullable=False)
    nombre_experiences_precedentes = Column(Float, nullable=False)
    annee_experience_totale = Column(Float, nullable=False)
    annees_dans_l_entreprise = Column(Float, nullable=False)
    annees_dans_le_poste_actuel = Column(Integer, nullable=False)
    distance_domicile_travail = Column(Integer, nullable=False)
    niveau_education = Column(Integer, nullable=False)
    frequence_deplacement = Column(Integer, nullable=False)
    annees_depuis_la_derniere_promotion = Column(Float, nullable=False)
    note_evaluation_precedente = Column(Integer, nullable=False)
    note_evaluation_actuelle = Column(Float, nullable=False)
    heure_supplementaires = Column(Integer, nullable=False)
    augmentation_salaire_precedente = Column(Integer, nullable=False)
    fe1_tranche_salariale = Column(Integer, nullable=False)
    fe2_satisfaction_globale = Column(Integer, nullable=False)
    fe3_tranche_age = Column(Integer, nullable=False)
    statut_marital_divorce = Column(Integer, nullable=False)
    statut_marital_marie = Column(Integer, nullable=False)
    departement_consulting = Column(Integer, nullable=False)
    departement_ressources_humaines = Column(Integer, nullable=False)

    prediction = relationship("Prediction", back_populates="input", uselist=False)


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    input_id = Column(Integer, ForeignKey("inputs.id"), unique=True, nullable=False)
    classe_predite = Column(Integer, nullable=False)
    probabilite = Column(Float, nullable=False)

    input = relationship("Input", back_populates="prediction")



        
