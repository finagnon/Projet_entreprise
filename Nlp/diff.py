#fonction avi negatif
def negatif_avis(data):
    data = data[data["Type"] == "Negatif"]
    return data

#fonction avi positif
def positif_avis(data):
    data = data[data["Type"] == "Positif"]
    return data


#designation des labels
def assign_label(comment):
        

        comment = comment.lower()
        if any(word in comment for word in ['formation', 'demande']):
            return 'Problème emploi et formation'
        elif any(word in comment for word in ['conseiller', 'accueil', 'personnel','téléphone','tlphone','telephone']):
                return 'Problème de compétence'
        elif any(word in comment for word in ['service', 'recevoir', 'dossier', 'aide', 'aider', 'rendezvous', 'rpondre']):
            return 'Problème gestion client'
        elif any(word in comment for word  in ['radiation','radier']):
            return 'Problème de radiation'
        elif any( word in comment for word in ['indemnité','indemnisation', 'indemniser','indemnisé','complément', 'allocation','alocation']):
            return "Problème d'indemnisation et allocation"
        elif any( word in comment for word in ['trop perçu', 'trop percu']):
            return "Problème de trop perçu"
        
        elif any( word in comment for word in ['sous traitant', 'sous-traitant']):
            return "Problème de sous-traitant"
        
        elif any( word in comment for word in ['actualiser','actualisation','mise à jour', 'mis a jour', 'mise à jours']):
            return "Problème d'indemnisation"
        elif any( word in comment for word in ['addresse','adress', 'address', 'adresse']):
            return "Problème d'addresse"
        
        
        else:
                return 'Colère ou problème spécifique'
