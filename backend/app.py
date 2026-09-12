from flask import Flask, jsonify, request
app=Flask(__name__)
HERITAGE=[{"id":1,"name":"Sabarmati Ashram","category":"Heritage","city":"Ahmedabad"},{"id":2,"name":"Adalaj Stepwell","category":"Heritage","city":"Gujarat"},{"id":3,"name":"Bhadra Fort","category":"Heritage","city":"Ahmedabad"},{"id":4,"name":"Sidi Saiyyed Mosque","category":"Heritage","city":"Ahmedabad"},{"id":5,"name":"Somnath Temple","category":"Heritage","city":"Gujarat"}]
@app.get("/api/health")
def health(): return jsonify({"status":"ok","project":"Sanskriti Canvas"})
@app.get("/api/heritage")
def heritage(): return jsonify(HERITAGE)
@app.get("/api/search")
def search():
 q=request.args.get("q","").lower().strip(); return jsonify([x for x in HERITAGE if q in x["name"].lower() or q in x["category"].lower() or q in x["city"].lower()])
@app.post("/api/contributions")
def contributions():
 data=request.get_json(silent=True) or {}; data["status"]="pending"; return jsonify(data),201
if __name__=="__main__": app.run(debug=True)
