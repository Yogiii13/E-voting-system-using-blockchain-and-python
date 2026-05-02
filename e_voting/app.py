from flask import Flask, render_template, request, jsonify
from e_voting.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/candidates/<constituency>')
def get_candidates(constituency):
    candidates = {
        'A': {'1': 'Candidate A', '2': 'Candidate B', '3': 'Candidate C'},
        'B': {'1': 'Candidate X', '2': 'Candidate Y', '3': 'Candidate Z'},
        'C': {'1': 'Candidate D', '2': 'Candidate E', '3': 'Candidate F'},
    }
    return jsonify(candidates.get(constituency.upper(), {}))

@app.route('/api/cast-vote', methods=['POST'])
def cast_vote():
    data = request.json
    voter_id = data.get('voter_id', '').strip()
    constituency = voter_id[:1].upper() if voter_id else ''
    candidate_id = data.get('candidate_id', '')

    if not voter_id:
        return jsonify({'success': False, 'error': 'Voter ID is required'}), 400
    
    if voter_id in blockchain.voter_ids:
        return jsonify({'success': False, 'error': 'This voter has already cast a vote'}), 400
    
    if constituency not in ['A', 'B', 'C']:
        return jsonify({'success': False, 'error': 'Invalid voter ID format'}), 400
    
    if not candidate_id:
        return jsonify({'success': False, 'error': 'Candidate must be selected'}), 400

    vote_data = {'constituency': constituency, 'candidate_id': candidate_id}
    blockchain.new_vote(voter_id, vote_data)
    blockchain.increment_candidate_votes(constituency, candidate_id)
    blockchain.voter_ids.add(voter_id)

    return jsonify({
        'success': True,
        'message': 'Vote cast successfully'
    })

@app.route('/api/blockchain')
def get_blockchain():
    return jsonify(blockchain.view_blockchain())

@app.route('/api/results')
def get_results():
    results = {}
    for constituency, votes in blockchain.candidates.items():
        results[constituency] = []
        for candidate_id, info in votes.items():
            results[constituency].append({
                'name': info['name'],
                'id': candidate_id,
                'votes': info['votes']
            })
    return jsonify(results)

@app.route('/api/commission-view', methods=['POST'])
def commission_view():
    data = request.json
    login_id = data.get('login_id', '')
    constituency = data.get('constituency', '').upper()
    
    result = blockchain.election_commission_view(login_id, constituency)
    
    if 'Access denied' in result:
        return jsonify({'success': False, 'error': result}), 403
    
    return jsonify({'success': True, 'data': result})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
