from flask import Flask, render_template, request, jsonify, redirect, url_for
import json, os

app = Flask(__name__)

# ── Données simulées (3 jurys) ─────────────────────────────────────────────
POLICES = {
    "POL-JURY-001": {
        "id": "POL-JURY-001",
        "client": "Dr. Ahmed Mansour",
        "initiales": "AM",
        "vehicule": "Mercedes Classe C",
        "immatriculation": "TUN-001-JR",
        "compagnie": "STAR Assurances Tunisie",
        "type": "Tous risques",
        "statut": "valide",
        "date_debut": "01/01/2025",
        "date_fin": "31/12/2025",
        "progress": 33,
        "jours_restants": 245,
        "montant": "1 200 TND",
        "couvertures": ["Responsabilité civile", "Vol & incendie", "Bris de glace", "Assistance 24h/24", "Dommages corporels"],
        "paye": True,
        "telephone": "+216 71 000 001",
        "email": "ahmed.mansour@example.tn"
    },
    "POL-JURY-002": {
        "id": "POL-JURY-002",
        "client": "Prof. Sonia Belhadj",
        "initiales": "SB",
        "vehicule": "Peugeot 308",
        "immatriculation": "TUN-002-JR",
        "compagnie": "STAR Assurances Tunisie",
        "type": "Tiers étendu",
        "statut": "expirée",
        "date_debut": "01/03/2024",
        "date_fin": "28/02/2025",
        "progress": 100,
        "jours_restants": 0,
        "montant": "650 TND",
        "couvertures": ["Responsabilité civile", "Vol & incendie", "Assistance 24h/24"],
        "paye": False,
        "telephone": "+216 71 000 002",
        "email": "sonia.belhadj@example.tn"
    },
    "POL-JURY-003": {
        "id": "POL-JURY-003",
        "client": "M. Karim Trabelsi",
        "initiales": "KT",
        "vehicule": "Renault Clio",
        "immatriculation": "TUN-003-JR",
        "compagnie": "STAR Assurances Tunisie",
        "type": "Responsabilité civile",
        "statut": "valide",
        "date_debut": "15/06/2025",
        "date_fin": "14/06/2026",
        "progress": 5,
        "jours_restants": 414,
        "montant": "380 TND",
        "couvertures": ["Responsabilité civile", "Assistance basique"],
        "paye": True,
        "telephone": "+216 71 000 003",
        "email": "karim.trabelsi@example.tn"
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan")
def scan():
    police_id = request.args.get("police", "")
    police = POLICES.get(police_id)
    if not police:
        return render_template("not_found.html", police_id=police_id)
    return render_template("scan.html", p=police)

@app.route("/client/<police_id>")
def client(police_id):
    police = POLICES.get(police_id)
    if not police:
        return redirect(url_for("index"))
    return render_template("client.html", p=police)

@app.route("/paiement/<police_id>")
def paiement(police_id):
    police = POLICES.get(police_id)
    if not police:
        return redirect(url_for("index"))
    return render_template("paiement.html", p=police)

@app.route("/api/payer/<police_id>", methods=["POST"])
def payer(police_id):
    if police_id in POLICES:
        POLICES[police_id]["paye"] = True
        POLICES[police_id]["statut"] = "valide"
        return jsonify({"success": True, "message": "Paiement confirmé !"})
    return jsonify({"success": False}), 404

@app.route("/admin")
def admin():
    return render_template("admin.html", polices=POLICES)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
