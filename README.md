# STAR Assurances - Système QR Code
## Projet PFE - Assurance Automobile avec QR Code

---

## Comment déployer en ligne (GRATUIT) - Render.com

### Étape 1 : Créer un compte GitHub
1. Va sur https://github.com et crée un compte gratuit

### Étape 2 : Mettre le projet sur GitHub
1. Crée un nouveau repository nommé `assurance-pfe`
2. Upload tous les fichiers de ce projet

### Étape 3 : Déployer sur Render
1. Va sur https://render.com et crée un compte gratuit
2. Clique **"New +"** → **"Web Service"**
3. Connecte ton GitHub et sélectionne `assurance-pfe`
4. Configure :
   - **Name**: assurance-pfe (ou ce que tu veux)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Clique **"Create Web Service"**
6. Attends 2-3 minutes → ton site sera en ligne sur une URL comme :
   `https://assurance-pfe.onrender.com`

---

## Les 3 QR codes pour les jurys

Une fois le site en ligne, tes 3 QR codes pointent vers :

| Jury | URL | Statut |
|------|-----|--------|
| Jury 1 - Dr. Ahmed Mansour | `TON-URL/scan?police=POL-JURY-001` | ✅ Valide |
| Jury 2 - Prof. Sonia Belhadj | `TON-URL/scan?police=POL-JURY-002` | ❌ Expirée |
| Jury 3 - M. Karim Trabelsi | `TON-URL/scan?police=POL-JURY-003` | ✅ Valide |

**Pour générer les QR codes imprimables :**
Va sur https://qr-code-generator.com et génère un QR pour chaque URL.

---

## Pages disponibles

| Page | URL | Description |
|------|-----|-------------|
| Accueil | `/` | Page principale |
| Scan (après QR) | `/scan?police=POL-JURY-001` | Ce que voit le jury en scannant |
| Espace client | `/client/POL-JURY-001` | Page du client |
| Paiement | `/paiement/POL-JURY-001` | Simulation de paiement |
| Administration | `/admin` | Dashboard admin |

---

## Tester localement (optionnel)
```
pip install flask gunicorn
python app.py
```
Puis ouvrir : http://localhost:5000
