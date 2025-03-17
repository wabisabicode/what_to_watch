from flask import jsonify

from . import app
from .models import Opinion


@app.route('/api/opinions/<int:id>/', methods=['GET'])
def get_opinion(id):
    opinion = Opinion.query.get_or_404(id)
    return jsonify({'opinion': opinion}), 200


def opinion_to_dict(opinion):
    return dict(
        id=opinion.id,
        title=opinion.title,
        text=opinion.text,
        source=opinion.source,
        timestamp=opinion.timestamp,
        added_by=opinion.added_by
    )
